# Scientific review

## Correctness — PASS

The statement fixes the entire stochastic process, positive parameters, the unwrapped coordinate, and centered variance normalization. The proof explicitly obtains bilateral-Laplace cycle-displacement tails and both cycle moments, retains the within-cycle correlation with exponential time, and invokes the appropriate centered regenerative variance law. An analytic hyperbolic inequality proves the strict negative correction for every nonsymmetric threshold. Taylor and exponential estimates give the weak- and strong-rate boundaries. The independently implemented geometric-tail and mixed-moment checks, 262 assertions, are supporting diagnostics, not infinite proofs. The uncompleted Poisson cycle has uniformly bounded second moment, giving no order-time variance contribution.

## Originality — PASS, qualified

Roberts–Sezik–Lardet (2024) computes the precise instantaneous-limit current but not a centered effective-dispersion theorem. Alston–Bertrand (2024) proves a nearest-site local-reset diffusivity formula, recovered here only at the symmetric threshold; asymmetric attraction basins are a different mathematical projector, so their lattice optimum does not dominate this theorem. Ghosh et al. (2023) use an active substrate potential during diffusion and discuss dispersion numerically, while Liu et al. (2024) chiefly investigates fat-tailed clock effects and numerical dispersion. None of the inspected primary texts supplies the exact asymmetric Brownian-projection diffusivity with the strictly negative clock-correlation term and the sharp all-asymmetry weak-rate coefficient. A broader unindexed renewal-reward/ratchet treatment could affect publication priority; there is no independent bibliographic certification.

## Mathematical value — PASS

A central transport observable for ratchet engines is the dispersion at fixed nonzero current. Without the clock–jump covariance, treating rectified reset events as independent compound-Poisson jumps produces the wrong answer. The theorem yields a new exact two-parameter dispersion law, a strict covariance sign, the sharp asymmetry-dependent enhancement coefficient, high-rate suppression and existence of a finite dispersion-maximizing reset rate. This is a motivated quantitative transport result, rather than an arbitrary finite slice. For \(\delta=1/4\) and \(\ell=8\) it predicts roughly \(1.9348D\), above the familiar nearest-site optimum, precisely because asymmetric attraction differs from nearest-site projection.

## Scope and residual risks

The theorem is about the singular instantaneous-return limit, free Brownian motion between projections, Poisson clocks and fixed interior asymmetry. The benchmark symmetric result and exact current are pre-existing. No finite-potential-strength, non-Poisson or unique-optimizer claim is assessed. Published priority remains provisional pending expert review.

Self-review: passed. Independent audit: not yet performed.
