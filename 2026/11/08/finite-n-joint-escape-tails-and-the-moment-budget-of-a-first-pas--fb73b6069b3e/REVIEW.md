# Scientific assessment of finite-\(N\) first-passage resetting escape tails

## Correctness — PASS

The statement fixes \(N\ge3\), positive barrier and diffusivity, and an arbitrary finite vector of positive excursion thresholds. The exact renewal mixture is established in Biroli–Majumdar–Schehr, arXiv:2512.00440, equations (10)–(13). Direct integration of the killed image heat kernel gives the event formula (8) in `RESULT.md`. The scaled integrand is bounded by \(w^{N-3}e^{-Bw^2/4}\), so dominated convergence produces the explicit gamma-function amplitude for every fixed \(N,k\). The same convergence gives the conditional inverse-gamma age law. Conditional surviving-distance moments converge after diffusive rescaling to Rayleigh moments, and their strictly positive integrand establishes the exact sum-of-exponents boundary. The two normalizer representations and multiple direct finite-event integrals were checked with `verify.py`; numerical tests support but do not replace the proof. Main correctness risk: no independent review of all analytical derivations.

## Originality — PASS, qualified

The closest prior paper, arXiv:2512.00440, gives the full conditional-independent stationary distribution, which is openly acknowledged as prior; it analyzes large-particle-number density, order statistics, gaps and counts. The reviewed source does not locate an explicit fixed-\(N\), large-negative-excursion orthant coefficient, posterior inverse-gamma age conditioning or total positive-moment budget. arXiv:2504.13501 covers optimization of first-passage search times, not this stationary tail comparison; arXiv:2609.24438 treats one-particle drift-diffusion threshold resetting. arXiv:2603.03162 discusses correlations in related models. Theorem 3 of arXiv:1610.04536 already establishes general tail dependence in heavy-tailed Gaussian scale mixtures; generic scale-mixture dependence is not a novel claim here. The killed Brownian conditioning and exact dependence on the model's finite particle count are essential to the quantified conclusion. Publicly available semantic record searches returned tangential work on renewal age correlations and Gaussian extreme pinning, rather than this claim; their results cannot prove global uniqueness. Publication priority and possible subsumption by a general regular-variation theorem remain genuine risks.

## Value — PASS

The stationary regime starts at three particles, but the exact positive mixed moments do not all exist there: means, variances and fourth moments have distinct particle-count thresholds. That sharp boundary matters because second- and fourth-order fluctuation statistics are natural observables in the motivating article. The result also quantifies non-vanishing dependence of any fixed number of simultaneous extreme negative excursions, rather than just saying particles are correlated, and identifies the rare-event reset-age profile. These statements are physically motivated at *finite* population size, not an arbitrary numerical slice or a renamed generic integral.

## Scope and limitations

The tail event is in the negative direction relative to the common *upper* barrier. The result is asymptotic at fixed \(N\) and fixed strictly positive thresholds, not uniform in \(N\) or near zero thresholds, and it does not extend to interacting or drifted walkers without further arguments. Originality remains provisional until wider independent literature and mathematical review. No external or independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
