"""Verify the square-lattice instance of the target claim.

Target: on isoradial G with rhombus angle theta_e, canonical critical weights
    p_e / (1 - p_e) = sin((pi - theta_e)/3) / sin(theta_e/3).
Check: for G = Z^2 (square lattice), theta_e = pi/2 for all edges, so the
canonical weight should be the standard critical bond value p = 1/2.
Also checks the triangular-lattice consistency value for reference.
"""
import math

def odds(theta):
    return math.sin((math.pi - theta) / 3.0) / math.sin(theta / 3.0)

def prob(theta):
    y = odds(theta)
    return y / (1.0 + y)

sq = prob(math.pi / 2)
print(f"square lattice theta=pi/2: odds={odds(math.pi/2):.12f} p={sq:.12f}")
assert abs(sq - 0.5) < 1e-12, "square lattice canonical weight must be p=1/2"

tri = prob(2.0 * math.pi / 3.0)
print(f"triangular lattice theta=2pi/3: odds={odds(2*math.pi/3):.12f} p={tri:.12f}")
# bond percolation on triangular lattice: p_c = 2 sin(pi/18)
pc_tri = 2.0 * math.sin(math.pi / 18.0)
print(f"known triangular bond p_c = 2 sin(pi/18) = {pc_tri:.12f}")
assert abs(tri - pc_tri) < 1e-12, "must match known triangular critical point"

print("OK: Z^2 with canonical weights = standard critical (p=1/2) bond percolation,")
print("so the target strictly implies square-lattice SLE(6) convergence.")
