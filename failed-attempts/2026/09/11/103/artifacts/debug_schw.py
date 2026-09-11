"""Validate shooter+area on exact Schwarzschild puncture (u=0, S=0).
Expect: outermost MOTS h=0.5 sphere, A=16*pi. J=0 so D=inf.
"""
import numpy as np, math, sys
sys.path.insert(0, "output/artifacts")
from puncture_mots import shoot, mots_area, find_mots

def P(r, t): return 1.0 + 1.0/(2.0*max(r,1e-9))
def Pr(r, t): return -0.5/(max(r,1e-9)**2)
def Pt(r, t): return 0.0

hs0, peq, roots = find_mots(P, Pr, Pt)
print("roots:", roots)
print("scan:", list(zip(np.round(hs0,3), np.round(peq,4))))
for h0 in roots:
    h,p,ts,hsa,psa = shoot(h0,P,Pr,Pt,nstp=4000)
    A = mots_area(ts,hsa,psa,P)
    print(f"h0={h0:.5f} peq={p:.3e} A={A:.6f} 16pi={16*math.pi:.6f}")
    print("h range:", hsa.min(), hsa.max())
