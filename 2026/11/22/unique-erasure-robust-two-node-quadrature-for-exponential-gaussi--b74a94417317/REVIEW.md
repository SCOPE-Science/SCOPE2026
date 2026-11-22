# Scientific review

## Correctness

**PASS.** Exact covariance integration and inversion of the two-point covariance matrix yield the expected posterior integral-variance reduction. A fixed-gap centering argument has two strictly negative derivatives with respect to \(\cosh\) of the center offset, hence rules out asymmetric competitors. Strict log concavity of the centered objective proves one interior optimum; sign checks at both endpoints prove existence. Implicit monotonicity and asymptotic expansions derive the advertised limits. The decoded standalone checker provides supplementary symbolic and direct numerical comparisons. It does not substitute for the analytic global proof.

## Originality

**PASS (self-review, provisional historical priority).** The strongest directly related published result, *Exact optimal nodes and stratification penalty for Ornstein–Uhlenbeck Bayesian quadrature* (2026), includes the fixed two-node \(p=1\) case, but its fixed exact-observation optimality theorem does not imply the objective when the observation set is randomly thinned. Older work on exact kernel conditioning and numerical integration supplies the risk formula and theory, not the present mixture optimization. A separate optimal Gaussian-noise design keeps both noisy observations rather than independently erasing them; those objectives are not equivalent. Claim-level checks also found a bridge-path erasure theorem under a different covariance and *path* loss. Inaccessible full dissertation text leaves an explicitly bounded priority risk. No exhaustive historical priority claim is made.

## Value

**PASS.** Independent query delivery failure is a natural constraint for scheduled sensor or costly function evaluations. The exact two-site theorem supplies a usable robust placement rule, proves that duplicated sites are never optimal for any positive delivery probability, and gives a strict monotone design response and two distinct correlation-length regimes. These solve an all-position optimization problem, not a numerical instance or restatement of the always-delivered answer. The result does not generalize to larger designs or additive noise without further analysis.

## Closest literature and limitations

The 2018 kernel-energy framework and 2019/2022 Bayesian quadrature analyses establish the context and standard conditioning, while the previously published stationary OU two-node theorem owns the \(p=1\) boundary. The new result concerns every \(0<p<1\), with the same scientific limitations listed in RESULT.md. Independently checking historical priority against inaccessible dissertation text is still warranted.

Self-review: passed. Independent audit: not yet performed.
