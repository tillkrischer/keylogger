import time
import argparse
from subprocess import Popen, PIPE

parser = argparse.ArgumentParser(description="Record Keypresses")
parser.add_argument("inputid", type=int, help="input device id (xinput list)")
parser.add_argument("output", type=str, help="output file")
args = parser.parse_args()

keycodes = {}
p = Popen(["xmodmap", "-pke"], stdout=PIPE)
for line in p.stdout:
    words = str(line).split()
    key = words[1]
    value = words[3] if len(words) > 3 else ""
    keycodes[key] = value

isControlDown = False
f = open(args.output, "w")
start = time.time()
p = Popen(["xinput", "test", str(args.inputid)], stdout=PIPE)
for line in p.stdout:
    words = str(line).split()
    goingdown = words[1] == "press"
    key = keycodes.get(words[2])
    if key == "Control_L" or key == "Control_R":
        isControlDown = goingdown
    if key == "q" and isControlDown:
        break
    s = []
    s.append(str(time.time() - start))
    s.append("keydown" if goingdown else "keyup")
    s.append(key)
    f.write(" ".join(s))
    f.write("\n")

