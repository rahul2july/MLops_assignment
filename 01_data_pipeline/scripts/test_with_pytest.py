##############################################################################
# Import the necessary modules
# #############################################################################

from utils import *
from constants import *

import warnings
warnings.filterwarnings("ignore")

import pytest
from city_tier_mapping import *
from significant_categorical_level import *

###############################################################################
# Write test cases for load_data_into_db() function
# ##############################################################################

def test_load_data_into_db():
    """_summary_
    This function checks if the load_data_into_db function is working properly by
    comparing its output with test cases provided in the db in a table named
    'loaded_data_test_case'

    INPUTS
        DB_FILE_NAME : Name of the database file 'utils_output.db'
        DB_PATH : path where the db file should be present
        UNIT_TEST_DB_FILE_NAME: Name of the test database file 'unit_test_cases.db'

    SAMPLE USAGE
        output=test_get_data()

    """
    
    load_data_into_db(DB_PATH, DB_FILE_NAME, DATA_DIRECTORY)

    print("Connecting to the database")
    cnx = sqlite3.connect(DB_PATH+DB_FILE_NAME)
    
    print("Reading the data from the loaded_data")
    loaded_data = pd.read_sql('select * from loaded_data', cnx)
    print("loaded_data shape is : ", loaded_data.shape)
    
    print("Connecting to the database")
    cnx_ut = sqlite3.connect(DB_PATH+UNIT_TEST_DB_FILE_NAME)
    
    print("Reading the data from the loaded_data_test_case")
    test_case = pd.read_sql('select * from loaded_data_test_case', cnx_ut)
    print("test_case shape is: ", test_case.shape)
    
    print("Closing the database Connections")
    cnx.close()
    cnx_ut.close()
    
    assert loaded_data.equals(loaded_data_test_case), "Dataframes not same, incorrect data loading"
    
    # assert test_case.equals(test_case)  # loaded_data

###############################################################################
# Write test cases for map_city_tier() function
# ##############################################################################
def test_map_city_tier():
    """_summary_
    This function checks if map_city_tier function is working properly by
    comparing its output with test cases provided in the db in a table named
    'city_tier_mapped_test_case'

    INPUTS
        DB_FILE_NAME : Name of the database file 'utils_output.db'
        DB_PATH : path where the db file should be present
        UNIT_TEST_DB_FILE_NAME: Name of the test database file 'unit_test_cases.db'

    SAMPLE USAGE
        output=test_map_city_tier()

    """
    map_city_tier(DB_PATH, DB_FILE_NAME, city_tier_mapping)
    
    print ("Connecting to the database")
    cnx = sqlite3.connect(DB_PATH+DB_FILE_NAME)
    
    print ("Reading the data from the city_tier_mapped")
    city_tier_mapped = pd.read_sql('select * from city_tier_mapped', cnx)
    print("city_tier_mapped shape is: ", city_tier_mapped.shape)
    
    print ("Connecting to the database")
    cnx_ut = sqlite3.connect(DB_PATH+UNIT_TEST_DB_FILE_NAME)
    
    print ("Reading data from the city_tier_mapped_test_case")
    city_tier_mapped_test_case = pd.read_sql('select * from city_tier_mapped_test_case', cnx_ut)
    print("city_tier_mapped_test_case shape is : ", city_tier_mapped_test_case.shape)
    
    print("Closing the database connections")
    cnx.close()
    cnx_ut.close()
    
    assert city_tier_mapped.equals(city_tier_mapped_test_case), "Dataframes not same, incorrect city tier mapping"
    
    # assert test_case.equals(city_tier_mapped_df)

###############################################################################
# Write test cases for map_categorical_vars() function
# ##############################################################################    
def test_map_categorical_vars():
    """_summary_
    This function checks if map_cat_vars function is working properly by
    comparing its output with test cases provided in the db in a table named
    'categorical_variables_mapped_test_case'

    INPUTS
        DB_FILE_NAME : Name of the database file 'utils_output.db'
        DB_PATH : path where the db file should be present
        UNIT_TEST_DB_FILE_NAME: Name of the test database file 'unit_test_cases.db'
    
    SAMPLE USAGE
        output=test_map_cat_vars()

    """    
    map_categorical_vars(DB_PATH, DB_FILE_NAME, list_platform, list_medium, list_source)
    
    print ("Connecting to the database")
    cnx = sqlite3.connect(DB_PATH+DB_FILE_NAME)
    
    print ("Reading the data from categorical_variables_mapped")
    categorical_variable_mapped = pd.read_sql('select * from categorical_variables_mapped', cnx)
    
    print ("Connecting to the database")
    cnx_ut = sqlite3.connect(DB_PATH+UNIT_TEST_DB_FILE_NAME)
    
    print ("Reading the data from the categorical_variables_mapped_test_case")
    categorical_variables_mapped_test_case = pd.read_sql('select * from categorical_variables_mapped_test_case', cnx_ut)
    print("categorical_variables_mapped_test_case shape is : ", categorical_variables_mapped_test_case.shape)
    
    print("Closing database connections")
    cnx.close()
    cnx_ut.close()
    
    assert categorical_variables_mapped.equals(categorical_variables_mapped_test_case), "Dataframes not same, incorrect categorical variables mapping"
    # assert test_case.equals(categorical_variable_mapped)

###############################################################################
# Write test cases for interactions_mapping() function
# ##############################################################################    
def test_interactions_mapping():
    """_summary_
    This function checks if test_column_mapping function is working properly by
    comparing its output with test cases provided in the db in a table named
    'interactions_mapped_test_case'

    INPUTS
        DB_FILE_NAME : Name of the database file 'utils_output.db'
        DB_PATH : path where the db file should be present
        UNIT_TEST_DB_FILE_NAME: Name of the test database file 'unit_test_cases.db'

    SAMPLE USAGE
        output=test_column_mapping()

    """ 
    interactions_mapping(DB_PATH, DB_FILE_NAME, INTERACTION_MAPPING, INDEX_COLUMNS)
    
    print ("Connecting to the database")
    cnx = sqlite3.connect(DB_PATH+DB_FILE_NAME)
    
    print ("Reading the data from the interactions_mapped")
    interactions_mapped = pd.read_sql('select * from interactions_mapped', cnx)
    print("interactions_mapped shape is : ", interactions_mapped.shape)
    print("interactions_mapped columns is : ", interactions_mapped.columns)
    
    print ("Connecting to the database")
    cnx_ut = sqlite3.connect(DB_PATH+UNIT_TEST_DB_FILE_NAME)
    
    print ("Reading the data from the interactions_mapped_test_case")
    interactions_mapped_test_case = pd.read_sql('select * from interactions_mapped_test_case', cnx_ut)
    print("interactions_mapped_test_case shape: ", interactions_mapped_test_case.shape)
    print("interactions_mapped_test_case columns: ", interactions_mapped_test_case.columns)
    
    print("Closing the database connections")
    cnx.close()
    cnx_ut.close()
    
    assert interactions_mapped.equals(interactions_mapped_test_case), "Dataframes not same, incorrect interactions mapping"
    
    # assert test_case.equals(interactions_mapped)