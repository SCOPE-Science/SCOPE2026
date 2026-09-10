"""Bounded fallback probe: generic tiny-integral template on the P0=(0,1) disk.

Shows the ONLY missing piece for the preset fallback is the certified
annihilating differential (needs blocked rank equality + Coleman engine).

Uniformizer t=x at P0 (y(P0)=1 != 0, so x is a uniformizer).
y(x)=sqrt(f), f=x^5-4x+1, series over Q to order 10; for a generic
(a,b), F_{a,b}(t) = int_0^t (a+b*x)/(2y) dx termwise.
No certified annihilator (a,b) is produced: that needs Coleman integrals
of basis differentials against the MW generator, i.e. the blocked engine.
"""
from fractions import Fraction

N = 10
f = [Fraction(1), Fraction(-4), Fraction(0), Fraction(0), Fraction(0),
     Fraction(1)]
s = [Fraction(0)]*N
s[0] = Fraction(1)
for n in range(1, N):
    fn = f[n] if n < len(f) else Fraction(0)
    acc = fn - sum(s[k]*s[n-k] for k in range(1, n))
    s[n] = acc/2
u = [2*c for c in s]
w = [Fraction(0)]*N
w[0] = 1/u[0]
for n in range(1, N):
    w[n] = -sum(u[k]*w[n-k] for k in range(1, n+1))/u[0]


def Fab(a, b):
    g = [a*(w[n] if n < N else Fraction(0))
         + b*(w[n-1] if 1 <= n and n-1 < N else Fraction(0))
         for n in range(N)]
    return [Fraction(0)] + [g[n-1]/n for n in range(1, N+1)]


for ab in [(Fraction(1), Fraction(0)), (Fraction(0), Fraction(1))]:
    F = Fab(*ab)
    print(f"omega={ab}: F coeffs t^1..t^6:",
          [str(c) for c in F[1:7]])
print("FALLBACK_PROBE_OK: generic series template works; "
      "certified annihilator unavailable (blocked rank/Coleman engine)")
