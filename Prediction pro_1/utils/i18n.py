"""
Internationalization (i18n) module - Swahili and English translations
"""

TRANSLATIONS = {
    'en': {
        # Header
        'app_title': 'HOUSEHOLD POVERTY PREDICTOR',
        'app_subtitle': 'Tanzania - TDHS 2022 Analysis',

        # Login / Register
        'login_welcome': 'Welcome to Household Poverty Predictor',
        'login_tab': 'Login',
        'register_tab': 'Register',
        'username_label': 'Username (First Name)',
        'password_label': 'Password (8 digits)',
        'login_button': 'Login',
        'register_button': 'Register',
        'login_help': 'Already have an account? Log in below.',
        'register_help': 'New user? Create an account — username is your first name (letters only), password is exactly 8 digits.',
        'logout_button': 'Logout',
        'logged_in_as': 'Logged in as',
        'error_invalid_username': 'Username must be your first name (letters only, no spaces or numbers).',
        'error_invalid_password': 'Password must be exactly 8 digits.',
        'error_username_taken': 'That username is already registered. Please log in instead.',
        'error_user_not_found': 'No account found with that username. Please register first.',
        'error_wrong_password': 'Incorrect password. Please try again.',
        'error_missing_fields': 'Please enter both username and password.',
        'success_registration': 'Registration successful! You can now log in.',
        'success_login': 'Login successful!',
        'generate_password_button': '🎲 Suggest Strong Password',
        'password_strong': 'Strong password',
        'password_weak': 'Weak password — avoid simple patterns like 12345678 or 11111111',
        
        # Navigation
        'tab_predictor': 'Predictor',
        'tab_dashboard': 'Research Dashboard',
        
        # Form labels
        'form_title': 'Household Characteristics',
        'form_description': 'Enter the details of the household you want to predict',
        
        'region': 'Region (hv024)',
        'region_help': 'Select the region where the household is located',
        
        'household_size': 'Number of Household Members (hv009)',
        'household_size_help': 'Enter the actual number of people living in the household (1-30)',
        
        'residence_type': 'Type of Residence (hv025)',
        'residence_urban': 'Urban',
        'residence_rural': 'Rural',
        
        'water_source': 'Water Source (hv201)',
        'water_piped': 'Piped into dwelling',
        'water_public': 'Public tap/standpipe',
        'water_well': 'Well',
        'water_surface': 'Surface water',
        'water_other': 'Other',
        
        'toilet_type': 'Toilet Facility (hv205)',
        'toilet_flush': 'Flush toilet',
        'toilet_pit': 'Pit latrine',
        'toilet_bucket': 'Bucket toilet',
        'toilet_none': 'No toilet',
        'toilet_other': 'Other',
        
        'assets_title': 'Asset & Service Ownership',
        'electricity': 'Electricity',
        'mobile_phone': 'Mobile Phone',
        'radio': 'Radio',
        'television': 'Television',
        'refrigerator': 'Refrigerator',
        'bicycle': 'Bicycle',
        'motorcycle': 'Motorcycle',
        'car': 'Car',
        
        # Buttons
        'predict_button': 'Predict',
        'export_csv': 'Download CSV',
        'export_json': 'Download JSON',
        'clear_form': 'Clear Form',
        'next_button': 'Next',
        'back_button': 'Back',

        # Wizard step labels
        'step_location': 'Location',
        'step_household': 'Household',
        'step_water': 'Water & Sanitation',
        'step_assets': 'Assets',
        
        # Results
        'results_title': 'Prediction Results',
        'no_prediction': 'No prediction yet',
        'no_prediction_help': 'Fill in the form and click Predict to see results',
        
        'poverty_probability': 'Poverty Probability',
        'classification': 'Classification',
        'poor': 'Poor',
        'non_poor': 'Non-poor',
        'prediction_accuracy': 'Prediction Accuracy',
        'accuracy_unavailable': 'N/A (train the model first)',

        # Four-tier classification labels used in the results table
        'tier_very_poor': 'Very Poor',
        'tier_poor': 'Poor',
        'tier_non_poor': 'Non Poor',
        'tier_well_off': 'Rich',

        'results_table_title': 'Prediction Summary',
        'poverty_status': 'Poverty Status',
        'probability_distribution': 'Probability Distribution',
        'probability_mark': 'Probability Mark',
        'result_status': 'Status',
        'result_probability': 'Poverty Probability',

        'feature_importance': 'Contributing Factors (Top 8)',
        'factor': 'Factor',
        'contribution': 'Contribution',
        
        'recommendations_title': 'Actionable Recommendations',
        'priority_high': 'High Priority',
        'priority_medium': 'Medium Priority',
        'priority_low': 'Low Priority',
        
        # Dashboard
        'dashboard_title': 'Research Dashboard',
        'dashboard_description': 'View and analyze all prediction results',
        
        'total_predictions': 'Total Predictions',
        'poor_count': 'Poor',
        'non_poor_count': 'Non-poor',
        'poor_percentage': 'Poor %',
        'non_poor_percentage': 'Non-poor %',
        'poverty_percentage_table': 'Poverty Percentage Breakdown',
        
        'analytics_title': 'Analytics & Insights',
        'poverty_distribution': 'Poverty Distribution',
        'predictions_by_residence': 'Predictions by Residence Type',
        'poverty_rate_by_residence': 'Poverty Rate by Residence',
        'poverty_trend': 'Poverty Trend (Last 10 Days)',
        'predictions_by_region': 'Predictions by Region',
        'poverty_rate_by_region': 'Poverty Rate by Region',
        
        'filters_title': 'Filters',
        'filter_region': 'Region',
        'filter_residence': 'Residence Type',
        'filter_poverty_level': 'Poverty Level',
        'filter_date_range': 'Date Range',
        'filter_all': 'All',
        'apply_filters': 'Apply Filters',
        'reset_filters': 'Reset Filters',
        
        'predictions_table': 'All Predictions',
        'date': 'Date',
        'region_col': 'Region',
        'household_size_col': 'Household Size',
        'residence_col': 'Residence',
        'poverty_level': 'Poverty Level',
        'probability_col': 'Probability',
        
        # Settings
        'settings_title': 'Settings',
        'language': 'Language',
        'theme': 'Theme',
        'theme_light': 'Light',
        'theme_dark': 'Dark',
        
        # Messages
        'prediction_success': 'Prediction completed successfully',
        'prediction_error': 'Error during prediction',
        'export_success': 'Data exported successfully',
        'export_error': 'Error exporting data',
        
        # Footer
        'footer_text': 'Household Poverty Status Predictor | TDHS 2022 | Tanzania',
        'footer_model': 'Model: Logistic Regression | Dataset: TDHS 2022',
    },
    
    'sw': {
        # Header
        'app_title': 'UTABIRI WA UMASKINI KATIKA KAYA',
        'app_subtitle': 'Tanzania - Uchambuzi wa TDHS 2022',

        # Login / Register
        'login_welcome': 'Karibu kwenye Mfumo wa Kutabiri Umaskini wa Kaya',
        'login_tab': 'Ingia',
        'register_tab': 'Jisajili',
        'username_label': 'Jina la Mtumiaji (Jina la Kwanza)',
        'password_label': 'Nywila (Namba 8)',
        'login_button': 'Ingia',
        'register_button': 'Jisajili',
        'login_help': 'Una akaunti tayari? Ingia hapa chini.',
        'register_help': 'Mtumiaji mpya? Fungua akaunti — jina la mtumiaji ni jina lako la kwanza (herufi tu), nywila ni namba 8 hasa.',
        'logout_button': 'Toka',
        'logged_in_as': 'Umeingia kama',
        'error_invalid_username': 'Jina la mtumiaji lazima liwe jina lako la kwanza (herufi tu, bila nafasi wala namba).',
        'error_invalid_password': 'Nywila lazima iwe namba 8 hasa.',
        'error_username_taken': 'Jina hilo la mtumiaji tayari limesajiliwa. Tafadhali ingia badala yake.',
        'error_user_not_found': 'Hakuna akaunti yenye jina hilo la mtumiaji. Tafadhali jisajili kwanza.',
        'error_wrong_password': 'Nywila si sahihi. Tafadhali jaribu tena.',
        'error_missing_fields': 'Tafadhali jaza jina la mtumiaji na nywila.',
        'success_registration': 'Usajili umefanikiwa! Sasa unaweza kuingia.',
        'success_login': 'Umeingia kikamilifu!',
        'generate_password_button': '🎲 Pendekeza Nywila Imara',
        'password_strong': 'Nywila imara',
        'password_weak': 'Nywila dhaifu — epuka mfululizo rahisi kama 12345678 au 11111111',
        
        # Navigation
        'tab_predictor': 'Kutabiri',
        'tab_dashboard': 'Dashibodi ya Utafiti',
        
        # Form labels
        'form_title': 'Sifa za Kaya',
        'form_description': 'Ingiza maelezo ya kaya unayotaka kutabiri',
        
        'region': 'Mkoa (hv024)',
        'region_help': 'Chagua mkoa ambapo kaya iko',
        
        'household_size': 'Idadi ya Wanachama wa Kaya (hv009)',
        'household_size_help': 'Andika namba halisi ya watu wanaoishi katika kaya (1-30)',
        
        'residence_type': 'Aina ya Makazi (hv025)',
        'residence_urban': 'Mjini',
        'residence_rural': 'Vijijini',
        
        'water_source': 'Chanzo cha Maji (hv201)',
        'water_piped': 'Maji yanayoingizwa nyumbani',
        'water_public': 'Bomba la umma/Kituo cha maji',
        'water_well': 'Kisima',
        'water_surface': 'Maji ya uso',
        'water_other': 'Nyingine',
        
        'toilet_type': 'Kiwanja cha Taka (hv205)',
        'toilet_flush': 'Choo cha kusafisha',
        'toilet_pit': 'Choo cha shimo',
        'toilet_bucket': 'Choo cha ndoo',
        'toilet_none': 'Hakuna choo',
        'toilet_other': 'Nyingine',
        
        'assets_title': 'Umiliki wa Mali na Huduma',
        'electricity': 'Umeme',
        'mobile_phone': 'Simu ya Mkononi',
        'radio': 'Redio',
        'television': 'Televisheni',
        'refrigerator': 'Jokofu',
        'bicycle': 'Baiskeli',
        'motorcycle': 'Pikipiki',
        'car': 'Gari',
        
        # Buttons
        'predict_button': 'Tabiri',
        'export_csv': 'Pakua CSV',
        'export_json': 'Pakua JSON',
        'clear_form': 'Futa Fomu',
        'next_button': 'Endelea',
        'back_button': 'Rudi Nyuma',

        # Wizard step labels
        'step_location': 'Mahali',
        'step_household': 'Kaya',
        'step_water': 'Maji na Usafi',
        'step_assets': 'Vifaa',
        
        # Results
        'results_title': 'Matokeo ya Utabiri',
        'no_prediction': 'Hakuna utabiri bado',
        'no_prediction_help': 'Jaza fomu na ubofye Tabiri kuona matokeo',
        
        'poverty_probability': 'Uwezekano wa Umaskini',
        'classification': 'Uainishaji',
        'poor': 'Maskini',
        'non_poor': 'Sio maskini',
        'prediction_accuracy': 'Usahihi wa Utabiri',
        'accuracy_unavailable': 'Haipatikani (fanya training kwanza)',

        # Madaraja manne ya uainishaji yanayotumika kwenye jedwali la matokeo
        'tier_very_poor': 'Maskini Sana',
        'tier_poor': 'Maskini',
        'tier_non_poor': 'Sio Maskini',
        'tier_well_off': 'Tajiri',

        'results_table_title': 'Muhtasari wa Utabiri',
        'poverty_status': 'Hali ya Umaskini',
        'probability_distribution': 'Mgawanyo wa Uwezekano',
        'probability_mark': 'Alama ya Uwezekano',
        'result_status': 'Hali',
        'result_probability': 'Uwezekano wa Umaskini',

        'feature_importance': 'Mambo Yanayochangia (Nane Makuu)',
        'factor': 'Jambo',
        'contribution': 'Mchango',
        
        'recommendations_title': 'Mapendekezo ya Hatua',
        'priority_high': 'Kipaumbele Cha Juu',
        'priority_medium': 'Kipaumbele Cha Kati',
        'priority_low': 'Kipaumbele Cha Chini',
        
        # Dashboard
        'dashboard_title': 'Dashibodi ya Utafiti',
        'dashboard_description': 'Tazama na uchambuzi matokeo yote ya utabiri',
        
        'total_predictions': 'Jumla ya Utabiri',
        'poor_count': 'Maskini',
        'non_poor_count': 'Sio maskini',
        'poor_percentage': 'Asilimia ya Maskini',
        'non_poor_percentage': 'Asilimia ya Wasio Maskini',
        'poverty_percentage_table': 'Mgawanyo wa Asilimia ya Umaskini',
        
        'analytics_title': 'Uchambuzi na Maarifa',
        'poverty_distribution': 'Usambazaji wa Umaskini',
        'predictions_by_residence': 'Utabiri Kulingana na Aina ya Makazi',
        'poverty_rate_by_residence': 'Kiwango cha Umaskini Kulingana na Makazi',
        'poverty_trend': 'Mwelekeo wa Umaskini (Siku 10 Zilizopita)',
        'predictions_by_region': 'Utabiri Kulingana na Mkoa',
        'poverty_rate_by_region': 'Kiwango cha Umaskini Kulingana na Mkoa',
        
        'filters_title': 'Vichujio',
        'filter_region': 'Mkoa',
        'filter_residence': 'Aina ya Makazi',
        'filter_poverty_level': 'Kiwango cha Umaskini',
        'filter_date_range': 'Eneo la Tarehe',
        'filter_all': 'Zote',
        'apply_filters': 'Tumia Vichujio',
        'reset_filters': 'Tengeneza Upya Vichujio',
        
        'predictions_table': 'Utabiri Wote',
        'date': 'Tarehe',
        'region_col': 'Mkoa',
        'household_size_col': 'Idadi ya Kaya',
        'residence_col': 'Makazi',
        'poverty_level': 'Kiwango cha Umaskini',
        'probability_col': 'Uwezekano',
        
        # Settings
        'settings_title': 'Mipangilio',
        'language': 'Lugha',
        'theme': 'Mandhari',
        'theme_light': 'Mwanga',
        'theme_dark': 'Giza',
        
        # Messages
        'prediction_success': 'Utabiri umekamilika kwa mafanikio',
        'prediction_error': 'Hitilafu wakati wa utabiri',
        'export_success': 'Data iliyohamishwa kwa mafanikio',
        'export_error': 'Hitilafu wakati wa kuhamisha data',
        
        # Footer
        'footer_text': 'Mbinu ya Kutabiri Hali ya Umaskini wa Kaya | TDHS 2022 | Tanzania',
        'footer_model': 'Muundo: Logistic Regression | Seti ya Data: TDHS 2022',
    }
}

