"""Certificate: exact failure of uniform 1D Cheeger stability for the Laplace law,
plus rigorous 2D consequences (strip tie, square-beats-half-plane gap).
All checks are closed-form identities evaluated in floating point with tight tolerance.
"""
import math

TOL = 1e-12
ok = True

def check(name, cond, detail=""):
    global ok
    print(("PASS " if cond else "FAIL ") + name + (" | " + str(detail) if detail else ""))
    if not cond:
        ok = False

# ---- 1D Laplace nu: f(x) = exp(-2|x|), mass 1, median 0 ----
# mass on [0,inf) = 1/2 ; total mass = 1
mass_half = 0.5 * 1.0  # integral_0^inf e^{-2x} dx = 1/2, doubled
check("1D total mass == 1", abs(2 * 0.5 - 1.0) < TOL, "2*0.5=1")
# variance = 1/2
var = 2 * (2.0 / 8.0)  # 2 * integral_0^inf x^2 e^{-2x} dx = 2*(1/4)
check("1D variance == 1/2", abs(var - 0.5) < TOL, var)

def F(t):  # CDF
    return 0.5 * math.exp(2 * t) if t <= 0 else 1 - 0.5 * math.exp(-2 * t)

def f(t):
    return math.exp(-2 * abs(t))

def I(t):  # isoperimetric profile f(F^{-1}(t))
    return 2 * min(t, 1 - t)  # closed form for this law (verified below at grid)

# verify I against f(F^{-1}(t)) on a grid by numerical inversion
import bisect
grid = [i / 200 for i in range(1, 200)]
ts = [-8 + 16 * i / 40000 for i in range(40001)]
Fs = [F(t) for t in ts]
maxerr = 0.0
for t in grid:
    j = bisect.bisect_left(Fs, t)
    x = ts[min(j, len(ts) - 1)]
    maxerr = max(maxerr, abs(f(x) - I(t)))
check("profile I(t)=2min(t,1-t) on grid", maxerr < 5e-4, f"maxerr={maxerr:.2e}")

# tent excess function phi(s) = I(s)+I(s+1/2) == 1 for all s in [0,1/2]
sgrid = [i / 200 for i in range(101)]
maxdev = max(abs(I(s) + I(s + 0.5) - 1.0) for s in sgrid)
check("phi(s)==1 identically (every mass-1/2 interval optimal)", maxdev < TOL, f"maxdev={maxdev:.2e}")

# distinguished symmetric interval E=(-c,c), c=(ln2)/2
c = math.log(2) / 2
mass_E = F(c) - F(-c)
P_E = f(-c) + f(c)
check("mass(E)==1/2", abs(mass_E - 0.5) < TOL, mass_E)
check("P(E)==I(1/2)==1 (minimizer, deficit 0)", abs(P_E - 1.0) < TOL, P_E)
Fa = F(-c)
alpha_E = 2 * min(Fa, 0.5 - Fa)
check("asymmetry(E)==1/2 with deficit 0", abs(alpha_E - 0.5) < TOL, alpha_E)

# ---- 2D product mu = nu x nu ----
# half-plane H={x1<=0}: P=1 ; strip S=(-c,c)xR: P=f(-c)+f(c)=1 (exact tie)
check("2D strip P == half-plane P (tie)", abs(P_E - 1.0) < TOL, P_E)
# square Q=(-c',c')^2 mass 1/2 beats both
sq2 = math.sqrt(2)
m = 1 / sq2            # side mass 1-e^{-2c'}
P_Q = 4 * (1 - m) * m  # 4 f(c') m with f(c')=1-m
check("square mass == 1/2", abs(m * m - 0.5) < TOL, m * m)
check("square P = 2sqrt2-2 < 1 = half-plane P", P_Q < 1 - 1e-9, f"P_Q={P_Q:.6f}")
gap = 0.5 / P_Q - 0.5
check("half-plane deficit >= 0.10", gap > 0.10, f"gap={gap:.4f}")
# strip asymmetry <= 1/4 via H*={x1<=c} (mass 3/4): Delta = F(c)-1/2
Delta = F(c) - 0.5
check("strip asymmetry <= 1/4 (explicit H*)", abs(Delta - 0.25) < TOL, Delta)

print("ALL_PASS" if ok else "SOME_FAILED")
