# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from random import randint
from uuid import uuid4

from google.protobuf import timestamp_pb2
from google.auth import credentials
from google.cloud import aiplatform
import vertexai

PROJECT = "abc"
PROJECT_NUMBER = 123
LOCATION = "us-central1"
LOCATION_EUROPE = "europe-west4"
LOCATION_ASIA = "asia-east1"
PARENT = f"projects/{PROJECT}/locations/{LOCATION}"

DISPLAY_NAME = str(uuid4())  # Create random display name
DISPLAY_NAME_2 = str(uuid4())

CREATE_DATE = "2022-06-11T12:30:00-08:00"

ORDER_BY = "CREATE_TIME desc"

STAGING_BUCKET = "gs://my-staging-bucket"
EXPERIMENT_NAME = "fraud-detection-trial-72"
CREDENTIALS = credentials.AnonymousCredentials()

SERVICE_ACCOUNT = "abc@abc.iam.gserviceaccount.com"

RESOURCE_ID = str(randint(10000000, 99999999))  # Create random resource ID
RESOURCE_ID_2 = str(randint(10000000, 99999999))

BATCH_PREDICTION_JOB_NAME = f"{PARENT}/batchPredictionJobs/{RESOURCE_ID}"
DATASET_NAME = f"{PARENT}/datasets/{RESOURCE_ID}"
ENDPOINT_NAME = f"{PARENT}/endpoints/{RESOURCE_ID}"
MODEL_NAME = f"{PARENT}/models/{RESOURCE_ID}"
VERSION_ID = "test-version"
TRAINING_JOB_NAME = f"{PARENT}/trainingJobs/{RESOURCE_ID}"

BIGQUERY_SOURCE = f"bq://{PROJECT}.{DATASET_NAME}.table1"
BIGQUERY_DESTINATION_PREFIX = "bq://bigquery-public-data.ml_datasets.iris"

GCS_SOURCES = ["gs://bucket1/source1.jsonl", "gs://bucket7/source4.jsonl"]
BIGQUERY_SOURCE = "bq://bigquery-public-data.ml_datasets.iris"
GCS_DESTINATION = "gs://bucket3/output-dir/"
INSTANCES_FORMAT = "jsonl"

TRAINING_FRACTION_SPLIT = 0.7
TEST_FRACTION_SPLIT = 0.15
VALIDATION_FRACTION_SPLIT = 0.15

BUDGET_MILLI_NODE_HOURS_8000 = 8000

ENCRYPTION_SPEC_KEY_NAME = f"{PARENT}/keyRings/{RESOURCE_ID}/cryptoKeys/{RESOURCE_ID_2}"

PYTHON_PACKAGE = "gs://my-packages/training.tar.gz"
PYTHON_PACKAGE_CMDARGS = f"--model-dir={GCS_DESTINATION}"
TRAIN_IMAGE = "gcr.io/train_image:latest"
DEPLOY_IMAGE = "gcr.io/deploy_image:latest"

PREDICTION_TEXT_INSTANCE = "This is some text for testing NLP prediction output"

