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
# Verification record

The mathematical proof is in `RESULT.md`. Standalone numerical verification is in `verify_pellytope.py`. Executing the script with Python 3 and SciPy independently evaluates each required support function from the original simplex vertices for all \(3\le d\le n\le16\), tests the sharp inradius formula and an explicit feasible center against every facet normal, and tests the longer-difference support identity. For \(3\le d\le n\le12\), separate linear programs confirm the formula. Additional linear programs demonstrate positive slack for all nonforced facets in 23 long-regime cases.

Observed output:

```
Direct Newton-simplex support checks: 12551
Independent linear-program optima: 55
Positive relative-interior margins in long regime: 23
```

Finite numerical optimization does not prove the theorem for unbounded integer parameters; the argument using support-function identities, concavity, and difference constraints supplies the all-parameter justification. The normal-ray premise is cited to the originating source rather than inferred from finite computations. No third-party or independent mathematical audit was performed.
