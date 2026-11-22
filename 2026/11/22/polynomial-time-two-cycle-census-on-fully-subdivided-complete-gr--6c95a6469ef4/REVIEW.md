# Scientific review

## Correctness — PASS
The update is the conservative degree-threshold parallel chip-firing map on the complete-graph subdivision. A direct Laplacian argument identifies the two complementary firing phases, with exactly the product of opposite-neighbor degrees many compatible chip positions for a firing phase. The subdivision-vertex elimination and reciprocal-choice inclusion–exclusion give the stated four-index sum without assuming independence of the cross-edge endpoint choices. All color assignments and temporal phases are counted exactly once at the orbit level. Exact arithmetic and direct exhaustive chip dynamics independently agree for the stated finite cases. The formula is proved for all integers \(n\ge3\); numerical experiments are corroborative only.

## Originality — PASS, with priority limitations
The earlier unrestricted cut-degree polynomial determines the period-two orbit count by an exponential graph-cut sum, and is expressly credited in the proof. It does not give the four-index formula or an \(O(n^4)\) evaluation for incidence graphs of complete graphs. Jiang (2010) proves the general firing-count equality and period constraints for complete bipartite graphs, which are not the present subdivided cliques. The examined complete-bipartite and tree classifications are not stronger results for this family. Targeted searches found no exact matching subdivision-clique sieve. Historical treatments not indexed or accessible in full may remain, so this is a qualified originality judgment, not a priority certificate.

## Value — PASS
Fully subdivided complete graphs are canonical high-symmetry incidence networks with \(\Theta(n^2)\) vertices and exponentially many firing configurations. The result gives a uniform polynomial-operation exact evaluator for a natural dynamical invariant, using a structural sieve to handle correlated edge orientations. This is a nontrivial algorithmic compression beyond merely evaluating small cases or substituting one graph into a general exponential sum.

## Scope and limits
The theorem counts only primitive temporal two-cycle orbits and makes no claims about other periods, all attractors or basins. It uses exact arithmetic operation complexity and does not assert a constant-bit operation model. Independent external verification and definitive historical priority are unestablished.

Self-review: passed. Independent audit: not yet performed.
