"""Exhaustive float pre-screen for S_{8,4} endpoint hitting time.
Reduced enumeration: H depends only on rows 0..6 (4*6^6 = 186624 solves).
Full count with q7 multiplicity: 746496. Aperiodicity filter applied post-hoc.
"""
import time, numpy as np

p0_opts = [0.25, 0.5, 0.75, 1.0]
interior = [(0.25,0.25,0.5),(0.25,0.5,0.25),(0.25,0.75,0.0),
            (0.5,0.25,0.25),(0.5,0.5,0.0),(0.75,0.25,0.0)]

t0=time.time()
maxH=-1.0
arg=None
# store all H values for top-5 distinct analysis (186624 floats)
import array
Hs = np.empty(4*6**6, dtype=np.float64)
idx=0
for i0 in range(4):
    p0=p0_opts[i0]; r0=1-p0
    for i1 in range(6):
        for i2 in range(6):
            for i3 in range(6):
                for i4 in range(6):
                    for i5 in range(6):
                        for i6 in range(6):
                            js=(i1,i2,i3,i4,i5,i6)
                            ps=[p0]+[interior[j][0] for j in js]
                            qs=[0]+[interior[j][1] for j in js]
                            rs=[r0]+[interior[j][2] for j in js]
                            A=np.zeros((7,7))
                            for r in range(7):
                                A[r,r]=1-rs[r]
                                if r<6: A[r,r+1]=-ps[r]
                                if r>0: A[r,r-1]=-qs[r]
                            h=np.linalg.solve(A,np.ones(7))
                            H=float(h[0])
                            Hs[idx]=H; idx+=1
                            if H>maxH+1e-9:
                                maxH=H; arg=(i0,)+js
print(f"screens {idx} time {time.time()-t0:.2f}s maxH={maxH} arg={arg}")
# distinct top values
uniq=np.unique(np.round(Hs,6))
top=np.sort(uniq)[-10:]
print("top10 distinct (rounded):", top)
# full-precision distinct top-5 via sorted unique of exact? float approx:
uniq2=np.unique(Hs)
print("num distinct float values:", len(uniq2))
print("top5 float distinct:", np.sort(uniq2)[-5:])
