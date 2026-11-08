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

# Verification of critical-coordinate escape factors

Execute `python verify.py` with Python 3 and SymPy at least 1.12. The verifier was run successfully with SymPy 1.14 and produced:

```
SEGRE_VERONESE_COORDINATE_ELIMINANTS_OK 20
GENERIC_SEPARABILITY_WITNESSES [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4)]
INFINITE_DEGREE_AND_IRREDUCIBILITY_FROM_WRITTEN_PROOF
```

For each degree one through five and four integer specializations, this recomputes the x- and y-resultants, verifies the exact divisibility by powers of s, checks both leading and constant coefficients, and searches for squarefree witnesses. The complete all-degree statement is established by the resultant identities, toric intersection count, irreducible incidence, and pair-incidence dimension argument in `RESULT.md`, not by numerical generalization. Parameter intersections and nongeneric coefficients are intentionally outside the theorem. Independent validation has not been performed.
