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

# Reproducible exact checks

Run `python3 verify.py` with Python 3 and only the standard library. The checker constructs each directed network, creates the subdigraph of monochromatic arcs for every named-palette assignment, and independently tests that this subdigraph is acyclic by topological sorting. It compares the resulting count with the theorem's closed formula, over exactly 180 graph/palette cases and 1,161,788 individual assignments. Its independent polynomial component performs monic integer long division by cyclotomic factors and reconstructs the complete forward-arm multiset via exact Möbius inversion in 195 configurations. Additional rational sign brackets check root parity in these configurations. It terminates with `VERIFY_OK` only if all tests pass.

The all-integer checks supplement the symbolic proof; exhaustive finite enumeration alone is not a proof of the statements for all positive parameter values. The logarithmic-derivative inequalities and the relative-uniqueness conclusion are established analytically in `RESULT.md`.
