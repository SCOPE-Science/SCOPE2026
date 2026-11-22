# Review of the sharp Gaussian-versus-forest variance boundary

## Correctness — PASS

The forest partition function \(\det(qI+L)\) gives \(\operatorname{Var}(R_q)=\sum_j q\lambda_j/(q+\lambda_j)^2\). Gaussian fourth moments give \(\operatorname{Var}(H_q)=2\sum_j q^2/(q+\lambda_j)^2\). Their difference has an exact sum-of-squares decomposition with constant \((25-n)/12\). The equality condition forces the full nonzero Laplacian spectrum to equal \(5q\), and connectedness then forces the complete graph with edge weight \(5q/n\). The complete-graph quadratic produces the stated phase window. The included standard-library exact-arithmetic checker passed 612 assertions, including direct weighted-rooted-forest enumeration on small trees. The infinite-size conclusion follows from the symbolic identity, not the finite tests.

## Originality — PASS, with priority risk

The 2019 forest-inverse-trace paper explicitly supplies the two underlying variance identities, and the 2022 follow-up studies variance reduction and practical comparisons. The claim is **not** novelty of those formulas or of Gaussian fourth moments. The new object of study is the best attainable variance difference over *all* connected weighted graphs of fixed order, with its sharp first-reversal order, unique optimizer and full complete-graph crossover interval. These extrema and their graph-equality characterization were not found as statements in the inspected primary texts or in semantic published-research searches. This optimization is short and derived from known exact formulas, so an equivalent elementary inequality or unpublished priority remains a real risk; an independent audit has not been performed. Existing published findings comparing a forest estimator with Rademacher probes concern a different probe law and are not statements about the Gaussian universal bound.

## Value — PASS

A sharp natural size threshold answers when unmodified forest-root sampling can possibly be less precise *per draw* than Gaussian trace probing. The complete-graph equality structure shows that the 25-to-26 transition is attained, not just a loose algebraic bound, and the explicit interval explains when the unexpected reversal occurs. It is a compact reference case for choosing trace-estimation methods during regularization sweeps and for checking implementations. It does not establish comparative time efficiency because Gaussian solves and forest generation have different costs.

## Closest literature and limitations

- Barthelmé et al., *Estimating the inverse trace using random forests on graphs*, arXiv:1905.02086, full 2019 conference text: equations (6), (7), and (9) contain the previously known ingredients; the inspected paper does not state the fixed-order extremal graph optimization or the 25-to-26 boundary.
- Pilavcı et al., *Variance Reduction for Inverse Trace Estimation via Random Spanning Forests*, arXiv:2206.07421, full 2022 conference text: examines forest control variates, stratification, and empirical run times rather than the present fixed-order minimax comparison.
- Other published semantic records address forest control-variate tuning, discrete Rademacher probes, or root-count fluctuations without covering the Gaussian sharp-size criterion in their available summaries. Summary-only comparisons leave a specific priority risk.

Single-draw variance is not equal-cost efficiency; no tail comparison, multiple-probe comparison or independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
