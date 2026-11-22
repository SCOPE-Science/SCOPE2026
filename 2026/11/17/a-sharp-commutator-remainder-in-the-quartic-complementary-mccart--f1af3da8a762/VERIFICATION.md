---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Exact positive-operator identity reconstructed from cyclic fourth-order trace words: D4=4Tr(A^3B+AB^3+A^2B^2-3ABAB). The square ||A^(1/2)(A-B)B^(1/2)||_2^2 equals Tr(A^3B+AB^3-2A^2B^2), and commutator square equals 2Tr(A^2B^2-ABAB); multiplying by 4 and 6 gives D4 exactly. Schatten Hölder puts the products in trace class for positive S4 operators; common finite-rank compressions pass the polynomial identity to arbitrary Hilbert space. Two rank-one noncommuting projections give D4=3, ||[P,Q]||_2^2=1/2 and zero first square, so 6 is sharp, also approached by PD perturbations. Unstrengthened zero requires [A,B]=0 and AB(A-B)=0; commuting compact positives admit joint eigenbasis, including possible kernel.

## originality

PASS

Best-of-knowledge: original contribution is the sharp 6 commutator stability remainder and exact positive-square identity, not the baseline complementary McCarthy inequality. Zhang Theorem 1.2 gives the latter at p=4 but not a commutator coefficient or equality witness; Audenaert and Li/Zhou give exponent-range context. Resultary search showed exact self-record and only different commutator/Schatten models. An older unindexed trace-word rearrangement could independently contain the same polynomial identity; no absolute priority is asserted.

## value

PASS

The decomposition strengthens a well-studied quartic matrix inequality by an optimally quantified noncommutativity penalty, makes extremizers explicit even without commutativity, and gives the complete zero-defect classification for arbitrary S4 positive operators. Although its algebraic verification is short, the sharp quantitative remainder and its infinite-dimensional validity are motivated mathematical stability information beyond a textbook trace expansion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
