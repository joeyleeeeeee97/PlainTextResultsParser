# -*- coding: UTF-8 -*-
import json as js
import os, getopt, argparse, collections
from prettytable import PrettyTable

workloads = ["fortune", "plaintext", "db", "update", "json", "query"]
stress = ["concurrencyLevels", "queryIntervals", "pipelineConcurrencyLevels"]
result_dict = collections.defaultdict(dict)
workload_field_map = {"query": "queryIntervals", "plaintext": "pipelineConcurrencyLevels", "db": "concurrencyLevels",
                      "update": "concurrencyLevels", "fortune": "concurrencyLevels", "json": "concurrencyLevels"}

# parse argumetns
parser = argparse.ArgumentParser(
    description="Analyse json resluts from FrameWork BenchMark.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument(
    '--files', default=[], nargs='+',
    help='FrameworkBenchmarks test result json files, such as results/timestamp/results.json'
)
parser.add_argument(
    '--datas', default=['latencyAvg', 'totalRequests', 'latencyMax'], nargs='+',
    help='interested datas to collect and print in parser'
)
args = parser.parse_args()

# gather data
for json_results in [js.loads(open(f).read()) for f in args.files]:
    stress_field_map = dict([(s, json_results[s]) for s in stress])
    for workload in [w for w in workloads if json_results["rawData"][w]]:
        for test_name, test_result in json_results["rawData"][workload].items():
            result_dict[workload][test_name] = test_result

# print table
for interested_data in args.datas:
    for k, workload_results in result_dict.items():
        pt = PrettyTable()
        pt.title = "Type: " + k + ", Result: " + interested_data
        pt.field_names = [workload_field_map[k]] + list(result_dict[k].keys())
        for i in range(len(workload_results[next(iter(workload_results))])):
            data_row = [v[i].get(interested_data) for v in workload_results.values()]
            pt.add_row([stress_field_map[workload_field_map[k]][i]] + data_row)
        print(pt)