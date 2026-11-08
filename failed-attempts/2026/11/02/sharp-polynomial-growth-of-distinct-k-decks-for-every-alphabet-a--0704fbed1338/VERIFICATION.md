---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Reconstructed the finite truncated signature S(w)=∏(1+X_letter), the pair-difference induction and degree-j bracket P↦[P,X_a+C]. For each old pair the vectors X_a+C span degree one because det(I+c 1^T)=1+|U|>0, so Jacobi/free-Lie generation gives a basis for each homogeneous Lie degree. Uniform letter replication scales leading degree-j differences by 2^(rj); independent base-2^j digit blocks give an injection into actual length-k decks after the exact nested-deck recovery identity and invertible suffix padding. Upper Θ order uses Nilforoushan–Parvaresh Theorem 5.1, with k=1 elementary. Small independently enumerated k-deck counts and Witt exponents corroborate, not certify all q,k. Correctness can be PASS despite earlier complete coverage making originality FAIL.

## originality

FAIL

FAIL, decisive earlier complete coverage: 2026-09-25 public theorem PositivePairExactDeckAsymptotics.actual_exactKDeckImage_weightedLyndon_isTheta states EXACT same all-q≥2,k≥1 cardinality Θ(n^(Σ j L_q(j)−1)). Public full Lean source plus theorem document at this dated commit demonstrate identical objects and quantifiers; proof imports a positive-word lower bound. This was published before 2026-11-02 assigned record. The assessed manuscript is a reproof of a covered conjecture, not an original main claim. Originality fails independently of mathematical correctness and potential value.

## value

PASS

PASS as a mathematical result (despite O FAIL): the exact polynomial order of distinct subsequence-count decks for every q and k is the natural all-parameter resolution of a concrete reconstruction/coding conjecture. The homogeneous Lie/positive-word construction gives substantive lower-bound control. It is worth knowing but was already established by the earlier public theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
