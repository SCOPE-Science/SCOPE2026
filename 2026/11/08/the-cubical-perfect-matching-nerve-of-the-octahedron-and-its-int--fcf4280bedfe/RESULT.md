# The cubical perfect-matching nerve of the octahedron and its integral equivariant inclusion

## Finding
Let \(O=K_{2,2,2}\), let \(P(O)\) be the simplicial complex whose vertices are graph edges and whose facets are perfect matchings, and let \(M(O)\) be the ordinary matching complex. The eight perfect-matching facets of \(P(O)\) have an intersection nerve \(N\) isomorphic to the one-dimensional cube \(Q_3\). The equivalence given by the facet-intersection nerve is equivariant for the entire group \(G=\operatorname{Aut}(O)\cong C_2^3\rtimes S_3\) of order \(48\), and the induced cube action is the full cube automorphism group. In particular,
\[
P(O)\simeq_G Q_3\simeq\bigvee^5 S^1,
\qquad H_1(P(O);\mathbb Z)\cong H_1(Q_3;\mathbb Z)
\]
as **integral** \(G\)-modules, with the right module understood as the oriented cycle lattice of the cube.

Exactly six disjoint two-edge matchings of \(O\) cannot be extended to a perfect matching. Call their set \(B\). They are precisely the six edges added when passing from \(P(O)\) to \(M(O)\), and there is a natural short exact sequence of integral \(G\)-modules
\[
0\longrightarrow H_1(P(O);\mathbb Z)
\longrightarrow H_1(M(O);\mathbb Z)
\longrightarrow \mathbb Z[B]_{\mathrm{or}}\longrightarrow0.
\]
The term \(\mathbb Z[B]_{\mathrm{or}}\) is the rank-six signed permutation lattice in which reversing the orientation of an added one-simplex multiplies its generator by \(-1\). In particular, inclusion induces a **primitive** rank-five embedding in the rank-eleven lattice, and the integral quotient is free of rank six. No equivariant integral splitting of the sequence is asserted.

Identify the rotation subgroup \(G^+\) with \(S_4\) through the four pairs of opposite cube vertices; let \(\det:G\to\{\pm1\}\) be the determinant of the corresponding signed-coordinate cube symmetry. For rational irreducible \(S_4\)-modules \(S^\lambda\), the full \(G\)-module is
\[
H_1(P(O);\mathbb Q)\cong
S^{(2,1,1)}\oplus(S^{(2,2)}\otimes\det).
\]
Central inversion acts with trace \(1\) and \((+1,-1)\)-eigenspace dimensions \((3,2)\) on \(H_1(P(O);\mathbb Q)\). Every full-group invariant integral one-cycle vanishes. On the six-dimensional relative quotient central inversion acts as \(-I\), reconciling the perfect-complex trace \(1\) with the ordinary-complex trace \(-5\).

## Assumptions and scope
Write the six vertices of \(O\) as \(a_i^b\) for \(i=0,1,2\) and \(b=0,1\). Two vertices are adjacent exactly when their part indices differ. Thus the only nonedges among different vertices are the three antipodal pairs \(\{a_i^0,a_i^1\}\). A graph matching is a set of pairwise vertex-disjoint edges. A perfect matching covers all six vertices. For this result, the facets of \(P(O)\) are the perfect matchings, whereas every matching is a face of \(M(O)\). These are not complexes of Morse matchings or acyclic vector fields.

Regard \(Q_3\) as the graph on \(\{0,1\}^3\) with edges between triples of Hamming distance one. The subscript \(\simeq_G\) means an equivariant homotopy equivalence of the geometric realizations. The module statement is integral; the Specht decomposition is over \(\mathbb Q\) only.

