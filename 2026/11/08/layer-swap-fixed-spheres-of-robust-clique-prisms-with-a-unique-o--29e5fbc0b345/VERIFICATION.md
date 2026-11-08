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

The accompanying standalone `verify_prism_fixed.py` recomputes the prism independence number directly by complete independent-set enumeration, and independently via maximum induced bipartite order, for all subsets of nine explicit test graphs. It then enumerates every fixed simplex for each robust level, builds simplicial chain boundary matrices, and verifies reduced homology over \(\mathbf F_2\) against the asserted integral-wedge ranks. The cases cover triangle, pentagon and heptagon bases, even cycles, a path, and several one-odd-cycle graphs with tree attachments, with parameters \(2\le k\le N+1\).

Run with `python3 verify_prism_fixed.py`. Recorded output is in `verification_output.txt`; successful output ends with `ALL_PRISM_FIXED_CHECKS_OK 9 graph_cases 52 k_values`. Computational checks provide corroboration, not proof of the universal quantifiers. The integral primitive-boundary argument and homotopy passage are in `RESULT.md`. No external verification has been performed.
