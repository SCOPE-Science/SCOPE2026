# Scientific review: Pareto-reset kinetic Ising spatial correlations

## Correctness — PASS

The no-reset pair correlation solves the standard Glauber half-line initial-boundary-value problem and equals a killed random-walk first-hit probability. Combining this with the **equilibrium** Pareto renewal-age tail gives the exact expectation formula (4). Its finite-temperature asymptotic follows from a normalized exponential tilt of the hitting-time subordinator and the law of large numbers. At zero temperature, Mellin inversion of the hitting-time Laplace transform yields the sharp negative-moment constant; a Poisson bound controls the lower-age cutoff. The block-variance regimes then follow from an exact Toeplitz covariance sum. The hypotheses, exact prefactors and boundary \(\alpha=3/2\) are explicitly handled. The finite checker evaluates independent Bessel integrals and transform identities but is not substituted for an infinite proof.

## Originality — PASS (qualified)

The closest work is Anagha V K and Nagar, *Ising Model with Power Law Resetting* (arXiv:2602.15495v1, publicly first released 2026-02-17). Its paper treats magnetization probability laws with global Pareto resets and identifies spatial correlation analysis as a further direction; the present claim instead proves spatial two-point asymptotics, exact distance prefactors, a finite-temperature versus zero-temperature change, and the \(\alpha=3/2\) block-variance boundary. Magoni–Majumdar–Schehr (arXiv:2002.04867) cover global **Poisson** resetting and magnetization statistics, not the Pareto distance asymptotic. Grange (arXiv:2207.08590) analyzes voter correlations under independent **sitewise Poisson** resets, not a common heavy-tailed renewal clock. Glauber's 1963 correlation evolution, hitting-time transforms, and stationary-age formula are classical tools, not claimed as new. Indexed searches and available previous claims yielded no matching theorem under equivalent objects/parameters. Search noncoverage cannot certify novelty; an unindexed general renewal-coarsening theorem remains a residual risk.

## Value — PASS

The main 2026 article explicitly motivates exploring spatial correlations, not only global magnetization. The result distinguishes algebraic spatial clustering at zero temperature from exponential clustering at any fixed positive temperature, supplies sharp nontrivial constants, and finds a physically natural susceptibility and self-averaging transition at \(\alpha=3/2\). The threshold governs window-to-window spin fluctuations under a common reset clock, not an arbitrary sliced numerical parameter. This is a meaningful, testable, exact classification within the specified kinetic spin model.

## Limitations and closest literature

The law is annealed over the initially sampled spin configuration and stationary reset clock. No quenched statements, equilibrium fluctuation–dissipation claim, nonstationary ages for \(\alpha\le1\), finite-size simultaneous scaling, or dynamical time-correlation result is established. Priority beyond accessible full texts, searches and related published findings has not been independently verified.

Self-review: passed. Independent audit: not yet performed.
