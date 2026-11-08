#!/usr/bin/env python3
"""Exact finite-state verification of an SIS single-vertex-vaccination cutoff.
Requires Python 3.10+ and SymPy 1.12+. Run: python verify_sis.py
"""
from itertools import combinations
import sympy as sp

L=sp.symbols('lambda', positive=True)
ORIGINAL=((0,1),(0,2),(0,4),(1,2),(1,3),(2,3))
PATH=((0,1),(1,2),(2,3))
TRIANGLE_ISOLATED=((0,1),(0,2),(1,2))

def burden(n, edges, rate):
    """Solve Poisson equations Q f = -|I| for all nonempty infected sets."""
    states=range(1, 1<<n)
    position={s:i for i,s in enumerate(states)}
    a=sp.zeros(len(position)); reward=sp.zeros(len(position),1)
    for i,s in enumerate(states):
        reward[i]=s.bit_count()
        for v in range(n):
            t=s^(1<<v)
            if s&(1<<v):
                a[i,i]+=1
                if t: a[i,position[t]]-=1
            else:
                k=sum((u==v and bool(s&(1<<w))) or (w==v and bool(s&(1<<u))) for u,w in edges)
                if k:
                    a[i,i]+=rate*k
                    a[i,position[t]]-=rate*k
    result=a.inv()*reward
    return sp.cancel(sum(result[position[1<<j]] for j in range(n))/n)

def residual(v):
    remains=[w for w in range(5) if w!=v]
    index={w:i for i,w in enumerate(remains)}
    return tuple(tuple(sorted((index[u],index[w]))) for u,w in ORIGINAL if u!=v and w!=v)

N_P=48*L**8+328*L**7+1075*L**6+2250*L**5+3233*L**4+3196*L**3+2088*L**2+816*L+144
D_P=2*(4*L**2+9*L+6)*(12*L**3+31*L**2+32*L+12)
Q=48*L**5+136*L**4+99*L**3-78*L**2-156*L-72
DELTA=L**2*(L+1)*Q/D_P
T=(3*L**2+3*L+2)/2
P=N_P/D_P

assert sp.cancel(burden(4, PATH, L)-P)==0, 'Path polynomial differs'
assert sp.cancel(burden(4, TRIANGLE_ISOLATED,L)-T)==0, 'Triangle polynomial differs'
assert sp.cancel(P-T-DELTA)==0, 'Difference factorization differs'
assert [int(x) for x in sp.Poly(Q,L).all_coeffs()]==[48,136,99,-78,-156,-72]
assert sp.sign(Q.subs(L,0))<0
assert sp.Poly(Q,L).count_roots(0,sp.oo)==1, 'Positive root not unique'
positive=[float(sp.re(r)) for r in sp.nroots(Q,maxsteps=200) if abs(float(sp.im(r)))<1e-10 and float(sp.re(r))>0]
assert len(positive)==1 and abs(positive[0]-1.02829796682632)<1e-10
print('Exact path, triangle, and factorization identities: PASS')
print('Unique positive root:',positive[0])

# Cross-check the optimal vertex at rational rates with a fresh direct CTMC solve.
for rate in (sp.Rational(1,4),sp.Rational(1,2),sp.Rational(1),sp.Rational(3,2),sp.Rational(2)):
    values=[burden(4,residual(v),rate) for v in range(5)]
    best=min(values)
    winners={v for v,x in enumerate(values) if x==best}
    expected={1,2} if rate<1 else ({0} if rate>1 else {1,2})
    # 1 is below threshold; rates 3/2,2 are above threshold
    assert winners==expected,(rate,winners,values)
    print('rate=',rate,' winners=',sorted(winners),' excess=',[sp.factor(x-best) for x in values])
print('Five exact-rational vaccine-optimization tests: PASS')

# Structural check: each vaccine class is one of the two indicated residual graphs,
# or contains a triangle on three of its four vertices.

def isomorphic(a,b):
    from itertools import permutations
    return any({tuple(sorted((p[u],p[v]))) for u,v in a}==set(b) for p in permutations(range(4)))
assert isomorphic(residual(0),TRIANGLE_ISOLATED)
assert isomorphic(residual(1),PATH) and isomorphic(residual(2),PATH)
for v in (3,4):
    es=set(residual(v))
    assert any(all(tuple(sorted(e)) in es for e in combinations(three,2)) for three in combinations(range(4),3))
print('Residual graph classification and containment checks: PASS')
print('ALL TESTS PASSED')
