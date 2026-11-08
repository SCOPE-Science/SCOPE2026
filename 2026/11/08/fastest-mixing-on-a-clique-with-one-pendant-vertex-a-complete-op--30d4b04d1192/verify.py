"""Standalone exact and numerical verification for the clique-with-one-leaf mixing theorem.
Runs with Python 3, sympy and numpy; no external files, network, or research metadata.
"""
from fractions import Fraction as F
from itertools import combinations
import random
import sympy as s
import numpy as np


def parameters(n):
    assert n >= 3
    den = 5*n-4
    return F(3, den), F(2*n-1, den), F(4*n-5, den), F(n+1, den)


def construct(n, edges):
    """Vertex ordering: leaf 0, hub 1, ordinary 2,...,n."""
    p,q,_,_ = parameters(n)
    P = s.zeros(n+1)
    P[0,1]=P[1,0]=s.Rational(q.numerator,q.denominator)
    for i in range(2,n+1):
        P[1,i]=P[i,1]=s.Rational(p.numerator,p.denominator)
    for (i,j),w in edges.items():
        assert 2 <= i < j <= n and w>=0
        P[i,j]=P[j,i]=s.Rational(w.numerator,w.denominator)
    for i in range(n+1):
        P[i,i]=1-sum(P[i,j] for j in range(n+1) if j!=i)
    assert all(P[i,i]>=0 for i in range(n+1))
    return P


def spectral_window(n,edges):
    p,q,t,lam=parameters(n)
    r=n-1
    W=s.zeros(r)
    for (i,j),w in edges.items():
        v=s.Rational(w.numerator,w.denominator)
        W[i-2,j-2]=W[j-2,i-2]=v
    L=s.diag(*[sum(W[i,j] for j in range(r)) for i in range(r)])-W
    # Use a symmetric numerical eigensolver only for randomized comparisons.
    ordinary=sorted(np.linalg.eigvalsh(np.array(L.tolist(),dtype=float)))[1:]
    assert len(ordinary)==n-2
    lo=float(F(n-2,5*n-4));hi=float(F(9*n-12,5*n-4))
    yes=all(e>=lo-1e-10 and e<=hi+1e-10 for e in ordinary)
    return yes,ordinary


def exact_check(n,edges):
    p,q,t,lam=parameters(n)
    P=construct(n,edges)
    v=s.Matrix([2*n-1,n-2]+[-3]*(n-1))
    L=s.eye(n+1)-P
    assert sum(v)==0
    assert s.expand((v.T*v)[0])==(n+1)*(5*n-4)
    assert L*v==s.Rational(lam.numerator,lam.denominator)*v
    assert P*s.ones(n+1,1)==s.ones(n+1,1)
    eigen=np.linalg.eigvalsh(np.array(P.tolist(),dtype=float))
    assert len(eigen)==n+1 and abs(eigen[-1]-1)<1e-10
    actual=max(abs(e) for e in eigen[:-1])
    yes,_=spectral_window(n,edges)
    assert (actual <= float(t)+1e-9)==yes
    if yes: assert abs(actual-float(t))<1e-9
    return actual


def test():
    n=s.symbols('n',positive=True,integer=True)
    den=5*n-4
    p=s.Rational(3,1)/den; q=(2*n-1)/den; lam=(n+1)/den
    # Three-coordinate quotient Laplacian: polynomial avoids radicals.
    T=s.Matrix([[q,-q,0],[-q,q+(n-1)*p,-(n-1)*p],[0,-p,p]])
    x=s.symbols('x')
    assert s.simplify(T.charpoly(x).as_expr()-x*(x-lam)*(x-3*(2*n-1)/den))==0
    assert s.simplify((n-1)*p+q)==1
    assert s.simplify(1-lam-(4*n-5)/den)==0
    assert s.simplify((1-p)-(n-2)/den-(4*n-5)/den)==0
    assert s.simplify((9*n-12)/den-(1-p)-(4*n-5)/den)==0
    count=5
    for k in range(3,14):
        pp,qq,t,ll=parameters(k)
        uniform=F(1,1)-pp
        base={(i,j): uniform/F(k-1,1) for i,j in combinations(range(2,k+1),2)}
        exact_check(k,base);count+=1
        P=construct(k,base)
        vec=s.Matrix([2*k-1,k-2]+[-3]*(k-1))
        assert (vec.T*(s.eye(k+1)-P)*vec)[0]==(k+1)**2
        count+=1
    # Exact rational sample of the full non-invariant family.
    rng=random.Random(7319)
    for k in range(3,8):
        pp,qq,t,ll=parameters(k)
        for rep in range(8):
            choices={}
            for i,j in combinations(range(2,k+1),2):
                choices[(i,j)]=F(rng.randint(0,9),10*(k-2))
            maxdeg=max((sum(w for (a,b),w in choices.items() if a==i or b==i) for i in range(2,k+1)),default=0)
            if maxdeg > 1-pp:
                choices={e:w*(1-pp)/maxdeg for e,w in choices.items()}
            actual=exact_check(k,choices)
            count+=1
    # Show n=3 prior example is recovered (7/11, 3/11, 5/11, 4/11).
    e={(2,3):F(4,11)}
    assert abs(exact_check(3,e)-7/11)<1e-10
    count+=1
    print('VERIFY_OK',count,'symbolic/exact comparisons')

if __name__ == '__main__':test()
