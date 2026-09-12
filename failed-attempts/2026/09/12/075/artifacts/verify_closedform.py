"""Reproducible verification: exact closed form + 4-step factor ( Sections 2-3 of DRAFT ).
Reads kasteleyn.py from same directory. Exits nonzero on failure.
"""
import math, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kasteleyn import logZ
def F0(a): return 0.25*math.log(2*a*(1+a*a))
def F1(a): return 0.5*math.log(2*a)
def C(a,r):
    if r in (0,2): return 0.0
    if r==3: return F1(a)-F0(a)
    return F1(a)-F0(a)+math.log(a)
def logK(n,a):
    return (n-1)*math.log(4*a*a)+(2*n-4)*math.log(1+a*a)
worst=0.0
for a in [0.2,0.3,0.5,0.7,0.9,1.3]:
    lz={n:logZ(n,a) for n in range(0,13)}
    for n in range(1,13):
        e=abs(lz[n]-(F0(a)*n*n+F1(a)*n+C(a,n%4))); worst=max(worst,e)
        assert e<1e-9,(a,n,e)
    for n in range(4,13):
        e=abs(logK(n,a)-(lz[n]-lz[n-4])); worst=max(worst,e)
        assert e<1e-9,(a,n,e)
print(f"closed form + 4-step factor verified; worst err={worst:.2e}")
