# Integral homotopy type of the five-regular Clebsch dominance complex

## Finding
Let \(C\) be the sixteen-vertex, five-regular Clebsch graph in the Cayley realization
\[
V(C)=\mathbb F_2^4,\qquad x\sim y\Longleftrightarrow
x-y\in\{e_1,e_2,e_3,e_4,e_1+e_2+e_3+e_4\}.
\]
Its dominance complex is the simplicial complex
\[
\operatorname{Dom}(C)=\{S\subseteq V(C):V(C)\setminus S\text{ dominates }C\}.
\]
There is an integral homotopy equivalence
\[
\boxed{\operatorname{Dom}(C)\simeq\bigvee^{131} S^9.}
\]
In particular its only nonzero reduced integral homology is \(\widetilde H_9(\operatorname{Dom}(C);\mathbb Z)\cong\mathbb Z^{131}\); the complex is \(8\)-connected. Its vertex-cover number is \(\tau(C)=11\), so this canonical vertex-transitive graph exhibits a strict instance \(8+2<11\) of Matsushita's connectivity lower bound for vertex covers.

## Assumptions and scope
The graph has labeled vertices \(0,1,\ldots,15\), representing binary four-vectors. Adjacent distinct vertices have bitwise XOR in \(\{1,2,4,8,15\}\). This distinguishes the **five-regular** Clebsch/folded-five-cube graph, of strongly regular parameters \((16,5,0,2)\), from its ten-regular complement, sometimes also called the Clebsch graph. For every vertex \(v\), let \(N[v]=\{v\}\cup N(v)\) be the **closed** graph neighborhood. Then the face criterion is precisely
\[
S\in\operatorname{Dom}(C)\Longleftrightarrow
\bigl(\forall v\in V(C)\bigr)\ N[v]\not\subseteq S.
\]
Faces include the empty face, but the discrete-Morse matching is on the **nonempty** face poset. Statements about integral homotopy refer to the geometric realization of this simplicial complex. All counts and homotopy statements concern the fixed graph above, not an infinite family.

## Proof
**1. Exact face system.** For each \(v\in V(C)\), compute \(N[v]\) from the five XOR directions. A subset \(S\) is a face if and only if none of the sixteen six-element sets \(N[v]\) is contained in it. This is exactly the displayed dominance criterion, since \(V(C)\setminus S\) dominates every \(v\) precisely when it intersects \(N[v]\). The two implementations in the verifier test the two logically equivalent conditions independently on all \(2^{16}\) vertex subsets. There are exactly \(53{,}730\) nonempty faces. Their numbers in dimensions \(0\) through \(11\), respectively, are
\[
(16,120,560,1820,4368,7992,11280,12150,9520,4768,1056,80).
\]
The complex has \(368\) facets: \(192\) of dimension \(9\), \(96\) of dimension \(10\), and \(80\) of dimension \(11\); hence it is nonpure.

**2. Fully specified discrete-Morse matching.** Put the vertex order
\[
(10,14,5,1,9,2,3,11,13,7,8,4,0,6,15,12).
\]
Initially all nonempty faces are unmatched. At each pivot \(p\) in this order, traverse all nonempty face masks in increasing numerical order. Whenever \(S\) is still unmatched, does not contain \(p\), and \(S\cup\{p\}\) is also a still-unmatched face, match \(S\) with \(S\cup\{p\}\). Every match is a covering relation in the face poset; no face occurs in two pairs. The complete deterministic rule gives \(26{,}799\) matched covering pairs and precisely \(132\) critical faces: one vertex and \(131\) nine-simplices.

**3. Exhaustive acyclicity certificate.** Consider every covering relation \(T\supset S\) between nonempty faces with \(|T|=|S|+1\). Direct it **upward** \(S\to T\) if the pair is matched and **downward** \(T\to S\) otherwise. The executable checker constructs all \(401{,}088\) such relations and performs a topological sort of the full directed graph. The sort visits exactly \(53{,}730\) distinct faces, proving it has no directed cycle. This is a complete finite verification, not a random sample or a rank-only homology computation. The precise face-set and matching SHA-256 values printed by the checker fingerprint the enumerated certificate.

