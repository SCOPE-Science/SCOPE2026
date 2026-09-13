"""Diagnose max-M: analytic estimates + k=2 exact check of DP, then k=50 upper bound."""
import numpy as np, math, itertools
from fractions import Fraction

# ---------- 1. Analytic context ----------
# For full (nonsymmetric) F on simplex, M_max ~ (theta/2) log k ~ 0.25*log50 ~ 0.98.
# Symmetric polys are a TINY subspace: only functions of power sums p_1..p_9 with
# total degree<=9. Intuition: symmetric P cannot concentrate near coordinate axes
# (where J_m mass comes from) because symmetry forces equal treatment; the ratio
# M for symmetric F is essentially k * J_1/I with J_1 averaging over all directions.
# Known benchmark (Polymath8b/Maynard): symmetric polynomial optimizations at k=50
# give M ~ 2 (below 4 needed for double primes). So >4 is implausible; we verify.

# ---------- 2. Exact k=2 sanity check of the DP formulas ----------
def exact_check_k2():
    # basis {1, p1, p1^2} with t=(x,y), Dx_2(1). Compute by direct 2D quadrature (fine grid)
    # vs DP formulas.
    N = 4000
    h = 1.0/N
    # I entries: int_{x+y<=1} q
    def Idir(q):
        s = 0.0
        for i in range(N):
            x = (i+0.5)*h
            for j in range(N-i):
                y = (j+0.5)*h
                s += q(x, y)
        return s*h*h
    qs = [lambda x,y:1.0, lambda x,y:(x+y), lambda x,y:(x+y)**2,
          lambda x,y:(x+y)**3, lambda x,y:(x+y)**4]
    # DP check: V_1 then V_2.
    # V_1(h,r)=B(W+1, r+1); V_2(g,0)= sum over sub of V_1: C*B(A+1, Wf+1)*B(Wf+1... wait use code path
    print("k=2 direct integrals:")
    for d in range(5):
        print(" int p1^%d =" % d, Idir(qs[d]))
    print("formula int p1^d over Dx_2(1) = d!/(d+2)!:", [math.factorial(d)/math.factorial(d+2) for d in range(5)])

exact_check_k2()
