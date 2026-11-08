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

The theorem is proved for every integer \(d\ge3\) in `RESULT.md`. The independent-audit channel has not been used.

Reproduce the finite exact computations with `python3 verify_chart.py` (standard library only). The program explicitly expands Plücker minors in the distinguished affine chart and verifies the key generator/ideal inclusions for \(2\le d\le6\); it also checks the rank-one cone Hilbert-series coefficient identity for degrees zero through seven.

Observed final output:

```
d=2 retained=5 transverse_k=1 CHART_AND_HILBERT_OK
d=3 retained=19 transverse_k=4 CHART_AND_HILBERT_OK
d=4 retained=69 transverse_k=9 CHART_AND_HILBERT_OK
d=5 retained=251 transverse_k=16 CHART_AND_HILBERT_OK
d=6 retained=923 transverse_k=25 CHART_AND_HILBERT_OK
ALL_EXACT_PLUCKER_CHECKS_OK
CERTIFICATE_OK
```

Finite computations do not establish the universal assertion. The proof uses an all-size determinant argument and separately establishes smoothness outside the identified Segre stratum. The result does not compute the nonreduced singular subscheme or the geometry of unbalanced truncations.
