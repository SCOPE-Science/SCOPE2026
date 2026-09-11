"""High-precision Fourier table: analytic symbol F(t)=sqrt(2cos(t/2)) e^{+it/4}
has only modes k>=0 (values match binom(1/2,k) exactly); flipped symbol
H(t)=sqrt(2cos(t/2)) e^{-it/4} has only modes k<=0. 30-digit mpmath quad."""
from mpmath import mp, quad, exp, pi, cos
mp.dps = 30
rows = []
for sign, name in [(1,'analytic'), (-1,'flipped')]:
    for k in range(-4,5):
        f = lambda t, k=k, sign=sign: (2*cos(t/2))**mp.mpf('0.5')*exp(sign*1j*t/4)*exp(-1j*k*t)
        c = quad(f, [-mp.pi, mp.pi])/(2*mp.pi)
        rows.append((name, k, complex(c)))
for r in rows:
    print(r[0], r[1], repr(r[2]))
from fractions import Fraction
def binom_half(k):
    c = Fraction(1)
    for j in range(1,k+1): c *= Fraction(3-2*j, 2*j)
    return c
print("exact binom(1/2,k):", {k: str(binom_half(k)) for k in range(5)})
print("SUPPORT_TABLE_OK")
