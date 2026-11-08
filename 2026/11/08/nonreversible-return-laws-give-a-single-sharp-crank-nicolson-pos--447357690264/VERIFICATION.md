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

# Reproducibility and limits

Run `python verify.py` with Python 3 and SymPy 1.14 or compatible exact symbolic algebra. The recorded output is `verification_output.txt`, reporting 5,754 passing exact checks and the symbolic directed-three-cycle positivity threshold.

The code verifies exact rational examples of reducible chains, nonreversible directed cycles and randomly generated rate matrices, plus selected symbolic formulas. Assertions use rational and algebraic equality/inequality, not floating-point tolerances. It does not enumerate all generators or all step sizes. The universal proof is the return generating-function identity and its strict monotonicity argument in RESULT.md.

No external independent scientific validation was performed. The evidence attached here is a self-review and an executable supplement, not an independent proof certificate.
