# You can create more variables according to your project. The following are the basic variables that have been provided to you
DB_PATH = "/Users/rahugup4/airflow/dags/Lead_scoring_data_pipeline/"
DB_FILE_NAME = "lead_scoring_data_cleaning.db"
#DB_FILE_NAME = "lead_scoring_data_cleaning_inference.db"

DB_FILE_MLFLOW_PATH = '/Users/rahugup4/Desktop/IIIT_Bangalore/MLops/Assignment/Assignment/03_inference_pipeline/scripts/'
DB_FILE_MLFLOW = "Lead_scoring_mlflow_production.db"


FILE_PATH = '/Users/rahugup4/Desktop/IIIT_Bangalore/MLops/Assignment/Assignment/03_inference_pipeline/scripts/prediction_distribution.txt'

TRACKING_URI = 'http://0.0.0.0:6006'




# list of the features that needs to be there in the final encoded dataframe
ONE_HOT_ENCODED_FEATURES = ['city_tier_1.0', 'city_tier_2.0', 'city_tier_3.0', 'first_platform_c_Level0', 'first_platform_c_Level1', 'first_platform_c_Level2', 'first_platform_c_Level3', 'first_platform_c_Level7', 'first_platform_c_Level8', 'first_platform_c_others', 'first_utm_medium_c_Level0', 'first_utm_medium_c_Level10', 'first_utm_medium_c_Level11', 'first_utm_medium_c_Level13', 'first_utm_medium_c_Level15', 'first_utm_medium_c_Level16', 'first_utm_medium_c_Level2', 'first_utm_medium_c_Level20', 'first_utm_medium_c_Level26', 'first_utm_medium_c_Level3', 'first_utm_medium_c_Level30', 'first_utm_medium_c_Level33', 'first_utm_medium_c_Level4', 'first_utm_medium_c_Level43', 'first_utm_medium_c_Level5', 'first_utm_medium_c_Level6', 'first_utm_medium_c_Level8', 'first_utm_medium_c_Level9', 'first_utm_medium_c_others', 'first_utm_source_c_Level0', 'first_utm_source_c_Level14', 'first_utm_source_c_Level16', 'first_utm_source_c_Level2', 'first_utm_source_c_Level4', 'first_utm_source_c_Level5', 'first_utm_source_c_Level6', 'first_utm_source_c_Level7', 'first_utm_source_c_others', 'total_leads_droppped', 'referred_lead']
# list of features that need to be one-hot encoded
FEATURES_TO_ENCODE = ['city_tier', 'first_platform_c', 'first_utm_medium_c', 'first_utm_source_c']


# experiment, model name and stage to load the model from mlflow model registry
MODEL_NAME = '/Users/rahugup4/Desktop/IIIT_Bangalore/MLops/Assignment/Assignment/mlruns/1/c9fdec93b24842c69b02688652c8bf5e/artifacts/models'
STAGE = 'production'
EXPERIMENT = "Lead_scoring_mlflow_production"


