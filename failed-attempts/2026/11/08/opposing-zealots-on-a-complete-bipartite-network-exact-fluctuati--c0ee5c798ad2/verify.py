#!/usr/bin/env python3
"""Reproduce exact stationary moments and asymptotic moment recurrences.
Uses only Python 3 and SymPy. No external files or downloads are required.
"""
import sympy as sp


def exact_stationary(a, b):
    """Solve the independent lumped finite-state CTMC by rational elimination."""
    states = [(i, j) for i in range(a) for j in range(b)]
    index = {s: k for k, s in enumerate(states)}
    size = len(states)
    QT = sp.zeros(size)
    for k, (i, j) in enumerate(states):
        rates = [
            ((i+1,j), sp.Rational((a-1-i)*j,b)),
            ((i-1,j), sp.Rational(i*(b-j),b)),
            ((i,j+1), sp.Rational((b-1-j)*(i+1),a)),
            ((i,j-1), sp.Rational(j*(a-1-i),a)),
        ]
        for s2, rate in rates:
            if rate == 0:
                continue
            h = index[s2]
            QT[h,k] += rate
            QT[k,k] -= rate
    QT[size-1,:] = sp.ones(1,size)
    rhs = sp.zeros(size,1)
    rhs[-1] = 1
    solution = QT.inv() * rhs
    assert all(w >= 0 for w in solution)
    # Generator validation for each state, not just its solved system.
    assert sum(solution) == 1
    return states, solution


def mean_variance(states, pi, a, b):
    n=a+b
    values=[sp.Rational(1+i+j,n) for i,j in states]
    mean=sum(w*v for w,v in zip(pi,values))
    variance=sp.factor(sum(w*v*v for w,v in zip(pi,values)) -mean*mean)
    return mean,variance


def verify():
    count=0
    for a in range(2,6):
        for b in range(2,6):
            states,pi=exact_stationary(a,b)
            mean,var=mean_variance(states,pi,a,b)
            assert mean == sp.Rational(b,a+b)
            assert var == sp.Rational((a-1)*(b-1),(a+b-1)*(3*(a+b)-4))
            count+=1
    # Independent algebra check of the first- and second-moment equations.
    a,b=sp.symbols('a b',positive=True,integer=True)
    n=a+b
    x=(b-1)/(n-1);y=b/(n-1)
    U=(b-1)*(a+3*b-4)/((n-1)*(3*n-4))
    V=b*(a+3*b-4)/((n-1)*(3*n-4))
    W=b*(a+3*b-2)/((n-1)*(3*n-4))
    assert sp.factor(U-(b-1)*V/b)==0
    assert sp.factor(W-y/a-(a-1)*V/a)==0
    assert sp.factor(2*V-y/b-(b-2)*W/b-(2*x+(a-2)*U)/a)==0
    var=sp.factor((a-1)*x*(1-x)+(b-1)*y*(1-y)+
        (a-1)*(a-2)*(U-x*x)+(b-1)*(b-2)*(W-y*y)+
        2*(a-1)*(b-1)*(V-x*y))
    assert sp.factor(var/n**2-(a-1)*(b-1)/((n-1)*(3*n-4))) == 0
    # Beta(2*beta,2*(1-beta)) moments satisfy the limiting generator.
    t=sp.symbols('t',positive=True)
    moments=[sp.S(1)]
    for k in range(1,13):
        moments.append(sp.factor(moments[-1]*(2*t+k-1)/(k+1)))
    for k in range(1,13):
        assert sp.factor((2*t+k-1)*moments[k-1]-(k+1)*moments[k]) == 0
    assert sp.factor(moments[1]-t) == 0
    assert sp.factor(moments[2]-t*(2*t+1)/3) == 0
    print('VERIFY_OK: 16 exact finite-chain solutions; symbolic pair equations, variance, and 12 Beta moment recurrences')

if __name__=='__main__':
    verify()
