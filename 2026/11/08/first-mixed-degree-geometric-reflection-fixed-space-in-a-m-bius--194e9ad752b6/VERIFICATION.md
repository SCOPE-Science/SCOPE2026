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

Command: `python3 mobius_reflection_fixed_verify.py` using standard Python 3.

The verifier enumerates exactly all perfect matchings in each finite Möbius ladder from 4 through 16 vertices, constructs both vertex-reflection classes, and checks equivalence between all setwise invariant original faces and the orbit-face construction. It reconstructs every simplicial elementary collapse with a unique-coface test, computes graph cycle ranks for the residual one-dimensional cases, and extracts the oriented two-cell relations after spanning-tree contraction at the essential mixed-degree case. Seven permitted generator/relator eliminations leave one free generator and one two-cell with null attaching word. The actual execution record ends `MOBIUS_REFLECTION_FIRST_MIXED_FIXED_TYPE_OK`.

Limits: These checks exhaust precisely the claimed finite range, not larger ladders. The cell-cancellation argument relies on standard CW homotopy operations, and no external or independent audit was performed.
