# Strong odd colorings of the Coxeter graph: a fourteen-partition rigidity theorem

## Finding

For the Coxeter graph \(X\) on 28 vertices, the strong odd chromatic number is exactly
\[\chi_{\mathrm{so}}(X)=4.\]
There are exactly **336** strong odd colorings using the four named colors \(0,1,2,3\), or exactly **14** color partitions after forgetting color names. In every optimum the four class sizes are \((4,8,8,8)\). Its unique four-vertex color class is a set of four vertices at mutual graph distance four, and this set determines the entire unnamed coloring uniquely. Conversely, each of the 14 four-vertex diameter-four cliques yields one optimum. The 14 optima form a single orbit under graph automorphisms.

## Assumptions and scope

A *strong odd coloring* of a simple finite graph is a proper vertex coloring in which every color appearing in the open neighborhood of any vertex occurs there an odd number of times. Names of colors matter for the count 336; for the count 14 colors are identified up to any global permutation. The color sets in an optimum are all nonempty.

The labeled 28-vertex Coxeter graph \(X\) has seven center vertices \(c_i\), indexed by \(i\in\mathbb Z/7\mathbb Z\), and for each \(j\in\{0,1,2\}\), seven leaf vertices \(x_{j,i}\), indexed by \(i\in\mathbb Z/7\mathbb Z\). Write \((s_0,s_1,s_2)=(1,2,4)\). Its edges are exactly
\[c_ix_{j,i}\quad\text{and}\quad x_{j,i}x_{j,i+s_j}\qquad(i\in\mathbb Z/7\mathbb Z,\ j\in\{0,1,2\}).\]
For the supplied checkers, the integer vertex labeling is \(c_i=i\) and \(x_{j,i}=7+7j+i\). The graph has 42 edges and is connected, cubic, and nonbipartite: the leaf cycle within each \(j\) is a seven-cycle. The second checker independently constructs the Coxeter graph as the disjointness graph on the 28 nonline three-subsets of the Fano plane and verifies an explicit graph isomorphism.

The fourteen diameter-four cliques are exactly the following sets, one for each \(i\in\mathbb Z/7\mathbb Z\) and each sign:
\[D_i^+=\{c_i,x_{0,i+4},x_{1,i+1},x_{2,i+2}\},\qquad D_i^-=\{c_i,x_{0,i+3},x_{1,i+6},x_{2,i+5}\}.\]
All subscripts are modulo seven.

## Proof

**Lower bound.** If a connected cubic graph has a strong odd coloring with at most three colors, then the three neighbors of each vertex use at most two colors, since the coloring is proper. Having two distinct neighbor colors would give multiplicities two and one, disallowed by strong oddness; hence all three neighbors must have the same color. Consequently any vertices joined by an even walk have the same color. In a connected nonbipartite graph every two vertices are joined by an even walk: append a route to an odd cycle, traverse it once, and return to reverse the parity of any walk. Therefore all vertices would share a color, contradicting properness. The Coxeter graph is connected and has seven-cycles, so \(\chi_{\mathrm{so}}(X)\ge4\).

**Local constraints for four colors.** At a cubic vertex \(v\), the colors of its three neighbors must be either all equal or pairwise different, and they must differ from the color of \(v\). There are precisely \(4\cdot(3+3!)=36\) permitted ordered color templates for the four ordered vertices \((v,u_1,u_2,u_3)\). Every strong odd four-coloring is exactly a global assignment satisfying all 28 such constraints; no other assumptions enter the finite enumeration.

**Complete exhaustive census.** The accompanying `check_cyclic.cpp` enumerates assignments with vertex \(c_0\) assigned color zero. It starts with all four colors available at all other vertices; repeatedly deletes a candidate only when the candidate has no permitted local-template support, then branches on a vertex of smallest remaining domain. A globally valid assignment can never be deleted by this support test, and every assignment not deleted is represented by one branch. Each singleton-domain leaf is checked against the original properness and odd-neighborhood conditions. This exhaustive search gives exactly **84** colorings with \(c_0=0\); since every named four-coloring can choose any of the four colors at \(c_0\), there are exactly \(4\cdot84=336\) named colorings. The checker canonically renames colors in order of first appearance and verifies there are exactly **14** resulting partitions. Every leaf has color-class sizes \((4,8,8,8)\).

