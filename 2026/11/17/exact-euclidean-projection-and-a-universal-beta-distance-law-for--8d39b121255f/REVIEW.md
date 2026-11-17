# Scientific review

## Correctness — PASS

For any two distinct circuit-hyperplanes \(H,J\), the sparse-paving intersection bound gives \(x(H)+x(J)\le2k-2\), so at most one constraint is violated. Projecting orthogonally onto the unique violated affine halfspace subtracts \(t/k\) on \(H\) and adds \(t/(n-k)\) outside; coordinate bounds, the outside mass of one, and \(|H\cap J|\le k-2\) prove this point belongs to **all** constraints defining the base polytope. Its squared Euclidean distance is exactly \(nt^2/[k(n-k)]\). Equality at distance \(\delta_{n,k}\) forces an omitted indicator vertex. The excised cap is a pyramid with explicit base, and its smaller distance superlevel sets are homothetic of ratio \(1-u\); dividing by known hypersimplex volume gives the exact beta law. Rational tests in 69 parameter/missing-basis families (2,220 sample points) and 180 independent numerical optimizations corroborated the proof. The small disconnected rank-two case is explicitly included.

## Originality — PASS (historical priority provisional)

Ferroni (arXiv:2105.04465), Hanely et al. (arXiv:2201.12442), Ferroni–Schröter (arXiv:2208.04893; arXiv:2310.05487), and the published exact Euclidean surface-area classification explain the circuit-hyperplane clip geometry, face enumerations, lattice-point/volume formulas, and surface measures. Their inspected material does not assert the all-point orthogonal projection onto a multi-clipped sparse-paving base polytope, its sharp Hausdorff extremizers, or the exact *conditional Euclidean distance* law. Database comparisons also distinguished the universal beta law for nearest-vertex margins in regular polytopes, which concerns a different random variable and geometry. Generic projection algorithms and older cap geometry are the principal residual priority risks; the absence of a search hit does not prove novelty.

## Mathematical value — PASS

Exact distance to a matroid feasibility region is a natural stability and approximation invariant; the formula completely solves it over an entire hypersimplex for every sparse-paving rank and nonbasis system. The theorem yields a unique violated-cut metric projection algorithm, sharp worst-case gap and complete set of worst cases, and a universal distance distribution under ambient intrinsic-volume sampling that depends on the matroid through only one atom weight. The conditional beta law survives arbitrary intersection patterns and even disconnected low-rank examples. The prior corner-volume formula alone is insufficient to identify the nearest-point map without the global orthogonal-feasibility proof.

## Limits and nearest prior work

No result is claimed for points outside the hypersimplex, nonsparse-paving matroids, or weighted/non-Euclidean norms. The known cap decomposition, Eulerian normalization and prior volume work are expressly credited. Independent mathematical examination is still needed to settle historical priority and to independently validate the analytic proof.

Self-review: passed. Independent audit: not yet performed.