PREDICTION_TABULAR_CLASSIFICATION_INSTANCE = [
    {
        "petal_length": "1.4",
        "petal_width": "1.3",
        "sepal_length": "5.1",
        "sepal_width": "2.8",
    }
]
PREDICTION_TABULAR_REGRESSOIN_INSTANCE = [
    {
        "BOOLEAN_2unique_NULLABLE": False,
        "DATETIME_1unique_NULLABLE": "2019-01-01 00:00:00",
        "DATE_1unique_NULLABLE": "2019-01-01",
        "FLOAT_5000unique_NULLABLE": 1611,
        "FLOAT_5000unique_REPEATED": [2320, 1192],
        "INTEGER_5000unique_NULLABLE": "8",
        "NUMERIC_5000unique_NULLABLE": 16,
        "STRING_5000unique_NULLABLE": "str-2",
        "STRUCT_NULLABLE": {
            "BOOLEAN_2unique_NULLABLE": False,
            "DATE_1unique_NULLABLE": "2019-01-01",
            "DATETIME_1unique_NULLABLE": "2019-01-01 00:00:00",
            "FLOAT_5000unique_NULLABLE": 1308,
            "FLOAT_5000unique_REPEATED": [2323, 1178],
            "FLOAT_5000unique_REQUIRED": 3089,
            "INTEGER_5000unique_NULLABLE": "1777",
            "NUMERIC_5000unique_NULLABLE": 3323,
            "TIME_1unique_NULLABLE": "23:59:59.999999",
            "STRING_5000unique_NULLABLE": "str-49",
            "TIMESTAMP_1unique_NULLABLE": "1546387199999999",
        },
        "TIMESTAMP_1unique_NULLABLE": "1546387199999999",
        "TIME_1unique_NULLABLE": "23:59:59.999999",
    }
]
SCRIPT_PATH = "task.py"
CONTAINER_URI = "gcr.io/my_project/my_image:latest"
ARGS = ["--tfds", "tf_flowers:3.*.*"]
REPLICA_COUNT = 1
MACHINE_TYPE = "n1-standard-4"
ACCELERATOR_TYPE = "ACCELERATOR_TYPE_UNSPECIFIED"
ACCELERATOR_COUNT = 0
NETWORK_ATTACHMENT_NAME = "network-attachment-name"
DOMAIN = "test.com"
TARGET_PROJECT = "target-project"
TARGET_NETWORK = "target-network"
PSC_INTERFACE_CONFIG = {
    "network_attachment": NETWORK_ATTACHMENT_NAME,
    "dns_peering_configs": [
        {
            "domain": DOMAIN,
            "target_project": TARGET_PROJECT,
            "target_network": TARGET_NETWORK,
        },
    ],
}

# Model constants
MODEL_RESOURCE_NAME = f"{PARENT}/models/1234"
MODEL_ARTIFACT_URI = "gs://bucket3/output-dir/"
SERVING_CONTAINER_IMAGE_URI = "http://gcr.io/test/test:latest"
SERVING_CONTAINER_IMAGE = "gcr.io/test-serving/container:image"
SERVING_CONTAINER_PREDICT_ROUTE = "predict"
SERVING_CONTAINER_HEALTH_ROUTE = "metadata"
DESCRIPTION = "test description"
SERVING_CONTAINER_COMMAND = ["python3", "run_my_model.py"]
SERVING_CONTAINER_ARGS = ["--test", "arg"]
SERVING_CONTAINER_ENVIRONMENT_VARIABLES = {
    "learning_rate": 0.01,
    "loss_fn": "mse",
}
SERVING_CONTAINER_PORTS = [8888, 10000]
INSTANCE_SCHEMA_URI = "gs://test/schema/instance.yaml"
PARAMETERS_SCHEMA_URI = "gs://test/schema/parameters.yaml"
PREDICTION_SCHEMA_URI = "gs://test/schema/predictions.yaml"

MODEL_DESCRIPTION = "This is a model"
SERVING_CONTAINER_COMMAND = ["python3", "run_my_model.py"]
SERVING_CONTAINER_ARGS = ["--test", "arg"]
SERVING_CONTAINER_ENVIRONMENT_VARIABLES = {
    "learning_rate": 0.01,
    "loss_fn": "mse",
}

SERVING_CONTAINER_PORTS = [8888, 10000]
EXPLANATION_METADATA = aiplatform.explain.ExplanationMetadata(
    inputs={
        "features": {
            "input_tensor_name": "dense_input",
            # Input is tabular data
            "modality": "numeric",
            # Assign feature names to the inputs for explanation
            "encoding": "BAG_OF_FEATURES",
            "index_feature_mapping": [
                "crim",
                "zn",
                "indus",
                "chas",
                "nox",
                "rm",
                "age",
                "dis",
                "rad",
                "tax",
                "ptratio",
                "b",
                "lstat",
            ],
        }
    },
    outputs={"prediction": {"output_tensor_name": "dense_2"}},
)
EXPLANATION_PARAMETERS = aiplatform.explain.ExplanationParameters(
    {"xrai_attribution": {"step_count": 1}}
)

