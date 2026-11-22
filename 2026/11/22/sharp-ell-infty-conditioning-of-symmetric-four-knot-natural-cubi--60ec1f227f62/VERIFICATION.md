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

The exact cardinal-spline identities and derivatives in RESULT.md form the mathematical proof. The standalone `verify.py` uses symbolic algebra to reconstruct these expressions and checks the two competing maxima and crossing relation. Direct rational-data interpolation checks supplement the symbolic derivation. Numerical root values and sample-grid checks do not certify novelty or substitute for the proof for all positive mesh ratios.

Run from the directory containing the files: `python verify.py` (Python 3 with SymPy 1.14 or compatible). Recorded successful output is `verification_output.txt`. The scope excludes asymmetric knots, other natural-spline end conditions, and extrapolation outside the knot interval.
