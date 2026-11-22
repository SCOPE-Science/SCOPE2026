"""Finite exact checks for the comb decomposition and spectral-hole mechanism.

These checks supplement, rather than replace, the infinite-dimensional proof.
"""
from fractions import Fraction as Q

checks = 0

def test(ok, message):
    global checks
    assert ok, message
    checks += 1

# The nilpotent block sends (x_1,...,x_L) to (0,x_1,...,x_{L-1}).
# For rational nonzero lambda, its inverse is a finite geometric sum.
for L in range(1, 29):
    for lam in [Q(1,2), Q(2,3), Q(-1,3), Q(1,1), Q(2,1)]:
        for trial in range(6):
            y = [Q((i * 7 + L + 3 * trial) % 17 - 8, 11) for i in range(L)]
            # x_k = sum_{j=1}^k lambda^{-(k-j+1)} y_j
            x = []
            for k in range(L):
                x.append(sum(lam ** (-(k - j + 1)) * y[j] for j in range(k + 1)))
            output = [lam * x[0]] + [lam * x[k] - x[k-1] for k in range(1, L)]
            test(output == y, f'inverse {L} {lam} {trial}')
# Exact finite residual r^L in one long block, at lambda=1/2.
for L in range(1, 65):
    lam = Q(1, 2)
    x = [lam ** (L - k - 1) for k in range(L)]
    r = [lam*x[0]]+[lam*x[k]-x[k-1] for k in range(1,L)]
    test(max(map(abs,x)) == 1 and max(map(abs,r)) == lam**L, f'residual {L}')
# At unit circle lambda=1, a ramp has norm one and defect 1/L.
for L in range(1, 65):
    x = [Q(k+1,L) for k in range(L)]
    r = [x[0]]+[x[k]-x[k-1] for k in range(1,L)]
    test(max(map(abs,x)) == 1 and max(map(abs,r)) == Q(1,L), f'unit ramp {L}')
# Explicit single-codimension range of lambda I-U on a finite segment,
# tested with a boundary correction approximating the infinite sum.
for lam in [Q(1,2),Q(-1,3),Q(2,3)]:
    for m in range(1,40):
        x = [Q((k*3+m)%13-6,17) for k in range(m)]
        y = [lam*x[0]]+[lam*x[k]-x[k-1] for k in range(1,m)]
        test(sum(lam**k*y[k] for k in range(m))==lam**m*x[-1], 'telescoping')
print('COMB_EXACT_FINITE_CHECK_OK', checks)
