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

The source file `verify.py` reconstructs the complex and its exact integral Morse chain matrices without reading `verification_output.txt`. It exhaustively checks the entire augmented face set, directed Hasse acyclicity, exact Smith normal forms, chain identities, and fixed-face patterns for all 253 affine group elements. The stored output is from direct execution in Python with SymPy 1.14. The exact integer computation is finite and exhaustive; no infinite-family classification or integral equivariant homotopy is certified.
