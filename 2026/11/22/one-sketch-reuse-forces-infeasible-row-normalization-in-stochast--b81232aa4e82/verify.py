"""Reproducibility checks for support-conditioned one-sketch normal landing.

Standalone Python 3 standard library; finite checks supplement, not replace, proof.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

assertions = 0

def check(condition, explanation):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(explanation)


def shared_update(y, i, eta):
    n = len(y)
    v = y[i]
    factor = 1 + eta*n - eta*n*n*v
    out = list(y)
    out[i] = v*factor*factor
    return out


def exact_shared_drift(y, eta):
    n = len(y)
    y2 = sum(v*v for v in y)
    y3 = sum(v*v*v for v in y)
    predicted = -2*eta*(n*y2 - 1) + eta*eta*n*(n*n*y3 - 2*n*y2 + 1)
    actual = sum((sum(shared_update(y,i,eta)) - 1) for i in range(n))/n
    return actual, predicted


def exact_independent_drift(y, eta):
    n = len(y)
    # Selection of coordinate j for norm correction; i for residual estimate.
    actual = F(0)
    for i in range(n):
        for j in range(n):
            factor = 1 - eta*n*(n*y[i]-1)
            actual += y[j]*(factor*factor - 1)/ (n*n)
    predicted = eta*eta*n*(n*sum(v*v for v in y)-1)
    return actual, predicted

for n in range(2,9):
    eta = F(1,2*n*n)
    for grid in range(1,8):
        for tup in product(range(grid+1), repeat=n-1):
            z = sum(tup)
            if z > grid: continue
            y = tuple(F(v,grid) for v in (*tup, grid-z))
            actual, predicted = exact_shared_drift(y,eta)
            check(actual == predicted,'shared exact drift')
            check(actual <= 0,'same-sketch norm drift not outward')
            ia,ip=exact_independent_drift(y,eta)
            check(ia == ip,'independent exact drift')
            check(ia >= 0,'independent sketch expected norm drift')
            for v in y:
                if v>0:
                    beta = eta*n
                    Y=n*v
                    g=1-beta*Y*(2-beta*(Y-1))
                    check(0<g<1,'per-coordinate squared-amplitude contraction')
    y=tuple([F(1,n-1)]*(n-1)+[F(0)])
    a,b=exact_shared_drift(y,eta)
    check(a<0,'a sparse feasible start drifts inward')

# The exact surrogate gradient is 2 (n*x_i^2-1)*x_i;
# shared stochastic step uses 2*B_i*x*(x^T B_i x-1), whose expectation is that gradient.
for n in range(2,15):
    x=[F(i+1,n*(n+1)) for i in range(n)]
    for j in range(n):
        grad = sum(F(2*n if i==j else 0)*x[j]*(n*x[i]*x[i]-1) for i in range(n))/n
        check(grad == 2*x[j]*(n*x[j]*x[j]-1),'surrogate gradient identity')

# Almost-sure assertion is PROVED using iid visitation, not inferred from this simulation.
for n in [3,5,8]:
    for support in range(1,n):
        rng = Random(100000+n*10+support)
        x=[(support**-.5 if i<support else 0.) for i in range(n)]
        eta=1/(2*n*n)
        for step in range(30000):
            i = rng.randrange(n)
            x[i] *= (1+eta*n-eta*n*n*x[i]*x[i])
        for j in range(n):
            check(abs(abs(x[j]) - (n**-.5 if j<support else 0.)) < 3e-7, 'random visitation limit')
        check(abs(sum(t*t for t in x)-support/n)<1e-6,'spurious squared norm limit')

# Matrix-valued Stiefel calculation, using a direct rank-one row estimator.
def step_matrix(X, i, eta):
    n=len(X)
    Y=[row[:] for row in X]
    sq=sum(v*v for v in X[i]); factor=1-eta*n*(n*sq-1)
    Y[i]=[v*factor for v in X[i]]
    return Y

def gram(X):
    p=len(X[0]); return [[sum(row[a]*row[b] for row in X) for b in range(p)] for a in range(p)]

# Exact two-dimensional Stiefel witness.
I=[[F(1),F(0)],[F(0),F(1)]]
Y=step_matrix(I,0,F(1,8))
check(Y==[[F(3,4),F(0)],[F(0),F(1)]], 'one exact rank-one sampled update')

# Full-rank Stiefel frames with overlapping supports and no zero rows.
from math import sqrt
for n,p in [(2,2),(3,2),(4,2),(5,3),(8,4)]:
    rr=Random(543000+n*11+p)
    cols=[]
    for j in range(p):
        v=[rr.gauss(0,1) for _ in range(n)]
        for u in cols:
            z=sum(v[i]*u[i] for i in range(n))
            v=[v[i]-z*u[i] for i in range(n)]
        norm=sqrt(sum(t*t for t in v))
        cols.append([t/norm for t in v])
    X=[[cols[j][i] for j in range(p)] for i in range(n)]
    G=gram(X)
    for a in range(p):
        for b in range(p):
            check(abs(G[a][b]-(1 if a==b else 0))<1e-12,'orthonormal input')
    U=[]
    for row in X:
        z=sqrt(sum(t*t for t in row))
        U.append([t/(sqrt(n)*z) if z else 0. for t in row])
    eta=1/(2*n*n)
    Z=[row[:] for row in X]
    for t in range(40000):
        i=rr.randrange(n)
        Z=step_matrix(Z,i,eta)
    for i in range(n):
        for a in range(p):
            check(abs(Z[i][a]-U[i][a])<2e-7,'matrix row equalization')
    final_gram=gram(Z)
    infeas=sum((final_gram[a][b]-(1 if a==b else 0))**2 for a in range(p) for b in range(p))/2
    lower=(p-1)**2/(2*p)
    check(infeas>=lower-1e-7,'universal constraint-violation lower bound')
print('PASS: %d total exact/supplementary checks' % assertions)
