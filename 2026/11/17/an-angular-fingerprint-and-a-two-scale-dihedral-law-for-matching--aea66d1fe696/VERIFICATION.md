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

The exact-rational checker `verification/check_angles.py` runs under Python 3 without third-party packages. It verifies 77 graph-size/matching-size configurations for orders 3 through 16, spanning 4,774 pairs of facets, including empty and maximal matchings. It constructs the original Laplacian from deleted edges, checks its explicitly proposed pseudoinverse against the exact zero-sum projector, and recomputes the normal Gram products and the complete multiplicity table. A finite verification is not an unrestricted mathematical proof. The proof in RESULT.md covers all permitted orders and matching sizes.

The second-order weak limit follows by Taylor expansions and exact pair counts; no probabilistic simulation is needed or claimed. Independent mathematical validation has not been performed.
