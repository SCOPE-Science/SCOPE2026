"""Reproduce exact algebra and finite-matrix checks for the star mobility law.

Requires Python 3.10+, sympy and numpy.  Finite checks supplement, and do
not replace, the elementary all-size proof in RESULT.md.
"""
from fractions import Fraction
from math import sqrt, isclose
from random import Random
import sympy as S
import numpy as np


def radial_perron(m, s, f, xi=1):
    return xi*f/(1+f)/(s*(s+(m+1)*f))*(m*f+sqrt(m*(s+f)*(s+m*f)))


def full_kernel(m, s, f, xi=1):
    n=m+1
    a=np.zeros((n,n),float)
    a[0,1:]=1
    a[1:,0]=1
    l=np.diag(np.sum(a,axis=1))-a
    return xi*f/(1+f)*np.linalg.solve(s*np.eye(n)+f*l,a)


def test_symbolic():
    m,s,r,f,xi=S.symbols('m s r f xi', positive=True)
    r_f=S.sqrt(m*(s+f)/(s+m*f))
    reduced=xi*m*(r+1)*(m-r*r)/((m+r)*(m*(r*r-1)+s*(m-r*r)))
    f_of_r=s*(m-r*r)/(m*(r*r-1))
    factored=xi*f/(1+f)/(s*(s+(m+1)*f))*(m*f+r*(s+m*f))
    assert S.factor(S.together(reduced - factored.subs(f,f_of_r)))==0
    diff=S.factor(S.together(S.diff(reduced,r)).as_numer_denom()[0])
    wanted=m*xi*(m-1)*(s*(m-r*r)**2-m*(m+r*r)*(r+1)**2)
    assert S.factor(diff-wanted)==0
    critical=4*m*(m+1)/(m-1)**2
    assert S.factor(m*(m+1)*4/(m-1)**2-critical)==0
    assert S.simplify(reduced.subs(r,S.Integer(1))-2*m*xi/(s*(m+1)))==0
    assert S.simplify(reduced.subs(r,S.sqrt(m)))==0
    star16=S.simplify(reduced.subs({m:16,s:20,r:2,xi:1}))
    assert star16==S.Rational(1,9)
    assert S.simplify((m*(m+r*r)*(r+1)**2/(m-r*r)**2).subs({m:16,r:2}))==20
    assert S.simplify(f_of_r.subs({m:16,s:20,r:2}))==5
    print('symbolic reduction, derivative, endpoints, exact optimum: PASS')


def test_exact_witness():
    m=16;s=S.Integer(20);f=S.Integer(5)
    n=m+1
    a=S.zeros(n,n)
    for i in range(1,n): a[0,i]=1;a[i,0]=1
    l=S.diag(*[sum(a[i,j] for j in range(n)) for i in range(n)])-a
    k=f/(1+f)*(s*S.eye(n)+f*l).inv()*a
    # exact Perron eigenvalue checked via positive right eigenvector
    u=S.Matrix([S.Rational(2,1)] + [S.Rational(1,1)]*m)
    # r=2 corresponds to a hub-vs-leaf eigenvector ratio? solve explicitly
    B=S.Matrix([[m*f,m*(s+f)],[s+m*f,m*f]])
    b=(f/(1+f)/(s*(s+(m+1)*f)))*B
    eig=S.Rational(1,9)
    v=S.Matrix([b[0,1],eig-b[0,0]])
    assert v[0]>0 and v[1]>0
    vv=S.Matrix([v[0]]+[v[1]]*m)
    assert k*vv==eig*vv
    assert all(k[i,j]>0 for i in range(n) for j in range(n))
    assert S.Rational(2*16,20*17)==S.Rational(8,85)
    print('17-patch exact rational matrix Perron certificate: PASS')


def test_numerical():
    rng=Random(773121)
    for _ in range(500):
        m=rng.randint(1,22)
        s=1+10**rng.uniform(-2,2)
        f=10**rng.uniform(-3,3)
        xi=10**rng.uniform(-1,1)
        k=full_kernel(m,s,f,xi)
        eigs=np.linalg.eigvals(k)
        spectral=max(abs(q) for q in eigs)
        claimed=radial_perron(m,s,f,xi)
        assert isclose(spectral,claimed,rel_tol=5e-10,abs_tol=1e-11), (m,s,f,claimed,spectral)
    lam=lambda f:radial_perron(16,20,f)
    assert lam(Fraction(7,4))>Fraction(1,10)
    assert lam(Fraction(40,1))>Fraction(1,10)
    assert lam(Fraction(42,1))<Fraction(1,10)
    assert lam(Fraction(1,1))<Fraction(1,10)
    assert isclose(lam(5),1/9,rel_tol=1e-14)
    print('500 full-matrix Perron matches and witness persistence signs: PASS')


if __name__=='__main__':
    test_symbolic()
    test_exact_witness()
    test_numerical()
