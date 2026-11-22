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

# Reproducibility

The proof is in `RESULT.md`; `check.py` is an independently executable supplementary diagnostic requiring Python 3 and NumPy. Run `python check.py` from this package directory. Successful execution prints `CYCLE_SPECTRAL_EXTREMAL_CHECK_OK 67056`.

The diagnostic computes each grounded matrix directly from its pinned vertices, uses symmetric eigendecomposition, compares global minima and maxima against the gap characterizations, tests positive times \(t=0.2,2.3\), inverse powers \(p=0.5,1,2.25\), uniform masses \(\mu=0,0.5,2\), and verifies the exact inverse trace for every tested pin set. Exhaustive enumeration is limited to \(3\le N\le10\). Floating-point tolerances test the numerics, while the closed-walk/strict-convexity proof supplies all-size, all-parameter validity. No external audit or independent validation is claimed.
