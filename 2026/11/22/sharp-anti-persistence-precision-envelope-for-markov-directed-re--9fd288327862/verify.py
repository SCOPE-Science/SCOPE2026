"""Independent rational checks for a Markov-directed renewal-current theorem.
Uses only the Python standard library. Run: python verify.py
"""
from fractions import Fraction as F
from math import sqrt

# Check the stationary two-state transition matrix and its eigenvalue.
P = ((F(2,3), F(1,3)), (F(1), F(0)))
pi = (F(3,4), F(1,4))
for j in range(2):
    assert sum(pi[i]*P[i][j] for i in range(2)) == pi[j]
mean = pi[0]-pi[1]
rho = P[0][0] - P[1][0]
assert mean == F(1,2) and rho == -F(1,3)
V = (1-mean*mean)*(1+rho)/(1-rho)
assert V == F(3,8)
# Finite-length variance by two independent paths:
# covariance summation and exact first/second moment matrix recursion.
for length in (1,2,3,4,5,9,15,25):
    predicted=(1-mean*mean)*(length+2*sum((length-h)*rho**h for h in range(1,length)))
    d=[(pi[0], pi[0], pi[0]), (pi[1],-pi[1],pi[1])]
    # entries hold probability, first unnormalized moment, second moment
    for step in range(2,length+1):
        nxt=[(F(0),F(0),F(0)) for _ in range(2)]
        for i in range(2):
            prob,m1,m2=d[i]
            for j in range(2):
                s=1 if j==0 else -1
                pp,aa,bb=nxt[j]
                w=P[i][j]
                nxt[j]=(pp+w*prob, aa+w*(m1+s*prob), bb+w*(m2+2*s*m1+prob))
        d=nxt
    first=sum(z[1] for z in d); second=sum(z[2] for z in d)
    assert first == mean*length
    assert second-first*first == predicted

# Independent tilted transfer matrix for independent durations N=1 or 2,
# each of probability 1/2, with per-cycle reward R=1.
# For P above, the principal eigenvalue of diag(exp(s),exp(-s)) P
# satisfies lambda^2 - (2/3) exp(s) lambda - 1/3 = 0.
T=F(2,3); lam=F(1)
lam1 = T*lam/(2*lam-T)
lam2 = (T*lam+2*T*lam1-2*lam1*lam1)/(2*lam-T)
assert lam1==F(1,2) and lam2==F(5,8)
loglam2=lam2-lam1*lam1
assert loglam2==F(3,8)
EN=F(3,2); varN=F(1,4)
k1=lam1/EN
k2=(loglam2+varN*k1*k1)/EN
assert k1==F(1,3) and k2==F(29,108)
# Check the same 29/108 by the independently stated renewal expression.
A=F(1); B=F(3,2)
D=varN*(A/B)**2
sigma=((1-mean*mean)*(A*A*(1+rho)/(1-rho))+mean*mean*D)/B
assert sigma==F(29,108) and sigma==k2

# Fixed-bias optimality: every allowed transition matrix must obey the
# lower bound. Exact fractions include endpoints and nonsymmetric cases.
for m in (F(1,5),F(1,2),F(4,5)):
    plus=(1+m)/2; minus=(1-m)/2
    rho_min=-minus/plus
    for z in range(1,20):
        p=minus*z/20  # prob(+ to -), not the entire admissible range
        q=plus*p/minus
        if q>1: continue
        r=1-p-q
        assert r>=rho_min
        assert (1+r)/(1-r)>=m
    assert (1+rho_min)/(1-rho_min)==m

# Marginal reversal-information upper bound from the iid-direction setting
# is (sqrt(3)-1)/2 at m=1/2; the Markov example gives 2/3.
precision=mean*mean/V
assert precision==F(2,3)
assert 2*precision+1>sqrt(3)  # implies 2/3 > (sqrt(3)-1)/2
print('PASS: exact finite-horizon moments, tilted renewal dispersion, sharp bound, and reversal-information example')
