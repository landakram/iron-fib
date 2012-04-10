import argparse
import json

parser = argparse.ArgumentParser(description="Fibonacci sequence up to a max")
parser.add_argument("-payload", type=str, required=False)
parser.add_argument("-d", type=str, required=False)
parser.add_argument("-e", type=str, required=False)
parser.add_argument("-id", type=str, required=False)

args = parser.parse_args()

max = 1000

if args.payload:
    payload = json.load(open(args.payload))
    max = payload.get('max', max)

cache = {0:0, 1:1}

n = 2
while n <= max:
    cache[n] = cache[n-1] + cache[n-2]
    n += 1

print "STDOUTSEP%sSTDOUTSEP" % json.dumps(cache)
