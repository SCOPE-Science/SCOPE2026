# Independent mathematical audit

## correctness

PASS

For positive real a_i,ell with 2ell<=min a_i, the three open caps x_i-x_{i+1}>a_i-ell in the box are pairwise disjoint: each forces one coordinate > a_i-ell>=ell and the next <ell, preventing shared-coordinate overlaps in a 3-cycle. On each cap, coordinates u=a_i-x_i>=0,v=x_{i+1}>=0 obey u+v<=ell and x_{i+2}=z+u-v with z=t-a_i. Direct strip-triangle intersection yields a new difference-facet segment length sqrt(6)[g_ell(z)-g_ell(z-a_{i+2})]/2, loss sqrt(2) times the same clipped-ramp difference on its u=0 and v=0 box sides, and loss sqrt(2)[k_ell(z)+k_ell(z-a_{i+2})]/2 on two box end faces. With the reflected box-section profile P_B and a_i+a_{i+2}=N-a_{i+1}, summation gives exactly P_diff=sqrt(6)S/2 and P_coord=P_B-sqrt(2)S-sqrt(2)T/2. Identities g_ell(-z)=2ell-g_ell(z) and k_ell(-z)=k_ell(z) imply the two sums are unchanged under t -> N-t; continuity handles exceptional levels and singleton endpoints. Independently enumerated exact rational half-plane intersections and midpoint-active facet tags for 400 seeded admissible parameter/height cases, testing actual coordinate and difference edge-length totals against both profiles at t and N-t; all passed. Separately computed unequal hexagon edge-multisets at (6,4,5;2), t=5,10 and difference (sqrt6-sqrt2)/2 at (3,4,5;2), t=5,7. Rebuilt the canonical Git tree SHA from all seven pinned blob IDs and matched 022558b4... . Analytical proof, not those finite tests, establishes the continuum theorem.

## originality

PASS

The complete 2022 public chainlink preprint gives complementary integer-section Ehrhart equality (Theorem 1/4.8), full-body vertex/facet structure and a volume trace (Proposition 6.8), not the distinct inherited Euclidean coordinate-facet and difference-facet perimeter profiles. The prior October 18 geometric records establish a single (4,5,6;2) equal-perimeter example and a parametric complementary-diameter gap, respectively, but neither entails the present simultaneous two-facet-family all-real-level identities for arbitrary positive a_i and ell in the half-size regime. The present Resultary entry is a mirror of the assigned result, not independent prior coverage. Best-of-knowledge originality, not certified global priority.

## value

PASS

The central remarkable feature of chainlink polytopes is equality of complementary Ehrhart section data. Establishing metric Euclidean perimeter equality for all real heights and arbitrary real admissible chain lengths, and separating the coordinate- and difference-facet totals despite their different Euclidean tangent speeds, gives an independently meaningful structural boundary valuation theorem. The explicit piecewise-linear formulas, noncongruent hexagon witness and sharp out-of-half-size counterexample explain rather than merely tabulate the geometry. Its natural object/invariant and complete three-coordinate domain make this more than a routine metric rephrasing of lattice-volume symmetry or the earlier one-pair perimeter check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
