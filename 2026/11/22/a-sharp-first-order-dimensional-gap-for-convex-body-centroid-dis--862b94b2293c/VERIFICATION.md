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

Execute `python3 check_centroid_rate.py` using Python 3 and the Python standard library. The checker makes exact-rational coefficient, induction-base, exponential-Taylor, and interval-moment assertions. The observed output was:

```
Unique positive critical point in [2.353317385, 2.353317386].
D interval: 0.2016192724880 0.2016192756721
c interval: 0.0382670481517 0.0382670738412
All exact-rational assertion checks passed.
```

The finite coefficient comparisons are not used as an infinite proof. The proof establishes the positive sign of all remaining coefficients by induction and derives the asymptotic expansion with uniform two-derivative control. No independent audit or proof assistant certification is claimed. Literature priority remains provisional.
