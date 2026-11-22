"""Reproducibility checks for the two-row, two-column HNB size factor.

The infinite-index part is proved analytically in RESULT.md; these checks
verify the exact finite rational inequality and finite-index formula.
"""
from fractions import Fraction as Q

checks = 0
for n in range(2, 25):
    poly = -2*n**3 + 183*n**2 - 236*n - 221
    assert poly > 0
    B = Q((2*n + 1)*(n*n + 22*n + 221), 1140*n*(n+1))
    assert B < Q(1,5)
    checks += 2

for w in [Q(9,10), Q(19,20), Q(99,100), Q(999,1000)]:
    e = 1-w
    p0 = e**3/(1+w)
    gamma0 = (1-p0)/(4*w)
    assert gamma0 >= Q(1,4)
    checks += 1
    for n in range(2, 101):
        # Gamma_{n-1}=F_{n-1} R_{n-1}/n^2, both terms exact.
        F = p0*sum(j*j*w**(j-1) for j in range(1,n+1))
        R = 1/e + 2*w/((n+1)*e**2) + w*(1+w)/((n+1)**2*e**3)
        gam = F*R/(n*n)
        assert gam <= Q(1,5)
        assert gam < gamma0
        checks += 2
print(f"PASS: {checks} exact-rational assertions")
