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

The accompanying `checker.py` is a standalone Python 3 program using only the standard library and exact rational arithmetic. Run `python3 checker.py` and compare its entire output to `checker_output.txt`. It exhausts the finite set of labeled connected simple graphs on two through six vertices, forms false-twin quotients, computes their rational adjacency rank, and checks the required class/degree patterns. It also directly checks a nonpermutation real orthogonal-block algebra isomorphism on the 24-vertex uniform blow-up of the eight-cycle using fractions, including all products of natural basis elements. The seven-vertex path provides a singular-quotient irregular obstruction. A finite graph census does not enumerate the continuum of possible real linear isomorphisms and does not prove the theorem. The theoretical proof derives the complete normal form.

The small-graph enumeration counts labeled graphs, not isomorphism classes. No independent audit has been performed.
