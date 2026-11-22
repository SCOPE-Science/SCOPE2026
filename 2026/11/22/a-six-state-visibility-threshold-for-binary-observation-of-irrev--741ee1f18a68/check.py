#!/usr/bin/env python3
"""Standalone finite-ring matrix and symbolic checks for the stated binary sensor theorem.
The analytic proof, not finite sampling, covers every allowed ring and rate.
Run: python check.py
Requires: numpy scipy sympy.
"""
import itertools
import math
import numpy as np
import sympy as sp
from scipy.linalg import expm

COUNT = 0

def check(condition, message):
    global COUNT
    assert bool(condition), message
    COUNT += 1

def rotate(word, j):
    return tuple(word[j:]+word[:j])

def reflection_exists(word):
    w=tuple(word)
    return tuple(w[::-1]) in {rotate(w,j) for j in range(len(w))}

def gen(n,a,b):
    Q=np.zeros((n,n),float)
    for i in range(n):
        Q[i,(i+1)%n] = a
        Q[i,(i-1)%n] = b
        Q[i,i] = -a-b
    return Q

def triple(Q, f, t, s):
    n=len(f); f=np.array(f,float); D=np.diag(f)
    return float((f@expm(t*Q)@D@expm(s*Q)@f)/n)

def run():
    for n in range(3,6):
        for word in itertools.product((0,1),repeat=n):
            check(reflection_exists(word),f'binary ring <=5 must reflect: {word}')
    special=(1,1,0,1,0,0)
    check(not reflection_exists(special),'six-state sensor must be chiral')
    a,b=sp.symbols('a b', positive=True)
    n=6;Q=sp.zeros(n)
    for i in range(n):
        Q[i,(i+1)%n]=a;Q[i,(i-1)%n]=b;Q[i,i]=-a-b
    f=sp.Matrix(special); D=sp.diag(*special)
    check(Q*sp.ones(n,1)==sp.zeros(n,1),'Q rows zero')
    check(sp.ones(1,n)*Q==sp.zeros(1,n),'Q cols zero')
    A12=(f.T*Q*D*Q*Q*f)[0]-(f.T*Q*Q*D*Q*f)[0]
    check(sp.factor(A12-(a-b)*(a*a+a*b+b*b))==0,'cubic asymmetry coefficient')
    for k in range(3):
        check(sp.simplify((f.T*(Q**k)*D*f)[0]-(f.T*D*(Q**k)*f)[0])==0,'one-lag symmetry')
    # Matrix exponential checks use exact finite-size propagators, independently of symbolic powers.
    for n in range(3,10):
        for aa,bb in [(0.3,1.7),(1.0,1.0),(3.5,.25)]:
            M=gen(n,aa,bb)
            P=expm(0.19*M)
            check(np.linalg.norm(P.sum(axis=1)-1,np.inf)<1e-12,'transition stochastic')
            check(np.linalg.norm(P.sum(axis=0)-1,np.inf)<1e-12,'stationary uniform')
            for j in range(min(n,5)):
                sensor=np.array([int((i+j)%3==0) for i in range(n)],float)
                D1=np.diag(sensor); u=np.ones(n)/n
                forward=u@D1@P@D1@np.ones(n)
                reverse=u@D1@P.T@D1@np.ones(n)
                check(abs(forward-reverse)<1e-12,'two-snapshot stationarity')
                for dt in [0.02,0.25]:
                    T=expm(dt*M)
                    x=u@D1@T@D1@T@D1@np.ones(n)
                    # three equal-lag binary observation law is trivially reversed
                    check(abs(x-u@D1@T.T@D1@T.T@D1@np.ones(n))<1e-12,'equal-lag triple reversal')
    for aa,bb in [(0.2,0.8),(0.8,.2),(.4,1.7),(1.7,.4),(2,1),(.75,3),(3,.75),(1,1)]:
        M=gen(6,aa,bb)
        for eps in [0.001,0.002,0.003,0.004]:
            delta=triple(M,special,eps,2*eps)-triple(M,special,2*eps,eps)
            expected=(aa-bb)*(aa*aa+aa*bb+bb*bb)*eps**3/6
            if aa==bb: check(abs(delta)<1e-13,'detailed balance zero asymmetry')
            else:
                check(delta*expected>0,'arrow sign at short lag')
                check(abs(delta/expected-1)<0.1,'uniform cubic leading behavior')
    for aa,bb in [(0.2,0.8),(0.8,0.2),(2,1),(1,2),(1,1)]:
        M=gen(6,aa,bb); h=.03; T=expm(h*M); u=np.ones(6)/6
        df=np.diag(np.array(special,float)); dz=np.eye(6)-df
        def wordprob(seq):
            out=u.copy()
            for j,x in enumerate(seq):
                out=out @ (df if x else dz)
                if j<3: out=out@T
            return out.sum()
        delta=triple(M,special,h,2*h)-triple(M,special,2*h,h)
        check(abs(wordprob([1,1,0,1])-wordprob([1,0,1,1])-delta)<1e-12,'four-frame word reduction')
    print('PASS',COUNT,'assertions')

if __name__=='__main__':run()
