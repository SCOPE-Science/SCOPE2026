"""Standalone exact checks for susceptibility-weighted SIR contact-degree allocation.
Theorems are proved in RESULT.md; this script tests finite integer cases independently.
Requires only Python 3 standard library.
"""
from fractions import Fraction as F

checks = 0

def require(cond):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(f'assertion {checks}')

def raw(k, a, b, rho):
    return rho * a * (a - 1) + b * (b - 1)

def thresholds(k):
    return [F(k + r, k - r - 1) for r in range(k - 1)]

def prediction(k, rho):
    t = thresholds(k)
    n = sum(rho > x for x in t)
    if n < len(t) and rho == t[n]:
        return {n, n + 1}
    return {n}

for k in range(2, 44):
    th = thresholds(k)
    require(all(th[i] < th[i+1] for i in range(len(th)-1)))
    tests = {F(1, 1), F(10000, 1), F(11,10), F(4,3), F(3,2), F(7,3)}
    for t in th:
        tests.add(t)
        tests.add(t-F(1, 100000))
        tests.add(t+F(1, 100000))
    for rho in sorted(tests):
        if rho <= 1:
            continue
        values = {a: raw(k, a, 2*k-a, rho) for a in range(1, 2*k)}
        minimum = min(values.values())
        actual = {k-a for a,v in values.items() if v == minimum}
        require(actual == prediction(k, rho))
        for r in range(k-1):
            diff = raw(k,k-r-1,k+r+1,rho)-raw(k,k-r,k+r,rho)
            require(diff == 2*((k+r)-rho*(k-r-1)))
        if rho > th[-1]:
            require(actual == {k-1})
            require(minimum == (2*k-1)*(2*k-2))

# Branching matrix identity: each row's number of remaining contacts times
# recipient's size-biased type probability and susceptibility. Trace = R.
for k in range(2,25):
    for rho in (F(11,10),F(13,7),F(31,3)):
        psi_b = F(1,2)/rho
        psi_a = rho*psi_b
        for a in range(1,2*k):
            b=2*k-a
            mat=((F(a-1)*F(a,2*k)*psi_a,F(a-1)*F(b,2*k)*psi_b),
                 (F(b-1)*F(a,2*k)*psi_a,F(b-1)*F(b,2*k)*psi_b))
            require(mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0] == 0)
            require(mat[0][0]+mat[1][1] == psi_b*raw(k,a,b,rho)/(2*k))

# Strict threshold-crossing example: K=3, high susceptibility=1,
# low susceptibility=1/20, beta=1.
k=3
rho=F(20)
psi_b=F(1,20)
require(psi_b*raw(k,3,3,rho)/(2*k) == F(21,20))
require(psi_b*raw(k,1,5,rho)/(2*k) == F(1,6))
require(prediction(k,rho) == {2})

print(f'PASS: {checks} exact assertions')
