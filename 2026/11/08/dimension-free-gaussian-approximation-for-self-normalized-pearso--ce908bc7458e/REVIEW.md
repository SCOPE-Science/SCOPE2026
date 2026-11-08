# Scientific assessment

## Correctness — PASS

The exact pairwise spherical inner-product covariance gives conditional variance \(4Q/d\). The critical Gaussian-radial coupling has an exact mean-square discrepancy \(2\operatorname{Var}(\|G\|/\sqrt d)\le2/d\), independently of the entire length array. A variance-one Gaussian quadratic form in each ambient coordinate has fourth moment at most \(15\), so a standard Wasserstein normal bound yields \((3\cdot15^{3/4}+\sqrt2)/\sqrt d<25/\sqrt d\). All quantifiers include dimension-varying random, dependent lengths and unrestricted finite step counts. No finite enumeration is used as an infinite proof.

## Originality — PASS, subject to historical priority

The closest 2026 source, arXiv:2609.05195, establishes first-order almost-sure/probability convergence and a moment inequality (Lemma 5.3), but no unconditional-in-step-count conditional \(W_1\) Gaussian approximation. Kabluchko–Marynych, Grundmann and Stam cover important fixed-length/equal-length/i.i.d.-radial special cases; these are not presented as new. The new statement combines a universal normalization, arbitrary dependence of lengths, unrestricted growth and an explicit dimension-only bound. An unlocated general-purpose Gaussian quadratic approximation may imply it; this remains an explicit priority risk.

## Value — PASS

The new limit is a second-order distributional strengthening of a recent first-order result in the same model. Its uniformity removes all assumptions on the step count and lengths that would normally be needed for unnormalized convergence, while handling Dirichlet and heavy-tail dependent lengths conditionally. It is a reusable mechanism for separating angular noise from random radial mixing in high-dimensional random flights; the exact finite-dimensional skewness formula supplies an independent consistency check.

## Verification and limits

`verify.py` reproduces exact small-dimensional spherical moment contractions, verifies quadratic Gaussian moment identities and the radial-variance bound, and runs seeded numerical diagnostics. It is a finite checker, not a complete certification of infinite asymptotics. Complete historic priority has not been independently verified. The normal approximation requires at least two positive lengths, and the value \(25\) is not claimed sharp.

Self-review: passed. Independent audit: not yet performed.
