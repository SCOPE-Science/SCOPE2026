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

# Verification and limitations

The mathematical proof is in `RESULT.md`, including the complete domain, exact normalizations, all branch and return formulas, derivative shape, fold uniqueness, invariant measures, and a critical cubic expansion. The standalone Python 3 checker is `verify_cosine_cusp.py`; run with `python3 verify_cosine_cusp.py` in the package directory.

The checker exercises a rational-parameter witness, verifies the original two-step map, confirms exactly three numerically located orbit points and the three multiplier signs, checks analytical cusp equations, the cubic coefficient and representative critical relaxation. The rational Taylor inequalities provide independent sign certificates for sample return values. These are finite diagnostics; parameter-uniform and asymptotic assertions rest on the analytic proof, not sampling.

The original published map and related statements are referenced in `RESULT.md`. The proof is restricted to \(0<c<b<a<1\); the full fold positions are uniquely defined, generally transcendental. Published-equivalence risk remains beyond inspected sources, and an independent audit is not performed.
