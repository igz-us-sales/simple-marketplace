import mlrun
import pandas as pd

DATA_URL = "https://s3.wasabisys.com/iguazio/data/iris/iris_dataset.csv"


def test_pd_describe():
    pd_describe = mlrun.import_function("function.yaml")

    run = pd_describe.run(inputs={"data": DATA_URL}, local=True)

    output_df = run.artifact("dataset_described").as_df()
    reference_df = pd.read_csv(DATA_URL).describe()

    assert output_df.equals(reference_df)
