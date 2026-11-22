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

The mathematical argument is in `RESULT.md`, Steps 1–4. The separately runnable `verify.py` checks closed kernel integrals, monotonicity on a finite grid and the two-by-two Gaussian conditioning identity, then compares optimized symmetric pairs against a finite grid of candidate separations for eight positive noise variances. `verification_output.txt` records the observed output. No finite grid validates uniqueness on the continuum; the analytic derivative inequalities supply that conclusion. The independently performed scientific audit remains absent.

`symbolic_check.py` is an optional exact-algebra check requiring SymPy; `symbolic_output.txt` reports successful simplification of the mean derivative, threshold derivative, integral prior variance, and first-order collision expansion. Its output likewise does not substitute for the proof of monotonicity.
