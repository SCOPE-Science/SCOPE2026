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

# Verification

The equality of the three root orders with Frobenius orbit lengths is proved in `RESULT.md`. The characteristic-sensitive incidence corrections follow from the exact identity \(BD=-A\), with the characteristic-two collapse described in the proof. The finite-field checker `verify_tangent_union.py` independently constructs polynomial-basis finite fields and counts projective rational zeros of the explicit defining polynomial.

Command: `python3 verify_tangent_union.py`.

Observed final line: `VERIFY_HYPERFLEX_TANGENT_MOTIVE_OK`.

Verified cases: every admissible ordered coefficient triple for \(q=5,7,8,9\) and \(n=2\); twelve sample triples for \(q=11,13\) and \(n=2\); every admissible triple for \(q=7\) and \(n=3\); and every triple over the base fields \(q=5,7,8,9\). The code uses exact operations, not floating point. Finite tests corroborate but do not establish the general statement, which rests on the explicit proof. The arithmetic-priority risk and the lack of independent mathematical audit remain.
