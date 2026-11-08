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

The program `check_transpose.py` (standard-library Python 3) was executed from the package's actual source file, and its complete output is embedded as `check_output.txt`. It reconstructs invariant original rook-face sets for full boards of orders 1–7, checks an independently generated simplicial orbit model through order 8, enumerates all graphs on at most five vertices plus a fixed 240-graph sample at order six, and compares complete mod-two homology against perfect-matching counts. There were 1,339 graph patterns in total. For orders 2, 4 and 6, it checks signed permutations of full-board perfect matching facets, action-composition laws and stabilizer signs. The final output marker is `TRANSPOSE_FIXED_GRAPH_BOARD_HOMOLOGY_AND_SYMMETRY_CHECKS_OK`.

The proof of integral homotopy does not infer its infinite-range conclusions from these finite tests: it uses a PL fixed-orbit identification, an all-graphs good star cover and a quotient by a contractible subcomplex. The integral representation is a relative-chain calculation. The code does not check an equivariant homotopy splitting and no independent mathematical audit has been performed.