# Endpoint constants
DEPLOYED_MODEL_DISPLAY_NAME = "model_name"
TRAFFIC_PERCENTAGE = 80
TRAFFIC_SPLIT = {"a": 99, "b": 1}
MIN_REPLICA_COUNT = 1
MAX_REPLICA_COUNT = 1
ACCELERATOR_TYPE = "NVIDIA_TESLA_P100"
ACCELERATOR_COUNT = 2
ENDPOINT_DEPLOY_METADATA = ()
PREDICTION_TABULAR_INSTANCE = {
    "longitude": "-124.35",
    "latitude": "40.54",
    "housing_median_age": "52.0",
    "total_rooms": "1820.0",
    "total_bedrooms": "300.0",
    "population": "806",
    "households": "270.0",
    "median_income": "3.014700",
}
MODEL_SERVING_CONTAINER_COMMAND = (["/usr/bin/tensorflow_model_server"],)
MODEL_SERVING_CONTAINER_ARGS = (
    [
        f"--model_name={MODEL_NAME}",
        "--model_base_path=$(AIP_STORAGE_URI)",
        "--rest_api_port=8080",
        "--port=8500",
        "--file_system_poll_wait_seconds=31540000",
    ],
)
PYTHON_PACKAGE_GCS_URI = (
    "gs://bucket3/custom-training-python-package/my_app/trainer-0.1.tar.gz"
)
PYTHON_MODULE_NAME = "trainer.task"
MODEL_TYPE = "CLOUD"

# Feature store constants (legacy)
FEATURESTORE_ID = "movie_prediction"
FEATURESTORE_NAME = (
    f"projects/{PROJECT}/locations/{LOCATION}/featurestores/{FEATURESTORE_ID}"
)
ENTITY_TYPE_ID = "users"
ENTITY_IDS = ["alice", "bob"]
ENTITY_TYPE_NAME = f"projects/{PROJECT}/locations/{LOCATION}/featurestores/{FEATURESTORE_ID}/entityTypes/{ENTITY_TYPE_ID}"
ENTITY_INSTANCES = {
    "movie_01": {
        "title": "The Shawshank Redemption",
        "average_rating": 4.7,
        "genre": "Drama",
    }
}
FEATURE_ID = "liked_genres"
FEATURE_IDS = ["age", "gender", "liked_genres"]
FEATURE_NAME = f"projects/{PROJECT}/locations/{LOCATION}/featurestores/{FEATURESTORE_ID}/entityTypes/{ENTITY_TYPE_ID}/features/{FEATURE_ID}"
FEATURE_VALUE_TYPE = "INT64"
FEATURE_CONFIGS = {
    "age": {"value_type": "INT64", "description": "User age"},
    "gender": {"value_type": "STRING", "description": "User gender"},
    "liked_genres": {
        "value_type": "STRING_ARRAY",
        "description": "An array of genres this user liked",
    },
}
SERVING_FEATURE_IDS = {
    "users": ["age", "gender", "liked_genres"],
    "movies": ["title", "average_rating", "genres"],
}
ONLINE_STORE_FIXED_NODE_COUNT = 1
SYNC = True
FORCE = True
BQ_DESTINATION_OUTPUT_URI = f"bq://{PROJECT}.example_dataset.example_table"
INPUT_CSV_FILE = "gs://cloud-samples-data-us-central1/vertex-ai/feature-store/datasets/movie_prediction.csv"
USERS_FEATURE_TIME = "update_time"
USERS_ENTITY_ID_FIELD = "user_id"
USERS_GCS_SOURCE_URI = (
    "gs://cloud-samples-data-us-central1/vertex-ai/feature-store/datasets/users.avro"
)
GCS_SOURCE_TYPE = "avro"
WORKER_COUNT = 1

