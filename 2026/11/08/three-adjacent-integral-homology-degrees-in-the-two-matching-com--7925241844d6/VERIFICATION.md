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

Execute `python3 verify_k223.py` and `python3 verify_k223.py reverse` from this package. Both use only the Python standard library. The first enumerates all 65,536 edge subsets, verifies the alternate three-star test, constructs 2,018 matched face pairs, topologically sorts the 4,107-vertex and 18,700-edge directed Hasse graph, computes signed Morse boundaries, and cancels 8 and 15 integral unit pivots leaving zero blocks. The reversed version independently constructs 2,026 pairs and cancels 1 and 14 integral pivots. Both compute direct original mod-two simplicial ranks 15,105,403,809,648,60, and both verify consecutive Morse boundary products vanish. See `verification_output.txt` for exact recorded output.

This proves integral homology but does not prove a homotopy wedge, full higher homotopy groups or equivariant action. The scripts are reproducible same-source computations, not an independent expert audit.
