import os

p1s=range(0,5)
p2s=range(0,5)

for i in p1s:
    for j in p2s:
        print(f"logging for p1:{i} and p2:{j}")
        os.system(f"python demo.py --param1={i} --param2={j}")