# Feature online store constants
FEATURE_ONLINE_STORE_ID = "sample_feature_online_store"
FEATURE_VIEW_ID = "sample_feature_view"
FEATURE_VIEW_BQ_URI = "bq://my_proj.my_dataset.my_table"
FEATURE_VIEW_BQ_ENTITY_ID_COLUMNS = ["id"]
FEATURE_VIEW_BQ_SOURCE = (
    vertexai.resources.preview.feature_store.utils.FeatureViewBigQuerySource(
        uri=FEATURE_VIEW_BQ_URI,
        entity_id_columns=FEATURE_VIEW_BQ_ENTITY_ID_COLUMNS,
    )
)
FEATURE_VIEW_RAG_SOURCE = (
    vertexai.resources.preview.feature_store.utils.FeatureViewVertexRagSource(
        uri=FEATURE_VIEW_BQ_URI,
    )
)
FEATURE_VIEW_BQ_EMBEDDING_COLUMN = "embedding"
FEATURE_VIEW_BQ_EMBEDDING_DIMENSIONS = 10
FEATURE_VIEW_BQ_INDEX_CONFIG = (
    vertexai.resources.preview.feature_store.utils.IndexConfig(
        embedding_column=FEATURE_VIEW_BQ_EMBEDDING_COLUMN,
        dimensions=FEATURE_VIEW_BQ_EMBEDDING_DIMENSIONS,
        algorithm_config=vertexai.resources.preview.feature_store.utils.TreeAhConfig(),
    )
)
FEATURE_GROUP_ID = "sample_feature_group"
FEATURE_GROUP_ID_2 = "sample_feature_group_2"
FEATURE_GROUP_BQ_URI = "bq://my_proj.my_dataset.my_table"
FEATURE_GROUP_BQ_ENTITY_ID_COLUMNS = ["id"]
FEATURE_GROUP_SOURCE = (
    vertexai.resources.preview.feature_store.utils.FeatureGroupBigQuerySource(
        uri=FEATURE_GROUP_BQ_URI,
        entity_id_columns=FEATURE_GROUP_BQ_ENTITY_ID_COLUMNS,
    )
)
REGISTRY_FEATURE_ID = "sample_feature"
REGISTRY_FEATURE_ID_2 = "sample_feature_2"
FG_2_REGISTRY_FEATURE_ID_3 = "sample_feature_3"
FG_2_REGISTRY_FEATURE_ID_4 = "sample_feature_4"
VERSION_COLUMN_NAME = "feature_column"
PROJECT_ALLOWLISTED = ["test-project"]
FR_FEATURE_ID = ".".join([FEATURE_GROUP_ID, REGISTRY_FEATURE_ID])
FR_FEATURE_ID_2 = ".".join([FEATURE_GROUP_ID, REGISTRY_FEATURE_ID_2])
FR_FEATURE_ID_3 = ".".join([FEATURE_GROUP_ID_2, FG_2_REGISTRY_FEATURE_ID_3])
FR_FEATURE_ID_4 = ".".join([FEATURE_GROUP_ID_2, FG_2_REGISTRY_FEATURE_ID_4])

FEATURE_GROUPS_MAPPING = {
    FEATURE_GROUP_ID: [REGISTRY_FEATURE_ID, REGISTRY_FEATURE_ID_2],
    FEATURE_GROUP_ID_2: [FG_2_REGISTRY_FEATURE_ID_3, FG_2_REGISTRY_FEATURE_ID_4],
}


FEATURE_VIEW_REGISTRY_SOURCE = (
    vertexai.resources.preview.feature_store.utils.FeatureViewRegistrySource(
        features=[FR_FEATURE_ID, FR_FEATURE_ID_2, FR_FEATURE_ID_3, FR_FEATURE_ID_4],
        project_number=PROJECT_NUMBER,
    )
)

