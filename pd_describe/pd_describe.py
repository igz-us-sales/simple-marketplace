import mlrun
import pandas as pd


def pd_describe(
    context: mlrun.MLClientCtx,
    data: mlrun.DataItem,
) -> None:
    """
    Sample function to log a description of a pandas dataframe.

    :param context: MLRun Context
    :param data:    MLRun input pointing to pandas dataframe (csv/parquet file path)
    """
    # Load data from DataItem
    df = data.as_df()

    # Pandas describe
    describe = df.describe()

    # Log described dataset
    context.log_dataset(key="dataset_described", df=describe)
