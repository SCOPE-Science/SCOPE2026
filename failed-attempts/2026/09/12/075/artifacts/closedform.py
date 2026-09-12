"""Identify closed forms of F0, F1, C_r as functions of a.
Data: for each a: F0, F1, C1, C3 (C0=C2=0).
Observe ratios like 0.427716 = ? For a=0.3: ratio_even = e^{8F0}?
"""
import numpy as np, math
from kasteleyn import logZ
data={}
for a in [0.2,0.3,0.5,0.7,0.9]:
    lz={n: logZ(n,a) for n in range(1,13)}
    # F0,F1 from class 0 (n=4,8,12)
    A=np.array([[16,4,1],[64,8,1],[144,12,1]])
    y=np.array([lz[4],lz[8],lz[12]])
    F0,F1,C0=np.linalg.solve(A,y)
    # C1 from n=1: C1 = lz1 - F0 - F1; C3 from n=3
    C1=lz[1]-F0-F1; C3=lz[3]-9*F0-3*F1
    data[a]=(F0,F1,C0,C1,C3)
    print(f"a={a}: F0={F0:.12f} F1={F1:.12f} C0={C0:.12f} C1={C1:.12f} C3={C3:.12f}")
print()
for a,(F0,F1,C0,C1,C3) in data.items():
    print(f"a={a}: e^{{8F0}}={math.exp(8*F0):.12f}  e^{{4F1}}={math.exp(4*F1):.12f} e^C1={math.exp(C1):.12f} e^C3={math.exp(C3):.12f}")
print()
# guess: e^{8F0} rational in a? e.g. a=0.3: 0.427716 = ? 0.3=x: try (1+x^2+...)? 
# a=0.5: e^{8F0} = e^{2 ln(5/4)} = (5/4)^2 = 1.5625. check
for a in [0.2,0.3,0.5,0.7,0.9]:
    from fractions import Fraction
    r=math.exp(8*data[a][0])
    print(f"a={a} e^8F0={r:.12f}  (1+a^2)^2/4a^2?={((1+a*a)**2/(4*a*a)):.6f}  4a^2/(1+a^2)^2?={(4*a*a/(1+a*a)**2):.12f}")
