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

Numerical diagnostic replay: run `python verify_napkin.py` using Python 3, NumPy and SciPy. The verification script uses independent integration of the proposed hole's cross-sectional widths, independently evaluates the original three-dimensional ray-support condition, checks the \(3/2\) asymptotic coefficient with decreasing angular deficits, and integrates the isotropic visibility indicator. Observed result: `PASSED 6824 numerical diagnostic assertions; analytic proof independent`.

The complete mathematical proof is in `RESULT.md` and does not use finite sampling as a substitute for universal arguments. Exact checks use closed ray membership, concavity and superlevel intervals, area integration, and local Taylor expansion. Sampling does not rigorously validate infinitely many radii or angles. Historical originality remains subject to independent research review.