TABULAR_TARGET_COLUMN = "target_column"
FORECASTNG_TIME_COLUMN = "date"
FORECASTNG_TIME_SERIES_IDENTIFIER_COLUMN = "time_series_id"
FORECASTNG_UNAVAILABLE_AT_FORECAST_COLUMNS = []
FORECASTNG_AVAILABLE_AT_FORECAST_COLUMNS = []
FORECASTNG_FORECAST_HORIZON = 1
DATA_GRANULARITY_UNIT = "week"
DATA_GRANULARITY_COUNT = 1

TIMESTAMP_SPLIT_COLUMN_NAME = "timestamp_split_column_name"
WEIGHT_COLUMN = "weight"
TIME_SERIES_ATTRIBUTE_COLUMNS = []
CONTEXT_WINDOW = 0
EXPORT_EVALUATED_DATA_ITEMS = True
EXPORT_EVALUATED_DATA_ITEMS_BIGQUERY_DESTINATION_URI = "bq://test:test:test"
EXPORT_EVALUATED_DATA_ITEMS_OVERRIDE_DESTINATION = True
QUANTILES = [0, 0.5, 1]
ENABLE_PROBABILISTIC_INFERENCE = True
VALIDATION_OPTIONS = "fail-pipeline"
PREDEFINED_SPLIT_COLUMN_NAME = "predefined"

SCHEMA_TITLE = "system.Schema"
SCHEMA_VERSION = "0.0.1"
METADATA = {}

EXPERIMENT_RUN_NAME = "my-run"
EXPERIMENT_RUN_STATE = aiplatform.gapic.Execution.State.RUNNING

METRICS = {"accuracy": 0.1}
PARAMS = {"learning_rate": 0.1}
CLASSIFICATION_METRICS = {
    "display_name": "my-classification-metrics",
    "labels": ["cat", "dog"],
    "matrix": [[9, 1], [1, 9]],
    "fpr": [0.1, 0.5, 0.9],
    "tpr": [0.1, 0.7, 0.9],
    "threshold": [0.9, 0.5, 0.1],
}
TEMPLATE_PATH = "pipeline.json"

ML_MODEL = "LinearRegression()"
EXPERIMENT_MODEL_ID = "my-sklearn-model"
EXPERIMENT_MODEL_INPUT_EXAMPLE = [[1, 2], [3, 4]]

STEP = 1
TIMESTAMP = timestamp_pb2.Timestamp()

# Hyperparameter tuning job
HYPERPARAMETER_TUNING_JOB_DISPLAY_NAME = "hpt_job"
HYPERPARAMETER_TUNING_JOB_ID = "4447046521673744384"
HYPERPARAMETER_TUNING_JOB_METRIC_SPEC = {"loss": "minimize"}
HYPERPARAMETER_TUNING_JOB_MAX_TRIAL_COUNT = 128
HYPERPARAMETER_TUNING_JOB_PARALLEL_TRIAL_COUNT = 8
HYPERPARAMETER_TUNING_JOB_LABELS = {"my_key": "my_value"}

# Custom job
CUSTOM_JOB_DISPLAY_NAME = "custom_job"
CUSTOM_JOB_WORKER_POOL_SPECS = [
    {
        "machine_spec": {
            "machine_type": "n1-standard-4",
            "accelerator_type": "NVIDIA_TESLA_K80",
            "accelerator_count": 1,
        },
        "replica_count": 1,
        "container_spec": {
            "image_uri": CONTAINER_URI,
            "command": [],
            "args": [],
        },
    }
]

CUSTOM_JOB_WORKER_POOL_SPECS_WITHOUT_ACCELERATOR = [
    {
        "machine_spec": {
            "machine_type": "n1-standard-4",
        },
        "replica_count": 1,
        "container_spec": {
            "image_uri": CONTAINER_URI,
            "command": [],
            "args": [],
        },
    }
]

VERSION_ID = "test-version"
IS_DEFAULT_VERSION = False
VERSION_ALIASES = ["test-version-alias"]
VERSION_DESCRIPTION = "test-version-description"

