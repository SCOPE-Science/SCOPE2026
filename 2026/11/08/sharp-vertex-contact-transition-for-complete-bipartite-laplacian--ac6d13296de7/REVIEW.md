# Self-review

## Correctness — PASS
The graph Laplacian has rank \(N-1\); class-permutation invariance and the strict convexity of the squared minimax objective force a one-parameter center. Direct substitution gives two vertex-distance quadratics with a single crossing. Their derivative signs yield the claimed piecewise optimizer; algebra gives both squared-radius formulas and the exact clearance. An independent convex-combination certificate of contact vertices confirms global optimality. The standalone checker rebuilt 138 instances from the original Laplacian vertices, with 77 strict screening cases; its numerical optimization is corroboration, not proof.

## Originality — PASS, provisional historical priority
The original 2017 Laplacian-simplex paper develops lattice and Ehrhart questions, not Euclidean minimum enclosing spheres. The 2018 continuation concentrates on code and lattice properties. The closest mathematical research record gives the all-vertex circumsphere only for vertex-transitive graphs; it implies the balanced \(K_{p,p}\) special case but cannot imply the unbalanced class-screening formula. A second record concerns inradii of trees, a different metric and graph family. General minimum-ball convex-combination criteria do not provide the explicit graph-dependent threshold. Searches covered the object name, graph family, vertex-orbit contact sets, equivalent minimum-enclosing-ball terminology, and pseudoinverse/spectral approaches. Further terminology-based prior art remains a residual risk.

## Value — PASS
The result is a complete minimum-enclosing-ball classification across a natural infinite two-parameter family, including a discontinuous change in the number of contacting vertices despite every member having simplex face structure. The exact adjacent transition \(K_{3,13}\) to \(K_{3,14}\) screens fourteen vertices at once, with explicit positive clearance. The result distinguishes the familiar equidistant vertex circumsphere from a genuinely optimal enclosing sphere; the distinction is not captured by lattice invariants or known vertex-transitive cases.

## Limits
Only unweighted complete bipartite graphs in full-Laplacian Euclidean coordinates are treated. No statement of independent validation is made.

Self-review: passed. Independent audit: not yet performed.
