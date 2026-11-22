# Scientific review

## Correctness — PASS

The finding concerns one explicit positive measure and four exact heights, not an unproved complete bifurcation curve. Direct differentiation yields a quartic in squared position with a positive denominator. At the four heights the primitive quartics and the exact rational sign brackets are verified by `check_exact.py`; the upper bounds on positive roots follow from Descartes' rule. Equal numbers of distinct roots and sign-variation bounds also rule out multiplicities. The center is nondegenerate, and the signs of the derivative determine exactly three, two, three, and one local maxima. The equal-weight sample representation is arithmetic, and robustness under sufficiently small distinct perturbations follows from simple-root stability and uniform tail signs. Risks: the robustness radius is not quantified; this does not affect the fixed-weight exact counterexample.

## Originality — PASS, best knowledge

The closest relevant primary text is Chaudhuri and Marron (2000), which exhibits Cauchy-kernel noncausality with signed regression weights and expressly reports no example with all positive observations, proposing that density-estimation causality may hold. The present example has only positive masses, so it is not a special case of the earlier signed construction. Hall, Minnotte and Zhang (2005) principally address compactly supported kernel density estimators, which does not directly cover the Cauchy kernel. Chaubey (2018) studies the wrapped Cauchy/Poisson circle estimator; Vila et al. (2022) study another model of trimodality. A previously indexed equal-weight three-atom Poisson result has a single three-to-one threshold, not a positive reentrant two-to-three mode transition for unequal weight. Actual semantic literature and published-result searches found no exact or stronger covering statement. Risks: inaccessible or unindexed historical positive-weight counterexamples remain possible, so novelty is provisional.

## Value — PASS

A mode's appearance under stronger positive-kernel smoothing contradicts a natural scale-space causality property, and the sign of the input masses is essential: it directly addresses a historical positive-data conjectural possibility. The four certified heights, rational masses and transfer to a finite equal-weight sample provide an unusually transparent analytical witness, useful for separating Gaussian diffusion intuition from Cauchy/Poisson harmonic extension. Its value is the explicit exact certificate with two reversals of mode-count direction at four fixed heights, not the known qualitative fact that a non-Gaussian smoothing kernel may create modes. An earlier review asserts that Cauchy KDEs can do so; historical priority for an equivalent quantitative witness remains uncertain.

## Scope and priorities

The result is not a complete all-weight or all-height classification, and it does not assert the earliest possible number of distinct sites. There is no independent audit. References and sources are listed in `RESULT.md`; the exact checker constitutes the core computational evidence.

Self-review: passed. Independent audit: not yet performed.
