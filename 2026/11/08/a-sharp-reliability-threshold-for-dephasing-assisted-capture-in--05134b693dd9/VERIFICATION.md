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

Run `python verify.py` with SymPy, NumPy and SciPy installed. The script constructs the four-dimensional survivor generator from the specified population/coherence equations, solves the first and second resolvent systems symbolically, reconstructs the capture-time variance, checks the derivative and polynomial identities, and compares the analytic moments against an independently integrated matrix-exponential survival function at 16 parameter pairs. All exact identity assertions and 32 numerical moment-integral comparisons passed.

The script is a finite computation for the symbolic equalities and selected numerical comparisons. The infinite parameter classification follows separately from the sign/Descartes proof in `RESULT.md`, not numerical sampling. No claim is made that these computations establish publication priority or provide independent scientific audit.
