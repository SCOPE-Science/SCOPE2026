---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For every fixed 0<a<1 the Poisson-kernel Fourier moment E u=(a,0) proves unbiased unit-row measurements and noise second moment 1-a²; normalized greedy residual forces row one. Batch one yields exact a^-2-1 MSE. For N=2 antipodal angle bands give P(||v_N||<r)>=cr; for N>=3, the regular-N-gon zero configuration has rank-two Jacobian sin(2pi/N)/N², giving a genuine two-dimensional small-ball lower bound cr² by an inverse chart. Tail integration makes E||v_N||^-2 infinite, and a.s. invertibility plus SLLN gives a.s. convergence. Local derivative control and Hoeffding give the stated O_a(1/N) ridge first-step MSE. Independent spot check of Poisson-kernel moment and regular-polygon Jacobian matches. Finite experiments never certify the divergent expectation.

## originality

PASS

This explicit unbiased, unit-row signal-averaging counterexample shows a real inverse-moment gap in the mean-square guarantee: N=1 has finite risk but all finite N>=2 give infinite first-step risk, although the estimator converges almost surely and ridge restores O(1/N). The compared March 2026 Kaczmarz signal-averaging paper states a finite full-expectation guarantee under bounded row norms without a uniform denominator lower bound. Earlier random-walk singular-moment and Gaussian-resampled-row studies give ingredients, not this precise contradiction under its algorithm and assumptions.

## value

PASS

A concrete all-finite-N counterexample to a published unconditional first-step mean-square guarantee is a consequential boundary for noisy row normalization: arbitrarily small bounded row noise and well-conditioned SPD A do not ensure inverse-square integrability. The batch-one/batch-two phase discontinuity and matched stabilizing ridge rate show a mathematical mechanism researchers must handle, not merely an anecdotal failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
