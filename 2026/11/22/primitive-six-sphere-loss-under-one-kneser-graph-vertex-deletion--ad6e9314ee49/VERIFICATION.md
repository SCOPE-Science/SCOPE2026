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

Run `python3 verify.py certificate.json` with Python 3. The script reconstructs all graph-neighborhood simplices, checks all 290 plus 202 free-face simplicial collapses, builds and eliminates every fundamental-group generator of both reduced two-complexes, and performs 99 exact signed integral relative-chain cancellations. The last reduction leaves precisely six degree-two generators, with all other relative chain groups canceled.

The stored certificate is compared against recomputation; it contains every collapse and unit pivot. The finite computation covers all faces of the specified fifteen-vertex graph and its fourteen-vertex vertex-deleted graph, not a sample. Euler characteristic and the simply connected Whitehead theorem supply the homotopy conclusion. No larger-parameter formula, equivariant equivalence or independent audit is asserted.
