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

# Verification procedure and limits

Run `python verify.py` using Python 3 and SciPy as declared in `requirements.txt`. The script implements the published definition of FJR+ as a linear program with normalized total candidate weight, and separately evaluates the four-test closed formula. It tests every pair of distinct approval sets and every committee when the candidate count is two or three and both type populations belong to \(\{1,2,3\}\), then tests deterministic pseudorandom cases up to seven candidates. It also enumerates the FJR comparison sets for the explicit separation and checks all EJR+ inequalities.

Observed result: 3,852 complete small cases and 1,653 pseudorandom cases agreed; the separate FJR and EJR+ checks passed for the example, and the published fractional system detected its level-four violation. A direct exact rational witness is provided in `RESULT.md`. Computational agreement cannot replace the universal argument, which is based on type symmetrization, a sharp candidate-weight lower bound and fractional-linear endpoint optimization.

This is the scope of the reproducibility work. It does not establish global literature uniqueness, validate claims about three or more ballot types, or constitute independent mathematical validation.
