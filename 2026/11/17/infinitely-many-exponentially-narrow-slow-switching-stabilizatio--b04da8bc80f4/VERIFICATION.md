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
# Reproducibility and verification

The accompanying standalone `verify.py` evaluates exact phase exponentials for the specified planar matrices, compares their direct numerical trace against the explicit oscillatory trace at nine test dwell times, verifies strict Jury stability at the predicted centers, and brackets the two stability boundaries of each tested window. Run with Python 3, NumPy, and SciPy:

```text
python verify.py
```

For \((a,d)=(0.1,11)\), the computed width divided by \(2e^{-\sigma t_n}/(\omega R)\) approaches one across indices \(n=2,4,6,8,10\), yielding approximately \(1.03992935\), \(1.00980593\), \(1.00257281\), \(1.00068567\), and \(1.00018348\). The additional cases at \((a,d)=(0.4,3)\) check indices \(n=2,4,6,8\) and exhibit the same asymptotic behavior. These computations use finite precision and finitely many indices; they do not certify the infinite-window theorem. The source's reduced focal-plane equation is treated exactly, while application to unreduced nonlinear oscillators is outside the proof.
