# H^{4,t} = ker(d: C^4_t -> C^5_t) / im(d: C^3_t -> C^4_t), t = stem+4.
# ker4(t) from ext_scan2 dimker; im = dimC3(t) (verified full rank above for t=59..64; verify 56,57,58 too).
from collections import defaultdict
import subprocess, re, sys
def ker4_via_script(stem):
    # call ext_scan2 stem 4
    p = subprocess.run(["python3","output/artifacts/ext_scan2.py",str(stem),"4"],capture_output=True,text=True,timeout=300)
    m = re.search(r"dimC=(\d+) nnzrows=(\d+) dimker=(\d+)", p.stdout)
    return tuple(map(int,m.groups()))
for stem in [52,53,54,55,56]:
    print("stem",stem, ker4_via_script(stem), flush=True)
