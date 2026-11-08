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

# Reproduction and scientific boundaries

Run `python verify_moments.py` in the same directory. It requires Python 3 and SymPy and returns the number of passing algebraic and exact-rational generator checks. The present run returned `117 exact/rational/numeric diagnostics passed` and the exact sixth-moment witness values `(1073/3680, 7627/26144)`.

The proof in `RESULT.md` independently establishes stationary existence and uniqueness, the conditional-moment recurrence, the one-fold classification at fixed variance and the global three-moment injectivity theorem. The code verifies polynomial identities and thirty exact Markov generator cases as a reproducibility aid; it cannot by itself verify the infinite family of rate pairs or establish scientific originality. No independent scientific audit has been performed.
