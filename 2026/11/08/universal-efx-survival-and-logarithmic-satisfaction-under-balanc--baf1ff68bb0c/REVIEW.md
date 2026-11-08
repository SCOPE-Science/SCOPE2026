# Scientific assessment

## Correctness: PASS
With independent exponential values, each agent's own value is gamma distributed, and her EFX constraints compare it with sums of the largest \(r-1\) rival values. Exponential minimum–residual independence yields the exact hypoexponential decomposition, allowing direct verification of the distribution formula. Since rows involve disjoint valuation entries, their success indicators are independent. Multinomial integration yields rational exact values; a Gumbel-window integral with controlled tails yields the fixed-\(r\) asymptotic. Twenty rational-to-quadrature checks, all tested two-good harmonic identities, and five independent Monte Carlo comparisons passed using the standalone checker.

## Originality: PASS, with residual risk
The motivating 2026 online fair-division papers examine adversarial irrevocable allocation and worst-case fairness guarantees, not the risk of a fixed balanced allocation under independent realized item utilities. Igarashi and Oh (2026) analyze ex-post envy-freeness without deletions, not EFX. The nearest recoverable earlier study of independent exponential lotteries treats EF1, which compares against the *smallest* \(r-1\) rival values instead of the *largest* \(r-1\). This change produces a distinct tail distribution and a sharp universal EFX exponent. Targeted title, conceptual-equivalence, and exact-formula searches yielded no identified coverage. Similar unindexed work or non-obvious implications remain possible; database search alone cannot certify novelty.

## Mathematical value: PASS
The EFX risk is a natural measurable limitation of ex-ante balanced lottery allocations. Its leading \(\log n/n\) single-agent survival law, universal in fixed bundle size apart from an exact constant, differs sharply from known EF1 decay. The exact binomial law also reveals a nontrivial logarithmic population of individually EFX-satisfied agents even when simultaneous EFX has vanishing probability. This is a structural probability law, not a small arbitrary enumerative improvement.

## Limits and closest literature
The theorem requires independent positive exponential values for all agent–good pairs and a nonadaptive allocation of equal size bundles; growing \(r\) and correlated utilities are not treated. Closest sources: Neoh and Teh (arXiv:2610.34625), Igarashi and Oh (arXiv:2610.34906), Cohen, Teh and Wooldridge (arXiv:2609.28333), and Chen and Long (arXiv:2609.23577). The last three use either a different fairness predicate or an adversarial online probability model. A prior fixed-bundle EF1 computation is a neighboring but non-covering claim.

Self-review: passed. Independent audit: not yet performed.
