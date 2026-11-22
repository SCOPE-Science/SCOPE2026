# Scientific assessment of the two-dimensional genomic-offset reliability law

## Correctness — PASS

The asserted law has been reconstructed directly from the source model: fixed two-dimensional positive-definite GEA metric, independent Gaussian locus effects, one adaptive trait, no direct effects, and Gaussian environmental displacements. The covariance of Gaussian quadratic forms reduces the quenched squared correlation to a rank-one Rayleigh quotient. Under the actual allelic-effect ensemble the orientation is anisotropic Gaussian, not uniform; the proof correctly uses the ratio of squared independent normal coordinates. Inversion establishes all CDF endpoints and degeneracy at equal eigenvalues. Two elementary angular integrals yield the mean; exact differentiation proves strict monotonicity; direct expansions prove the distinct mean and median asymptotic rates. The executable checker passed after invocation from the standalone package. Numerical checks are corroborative only; the infinite-parameter theorem rests on symbolic identities.

## Originality — PASS within inspected literature

François (2026), equations (3.7), (4.19) and (4.20), provides the rank-one correlation formula and deterministic spectral bounds. Those are explicitly prior results, not contributions here. Inspection of its full available HTML also found formulas for *relative fitness at a fixed environment*, a different random variable; it does not give the architecture-averaged CDF of the *across-environment squared predictive correlation*. Gain et al. (2023) develops the geometric genomic-offset model and compares predictive correlations across simulations and a common garden, not the analytical ensemble law established here. Capblancq et al. (2026) concerns generalized stabilizing-selection gradients; only abstract-level access was possible, with resulting priority uncertainty. Published mathematical records on anisotropic Gaussian angles and rank-one matrix approximations were also compared; their applications, statistics, and probabilistic interpretations do not imply this conditional genomic-offset law without the present reduction and integration. Cauchy-ratio and quadratic-normal identities themselves are classical and not asserted to be new.

The precise nontrivial distinction is the entire predictive-reliability distribution *under an explicit uncertain genetic architecture*, along with the different average-versus-typical spectral rates. The 2026 originating paper's spectral support bounds alone give neither a probability of poor prediction nor a mean reliability loss.

## Value — PASS

Genomic-offset prediction is often evaluated by a single explanatory correlation, but an unobserved genetic architecture makes that correlation itself uncertain. Under a natural two-gradient/one-trait benchmark, the exact CDF calibrates how frequently architecture uncertainty yields low predictive reliability even with fixed GEA information. The divergence between \(\kappa^{-1/2}\) average error and \(\kappa^{-1}\) median error resolves a consequential distinction between typical and mean performance: exceptionally misaligned architectures dominate the average despite increasingly high typical accuracy. This is a natural mathematical quantity tied to the motivating framework rather than an arbitrary numeric subcase.

## Limitations and priority risk

The law does not certify empirical fitness prediction; Gaussianity, a single adaptive trait, two environmental variables, positive-definite metrics, and absent direct effects matter. Relevant generalized-selection work was accessible at abstract level only, and an unindexed equivalent of the planar Gaussian ratio law may predate this application. The originality judgement is therefore literature-bounded and requires independent historical evaluation.

Self-review: passed. Independent audit: not yet performed.
