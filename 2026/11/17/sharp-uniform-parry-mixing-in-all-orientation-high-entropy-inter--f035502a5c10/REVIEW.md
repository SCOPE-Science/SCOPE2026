# Mathematical review

## Correctness (C): PASS
The published affine normal form and cubic characteristic polynomial are specified exactly. The proof checks strict primitivity using matrix support intersections, proves the Perron root range from row sums, and handles all three mutually exclusive terminal switch types. The complementary roots are bounded by a quadratic sum/product argument or by direct signed evaluations of the cubic at \(-1,0,1\). The Parry conjugacy and spectral-radius identity then deliver the claimed mixing rate. The final-plus-to-minus word supplies an exact, not numerical, asymptotic sharpness witness. The checker exhaustively tests the finite orientation sets from three through twelve branches, but these tests are not used to extrapolate the theorem.

## Originality (O): PASS (provisional priority)
Oliveira's relevant full text [1] explicitly provides the adjacency matrix and cubic spectral polynomial, but studies kneading, entropy, homology and periodic-orbit enumerations rather than the uniform subleading unit-disk bound and maximal-entropy mixing scale. Coles–Pavlov [2] gives general primitive-matrix mixing lower bounds with completely different quantitative specialization, and does not dominate the sharp all-orientation result. Targeted mathematical-record queries surfaced spectral results for optimally selected symmetric chains on other graph families, neither equivalent to nor stronger than this result for forced Parry chains. The previously recorded terminal-agreeing orientation-word calculation concerns the physical Lebesgue invariant measure and its switching indicator, not full Parry-chain mixing. No accessible comparison implied the claim; unindexed historical spectral matrix literature remains a priority risk.

## Mathematical value (V): PASS
The exact all-orientation family has exponentially many combinatorial configurations while maintaining high topological entropy. A sharp uniform \(1/n\) spectral-root mixing law for the *maximal-entropy* dynamics is a natural quantitative dynamical invariant not determined by the published entropy bounds; the sharp one-switch construction shows the order cannot be improved. This is a whole-family spectral result, not a fixed small-matrix computation or a renamed known estimate.

## Scientific limits
The source's cubic determinant and Markov realization are credited as premises; the new result is their nontrivial uniform spectral consequence and its optimality. Rate is asymptotic in time for fixed branch count and does not assert a finite-time total-variation bound. Outside literature, especially historical directed graph spectral bounds, may affect publication priority.

Self-review: passed. Independent audit: not yet performed.

## Sources
[1] Oliveira, arXiv:2611.03287v1, https://arxiv.org/html/2611.03287v1.
[2] Coles and Pavlov, arXiv:2611.10951v1, https://arxiv.org/html/2611.10951v1.
