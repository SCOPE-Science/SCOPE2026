# Self-review

## Correctness — PASS

The exact radial Fokker–Planck generator becomes the squared-Bessel generator under \(Y=R^4/(16D_0)\), with shape \(k=1-\alpha/2\). The starting-from-zero gamma law, Poisson-age product, closed stationary moments, affine conditional mean, and strict digamma-based inversion were reconstructed independently of the computational checker. The strict likelihood-ratio order follows by conditioning on the gamma factor and the increasing posterior family, not by inspecting plots. The packaged checker executes symbolic identities, quadrature comparisons and an exact transition simulation. Finite checks do not establish the theorem on their own.

## Originality — PASS (qualified)

Sandev et al., arXiv:2609.24427v1, already provide the exact propagators and the stationary Bessel densities. Liu et al., DOI 10.1103/xz7y-n8w2, study interpretation choice using time-averaged diffusivities for a related regularized radial model. Rose et al., arXiv:1806.01298, give the general resetting spectral shift. The new contribution concerns the model-specific fourth-power conjugacy and autocorrelation, the strict radial likelihood-ratio hierarchy and the invertible three-parameter observation map. Searches of these publications, published-finding corpus and related literature did not find the complete assertion; an unindexed earlier specialization and the generic spectral implication remain real risks.

## Value — PASS

The three-parameter inverse problem is directly motivated by published work on identifying multiplicative-noise conventions. The stationary shape ratio is independent of the reset rate and diffusivity, the lag correlation is independent of the convention and diffusivity, and the fourth moment fixes the remaining scale. These exact complementary observables give population-level identifiability without first knowing any of the three parameters. The likelihood-ratio theorem additionally orders every increasing radial cost, not just a few moments. The result does not claim finite-sample identifiability rates or extension to other boundary/reset/memory models.

## Primary literature and limitations

Compared the motivating full article's stationary, threshold, memory and conclusion sections; the related open regularized-diffusion inference study; and the general reset spectrum study. The exact singular boundary process, ordinary Poisson resetting, and population observables are essential; general memory subordination or regularized diffusivity may change the two-time statistics. No independent audit or physical measurement has been performed.

Self-review: passed. Independent audit: not yet performed.
