import numpy as np, math
from kasteleyn import logZ
# Test exact quadratic-per-class hypothesis: within each mod-4 class, logZ = F0 n^2 + F1 n + C_r EXACTLY (res ~1e-25).
# Verify with 3-point determination: for class r, use 3 values to predict a 4th.
import itertools
for a in [0.3, 0.7, 0.9, 0.2]:
    print(f"--- a={a} ---")
    for r in [0,1,2,3]:
        sub=[n for n in range(1,29) if n%4==r]
        n1,n2,n3=sub[0],sub[1],sub[2]
        y=np.array([logZ(n,a) for n in (n1,n2,n3)])
        A=np.vstack([[n1*n1,n1,1],[n2*n2,n2,1],[n3*n3,n3,1]])
        coef=np.linalg.solve(A,y)
        for n in sub[3:]:
            pred=coef[0]*n*n+coef[1]*n+coef[2]
            err=pred-logZ(n,a)
            if abs(err)>1e-9:
                print(f"  r={r} FAIL at n={n} err={err:.3e}")
                break
        else:
            print(f"  r={r} EXACT through n={sub[-1]}: F0={coef[0]:.10f} F1={coef[1]:.10f} C={coef[2]:.10f}")
