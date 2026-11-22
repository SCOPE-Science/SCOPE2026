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

The self-contained Python 3 verifier `verify.py` and explicit `collapse_certificate.json` were executed together. It recomputed the \(168\)-element matrix group, \(179\) subgroups, \(2495\) nonempty strict chains, four orbit-cell counts \((13,37,37,12)\), and all \(49\) free-face cancellations, with one vertex remaining.

Execution: `python3 verify.py` in the directory containing both attached artifacts.

```
PSL27_ORBIT_SUBGROUP_COMPLEX_COLLAPSE_OK
group=168 subgroups=179 proper=177 chains=2495
orbit_cells=(13,37,37,12) certified_collapses=49 residual_vertex=1
```

No floating-point, random, external solver, or unexamined binary artifact is used. The verifier establishes exact properties of this finite action. It does not establish absence of previously published equivalent results, any extension to other simple groups, or independent validation.
