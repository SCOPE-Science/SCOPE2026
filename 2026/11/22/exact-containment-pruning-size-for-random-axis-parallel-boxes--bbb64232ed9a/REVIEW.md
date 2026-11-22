# Scientific review — containment-minimal random boxes

## Correctness — PASS
The sampled side lengths are independent with density \(2(1-x)\). Given a box, another sampled box lies inside it with probability equal to the square of its volume, giving the exact binomial-sum expectation. The density of the product of side lengths has an explicit logarithmic singularity, obtained by a simplex convolution. Gaussian scaling and dominated convergence yield the dimension-dependent leading term, and the planar exact product density gives the stated second-order term. For any finite box family, a piercing set for all containment-minimal members pierces every other box, so the optimization equivalence is pointwise. The standard-library checker independently compared the planar product-density integral and finite exact sums and passed 255 assertions. Finite checks do not prove asymptotics.

## Originality — PASS (best-knowledge, historical risk retained)
Tran's full accessible 2010 work concerns the optimal hitting-set size in precisely this random-box model, not the number of containment-minimal sampled boxes. Chao–Hwang–Liang's readable 1996 manuscript/1998 paper concerns union volume and Mellin integrals, not the inclusion poset. Coffman–Lueker–Spencer–Winkler's abstract describes maximum-size disjoint box packings; their full manuscript could not be inspected, and an auxiliary priority risk remains. The previously recorded one-dimensional minimal-interval mean has \(\sqrt n\)-order growth but does not imply the sharp higher-dimensional logarithmic exponent, constant, or planar correction. Targeted literature searches and published-finding corpus similarity searches did not reveal a stronger implication or identical table; absence of hits does not establish uniqueness.

## Value — PASS
Removing boxes that contain smaller ones is a natural exact, lossless preprocessing operation for piercing/hitting-set instances. The theorem quantifies the expected number of constraints remaining after this operation in the standard random-box model, including a sharp leading constant in every fixed dimension and a two-term planar expansion. The new logarithmic factor characterizes how diverse box aspect ratios change containment pruning as dimension increases; the result does not purport to improve Tran's optimal piercing bounds.

## Limitations and closest literature
The statement concerns expectation only, fixed dimension, and independent uniform-coordinate endpoints. There is no concentration bound or claim about the distribution of surviving boxes. Classical extreme-point literature, older rectangle-containment algorithm papers, and the uninspected full Coffman text remain potential priority risks. The closest documented comparison is the one-dimensional minimal-interval expectation, not a two-dimensional or all-dimensional box theorem. No independent verification has been performed.

Self-review: passed. Independent audit: not yet performed.
