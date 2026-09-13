import numpy as np
import sys
sys.path.insert(0, 'output/artifacts')
from delta import Delta, r, eu, es, lam, mu, apply_B

# Verify non-cohomology: fixed point vs period-3 orbit (exact values)
p_fix = np.array([0.,0.])
avg_fix = r(p_fix)
P = [np.array([0.75,0.5]), np.array([0.0,0.25]), np.array([0.25,0.25])]
avgs = [r(p) for p in P]
print("avg_fix=", avg_fix, " orbit avgs=", avgs, " mean=", np.mean(avgs))

# Scan: grid of x, menu of (a,b)
menu = [0.05, 0.04, 0.03, 0.02, 0.01, -0.05, -0.03, 0.05j if False else 0.05]
pairs = [(a,b) for a in [0.05,0.03,0.02,0.01,-0.02,-0.05] for b in [0.05,0.03,0.02,0.01,-0.02,-0.05]]
n = 40
xs = np.linspace(0,1,n,endpoint=False)
best_min = 1e9
worst = None
import time
t0=time.time()
res = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        x = np.array([xs[i], xs[j]])
        best = 0.0
        for (a,b) in pairs:
            d = Delta(x,a,b,N=14)
            q = abs(d)/abs(a*b)
            if q>best: best=q
        res[i,j]=best
        if best<best_min:
            best_min=best; worst=(xs[i],xs[j])
print("time", time.time()-t0)
print("inf over grid of best-ratio:", best_min, "at", worst)
print("percentiles:", np.percentile(res,[0,1,5,25,50,75,100]))
np.save('output/artifacts/scan1_res.npy', res)
