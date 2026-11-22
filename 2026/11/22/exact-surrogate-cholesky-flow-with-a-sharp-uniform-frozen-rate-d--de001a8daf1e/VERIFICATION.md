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

# Verification of the exact scalar surrogate coefficient

Run `python verify.py`. The standalone checker uses only the Python 3 standard library. It returned `VERIFY_OK 452 finite_checks q= 0.78693868057473315` for the packaged source, exercising the ODE solution, the parameter-uniform coefficient and Schur-complement inequalities, sharpness sequences, and PSD examples.

The analytic derivative identity, logarithmic-convexity argument and Schur-complement induction in `RESULT.md` are the actual evidence for universal assertions. A finite checker is not an exhaustive proof. These checks do not establish floating-point backward stability or comparative matrix reconstruction accuracy. No independent mathematical audit has been performed.
