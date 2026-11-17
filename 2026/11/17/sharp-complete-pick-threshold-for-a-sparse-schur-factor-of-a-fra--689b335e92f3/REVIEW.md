# Review: sharp complete-Pick threshold for a sparse Schur factor

## Correctness — PASS

The full all-degree coefficient argument was reconstructed: normalized positivity of both factors, nonvanishing, reduction to \(1-1/K\), coefficient identity \(c_n-\tau c_{n-m}\), and strict increase of \(c_n/c_{n-m}\) for \(n\ge m+1\). Endpoint \(\alpha=1\), equality at \(\tau=T_{\alpha,m}\), gamma asymptotics, and the positive concavity-obstruction number \(151/551\) were separately checked. The exact-rational checker passes 41970 supplementary tests; these are not substitutes for the infinite proof.

## Originality — PASS (best-knowledge, with risks)

The closest full primary manuscript is H. Sau, arXiv:2606.09680, whose complete-Pick-*factor* conclusion is weaker than complete Pick of the entire kernel. Its Example 3.2 concerns monomial numerator defects. The closest published published-finding corpus classification at `2026/11/8/SCOPE-sharp-complete-pick-phase-diagram-for-monomial-defects-of-power--a614d1883358` also studies a **numerator** monomial defect, and its threshold does not imply the **denominator** Schur-product threshold. Targeted published-finding corpus and web searches for aliases, general Pick inequalities, and reciprocal coefficient conditions found no covering family statement. Older equivalences and unindexed literature are a residual priority risk; an original 2024 characterization was compared through its abstract and the theorem quoted in Sau, not directly in full text.

## Mathematical value — PASS

The theorem exhibits an exact stability boundary for the Schur product of two individually complete-Pick kernels, identifies the first failure degree and its large-order decay, and separates complete Pick from concave operator-shift behavior by an explicit positive-parameter example. The kernel family is natural to complete-Pick factorization, not an arbitrary finite data slice.

## Scope and limitations

Only normalized single fractional-power kernels with one monomial pullback factor and real nonnegative amplitude are classified; there is no claim about general Schur factors, all concavity parameters, or independently verified publication priority.

Self-review: passed. Independent audit: not yet performed.