## Proof
**Eight perfect matchings.** Any perfect matching contains exactly one edge between each unordered pair of parts \(\{0,1\}\), \(\{1,2\}\), and \(\{2,0\}\). Indeed, the number of matching edges incident with each part is two, which forces those three edge-type counts to be one. Every choice \(\epsilon=(\epsilon_0,\epsilon_1,\epsilon_2)\in\{0,1\}^3\) determines the unique matching
\[
F_\epsilon=\bigl\{\{a_0^{\epsilon_0},a_1^{\epsilon_1}\},
\{a_1^{1-\epsilon_1},a_2^{\epsilon_2}\},
\{a_2^{1-\epsilon_2},a_0^{1-\epsilon_0}\}\bigr\}.
\]
These are exactly the eight perfect matchings. Two distinct matchings share an edge precisely when their binary labels differ in one coordinate: a common edge fixes two labels, leaving exactly one other label free. Every original graph edge belongs to exactly two perfect matchings. Hence no three facets have nonempty intersection, and the facet-intersection nerve is exactly the graph \(Q_3\).

**Canonical equivariant nerve equivalence.** Let \(\mathcal F\) be the poset of nonempty faces of \(P(O)\) and \(\mathcal I\) the poset of nonempty faces of the nerve. The maps
\[
\sigma\mapsto \{F:\sigma\subseteq F\},
\qquad A\mapsto\bigcap_{F\in A}F
\]
are order-reversing. They are everywhere defined because \(\sigma\) lies in a perfect-matching facet, and a nerve simplex is by definition an intersecting collection of facets. Their compositions enlarge each nonempty face. The resulting equivariant closure-operator homotopies on order complexes (equivalently, barycentric subdivisions) give \(P(O)\simeq_G N\). The full graph group independently permutes the two vertices of each part and permutes the three parts, so \(G\cong C_2^3\rtimes S_3\) has order \(48\). Its induced action on the eight perfect matchings is faithful: each original graph edge is the intersection of the unique pair of facets containing it. There are also exactly \(48\) automorphisms of \(Q_3\) (the image of one vertex and permutation of its three neighbors determine an automorphism), so the induced action is the full cube group. Thus \(H_1(P(O);\mathbb Z)\) is naturally the five-dimensional integral cube cycle lattice.

**The exact relative module.** Every one-edge matching extends to a perfect matching. A two-edge matching fails to extend precisely when its two unused vertices form one of the three antipodal nonedges; after choosing that nonedge the remaining four vertices admit exactly two disjoint-edge pairings. Therefore exactly \(3\cdot2=6\) two-edge matchings are unextendible. Each is a missing one-simplex of \(P(O)\), and all three-edge matchings are perfect. Consequently \(M(O)\) is obtained from \(P(O)\) by adding exactly six edges, all with endpoints already present. Both spaces are connected because the nerve is a connected cube, and the union-of-facets property gives the same vertex set. The relative simplicial chain complex has only \(C_1(M(O),P(O))\cong\mathbb Z[B]_{\mathrm{or}}\) nonzero. Its differential is zero because endpoints lie in \(P(O)\). The long exact sequence of the pair, together with \(H_0(P(O))\xrightarrow{\sim}H_0(M(O))\), gives the claimed short exact sequence, including integral primitivity. Its ranks are \(5,11,6\); nonequivariantly \(M(O)\simeq\bigvee^{11}S^1\).

**Integral and rational symmetry.** Since the nerve is a graph, its integral first homology is the kernel of the oriented edge-incidence map from \(\mathbb Z^{12}\) to \(\mathbb Z^8\). For any cube symmetry \(g\), an equivariant graph Lefschetz count yields
\[
\operatorname{tr}(g\mid H_1(Q_3;\mathbb Q))
=1-\operatorname{tr}(g\mid C_0(Q_3;\mathbb Q))
+\operatorname{tr}(g\mid C_1(Q_3;\mathbb Q)).
\]
The last trace counts fixed oriented edges with their induced signs. A direct check of all \(48\) signed-coordinate symmetries gives the following complete class table, using cycle type \(\mu\) on the four opposite-vertex pairs, and \(\delta=\det(g)\):

