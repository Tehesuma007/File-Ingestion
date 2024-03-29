
import os
import subprocess
import pandas as pd
import datetime 
import gc
import re
import logging
logger = logging.getLogger(__name__)




def col_header_val(df,table_config):
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace('[#,@,&,:]','', regex=True)
    df.columns = df.columns.str.replace(' ', '')
    df.columns = df.columns.str.replace(':', '')
    df.columns = df.columns.str.replace('.', '_')
    expected_col = list(map(lambda x: x.lower(), table_config['columns']))
    expected_col.sort()
    df.columns = list(map(lambda x: x.lower(), list(df.columns)))
    df = df.reindex(sorted(df.columns), axis=1)
    if len(df.columns) == len(expected_col) and list(expected_col)  == list(df.columns):
        print("column name and column length validation passed")
        return 1
    else:
        print("column name and column length validation failed")
        mismatched_columns_file = list(set(df.columns).difference(expected_col))
        print("Following File columns are not in the YAML file",mismatched_columns_file)
        missing_YAML_file = list(set(expected_col).difference(df.columns))
        print("Following YAML columns are not in the file uploaded",missing_YAML_file)
        logger.info(f'df columns: {df.columns}')
        logger.info(f'expected columns: {expected_col}')
        return 0
