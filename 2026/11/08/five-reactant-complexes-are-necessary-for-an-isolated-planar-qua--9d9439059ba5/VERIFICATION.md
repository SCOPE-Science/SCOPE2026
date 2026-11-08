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

Run `python verify.py` in a Python environment with SymPy. The program uses exact integer and rational symbolic arithmetic to check all 15 two-row rank conditions, the expansion about the equilibrium, and the five directed mass-action reactions producing the claimed vector field and full zero Jacobian. Expected terminal line:

`VERIFY_OK independent_coefficient_pairs=15 sharp_reactions=5 isolated_positive_equilibrium=1 zero_full_jacobian=1`

The proof's infinite statement is the linear-algebra-and-definite-quadratic argument in RESULT.md; the symbolic checks verify only its finitely stated coefficient identities and a sharpness witness. No exhaustive search over reaction networks, independent scientific audit, or historical-priority certification has been performed.
