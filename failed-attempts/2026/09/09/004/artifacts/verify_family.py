# FINAL certificate: frozen braid-twist family w_m = [1,1,1,-2] + [-1]^{2m} + [-1,-1,-1,-2], n=3.
# Certifies for m=0..4: knot closure, Alexander (exact Laurent), degdiff, genus lower bound 2g>=span, det, Fox-Milnor square test.
import sys; sys.path.insert(0,'output/artifacts')
import sympy as sp
from burau import alexander, perm
t=sp.Symbol('t')
w0=[1,1,1,-2,-1,-1,-1,-2]
def canon(w,n=3):
    # canonical Laurent representative: clear to polynomial with min-degree 0 then fix sign D(1)>0
    d=sp.expand(alexander(w,n))
    e=sp.expand(d*t**24)
    p=sp.Poly(e,t); exps=sorted(m[0]-24 for m in p.monoms() if p.coeff_monomial(m)!=0)
    lo,hi=exps[0],exps[-1]
    q=sp.expand(d*t**(-lo))
    if q.subs(t,1)<0: q=-q
    return sp.expand(q), lo, hi
import math
print("m,c,knot,span,lo,hi,glow,det,square?,D(1),Delta_canon")
for m in range(5):
    w=w0[:4]+[-1]*(2*m)+w0[4:]
    p=perm(w,3)
    v=0;seen=set()
    for _ in range(3): seen.add(v); v=p[v]
    knot=len(seen)==3
    q,lo,hi=canon(w)
    span=hi-lo
    det=int(round(abs(complex(sp.expand(alexander(w,3)).subs(t,-1)))))
    r=int(math.isqrt(det)); sq=(r*r==det)
    print(f"{m},{len(w)},{knot},{span},{lo},{hi},{(span+1)//2 if span%2 else span//2},{det},{sq},{q.subs(t,1)},{q}")
