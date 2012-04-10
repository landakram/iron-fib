import argparse
from iron_worker import *

parser = argparse.ArgumentParser(description="Runs a worker to calculate Fibonacci numbers")
parser.add_argument("--max", type=int, required=False)

args = parser.parse_args()

max = args.max if args.max is not None else 100000

worker = IronWorker(config="config")
task = worker.postTask(name="FibWorker", payload={ "max": max })

print task
