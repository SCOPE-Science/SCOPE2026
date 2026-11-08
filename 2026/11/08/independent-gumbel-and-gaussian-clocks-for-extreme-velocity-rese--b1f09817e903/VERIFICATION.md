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

The included standalone `verify.py` is a deterministic reproducer for the one-flight Gaussian/exponential mixture, exact saddle identities, conditional length concentration, and finite-sample exceedance calculations. Run `python verify.py` with Python 3, SymPy and SciPy.

Finite quadratures and symbolic algebra confirm diagnostic identities but cannot establish an infinite limiting law. The complete mathematical argument, including marked point-process convergence and the random-renewal-count coupling, is given in `RESULT.md`. Independent external scientific audit has not been performed.
