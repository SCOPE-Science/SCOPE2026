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

Execute `python3 verify.py` using Python 3.10 or later; no third-party dependencies are required. The expected literal stdout is `verify_output.txt`.

The checker independently enumerates every reduced-row-echelon linear subspace of dimensions three, four, five and six inside the six-dimensional coefficient space over \(\mathbb F_2\) and \(\mathbb F_3\). Each space is tested against all three literal matrix-square coordinates and all polarization cross-terms. Inclusion-maximal spaces are determined by containment in the uniquely found admissible four-space. The checker verifies the number and dimensions of maximal spaces, their multiplication types, their dimension-two intersection graph and its complete-bipartite structure, and every square-zero point's number of containing maximal spaces. For the two prime fields it also compares the exact total count with \(2q^4-q^2\).

This exhaustive work checks only the two fields stated and is not an infinite proof or a claim about extension fields. The full classification, and applicability to every prime power and characteristic, rest on the explicit rank-one pencil argument in `RESULT.md`. No external or independent audit is recorded.