The same checker computes graph distances by breadth-first search and tests all \(\binom{28}{4}\) four-vertex subsets, finding exactly 14 sets whose six pair distances equal four; it verifies those 14 are precisely the explicit \(D_i^\pm\) above. It records the unique size-four class from every solution; the image consists of exactly those 14 sets, each appearing exactly six times when \(c_0\) is fixed. Because six is the number of permutations of the other three named colors, the underlying unnamed coloring is unique for each such set. This establishes the correspondence, both existence and uniqueness.

**Single symmetry orbit.** The map \(c_i\mapsto c_{i+1}\), \(x_{j,i}\mapsto x_{j,i+1}\) is a graph automorphism sending \(D_i^\pm\) to \(D_{i+1}^\pm\). The map \(c_i\mapsto c_{-i}\), \(x_{j,i}\mapsto x_{j,-i}\) also preserves every edge (each leaf-cycle edge is undirected), and exchanges \(D_i^+\) with \(D_{-i}^-\). Thus all 14 diameter-four sets, and by the established bijection all 14 color partitions, form a single orbit.

## Verification

`check_cyclic.cpp` is a standalone C++17 implementation using only its standard library. Compile and run with `g++ -std=c++17 -O2 check_cyclic.cpp -o check_cyclic && ./check_cyclic`. It verifies 28 vertices, 42 edges, 36 local templates, exactly 84 solutions with \(c_0=0\), 14 unnamed color partitions, all class sizes \((4,8,8,8)\), the diameter-four four-set classification, and uniqueness of the partition for each such set. Its printed first-appearance-normalized witness is `0012321132021211201301220003` in vertex order zero to 27. The program checks this and every other final assignment directly.

`check_fano.py` is a second standalone Python 3 standard-library implementation using independently constructed Fano nonline triples. It verifies a fixed explicit isomorphism to the seven-claw graph and branches over entire admissible four-vertex star templates instead of using the first program's domain-pruning routine. It also returns 84 root-fixed named colorings, 336 unrestricted named colorings, 14 unnamed partitions and the same class sizes. Its complete enumeration checks every local condition at its leaves. See `verification_expected.txt` for exact program outputs.

The lower bound and the symmetry argument are written mathematical proofs; the finite upper-bound and census are certified by executable exhaustive enumeration with two different source representations and search procedures. No computational claim for any larger family is made.

## Relationship to prior work

Kwon and Park introduced strong odd coloring and established bounds in sparse graphs (first publicly posted 2024-01-22). Caro, Petruševski, Škrekovski, and Tuza studied strong odd coloring of trees, unicyclic graphs, and graph products (publicly posted 2024-10-03). Neither inspected paper states this exact Coxeter-graph chromatic number or its optimum census. The 2014 article *Mapping planar graphs into the Coxeter graph* describes the 28-vertex Coxeter graph via the Fano plane but studies homomorphisms from other graphs **into** it, which is logically different from coloring the Coxeter graph itself under local parity constraints. Related existing exact coloring enumerations for sunlets, crowns and cyclic prisms have different underlying graphs, and existing Coxeter perfect-matching results concern a different invariant.

## Limitations

This is a result for one canonical finite graph, not a theorem for all cubic graphs or arbitrary Coxeter-like families. The exhaustive enumeration assumes the explicit graph representation given above, with an independent Fano-model isomorphism check. The count concerns exact strong odd colorings, not ordinary proper colorings or general odd colorings. The literature comparison is best knowledge; an equivalent result in an unindexed or inaccessible source remains a publication-priority risk. No independent human mathematical audit has been performed.

## References

1. H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653, first posted 2024-01-22, https://arxiv.org/abs/2401.11653.
2. Y. Caro, M. Petruševski, R. Škrekovski and Zs. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336, first posted 2024-10-03, https://arxiv.org/abs/2410.02336.
3. A. Harutyunyan et al., *Mapping planar graphs into the Coxeter graph*, available manuscript https://www.lamsade.dauphine.fr/~aharutyunyan/CoxeterFinal.pdf, 2014.