# Tanzania Regions and Districts
TANZANIA_REGIONS = {
    'en': {
        'Arusha': ['Arusha', 'Arumeru', 'Karatu', 'Ngorongoro', 'Monduli'],
        'Dar es Salaam': ['Kinondoni', 'Ilala', 'Temeke', 'Ubungo'],
        'Dodoma': ['Dodoma Urban', 'Dodoma Rural', 'Beeswax', 'Iringa', 'Iramba'],
        'Geita': ['Geita', 'Nzega', 'Kahama', 'Bukoba'],
        'Iringa': ['Iringa Urban', 'Iringa Rural', 'Mufindi', 'Njombe'],
        'Kagera': ['Bukoba', 'Muleba', 'Karagwe', 'Biharamulo'],
        'Katavi': ['Mpanda', 'Sumbawanga'],
        'Kigoma': ['Kigoma Urban', 'Kigoma Rural', 'Kasulu', 'Kibondo'],
        'Kilimanjaro': ['Moshi', 'Mwanga', 'Same', 'Rombo', 'Hai'],
        'Lindi': ['Lindi Urban', 'Lindi Rural', 'Mtwara', 'Kilwa'],
        'Manyara': ['Babati', 'Hanang', 'Iramba', 'Kiteto'],
        'Mbeya': ['Mbeya Urban', 'Mbeya Rural', 'Kyela', 'Rungwe'],
        'Morogoro': ['Morogoro Urban', 'Morogoro Rural', 'Mvomero', 'Ulanga'],
        'Mtwara': ['Mtwara Urban', 'Mtwara Rural', 'Newala'],
        'Mwanza': ['Mwanza Urban', 'Mwanza Rural', 'Nyamagana', 'Sengerema'],
        'Njombe': ['Njombe Urban', 'Njombe Rural', 'Makambako'],
        'Pemba': ['Pemba North', 'Pemba South'],
        'Pwani': ['Bagamoyo', 'Chalinze', 'Pangani'],
        'Rukwa': ['Sumbawanga', 'Nkansi'],
        'Ruvuma': ['Songea', 'Mbinga', 'Tunduru'],
        'Simiyu': ['Bariadi', 'Busega', 'Itilima'],
        'Singida': ['Singida Urban', 'Singida Rural', 'Iramba'],
        'Tabora': ['Tabora Urban', 'Tabora Rural', 'Nzega', 'Uyui'],
        'Tanga': ['Tanga Urban', 'Tanga Rural', 'Bumbuli', 'Korogwe', 'Lushoto'],
        'Unguja': ['Unguja North', 'Unguja South'],
    },
    'sw': {
        'Arusha': ['Arusha', 'Arumeru', 'Karatu', 'Ngorongoro', 'Monduli'],
        'Dar es Salaam': ['Kinondoni', 'Ilala', 'Temeke', 'Ubungo'],
        'Dodoma': ['Dodoma Jiji', 'Dodoma Viji', 'Beeswax', 'Iringa', 'Iramba'],
        'Geita': ['Geita', 'Nzega', 'Kahama', 'Bukoba'],
        'Iringa': ['Iringa Jiji', 'Iringa Viji', 'Mufindi', 'Njombe'],
        'Kagera': ['Bukoba', 'Muleba', 'Karagwe', 'Biharamulo'],
        'Katavi': ['Mpanda', 'Sumbawanga'],
        'Kigoma': ['Kigoma Jiji', 'Kigoma Viji', 'Kasulu', 'Kibondo'],
        'Kilimanjaro': ['Moshi', 'Mwanga', 'Same', 'Rombo', 'Hai'],
        'Lindi': ['Lindi Jiji', 'Lindi Viji', 'Mtwara', 'Kilwa'],
        'Manyara': ['Babati', 'Hanang', 'Iramba', 'Kiteto'],
        'Mbeya': ['Mbeya Jiji', 'Mbeya Viji', 'Kyela', 'Rungwe'],
        'Morogoro': ['Morogoro Jiji', 'Morogoro Viji', 'Mvomero', 'Ulanga'],
        'Mtwara': ['Mtwara Jiji', 'Mtwara Viji', 'Newala'],
        'Mwanza': ['Mwanza Jiji', 'Mwanza Viji', 'Nyamagana', 'Sengerema'],
        'Njombe': ['Njombe Jiji', 'Njombe Viji', 'Makambako'],
        'Pemba': ['Pemba Kaskazini', 'Pemba Kusini'],
        'Pwani': ['Bagamoyo', 'Chalinze', 'Pangani'],
        'Rukwa': ['Sumbawanga', 'Nkansi'],
        'Ruvuma': ['Songea', 'Mbinga', 'Tunduru'],
        'Simiyu': ['Bariadi', 'Busega', 'Itilima'],
        'Singida': ['Singida Jiji', 'Singida Viji', 'Iramba'],
        'Tabora': ['Tabora Jiji', 'Tabora Viji', 'Nzega', 'Uyui'],
        'Tanga': ['Tanga Jiji', 'Tanga Viji', 'Bumbuli', 'Korogwe', 'Lushoto'],
        'Unguja': ['Unguja Kaskazini', 'Unguja Kusini'],
    }
}


def get_text(key: str, language: str = 'en') -> str:
    """
    Get translated text
    
    Args:
        key: Translation key
        language: Language code ('en' or 'sw')
    
    Returns:
        Translated text or key if not found
    """
    if language not in TRANSLATIONS:
        language = 'en'
    
    return TRANSLATIONS[language].get(key, key)


def get_all_translations(language: str = 'en') -> dict:
    """Get all translations for a language"""
    return TRANSLATIONS.get(language, TRANSLATIONS['en'])


def get_regions(language: str = 'en') -> list:
    """Get list of regions"""
    if language not in TANZANIA_REGIONS:
        language = 'en'
    return sorted(list(TANZANIA_REGIONS[language].keys()))


def get_districts(region: str, language: str = 'en') -> list:
    """Get list of districts for a region"""
    if language not in TANZANIA_REGIONS:
        language = 'en'
    return TANZANIA_REGIONS[language].get(region, [])
