# Scientific review

## Correctness — PASS
The exponential Gaussian Markov conditional-variance identities reduce the integrated prediction loss to the sum of two terminal-gap costs and \(n-1\) interior-gap costs. Both are strictly convex, have derivative zero at zero, and force a unique, strictly interior optimum. Lagrange conditions show symmetric margins and equal interior gaps. A positive algebraic derivative difference proves the terminal gaps are strictly shorter. Both asymptotic expansions follow from those same equations. The extracted standalone checker passed 1,192 supplementary assertions, not a substitute for proof.

## Originality — PASS (historical priority provisional)
The closest accessible primary paper, Dasgupta, Mukhopadhyay and Keith (arXiv:2004.13967, Section 5 and Theorem 5.2), fixes both endpoints to \(0\) and \(1\) before optimizing and cannot imply the nonzero free-terminal optimal margins. Zimmerman (2006, DOI:10.1002/env.769) motivates kriging network design but studies different finite-grid settings. Sikolya and Baran (2019, DOI:10.1080/03610926.2019.1645855) likewise fix endpoints. The closest identified OU Bayesian-quadrature result optimizes variance of the field integral rather than integrated pointwise predictive variance and produces longer, not shorter, terminal gaps. The accessible published literature and semantic research-record comparisons found no equivalent or dominating result; failure to find one is not proof of priority. The full Antognini–Zagoraiou (2010) article was inaccessible and remains a material historical-priority caveat.

## Value — PASS
The unconstrained optimum is substantively different from the common endpoint-fixed designs; a 40.44% model-prediction-variance improvement arises for two stations at \(	heta L=1\). The exact \(1:3\) near-unity-correlation margin ratio, unique optimizer for every sensor count, and logarithmic long-transect boundary correction are relevant benchmarks for geostatistical monitoring. The result does not imply empirically calibrated improvements when drift, noise or nonstationarity is present.

## Closest literature and limits
Compare Zimmerman (2006), Dasgupta et al. (2020 preprint / 2022 journal), Sikolya–Baran (2019), and the inaccessible exact-design paper of Antognini–Zagoraiou (2010). No independent mathematical or historical-priority audit has been completed. The known-mean, known-covariance, exact-observation, one-dimensional assumptions are essential. The result proves no general noisy, empirical or higher-dimensional optimality.

Self-review: passed. Independent audit: not yet performed.
