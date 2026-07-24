"""
Poverty Predictor Model - Logistic Regression (TDHS 2022)

This module loads a trained logistic-regression model (intercept + coefficients)
from `models/model_coefficients.json`, which is produced by `train_model.py`
using a real training dataset placed at `data/training_data.csv`.

If that file has not been generated yet (i.e. no training dataset has been
supplied), a documented FALLBACK coefficient set is used instead so the app
keeps working. The fallback is intentionally calibrated so that BOTH "poor"
and "non-poor" outcomes are reachable (unlike the previous hardcoded version,
which used only negative coefficients and therefore could never classify a
household as "poor"). Once a real dataset is supplied and `train_model.py`
is run, the learned coefficients automatically replace the fallback.
"""

import json
import os
import numpy as np
from typing import Dict, List


COEFFICIENTS_PATH = os.path.join(os.path.dirname(__file__), 'model_coefficients.json')

# Feature order used everywhere (model input, importance ranking, etc.)
FEATURE_LABELS = {
    'householdSize': 'Household Size',
    'residence': 'Type of Residence (Urban)',
    'waterSource': 'Water Source (Safe)',
    'toiletType': 'Toilet Facility (Improved)',
    'hasElectricity': 'Electricity Access',
    'hasMobilePhone': 'Mobile Phone Ownership',
    'hasRadio': 'Radio Ownership',
    'hasTelevision': 'Television Ownership',
    'hasRefrigerator': 'Refrigerator Ownership',
    'hasBicycle': 'Bicycle Ownership',
    'hasMotorcycle': 'Motorcycle Ownership',
    'hasCar': 'Car Ownership',
}

# FALLBACK coefficients — used only until a real dataset is trained on.
# Baseline (intercept) represents a household with none of the protective
# factors below; each protective factor (safe water, electricity, assets...)
# pulls the poverty probability DOWN. Household size pulls it slightly UP,
# reflecting that larger households are, on average, more resource-strained.
# This keeps predictions balanced instead of collapsing to a single class.
FALLBACK_INTERCEPT = 1.7
FALLBACK_COEFFICIENTS = {
    'householdSize': 0.12,
    'residence': -0.55,       # Urban = 1 -> lowers poverty risk
    'waterSource': -0.75,     # Safe water = 1 -> lowers poverty risk
    'toiletType': -0.65,      # Improved toilet = 1 -> lowers poverty risk
    'hasElectricity': -0.85,
    'hasMobilePhone': -0.45,
    'hasRadio': -0.25,
    'hasTelevision': -0.55,
    'hasRefrigerator': -0.70,
    'hasBicycle': -0.20,
    'hasMotorcycle': -0.45,
    'hasCar': -0.90,
}


def _load_coefficients():
    """Load trained coefficients if available, else use the documented fallback."""
    if os.path.exists(COEFFICIENTS_PATH):
        try:
            with open(COEFFICIENTS_PATH, 'r') as f:
                data = json.load(f)
            return data['intercept'], data['coefficients'], data.get('trained', True)
        except Exception:
            pass
    return FALLBACK_INTERCEPT, dict(FALLBACK_COEFFICIENTS), False


class PovertyPredictor:
    """
    Logistic Regression model for household poverty prediction, trained on
    (or falling back to a balanced approximation of) the TDHS 2022 dataset.
    """

    def __init__(self):
        self.intercept, self.coefficients, self.is_trained = _load_coefficients()
        self.feature_labels = FEATURE_LABELS

    def reload(self):
        """Re-read coefficients from disk (used after retraining)."""
        self.intercept, self.coefficients, self.is_trained = _load_coefficients()

    def _sigmoid(self, z: float) -> float:
        z = np.clip(z, -35, 35)
        return 1 / (1 + np.exp(-z))

    def predict(self, features: Dict[str, float]) -> Dict:
        """
        Predict poverty probability and classification.

        Returns a dict with:
            - probability: float (0-1), probability the household is "poor"
            - classification: 'poor' or 'non-poor' (0.5 threshold)
            - tier: finer-grained label ('very_poor', 'poor', 'non_poor', 'well_off')
            - score: percentage string for display
            - featureImportance: top 8 contributing factors
        """
        z = self.intercept
        for feature_name, coefficient in self.coefficients.items():
            if feature_name in features:
                z += coefficient * features[feature_name]

        probability = self._sigmoid(z)
        classification = 'poor' if probability >= 0.5 else 'non-poor'
        tier = self._tier_for(probability)
        score = f"{probability * 100:.1f}%"
        feature_importance = self._calculate_feature_importance(features)

        return {
            'probability': round(float(probability), 4),
            'classification': classification,
            'tier': tier,
            'score': score,
            'featureImportance': feature_importance,
        }

    @staticmethod
    def _tier_for(probability: float) -> str:
        """Four-tier classification for the results table."""
        if probability >= 0.75:
            return 'very_poor'
        elif probability >= 0.5:
            return 'poor'
        elif probability >= 0.25:
            return 'non_poor'
        else:
            return 'well_off'

    def _calculate_feature_importance(self, features: Dict[str, float]) -> List[Dict]:
        """Top 8 factors by absolute contribution to the linear score."""
        contributions = []
        for feature_name, coefficient in self.coefficients.items():
            if feature_name in features:
                contribution = abs(coefficient * features[feature_name])
                contributions.append({
                    'factor': feature_name,
                    'label': self.feature_labels.get(feature_name, feature_name),
                    'contribution': round(contribution, 4),
                    'coefficient': round(coefficient, 4),
                    'value': features[feature_name],
                })
        contributions.sort(key=lambda x: x['contribution'], reverse=True)
        return contributions[:8]

    def get_model_info(self) -> Dict:
        return {
            'name': 'Logistic Regression',
            'dataset': 'TDHS 2022' if self.is_trained else 'TDHS 2022 (fallback coefficients — awaiting training data)',
            'features': len(self.coefficients),
            'intercept': self.intercept,
            'coefficients': self.coefficients,
            'trained': self.is_trained,
        }


# Initialize global model instance
model = PovertyPredictor()


def predict_poverty(
    household_size: int,
    residence: int,
    water_source: int,
    toilet_type: int,
    has_electricity: bool,
    has_mobile_phone: bool,
    has_radio: bool,
    has_television: bool,
    has_refrigerator: bool,
    has_bicycle: bool,
    has_motorcycle: bool,
    has_car: bool,
) -> Dict:
    """Convenience function for poverty prediction."""
    features = {
        'householdSize': household_size,
        'residence': residence,
        'waterSource': water_source,
        'toiletType': toilet_type,
        'hasElectricity': int(has_electricity),
        'hasMobilePhone': int(has_mobile_phone),
        'hasRadio': int(has_radio),
        'hasTelevision': int(has_television),
        'hasRefrigerator': int(has_refrigerator),
        'hasBicycle': int(has_bicycle),
        'hasMotorcycle': int(has_motorcycle),
        'hasCar': int(has_car),
    }
    return model.predict(features)
