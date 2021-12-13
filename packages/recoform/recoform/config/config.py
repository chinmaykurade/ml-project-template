import pathlib
import pandas as pd
import recoform

pd.options.display.max_rows = 10
pd.options.display.max_columns = 10


PACKAGE_ROOT = pathlib.Path(recoform.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"
EXTERNAL_MODEL_DIR = PACKAGE_ROOT / "external_models"
DATASET_DIR = PACKAGE_ROOT / "datasets"

TESTING_FILE = "test.json"

PIPELINE_NAME = "recommender"
PIPELINE_SAVE_FILE = f"{PIPELINE_NAME}_output_v"