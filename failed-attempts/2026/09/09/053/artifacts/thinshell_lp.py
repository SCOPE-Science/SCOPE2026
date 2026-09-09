"""Exact thin-shell variance for uniform on B_p^n.
Dirichlet-Gamma derivation:
E[X_1^2 X_2^2] = [n/(n+4)] [G(3/p)^2/G(1/p)^2][G(n/p)/G(n/p+4/p)]
E[X_1^4]     = [n/(n+4)] [G(5/p)/G(1/p)][G(n/p)/G(n/p+4/p)]
Var(sum X_i^2) = n Var(X_1^2) + n(n-1) Cov(X_1^2,X_2^2).
Report isotropic ratio s_n^2 = Var_iso(|X_iso|^2)/n, X_iso=X/sigma.
s_n^2 = Var(sum X_i^2)/(n sigma^4)."""
import math
from math import gamma

def E2(n,p): return (n/(n+2))*gamma(3/p)*gamma(n/p)/(gamma(1/p)*gamma(n/p+2/p))
def E4(n,p): return (n/(n+4))*gamma(5/p)*gamma(n/p)/(gamma(1/p)*gamma(n/p+4/p))
def E22(n,p):
    return (n/(n+4))*(gamma(3/p)**2/gamma(1/p)**2)*(gamma(n/p)/gamma(n/p+4/p))

print(f"{'n':>6} {'p':>6} {'sigma2':>10} {'E4':>12} {'E22':>12} {'Var_sum':>12} {'s_n^2':>10}")
for n in [2,5,10,20,50,100,500,2000]:
    for p in [1.0,1.25,1.5,1.75,2.0,3.0,5.0,10.0]:
        try:
            s2=E2(n,p); e4=E4(n,p); e22=E22(n,p)
            v1=e4-s2**2; c=e22-s2**2
            vsum=n*v1+n*(n-1)*c
            s2n=vsum/(n*s2**2)
            print(f"{n:>6} {p:>6} {s2:>10.6f} {e4:>12.6e} {e22:>12.6e} {vsum:>12.6e} {s2n:>10.4f}")
        except Exception as ex:
            print(n,p,"ERR",ex)
    print()
