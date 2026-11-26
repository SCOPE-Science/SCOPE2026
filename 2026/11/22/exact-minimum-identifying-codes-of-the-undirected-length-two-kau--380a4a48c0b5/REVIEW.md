# Independent mathematical audit

## correctness

PASS

Reassessed the corrected claim against the closed-neighborhood predicate on distinct ordered pairs and the exact replay. The number of vertices is q(q-1); edges of the symmetrized shift satisfy b=c or d=a only for distinct pairs, and the vertex itself is included separately. For each candidate code, the bit-mask intersections with all closed neighborhoods must be nonzero and pairwise distinct, exactly the two identifying conditions. The independent replay constructed these neighborhoods and exhausted the complete k=m-1 and k=m layers. For q=4 these were 0/220 and 168/495 accepted; for q=5, 0/4845 and 24/15504; for q=6, 0/593775 and 4320/2035800. If a smaller code existed its signatures would stay nonempty and distinct under extension, since restricting to the smaller code recovers the old signatures. The zero layers therefore rule out all smaller k. Simultaneous alphabet permutations preserve the adjacency predicate and act on code subsets. The independent orbit replay verified all supplied representatives, generated their images under every permutation, and checked that the respective disjoint orbit unions equal the enumerated code sets. At q=4 the sorted sizes are 6,6,12,12,12,24,24,24,24,24; at q=5 the one size is 24; at q=6 every one of six orbits has size 720. The corrected files agree with these counts and state exactly the tested scope.

## originality

PASS

The frozen finding's q=3 minimum fails novelty: U_3 consists of two directed-cycle triangles joined by reversal, so it is the triangular prism L(K_{2,3}); Foucaud et al., Proposition 11 and the following K_{2,n} example give the exact minimum there. The proof restricts the two omitted edges at optimum to one edge incident with each hub of K_{2,3}; that condition suffices, so the labeled count nine is also a direct consequence. No priority claim about the q=3 orbit decomposition is necessary because the repaired finding drops the row entirely. For the repaired q=4,5,6 scope, the line-graph implication no longer applies, the known directed and de Bruijn results do not cover it, and no earlier exact census for the repaired class was established in the bounded checks.

## value

PASS

The repaired question concerns the first consecutive cases of the undirected length-two family outside the line-graph reduction. The exact code sizes show the breakdown at six symbols of the equality with alphabet size observed at four and five. The counts and complete orbit representatives expose substantially different optimum structures on consecutive graphs, not merely a success on one witness in each. This supplies useful exact benchmarks for a natural identification invariant in shift networks, without claiming a general law or gaining credit for the previously known prism minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
