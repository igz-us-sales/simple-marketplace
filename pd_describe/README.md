# Pd Describe

Use pandas `describe` function on a given CSV or Parquet file.

Example:
```python
import mlrun

mlrun.mlconf.hub_url = 'https://raw.githubusercontent.com/igz-us-sales/simple-marketplace'

pd_describe = mlrun.import_function("hub://pd_describe")

run = pd_describe.run(inputs={"data": 'https://s3.wasabisys.com/iguazio/data/iris/iris_dataset.csv'})

describe_df = run.artifact("dataset_described").as_df()
```