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

The finite checks can be reproduced with `python3 verify_pappus_full.py` from the same directory as `character_classes.tsv`; Python's standard library suffices. The file `verification_output.txt` records the exact successful output.

The checker reconstructs the 18-vertex, 27-edge Pappus graph from the displayed edges, enumerates all 2,597 independent simplices and all 216 automorphisms by adjacency-preserving backtracking, computes every mod-two boundary rank, and evaluates every rational homology trace twice by independent signed-fixed-face and vertex-cycle formulas. It enumerates all conjugacy classes and checks their table text; it computes the derived series of the automorphism group by exhaustive commutator closure, then checks the dimension-four projector for the characteristic order-three subgroup, the global character squared norm, and both invariant-subspace dimensions.

The rational-homology conclusion follows from the verified mod-two upper bounds together with the exact Euler characteristic, not from an assumption that finite-field homology equals integral homology. Irreducibility follows from the characteristic-subgroup decomposition and exact character inner product. Quotient claims are rational only. This program is a same-package reproducibility check, not an independent audit or a proof of publication priority.
