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

`python3 verify_pure_reflections.py` with Python 3's standard library reconstructs all \(n(n-1)\) pure-cycle facets from their explicit two-gap form, applies both reflection axis types, lists every admissible two-vertex incidence orbit in each facet, and calculates the maximal orbit-face structure for all \(6\le n\le50\). It matches the predicted **two disjoint complete simplices** in all 68 axis cases. For \(n\le11\), it separately generates every original simplex before testing invariance, bypassing the orbit-facet projection in the tested cases. For \(n\le17\), it independently enumerates reduced fixed-orbit faces and signs and obtains reduced Lefschetz number \(+1\).

The verification run prints:

```
ALL_VERIFY_OK checked_axes=68 n_min=6 n_max=50 fully_enumerated_fixed_faces=1242 full_invariant_axes=9
```

The proof of the unlimited theorem is combinatorial, not an extrapolation from the finite range. No independent external mathematical validation was performed. The full original 2026 preprint PDF was inaccessible for source comparison; the exact facet classification was also checked against the complete published mathematical proof of a separate rotation theorem.
