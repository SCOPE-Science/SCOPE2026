# Review of the binary Sinkhorn contraction theorem

## Correctness — PASS

For every positive binary kernel and both interior target marginals, the exact row/column log-ratio update is derived, not postulated. The Bernoulli variance decomposition yields a nonnegative derivative, and the rationalization with \(k=\sqrt R\) shows that its supremum occurs at an explicit finite positive scaling. AM–GM yields the closed optimal constant, so both the upper Lipschitz estimate and its sharpness hold globally. The rank-one case, strict contraction, unique projective fixed point, the classical Birkhoff equality condition and reverse-order transposition are separately addressed. The 972 exact-rational identities and 4,200 randomized cases validate implementation/algebra but are not the universal proof.

## Originality — PASS, with priority risk

The nearest covering-looking global theory is the Hilbert-metric bound of Lehmann, von Renesse, Sambale and Uschmajew (2021/2022), which supplies the more conservative square of the Birkhoff coefficient. Its equality condition for imbalanced binary row targets does not follow, and the new exact coefficient is strictly sharper. The finite-step derivative Markov kernel of Forde (2026) supplies a general pointwise framework but does not itself state the optimized binary supremum or the two-marginal order criterion. Xu–Chen (2026) and Gao et al. (2026) study acceleration or local convergence, with different implications. Knight (2008) presents an older exact asymptotic rate but was available here only in abstract, leaving open an equivalent historical binary result. The derivative is standard calculus; the asserted increment is the all-scaling sharp value and ordering. No database absence is treated as proof of novelty.

## Value — PASS

The exact, computable, worst-case factor gives a parameter-dependent nonasymptotic guarantee for a basic numerical algorithm. It exposes a significant regime in which a standard kernel-only Birkhoff guarantee misses strong stability induced by imbalanced marginals. The ordering rule compares meaningful projective certificates; it does not pretend different local eigenrates or per-instance iteration domination. It supplies a calibrated benchmark for more complex scaling methods.

## Limitations and sources

Strict positivity, binary dimensions, exact unrelaxed half-steps and projective coordinates are essential. Historical priority in older binary IPFP and contingency-table literature remains incompletely determined; Knight (2008) was not read in full. Main primary comparators: arxiv:2605.30267v1, doi:10.1007/s11590-021-01830-0, arxiv:2609.07954v1, and arxiv:2608.11760v1. All present verification is same-model; no independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
