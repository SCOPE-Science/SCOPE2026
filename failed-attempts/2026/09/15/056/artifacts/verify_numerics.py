"""Reproducible verification of the key numerics for lane-20259.

Checks (all from first principles, stdlib only):
  1. |bP^{16}| = 2^{2k-2}(2^{2k-1}-1) * num(|B_{2k}|/(4k)) with k=4 equals 8128.
  2. E8^{1016} signature realizes 8128 (Milnor bP_16 generator input).
  3. Reactivity threshold 8*8128 = 65024.
Writes results to verify_numerics.json in the same directory.
"""
import json
from fractions import Fraction

B8 = Fraction(-1, 30)          # 8th Bernoulli number
val = abs(B8) / 16             # |B8|/(4k), k=4 -> 1/480
order_bP16 = 2**6 * (2**7 - 1) * val.numerator
sig = 8 * 1016
threshold = 8 * 8128

assert str(val) == "1/480", val
assert order_bP16 == 8128, order_bP16
assert sig == 8128, sig
assert threshold == 65024, threshold
assert 8128 == 2**6 * 127

out = {
    "B8": str(B8),
    "|B8|/16": str(val),
    "|bP_16|": order_bP16,
    "factorization": "2^6 * 127",
    "E8_1016_signature": sig,
    "reactivity_threshold_8x8128": threshold,
    "Theta_15": "Z/8128 (+) Z/2",
    "status": "ALL CHECKS PASS",
}
with open("verify_numerics.json", "w") as f:
    json.dump(out, f, indent=2)
print(json.dumps(out, indent=2))
