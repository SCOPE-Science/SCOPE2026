"""Decision-phase exact certificate check for lane-1004.

Uses ONLY exact integer/Fraction arithmetic (no floats) to test the strongest
target-adjacent alternative available after the target blocked:
  (A) head lemma: twisted bound holds for 1<=q<=312 via odd-integer norm;
  (B) weak global theorem: max >= 1/(54q) for all q>=1 via one-coordinate norm.
Both checkable here; the question is whether either independently passes Audit
(originality/value), not just correctness. Results -> exact_cert.json.
"""
from fractions import Fraction
import json

# Rigorous upper bound u > sqrt(2): u^2 > 2 checked in integers.
u = Fraction(141422, 100000)
assert 141422 * 141422 > 2 * 100000 * 100000, "u^2 must exceed 2"
a = 32 * u  # 45.25504 exactly

# (A) Head coverage: sufficient exact condition 640000*q >= (a*q+8)^2.
covered = [q for q in range(1, 2000) if 640000 * q >= (a * q + 8) ** 2]
head_ok = covered == list(range(1, 313))
fails_at_313 = not (640000 * 313 >= (a * 313 + 8) ** 2)

# (B) Weak global bound: needs (54 - a)*q >= 8 for all q>=1; worst at q=1.
weak_ok = (Fraction(54) - a) * 1 >= 8  # 8.74496 >= 8

out = {
    "sqrt2_upper_bound": str(u),
    "integer_check_u2_gt_2": True,
    "head_covered_q": [covered[0], covered[-1], len(covered)] if covered else [],
    "head_is_exactly_1_to_312": bool(head_ok),
    "bound_fails_at_313": bool(fails_at_313),
    "weak_global_c": "1/54",
    "weak_global_holds_all_q": bool(weak_ok),
    "method_class": "single-coordinate quadratic integer norm only; exponent 1, no joint/spectral input",
}
with open("exact_cert.json", "w") as f:
    json.dump(out, f, indent=1)
print(json.dumps(out, indent=1))
assert head_ok and fails_at_313 and weak_ok
print("EXACT_OK")
