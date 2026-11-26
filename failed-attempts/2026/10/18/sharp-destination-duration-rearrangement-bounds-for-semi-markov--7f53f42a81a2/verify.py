"""Exact small-network checks for the semi-Markov variance envelope theorem.
No external dependencies. This verifier checks examples; the general statement is proved analytically.
"""
from fractions import Fraction as F
from itertools import product, combinations


def inverse(A):
    n = len(A)
    M = [[F(A[i][j]) for j in range(n)] + [F(i == j) for j in range(n)] for i in range(n)]
    for k in range(n):
        p = next(i for i in range(k, n) if M[i][k])
        M[k], M[p] = M[p], M[k]
        z = M[k][k]
        M[k] = [x/z for x in M[k]]
        for i in range(n):
            if i != k:
                z = M[i][k]
                M[i] = [x-z*y for x,y in zip(M[i], M[k])]
    return [row[n:] for row in M]


def matvec(A,v):
    return [sum((a*b for a,b in zip(row,v)), F(0)) for row in A]

# A three-transient-state directed cycle, with escape to an absorbing target
# at probability 1/2 from every transient state. Holding laws are fixed at
# each state and independent of the experiment's assignment of holding times
# to the two possible next destinations.
held = [(1,2,3,5), (1,1,2,3), (1,2,2,4)]
n=3
P = [[F(1,2) if j == (i+1)%n else F(0) for j in range(n)] for i in range(n)]
N = inverse([[F(i==j)-P[i][j] for j in range(n)] for i in range(n)])
mu = [sum(map(F, v),F(0))/4 for v in held]
nu = [sum((F(t*t) for t in v),F(0))/4 for v in held]
m = matvec(N,mu)
options = tuple(tuple(combinations(range(4),2)) for _ in range(n))
low = [None]*n
high = [None]*n
checks = 0
records = []
for choices in product(*options):
    a = [m[(i+1)%n] * sum((F(held[i][j]) for j in chosen),F(0))/4 for i,chosen in enumerate(choices)]
    h = matvec(N,[nu[i]+2*a[i] for i in range(n)])
    var = [h[i]-m[i]*m[i] for i in range(n)]
    records.append((choices,var))
    for i in range(n):
        low[i] = var[i] if low[i] is None or var[i]<low[i] else low[i]
        high[i] = var[i] if high[i] is None or var[i]>high[i] else high[i]
        checks += 2

# The upper assignment sends the largest two atom-slots to the positive
# residual-mean branch. Ties in the holding times are harmless.
up = tuple(tuple(sorted(range(4), key=lambda j:(held[i][j],j))[-2:]) for i in range(n))
down = tuple(tuple(sorted(range(4), key=lambda j:(held[i][j],j))[:2]) for i in range(n))
recmap = {choices:vars for choices,vars in records}
assert recmap[up] == high, (up, recmap[up], high)
assert recmap[down] == low, (down, recmap[down], low)
checks+=6
for choices, var in records:
    for i in range(n):
        assert low[i] <= var[i] <= high[i]
        checks+=1

# Smallest strict example: three total states i->j or target, and j->target.
# At i, duration Uniform(0,2) and choosing j for low/high halves produces
# extremal covariance +/-1/4 with the indicator of taking branch j.
mu0=F(1); nu0=F(4,3); p=F(1,2); mj=F(1); nuj=F(1)
mean = mu0+p*mj
var_low = (nu0 + 2*F(1,4)*mj + p*nuj) - mean*mean
var_high = (nu0 + 2*F(3,4)*mj + p*nuj) - mean*mean
assert (mean,var_low,var_high)==(F(3,2),F(1,12),F(13,12))
checks += 3

# Completely independent pair at i has E[tau * 1_J]=E[tau]/2.
var_ind = nu0+2*F(1,2)+p*nuj-mean*mean
assert var_ind == F(7,12)
checks += 1

print(f'PASS: {checks} exact rational checks over {len(records)} couplings')
print('network means:', [str(x) for x in m])
print('network min variances:', [str(x) for x in low])
print('network max variances:', [str(x) for x in high])
print('three-state strict example: mean=3/2, min=1/12, independent=7/12, max=13/12')
