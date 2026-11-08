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

# Reproducibility

Execute `python verify.py` with Python 3.10+ and SymPy 1.14.0. The script checks the actual two-by-two transfer matrices, symbolic factorization of the real-disk conditions, both limiting matrix identities, and the explicitly solved phase covariance at one fixed long step. It also solves twelve strictly stable rational examples using exact arithmetic and checks positive definiteness and the stationary matrix equation. The verifier passes when the final line begins `PASS:`. See `VERIFY_OUTPUT.txt` for the direct captured output.

The proof in `RESULT.md` establishes the infinite-time covariance limit and universal parameter assertions; rational samples do not certify those infinite or continuous quantifiers. The model adds independent zero-mean equal-variance disturbances to solution values. It makes no assumption of a hardware rounding-error distribution, nor does it establish stability on arbitrary nonperiodic steps or in multiple dimensions. No independent scientific audit has been performed.
