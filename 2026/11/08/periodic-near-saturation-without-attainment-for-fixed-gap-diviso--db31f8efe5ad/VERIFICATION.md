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

Run `python3 verify.py` with Python's standard library. The test enumerates exact CRT weights for primorial moduli up to \(2310\), verifies each against the independent gcd-based finite-sum formula, constructs residue-graph covers for multiple separations, and checks the resulting weight inequalities. It also computes the exact optimum \(927/1225\) for the length-\(210\) weighted cycle by a two-boundary-state dynamic program. The expected marker is `VERIFY_OK`.

These are finite reproducibility checks. The infinite periodic approximation follows from the proved elementary fixed-modulus asymptotic, CRT/Hellinger product, and the classical Mertens estimate. No external audit has been performed.
