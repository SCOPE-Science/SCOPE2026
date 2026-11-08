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

# Computational and mathematical verification

Execute `python3 verify_symmetry.py` with standard Python 3 and no third-party packages. Its recorded stdout is `symmetry_output.txt`, ending in `ALL_CHECKS_PASS`. The program constructs the original graph, all 16 graph-metric balls, all 248 nonempty simplices, the original boundary matrices over two elements, and exactly 96 graph automorphisms. It verifies the original boundary ranks, the orientations and exact zero boundaries of two independent integral three-cycles, each of their 96 images, all signed simplicial fixed-face Lefschetz traces, and every character pair multiplicity. The integral cycle basis and the passage from chain traces to homology traces are justified explicitly in RESULT.md; recomputation of mod-two ranks alone would not establish integral third-homology actions without the explicit primitive cycles. The recorded calculation is a complete finite enumeration for this particular graph, not a proof for an infinite graph class. No independent external certification or human publication-priority audit has been performed.
