"""Reproducible exact sign certificate and finite diagnostics for Gaussian band landing.

Run with Python 3 standard library. The general theorem is proved in RESULT.md;
finite numerical checks here are not an infinite-domain proof.
"""
from fractions import Fraction
from math import exp, erf, sqrt, log, isfinite

count = 0

def check(condition, message):
    global count
    assert condition, message
    count += 1

def poly(z):
    return z - 2*z**4 + 8*z**64 - 12*z**144

# Exactly rational witnesses of the three sign changes. No floating-point here.
locations = [(3, 5, +1), (7, 8, -1), (49, 50, +1), (199, 200, -1)]
for n, d, sign in locations:
    p = poly(Fraction(n, d))
    check((p > 0) if sign > 0 else (p < 0), f"incorrect sign at {n}/{d}")

# Exact polynomial degree structure and Descartes sign pattern (independent of floats).
terms = [(1, Fraction(1)), (4, Fraction(-2)), (64, Fraction(8)), (144, Fraction(-12))]
check([power for power, _ in terms] == [1, 4, 64, 144], "bad polynomial exponents")
check([1 if c > 0 else -1 for _, c in terms] == [1, -1, 1, -1], "bad signs")

# Floating-point demonstrations, not proofs.
def derivbracket(s, bands):
    return sum(a*exp(-a*a/(2*s*s))-b*exp(-b*b/(2*s*s)) for a,b in bands)

def probability(s, bands):
    return sum(erf(b/(sqrt(2)*s))-erf(a/(sqrt(2)*s)) for a,b in bands)

def bisect(f, left, right, iterations=100):
    fl, fr = f(left), f(right)
    check(fl * fr < 0, "root not bracketed")
    for _ in range(iterations):
        mid = (left + right)/2
        if f(mid) * fl > 0:
            left, fl = mid, f(mid)
        else:
            right = mid
    return (left+right)/2

bands = [(1,2),(8,12)]
roots = [bisect(lambda s:derivbracket(s,bands), a,b) for a,b in [(1,2),(2,5),(5,10)]]
expected = [1.471072558380158, 3.7783833788152963, 8.02022034691668]
for root, target in zip(roots, expected):
    check(abs(root-target) < 2e-9, "numerical root mismatch")
    check(isfinite(probability(root, bands)), "nonfinite probability")
check(probability(roots[0],bands)>probability(roots[1],bands), "first peak")
check(probability(roots[2],bands)>probability(roots[1],bands), "second peak")

s0=sqrt(3/(2*log(2)))
check(abs(s0-1.471068510074716)<1e-12, "single-band optimum formula")
check(abs(exp(2/s0**2)-2**(4/3)) < 1e-12, "boundary coefficient identity")

# Finite asymptotic illustrations: compare two local branch maxima in two scale windows.
def golden_max(f,lo,hi,iterations=120):
    ratio=(sqrt(5)-1)/2
    x1=hi-ratio*(hi-lo); x2=lo+ratio*(hi-lo)
    for _ in range(iterations):
        if f(x1)<f(x2):
            lo=x1; x1=x2; x2=lo+ratio*(hi-lo)
        else:
            hi=x2; x2=x1; x1=hi-ratio*(hi-lo)
    s=(lo+hi)/2
    return s,f(s)

def tie_for_R(R):
    def gap(q):
        b=[(1,2),(R,R*q)]
        sn,vn=golden_max(lambda s:probability(s,b),1,2)
        sf,vf=golden_max(lambda u:probability(R*u,b),1,3)
        return vf-vn
    return bisect(gap,1.5,2)

for R in [16,32,64,128]:
    q=tie_for_R(R)
    check(1.5<q<2,"tie width out of bounds")
    check(abs(R*(2-q)-2**(4/3)) < 0.2, "slow asymptotic convergence")

print(f"{count} checks passed; rational sign certificate exact; other diagnostics finite.")
print("Two-band stationary scales:", ', '.join(f'{r:.12f}' for r in roots))
