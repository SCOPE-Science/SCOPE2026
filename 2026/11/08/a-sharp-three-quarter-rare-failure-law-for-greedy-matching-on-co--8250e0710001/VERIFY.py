"""Reproduce finite probability checks for the cocktail-party greedy matching result.
Run with Python 3.9+: python VERIFY.py. No third-party dependencies.
"""
from fractions import Fraction
from functools import lru_cache
from math import comb, log

assertions=0
def check(cond, msg):
    global assertions
    assertions+=1
    if not cond: raise AssertionError(msg)

@lru_cache(None)
def reduced_failure(m,f):
    if m==1: return Fraction(f,1)
    s=2*(m-f)
    D=m*(2*m-1)-f
    assert D>0
    return ((comb(s,2)*reduced_failure(m-1,f) if s>=2 else 0)
            +(2*f*s*reduced_failure(m-1,f-1) if f and s else 0)
            +(2*f*(f-1)*reduced_failure(m-1,f-2) if f>=2 else 0))/D

@lru_cache(None)
def graph_failure(mask,n):
    vertices=[v for v in range(2*n) if mask>>v&1]
    if len(vertices)==2:
        u,v=vertices
        return Fraction(int(u//2==v//2),1)
    edges=[(u,v) for i,u in enumerate(vertices) for v in vertices[i+1:] if u//2!=v//2]
    return sum((graph_failure(mask^(1<<u)^(1<<v),n) for u,v in edges),Fraction(0,1))/len(edges)

# Independent labeled-graph computation versus the symmetry recursion.
for n in range(2,6):
    val=graph_failure((1<<(2*n))-1,n)
    check(val==reduced_failure(n,n),f'graph comparison failed: n={n}')

# Independently check exact transition counts, first two factorial moment formulas.
for m in range(2,40):
    for f in range(m+1):
        s=2*(m-f); D=m*(2*m-1)-f
        check(comb(s,2)+2*f*s+2*f*(f-1)==D, f'edge count {m} {f}')
        if f>=1:
            singleton_survival=comb(2*m-2,2)-(f-1)
            check(singleton_survival==D-4*(m-1),f'one pair {m} {f}')
        if f>=2:
            double_survival=comb(2*m-4,2)-(f-2)
            check(double_survival>=0,f'two pair count {m} {f}')
            q=Fraction(double_survival,D)
            q_max=Fraction(comb(2*m-4,2),m*(2*m-1)-2)
            check(q<=q_max, f'two pair monotonicity {m} {f}')
            check(q_max<=Fraction((m-1)**4,m**4),f'comparison power four {m} {f}')

# Direct exact distribution recursion for the reduced chain; check probability mass.
@lru_cache(None)
def state_distribution(n):
    dist={n:Fraction(1)}
    for m in range(n,1,-1):
        new={}
        for f, mass in dist.items():
            s=2*(m-f); D=m*(2*m-1)-f
            for next_f,weight in ((f,comb(s,2)),(f-1,2*f*s),(f-2,2*f*(f-1))):
                if weight:
                    new[next_f]=new.get(next_f,Fraction())+mass*Fraction(weight,D)
        check(sum(new.values())==1,f'probability mass {n} {m}')
        dist=new
    return dist
for n in range(2,29):
    dist=state_distribution(n)
    check(dist.get(1,Fraction())==reduced_failure(n,n),f'moment matching {n}')
    p=reduced_failure(n,n)
    bound=Fraction(3*n,4*n*n-1)
    check(p<=bound,f'upper bound {n}')
    # Harmonic-number explicit error estimate.
    H=sum((Fraction(1,j) for j in range(1,n)),Fraction(0))
    check(bound-p<=12*H/(n*n),f'lower bound {n}')
    # n*f1 limit is asymptotic; never use this as a proof.

@lru_cache(None)
def float_failure(m,f):
    if m==1: return float(f)
    ss=2*(m-f);den=m*(2*m-1)-f
    return ((ss*(ss-1)//2*float_failure(m-1,f) if ss>=2 else 0.0)
        +(2*f*ss*float_failure(m-1,f-1) if f and ss else 0.0)
        +(2*f*(f-1)*float_failure(m-1,f-2) if f>=2 else 0.0))/den
for n in (40,80,160,320,640):
    x=float_failure(n,n)
    check(abs(n*x-0.75)<12*(1+log(n))/n, f'asymptotic bound {n}')

print('VERIFY_OK',assertions,'checks')
for n in range(2,9): print(n,str(reduced_failure(n,n)))
