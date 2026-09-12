import numpy as np, math
from kasteleyn import logZ

for a in [0.5, 0.3, 0.8]:
    print(f"===== a={a} =====")
    ns = list(range(1, 31))
    lz = np.array([logZ(n, a) for n in ns])
    f = lz / np.array(ns)**2
    for n, v in zip(ns, f):
        print(f"n={n:3d} (1/n^2)logZ={v:.10f}")
    print()
