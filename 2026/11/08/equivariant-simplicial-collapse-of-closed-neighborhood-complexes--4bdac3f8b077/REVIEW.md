# Scientific review of the closed-neighborhood collapse theorem

## Correctness — PASS

For a finite graph with no four-cycle as a subgraph, any nonadjacent pair has at most one common neighbor. This establishes a *unique center* for every simplex lying outside the clique complex. The stated center-pairing partitions the relative face set and, when ordered by decreasing lower-face size, is a sequence of actual elementary free-face collapses. Graph automorphisms preserve both the center and all cardinality stages. Since the graph is four-cycle-free, its graph triangles are pairwise edge-disjoint, so the clique complex collapses to a graph by removing one free triangle edge at a time. The integral homology module is the ordinary graph cycle lattice modulo a primitive, signed triangle-boundary sublattice. The four-cycle example correctly demonstrates failure outside the hypothesis. `verify.py` exhaustively replays this construction for all 8,597 qualifying labeled graphs with at most six vertices, and checks complete automorphism groups of three representative examples. Finite checks corroborate but do not replace the all-graph proof.

## Originality — PASS, with residual risk

The closest primary source is Matsushita, *Closed neighborhood complexes of graphs* (arXiv:2511.12608, November 16, 2025). Its theorems concern suspension relations to independence complexes, combinatorial Alexander duality, and fundamental groups. Inspection of the mathematical statements and relevant proof sections found no collapse onto the clique complex under a no-four-cycle condition, nor the integral signed-triangle module. Borgwardt and collaborators, *Reconstruction of C4-free graphs from the set of closed neighborhoods and digital convexity* (arXiv:2510.21195, October 24, 2025), establishes graph reconstruction, not homotopy. Relevant published graph-Cech and *open* neighborhood-complex results concern distinct complexes, metrics or product families and do not imply the present statement. Indexed-equivalence searches returned no covering theorem, but absence of an indexed result is not proof that no equivalent published or unindexed proof exists. This residual originality risk remains.

## Mathematical value — PASS

The theorem classifies a natural infinite family of graph-defined Cech/closed-neighborhood simplicial complexes in *simple-homotopy* and in integral symmetry representation terms, not just by Betti numbers. The explicit collapse explains why complexes of potentially high dimension have only graph-like topology; the triangle-relation module distinguishes automorphism actions even when circle ranks coincide. The four-cycle creates a higher-dimensional sphere, providing a natural sharp boundary for a uniform graph-recovery result. The scope is mathematically motivated by the recently developed closed-neighborhood construction, rather than an arbitrary finite parameter choice.

## Limitations and closest comparisons

The four-cycle prohibition is stronger than forbidding *induced* four-cycles. The claim is not a classification for all finite graphs, and the final collapse to a graph after triangle removal is not asserted to be equivariant. The abstract-level available summaries of some related published graph-Cech calculations cannot support a full-text exclusion of all possible equivalent treatments. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
