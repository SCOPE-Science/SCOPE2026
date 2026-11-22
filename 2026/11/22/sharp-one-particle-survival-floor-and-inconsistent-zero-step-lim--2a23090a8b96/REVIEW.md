# Scientific review

## Correctness

PASS. The one-particle transition separates exactly into a zero-Poisson-predictor branch and a positive-predictor binomial-backtracking branch. The Poisson generating function yields the closed-form survival formula without approximation; nonincrease of the state and absorption at nonpositive counts yield the all-time semigroup; the Taylor coefficient yields the wrong continuum limit. Completing a square gives the unique, globally sharp \(3/4\) midpoint floor. Verification is reproducible from the accompanying independent implementation of the probability kernel. The proof does not rely on finite tests as infinite certification.

## Originality

PASS with residual risk. Definition 3 and Appendix A of Scott--McCallum--Foster (arXiv:2611.16975v1) were read directly, including the source's low-count condition and first-order local weak-error result. These facts mean that a local low-count inconsistency is **not** the novelty asserted here. The new full one-molecule semigroup, exact unadjusted comparator, and the sharp global survival floor/large-step return are additional statements not obtained by merely restating the source's generic bounds. Earlier tau-leaping references concern original weak-order scaling and alternative nonnegativity mechanisms. Search cannot exclude an older unindexed equivalent finite-step calculation.

## Value

PASS. The algorithm's intended binomial handling of degenerate predictor steps is most active exactly in low-copy-number kinetics. Here its backtracking prevents one-particle disappearance in at least three quarters of midpoint steps, even as the true disappearance probability tends to one, while the scheme it modifies retains exactly the right one-particle survival probability. The exact floor and the noncommutation of step refinement with the true generator give an actionable boundary for using the correction or adding critical-event handling. No stronger claims about typical systems are drawn.

## Closest literature and limitations

The source's Appendix A first-order local-error coefficient already warns that degenerate, low-count channels are outside favorable error assumptions. The present global formula goes beyond that coefficient. The results are restricted to one initial molecule, a clipped linear death propensity and a fixed \(\theta\in[1/2,1)\); the large-step floor requires \(\theta=1/2\). Review of earlier weak-order and negative-population publications was limited by access to some article full text. The mathematical argument remains subject to independent audit.

Self-review: passed. Independent audit: not yet performed.
