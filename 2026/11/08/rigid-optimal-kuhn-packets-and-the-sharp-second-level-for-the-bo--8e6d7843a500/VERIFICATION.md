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

# Verification performed

The exact rational script `checker.py` was executed with the standard Python interpreter. It produced PASS and checked the short lattice vector shell, the finite compatible-frame count, every optimal permutation simplex centroid calculation, and the six explicit balls for the second-level frame. These finite checks corroborate the analytic finite reduction; they are not a proof for arbitrary frames on their own.

The analytic proof establishes the quantifier over all independent BCC lattice triples by proving that any frame of packet radius strictly below \(1/\sqrt2\) has all seven nonempty subset sums inside an explicit 14-vector shell. The sign-parity case split classifies the entire shell without numerical approximations. The exact gap follows from the next possible squared lattice-vector length and an explicit attaining frame.

A separate external mathematical audit has not been performed. Historical novelty remains provisional.
