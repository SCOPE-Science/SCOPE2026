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

The complete graph classification is proved in `RESULT.md` by unique midpoint representations (for pairs with a support of cardinality at least the monomial degree) and by minimal faces of the uniform-matroid independence polytope (for pairs below the degree). The proof is valid for every integer \(2\le r\le n\), not merely the tested sizes.

The accompanying exact Python program `verify_skeleton.py` requires only the Python standard library. It constructs the binary monomial vertices and all unordered pairs, then checks equal-midpoint signatures and exact degree/edge counts. Test coverage: all integer pairs \(2\le r\le n\le7\) plus \((n,r)=(8,4)\). Signature uniqueness is not a general proof of adjacency in an arbitrary polytope; the separate analytic midpoint argument supplies that proof for this family. Equal midpoint signatures of distinct pairs do certify nonadjacency.

This is a self-review, not an independent mathematical audit. Any broader claims about arbitrary hypergraphs or relaxation polytopes are unproved.
