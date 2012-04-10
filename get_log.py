from iron_worker import *
import argparse
import json

parser = argparse.ArgumentParser(description="Grabs the log for an IronWorker task.")
parser.add_argument("--task", type=str, required=True)

args = parser.parse_args()

worker = IronWorker(config="config")
log = worker.getLog(args.task)

print json.loads(log.split("STDOUTSEP")[1])
