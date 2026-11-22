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

# Verification of exact Markov-positivity formulas

Run `python verify.py` in the same directory, with Python 3.10 or later. No third-party packages, network access or external files are required. The checker evaluates the unmodified two-stage method by exact-rational stage solves on homogeneous absorbing birth-chain generators of two, three, four and five states. It independently evaluates the stated closed coefficients and checks equality, row sums and nonnegativity across a finite parameter grid. Deterministic midpoint integration checks the claimed positivity probabilities numerically at selected steps. On a fresh invocation the output was `VERIFY_OK 5495`.

The universal claims are proved symbolically in `RESULT.md`: all entries reduce to explicit rational expressions with positive denominators, whose signs reduce to the factored inequalities there. Numerical tests neither prove the full continuous-variable classification nor provide independent mathematical validation. The source literature and comparison limitations are discussed in `RESULT.md` and `REVIEW.md`.
