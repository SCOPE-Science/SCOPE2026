# Scientific review

## Correctness — PASS

The stochastic dynamics, first-hit stopping time, common-reset regeneration and domain are explicitly defined. Whitening transforms correlated Brownian motion to the classical absorbing wedge with opening \(\alpha=\arccos(-\rho)\), giving the sharp integrability cutoffs for the first three exit moments. The degree-two, degree-four, and degree-six polynomial formulas satisfy the stopped-process moment equations and boundary conditions; finiteness from the wedge tail legitimizes their expectation interpretation. The known Poisson-restart renewal identity then gives the exact sign polynomial \(cU+6-9c^2\). Its unique positive root determines every possible strict first-order sign, and the computed third moment gives a positive quadratic coefficient at every physical tangency. The packaged symbolic checker passed 27 assertions and independently reproduced the perfectly anticorrelated interval limit. It does not replace the analytic tail argument. Risks: no global rate optimization is proved; degenerate \(\rho=-1\) is only a verification limit.

## Originality — PASS (best-knowledge)

The nearest direct physical source, Biroli–Majumdar–Schehr, arXiv:2303.18012, treats searchers with independent Brownian noises, even when their reset alarms are shared. The new intrinsic covariance \(\rho\) is not a synonym for their reset-induced dependence. Their complete first-passage approach does not state the correlation–starting-geometry phase diagram. Chupeau–Bénichou–Majumdar, arXiv:1501.02274, study arbitrary Brownian wedges without resetting; Pal–Reuveni, arXiv:1607.06048, study restart in general without the present exact correlated-exit moments. The generic renewal formula and wedge exponent are acknowledged as prior results. The full relevant primary texts were inspected in their lawful arXiv HTML representations, including the primary paper's model and synchronous protocol, the wedge survival exponent, and the renewal identity. Comparisons against public scientific statements found adjacent but non-covering work on shared-clock dependence, independent-walker resetting, and other first-passage statistics. Residual priority risk: earlier wedge exit-moment studies could indirectly supply the formulas and a reader could combine them with the standard restart rule; an independent comprehensive literature review is still required.

## Mathematical value — PASS

This is a motivated complete **local** classification for the simplest cooperative search with nonzero intrinsic noise correlation. It separates spatial heterogeneity from common-bath anticorrelation and produces exact, scale-free critical boundaries: \(\rho_* = -(1+\sqrt{55})/9\) at equal starts and \(U=3\) as the geometry boundary beyond which arbitrarily weak reset always helps. Crucially, the vanishing first response is resolved by a strict quadratic theorem rather than being misclassified as improvement or left indeterminate. The result can guide correlation-controlled paired search protocols, although it does not imply an experimentally implementable resetting benefit or a global optimum.

## Literature and limitations

Sources: arXiv:2303.18012 (primary dated 2023-03-31), arXiv:1501.02274 (wedge survival), arXiv:1607.06048 (renewal). The claim excludes global reset optimization, empirical uncertainty and energetic accounting. The independent publication-priority check has not been performed.

Self-review: passed. Independent audit: not yet performed.
