# Independent mathematical audit

## correctness

PASS

Deleting s vertices leaves 15−3s+e_P(S) edges, ruling out s≤2 and forcing pairwise intersecting auxiliary edges at s=3. Three intersecting edges are a star or a triangle. The star deletion leaves a tree; the triangle deletion leaves a six-cycle. A four-set with no three-star is a P₅, a C₄ plus an isolate, or K₃ plus K₂: only C₄ works, leaving a double-star. Hence each center supplies a connected budget-four component formed by four minima, their common full star, and 24 one-edge extensions using off-center edges; the 15 squares are isolated. The 20 minima each have seven feasible one-edge extensions. At size five the only no-star sets are the 12 auxiliary five-cycles, all infeasible, giving 240 new states and 840 new edges. At budget five overlaps connect centers, and squares attach via size-five supersets. The only minimum-pair case whose union does not fit the budget is disjoint stars. At least one star omits the edge between centers, and their noncenter neighbor sets share two labels. Adding the two corresponding target spokes and deleting the extra initial spoke reaches a valid square; adding the last target spoke then permits the last two removals. This realizes the six-toggle lower bound. Same-center pairs and distinct-center pairs sharing an edge use their unions. Counting gives 30/90/70 pairs at 2/4/6. A separately written full enumeration confirmed these facts and established 20/140/240 states at eccentricities 8/9/10 respectively, hence radius 8 and diameter 10, attained by 120 unordered pairs.

## originality

PASS

The cardinality-three classification, fixed-size exchange graph, state counts and bare budget-five connectivity are not the distinct contribution. The inspected earlier records supply the first three, and the reported general subcubic theorem would imply the fourth. What survives is the exact budget-four component and obstruction structure, the no-detour distance formula for all optimum pairs at the minimum connecting budget, and the all-state eccentricity and diameter-pair profile. No verified prior result subsumes these claims.

## value

PASS

Petersen is a canonical cubic obstruction graph here, not an arbitrary small input. The floor-budget components explain exactly how optimal exchange classes are trapped and identify further trapped feasible states. At the next budget those same square states enable symmetric-difference geodesics even for disjoint optima, whose full union does not fit. The eccentricity trichotomy is an exact benchmark for the natural entire feasible-state metric, not implied by connectivity or by its optimum subgraph. These structural facts and exact distances are useful for comparing minimum-extra-budget and no-detour reconfiguration questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
