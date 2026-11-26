# Independent mathematical audit

## correctness

PASS

Reconstructed the face classification in the dual of the full grid: absent primal edges identify neighboring cells (including the exterior), and the cells incident to each vacant site form one such class. A vacancy on the outer boundary can only contribute to the exterior. In a bounded nonsingleton class the generating vacancies must therefore be interior middle-row sites; their stars share a cell exactly for consecutive columns. A maximal run bounded at both ends, with its top and bottom and both middle-row endpoints occupied, produces exactly one two-row rectangle of span d. The remaining bounded cells are occupied unit squares. Euler's formula and independence give the stated finite mean even for n=1,2. The corridor series is geometric with ratio at most 4/27; its derivative series is uniformly summable by bounding the terms and their derivatives using that ratio. The variance is O(n) by the component change bound of 3 per vertex, giving L² convergence. The Bernoulli score identity gives the normalized covariance limit. Independently differentiated the rational density, verified the polynomial's strictly positive derivative using the split at 8/25, and confirmed the root 0.3286185980908836... and cubic coefficient 11. A bounded dual-cell check matched actual face cell sets for all 37,448 masks through n=5; the same reviewer-written program checks the derivative symbolically. The uploaded checker was read, not run; its indicated derivative test at lines 107–110 is algebraically tautological, and is not relied on.

## originality

PASS

Best of current knowledge, the span-resolved bounded-face law and the resulting exact finite mean and unique limiting-density peak are distinct. Closest published comparisons change the occupation model, the observable, or the graph family. Euler's identity, concentration, and the product-measure score identity are standard ingredients, not originality claims.

## value

PASS

Three rows are the first open width with a separate interior row capable of supporting nonunit vacancy corridors. The exact face spectrum explains the infinite geometric correction, yields component expectation for every strip length, and locates the occupation level separating the two signs of the limiting occupancy–component response. These are usable benchmarks beyond an isolated numerical optimum; no planar critical-threshold or wider-strip claim is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
