import itertools
pairs=[
[(0,1),(2,3),(4,5)],
[(0,1),(2,4),(3,5)],
[(0,1),(2,5),(3,4)],
[(0,2),(1,3),(4,5)],
[(0,2),(1,4),(3,5)],
[(0,2),(1,5),(3,4)],
[(0,3),(1,2),(4,5)],
[(0,3),(1,4),(2,5)],
[(0,3),(1,5),(2,4)],
[(0,4),(1,2),(3,5)],
[(0,4),(1,3),(2,5)],
[(0,4),(1,5),(2,3)],
[(0,5),(1,2),(3,4)],
[(0,5),(1,3),(2,4)],
[(0,5),(1,4),(2,3)],
]
mc=[0.0380653,0.0062495,-0.0149882,0.0063749,-0.0006182,0.0017831,-0.0145273,-0.0001701,-0.0002869,0.0018824,-0.0002872,0.0009466,-0.0052902,-0.0007602,0.0019903]
def compat(w,P):
    return all(w[i]==w[j] for (i,j) in P)
# true-ish e6
import math
s2=sum(sum(v for v,P in zip(mc,pairs) if compat(w,P))**2 for w in itertools.product([0,1],repeat=6))
print("e6^2",s2,"e6",math.sqrt(s2))
# interval propagation with half-width w per V
for w in [0.0005,0.001,0.002,0.003,0.005]:
    lo=[v-w for v in mc]; hi=[v+w for v in mc]
    e2lo=0.0; e2hi=0.0
    for wd in itertools.product([0,1],repeat=6):
        idx=[i for i,P in enumerate(pairs) if compat(wd,P)]
        Slo=sum(lo[i] for i in idx); Shi=sum(hi[i] for i in idx)
        # S interval [Slo,Shi]
        sq_lo = 0.0 if Slo<=0<=Shi else min(Slo**2,Shi**2)
        sq_hi = max(Slo**2,Shi**2)
        e2lo+=sq_lo; e2hi+=sq_hi
    print(f"w={w}: e6 in [{math.sqrt(e2lo):.4f},{math.sqrt(e2hi):.4f}], f3hi={math.sqrt(e2hi)*(6**0.75):.4f}")
# level4
A=0.15885245; B=-0.0625; C=0.02864755
V4=[A,C,B]; P4=[[(0,1),(2,3)],[(0,2),(1,3)],[(0,3),(1,2)]]
def c4(w,P): return all(w[i]==w[j] for (i,j) in P)
s4=sum(sum(v for v,P in zip(V4,P4) if c4(w,P))**2 for w in itertools.product([0,1],repeat=4))
print("e4^2",s4,"e4",math.sqrt(s4))
for w in [0.0005,0.001,0.002,0.005]:
    lo=[v-w for v in V4]; hi=[v+w for v in V4]
    e2lo=e2hi=0
    for wd in itertools.product([0,1],repeat=4):
        idx=[i for i,P in enumerate(P4) if c4(wd,P)]
        Slo=sum(lo[i] for i in idx); Shi=sum(hi[i] for i in idx)
        sq_lo=0.0 if Slo<=0<=Shi else min(Slo**2,Shi**2)
        sq_hi=max(Slo**2,Shi**2)
        e2lo+=sq_lo; e2hi+=sq_hi
    print(f"w={w}: e4 in [{math.sqrt(e2lo):.4f},{math.sqrt(e2hi):.4f}], f2lo={math.sqrt(e2lo)*(2**0.75):.4f} f2hi={math.sqrt(e2hi)*(2**0.75):.4f}")
