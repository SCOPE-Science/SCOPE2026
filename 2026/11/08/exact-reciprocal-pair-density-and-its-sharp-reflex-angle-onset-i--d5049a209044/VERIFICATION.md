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

# Finite reproducibility diagnostics

With Python 3, install the pinned diagnostic dependencies using `python -m pip install -r requirements.txt`, then run `python verify.py`. The script checks the exact half-plane and full-plane geometric constants, polygonal union-area symmetry and positivity, one-dimensional numerical quadrature, the onset-slope approximation, and seeded finite-sample reciprocity counts at four apertures using the nearest 48 Euclidean candidates; any unresolved candidates are reported by the script. All 40 diagnostic assertions completed successfully in the recorded run.

The numerical polygonal areas and samples have finite-resolution error. They establish neither the exact area identity nor the infinite probability limit; the analytic proof in `RESULT.md` supplies those statements by lens geometry, Palm/Mecke integration, and a finite-range truncation law of large numbers.

No independent audit or external certification has been performed.
