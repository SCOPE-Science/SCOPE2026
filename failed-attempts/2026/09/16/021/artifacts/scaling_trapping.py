"""Verify scaling criticality, virial coefficient, Pohozaev/energy identities,
and quantitative energy-trapping + virial coercivity for the 3D focusing
energy-critical generalized Hartree family (d=3, p=3+alpha, 0<alpha<3)."""
import json
import sympy as sp

a = sp.symbols('a', positive=True)
p = 3 + a  # energy-critical power in d=3

# (1) Hdot1 dilation u_l(x) = l^{1/2} u(l x): grad norm scales l^0.
# D(f) = iint |x-y|^{-(3-a)} |f(x)|^p |f(y)|^p scales l^{p-3-a}.
d_exp = sp.simplify(p - 3 - a)
assert d_exp == 0, d_exp
print("Hdot1-scaling exponent of D:", d_exp, "-> energy-critical iff p=3+a. OK")

# (2) L^2 dilation u^mu(x) = mu^{3/2} u(mu x): grad -> mu^2, D -> mu^{3p-3-a}.
l2_exp = sp.simplify(3 * p - 3 - a)   # = 6+2a at p=3+a
print("L2-scaling exponent of D:", l2_exp)
coef = sp.simplify(l2_exp / (2 * p))  # d/dmu E(u^mu)|1 = ||grad||^2 - coef*D
assert coef == 1, coef
print("virial coefficient (3p-3-a)/(2p) =", coef, "-> K(u)=||grad||^2-D(u). OK")

# (3) Pohozaev for ground state: ||grad W||^2 = D(W);
# E(W) = (1/2-1/(2p))||grad W||^2 = (p-1)/(2p)||grad W||^2.
Efrac = sp.simplify((p - 1) / (2 * p))
print("E(W)/||grad W||^2 =", Efrac)

# (4) Trapping: y=||grad u||^2/||grad W||^2, E >= (||gradW||^2/2)(y-y^p/p).
# Given E <= (1-d0)E(W), y(0)<1 => y(t) <= y_max<1; coercivity c=1-y_max^{p-1}.
def trapping(alpha, d0=0.1):
    pp = 3 + alpha
    target = (1 - d0) * (pp - 1) / pp  # (y - y^p/p) threshold, normalized
    lo, hi = 0.0, 1.0 - 1e-12
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if mid - mid**pp / pp < target:
            lo = mid
        else:
            hi = mid
    y_max = 0.5 * (lo + hi)
    return y_max, 1 - y_max ** (pp - 1)

out = {}
for alpha in [0.5, 1.0, 2.0]:
    y_max, c = trapping(alpha)
    out[str(alpha)] = {"p": 3 + alpha, "y_max": y_max, "coercivity_c": c,
                       "Efrac": float((2 + alpha) / (2 * (3 + alpha)))}
    print(f"alpha={alpha}: p={3+alpha}, y_max={y_max:.6f}, K>=c||grad||^2 c={c:.6f}")
    assert y_max < 1 and c > 0

with open("trapping_summary.json", "w") as f:
    json.dump(out, f, indent=2)
print("WROTE trapping_summary.json")
