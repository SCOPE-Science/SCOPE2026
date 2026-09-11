"""Route B (analytic gap computation): Frostman/energy tensorization is
quantitatively insufficient to close the Mattila tail -- even granting the
optimal formal pointwise spherical majorant.

s0 = dim_H E0 = 2 ln6/ln20. Granted majorant: sigma(t) <= C t^{-(s0-1)}.
Mattila tail [T,oo): int sigma^2 t dt <= C^2 int_T^oo t^{1-2(s0-1)} dt.
Converges iff 1-2(s0-1) < -1 iff s0 > 2 (impossible in the plane).
Closing via ANY uniform majorant sigma(t) <= C t^{-g} needs g > 1.
"""
import math

s1 = math.log(6) / math.log(20)
s0 = 2 * s1
alpha = s0 - 1            # granted-majorant exponent
tail_exp = 1 - 2 * alpha  # exponent of t in majorant integrand
gap = 1.0 - alpha         # distance from granted exponent to needed g>1

print("ROUTE B GAP LEDGER")
print(f"factor dim  = {s1:.6f}")
print(f"s0 = dim E0 = {s0:.6f}")
print(f"granted-majorant exponent alpha = s0-1 = {alpha:.6f}")
print(f"majorant integrand ~ t^{tail_exp:+.6f}  ->  partial tail to R grows ~ R^{tail_exp+1:.4f}")
print(f"exponent gap to Mattila-closure need (g>1): {gap:.6f}")
print(f"Iosevich-Liu check: sA+sB+max = {3*s1:.6f} < 2  (gap {2-3*s1:.6f})")
print(f"Guth-Iosevich-Ou-Wang check: dim {s0:.6f} < 5/4 (gap {1.25-s0:.6f})")
print("OUTCOME: BLOCKED -- energy/Frostman input misses closure by 0.80 in exponent;")
print("no pointwise input available from Frostman alone. Route abandoned.")
