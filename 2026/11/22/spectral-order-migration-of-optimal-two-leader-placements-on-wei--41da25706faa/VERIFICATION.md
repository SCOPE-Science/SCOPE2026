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

# Verification instructions

Install NumPy as specified in `requirements.txt` and execute `python verify.py` in the same directory as this file. The exact, self-contained mathematical assertions and derivations are in `RESULT.md`; the executable checker is a finite diagnostic, not an infinite certificate.

Expected output:

```
VERIFY_OK exact_parameter_instances=45 exact_pair_inversions=1290 continuous_parameter_order_instances=1280 leader_sets=5960 threshold_checks=96
```

The exact portion builds integer/rational conductance Laplacians, enumerates all unordered two-leader choices for each of 45 parameter triples, obtains every inverse by rational Gauss–Jordan elimination, and compares the exact squared-inverse trace against the claimed minimum. The continuous-order portion independently diagonalizes all grounded Laplacians at 160 graph/conductance choices and checks the real-power objective at eight spectral orders, including noninteger orders. A further 96 threshold checks compare numerical solutions with strict order monotonicity and both explicit endpoint values. Tolerances apply only to floating-point comparisons; the rational tests use exact equality.

Limitations: finite enumeration cannot establish an all-size classification, a continuum-order identity, a unique threshold for every parameter, an asymptotic expansion, or publication priority. Those statements require the analytic proof and source comparisons in `RESULT.md` and `REVIEW.md`.
