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

The proof uses exact deck-orbit minimization, Haar independence, a symmetric vertical-offset integral, and global pointwise differential inequalities; these steps prove the statement for every \(a,b>0\). The embedded `check_klein.py` is a separately reproducible standard-library Python program. Run with `python3 check_klein.py` in the directory containing the extracted file.

The source program was executed successfully in this package before assembly. It sampled 125,000 independent area-uniform pairs at each of seven shapes (875,000 total), compared its reduced deck formula against finite direct orbit minimization on the first 1,800 pairs per shape (12,600 exact-consistency checks), performed 12 CDF quadrature checks at two shapes, and evaluated the general energy integral using an independent one-dimensional quadrature. The verification output ended:

```
DIRECT_DECK_ORBIT_OK count= 12600
FULL_CDF_QUADRATURE_OK geometries=2 radii=12
GLOBAL_OPTIMIZER_BOUND_CONSISTENCY_OK tstar= 1.061610405842267 normalized_minimum= 0.16364114978233632
```

The correctness proof does not depend on these finite tests. No external proof assistant or independent mathematical audit is claimed. The checker uses the standard library only; empirical frequencies have sampling error.
