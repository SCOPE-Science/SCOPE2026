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

# Reproduction and scientific limits

Use Python 3.10+ with NumPy, SciPy, and SymPy. Execute `python check_stationary_memory.py` from this directory. The observed output was `PASS 4743 deterministic assertions`. The script checks exact algebraic threshold equations and the Bessel coefficient, Fourier-to-Bessel agreement for moderate times, large-time alternating sign extrema and pole dominance, plus direct sparse finite-ring Markov dynamics and invariance of the finite Gibbs distribution. Long-time direct quadrature is deliberately not used because oscillatory cancellation causes floating-point error; the analytic asymptotic proof uses Bessel identities, absolute convergence and explicit remainder bounds instead. The finite-ring agreement supports—but does not prove—the infinite-chain theorem.

The cited 2024 paper supplies the known exact dynamical formulas. Publication-priority comparisons distinguish the new post-exceptional-point eventual-sign phase diagram from prior stationary rate crossovers. Remaining uncertainty includes unindexed analytically equivalent publications and an inaccessible complete text of a related alternating-bath study. No independent external audit has been performed.
