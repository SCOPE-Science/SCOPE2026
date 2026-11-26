# Independent mathematical audit

## correctness

PASS

Hoehner's equality characterization is unique up to orthogonal transformations and gives exactly the coordinate set after division by sqrt(2+phi). I independently enumerated the exact support planes that can become facets after at most two deletions. Every facet contains a triple and a facet plane can have at most two original vertices on its outside, so this enumeration is exhaustive. For surviving polygons the directed boundary edges were determined by exact sidedness before taking oriented determinant sums. The 212 candidate planes give base volume 20u^2, the asserted losses for all 32 singleton deletions, and exact agreement with the geometric predicates and algebraic formulas for all 496 unordered pairs. The strict increasing order is 2d_D-eta, 2d_I, d_I+d_D-delta, d_I+d_D, 2d_D with counts 30,66,60,180,160; 0<delta<eta also checks exactly. The replay uses integer arithmetic in the basis (1,phi,3u,3phi*u) and no candidate hull library or symmetry reduction. Some deletion facets are polygons rather than triangles (306 of 496 hulls have at least one), so the source code's comment about exactly three contacts must not be used as a premise; the independent replay triangulates the actual polygonal facets.

## originality

PASS

The established optimizer and its undeleted volume are not new. The supported distinct result is the exhaustive two-erasure convex-hull volume spectrum, including its nonadditive interaction deductions and sharp pair classifications. The closest catalogue record uses exactly the same erasures but a different invariant; the known global volume theorem supplies the original body, not the volumes of its punctured hulls.

## value

PASS

Worst and best failures are a natural robustness invariant for this canonical optimizer. Classifying all pairs resolves which two point failures interact and by how much; in particular, adjoining the two face-normal erasures gives the smallest loss, whereas nonadjacent ones give the largest. The exact split gives substantially more than a numerical loss or a bound on the original optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
