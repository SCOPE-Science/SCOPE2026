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

# Computational verification and reproducibility

Run `python verify.py` with Python 3 and installed `sympy`, `scipy`, `numpy`. The checker performs exact symbolic assertions for the full reciprocal derivative, the matched-rate identity, rigidity conditions, the second-order activity coefficient, and non-unit parameter cases. It also integrates independent numerical initial-value problems for three unequal/equal relaxation-rate ratios, comparing the fitted logarithmic correction to the analytic predictions, and checks an exact affine-time observable at sampled times.

The analytic proof in RESULT.md, not the integrations, supports the infinite-time statements. Finite tests do not establish uniqueness of published claims or a general mathematical theorem. No independent audit or independent scientific validation has been performed.
