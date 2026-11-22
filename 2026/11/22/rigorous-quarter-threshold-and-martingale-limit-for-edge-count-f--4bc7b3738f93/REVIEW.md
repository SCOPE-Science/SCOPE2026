# Scientific review: edge-count variance in parent-linked duplication graphs

## Correctness — PASS

The claim is restricted to fixed \(0<p<1\), \(0<r\le1\), and the one-vertex seed. The proof independently derives all three finite recurrences from the attachment marks, including the crucial cancellation of a \(4p^2v_n/n^2\) term when applying total variance. Degree-square closure follows from the exact identity \(\sum_u\sum_{w\sim u}\deg(w)=\sum_w\deg(w)^2\). Jensen's inequality makes the variance forcing nonnegative. Both exponents \(2p\) and \(2p+p^2\) are below one at and below the quarter boundary; the forcing therefore has a positive finite limit there. Above the boundary, \(2p+p^2<4p\) makes the exact variance series summable. Its positive limit supplies the nondegenerate \(L^2\) martingale convergence. Exact finite-law enumeration and the earlier published \(r=1\) coefficient cross-check passed 2,248 rational assertions. The checker is not substituted for the analytical infinite proof.

## Originality — PASS under checked evidence

Bhat et al. (2016), Sec. II.B, already anticipated **the same three variance exponents at \(p=1/4\)** for the \(r=1\) copying model, derived an exact but unclosed variance identity, and gave a continuum-derived coefficient for \(p\le1/4\). Thus the quarter boundary and earlier formal coefficient are explicitly not claimed as discoveries. The assessed new claim rigorously closes the exact finite moment system for the parent-link model, proves coefficients across all fixed \(0<r\le1\), provides a convergent exact supercritical constant, and proves a nondegenerate \(L^2\) centered martingale limit. The source's \(r=1\) coefficient is recovered exactly, not contradicted. The recent 2026 full text studies typical degrees, local weak limits and maxima; no theorem inspected there implies the global variance limit. Hermann and Pfaffelhuber (2016) concern \(r=0\), starting with an initial edge; Turowski and Szpankowski (2021) add edges to every non-neighbor with probability \(r/n\), a genuinely different law. The closest indexed edge-density finding covers a distinct full-copying endpoint \(p=1\), outside the theorem's domain. An unindexed rigorous variant of the older physics computation remains a historical priority risk.

## Value — PASS

A previously unclosed second-moment equation is resolved by tracking exactly one extra natural graph statistic, the sum of squared degrees. This converts a predicted fluctuation transition into a rigorous variance trichotomy with computable constants for the entire parent-link probability range and gives a genuine nondegenerate martingale limit. Both the exact finite closure and positive-supercritical variance matter for inference about network densification and non-self-averaging; this is more than a routine normalization or parameter relabeling. No Gaussian limit below the threshold or supercritical limit distribution is asserted.

## Closest literature and residual limitations

The relevant primary sources are Bhat, Krapivsky, Lambiotte and Redner (2016), arXiv:1610.01662, Sec. II.B; Dey, Maitra, Manthripragada and Terlov (2026), arXiv:2611.00123, §§2–3; Hermann and Pfaffelhuber (2016), arXiv:1408.0904, §§2–3; and Turowski and Szpankowski (2021), DOI:10.37236/9251, §§1–2. Unindexed earlier proofs or alternative parameterizations remain possible. The package includes a reproducible finite exact checker; no independent validation or audit has occurred.

Self-review: passed. Independent audit: not yet performed.
