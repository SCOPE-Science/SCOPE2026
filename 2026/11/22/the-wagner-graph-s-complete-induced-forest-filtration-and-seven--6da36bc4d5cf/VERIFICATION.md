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

The certificate directory contains four ordered discrete-Morse matchings, one for each stage, encoded as explicitly checked elementary-collapse and critical-deletion operations. Run `python3 verify.py`; no nonstandard Python packages or external downloads are required.

The executable reconstructs all 256 subsets of the specified eight-vertex graph. It verifies actual face predicates and full f-vectors, every collapse's codimension, unique coface and maximality requirements, maximality of every critical deletion, the complete original-face directed Hasse graph's acyclicity, critical-cell counts, stage inclusions, and signed Lefschetz traces for each of the sixteen dihedral symmetries. The attached `verification_output.txt` records the exact verified results. The integral homotopy conclusion follows from these complete matchings via finite discrete Morse theory, not from a mod-two computation or an unverified log.

This exact finite classification does not extend to arbitrary Möbius ladders. The rational dihedral character is not an asserted integral lattice classification. Independent scientific review has not been performed.
