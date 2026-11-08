"""Reproduce the exact second-moment identities for uniform singleton
residual-tracking randomized Kaczmarz on equal-row scalar least squares.
Needs Python 3.10+ and SymPy; finite checks are supplementary, not a
substitute for the analytic positive-map spectral argument.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import math
import sympy as sp

checks = 0

def check(ok, description):
    global checks
    if not bool(ok):
        raise AssertionError(description)
    checks += 1

def moment_matrix(m, a):
    c = 1 - m*a
    return (
      (c*c, 0, 0, m*m*a*a),
      (c/F(m), c*F(m-1,m), 0, -a),
      (F(1,m*m), F(2*(m-1),m*m), F((m-1)**2,m*m), F(1,m*m)),
      (F(m-1,m*m), F(-2*(m-1),m*m), F(m-1,m*m), F(m*m-m-1,m*m))
    )

def matvec(M, x):
    return tuple(sum(a*b for a,b in zip(row,x)) for row in M)

def obs(e, s):
    m = len(s)
    t = sum(s)/m
    v = sum(q*q for q in s)/m-t*t
    return (e*e,e*t,t*t,v)

def step(e,s,i,a):
    m=len(s)
    t=sum(s)/m
    ep=(1-m*a)*e +m*a*(s[i]-t)
    sp=list(s)
    sp[i]=e
    return (ep,tuple(sp))

m,a,z=sp.symbols('m a z', positive=True)
c=1-m*a
M=sp.Matrix([
    [c*c,0,0,m*m*a*a],
    [c/m,c*(m-1)/m,0,-a],
    [1/m**2,2*(m-1)/m**2,(m-1)**2/m**2,1/m**2],
    [(m-1)/m**2,-2*(m-1)/m**2,(m-1)/m**2,(m*m-m-1)/m**2],
])
P=m*(m-1)*(2*m-1)*a*a-(m-2)*(2*m-1)*a-2
check(sp.simplify((sp.eye(4)-M).det()+2*a*P/m**2)==0, 'det(I-M) identity')
char0=(z-1)*(m*z-m+1)**2*(m*z-m+2)/m**3
poly=sp.det(z*sp.eye(4)-M)
check(sp.simplify(poly.subs(a,0)-char0)==0,'char polynomial at zero')
check(sp.simplify(-sp.diff(poly,a).subs({a:0,z:1})/sp.diff(poly,z).subs({a:0,z:1})+2*m)==0,'root derivative at zero')

for n in range(2,21):
    an=(n-2+math.sqrt((n-2)**2+8*n*(n-1)/(2*n-1)))/(2*n*(n-1))
    check(1/n < an <2/n, f'frontier between gradient scales for m={n}')
    check(abs((n*(n-1)*(2*n-1)*an*an-(n-2)*(2*n-1)*an-2))<1e-9,'frontier root')
    for factor,stable in ((.80,True),(1.20,False)):
        T=sp.Matrix(moment_matrix(n,sp.Float(an*factor)))
        vals=[complex(v) for v in T.eigenvals(multiple=True)]
        radius=max(abs(v) for v in vals)
        check((radius<1) if stable else (radius>1),f'spectral side m={n}, {factor}')

# Every conditional moment recurrence is an exact rational identity, also
# for nonexchangeable initial reference tables.
for n in (2,3,4,5,6):
    alphas=(F(1,n+1),F(2,3*n),F(1,2*n))
    seeds=[
        (F(1),tuple(F(1) for _ in range(n))),
        (F(3,2),tuple(F(j-2) for j in range(n))),
        (F(-1,3),tuple(F((-1)**j*(j+1),5) for j in range(n))),
    ]
    for alpha in alphas:
        mat=moment_matrix(n,alpha)
        for e,s in seeds:
            expected=tuple(sum(obs(*step(e,s,i,alpha))[q] for i in range(n))/n for q in range(4))
            actual=matvec(mat,obs(e,s))
            for q in range(4):
                check(expected[q]==actual[q],f'moment closure m={n}, alpha={alpha}, q={q}')

# Exhaustive enumeration of a finite number of sample-index words checks
# the exact iterate-vs-moment formulas, not any infinite-time assertion.
for n,depth in ((2,8),(3,6),(4,5)):
    alpha=F(1,n+1)
    Mnum=moment_matrix(n,alpha)
    states={(F(1),tuple(F(1) for _ in range(n))):F(1)}
    target=obs(*next(iter(states)))
    for k in range(depth+1):
        measured=[F(0)]*4
        for (e,s),p in states.items():
            o=obs(e,s)
            for q in range(4):
                measured[q]+=p*o[q]
        for q in range(4):
            check(measured[q]==target[q],f'finite-word moment m={n}, k={k}, q={q}')
        if k<depth:
            new=defaultdict(lambda:F(0))
            for (e,s),p in states.items():
                for i in range(n):
                    new[step(e,s,i,alpha)]+=p/n
            states=new
            target=matvec(Mnum,target)

# Directly check the source's recommended step and exact threshold comparison.
for n in (2,3,4,8,16,32,64):
    alpha=(n-2+math.sqrt((n-2)**2+8*n*(n-1)/(2*n-1)))/(2*n*(n-1))
    recommended=1/(n*(n+4))
    check(recommended<alpha, f'source sufficient step safely below frontier m={n}')

print(f'PASS: {checks} symbolic/exact-rational/spectral assertions')
