# Scientific review

## Correctness — PASS

The claimed convergence is conditional only on a cited, genuinely proved input: the first-order Gaussian free-field maximum for the same uniform recursive tree (Angel–Goldschmidt–Michaeli, 2026, Corollary 13). The additional steps are independently reconstructed. Recursion on newly attached vertices yields the exact annealed depth-profile product. Gaussian exponential tilting gives an exact marked many-to-one identity whose size-biased depth is a sum of independent Bernoulli variables, while each tilted ancestral edge has law \(N(1,1)\). Chernoff, Hoeffding and Gaussian martingale inequalities yield exponential concentration for depth, empirical bounded tests, energy and the whole partial-sum profile. Counting a near-maximal bad path with weight \(e^{\eta}\) costs only \(n^\varepsilon\); choosing the level deficit smaller than the large-deviation exponent rules out all such paths. The cited maximum lower bound then transfers all properties to the actual maximizer. Finite checker: 105 exact identities passed. There is no claim that finite checks establish asymptotic assertions.

## Originality — PASS against examined evidence

The paper motivating this result proves the peak height and heuristically indicates its depth; it does not state or prove the empirical ancestral-increment law and simultaneous full path-shape limit. The exponential-spine change of measure and normal tilt are classical and are credited, not claimed as independently new. The accessible full text of Mallein's 2016 fixed-generation branching-random-walk work was inspected for possible genealogical implication; its close-relative and Brownian-excursion results do not directly cover the random-depth, fixed-population uniform recursive tree. Jagannath's binary-tree Gibbs-overlap findings address a different statistic. Searches found no matching indexed claim. These facts are not a proof of global novelty: an as-yet-unidentified general spine-localization theorem might imply this special case.

## Value — PASS

The motivating maximum theorem alone gives no macroscopic distribution of the increments that build the maximizing path. The new theorem identifies this distribution, determines a nonzero fraction of locally negative steps along an extremal path, establishes the natural quadratic-energy limit and resolves the suggested localization at depth \(\sqrt e\log n\) with a whole-path shape. These are natural structural observables for rare Gaussian peaks in random geometries, not a selected unmotivated finite computation or a restatement of maximum height.

## Closest literature and limitations

Angel–Goldschmidt–Michaeli (2026, arXiv:2611.18353) supplies the exact extremal-height input. Mallein (2016, arXiv:1605.08292) supplies a closely related but fixed-generation genealogy viewpoint, and Jagannath (2015, arXiv:1509.07527) the binary-tree Gibbs-overlap viewpoint. Classical spine changes of measure precede this argument. The present result is annealed, lacks a second-order limit or quenched statement, and carries residual historical-priority risk from broader branching-random-walk theory.

Self-review: passed. Independent audit: not yet performed.
