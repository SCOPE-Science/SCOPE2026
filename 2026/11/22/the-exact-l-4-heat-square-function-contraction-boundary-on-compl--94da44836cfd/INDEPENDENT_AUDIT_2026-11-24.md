# Independent mathematical audit

## correctness

PASS

The frozen quantifier over any real or complex Hilbert space is false: for H={0}, e.g. K_{3,1} has the inequality for all inputs, and all part sizes have best nonnegative constant 0. The complete replacements in repairs/2 restrict to nonzero H and explicitly describe {0}; this closes the gap without changing any graph size or scalar result. Recheck: the Laplacian decomposes the centered input into two supported contrasts of eigenvalues n and m and the block-constant mode of eigenvalue m+n. Integration gives the normalized off-diagonal coefficient 4 lambda mu/(lambda+mu)^2, strictly in (0,1) for either contrast versus the block mode. On each part let X=||u_i||^2+||a||^2, beta_i=Re<u_i,a>. The pointwise fourth-power difference is 4(1-rho)X beta_i+4(1-rho^2)beta_i^2. The constant ||a||^2 contribution cancels in the sum; on parts of size two the opposite contrasts have equal norms so the remaining cubic term cancels, and on singleton parts there is no contrast. The squared terms give the exact equality characterization. The nonzero between-part mode along a unit vector proves sharpness even at K_{1,1}. On a size-at-least-three part the contrast (2,-1,-1,0,...) has both sum of cubes and sum of squares equal to 6. With block value -1/4 and opposite mean chosen to center the total, the deficit is -(3/2)(1-rho)(3-rho)<0, with no contrast on the other part. Relabeling and embedding along a unit vector handles all sizes and fields. Source code was inspected, not executed: the repaired verification notes distinguish exact rational witness/deficit arithmetic from complex floating-point samples and do not claim the checker independently verifies the integral. The original record, scripts and historical audit are unmodified.

## originality

PASS

For the repaired nonzero-data scope, credit the established L^2 benchmark, the small-graph cases, and the cycle/cubic overlap; do not credit the abstract two-frequency obstruction or the C4 example as distinct. The supported distinct claim is the uniform biclique fourth-power deficit, giving the whole Hilbert-valued boundary with the full equality characterization and a quantitative explicit negative deficit. Available evidence does not establish that this package is covered; historical priority is not certified.

## value

PASS

The nonzero-space repair preserves a natural sharp threshold over the entire complete-bipartite family, rather than an isolated numerical application. The exact two-part deficit identifies the cancellation and orthogonality governing equality, and its strict quantified witness works at every larger size. These finer statements remain useful even where bare contractivity or failure is supplied by related general or small-order results. No amplified optimum or general-graph classification is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
