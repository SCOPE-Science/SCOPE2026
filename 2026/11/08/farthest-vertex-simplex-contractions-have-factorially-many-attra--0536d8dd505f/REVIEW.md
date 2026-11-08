# Scientific review

## Correctness — PASS

The proof uses barycentric distance comparison to identify the minimum coordinate as the farthest vertex, reduces the labelled dynamics to a strictly contracting sorted-map quotient, calculates its unique geometric fixed vector and positive minimum gap, and establishes a single global finite lock-in time. After lock-in, rank order rotates one position each step. Periodic points are exactly the permutations of the geometric vector, yielding \((N-1)!\) primitive cycles of length \(N\), each with return derivative \(\lambda^N I\). An exact phase-matched contraction proves global convergence. Symmetry off a null family of tie hyperplanes proves equal basin volume. Independent rational-arithmetic code executed successfully with 15,580 supporting assertions; the general result is analytic.

## Originality — PASS within inspected evidence

The direct antecedent, Abdulaziz (arXiv:2407.02506v1), treats two-dimensional regular polygons, explicitly including the equilateral triangle. This provides the planar case but not the regular-simplex \(d\ge3\) theorem. Gaivão and Pires (arXiv:2405.08444v1) establish multi-dimensional generic periodicity under conditions, but do not imply the all-parameter exact cycle census, coordinates or physical basin laws. Also compared were indexed farthest-facet projection and static simplex distance results; they operate on different dynamical maps or non-dynamical invariants. Originality is assessed relative to the inspected statements, not inferred solely from lack of search matches.

## Mathematical value — PASS

The result gives a complete high-dimensional answer for a canonical geometric rule: factorially many attracting cycles, precisely determined geometric coordinates, all-parameter global finite time before periodic symbolic scheduling, and equal basin volumes. For a tetrahedron it predicts six distinct four-cycles, a behavior not obtained by extending planar polygon parity formulas. This is a structural classification, not a single numerical instance or a routine incremental bound.

## Scope, closest literature, and residual risks

For regular Euclidean simplices of dimension at least three only, with common contraction factor strictly between zero and one and specified tie breaking. The uniform transient estimate is not claimed optimal. The older planar farthest-vertex paper establishes the triangle case, while general multi-dimensional contraction theorems are largely generic. A pre-existing exact high-dimensional formula under another terminology cannot be ruled out by these searches. No independent mathematical verification has been performed.

Self-review: passed. Independent audit: not yet performed.
