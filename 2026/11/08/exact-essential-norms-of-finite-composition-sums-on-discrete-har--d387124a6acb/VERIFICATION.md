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

The proof is analytic. The finite checker is an independent finite arithmetic corroboration of the explicit examples and matrix equations, not a certification of operator essential norms on infinite spaces. To reproduce, run `python3 checks/tree_essential_norm_check.py`. The expected success line starts with `TREE_ESSENTIAL_EXACT_FINITE_OK`. The checker uses only Python standard-library integer and rational arithmetic. No external theorem prover was used.

The compactness lower bound follows from an isometrically embedded `c0` basis supported on pairwise disjoint finite level sets. Exact coefficient cancellation is retained by the aggregate matrices; it must not be replaced by separate absolute coefficient counts. Independent mathematical auditing has not occurred.
