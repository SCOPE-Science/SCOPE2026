"""Exact certificate for the three-colour antiprism Potts ground-state formula.

Usage: python verify.py
Requires Python 3 and sympy. Only finite checks are computational;
the proof of the all-size assertion is the rational generating-function
identity derived from a nine-state transfer in the accompanying result.
"""
from collections import defaultdict
from itertools import product
import sympy as sp

x, y, t = sp.symbols('x y t')
pairs = [(a,b) for a in range(3) for b in range(3)]
T = sp.zeros(9)
for row, (a,b) in enumerate(pairs):
    for c in range(3):
        T[row, pairs.index((b,c))] = x ** (int(c==a)+int(c==b)) * y ** int(c==0)

D = sp.Poly((sp.eye(9)-t*T).det(method='domain-ge'), x)
D0, D1, D2 = (sp.expand(D.nth(k)) for k in (0,1,2))
q = t**3*y
assert sp.expand(D0-(1-q)**2)==0
assert sp.expand(D1+2*t**4*y*(y+2)*(1-q))==0
D2_res = sp.Add(*(term for term in sp.Add.make_args(D2)
                if sp.Poly(term,t).degree() % 3 == 2))
assert sp.expand(D2_res - t**2*(2*y+1)*(-1-4*q+4*q**2))==0
R = sp.cancel(D2_res/D0 - sp.Rational(1,2)*(D1/D0)**2)
R_target = t**2*(-(2*y+1)-4*(2*y+1)*q-(2*y**2+4)*q**2)/(1-q)**2
assert sp.cancel(R-R_target)==0


def predicted(N):
    m,r=divmod(N,3)
    if r==0: return 0,{m:6}
    if r==1: return 1,{m:4*N,m+1:2*N}
    return 2,{m:N*(9*m-3),m+1:N*(10*m+2),m+2:N*(2*m-2)}


def dynamic(N):
    # Dynamic min-plus counting, independent of determinant computation.
    counts = {}
    for a,b in pairs:
        D = {(a,b,int(a==0)+int(b==0)):(int(a==b),1)}
        for j in range(2,N):
            new={}
            for (u,v,k),(cost,num) in D.items():
                for c in range(3):
                    key=(v,c,k+int(c==0))
                    val=cost+int(c==u)+int(c==v)
                    previous=new.get(key)
                    if previous is None or val<previous[0]:new[key]=(val,num)
                    elif val==previous[0]:new[key]=(val,previous[1]+num)
            D=new
        for (u,v,k),(cost,num) in D.items():
            val=cost+int(v==a)+int(u==a)+int(v==b)
            old=counts.get(k)
            if old is None or val<old[0]:counts[k]=(val,num)
            elif val==old[0]:counts[k]=(val,old[1]+num)
    best=min(v[0] for v in counts.values())
    return best,{k:num for k,(cost,num) in counts.items() if cost==best}


def exhaustive(N):
    # Completely independent direct configuration enumeration.
    best=10**8
    by_k=defaultdict(int)
    for colors in product(range(3),repeat=N):
        cost=sum(colors[i]==colors[(i+d)%N] for i in range(N) for d in (1,2))
        if cost<best:best=cost;by_k.clear()
        if cost==best:by_k[sum(c==0 for c in colors)]+=1
    return best,dict(by_k)

for N in range(6,35):
    assert dynamic(N)==predicted(N),(N,dynamic(N),predicted(N))
for N in range(6,11):
    assert exhaustive(N)==predicted(N),(N,exhaustive(N),predicted(N))

# Trace coefficient x^0 and x^1 and x^2 are derived in the result from
# -t*d/dt log det(I-tT); this checks that the transfer counts every edge.
for N in range(6,10):
    trace=sp.expand(sp.trace(T**N))
    e,c=predicted(N)
    base=sum(val*y**k for k,val in c.items())
    assert sp.expand(sp.Poly(trace,x).nth(e)-base)==0
    for r in range(e): assert sp.Poly(trace,x).nth(r)==0
print('ALL_EXACT_CHECKS_PASSED')
