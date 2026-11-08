# Scientific review of sharp quantile-transport constants

## Correctness
**PASS.** An exact CDF yields the explicit continuous quantile and derivative. For \(x>0\), writing \(t=e^{-x}\) and \(a=-\log(1-t)\), the two simple logarithmic bounds give \(h'(x)>0\), while \(a>t\) gives \((h(x)/x)'<0\). These signs prove the sharp double inequality for the quantile transport at every point, and the asymptotic forms of \(h\) establish endpoint optimality. The coupling and integrated-quantile steps are valid with all needed moments finite. The 9,264 finite diagnostics passed; they are corroboration rather than an infinite proof.

## Originality
**PASS, with a stated residual priority risk.** Doumas (2026) gives the variance representation. Giam (2026) subsequently proves scalar strict decrease, a strong prior result specifically acknowledged and excluded from the novelty claim. The submitted claim is a strictly stronger all-quantile, sharp two-sided transport theorem and its centered convex-order consequences. The inspected primary Doumas full text, Giam's accessible abstract, and the relevant stochastic-order review sections do not assert the sharp bounds. Giam's complete article was not materially inspected, so an implicit stronger argument there is a priority risk; no absence of novelty is inferred merely from unsuccessful searches.

## Mathematical value
**PASS.** For the minimum of independent coupon-collector completion-time limit variables, variance is only one measure of spread. The theorem establishes a simultaneous comparison at every pair of probability levels, explicitly identifying the optimal unavoidable contraction and its asymmetric tail behavior. It also controls all independent-copy distance moments and establishes centered convex ordering, tools that are not delivered by a scalar variance comparison.

## Literature and limits
Primary source: Doumas, arXiv:2603.11129v1 (2026-03-11). Strongest direct prior coverage: Giam, DOI 10.1016/j.spl.2026.110790 (2026), which settles scalar variance monotonicity. General methodological context: Jeon–Kochar–Park (2006) on dispersive order and Kochar (2012) on comparisons of order statistics. The logarithmic exponential law has increasing hazard rate, so cited results requiring decreasing failure rate are not a direct implication for this specific comparison. The claim does not address finite coupon counts with growing number of collectors or non-exponential extreme-value models. Historical priority and mathematical validity await independent verification.

Self-review: passed. Independent audit: not yet performed.
