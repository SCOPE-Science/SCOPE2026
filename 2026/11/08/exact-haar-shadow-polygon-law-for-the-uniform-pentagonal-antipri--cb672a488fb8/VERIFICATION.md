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

# Reproducibility and limits

Run `python3 verify_pentagonal_antiprism.py` from the directory containing the file, using Python 3 standard library only. The actual checker was executed on the packaged source and returned the following successful checks:

```
EXACT_PENTAGONAL_ANTIPRISM_CHAMBERS_OK rays=30 cells=32
signature_counts {8: {'CCE': 10, 'DDE': 10}, 6: {'ABBPP': 10}, 10: {'AAAAA': 2}}
probabilities {'6': 0.659378121806623, '8': 0.3201882582698952, '10': 0.02043361992348188} expected 6.722110996233718
PENTAGONAL_ANTIPRISM_SILHOUETTE_OK
INDEPENDENT_PROJECTED_HULL_CROSSCHECK_OK 10000
MEAN_FROM_TWO_EDGE_ORBITS_OK 6.722110996233717
```

The exact part does not rely on floating-point tolerances to decide algebraic signs; it uses arithmetic in \(\mathbb Z[\varphi]\), with \(\varphi^2=\varphi+1\), and exhausts the 64 sign masks and 30 directed great-circle-intersection rays. All 32 nonempty chambers and physical-angle types are enumerated. Girard's theorem supplies the continuous spherical areas. The last two lines independently test geometric 2D convex hulls for 10,000 seeded Haar viewing directions and reproduce a previously known mean, but these numerical checks alone are neither exhaustive nor an infinite proof.

No independent mathematical audit has been performed. The complete archival Kettner–Welzl (1997) article was not accessible; historical priority remains uncertain. The theorem excludes great-circle boundary views and is specific to the uniform pentagonal antiprism under Haar orientation.
