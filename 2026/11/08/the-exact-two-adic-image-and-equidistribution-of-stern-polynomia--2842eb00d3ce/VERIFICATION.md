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

The proof constructs the entire affine residue image, proves all points are reachable, and verifies that the binary transition graph has uniform stationary measure, a single communicating class, and an aperiodic state. The full natural-density limit follows from uniform convergence on arbitrary sufficiently long binary suffix blocks.

Checks performed before acceptance: direct recurrence enumerations up to \(2^{15}\), exhaustive reachable-state and predecessor counts for moduli \(2^1\) through \(2^8\), projective branch images and inverse formulas through modulus \(2^9\), cyclic unit generation through modulus \(2^{12}\), and dyadic distributions at finite depths. Verification code: `verify.py`. All tests are finite and cannot substitute for the general proof.

Scientific limits: no claim for odd prime moduli, other Stern-polynomial evaluations, or historical uniqueness. Independent audit: not performed.
