#!/usr/bin/env python3
"""Exact rational checks for Brownian quadratic-energy Legendre sensor theorem.

This finite checker supports the analytic proof in RESULT.md; it does not
replace the infinite-dimensional or all-subsets argument.
"""
from fractions import Fraction as F
from itertools import combinations
from math import pi


def plus(a,b):
    return [((a[k] if k<len(a) else F(0))+(b[k] if k<len(b) else F(0))) for k in range(max(len(a),len(b)))]

def mult(a,b):
    z=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): z[i+j]+=x*y
    return z

def scale(a,c): return [c*x for x in a]
def integrate(a): return [F(0)]+[x/F(k+1) for k,x in enumerate(a)]
def integral(a): return sum((x/F(k+1) for k,x in enumerate(a)),F(0))

def polynomials(N):
    L=[[F(1)],[F(-1),F(2)]]
    for n in range(1,N):
        v=plus(scale(mult(L[n],[F(-1),F(2)]),F(2*n+1)),scale(L[n-1],F(-n)))
        L.append(scale(v,F(1,n+1)))
    return L[:N+1]

def d2(n):
    if n==0:return F(1,9)
    return F(1,4*(2*n-1)**2*(2*n+3)**2)
def e2(n):return F(1,16*(2*n+3)**2*(2*n+1)*(2*n+5))
def q2(i,j):
    if i==j:return d2(i)
    if {i,j}=={0,1}:return F(1,48)
    if abs(i-j)==2:return e2(min(i,j))
    return F(0)
def score(S):return sum((q2(i,j) for i in S for j in S),F(0))
def risk(m):
    if m==1:return F(1,9)
    return F(2*m*m-m+1,4*(2*m-3)*(2*m-1)**2*(2*m+1)**2)

def main():
    n=13
    L=polynomials(n)
    f=[integrate(z) for z in L]
    for i in range(n+1):
        for j in range(n+1):
            rational_gram=integral(mult(f[i],f[j]))
            observed=F((2*i+1)*(2*j+1))*rational_gram*rational_gram
            assert observed==q2(i,j),(i,j,observed,q2(i,j))
    print('PASS: all exact squared Gram entries for Legendre degrees 0..13')

    # Finite support searches, independent of the all-subsets compression proof.
    for m in range(1,8):
        target=score(range(m))
        for S in combinations(range(13),m):
            if tuple(S)==tuple(range(m)):continue
            assert score(S)<target,(m,S)
        assert F(1,3)-2*target==risk(m)
    print('PASS: strict finite optimality for every subset of degrees 0..12, cardinality 1..7')

    for m in range(2,101):
        tail=F(1,64)*(F(1,(2*m-1)**2)+F(1,(2*m+1)**2))+F(1,128)*(F(1,2*m+3)-F(1,2*m-1))
        assert 2*tail+4*(e2(m-2)+e2(m-1))==risk(m)
    assert risk(1)==F(1,9)
    assert risk(2)==F(7,900)
    assert risk(3)==F(4,3675)
    print('PASS: closed-form tail identities at every integer m=2..100')

    # Numerical KL tails, using a positive integral-test remainder bracket.
    for m in [20,100,1000]:
        partial=sum(1/(k-.5)**4 for k in range(m+1,m+20001))
        tail_lo=1/(3*(m+20001-.5)**3)
        tail_hi=1/(3*(m+20000-.5)**3)
        opt_lo=2*(partial+tail_lo)/pi**4
        opt_hi=2*(partial+tail_hi)/pi**4
        r=float(risk(m))
        assert r>opt_hi
        print(f'm={m}: Legendre/KL ratio in ({r/opt_hi:.9f}, {r/opt_lo:.9f})')
    print('Asymptotic efficiency ratio:',3*pi**4/128)
    print('PASS: all finite checks completed')

if __name__=='__main__':main()
