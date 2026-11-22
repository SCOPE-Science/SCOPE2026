# Review of the cross-polytope intersection-body classification

## Correctness
**PASS.** The measure normalization is fixed by the coarea identity with independent standard Laplace coordinates: the central section volume equals \(2^n f_{\sum u_iX_i}(0)/(n-1)!\). Fourier inversion and partial fractions give the exact radial formula. The Vandermonde cancellation constructs the polynomial numerator; a nonzero residue along every denominator hyperplane rules out common factors. The resulting homogenized equation is linear in the homogenizing variable, so Gauss's lemma proves absolute irreducibility. Comparing homogeneous top-degree factor sets and parity of the next term distinguishes all signed orthants. The argument applies to all integers \(n\ge4\) and excludes coordinate-hyperplane artifacts. Independent convex-hull section computations and exact symbolic checks are supporting finite checks, not an infinite proof.

## Originality
**PASS, with residual priority uncertainty.** The 2021 work of Berlow, Brandenburg, Meroni and Shankar proves general semialgebraicity and a denominator-degree upper bound, and works out cube examples. The present theorem identifies a different, cross-polytopal family with exact irreducible degree \(\binom n2\) for *every* orthant; the noncancellation argument is essential to obtain equality in the prior upper bound. The 2024 translation/convexity paper does not state these exact degrees. The 2026 restricted-section preprint uses the same known Fourier integral, but studies extrema of selected hyperplane sections; it does not state the algebraic-boundary classification. The three-dimensional specialization is a known special calculation, and is not included in the new scope \(n\ge4\). Searches of related indexed findings revealed a section-face-spectrum result and earlier octahedral computations, not an all-dimensional degree classification. The possibility of equivalent unindexed classical work remains.

## Mathematical value
**PASS.** The sharp exact degrees and component count classify a canonical intersection-body family in all dimensions, turning a general possible-degree bound into an attained value and a complete list of irreducible components. The dimension-four consequence (16 sextic components) is concrete and verifiable. This gives structural information about an algebraic-geometric invariant of a natural convex body and is not merely a computation at an arbitrary parameter choice.

## Limits and relationship to closest work
The Laplace integral, semialgebraicity, and general component-degree bound are existing tools, not new discoveries. The classification applies to the origin-centered standard cross-polytope only. The real algebraic hypersurfaces may contain points beyond the convex body's Euclidean boundary. Independent validation has not been performed; unindexed equivalent computations cannot be ruled out by database search alone.

Self-review: passed. Independent audit: not yet performed.
