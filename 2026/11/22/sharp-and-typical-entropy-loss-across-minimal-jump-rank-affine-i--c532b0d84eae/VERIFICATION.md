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

# Verification of the orientation entropy theorem

The standalone `check_orientation_entropy.py` was executed in Python 3 and completed successfully. It used integer Bareiss determinants for 1,512 exact spectral-polynomial identity evaluations, covering every orientation word with three to eight branches and three distinct integer spectral arguments. A separate direct enumeration of 32,764 words for two to fourteen branches checked the exact three-part binomial multiplicity table, unique entropy-minimizing word, maximizing spectral radius, and the uniform entropy-loss bound.

**Proof controls.** The positive Perron-vector reconstruction validates the scalar root selection for every branch count. Comparisons of scalar equations establish uniqueness of the minimizing word for arbitrary branch count, not only for the enumerated cases. The error bound uses \(n-1\le\lambda\le n\) and does not use an uncontrolled numerical fit. The Gaussian limit relies on the standard iid Bernoulli central limit theorem after an explicitly bijective sign-to-flip transformation.

**Limitations.** The finite checker is not a proof for all integers. The source's Markov construction and entropy identification are independently sourced premises, not re-proved in the checker. The distribution is with respect to uniformly sampled orientation words, not spatial points or trajectories. No independent mathematical audit is claimed.
