# Review of endpoint singleton limits

## Correctness

**PASS.** For every prescribed \(r\)-subset of singleton labels, the exact event probability is \(B_{n-r}/B_n\). This yields all joint factorial moments for disjoint spatial windows. The Bell saddle-point formula establishes the Poisson limit under the natural \(B_{n-1}/B_n\) scale; far-left and far-right windows are disjoint in original labels. The expected gaps require a separate fourth-moment estimate for the total singleton count, which controls reciprocal-count tails. A standalone exact checker passed 1,106 cases; no finite test is treated as proof of the limit.

## Originality

**PASS, with acknowledged priority risk.** Sun and Wu (arXiv:1007.1341v1, Sections 2–3, especially Remark 3.11) derive finite singleton-position counts and request asymptotic expectations, but the inspected paper does not state independent endpoint Poisson point processes or their mean gap scale. Arratia and Tavaré (Advances in Mathematics 104, 1994; arXiv:1308.3279v1, Sections 1, 6, 10.1) derive Poisson approximations for component-size counts; the fixed labeled endpoint singleton process and joint endpoint limit are a different observable. NIST DLMF 26.7.7 supplies an asymptotic ingredient. published-finding corpus semantic comparison did not identify the same theorem. An unrecorded corollary of a more general exchangeable sparse-point-process result could cover it; literature search does not establish uniqueness.

## Value

**PASS.** The 2010 study explicitly motivates asymptotics for extreme singleton labels. The result resolves their scale, gives the full two-ended Poisson process rather than a single marginal, and demonstrates asymptotic independence across the endpoints in a setting of strictly positive finite-sample indicator covariance. The precise \(n/W(n)\) gap size has an intrinsic interpretation as the reciprocal singleton density, not an arbitrary parameter slice.

## Limitations and literature

The conclusion concerns fixed bounded scaled windows, not uniform error bounds for moving windows or finite-\(n\) independence. The finite checker cannot certify the limiting theorem; priority is not independently established. Closest inspected sources: Sun–Wu, https://arxiv.org/html/1007.1341v1; Arratia–Tavaré, https://arxiv.org/html/1308.3279v1; NIST DLMF, https://dlmf.nist.gov/26.7. Goh–Schmutz (1994), https://doi.org/10.1137/S0895480190186974, was available only at abstract level; its stated subject is largest block size, not singleton-label extremes.

Self-review: passed. Independent audit: not yet performed.
