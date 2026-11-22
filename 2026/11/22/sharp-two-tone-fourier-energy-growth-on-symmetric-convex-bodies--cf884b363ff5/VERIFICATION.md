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

The analytic proof is contained in RESULT.md and does not depend on numerical sampling. The exact two-eigenvalue reduction is obtained by expanding the squared modulus of the two-tone sum under central symmetry; every remaining inequality follows from positive scalar derivatives and the explicit unimodal-mixture representation.

Execute `python3 CHECK.py` (Python standard library only); it passed 18,308 deterministic checks of cube and non-product diamond examples, exact Gram-eigenvalue formulas, arbitrary complex coefficients, near-collision sharpness and the fourth-to-second moment asymptotic coefficient. These checks cover only selected values and are not an exhaustive or independent mathematical verification.
