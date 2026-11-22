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

# Verification and reproduction

The theorem is proven in `RESULT.md` using the two-chart double cover, the simple critical points and alternating \(\pm1\) critical values of \(T_n\), local double-root node criteria, and the product-discriminant formula. No infinite claim is justified solely by finite calculations.

The standalone `check.py` uses Python 3 with SymPy. Running `python check.py` from the extracted package performs exact symbolic verification in degrees \(2\) through \(8\) of the Chebyshev identity, discriminant factors up to nonzero constants, every singular fiber's double-root count, and squarefreeness of a generic fiber. The check establishes only those finite cases. The all-degree genus, stability, exhaustion and total-surface singularity assertions are supported by the written proof, not by the script.

No external independent audit has been performed. The classification excludes the parameter \(\lambda=\infty\), and no regularization or Néron data is claimed.
