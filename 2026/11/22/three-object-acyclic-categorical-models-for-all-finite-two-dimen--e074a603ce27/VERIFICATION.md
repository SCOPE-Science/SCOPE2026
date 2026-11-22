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

# Reproducibility and scope

Run `python check_presentation_models.py` with Python 3 and SymPy installed to reproduce all exact sample assertions. The code builds every composite arrow for eight explicit finite presentation complexes, checks full-table size, associative composability (three successive nonidentity arrows cannot occur), enumerates the link graph and all its edges, verifies link connectivity and the number of independent cycles, checks the signed image of every relator letter and the cellular identity \(\partial_1\partial_2=0\), and computes eight integral Smith-normal-form sample checks.

The Smith calculations provide independent finite checks for examples with two-torsion, three-torsion, and free top-dimensional homology. They do not prove the arbitrary-word theorem: the general justification is the exact graph structure and the sink mapping-cone homotopy pushout in RESULT.md. The identity of spaces is asserted up to homotopy equivalence. No independent mathematical audit was performed. No claim of computer-assisted formal verification or exhaustive priority search is made.
