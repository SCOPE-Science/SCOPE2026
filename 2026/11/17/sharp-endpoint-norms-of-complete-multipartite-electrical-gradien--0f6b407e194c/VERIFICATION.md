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

# Verification details

Run `python3 verify.py` with SymPy installed. The script reconstructs every projection matrix using a grounded Laplacian inverse over exact rational numbers; this is algorithmically independent of the partwise dipole formula used in the proof. It checks symmetric idempotence, every individual absolute row sum, exact extremizing sign fields, endpoint maxima, and complete finite partition extremizers.

Observed diagnostics:

```text
EXACT_GROUNDED_LAPLACIAN_PROJECTION_GRAPHS_PASSED 128
EXACT_EDGE_ROW_FORMULAS_PASSED 2926
EXACT_SIGN_EXTREMIZERS_PASSED 2926
PARTITION_EXTREMAL_CLASSIFICATION_PASSED 17
ALL_EXACT_MULTIPARTITE_HODGE_ENDPOINT_CHECKS_PASSED
```

The 128 graphs exhaust integer-part-size multisets with total vertex number from two through ten. The final classification test exhausts multipartite integer partitions from two through eighteen vertices. Rational finite verification is not a substitute for the universal algebraic proof. No external or independent mathematical audit was performed.
