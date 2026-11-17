---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: A dimension-two generator over F5 has six projective nonzero column types; the complete weight enumerator gives 1+4Σ_i t^{N-m_i}. Its first moment recovers N, hence the full multiplicity multiset and number of zero columns. Monomial equivalence reduces exactly to PGL2(5) orbits. Group order 120, seven proven cycle types, and Burnside orbit coefficients give the eleven possible count patterns 1,1,1,1,1,1,1,2,2,3,6. Minimal nonnegative distinct multiplicities force thresholds 6/10/15 and zero-column padding handles every larger length. The two six-column examples have the same enumerator but different orbits, with exact distortion 36/25 by bounding all possible weight ratios and exhibiting an attaining Möbius permutation. An independent 120-map enumeration reproduced every pattern and the rational distortion; infinite-length coverage follows the algebra, not extrapolation.

## originality

PASS

PASS best of knowledge: Dodunekov–Simonis supply the general projective-multiset equivalence premise, and Bennett–Fox–Morrell define distortion plus an algorithm over arbitrary q/k. Neither inspected result, nor the parallel quaternary rank-two classification, establishes the eleven six-point PGL2(5) fiber populations, sharp lengths or first-pair distortion. These require explicit finite-group orbit classification combined with full-length zero-coordinate padding. Possible hidden six-point configuration orbit tables remain a concrete priority risk.

## value

PASS

PASS: Hamming weight enumerators are natural yet incomplete invariants of code equivalence. The exact sizes of their rank-two quinary fibers, the first ambiguity threshold, and a sharp quantitative minimum distortion answer motivated classification and information-loss questions, not arbitrary numerical samples. The complete eleven-pattern classification has all-length implications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
