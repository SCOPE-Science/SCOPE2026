# Independent mathematical audit

## correctness

PASS

In S(H) the two parts are independent forcing systems: colors within a part are changed using the white-neighbor count of vertices in the other part, regardless of their own colors. An initially unseeded original layer cannot begin, and white subdivision vertices on a cycle cannot be removed first from that cycle. Conversely white subdivision edges in a forest are peeled by a leaf, and one blue original seed reaches all originals by connectivity. Coefficient extraction over all spanning forests gives T_H(1+z,1) with exponent n−1−|F|; minimizing requires precisely a root and the complement of a spanning tree. The minima have one token in the original part, so a host-edge slide never preserves minimality. An exchange changes either the root or removes one tree edge and inserts another; this gives the product and the distance by adding a missing target edge on a fundamental cycle and removing an edge outside the target tree. The proof phrase 'one-edge symmetric difference' means one replacement (symmetric difference of size two). In K_n the number of tree-neighbors is the sum of path lengths of non-tree edges, hence W(T)−(n−1); the root factor adds n−1. Summing W over trees by edge cuts counts both shore orderings, and then the handshake lemma accounts for the other factor 2. The given path and the second tree are disjoint for n≥4, and n=2,3 are handled separately. All substantive claims in RESULT.md lines 5–31 and 43–65 follow. The two packaged programs were inspected, not run; proof rather than finite examples handles every H and n.

## originality

FAIL

The claimed surviving reconfiguration result is a direct specialization of the previously reported incidence/lazy-burning factorization plus ordinary graph and matroid basis exchange, not a separate structural theorem beyond it. This is coverage by implication, not a claim that the exact product formula was located verbatim. Applying prior incidence factorization and the graph/dual tests yields the feasible family as a direct product, with minimum choices independently {root} and a cographic basis. One-token exchange is by definition the basis graph of U_{1,n}⊕M*(H), whose exchange graph is the product of the two basis graphs; complementing the cographic factor gives the familiar spanning-tree graph. The distance is its standard basis difference metric, and the no-slide fact is forced by the two ranks and incidence bipartition. The K_n additions are direct tree-graph and Cayley counts from that product. No separate supported nonmechanical claim was found in the frozen statement.

## value

FAIL

The exposition is a useful example of the split between jumps and slides, but the instance does not establish an additional nonmechanical invariant: the prior separation fixes the two minimum factors, standard basis exchange fixes the metric, and the clique degree, edge sum and diameter are ordinary path, cut and disjoint-tree counts applied to that product. It does not isolate a further unknown precise graph statistic or structural obstruction beyond those consequences. A useful exposition of this specialization is not itself a new finding of the required value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
