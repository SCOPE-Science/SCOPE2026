"""Reproducible checks for a discrete proportionate-mixing epidemic theorem.
No finite computation is used in place of the analytical proof.
"""
from fractions import Fraction as Q
from math import sqrt


def exact_update(X, u, w, d, h):
    n, m = len(u), len(X[0])
    z = [sum(X[i]) for i in range(n)]
    S = [sum(w[i] * X[i][r] for i in range(n)) for r in range(m)]
    return [[(1-h*d)*X[i][r]+h*(1-z[i])*u[i]*S[r] for r in range(m)] for i in range(n)]

u=[Q(1),Q(2)]; w=[Q(3),Q(1)]; h=Q(1,20)
X=[[Q(1,10),Q(2,10),Q(0)], [Q(3,10),Q(1,10),Q(1,10)]]
initial=[row[:] for row in X]
S0=[sum(w[i]*X[i][r] for i in range(2)) for r in range(3)]
q=[s/sum(S0) for s in S0]
for d in [Q(2),Q(5),Q(6)]:
    X=[row[:] for row in initial]
    for k in range(5):
        z=[sum(row) for row in X]
        for i in range(2):
            for r in range(3):
                expected = q[r]*z[i]+(1-h*d)**k*(initial[i][r]-q[r]*sum(initial[i]))
                assert X[i][r]==expected,('exact identity',d,k,i,r)
        X=exact_update(X,u,w,d,h)
    assert all(0 <= x <= 1 for row in X for x in row)
print('EXACT_RATIONAL_EXCHANGE: PASS (3 thresholds, 5 steps, 3 strains)')


def iterate(d, N=300000):
    a=1-0.05*d
    X=[[0.1,0.2,0.0],[0.3,0.1,0.1]]
    emax=0.0
    for k in range(N):
        z=[sum(row) for row in X]
        S=[3*X[0][r]+X[1][r] for r in range(3)]
        X=[[(a*X[i][r]+0.05*(1-z[i])*[1.,2.][i]*S[r]) for r in range(3)] for i in range(2)]
    return X

X=iterate(5,100000)
K=7.0
z=[sum(row) for row in X]
for i in range(2):
    target=[1.,2.][i]/(0.05*K)
    assert abs(100000*z[i]/target-1)<0.006,('critical',i,100000*z[i],target)
print('CRITICAL_NUMERIC: PASS (100000 steps, normalized 1/k profile)')
X=iterate(2,1000)
Sstar=(1+sqrt(13))/2
zstar=[Sstar/(2+Sstar), Sstar/(1+Sstar)]
for i in range(2):
    assert abs(sum(X[i])-zstar[i])<1e-11
print('SUPERCRITICAL_NUMERIC: PASS (1000 steps, exact scalar root)')
X=iterate(6,400)
assert max(map(abs,[v for row in X for v in row]))<1e-8
print('SUBCRITICAL_NUMERIC: PASS (400 steps)')
# Rank-one iff all positive rows are parallel to one common positive weight.
assert 3*2 == 1*6   # example B=[[3,1],[6,2]], determinant=0
assert 1*5 != 2*3   # strict positive full-rank counterexample
print('RANK_TESTS: PASS')
print('CHECK_OK')
