# Scientific review

## Correctness — PASS

The transfer operator has exactly the stated action on the four functions \(1,\mathbf1_{[0,1/\beta)},x,x\mathbf1_{[0,1/\beta)}\); the stationary density is normalized and invariant. Duality converts the coordinate covariance at every lag into an exact finite-dimensional matrix element. The four distinct characteristic roots and the explicit three-lag quadratic recurrence remove the third nonconstant mode, and initial moments determine the remaining coefficients. Rational factorization with strictly positive coefficients after \(\beta=1+t\) proves positivity and monotonicity without sampling. The packaged `check.py` verifies all critical polynomial identities symbolically. The proof's scope is stationary \(m\in\mathbb Z_{\ge1}\) only.

## Originality — PASS within inspected evidence

The classic invariant density is attributed to Rényi/Parry; Cornean–Sørensen (2025) already provide the exact relevant invariant transfer space and spectral eigenvalues for the encompassing quadratic family. Suzuki (2023) studies stationary densities and response in random beta systems. The inspected full texts do not assert the exact coordinate correlation coefficients, the vanishing specific mode, or the strict ordering of the Green–Kubo variance over all integral quadratic bases. These are directly computable consequences of the existing finite-dimensional framework, not a claim of a new transfer construction. This close derivability, unindexed papers, and existing numerical diffusion formulas are residual originality risks, not concealed evidence.

## Mathematical value — PASS

The coordinate is a canonical interval observable and the long-run variance is a natural fluctuation measure, rather than an arbitrary finite statistic. The combined identity distinguishes observable-invisible spectral modes, proves positivity at every lag despite a negative alternating mode, and gives a sharp ordered transport law over the entire integer-family of quadratic Pisot bases. This identifies a non-obvious parameter trend beyond the previously published spectral decay asymptotics and exact invariant densities. No claim is made about central limit behavior or random beta mixing.

## Closest literature and limits

Suzuki (2023, arXiv:2303.17521) is the dated scope source; Cornean–Sørensen (2025, arXiv:2502.17113), especially Appendix C, is the closest direct mathematical antecedent. The inspected results supply a powerful framework from which aspects of this theorem can be reconstructed; no independence, publication priority or external certification is inferred. Generalizations to other algebraic bases and nonstationary initial states remain unproved.

Self-review: passed. Independent audit: not yet performed.
