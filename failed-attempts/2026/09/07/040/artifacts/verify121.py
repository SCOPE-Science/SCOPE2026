import numpy as np, math, json, csv
from verify_twist import envelope_for_q, direct_check
r = envelope_for_q(121, 11)
dc = direct_check(121, 11, r["argmax"])
r["direct_recompute"] = float(dc)
r["agreement"] = float(abs(dc - r["argmax"]["absS"]))
print(json.dumps({k: r[k] for k in ["q","maxR","argmax","direct_recompute","agreement"]}))
with open("output/artifacts/envelope_q121.csv","w",newline="") as f:
    w = csv.writer(f); w.writerow(["N","envelope_max_absS","trivial_N"])
    for i,e in enumerate(r["envelope"],start=1):
        w.writerow([i,e,i])
env = r.pop("envelope")
with open("output/artifacts/summary_q121.json","w") as f:
    json.dump(r,f,indent=1)
print("DONE121")
