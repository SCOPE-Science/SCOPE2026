# Scientific review

## Correctness — PASS
The regenerative stationary-age mixture is exact: an independent exponential age and an independent thermal Gaussian combine with the bounded orientation-dependent drift. The upper bound uses the maximum possible drift and thermal variance. For every strictly positive rotational diffusivity the lower bound constructs angular paths aligned to an arbitrary projection direction over a logarithmically long age; their probability costs only \(O(\sqrt{x}\log x)=o(x)\). This matches the leading and first subleading coefficients. At zero rotational diffusivity the orientation is frozen; an exact age-integrated moment generating function and a direct long-age event prove the angular cosine coefficient. Fixed-angle Gaussian marginal nonnormality follows from a positive linear term in the transverse logarithmic tail. Uniformity in angle is supported by compactness of the circle heat kernel and uniform frozen-heading integrals. The standard-library numerical checker tests finite formulas only and is not the infinite-asymptotic proof.

## Originality — PASS, qualified
Shee (2024), arXiv:2409.06920, studies exactly the full position-and-heading reset harmonic-trap model, with moments and radial kurtosis, but the read text does not give a uniform angular far-tail asymptotic, its first linear coefficient, or the rotational-diffusion singularity. Chaudhuri and Dhar (2020), arXiv:2005.14234, study harmonic confinement without resetting; Kumar, Sadekar and Basu (2020), arXiv:2008.03294, study complete resets without harmonic confinement and obtain nonquadratic stationary tails. Nearby indexed research concerns unrelated harmonic Jacobian extremals, numerical Langevin covariance, or Brownian boundary laws rather than this observable. A general unindexed theorem about Gaussian mixtures with bounded adapted drift could subsume this proof; no absence-of-prior-work guarantee is claimed.

## Mathematical value — PASS
For a canonical non-equilibrium confined swimmer, the statement identifies a sharp, physically relevant discontinuity: arbitrarily weak heading diffusion changes the first subleading far-right-tail coefficient from a direction-dependent cosine to the same positive value in every direction. This contrasts rare events with anisotropic bulk behavior and proves non-Gaussianity even along a radial fourth-moment crossover. The result requires an angular small-ball lower bound, not just a formal Gaussian upper envelope, and is not merely recomputation of the source's moment formulas.

## Limits and comparison
The expansion holds at fixed positive thermal noise, trap, propulsion, and reset parameters. It says nothing about the prefactor, density asymptotic or uniform scaling as the rotational diffusion vanishes. The literature comparison supports best-knowledge originality but cannot establish publication priority. No independent validation was performed.

Self-review: passed. Independent audit: not yet performed.
