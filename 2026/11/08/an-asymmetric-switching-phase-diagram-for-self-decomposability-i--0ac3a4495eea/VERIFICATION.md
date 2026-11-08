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

# Verification record

The explicit characteristic function was reconstructed from the two coupled stationary generator equations, using the known stationary probabilities of the switching states. The isotropic Lévy density was computed by Gaussian subordination of logarithms, with positivity derived pointwise from the ordering of heat-kernel weights. The one-dimensional critical inequality and the dimension-at-least-two Bessel derivative supremum were checked symbolically in the proof. The endpoint \(d=2\) uses the logarithmic small-argument asymptotic of \(K_0\), while dimensions above two use its power-law analogue. The compound-Poisson jump density was normalized by polar integration and the radial small-argument limit. The resulting law is an invariant *distribution* of the constructed Lévy-driven OU process, not an equivalence of time-dependent trajectories.

Run the included standalone numerical diagnostic with `python CHECKER.py` in an environment with Python 3 and SciPy. It reports 917 successful finite assertions, including Lévy exponent inversion, Bessel recurrences, cross-threshold sign tests, and stationary variance. These numerical calculations do not prove all-parameter inequalities or uniqueness. No independent validation was conducted.
