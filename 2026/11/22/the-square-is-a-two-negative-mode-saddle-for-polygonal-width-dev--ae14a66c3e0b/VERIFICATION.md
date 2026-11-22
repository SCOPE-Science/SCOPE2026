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

# Reproducibility and limits

Run `python3 verify.py` after extracting this record's seven complete files. Python 3 with SymPy is required. The checker performs exact symbolic differentiation of the explicit adjacent-edge-pair formula and confirms the entire 4×4 Hessian and stationary point; it checks 56 direct maximum-minus-minimum angular quadratures using 8,192 midpoint directions each against the independent full kernel and local Taylor expression, then runs 250 randomized parallelogram comparisons. Expected marker: `VERIFY_OK 306 second-order Hessian and independent width quadratures`. It was obtained using the exact code embedded with this result.

The derivation in RESULT.md, not those finite tests, proves all assertions for sufficiently small real perturbations. No finite computation certifies an unrestricted classification or the behavior along quadratic null directions. A published source proves the known edge-pair moment kernel. Independent scientific audit is not performed.
