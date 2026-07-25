#!/usr/bin/env python3
"""
Generate a SAMPLE / SYNTHETIC training dataset.

IMPORTANT: This is NOT the real TDHS 2022 dataset. It is a placeholder,
generated from a simple, documented statistical rule, so that the app has a
working, balanced model (i.e. one that can predict BOTH "poor" and
"non-poor") out of the box. Replace data/training_data.csv with a real TDHS
extract and re-run train_model.py as soon as it is available — the model
will automatically retrain on the real data and overwrite the results
produced from this sample.

Run:  python data/generate_sample_data.py
"""

import os
import numpy as np
import pandas as pd

RNG = np.random.default_rng(42)
N = 4000


def generate():
    residence = RNG.binomial(1, 0.4, N)  # 40% urban
    household_size = np.clip(RNG.poisson(5, N) + 1, 1, 20)

    # Latent "wealth index" — urban households and smaller households tend
    # to score higher on average, with random noise layered on top.
    wealth = (
        1.4 * residence
        - 0.08 * household_size
        + RNG.normal(0, 1.0, N)
    )

    def bernoulli_from_wealth(base, weight):
        p = 1 / (1 + np.exp(-(base + weight * wealth)))
        return RNG.binomial(1, p)

    water_source = bernoulli_from_wealth(-0.3, 0.9)
    toilet_type = bernoulli_from_wealth(-0.4, 0.85)
    has_electricity = bernoulli_from_wealth(-0.5, 1.0)
    has_mobile_phone = bernoulli_from_wealth(0.3, 0.7)
    has_radio = bernoulli_from_wealth(-0.2, 0.5)
    has_television = bernoulli_from_wealth(-0.6, 0.9)
    has_refrigerator = bernoulli_from_wealth(-0.9, 1.0)
    has_bicycle = bernoulli_from_wealth(-0.1, 0.4)
    has_motorcycle = bernoulli_from_wealth(-0.5, 0.7)
    has_car = bernoulli_from_wealth(-1.4, 1.1)

    # Ground-truth poverty label driven by the same latent wealth index plus
    # its own noise term, so it is correlated with but not identical to the
    # individual assets above (as in real survey data).
    poverty_logit = -1.1 * wealth + RNG.normal(0, 0.6, N)
    is_poor = (poverty_logit > 0).astype(int)
    classification = np.where(is_poor == 1, 'poor', 'non-poor')

    df = pd.DataFrame({
        'householdSize': household_size,
        'residence': residence,
        'waterSource': water_source,
        'toiletType': toilet_type,
        'hasElectricity': has_electricity,
        'hasMobilePhone': has_mobile_phone,
        'hasRadio': has_radio,
        'hasTelevision': has_television,
        'hasRefrigerator': has_refrigerator,
        'hasBicycle': has_bicycle,
        'hasMotorcycle': has_motorcycle,
        'hasCar': has_car,
        'classification': classification,
    })
    return df


if __name__ == '__main__':
    df = generate()
    out_path = os.path.join(os.path.dirname(__file__), 'training_data.csv')
    df.to_csv(out_path, index=False)
    print(f"Wrote {len(df)} sample rows to {out_path}")
    print(df['classification'].value_counts())
