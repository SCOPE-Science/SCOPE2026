#!/usr/bin/env python3
"""Exact identities, validated finite examples and numerical falsification checks for a SIRD final-size envelope.
The analytic proof is in RESULT.md; numerical probes do not replace it.
"""
from fractions import Fraction
from math import exp, log
import random
import sympy as sp
import mpmath as mp

u,z,e=sp.symbols('u z e', positive=True)
h=sp.log(1/(z+e*sp.exp(-u)))
assert sp.simplify(sp.diff(h,u)-e/(z*sp.exp(u)+e)) == 0
assert sp.simplify(sp.diff(h,u,2)+z*e*sp.exp(u)/(z*sp.exp(u)+e)**2) == 0

# The two-group example does not satisfy any of the paper's H2a-H2d alternatives.
B=[[Fraction(2),Fraction(1,4)],[Fraction(3,5),Fraction(9,5)]]
row_sums=[sum(row) for row in B]
assert any(B[i][j]<1 for i in range(2) for j in range(2))  # H2a fails
assert all(v>1 for v in row_sums) # H2b fails
assert all(v/Fraction(6,5)>1 for v in row_sums) # H2c and H2d fail

mp.mp.dps=60
beta=mp.matrix([[2,mp.mpf(1)/4],[mp.mpf(3)/5,mp.mpf(9)/5]])
M=mp.matrix([sum(beta[i,j] for j in range(2))*mp.log(2) for i in range(2)])
c=mp.matrix([sum(beta[i,j] for j in range(2))*mp.log(mp.mpf(12)/11) for i in range(2)])
eta=min(c[i]/M[i] for i in range(2)); q=1-eta; K=1/eta
assert 0<eta<1

def fun(y):
    return mp.matrix([sum(beta[i,j]*mp.log((mp.mpf(6)/5)/(mp.mpf(3)/5+mp.exp(-y[j])/2)) for j in range(2)) for i in range(2)])

ys=mp.findroot(lambda a,b:(fun(mp.matrix([a,b]))[0]-a,fun(mp.matrix([a,b]))[1]-b),(mp.mpf('0.9'),mp.mpf('1.0')))
assert all(abs(fun(ys)[i]-ys[i])<mp.mpf('1e-50') for i in range(2))
l=mp.matrix([0,0]); upper=mp.matrix(M)
for n in range(41):
    for i in range(2):
        assert l[i]-mp.mpf('1e-50') <= ys[i] <= upper[i]+mp.mpf('1e-50')
        assert upper[i]-l[i] <= K*q**n*M[i]+mp.mpf('1e-50')
    l,upper=fun(l),fun(upper)
for i in range(2):
    assert abs(upper[i]-l[i])<mp.mpf('0.05')
print('Off-H2 test: positivity, uniqueness numerical witness and n=0..40 bracket certificate PASS')
print('Parameters: eta=',mp.nstr(eta,25),'q=',mp.nstr(q,25),'K=',mp.nstr(K,25))
print('Final logarithmic loss=',[mp.nstr(ys[i],26) for i in range(2)])
print('Final susceptible values=',[mp.nstr(mp.exp(-ys[i]),26) for i in range(2)])

# Numerical stress-tests deliberately include large and small transmission, removal, and seeds.
rng=random.Random(20260121)
for trial in range(500):
    m=rng.randrange(2,6)
    S=[rng.uniform(.3,3) for _ in range(m)]
    I=[rng.uniform(0.001,1) if rng.random()>.3 else 0 for _ in range(m)]
    I[0]=max(I[0],.001)
    R=[rng.uniform(0,1) for _ in range(m)]
    mu=[rng.uniform(.2,4) for _ in range(m)]
    gamma=[rng.uniform(.2,4) for _ in range(m)]
    b=[[rng.uniform(.005,3) for _ in range(m)] for __ in range(m)]
    N=[S[j]+I[j]+R[j] for j in range(m)]
    eps=[mu[j]/(gamma[j]+mu[j]) for j in range(m)]
    Z=[(1-eps[j])*N[j]+eps[j]*R[j] for j in range(m)]
    mx=[sum(b[i][j]/mu[j]*log(N[j]/Z[j]) for j in range(m)) for i in range(m)]
    cc=[sum(b[i][j]/mu[j]*log(N[j]/(Z[j]+eps[j]*S[j])) for j in range(m)) for i in range(m)]
    et=min(cc[i]/mx[i] for i in range(m)); qq=1-et; KK=1/et
    assert 0<et<1
    def F(y): return [sum(b[i][j]/mu[j]*log(N[j]/(Z[j]+eps[j]*S[j]*exp(-y[j]))) for j in range(m)) for i in range(m)]
    lo=[0]*m; hi=mx[:]
    for n in range(15):
        assert all(lo[j]<=hi[j]+1e-10 for j in range(m))
        assert all(hi[j]-lo[j]<=KK*qq**n*mx[j]+1e-9 for j in range(m))
        lo,hi=F(lo),F(hi)
print('500 random positive model matrices x 15 exact-bound-floating probes PASS')

# The seed-free case can admit multiple mathematical roots; root at zero and a positive root.
f=lambda y:4*mp.log(2/(1+mp.exp(-y)))-y
assert f(mp.mpf(0))==0
assert f(mp.mpf('0.01'))>0 and f(mp.mpf(4))<0
print('Seed-free degeneracy boundary PASS')
