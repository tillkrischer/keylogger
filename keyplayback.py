import time
import argparse
from subprocess import Popen, PIPE

def parseLine(f):
    line = f.readline()
    if line == "":
        return (None, None)
    else:
        words = line.split()
        timestamp = float(words[0])
        command = " ".join(words[1:])
        return (timestamp, command)

parser = argparse.ArgumentParser(description="Record Keypresses.")
parser.add_argument("input", type=str, help="input file")
parser.add_argument("--speed", "-s", type=int, default=1, help="relative speed of playback")
args = parser.parse_args()

f = open(args.input, "r")
start = time.time()

timestamp, command = parseLine(f)
while timestamp:
    elapsedtime = time.time() - start
    while timestamp and timestamp < elapsedtime * args.speed:
        Popen(["xte", command])
        timestamp, command = parseLine(f)
    time.sleep(0.01)

