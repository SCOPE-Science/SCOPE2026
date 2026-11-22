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

# Verification instructions and limits

Execute `python verify_counts.py` with SymPy installed. The verifier reconstructs the eight-state continuous-time generator and five distinct accepted-event jump matrices; verifies the stationary distribution and probability conservation; solves the five centered current-corrector equations; establishes all ten off-diagonal asymptotic covariance formulas, all five mean-count rates and all five Fano factors; and checks positivity certificates for global signs and the unique positive hopping-noise stationary point. If NumPy and SciPy are installed, it also compares selected cross-covariances against central finite differences of the tilted-generator dominant eigenvalue at two positive Langmuir rates.

The exact symbolic checks establish identities for arbitrary positive real exchange rate, while the numerical eigenvalue comparisons are only separate numerical sanity checks and do not supply infinite-parameter proofs. The two rate normalizations, three-site geometry, one internal attachment/detachment site, non-overlapping event categories and long-time limit are essential. External or independent scientific audit has not been performed.
