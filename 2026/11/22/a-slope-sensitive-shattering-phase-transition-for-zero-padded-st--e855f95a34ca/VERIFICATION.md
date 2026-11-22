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

# Verification and scope

A complete proof is supplied in `RESULT.md`, covering the mechanical coding representation, the role of variable factor lengths, the sharp lower and upper VC bounds, and the exact support tests. The proof is independent of computation.

The standalone Python 3 program `verify.py` creates all rational-rotation words to a fixed horizon, closes the resulting factors under all suffix truncations, computes every trace on each support of cardinality at most four, and compares it to an independently generated rational-arc geometric oracle. The eight parameter cases produced 7,808 paired comparisons with no mismatch. Rational rotations only test arithmetic and trace accounting; they are not substitutes for the infinite irrational theorem. A direct eight-pattern witness at slope \((\sqrt5-1)/2\) is given in the result.

The preceding original literature proves the sliding-window dimension two and the general one-unit gap bound; neither alone determines the claimed slope-specific values and complete support structure. The full 2005 Muller preprint was not accessible, so historical overlap beyond the accessible abstract remains a limitation. Independent mathematical validation is not performed.
