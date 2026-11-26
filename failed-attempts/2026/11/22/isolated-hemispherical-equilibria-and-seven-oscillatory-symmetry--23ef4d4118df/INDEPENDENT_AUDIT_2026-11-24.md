# Independent mathematical audit

## correctness

PASS

Independently recomputed the whole phase portrait with /workspace/branches/audit_replays/icosahedron.py (run with Python 3). Constructed the standard vertices from cyclic permutations of (0,±1,±φ) and joined pairs at squared distance 4 using exact Z[φ] arithmetic; checked an explicit isomorphism to the frozen ring-labelled graph. Computed the ±1 spin update for every state, peeled the transient vertices of the functional digraph by indegree, and traced the residual cycles, without assuming period ≤2 or any entrance-time bound. This produced the exact 14 fixed states, 156 temporal two-cycles, all basin sizes and the full joint first-entry/period table. The fixed-support set consists of exactly the twelve distinct caps and the two constant states. The cap basins all have size 1; both consensus basins have size 1586. Sharpness follows both from the 240 states of entry time five and from the relabelled trajectory 87→47→23→41→16→0. Every graph automorphism maps an ordered triangle to one of 20×6 possibilities, and the tested distinct triples of distances to the three seed vertices determine every image; all 120 induced maps preserve adjacency. Quotienting unordered temporal cycles by these maps, without an added opinion-complement quotient, reproduced the exact multiset of class sizes and basin attributes; the repeated pairs are not unique class identifiers. The source Python/C++ and captured output agree on the aspects they check; neither frozen script was executed. The result is exact for this graph, not a general polyhedral theorem.

## originality

FAIL

Verified earlier equivalent coverage in the distinct published November 17 record 4b6d7cb731ad. Its Finding gives the same graph, labeling, majority rule, fixed supports, singleton cap basins, consensus basins, temporal census, basin distribution, automorphism quotient sizes, sharp time and probabilities. Re-aggregation of its published 82-row state_orbits.csv yields exactly the ostensibly more detailed first-entry-by-period table and class-by-basin multiset in the frozen November 22 result. This is not a matching title, identical-record self-hit or inference from a same-day date. The earlier record also has a symbolic proof of cap isolation and additional population-weight counts.

## value

FAIL

The natural invariant is worth knowing: cap stability differs from basin accessibility, and an exact labeled phase portrait is useful for graph-specific comparison. But the submitted contribution is a recomputation of the existing same-model census and mechanically readable orbit attributes, rather than a new useful fact. The alternate checker gives useful corroboration without constituting a surviving distinct mathematical finding. A sample sharpness trajectory and reformatted tables do not provide a worthwhile repairable remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