# TensorBoard
TENSORBOARD_LOG_DIR = "gs://fake-dir"
TENSORBOARD_ID = "8888888888888888888"
TENSORBOARD_NAME = (
    f"projects/{PROJECT}/locations/{LOCATION}/tensorboards/my-tensorboard"
)
TENSORBOARD_EXPERIMENT_NAME = "my-tensorboard-experiment"
TENSORBOARD_PLUGIN_PROFILE_NAME = "profile"

# Vector Search
VECTOR_SEARCH_INDEX = "123"
VECTOR_SEARCH_INDEX_DATAPOINTS = [
    aiplatform.compat.types.index_v1beta1.IndexDatapoint(
        datapoint_id="datapoint_id_1", feature_vector=[0.1, 0.2]
    ),
    aiplatform.compat.types.index_v1beta1.IndexDatapoint(
        datapoint_id="datapoint_id_2", feature_vector=[0.3, 0.4]
    ),
]
VECTOR_SEARCH_INDEX_DATAPOINT_IDS = ["datapoint_id_1", "datapoint_id_2"]
VECTOR_SEARCH_INDEX_ENDPOINT = "456"
VECTOR_SEARCH_DEPLOYED_INDEX_ID = "789"
VECTOR_SEARCH_INDEX_QUERIES = [[0.1]]
VECTOR_SEARCH_INDEX_HYBRID_QUERIES = [
    aiplatform.matching_engine.matching_engine_index_endpoint.HybridQuery(
        dense_embedding=[1, 2, 3],
        sparse_embedding_dimensions=[10, 20, 30],
        sparse_embedding_values=[1.0, 1.0, 1.0],
        rrf_ranking_alpha=0.5,
    ),
    aiplatform.matching_engine.matching_engine_index_endpoint.HybridQuery(
        dense_embedding=[1, 2, 3],
        sparse_embedding_dimensions=[10, 20, 30],
        sparse_embedding_values=[0.1, 0.2, 0.3],
    ),
    aiplatform.matching_engine.matching_engine_index_endpoint.HybridQuery(
        sparse_embedding_dimensions=[10, 20, 30],
        sparse_embedding_values=[0.1, 0.2, 0.3],
    ),
    aiplatform.matching_engine.matching_engine_index_endpoint.HybridQuery(
        dense_embedding=[1, 2, 3]
    ),
]
VECTOR_SEARCH_FILTER = [
    aiplatform.matching_engine.matching_engine_index_endpoint.Namespace(
        "color", ["red"], []
    ),
    aiplatform.matching_engine.matching_engine_index_endpoint.Namespace(
        "shape", [], ["squared"]
    ),
]
VECTOR_SEARCH_NUMERIC_FILTER = [
    aiplatform.matching_engine.matching_engine_index_endpoint.NumericNamespace(
        name="cost", value_int=5, op="GREATER"
    )
]
VECTOR_SEARCH_PER_CROWDING_ATTRIBUTE_NEIGHBOR_COUNT = 5
VECTOR_SEARCH_INDEX_DISPLAY_NAME = "my-vector-search-index"
VECTOR_SEARCH_INDEX_DESCRIPTION = "test description"
VECTOR_SEARCH_INDEX_LABELS = {"my_key": "my_value"}
VECTOR_SEARCH_GCS_URI = "gs://fake-dir"
VECTOR_SEARCH_INDEX_ENDPOINT_DISPLAY_NAME = "my-vector-search-index-endpoint"
VECTOR_SEARCH_PRIVATE_ENDPOINT_SIGNED_JWT = "fake-signed-jwt"
VECTOR_SEARCH_VPC_NETWORK = "vpc-network"
VECTOR_SEARCH_PSC_PROJECT_ALLOWLIST = ["test-project", "test-project-2"]
VECTOR_SEARCH_PSC_AUTOMATION_CONFIGS = [
    ("test-project", "network1"),
    ("test-project2", "network2"),
]
VECTOR_SEARCH_PSC_MANUAL_IP_ADDRESS = "1.2.3.4"
