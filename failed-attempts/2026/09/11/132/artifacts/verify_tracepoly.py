"""Verify T(x^3-2) is divisible by f(x), i.e. T(tau)=0 for tau=x0^3-2. Stdlib only."""
from fractions import Fraction
# f(x) = x^5 - x^4 + x^3 + 0 x^2 + 2x^2... careful: f = x^5-x^4+x^3+2x^2+0x-1 (asc)
f = [Fraction(-1), Fraction(0), Fraction(2), Fraction(1), Fraction(-1), Fraction(1)]
# T(w) asc: 289 + 527w + 367w^2 + 120w^3 + 18w^4 + w^5
T = [Fraction(289), Fraction(527), Fraction(367), Fraction(120), Fraction(18), Fraction(1)]
# u(x) = x^3 - 2 asc
u = [Fraction(-2), Fraction(0), Fraction(0), Fraction(1)]
def pmul(p, q):
    r = [Fraction(0)]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i+j] += a*b
    return r
def padd(p, q):
    n = max(len(p), len(q))
    r = [Fraction(0)]*n
    for i, a in enumerate(p): r[i] += a
    for i, a in enumerate(q): r[i] += a
    return r
# compose T(u): Horner with poly arithmetic
H = [Fraction(0)]
for c in reversed(T):
    H = padd(pmul(H, u), [c])
print("deg T(x^3-2) =", len(H)-1)
# reduce mod f (monic deg 5)
R = list(H)
while len(R) > 5:
    c = R[-1]
    k = len(R)-6  # x^k * f has degree k+5 = len(R)-1
    for i in range(6):
        R[k+i] -= c*f[i]
    while R and R[-1] == 0: R.pop()
print("remainder =", [str(v) for v in R])
assert all(v == 0 for v in R), "T(x^3-2) not divisible by f"
print("TRACEPOLY_OK")
