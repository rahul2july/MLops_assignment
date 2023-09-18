# You can create more variables according to your project. The following are the basic variables that have been provided to you
DB_PATH = '/Users/rahugup4/airflow/dags/Lead_scoring_data_pipeline/'
DB_FILE_NAME = 'lead_scoring_data_cleaning.db'
UNIT_TEST_DB_FILE_NAME = 'unit_test_cases.db'
# Iteration 1 - Data Pipeline
#DATA_FILE = 'leadscoring.csv'

# Iteration 2 - Inference Pipeline
DATA_FILE = 'leadscoring_inference.csv'

DATA_DIRECTORY = '/Users/rahugup4/airflow/dags/Lead_scoring_data_pipeline/data/'
MAPPING_DIRECTORY = "/Users/rahugup4/airflow/dags/Lead_scoring_data_pipeline/mapping/"
INTERACTION_MAPPING = MAPPING_DIRECTORY + "interaction_mapping.csv"
INDEX_COLUMNS= ['created_date', 'city_tier', 'first_platform_c', 'first_utm_medium_c', 'first_utm_source_c', 'total_leads_droppped', 'referred_lead', 'app_complete_flag']
INDEX_COLUMNS_TRAINING = []
INDEX_COLUMNS_INFERENCE = []
NOT_FEATURES = []
INDEX_COLUMNS = ['created_date', 'city_tier', 'first_platform_c', 'first_utm_medium_c', 'first_utm_source_c', 'total_leads_droppped', 'referred_lead', 'app_complete_flag']






