# Self-review

## Correctness — PASS
The harmonic extension on each unobserved arc is uniquely linear by the unit-edge Euler–Lagrange equations. Its \(2	imes2\) Gram contribution has coefficients \(s_t\) and \(c_t\), verified by finite power sums. The antisymmetric eigenvalue \(t(t-1)/(6(t+1))\) is strictly convex, making the full Gram matrix Loewner-convex in each gap. A strict transfer argument, using triangle-edge permutation symmetry and the fact that a constant top eigenvector requires all gaps equal, excludes every unbalanced integer triple. Direct reflection reduction computes the two radical branches. The included executable verifies exact sums, all 12,341 ordered gap spectra through cycle length 43, and selected Parseval identities, but the proof is analytic for every \(N\ge3\). The comparison of the two-edge strictness at zero missing vertices is included in the proof.

## Originality — PASS relative to inspected sources
The motivating graph-frame paper establishes host Parseval analysis and harmonic Dirichlet completion but does not choose an optimally stable three-anchor set. The full published results for a contiguous path in a cycle give a fixed-set frame spectrum but do not optimize global anchor placement. The three-column Fourier Vandermonde Riesz theorem optimizes a different Gram matrix over frequencies and does not imply the harmonic-extension operator norm. Searches included exact harmonic anchor placement, three-node cyclic harmonic interpolation, periodic spline mesh balance, aliases and Riesz/frame equivalences. The distinction is the strict matrix-convex balancing and the exact optimal coefficient-energy value. An older equivalent result in periodic linear-spline or optimal knot-placement theory cannot be ruled out absolutely; no independent literature certification is claimed.

## Mathematical value — PASS
Three anchors are the first cyclic design with a nontrivial choice of three complementary arc lengths. The complete classification of all optimal placements, finite-grid radical and strict \(1/(3N)\) arithmetic penalty quantify the energy inflation introduced by harmonic lifting before a Parseval cyclic Fourier analysis. This is an objective relevant to stable, energy-controlled graph wavelet measurements; it is neither just a numerical instance nor a mere rephrasing of Parseval tightness. It does not solve multi-anchor or weighted designs.

## Scientific and bibliographic limitations
No independent external audit has been performed. The proof concerns the operator's largest squared singular value, not its entire spectrum for all placements, nor the lower bound or condition ratio. The bibliographic comparison is bounded by the genuinely inspected primary manuscripts and indexed records.

Self-review: passed. Independent audit: not yet performed.
