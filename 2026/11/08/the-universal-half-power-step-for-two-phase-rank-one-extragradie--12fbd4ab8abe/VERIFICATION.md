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

# Reproducibility and mathematical limits

Run `python verify.py` in the same directory, after installing `requirements.txt`. The file `verification_output.txt` records the actual check count. The code uses a symbolic three-by-three product and reduction modulo the unit-vector relation to confirm the characteristic-polynomial identity, verifies the derivative sign certificate and exact rational cases, and compares the predicted singular values against numerical singular-value decomposition over a dense grid.

The proof in `RESULT.md`, not the finite grid, establishes all real unit-row pairs and all real nonnegative equal steps. Symbolic testing is a guard against arithmetic mistakes; it does not establish originality, the physical relevance of larger models, or an independent audit.
