"""Exact isotropic moments for uniform on B_p^n via Beta-Gamma formula.
E|X_1|^r = [n/(n+r)] G(1/p+r/p) G(n/p) / [G(1/p) G(n/p+r/p)].
Cross-check p=1,r=2 against direct simplex integration 2/((n+1)(n+2)).
Also tabulate L_K^2 = V^{-2/n} sigma^2, V=(2G(1+1/p))^n/G(1+n/p)."""
import math
from math import gamma

def E_abs_r(n,p,r):
    return (n/(n+r))*gamma(1/p+r/p)*gamma(n/p)/(gamma(1/p)*gamma(n/p+r/p))

def vol(n,p):
    return (2*gamma(1+1/p))**n/gamma(1+n/p)

print("check p=1,r=2 vs 2/((n+1)(n+2)):")
for n in [1,2,3,5,10,50]:
    a=E_abs_r(n,1.0,2); b=2/((n+1)*(n+2))
    print(f" n={n} formula={a:.12f} direct={b:.12f} diff={abs(a-b):.2e}")
    assert abs(a-b)<1e-9
print("ISOTROPIC_R2_OK")

print("\nsigma^2=E X_1^2 and L_K^2 table:")
print(f"{'n':>5} {'p':>5} {'sigma2':>12} {'L_K^2':>10} {'L_K':>8}")
for n in [2,5,10,50,200,1000]:
    for p in [1.0,1.25,1.5,1.75,2.0]:
        s2=E_abs_r(n,p,2)
        V=vol(n,p)
        LK2=(V**(-2/n))*s2
        print(f"{n:>5} {p:>5} {s2:>12.6f} {LK2:>10.6f} {math.sqrt(LK2):>8.4f}")