| \(\mu\) | \(\delta\) | size | \(\operatorname{tr}(g\mid H_1)\) |
| --- | ---: | ---: | ---: |
| \((1,1,1,1)\) | \(+1\) | 1 | 5 |
| \((1,1,1,1)\) | \(-1\) | 1 | 1 |
| \((2,1,1)\) | \(+1\) | 6 | -1 |
| \((2,1,1)\) | \(-1\) | 6 | -1 |
| \((2,2)\) | \(+1\) | 3 | 1 |
| \((2,2)\) | \(-1\) | 3 | -3 |
| \((3,1)\) | \(+1\) | 8 | -1 |
| \((3,1)\) | \(-1\) | 8 | 1 |
| \((4)\) | \(+1\) | 6 | 1 |
| \((4)\) | \(-1\) | 6 | 1 |

The values equal \(\chi_{(2,1,1)}(\mu)+\delta\chi_{(2,2)}(\mu)\), proving the rational decomposition by character orthogonality. Antipodal inversion exchanges each of the six unextendible one-simplex's endpoints, so its action on the signed relative module is \(-I\). Its two traces are consequently \(1\) on \(H_1(P(O))\) and \(-5=1-6\) on \(H_1(M(O))\). Finally, for each cube edge some cube symmetry fixes the underlying edge while reversing its orientation. Therefore any invariant integral one-cycle has coefficient zero on every cube edge; the invariant cycle lattice is trivial.

## Verification
Run `python3 verify_octahedral_perfect.py` using Python 3 and no external packages. The verifier independently enumerates all three-edge perfect matchings and reconstructs the eight via binary coordinates, lists all faces of both matching complexes, checks the six unextendible two-edge matchings, checks exactly two perfect matchings per graph edge, reconstructs the twelve nerve edges and verifies the cube correspondence, checks triangle freeness of the nerve, enumerates all 48 automorphisms and their faithful actions, checks the complete ten-class character table and Specht-character identity, and tests the center and invariant-cycle obstruction. Its expected final line is `VERIFY_OK`. The adjoining file `verification_octahedral_perfect.txt` records an actual execution.

Finite exhaustive checks verify the eight-facet calculations; the poset proof and relative-chain argument supply the structural integral statements. This proof makes no claim for higher cocktail-party graphs.

## Relationship to prior work
Bayer, Jelić Milutinović, and Vega define perfect-matching complexes and determine homotopy types for honeycomb families (first public 2022-09-06). Chandrakar and Singh study polygonal line tilings and characterize nonextendible matchings in grid families (first public 2024-07-08); neither family theorem covers \(K_{2,2,2}\). A published calculation titled *The full octahedral symmetry representation of the matching complex* treats the **ordinary** complex \(M(O)\), proving its eleven-circle homotopy type and complete rational representation, but explicitly excludes the perfect-matching subcomplex. The previously known ordinary representation is consistent with, and once the present inclusion is known supports, the rational irreducible decomposition above; it does not itself establish the natural cubical nerve, the integral equivariant embedding or the signed six-edge quotient. The distinction is not merely a change of name: the two complexes have different integral cycle ranks and a nontrivial relative representation.

## Limitations
The integral representation is given as a concrete oriented cycle lattice and an exact sequence, not as a classification of all indecomposable integral \(G\)-lattices. The rational decomposition need not split integrally, and no equivariant integral splitting of the relative extension is claimed. Equivariant homotopy equivalence to the cube does not mean that \(P(O)\) is isomorphic as a simplicial complex to the one-dimensional cube (the former has eight two-simplices). The full literature may contain an unindexed equivalent computation; no general result for higher-dimensional cross-polytope graphs follows.

## References
1. M. Bayer, M. Jelić Milutinović and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803v1, first public 2022-09-06. https://arxiv.org/abs/2209.02803
2. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809v1, first public 2024-07-08. https://arxiv.org/abs/2407.05809
3. *The full octahedral symmetry representation of the matching complex*, publicly available mathematical record (2026), addressing the ordinary matching complex. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-full-octahedral-symmetry-representation-of-the-matching-comp--c700eceb52bb
