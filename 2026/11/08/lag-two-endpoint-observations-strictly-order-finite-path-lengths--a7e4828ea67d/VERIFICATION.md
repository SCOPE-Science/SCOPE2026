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

# Verification

Run `python3 verify.py` beside the result. This standard-library checker constructs exact rational first-exit transforms on the planar squares, first-coalescence transforms of two independent reflected walkers, and stationary pair-covariance equations. It independently builds the entire noisy-voter binary-state transition matrix on small paths and compares stationary root time-two repetition probabilities.

The actual execution completed with the message `VERIFY_OK; exact independent stationary, pair-coalescence, square-exit checks: 38`. The grouped exact comparisons cover path sizes from two through seven and copy-survival parameters \(c=1/2\) and \(c=2/3\); direct binary-configuration tests cover the computationally tractable smaller sizes. The computed gaps were positive and met the claimed quantitative bound. Checks use `fractions.Fraction` for exact rational arithmetic, without Monte Carlo inference or a numerical tolerance.

The all-size, all-parameter theorem does **not** follow from this finite test suite. The general proof relies on a coalescing-genealogy identity, explicit pathwise folding of independent simple random walks into a two-dimensional walk, and nested planar domains with a positive-probability separating event. The two-vertex boundary case is handled separately. The hypotheses require fixed shared noise strictly inside the unit interval and unweighted finite paths observed at an endpoint. No sample-complexity or independent external mathematical validation is asserted.
