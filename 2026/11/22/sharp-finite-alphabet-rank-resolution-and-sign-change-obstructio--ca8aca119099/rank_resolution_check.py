"""Exact arithmetic checks of interval-moment rank laws and their sharp thresholds.
Run: python rank_resolution_check.py
Requires SymPy. All checks use exact rational arithmetic.
"""
from fractions import Fraction
from math import comb, factorial
from itertools import product
from sympy import Matrix, Rational
import json

checks = 0

def require(assertion):
    global checks
    if not assertion:
        raise AssertionError('exact check failed')
    checks += 1

def matrix(p,m):
    s = Rational(0)
    boundaries = [s]
    for a in p:
        s += a
        boundaries.append(s)
    return Matrix([[(boundaries[j+1]**(k+1)-boundaries[j]**(k+1)) / ((k+1)*p[j])
                    for j in range(len(p))] for k in range(m+1)])

def probabilities(p,q,m):
    # The conditional rank probability is a Bernstein-polynomial average.
    A = matrix(p,m)
    moments = A*Matrix(q)
    out=[]
    for r in range(m+1):
        value=Rational(0)
        for t in range(m-r+1):
            value += comb(m,r)*(-1)**t*comb(m-r,t)*moments[r+t]
        out.append(value)
    return out

# Exact ranks, including irregular positive masses.
for K in range(2,11):
    for raw in (list(range(1,K+1)),list(range(K,0,-1)), [1]*K):
        d=sum(raw)
        p=[Rational(x,d) for x in raw]
        for m in range(1,K+2):
            require(matrix(p,m).rank()==min(K,m+1))
        require(probabilities(p,p,K-1)==[Rational(1,K)]*K)

# Sharp alternate-sign example and exact first nonzero rank response.
for K in range(3,11):
    s=K-1
    p=[Rational(1,K)]*K
    eps=Rational(1,2*K*max(comb(s,j) for j in range(K)))
    q=[p[j]+eps*(-1)**j*comb(s,j) for j in range(K)]
    require(all(v>0 for v in q) and sum(q)==1)
    for m in range(1,s):
        require(probabilities(p,q,m)==[Rational(1,m+1)]*(m+1))
    at_first=probabilities(p,q,s)
    expected=[Rational(1,K)+eps*(-1)**r*factorial(s)*comb(s,r)/K**s
              for r in range(K)]
    require(at_first==expected)
    pearson=sum(K*(v-Rational(1,K))**2 for v in at_first)
    require(pearson==eps**2*factorial(s)**2*Rational(K,K**(2*s))*comb(2*s,s))

# Exhaustive low-dimensional implication: a null-matching nonzero
# perturbation cannot have <= m sign changes.
def sign_changes(values):
    nz=[1 if z>0 else -1 for z in values if z]
    return sum(nz[i]!=nz[i-1] for i in range(1,len(nz)))
for K in range(3,7):
    p=[Rational(1,K)]*K
    for h_head in product(range(-2,3),repeat=K-1):
        h=list(h_head)+[-sum(h_head)]
        if not any(h) or max(abs(z) for z in h)>2:
            continue
        eps=Rational(1,10*K)
        q=[p[j]+eps*h[j] for j in range(K)]
        require(all(v>0 for v in q))
        sc=sign_changes(h)
        for m in range(max(1,sc),K):
            require(probabilities(p,q,m)!=[Rational(1,m+1)]*(m+1))

# Arbitrary positive nulls: alternating full-minor null vector is sharp.
for K in range(3,8):
    raw=[j*j+1 for j in range(1,K+1)]
    p=[Rational(x,sum(raw)) for x in raw]
    for m in range(1,K-1):
        A=matrix(p,m)[:,:m+2]
        h=[(-1)**j*A[:,[k for k in range(m+2) if k!=j]].det() for j in range(m+2)]
        require(all(h[j]*(-1)**j>0 for j in range(m+2)))
        require(A*Matrix(h)==Matrix([0]*(m+1)))
        full=h+[Rational(0)]*(K-m-2)
        require(sign_changes(full)==m+1)
        eps=Rational(1,100)*(min(p)/max(abs(z) for z in full))
        q=[p[j]+eps*full[j] for j in range(K)]
        require(all(z>0 for z in q) and sum(q)==1)
        require(probabilities(p,q,m)==[Rational(1,m+1)]*(m+1))

print(json.dumps({'status':'passed','exact_assertions':checks,
                  'scope':'ranks, alternating blind alternatives, first visible signal, sign-change obstruction',
                  'arithmetic':'symbolic rational','K_checked':'2..10'}))
