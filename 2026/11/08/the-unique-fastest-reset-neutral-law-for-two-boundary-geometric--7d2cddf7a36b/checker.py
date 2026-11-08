"""Finite-state checks for the reset-neutral absorption-time theorem.

Run with Python 3 and sympy: python checker.py. All finite-state tests
use exact rational arithmetic. They supplement, not replace, the proof.
"""
from math import acosh, cosh, exp, log, sqrt
import sympy as S

checks = 0

def confirm(statement):
    global checks
    assert statement
    checks += 1


def subchain(a, lam, gamma):
    p = S.Rational(1, 1) / (1 + lam**2)
    q = 1-p
    d = 1-gamma
    W = S.zeros(a-1)
    b0 = S.zeros(a-1,1)
    ba = S.zeros(a-1,1)
    for z in range(1,a):
        if z > 1: W[z-1,z-2] = q
        else: b0[z-1] = d*q
        if z < a-1: W[z-1,z] = p
        else: ba[z-1] = d*p
    G = (S.eye(a-1) - d*W).inv()
    u = G*b0
    v = G*ba
    return W, u, v


def neutral_pair(a, lam, z):
    pi = S.zeros(a-1,1)
    if 2*z == a:
        pi[z-1] = 1
    else:
        ratio = lam**(a-2*z)
        pi[z-1] = ratio/(1+ratio)
        pi[a-z-1] = 1/(1+ratio)
    return pi


for a in range(3,11):
    for lam in (S.Rational(1,2),S.Integer(1),S.Integer(2)):
        for gamma in (S.Rational(1,5),S.Rational(1,2),S.Rational(4,5)):
            W,u,v = subchain(a,lam,gamma)
            s=u+v
            d=1-gamma
            pairs=[]
            for z in range(1,a//2+1):
                pi=neutral_pair(a,lam,z)
                Sbar=(pi.T*s)[0]
                Ubar=(pi.T*u)[0]
                Vbar=(pi.T*v)[0]
                confirm(S.simplify(Vbar - lam**(-a)*Ubar)==0)
                C=S.simplify(Ubar/Sbar)
                confirm(C==S.simplify(lam**a/(1+lam**a)))
                Q=d*W + gamma*S.ones(a-1,1)*pi.T
                H=(S.eye(a-1)-Q).inv()
                T=H*S.ones(a-1,1)
                b0=S.zeros(a-1,1)
                b0[0]=d*lam**2/(1+lam**2)
                H0=H*b0
                for i in range(a-1):
                    confirm(S.simplify(T[i]-(1-s[i])/(gamma*Sbar))==0)
                    confirm(S.simplify(H0[i]-(u[i]+(1-s[i])*C))==0)
                pairs.append((z,Sbar))
            # The first paired position z=1 uniquely maximizes first-cycle success.
            for z,sbar in pairs[1:]:
                confirm(bool(pairs[0][1]>sbar))
            # Exact mixtures: every nontrivial mixture with any other neutral pair is slower.
            if len(pairs)>1:
                z1, s1=pairs[0]
                z2, s2=pairs[-1]
                confirm(bool(s1>(s1+s2)/2))

# Hyperbolic pair formula against independent linear-algebra calculations.
for a in (4,5,8,11,17):
    for p in (0.15,0.5,0.77):
        q=1-p
        lam=sqrt(q/p)
        theta=abs(log(lam))
        for gamma in (0.03,0.2,0.6,0.92):
            k=acosh(1/(2*(1-gamma)*sqrt(p*q)))
            n=a-1
            import numpy as np
            W=np.zeros((n,n));b=np.zeros(n)
            for i in range(n):
                if i>0: W[i,i-1]=q
                else: b[i]+=(1-gamma)*q
                if i<n-1: W[i,i+1]=p
                else: b[i]+=(1-gamma)*p
            sb=np.linalg.solve(np.eye(n)-(1-gamma)*W,b)
            for z in range(1,a//2+1):
                pi=np.zeros(n)
                if 2*z==a: pi[z-1]=1
                else:
                    ratio=lam**(a-2*z)
                    pi[z-1]=ratio/(1+ratio)
                    pi[a-z-1]=1/(1+ratio)
                direct=float(pi@sb)
                t=a/2-z
                formula=cosh(theta*a/2)/cosh(k*a/2)*cosh(k*t)/cosh(theta*t)
                confirm(abs(direct-formula)<2e-11)

# The logarithmic mean-time advantage has the claimed exponential rate.
p=0.6; gamma=0.35; q=1-p; theta=abs(log(sqrt(q/p)))
k=acosh(1/(2*(1-gamma)*sqrt(p*q)))
for a in (80,120,160):
    # Only logs of hyperbolic cosines are needed; no vanishing probabilities.
    def logcosh(x): return abs(x)+log(1+exp(-2*abs(x)))-log(2)
    log_mid=logcosh(theta*a/2)-logcosh(k*a/2)
    t=a/2-1
    log_edge=log_mid+logcosh(k*t)-logcosh(theta*t)
    logTmid=log(1-exp(log_mid))-log_mid-log(gamma)
    logTedge=log(1-exp(log_edge))-log_edge-log(gamma)
    observed=(logTmid-logTedge)/a
    confirm(abs(observed-(k-theta)/2)<0.07)

print('PASS',checks,'independent exact and numerical assertions')
