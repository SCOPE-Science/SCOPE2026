# Scientific review

## Correctness
PASS. The bridge-to-stationary-OU logit change of variables is checked from the exact covariance. Gaussian Hermite projection yields a nonnegative explained-variance series whose convolution factors are strictly unimodal by an explicit derivative inequality. This proves global midpoint uniqueness for every finite nonnegative Gaussian observation-noise variance, without relying on sampled comparison times. Parseval establishes convergence; direct bivariate Gaussian moments establish the exact prior variance. Independent symbolic identities and numerical cross-formula calculations corroborate (but do not replace) the proof.

## Originality
PASS with residual historical-priority risk. The closest inspected full texts concern tracked-bridge quadratic gyration, signed Gaussian Brownian areas, and modulus integration-by-parts; none of those statements implies the noisy observation conditional variance for the nonlinear absolute-area target. Relevant published mathematical findings deal with local-time/absolute-area cross covariance or signed Brownian kernel quadrature, and are also non-covering. Searches included synonyms for absolute area, Gaussian posterior integrated modulus, noisy one-point sampling and logit-time Hermite arguments. This is not an assertion that every older publication is searchable or accessible. No novel claim is made for classical Gaussian regression or bridge moment identities in isolation.

## Value
PASS. The absolute area is a natural nonlinear stochastic path integral. A single real-valued noisy observation can extract over half of its variance even though its correlation with the target is zero, so affine estimation fails completely. A globally valid sampling-time rule and a full risk/noise budget law, including a sharp quadratic high-noise decay, provide a concrete design benchmark beyond textbook signed-Gaussian-integral quadrature. The result is restricted to one fixed time and homogeneous Gaussian measurement noise, not arbitrary sensing protocols.

## Closest literature and limits
Alsolami–Burridge–Gnacik (2020, arXiv:2004.05394) study two-dimensional tracked-bridge shape, not single-observation nonlinear posterior risk. Swanepoel (2017) studies Gaussian signed areas. Grothaus–Voßhall (2016) gives modulus-law integration by parts but not the stated design. The published local-time/displacement covariance profile and stratified Brownian kernel quadrature results examine different conditioning targets and sampling models. Remaining risk: older nonlinear Gaussian functional estimation or experimental-design results could yield an equivalent midpoint theorem in different language. Analytic correctness and historical publication-priority validation remain independent-review questions.

Self-review: passed. Independent audit: not yet performed.
