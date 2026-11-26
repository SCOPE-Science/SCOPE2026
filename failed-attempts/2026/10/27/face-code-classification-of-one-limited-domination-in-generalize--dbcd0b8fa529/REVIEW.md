# Independent mathematical audit

## correctness

PASS

With T the complement, any vertex having two neighbors in T is forced into T. Two occupied points fill a coordinate line, and three corners fill the fourth corner of a coordinate rectangle. Along paths in any component, a full line in an active direction propagates to the next vertex by the rectangle rule, or is already the same line when the path changes that direction. Hence the component frees every active coordinate and fixes every other coordinate. A distance-two connection between distinct components would give an intermediate vertex forced into T, so components are at distance at least three. Domination excludes the whole graph as a component. Conversely, a proper face has outside neighbors reached by changing a fixed coordinate; none belong to another face. An outside vertex can reach at most one vertex of any given face by a single change and cannot reach two separate faces. For the optimum, each T-vertex contributes at least q_*−1 boundary edges from its fixed coordinates and each D-vertex contributes at most one. A shortest-alphabet hyperplane attains |T|=N/q_*. Equality forces exactly one fixed coordinate of size q_* in each component, and every vertex outside one such hyperplane is already adjacent to that hyperplane, ruling out a second component. This proves the labelled count, including d=1 and ties of q_i. The recorded ten exhaustive subset profiles and five ILP profiles corroborate small cases; the verifier was inspected, not executed, and is not required by the proof.

## originality

FAIL

The central face-code structure is the closed-set decomposition for two-neighbor bootstrap percolation on Hamming graphs, with the full graph excluded. The earlier deterministic face-merging proof works coordinatewise with unequal clique sizes, and the extremum and its rigidity are immediate boundary consequences of that structure. No verbatim unequal-alphabet one-limited theorem is needed for this implication.

## value

FAIL

The underlying structural classification is natural and useful, but it is already furnished by the deterministic bootstrap-closure mechanism. The additional domination and unequal-alphabet conclusions amount to excluding the full product and applying a tight crossing-edge count to those same components. No separate unknown invariant or substantial obstruction survives this translation in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
