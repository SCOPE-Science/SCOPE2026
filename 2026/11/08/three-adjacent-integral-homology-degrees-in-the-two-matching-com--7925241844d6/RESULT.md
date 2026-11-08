# Three adjacent integral homology degrees in the two-matching complex of \(K_{2,2,3}\)

## Finding
Let \(G=K_{2,2,3}\) be the complete tripartite graph on the vertex parts \(\{0,1\}\), \(\{2,3\}\), and \(\{4,5,6\}\). The complex \(X=M_2(G)\) has the 16 edges of \(G\) as simplicial vertices; a set of these edges is a face precisely when each original graph vertex has selected degree at most two. Then
\[
\widetilde H_i(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=3,\\
\mathbb Z^{19},&i=4,\\
\mathbb Z^6,&i=5,\\
0,&\text{otherwise}.
\end{cases}
\]
There is no integral torsion. The complex has 4,107 nonempty simplices and is nonpure with maximal faces of dimensions three through six. The result is an integral homology classification, **not** a statement that the space is homotopy equivalent to a wedge of spheres.

## Assumptions and scope
Graphs are simple and undirected. The 16 edges are ordered lexicographically by the partition pair followed by endpoints. An edge subset is encoded by a 16-bit integer, with the bit set exactly for selected edges. All chain complexes use the usual increasing-edge orientation, the empty face is excluded from ordinary cellular differentials, and the reduced homology convention has one connected component contributing no reduced degree-zero homology. No other complete tripartite part sizes are covered.

## Proof
**1. Exact domain.** The seven graph vertices have three prescribed parts, with all edges joining different parts and no internal edges. Exhaustively test every one of \(2^{16}=65,536\) subsets against degree at most two. An independent equivalent test forbids every three-edge star centered at a graph vertex. Both tests produce the number of faces by cardinality
\[
(1,16,120,508,1213,1476,714,60).
\]
The initial \(1\) is the empty face. Maximal faces have dimensions \(3,4,5,6\), with counts \(1,36,294,60\), respectively.

**2. Acyclic reductions.** In the increasing graph-edge order, sequentially pair every still-unmatched face not containing the next edge with its admissible coface obtained by adding that edge. There are exactly 2,018 pairs, leaving critical cell counts \(c_3=9\), \(c_4=42\), and \(c_5=21\), with no other critical faces in the augmented face poset. In particular, the pair containing the empty face is removed; in the ordinary unaugmented complex the result is one critical vertex plus these higher cells. The directed Hasse graph, oriented downwards except upwards along the matched incidences, has exactly 4,107 nonempty faces and 18,700 cover relations. The checker topologically sorts this entire graph; it is acyclic.

Reverse the graph-edge order and repeat the identical procedure. This independently yields 2,026 pairs, with critical counts \(c_3=2\), \(c_4=34\), \(c_5=20\), plus a critical vertex in the ordinary complex. This second matching is likewise acyclic on all 18,700 cover relations.

**3. Integral chain reductions.** For each matching use the actual signed simplicial boundary \(\partial[e_{i_0},\dots,e_{i_k}]=\sum_{j=0}^k(-1)^j[e_{i_0},\dots,\widehat{e_{i_j}},\dots,e_{i_k}]\). For a paired lower simplex \(a\) and upper simplex \(b\), the incidence \([b:a]\) is \(\pm1\). Eliminate it using the exact relation
\[
a\equiv-[b:a]^{-1}\sum_{c\ne a}[b:c]\,c,
\]
recursively along the directed acyclic matching, and project every upper matched cell to zero. This produces the signed Morse matrices on the critical cells. For the increasing-edge ordering, \(\partial^{\mathrm M}_4\) is an integer matrix of size \(9\times42\) with rank eight, and \(\partial^{\mathrm M}_5\) has size \(42\times21\) with rank fifteen. Every nonzero Smith invariant of both matrices is \(1\), witnessed constructively by sequences of eight and fifteen integral unit-pivot row and column eliminations with zero remaining blocks. The differential composition is identically zero.

For the reversed order the corresponding matrices have sizes \(2\times34\) and \(34\times20\); their ranks are one and fourteen, respectively, and again all nonzero Smith invariants are \(1\). In this second computation every pivot and residual zero block is independently obtained from reversed graph-edge enumeration.

**4. Homology.** The first critical Morse complex therefore has the chain dimensions \(9,42,21\) in degrees \(3,4,5\), with boundary ranks \(8,15\). It follows that the homology ranks are \(9-8=1\), \(42-8-15=19\), and \(21-15=6\). The unit Smith invariants rule out all integral torsion, and the single ordinary critical vertex confirms connectedness. The second reduction gives \(2-1=1\), \(34-1-14=19\), and \(20-14=6\), in agreement.

## Verification
Run `python3 verify_k223.py` and `python3 verify_k223.py reverse` (Python standard library only). Each program rebuilds the domain, independently checks star exclusion, constructs the matching, topologically sorts every reversed Hasse edge, computes exact signed Morse matrices, performs integral unit-pivot eliminations, and verifies the chain-complex identity. Direct mod-two ranks of the original simplicial boundaries, independently evaluated without the Morse matrices, are \((15,105,403,809,648,60)\) for degrees one through six and agree with the integral Betti numbers. Exact deterministic console outputs accompany the scripts.

## Relationship to prior work
Vega (arXiv:1909.10406; first public version September 23, 2019) introduces the two-matching complex and proves results for leaf modifications, wheels and perfect caterpillars. Singh (arXiv:2006.13632; first public version June 24, 2020) studies higher matching complexes of complete graphs and complete bipartite graphs. Neither result determines the integral two-matching homology for the complete **tripartite** graph with part sizes \(2,2,3\). The balanced complete-tripartite example \(K_{2,2,2}\) is a different graph, and its previously studied two-matching invariant does not imply the present three-degree profile. Targeted searches for part-size aliases, bounded-degree complexes, complete multipartite formulations and stronger family theorems found no equivalent classification in inspected literature.

## Limitations
The result gives integral homology, not the full homotopy type. In particular the attaching maps of higher Morse cells need not vanish in homotopy even when all the reduced homology groups are free abelian; no wedge decomposition or equivariant classification is asserted. Searches cannot exclude unindexed or inaccessible equivalents. No claim is made about general \(K_{a,b,c}\) or other degree caps.

## References
1. J. Vega, *2-Matching Complexes*, arXiv:1909.10406 (first public version 2019-09-23). https://arxiv.org/abs/1909.10406
2. A. Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632 (first public version 2020-06-24). https://arxiv.org/abs/2006.13632
3. R. Forman, *Morse Theory for Cell Complexes*, Adv. Math. **134** (1998), 90–145.
