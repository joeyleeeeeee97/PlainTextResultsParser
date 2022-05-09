# PlainTextResultsParser for [FrameWorkBenchmark](https://github.com/TechEmpower/FrameworkBenchmarks)

## Summary
Provide a plaintext results [FrameWorkBenchmark](https://github.com/TechEmpower/FrameworkBenchmarks) json parser based on python [prettytable](https://pypi.org/project/prettytable/), 
Pros:
- No need to copy files from server
- Easy to visualize data instantly and automatically
- More flexible, we could select interested data and even compare between runs

Demo：
```
python FrameWorkBenchmark_parser.py --data latencyAvg  totalRequests  --files  netty-async/results.json.1  netty-async/results.json.2
+---------------------------------------------------------------+
|              Type: plaintext, Result: latencyAvg              |
+---------------------------+---------------------+-------------+
| pipelineConcurrencyLevels | netty-async-virtual | netty-async |
+---------------------------+---------------------+-------------+
|             4             |       71.33us       |   96.84us   |
|             8             |       113.10us      |   214.25us  |
|             16            |       299.17us      |   498.47us  |
|             32            |       530.01us      |    0.90ms   |
|            256            |        4.59ms       |    8.48ms   |
|            1024           |       19.88ms       |   34.68ms   |
+---------------------------+---------------------+-------------+
+-------------------------------------------------------+
|             Type: json, Result: latencyAvg            |
+-------------------+---------------------+-------------+
| concurrencyLevels | netty-async-virtual | netty-async |
+-------------------+---------------------+-------------+
|         4         |       68.86us       |   73.23us   |
|         8         |       85.92us       |   96.26us   |
|         16        |       104.07us      |   119.98us  |
|         32        |       135.47us      |   209.89us  |
|         64        |       257.47us      |   416.03us  |
|        128        |       516.78us      |   845.06us  |
|        256        |        1.04ms       |    1.69ms   |
|        512        |        2.07ms       |    3.39ms   |
+-------------------+---------------------+-------------+
```

## Usage
Setup via `pip3 install prettytable`, list results json files with --files and interested data with --data.
Note:
- The result files must be formatted by FrameWorkBenchmark
- Make sure different result files are from the same stress level when comparing them
