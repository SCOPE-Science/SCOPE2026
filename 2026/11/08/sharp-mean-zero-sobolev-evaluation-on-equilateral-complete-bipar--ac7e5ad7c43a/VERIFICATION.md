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

# Reproducible checks and scope

The analytical argument in `RESULT.md` proves the result for every integer \(m,n\ge3\). The accompanying `verify.py` uses Python 3 and SymPy; invoke `python verify.py` from the same directory. It reports:

```
SYMBOLIC_ALL_DIMENSIONS_CHECKS_PASSED
EXACT_SUBDIVISION_AND_ENERGY_CHECKS_PASSED 87
ALL_COMPLETE_BIPARTITE_SOBOLEV_CHECKS_PASSED
```

Symbolic identities checked include the explicit Green value, its normalization, the quadratic completion, symmetry, midpoint displacement, boundary identities, and asymptotics. Independently, physical edges are subdivided at rational test points and the complete Kirchhoff problem is solved using exact rational matrices, with zero arclength mean enforced after solving. The computed diagonal Green values also equal an independently integrated derivative energy. These calculations do not verify bibliographic priority and finite-dimensional samples alone would not prove the universal result.
