#!/usr/bin/env python3
"""Exact symbolic checks for a three-habitat stochastic-growth allocation theorem.
Scientific statement and assumptions are in RESULT.md. Requires SymPy >= 1.10.
"""
import itertools
import sympy as sp
v=sp.symbols('v', positive=True)
S=sp.Matrix([[2,-1,-2],[-1,2,2],[-2,2,3]])
r=sp.Matrix([2,1,0])
xs=[
    sp.Matrix([1,0,0]),
    sp.Matrix([sp.Rational(1,2)+1/(6*v),sp.Rational(1,2)-1/(6*v),0]),
    sp.Matrix([sp.Rational(3,5),(5-v)/(5*v),(3*v-5)/(5*v)]),
    sp.Matrix([(5*v+2)/(9*v),0,(4*v-2)/(9*v)]),
]
assert [S[:i,:i].det() for i in range(1,4)]==[2,3,1]
assert S==S.T
# Exact stationary and inactive KKT inequalities, stated as elementary factors.
for i,x in enumerate(xs):
    assert sp.simplify(sum(x)-1)==0
    g=r-v*S*x
    pos=[k for k in range(3) if x[k]!=0]
    for k in pos[1:]:
        assert sp.simplify(g[k]-g[pos[0]])==0,(i,k)
    print('REGIME',i,'x=',tuple(x),'inactive_differences=',
          [(j,sp.factor(g[j]-g[pos[0]])) for j in range(3) if j not in pos])
    print('OBJECTIVE',i,sp.factor(r.dot(x)-v/2*(x.T*S*x)[0]))
# Exact continuous joins
for i,b in enumerate([sp.Rational(1,3),sp.Rational(5,3),sp.Integer(5)]):
    assert xs[i].subs(v,b)==xs[i+1].subs(v,b)
# Numerically distinct algebraic optimization audit across all active-set subsets using exact rational grid
checks=0
for numerator in range(1,151):
    t=sp.Rational(numerator,24)
    k=0 if t<=sp.Rational(1,3) else 1 if t<=sp.Rational(5,3) else 2 if t<=5 else 3
    x=xs[k].subs(v,t)
    assert all(0<=xx<=1 for xx in x)
    g=r-t*S*x
    active=[j for j in range(3) if x[j]>0]
    assert all(g[j]==g[active[0]] for j in active)
    assert all(g[j]<=g[active[0]] for j in range(3) if j not in active)
    # Independent objective comparison against ALL feasible support stationary KKT candidates.
    cand=[]
    for sub in itertools.chain.from_iterable(itertools.combinations(range(3),k) for k in [1,2,3]):
        klen=len(sub)
        C=sp.Matrix([[t*S[i,j] for j in sub]+[1] for i in sub]+[[1]*klen+[0]])
        rhs=sp.Matrix([r[i] for i in sub]+[1])
        solution=C.inv()*rhs
        z=sp.zeros(3,1)
        for m,idx in enumerate(sub):z[idx]=solution[m]
        if all(z[j]>=0 for j in range(3)):
            cand.append(r.dot(z)-t/2*(z.T*S*z)[0])
    value=r.dot(x)-t/2*(x.T*S*x)[0]
    assert all(value>=other for other in cand)
    checks+=1
assert checks==150
assert sp.simplify(r.dot(xs[3])-v/2*(xs[3].T*S*xs[3])[0]+(v*v-10*v-2)/(9*v))==0
assert (r.dot(xs[3])-v/2*(xs[3].T*S*xs[3])[0]).subs(v,6)==sp.Rational(13,27)
assert list(r-6*sp.Matrix([S[i,i]/2 for i in range(3)]))==[-4,-5,-9]
assert [sp.simplify(z.subs(v,6)) for z in xs[3]]==[sp.Rational(16,27),0,sp.Rational(11,27)]
print('PASS exact covariance principal minors, 4 KKT regimes, 3 boundary joins, 150 exact full active-set comparisons, and sink-rescue witness')
