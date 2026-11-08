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

# Verification notes

The accompanying `VERIFY.py` is standalone apart from SymPy. It checks the five chart substitutions symbolically, enumerates all 21 allowed binary coordinate-support patterns (not assumed to prove the full singular theorem), computes the Jacobian rank at each torus representative, and verifies that the singular supports correspond to the two coordinate lines and two isolated coordinate points.

The unrestricted claim is justified by the five-chart proof and the scroll-cone divisor-class argument in `RESULT.md`. The algebraic input that the four quadrics generate the prime ideal and that the full relation variety is the indicated projective cone is taken from Example 3.8 of arXiv:2610.37351v1. Independent review and any verification beyond the documented calculations are not performed.
