# Mathematical review

## Correctness — PASS

The domain is all integers \(a,q\ge1\), \(b\ge a+2\), \(n\ge2\). Each of the \(n+1\) contributions with a fixed number of right-block choices is a complete integer interval with strictly increasing endpoints. Their consecutive gap lengths exactly equal \(b-1-na+k(a-q)\), establishing the cardinality formula without asymptotic assumptions. Reflection reduces the proof to \(a\ge q\). Before the first overlap the disjoint-interval formula is exact and positive for indices at least three; after the first overlap the reversed-gap sum is convex, so the Buchweitz difference is concave. The boundary estimate is strictly positive whenever there is a nonempty pre-overlap positive region. This excludes disconnected positive support globally. Boundary \(n=2\), equal block lengths, and first-overlap index \(2\) were independently considered. A standalone checker recomputes 5940 direct exact instances, 11520 interval-support parameter cases and 4940 boundary instances; the infinite result rests on the written proof, not those samples.

## Originality — PASS within inspected literature

Eliahou, García-García, Marín-Aragón and Vigneron-Tenorio (arXiv:2011.09187, first published 2020-11-18; journal DOI:10.1007/s00574-022-00322-8) explicitly ask in Question 4.1 about interval shape for arbitrary finite sets and gapsets. The inspected primary article gives constructions for three-block and other more complicated sets and uses general eventual sumset theory, but does not establish the universal two-block interval-shape theorem or the exact two-block adjacent-gap formula as a theorem. Its results neither imply the all-index connected positive support for this infinite parameter family nor rule out a disconnected two-block support. published-finding corpus searches for Buchweitz, two integer blocks, adjacent interval gaps, and equivalent cardinality phrasing returned no direct or dominating result; closest semigroup and sumset entries address other invariants and objects. Direct web searches for “Buchweitz set” plus two intervals, union of intervals and support connectivity likewise gave no equivalent primary result. The original open question itself is not resolved in full, and absence of an indexed hit does not certify novelty.

## Mathematical value — PASS

Question 4.1 in the motivating study directly asks for the *shape* of the positive support, not merely a large-index asymptotic. A union of two positive-length integer blocks is the first structurally natural family beyond a single interval; in that family the theorem gives a complete affirmative answer, handles every gap size and pair of block lengths, and gives an exact formula at each index. The concavity-after-first-overlap mechanism and boundary positivity are structural information not supplied by general eventual sumset asymptotics. No assertion of a general solution or of optimal extensions is made.

## Closest literature and limitations

The source is S. Eliahou, J. I. García-García, D. Marín-Aragón and A. Vigneron-Tenorio, *The Buchweitz Set of a Numerical Semigroup*, arXiv:2011.09187, journal DOI:10.1007/s00574-022-00322-8 (especially Sections 2–4 and Question 4.1). General finite-sumset stabilization results cited there are asymptotic and cannot by themselves determine the intermediate positivity pattern. The present proof does not address arbitrary gapsets, singleton blocks, general finite sets, or the separate unimodality question (Question 4.2). Unindexed equivalent two-block additive results remain the material originality risk. Finite checks do not certify infinite claims.

Self-review: passed. Independent audit: not yet performed.
