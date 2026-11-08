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

Execute `python3 verify.py` with Python 3.9 or later; only the standard library is used. This code checks all faces twice, all matching pairs, the entire directed Hasse graph, all critical cells, each signed integer Morse differential and reduced mod-two homology. Expected status line contains `VERIFY_OK`.

Exact face count including the empty face: 18,722. Exact nonempty matched pairs: 9,358. Critical nonempty masks: 1, 149522, 4737312, 4792338, 9584676, with dimension counts one zero-, one four-, three five-cells. Directed Hasse graph: 18,721 nodes and 104,568 covers; a topological ordering visits every node. Integer Morse boundary vector: \((0,0,0)\). Reduced mod-two Betti ranks: one in degree four, three in degree five, all others zero.

The actual proof of integral homotopy uses the full finite acyclic matching and signed integer attaching maps, not the mod-two ranks. This verification applies only to the specified 24-vertex graph. Independent external audit is not performed.
