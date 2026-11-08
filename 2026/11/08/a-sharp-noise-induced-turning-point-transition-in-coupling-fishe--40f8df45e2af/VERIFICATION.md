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

Execute `python verify.py` with Python 3, SymPy and mpmath from the folder containing the extracted files. It independently solves the stationary Lyapunov identities, recomputes all three Gaussian Fisher-matrix entries, checks the rational derivative and its cubic numerator, and tests the endpoint and normalized polynomial identities. It then performs 152 exact-rational sign comparisons and solves the algebraic double-root equations at 50-digit working precision. Representative root counts are checked on both sides of the threshold.

These checks verify algebra and numerical reproducibility. They do not independently certify the entire real parameter domain or prove publication priority. The strict concavity, one-threshold argument, global zero count, large-noise asymptotics and square-root bifurcation are supplied as an analytic proof in RESULT.md. The script has no external inputs, files or network dependencies other than the stated mathematical Python packages.
