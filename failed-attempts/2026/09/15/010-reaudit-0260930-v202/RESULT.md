# Conditional span-dimension lemma and weak/strong hypothesis separation for fixed-field reciprocal spans

## Context

Let DF(p,n,m) = (F_{p^n}, Frob_{p^m}) with m | n, K = F_{p^n}, F = Fix(sigma) of size q = p^m, and k = F_p. Hils-Hrushovski-Ye-Zou (arXiv:2406.00880) prove coarse pseudofinite dimension delta equals transformal transcendence degree for quantifier-free types and existential-definable sets (Theorem 7.7, Corollary 7.9), and give a fixed-prime forall_2 counterexample (Example 7.12) with delta = 0 but positive transformal degree under the strong hypothesis lim p^{m_i}/n_i = 0. The characteristic-zero target asks whether delta = max trf.deg holds for all L_sigma-definable sets under only the weak hypothesis m/n -> 0 (plus q -> infinity, p -> infinity). The natural negative route is verbatim transfer of the Example 7.12 fixed-field linear span.

## Definitions

For y in K \ F let X = {1/(x-y) : x in F}, Y = k-span(X), Y^F = F-span(X). Coarse dimension: delta(Z) = lim_U log|Z_i|/log|K_i| with |K_i| = p_i^{n_i}. Note [K:F] = n/m and [F(y):F] <= n/m for every y in K.

## Result

Lemma (proved): every N-subset of X with N <= [F(y):F] is F-linearly independent (hence k-independent). Conditional corollary (proved): if [F(y):F] >= q then dim_F(Y^F) = dim_k(Y) = q exactly, so log|Y|/log|K| = q/n and log|Y^F|/log|K| = mq/n. Consequently, conditional on maximal-degree approximants, the target-compatible sequences A (m=1, n=p^2, p->infinity) and B (m=1, n=p, p->infinity) both satisfy m/n->0, q->infinity, p->infinity but give span coarse contributions 0 and 1 respectively (sequence B value an explicitly conditional hypothetical). The verbatim fixed-prime span transfer therefore cannot yield a delta=0 counterexample in general: it needs a strong subsequence (q/n->0) plus maximal-degree approximants.

## Proof / evidence

Partial fractions over F: from sum_{j=1}^N c_j/(x_j-y) = 0 with distinct x_j in F and nonzero c_j in F, clearing denominators gives nonzero P(T) = sum_j c_j prod_{l!=j}(x_l-T) in F[T] of degree <= N-1 with P(y) = 0. Contrapositively N <= [F(y):F] forces independence. Under [F(y):F] >= q all of X (size q) is independent, giving exact rank q and the stated log-ratios. Sequences A and B are admissible (m|n after suitable indexing, m/n->0) and maximal-degree approximants exist by finite-field primitive elements; on A, q/n = 1/p -> 0, on B, q/n = 1. Executed artifact output/artifacts/span_delta.py confirms: GF(4)/GF(2) trace-kernel identity ker(Tr) = im(sigma-id) of size 2; actual k-ranks and F-ranks for maximal-degree y in A-like (p=2,m=1,n=4, full rank 2), B-like boundary (p=2,m=1,n=2, full rank 2), capped (p=3,m=1,n=2, k-rank 2 with dependence certificate (1,2,2)), and F-capped (p=2,m=2,n=4, F-rank 2 = [K:F]) cases; plus the conditional asymptotic delta table.

## Limitations

Dimension and coarse-contribution formulas proved only in the conditional case [F(y):F] >= q (uncapped regime q <= n/m); no capped generality dim = min(q,n) is claimed and capped script rows are examples only. All sequence deltas conditional on maximal-degree approximants. Uniform cross-p L_sigma-definability of the span (finite-field trace has unboundedly many terms; MS08 bilinear-form input is fixed-prime) and positive transformal degree of the ultraproduct span element remain open. The full characteristic-zero dichotomy stays open.

## Reproducibility

Run python3 output/artifacts/span_delta.py. Check the DRAFT.md Section 2 proof and Section 4 for the rank table. Compare HHYZ Section 7 (Theorems 7.7-7.8, Corollary 7.9, Example 7.12) for the fixed-prime baseline.

## References

Hils-Hrushovski-Ye-Zou, Lang-Weil type estimates in finite difference fields, arXiv:2406.00880. Zou, Pseudofinite difference fields and counting dimensions, arXiv:1806.10026. Macpherson-Steinhorn, One-dimensional asymptotic classes, Trans. AMS 360 (2008), Lemma 3.9 (fixed-prime bilinear form, cited for definability context only).
