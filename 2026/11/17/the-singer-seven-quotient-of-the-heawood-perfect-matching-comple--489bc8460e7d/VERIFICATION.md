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

# Reproducibility and scope of verification

Run `python3 verify_heawood_rotation.py` with Python 3's standard library and compare its complete JSON standard output with `verification_output.json`. The supplied code and output were used for this finding.

The checker verifies the 21 Heawood edges, 24 perfect matchings, and exact face vector \((21,168,560,756,504,168,24)\). It constructs an acyclic 1092-pair Morse matching by checking all 8736 Hasse incidences, leaving one critical vertex and sixteen two-faces. It constructs the full 4511-face equivariant nerve, checks three invariant vertices and no invariant positive-dimensional simplex, and independently checks the quotient-cell vector \((6,36,128,198,168,84,24,3)\) using Burnside's formula. Every integer cellular boundary composition vanishes. A deterministic 321-pivot unit cancellation leaves one zero-cell and four two-cells and no other cellular groups or differentials.

The finite arithmetic verifies the particular chain model exhaustively; it does not replace the mathematical arguments that the equivariant nerve descends to orbit spaces, that all rotation stabilizers normally generate the cyclic group, or that homological Whitehead applies to the simply connected finite CW quotient. Those are explicitly justified in the proof. In particular, the calculation neither asserts a homeomorphism classification nor a general all-projective-planes formula.
