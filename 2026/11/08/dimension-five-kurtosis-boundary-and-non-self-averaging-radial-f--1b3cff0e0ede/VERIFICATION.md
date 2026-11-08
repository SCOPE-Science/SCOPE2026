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

# Reproducibility and boundaries

The package contains `checker.py`, which runs with Python 3 and no third-party dependencies: `python3 checker.py`. Its successful execution reported `PASS: 1951 exact-rational or explicitly identified numeric diagnostics`.

The exact-rational part solves the Markov-generator moment identities independently of the GEM representation over 30 integer dimensions and eight positive rational reorientation parameters. It compares these with four-sample GEM coincidence probabilities, with the dimension-one beta-law fourth moment, and with a direct angular Gram variance expansion. It also checks the excess-kurtosis algebra and exact sign threshold over this grid. Other diagnostic assertions compare the parameter optimizer with nearby values numerically and verify the limiting maximum constant. Their finite nature is explicit.

The general proof is in `RESULT.md`: the irreducible stationary random-barycenter representation and the spherical generator identities establish the all-parameter moments; a finite-Gaussian-vector multivariate central limit theorem and a dimension-uniform conditional squared-tail estimate establish the conditional angular fluctuation limit. The only probabilistic infinite-dimensional step is passing from finite to countably many weighted directions, justified by the summability of their squared GEM weights. An experiment cannot establish this limit, and none is used as a substitute for proof.

The result is restricted to stationary, independent full-direction redrawing, without translational Brownian noise, at fixed strictly positive reorientation-to-trap ratio in the high-dimensional limit. The conditional radial limit has a weight-dependent variance, so it is not an ordinary fixed-variance Gaussian law. Verification here is self-review; an independent audit has not been performed.
