# Self-review

## Correctness (PASS)

The precise assertion is the existence of a unique **height threshold** distinguishing global side-on and oblique projected-perimeter minimizers of a single-apex circular cone, **without** claiming uniqueness of every oblique optimum. The convex support of a projected disk and a point gives an exact piecewise complete/incomplete elliptic-integral expression. For each fixed positive viewing cosine, the perimeter difference relative to side-on decreases strictly in the cone height and crosses zero exactly once. An explicit derivative comparison proves strict side-on optimality for heights up to the radius. The complete-elliptic boundary expansion gives a strictly positive \(c^2\log(1/c)\) local penalty for every fixed height; compactness shows the minimax threshold is attained away from side-on, and elementary endpoint comparisons place it strictly below the axial tie height. These steps prove an abrupt rather than continuous optimizer switch.

The standalone checker independently forms the convex hull of projected rim vertices and the apex, compares the geometric perimeter with the elliptic formula, checks derivative identities and numerical examples, and passed 738 diagnostics. The numerical root \(h_*\approx1.6014993045\) is explicitly *not* an interval-certified theorem. The exact threshold is the stated minimax of unique crossings; no universal finite mesh is used as proof.

## Originality (PASS, best knowledge with residual priority risk)

The 2001 paper by Vickers and Brown studies random projected area/perimeter of convex solids, but its relevant right-cone formula and appendix concern **projected area** and not the strict global shadow-**perimeter** minimizer transition. Finch's arXiv:1212.5946v1 (2012-12-24) discusses **three-dimensional surface area and mean width**, not optimization of projected planar perimeter by a viewing latitude. The published published-finding corpus bicone shadow-perimeter result `0f13e384bdf1` concerns a *two-apex symmetric bicone* and a **continuous** direction bifurcation. The same-cone published published-finding corpus result `19c34891a8b8` concerns the **maximal projected area**, not its minimum planar perimeter. The statements, support functions, and extremized functionals differ, so none of the inspected claims implies this one. Exact-or-alias and broader-coverage searches found no decisive domination. An equivalent obscure historical result cannot be excluded by database search alone.

## Mathematical value (PASS)

Minimum silhouette boundary length is a natural geometric invariant for a canonical body of revolution. The single-apex cone displays a sharp first-order optimizer transition while the side-on direction remains strictly locally stable at *every* height, unlike its nearby symmetric-bicone analogue. The logarithmic local penalty explains why the change cannot arise by an infinitesimal tilt. This distinction is geometric, structural and not merely a substitution into an existing perimeter formula.

## Scope and outstanding limits

Only solid right circular single-apex cones, orthographic planar perimeters, and Euclidean normal directions are covered. The exact minimax theorem does not establish the number of all oblique stationary or minimizing latitudes; its decimal threshold has no independent interval certificate. Relevant historical sources outside the directly examined portions may contain older equivalent statements. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
