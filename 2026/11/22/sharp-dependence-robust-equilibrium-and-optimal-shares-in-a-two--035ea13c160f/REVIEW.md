# Scientific review

## Correctness — PASS
The monotone self-consistency equations \(x=Q(a(2x-1))\) and \(y=Q(2a(2y-1))\) follow from individual choices and welfare marginal cost, respectively. Uniform-marginal event inclusions bound each root strictly inside its stated interval. A rotation copula puts its difference support on exactly two values; circular-noise smoothing and mixing exactly realize every intermediate root without losing uniform marginals, smoothness, or positive density. For any fixed copula, strict decrease of \(Q\) proves the planner share lies closer to \(1/2\). These constitute proofs rather than inference from finite simulations. The 721 numerical checks in \(\texttt{verify.py}\) are supplementary.

## Originality — PASS within inspected literature
Su–Mehr–Sastry (arXiv:2607.03625) already give a general given-joint-distribution equilibrium/optimality framework, and Bhattacharya–Makiranta (arXiv:2611.07787) give general pointwise uniqueness under relative congestion dominance. Makarov's classic fixed-marginal tail bounds and Zhang–Richardson's modern discussion (arXiv:2405.08806) are credited. The present theorem identifies all attainable **endogenous** equilibrium/planner shares with only marginals fixed and supplies exact positive-smooth realization plus planner ordering, which is not stated by the inspected references. Relevant indexed mathematical findings concern distinct noisy-resource models or fixed-marginal sum distributions; negative queries alone are not proof of novelty. The original Makarov full text was not inspected, and unindexed equivalent work remains a residual priority risk.

## Value — PASS
The complete partial-identification intervals quantify exactly what is unknowable about a congested market from two known marginal valuation distributions. Their widths shrink with congestion strength, and the planner's possible aggregate shares are always more tightly bounded around balanced allocation. Strong regularity of the joint valuation distribution does not remove the identification uncertainty. The result is a structural application, not simply a textbook pointwise equilibrium derivation.

## Limitations
Only two symmetric linear-congestion destinations, standard-uniform valuation marginals and strictly positive smooth joint densities are covered; the joint attainable set of the Nash/optimum pair is not classified. Endpoint values are not attained. No independent audit or empirical test has been performed.

Self-review: passed. Independent audit: not yet performed.
