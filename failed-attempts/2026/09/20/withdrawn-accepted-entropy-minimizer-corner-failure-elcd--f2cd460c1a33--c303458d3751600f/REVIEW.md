# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. The source definition of the mathematical entropy and the Section 3 rectangle/corner construction were checked directly in arXiv:2609.19838v1. Differentiation gives strict convexity, strict monotonic decrease in pressure, and a unique unconstrained density minimizer e^{-1}p^{1/gamma}; projection onto the density interval proves the exact rectangle formula. The entropy-gap identity follows by substituting log p = gamma(log rho_0 + 1). Adding c rho shifts the stationary logarithmic density by -(gamma-1)c/gamma while preserving the entropy Hessian. A standalone numerical artifact checks the closed form against dense one-dimensional searches and reproduces the Configuration 3 example.

The result deliberately distinguishes two statements. Algorithm 1 does exactly minimize over its four listed corner candidates, so the implemented rule is not claimed to be internally inconsistent. The incorrect statement is the paper's identification of that corner search with minimization over the entire rectangle. The normalization obstruction applies to the implemented corner rule itself.

## Originality

PASS, to the best of our knowledge, with a narrow claim. Convex functions having interior minima, affine freedom of entropy pairs, and relative entropy/Bregman cancellation of affine terms are standard and are not claimed as new. The new claim is source-specific: arXiv:2609.19838v1 states that convexity reduces its continuous rectangle minimization to four corners, while the exact minimizer has the closed form reported here; the same new ELCD selector also depends on affine entropy normalization. Searches for the paper title/identifier together with terms such as corner minimizer, entropy normalization, affine shift, and rectangle minimization found the preprint and mirrors but no independent correction or equivalent analysis. Existing SCOPE records were searched by the source title and synonymous mathematical terms, with no overlap found.

No inaccessible paper was identified as a close source likely to overturn the source-specific correction. The principal historical-risk literature is the broad entropy-stable and relative-entropy literature, which certainly contains the underlying affine-invariance facts but is not known to analyze this 2026 ELCD selection rule.

## Value

PASS. The finding corrects the mathematical interpretation of a newly proposed numerical interface-state rule and supplies an O(1) exact minimizer. The issue occurs on a state pair present in one of the paper's own benchmark problems. The affine-normalization result is stronger than the corner error: it shows that raw entropy value is not an intrinsic selection criterion for a conservation law unless a normalization is made part of the method. This gives a concrete design requirement for future entropy-based characteristic decompositions.

## Limitations

The analysis does not show that replacing the corner selector by the continuous minimizer improves shock resolution, stability, or convergence. It does not invalidate the paper's reported computations. A normalization-invariant criterion based on relative entropy is suggested only as a structural repair direction; no performance theorem is claimed.
