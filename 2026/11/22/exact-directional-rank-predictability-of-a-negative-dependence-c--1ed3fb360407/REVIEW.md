# Self-review

## Correctness — PASS

For all real parameters \(\theta>0\), the published piecewise copula is differentiated in each conditioning coordinate. Squared conditional CDFs are integrated exactly over the entire unit square, with switching curves handled by partitioning their domains. The population formula \(\xi(B\mid A)=6\int\int F_{B\mid A}^2-2\) follows from uniform marginals. Both closed forms, their strict gap, and the one-root global maximum have complete symbolic derivations in RESULT.md. Exact symbolic simplification and independently implemented adaptive quadrature of the original conditional CDFs passed five parameter checks. The infinite continuum assertion relies on the analytic integration and cubic monotonicity, not the numerical samples.

## Originality — PASS (bounded literature comparison)

The 2020 Bhuyan–Ghosh–Majumder–Mitra paper supplies the underlying joint law; the 2021 preprint and 2022 published Ghosh–Bhuyan–Finkelstein paper supply the exact copula, conditional laws and ordinary symmetric rank correlations. Those are **not** claimed as new. The inspected 2024 survey of rank-dependence properties covers many other named copulas, including Marshall–Olkin, but not a directional coefficient for this one. The 2026 unrestricted rank-dependence feasibility result and published generic rank-correlation identities do not imply the model-specific two coefficients or their unique sharp asymmetry maximum. Search comparisons with other published records on directional rank dependence, the Marshall–Olkin family and reflection operations yielded no statement covering this theorem. Historical priority is not certified exhaustively; an inaccessible or unindexed earlier model-specific calculation remains possible.

## Value — PASS

The original family is explicitly asymmetric and strongly negatively dependent, yet its Kendall coefficient cannot describe which variable is more predictable from the other. The exact two nonlinear, directional rank coefficients and the unique parameter of maximum asymmetry quantify a motivated characteristic of the original model; the sharp result is over its entire natural parameter domain and adds information not contained in the already-known symmetric concordance measures. The result is not an estimator, confidence interval, or causal direction argument.

## Closest sources and limits

- Bhuyan et al., *Stat* (2020), DOI 10.1002/sta4.276: original joint construction and negative dependence.
- Ghosh, Bhuyan and Finkelstein, arXiv:2102.05386 (2021), published *Statistical Methods & Applications* (2022), DOI 10.1007/s10260-022-00636-3: the copula and its conditional laws and Kendall/Spearman calculations are prior results.
- Ansari and Rockel, *Dependence Modeling* (2024), DOI 10.1515/demo-2024-0002: inspected family-by-family dependence table and rank-correlation methods.
- *The exact region and an inequality between Chatterjee's and Spearman's rank correlations*, *JMVA* (2026), DOI 10.1016/j.jmva.2026.105630: universal feasible region, not this model-specific calculation; only accessible summary/material was inspected.

The proof is analytical, and the attached checker is supplementary. No external independent validation has been performed.

Self-review: passed. Independent audit: not yet performed.
