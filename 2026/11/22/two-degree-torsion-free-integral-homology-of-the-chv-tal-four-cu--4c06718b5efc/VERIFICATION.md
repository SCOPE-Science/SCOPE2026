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

Reproducibility: run `python3 verify.py` with Python 3.10+ and SymPy. The graph is encoded as an explicit undirected edge list; the script verifies all 4095 nonempty vertex subsets, 282 forbidden quadruples, 125 individually legal simplicial collapses, signed boundary composition zero and complete integral Smith factors. The final triangulation contains 12 vertices, 66 edges, 143 triangles, 88 tetrahedra. Integer boundary ranks are 11, 55, 80 with all nonzero Smith factors equal to one. The resulting reduced dual homology is free rank eight in each of dimensions two and three. The full original dual's finite-field ranks are separately verified in characteristics two and three. The recorded output is `verify_output.txt`. These computations establish the complete finite graph result and no broader family theorem. Independent external audit has not been performed.
