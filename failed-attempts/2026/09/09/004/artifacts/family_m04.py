import sys; sys.path.insert(0,'output/artifacts')
import sympy as sp
from burau import alexander, perm
t=sp.Symbol('t')
w0=[1,1,1,-2,-1,-1,-1,-2]
def degdiff(d):
    e=sp.expand(d)
    # get exponents including negative: multiply by t^24 then find min/max nonzero
    exps=[]
    p=sp.Poly(sp.expand(e*t**24),t)
    for m in p.monoms():
        if p.coeff_monomial(m)!=0: exps.append(m[0]-24)
    return (max(exps)-min(exps)), min(exps), max(exps)
for m in range(5):
    w=w0[:4]+[-1]*(2*m)+w0[4:]
    p=perm(w,3)
    v=0;seen=set()
    for _ in range(3): seen.add(v); v=p[v]
    knot=len(seen)==3
    d=sp.expand(alexander(w,3))
    dd,lo,hi=degdiff(d)
    det=abs(complex(d.subs(t,-1)))
    c=len(w)
    gcan=(1+c-3)/2
    print(f"m={m} c={c} knot={knot} degdiff={dd} [{lo},{hi}] det={det:.1f} gcan={gcan} D={d}")
