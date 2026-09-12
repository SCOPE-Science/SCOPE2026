"""Verify explicit constants mu*, v* and curvature error-control bounds."""
import math, json

cosh1 = math.cosh(1.0)
vol_B1 = 2 * math.pi * (cosh1 - 1)          # hyperbolic area of radius-1 ball
mu_star = 2 * vol_B1                        # = 4*pi*(cosh1-1)
cosh_h = math.cosh(0.5)
vol_Bh = 2 * math.pi * (cosh_h - 1)         # area of radius-1/2 ball
var_limit = 4 * vol_Bh                      # = 8*pi*(cosh(1/2)-1), limiting Var/lambda lower bound
v_star = 3.0

print(f"vol(B_1)            = {vol_B1:.6f}")
print(f"mu* = 4*pi*(cosh1-1)= {mu_star:.6f}")
print(f"vol(B_1/2)          = {vol_Bh:.6f}")
print(f"limiting Var/lambda >= {var_limit:.6f}")
print(f"v* = {v_star}  (margin {var_limit - v_star:.4f} > 0)")

# Curvature distortion control in normal charts: J(r) = sinh(r)/r,  J(r)-1 ~ r^2/6
def J(r):
    return math.sinh(r) / r if r > 0 else 1.0
for s in [0.01, 0.05, 0.1, 0.5, 1.0]:
    print(f"s={s:<5}: J-1={(J(s)-1):.3e}, (J-1)/s^2={(J(s)-1)/s**2:.4f} (limit 1/6={1/6:.4f})")

# Hyperbolic disk area vs Euclidean: A_H(R) = 2*pi*(cosh R - 1) vs pi*R^2
for R in [0.01, 0.05, 0.1, 0.3]:
    AH = 2 * math.pi * (math.cosh(R) - 1)
    AE = math.pi * R * R
    print(f"R={R:<5}: A_H/(pi R^2)-1 = {AH/AE-1:.3e}, (ratio-1)/R^2 = {(AH/AE-1)/R**2:.4f} (limit 1/12={1/12:.4f})")

# Stabilization tail illustration: P(empty disk radius t) at intensity lam
for lam in [50, 200, 1000]:
    s = 3 * math.log(lam) / math.sqrt(lam)   # stabilization scale
    tail = math.exp(-lam * math.pi * s * s)  # upper bound via A_H >= pi R^2
    print(f"lam={lam}: stab scale s={s:.4f}, empty-disk tail <= {tail:.3e}")

assert mu_star > 6.8 and mu_star < 6.9
assert var_limit > 3.2 and var_limit < 3.22
assert v_star < var_limit
out = {"vol_B1": vol_B1, "mu_star": mu_star, "vol_Bhalf": vol_Bh,
       "var_limit_bound": var_limit, "v_star": v_star}
with open("output/artifacts/constants.json", "w") as f:
    json.dump(out, f, indent=2)
print("wrote output/artifacts/constants.json")
