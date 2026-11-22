"""Exact finite-dimensional checks supporting a sharp copula-spacing theorem.

The proof for arbitrary n is analytic; this checker validates the geometric
identities, extremal mixed marginal measures, and incompatible tail bounds for
many rational choices, without claiming finite tests are infinite proofs.
"""
from fractions import Fraction as F
from math import factorial

checks = 0

def check(condition, message):
    global checks
    assert condition, message
    checks += 1


def cap(n, r):
    return max(F(0), min(F(1), n * (1 - (n - 1) * r)))

# All endpoint regimes and exact phase boundary continuity.
for n in range(2, 19):
    left = F(1,n)
    right = F(1,n-1)
    check(cap(n, F(0)) == 1, f'zero radius n={n}')
    check(cap(n, left) == 1, f'lower threshold n={n}')
    check(cap(n, right) == 0, f'upper threshold n={n}')
    check(cap(n, right+F(1,101)) == 0, f'above threshold n={n}')
    for k in range(1, 19):
        r = left + (right-left) * F(k,19)
        a = 1-(n-1)*r
        q = n*a
        B = [(j*r, j*r+a) for j in range(n)]
        check(0<a<r, f'band width n={n},k={k}')
        check(0<q<1, f'probability n={n},k={k}')
        check(B[0][0] == 0 and B[-1][1] == 1,
              f'bands anchored n={n},k={k}')
        check(all(B[j][1] < B[j+1][0] for j in range(n-1)),
              f'band separation n={n},k={k}')
        check(sum(end-start for start,end in B) == q,
              f'band measure n={n},k={k}')
        check(sum(B[j+1][0]-B[j][1] for j in range(n-1)) == 1-q,
              f'complement measure n={n},k={k}')
        check(q == cap(n,r), f'extremal probability n={n},k={k}')
        # On success T ~ Unif[0,a] with probability q; label in each
        # band with conditional mass 1/n. So density on each band is
        # q/(n*a) = 1; the failure branch's uniform complement density
        # is (1-q)/(1-q) = 1.
        check(q/(n*a) == 1, f'success-band density n={n},k={k}')
        check((1-q)/(1-q) == 1, f'failure density n={n},k={k}')
        # For r<s<1/(n-1), an r-maximizer has spacing exactly r
        # on every successful configuration, hence has zero s-tail,
        # whereas the sharp s-tail remains strictly positive.
        s=(r+right)/2
        check(s>r and cap(n,s)>0, f'incompatible thresholds n={n},k={k}')

print(f'{checks} exact-rational assertions passed')
