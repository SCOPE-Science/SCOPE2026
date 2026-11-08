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
# Verification

The standalone file `check_skew_bipyramid.py` was executed with Python, NumPy, SciPy and mpmath. It reconstructs the bipyramids' three-dimensional convex hulls from vertices, derives edges from the hull facets, and checks plane-edge crossing counts for 18 parameter configurations (polygon orders \(3,4,5,6,7,9\) and shear ratios \(0.3,1.4,4.0\)), using 85,000 independent Haar directions in each. It also compares the closed form to independently integrated angular densities (error below \(3\times10^{-13}\)), and compares the leading \(\lambda^n\) imbalance coefficient for odd \(n=3,5,7,9\) using 70-digit precision.

Observed outputs:

```
SKEW_BIPYRAMID_FULL_LAW_OK 18 configurations x 85000 directions
SKEW_BIPYRAMID_QUADRATURE_OK
SKEW_BIPYRAMID_HIGH_ORDER_ASYMMETRY_OK n=3,5,7,9
```

The symbolic argument for every order is given in `RESULT.md`; numerical tests do not establish infinite or universal claims. No independent audit or external certification has been performed.
