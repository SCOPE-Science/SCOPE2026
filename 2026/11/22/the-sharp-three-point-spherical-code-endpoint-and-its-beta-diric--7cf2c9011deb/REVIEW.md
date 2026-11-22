# Review of the spherical-code endpoint result

## Correctness — PASS

The upper separation bound follows from \(\|U_1+U_2+U_3\|^2\ge0\); its equality cases are exactly planar regular triples. The exact Gram density has the correct three-point Jacobian and gamma normalization, and the change to scaled slack variables is invertible on the event. The cap-lens calculation independently computes the total small-probability mass, including the tangency exponent in codimension \(d-2\). The potentially singular \(d=3\) case is normalized by that independent mass calculation and Scheffé's lemma rather than by unjustified uniform convergence. The limiting beta and Dirichlet laws follow by an explicit simplex Jacobian. The independent two-dimensional beta quadrature is a finite sanity check, not the proof. All conclusions are for fixed integer \(d\ge3\).

## Originality — PASS, with residual priority risk

The first publicly posted archival source (Brauchart et al., 2015) treats many-point separation and covering; its relevant separation section concerns \(N\to\infty\), not a fixed three-point, near-optimal hard-cap partition function. Rankin gives the optimal deterministic separation but no neighborhood measure. Moran gives general bounds on the minimum angle, Cai–Fan–Jiang many-point extreme-angle limits, and Jenssen–Joos–Perkins hard-cap abundance estimates outside the present near-120-degree fixed-three critical window. A direct comparison of the events and parameter limits does not yield the gamma coefficient or conditional Beta–Dirichlet distribution. Nearby published research results on three-vertex spherical *perimeter*, intrinsic *angles*, latitude-circle triangles, and four-cap *coverage* also do not imply this claim. Exact statement and implication checks were performed; absence in an index is not proof of global uniqueness. Some historical papers and derivative theorems cannot be exhaustively ruled out.

## Value — PASS

The three-point spherical code is the smallest nontrivial hard-cap packing configuration with a rigidity threshold: all three pair distances must become simultaneously critical and the Gram determinant degenerates at a planar equilateral triple. The exact probability exponent \( (d+2)/2\), its full gamma coefficient, and the marked Beta–Dirichlet law quantify the near-optimal volume of this natural configuration space, in contrast with the familiar many-point, small-separation regime. The decomposition identifies how three independent pair slacks share the rare residual Gram rank defect. This is a substantive boundary-law result, not the elementary optimization inequality alone.

## Sources, reproducibility and limits

The primary sources compared include Rankin (1955), Moran (1979), Cai–Fan–Jiang (2013), Brauchart et al. (first posted 2015), and Jenssen–Joos–Perkins (2018). Some accessible texts were rehosts or html versions; an unlocated older treatment of exactly three random sphere points and a cap-packing endpoint remains a possible priority risk. The packaged `verify.py` passed its independent finite numeric tests in dimensions 3 through 5 and gamma normalization tests through dimension 9. No dimension-uniform estimate or nonuniform-sampling theorem is claimed.

Self-review: passed. Independent audit: not yet performed.
