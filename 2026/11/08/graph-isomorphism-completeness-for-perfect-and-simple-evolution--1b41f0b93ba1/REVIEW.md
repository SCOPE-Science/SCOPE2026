# Independent mathematical audit

## correctness

PASS

The repaired claim is the simple-promise theorem in repairs/4/RESULT.md, with the upper bound for perfect inputs clearly identified as known. A perfect target has linearly independent basis squares, so multiplying distinct images shows disjoint column support and forces the isomorphism to be monomial. The exact coefficient equation is a_ij s_j = s_i^2 b_{σ(i),σ(j)}. The directed generator cycles encode exactly the index permutations and scalar shifts, including singleton cycles for q=2; the second relation encodes that equation, including zeros and loops. Incidence paths with oriented endpoint colors preserve loops and both arc relations, and distinct pendant-leaf counts at least two recover all vertex colors. The upper reduction applies to the simple subclass because E² is a nonzero ideal in a simple algebra. For the lower bound, the unique added hub recovers n and the original nonisolated induced subgraph, and the omitted isolate count is n minus its order. The block matrix has zero kernel over every field by eliminating its two blocks in order; the bidirectional arcs make it strongly connected, so multiplication by successive natural basis vectors propagates any nonzero ideal to all squares. Over any field monomiality preserves loops and hence the x-layer, whose off-diagonal arcs recover the connected input graph; forward isomorphisms preserve both layers. The dimension is 4n+6 for n>=1, and the separate one-dimensional simple algebra handles the empty graph. The inspected frozen checker and output provide only bounded corroboration, including 2565 upper comparisons and 75 lower cases; no scripts were executed.

## originality

PASS

The original perfect-promise contribution fails originality: a distinct earlier Resultary result already gives both fixed-field reductions (including the n(q−1)-vertex upper reduction), and Costoya et al. prove perfect-algebra hardness with an explicit isomorphism-reflecting construction over all fields. The repair claims as contribution only the faithful all-characteristic simple-algebra lower construction and the consequent complexity result on that stronger promise. This is distinct in the inspected comparisons: Costoya et al.'s vertex lines are already nonzero proper ideals when the dimension exceeds one. The upper reduction and known structural facts are credited and reused, not claimed as contributions.

## value

PASS

Hardness after imposing algebraic simplicity is a meaningful strengthening: direct regular-algebra encodings need not satisfy it. The linear-dimension, 0–1 construction keeps rigidity and graph recovery while supplying simplicity uniformly in the characteristic. This isolates which structural restriction does not lower the complexity, rather than restating the known perfect-case classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
