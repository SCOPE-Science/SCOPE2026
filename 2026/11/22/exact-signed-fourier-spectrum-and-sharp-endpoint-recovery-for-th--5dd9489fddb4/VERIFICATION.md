---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact finite verification

The accompanying `verify.py` (standard-library only) exhaustively computes all \(2^{13}=8192\) normalized independent edge-sign configurations of the order-three Aztec diamond. A deterministic spanning tree removes the \(2^{23}\)-fold vertex-switch gauge redundancy. Each normalized signed perfect-matching sum is compared against a separately evaluated 12-by-12 integer Kasteleyn determinant using fraction-free elimination. All values agree.

The script asserts the entire normalized signed table, the complete sign-symmetrized spectrum, the full convolution rank and nullity, the sharp surviving gap, Parseval, the exact inverse Walsh projection kernel and its \(\ell^1\)-norm numerator \(164610\), and an independent inverse-transform identity. It also checks that eight of the 36 singleton frequencies vanish.

Invocation: `python3 verify.py`.

All checks are exact integers. The proof of uniqueness and norm optimality uses the gauge-action and translation-averaging arguments in `RESULT.md`. The finite computational checks do not establish statements for larger Aztec diamonds. Independent external validation has not been performed.
