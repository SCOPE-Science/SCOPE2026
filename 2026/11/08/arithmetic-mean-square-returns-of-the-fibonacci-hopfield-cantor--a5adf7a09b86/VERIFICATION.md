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

The source proofs of the rotation semiconjugacy and gap lengths were read in arXiv:2206.11933 (Lemma 6), and the invariant-line conjugacy was read in arXiv:2210.00414 (proof of Theorem 2.3). The included `checker.py` numerically integrates the truncated staircase with high-precision arithmetic and independently checks the exact formula at six Fibonacci indices, the Fibonacci return identity, and the two-sided bounds. The checker explicitly includes the phase-wrap breakpoint and passes. The full theorem, all integer quantifiers, and the arithmetic tail estimate depend on the displayed proof, not on the sampled indices. The independent mathematical audit remains unperformed.