**4. Passage to integral homotopy.** Forman's discrete Morse theorem gives a CW complex homotopy equivalent to \(\operatorname{Dom}(C)\), with one cell for each critical face. Here the CW complex has exactly one zero-cell and \(131\) nine-cells and no other cells. Every attaching map of a nine-cell has target the single zero-cell because there are no positive-dimensional cells below dimension nine. All such maps are therefore constant. The CW complex is \(\bigvee^{131}S^9\), which proves the integral homotopy statement, not just its Betti vector. No extrapolation from finite samples is involved: the entire fixed sixteen-vertex graph has been exhausted.

**5. Vertex-cover corollary.** Exhaustive testing of all \(2^{16}\) vertex subsets finds independent sets of maximal size \(5\), with \(16\) attaining this size. Thus \(\tau(C)=16-5=11\). The displayed wedge is exactly \(8\)-connected, and the published general inequality \(\operatorname{conn}(\operatorname{Dom}(G))+2\le\tau(G)\) is strict by one for this graph.

## Verification
Run `python3 verify_clebsch_dominance.py` under Python 3 using only its standard library. The script performs graph-adjacency and strongly-regular-parameter checks, independently evaluates the face condition in two ways for every one of the \(65{,}536\) subsets, reconstructs the specified matching, checks disjointness and codimension one of all matched pairs, builds all \(401{,}088\) Hasse covers, and topologically sorts the complete oriented poset. It also checks the full face vector, Euler characteristic \(-130=1-131\), the vertex-cover number, and SHA-256 fingerprints. The exact output is provided in `verification_clebsch_dominance.txt`; its last line is `CLEBSCH_DOMINANCE_INTEGRAL_WEDGE_PASS`. This program is a complete finite certificate for the specified sixteen-vertex complex; it does not prove any assertion about a graph family.

## Relationship to prior work
Marietti–Testa [1] develop the core technique and apply it to dominance complexes of forests. Taylan [2] calculates dominance complexes for chordal graphs. The five-regular Clebsch graph is triangle-free, contains four-cycles, and is neither a forest nor chordal; those stated classifications do not determine its dominance complex. Matsushita [3] proves the general bound involving the vertex-cover number, but not this graph's integral homotopy type. Matsushita–Wakatsuki [4] identify the dominance complex with the combinatorial Alexander dual of the **open-neighborhood complex of the complement graph**; this formal relation alone does not supply the claimed integral wedge. The publicly recorded determination [5] of the five-regular Clebsch graph's own open-neighborhood complex as \(\bigvee^{31}S^2\) concerns \(\mathcal N(C)\), not \(\mathcal N(\overline C)\), and so does not settle \(\operatorname{Dom}(C)\). Other Clebsch results on ordinary independence and matching complexes likewise impose different face conditions. Searches for the literal graph, its folded-cube/Greenwood–Gleason aliases, closed-neighborhood avoidance, Alexander duality, and previously recorded related results found no inspected theorem implying this exact homotopy classification. Publication priority beyond the inspected sources is not certified.

## Limitations
This is an exact result for the specific five-regular, sixteen-vertex graph, not a general statement about strongly regular graphs or other folded hypercubes. The procedure determines nonequivariant **integral homotopy type**, but does not determine the full automorphism representation on homology or an equivariant wedge splitting. The finite certificate's acyclicity depends on the explicitly supplied enumeration and topological-sort implementation and is reproducible from source. Possible unindexed or implicit earlier calculations remain an originality risk. Independent mathematical audit has not been performed.

## References
[1] M. Marietti and D. Testa, *Cores of simplicial complexes*, arXiv:math/0703351v1, first publicly submitted 2007-03-12, https://arxiv.org/html/math/0703351v1 (especially Sections 1 and 8).

[2] D. Taylan, *Matching trees for simplicial complexes and homotopy type of devoid complexes of graphs*, arXiv:1501.06754v1, first publicly submitted 2015-01-27, https://arxiv.org/abs/1501.06754.

[3] T. Matsushita, *Dominance complexes and vertex cover numbers of graphs*, arXiv:2009.04145, first publicly submitted 2020-09-09, https://arxiv.org/abs/2009.04145.

[4] T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639, first publicly submitted 2023-12-05, https://arxiv.org/abs/2312.02639.

[5] *The five-regular Clebsch neighborhood complex is a wedge of 31 two-spheres*, public result at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-5-regular-clebsch-neighborhood-complex-is-a-wedge-of-31-2-sp--1dc11cc6574a.

[6] R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145, DOI: 10.1006/aima.1997.1650.
