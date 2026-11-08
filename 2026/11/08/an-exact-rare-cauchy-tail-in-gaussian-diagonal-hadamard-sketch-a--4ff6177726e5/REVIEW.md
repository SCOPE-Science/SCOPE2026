# Scientific review

## Correctness — PASS

The proof starts with the exact two-column Gram identity for uniformly sampled Hadamard rows, derives the coefficient rational form, and checks almost-sure nonvanishing of its denominator including the rank-one Gram collision cases. Gaussian angular integration gives the conditional CDF and finite support when \(|\rho|<1\). When \(\rho=\pm1\), independent normal sum and difference give a standard-Cauchy quotient. The two collision events have total probability \(2^{1-m}\); the other finitely many mixture components are bounded by \(m/(2\sqrt{m-1})\) for \(m\ge2\). This proves the exact far-tail and the complete \(0<p<1\) absolute-moment regime. The 105 arithmetic/quadrature tests in `check_tail.py` are supporting finite checks, not the proof.

## Originality — PASS, subject to historical priority

Song and Zhang (2026, Section 3) already give the starting coefficient formula and state that a ratio of independent Gaussians is Cauchy. They establish a constant-probability failure on a *different event*, but not the exact rare-event mixture, support cutoff, far-tail coefficient or all-integer sampling-budget moment threshold. Price, Song and Woodruff (2017) and Song, Ye, Yin and Zhang (2023) use a sign-diagonal SRHT and do not imply the new Gaussian-diagonal distribution. Comparisons with accessible previous mathematical claims and relevant searches yielded no stronger direct coverage. Because Gaussian quotient identities are classical, earlier equivalent priority is a residual risk.

## Value — PASS

The example exposes a substantive gap between high-probability regression accuracy and integrated-risk guarantees for a natural random-sketch modification: the estimator is defined almost surely yet has infinite expected absolute error and squared error at every finite row count. The exact finite-\(m\) collision weight identifies the mechanism and the precise rare-tail scale. It is a sharp, self-contained benchmark for analyzing or preventing undesirable sketch-conditioning events, not a claim about the separate Gaussian-pooling construction.

## Limits and closest literature

The conclusion is restricted to one-column full-rank least squares, independent row sampling with replacement, and a shared Gaussian diagonal. It does not cover sampling without replacement, regularized coefficients, fresh per-row Gaussian weights, or the balanced pooled sketch. The 2026 primary paper already identifies failure of the same Gaussian-diagonal modification by a different argument; the present claim is the exact full risk-tail classification. Priority remains best-knowledge.

Self-review: passed. Independent audit: not yet performed.
