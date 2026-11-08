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

# Reproducible verification

Execute `python3 verify.py` using only the Python standard library. The program derives the complete face family from the stated metric (including the empty face), validates its vector, creates a deterministic full-face discrete Morse matching, and certifies the reversed Hasse graph is acyclic via an exhaustive topological sort. It reports 12,760 matching pairs, one critical vertex, nine critical four-cells, and 25,530 fully processed nonempty faces. The discrete-Morse theorem upgrades this finite combinatorial certificate to the stated ordinary homotopy equivalence.

The program then computes all six order-five subgroup orbit complexes directly and checks the complete signed chain character at all 25 translations. It asserts the stated fixed face vectors and character values. `verification_output.txt` is the exact captured stdout of a successful local execution. Hashes of both files are included in the enclosing package.

The verifier does not prove originality or the existence of a compatible integral equivariant splitting. The only source with an asserted nonequivariant theorem is Adams et al., Theorem 7.1; the remaining group-action calculations are proved directly in `RESULT.md` and checked independently by the code.
