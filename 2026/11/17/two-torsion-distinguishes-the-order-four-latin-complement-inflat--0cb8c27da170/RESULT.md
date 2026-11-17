# Two-torsion distinguishes the order-four Latin-complement inflations

## Finding
For any Latin square \(L\) of order four, let \(X_L\) be the two-dimensional three-coloured simplicial complex with three disjoint sets of four vertices \(A=\{a_0,\ldots,a_3\}\), \(B=\{b_0,\ldots,b_3\}\), and \(C=\{c_0,\ldots,c_3\}\). Every edge between distinct colours is present, and the triangle \(\{a_i,b_j,c_k\}\) is present **exactly when** \(k\ne L(i,j)\). Let \(f_L:X_L\to\Delta^2\) send vertices to their colours.

**Theorem (complete order-four classification).** Exactly two cases occur, according to the Latin-square isotopy class:
\[
\begin{array}{c|c|c|c}
L\text{ isotopic to}&\pi_1(X_L)&H_1(X_L;\mathbb Z)&H_2(X_L;\mathbb Z)\\\hline
(i+j)\bmod4&1&0&\mathbb Z^{11}\\
i\mathbin{\mathrm{xor}}j&\mathbb Z/2&\mathbb Z/2&\mathbb Z^{11}.
\end{array}
\]
In the cyclic case \(X_L\simeq\bigvee^{11}S^2\); in the Klein-four case \(X_L\) cannot be homotopy equivalent to a wedge of spheres. Every such complex has exactly twelve vertices, forty-eight edges, and forty-eight triangles; each edge is incident to three triangles. The diagram of simplices over the three colours has surjective restriction maps between **every pair of comparable nonempty base faces**, with the same restriction-fibre sizes in both cases. Nevertheless, it is not flabby: sixteen of the sixty-four compatible assignments on the boundary of the base triangle do not extend.

Of the 576 labelled order-four Latin squares, 432 lie in the cyclic isotopy class and 144 in the Klein-four class. Thus the same local lifting multiplicities and face counts support both simply connected and torsion-bearing spaces.

## Assumptions and scope
An order-four Latin square is a map \(L:\{0,1,2,3\}^2\to\{0,1,2,3\}\) such that every row and column is a permutation. Independent permutations of row, column, and symbol sets constitute an *isotopy*. Such permutations induce a colour-preserving simplicial isomorphism of the complexes defined above. The two representative laws are the additive groups \(\mathbb Z/4\) and \((\mathbb Z/2)^2\), with two-bit symbols encoded by the integers zero to three.

The base simplex has vertices \(A,B,C\). Its diagram takes a nonempty base face to the set of simplices of \(X_L\) mapping bijectively onto that face, with coordinate-forgetting maps. The top-fibre has forty-eight elements, each edge-fibre has sixteen, and each vertex-fibre has four. A top-to-edge restriction has three preimages of each edge; an edge-to-vertex restriction has four preimages of each vertex. These properties do not imply global flabbiness, which asks for surjectivity on sections over every nested pair of base opens. All homology and fundamental groups are those of the geometric realizations with integral coefficients unless another ring is displayed.

## Proof
**1. Uniform local lifting, and its global failure.** There are \(3\cdot4=12\) vertices, \(3\cdot4^2=48\) edges, and \(4^3-4^2=48\) triangles. Any row-column edge lies in three triangles, since only the symbol \(L(i,j)\) is excluded. A row-symbol edge lies in three triangles because exactly one column has the forbidden symbol; similarly for column-symbol edges. Thus all comparable-face maps are surjective with the indicated uniform fibres. A compatible boundary section specifies one vertex in each colour and has \(4^3=64\) choices. Exactly sixteen choices, the graph of \(L\), have no extension to the interior. This proves nonflabbiness and precisely locates the nonlocal obstruction.

**2. Exhaustion of Latin isotopy classes.** The independently rerunnable enumerator in `verify.py` constructs all order-four Latin squares by row permutations with distinct entries in every column, obtaining exactly 576. It then takes the orbits of the two indicated group tables under all independent permutations of the row, column and symbol labels. The resulting orbits have cardinalities 432 and 144; they are disjoint and their union is the entire enumerated set. Hence no additional case is possible, and all simplicial invariants reduce to those of the two group tables.

**3. Exact integral chains.** Orient every triangle as \([a_i,b_j,c_k]\) and each edge by increasing vertex label. The boundary of a triangle is
\[
\partial_2[a_i,b_j,c_k]=[b_j,c_k]-[a_i,c_k]+[a_i,b_j].
\]
Construct this forty-eight-by-forty-eight signed integer matrix by listing all allowed triples. Its exact Smith normal form has 37 unit nonzero diagonal entries for the cyclic table; for the Klein table it has 36 unit diagonal entries and one diagonal entry equal to two. The rank of \(\partial_1\) is eleven because the complete tripartite one-skeleton is connected. Both matrices have rank 37 over \(\mathbb Q\), so \(H_2=\ker\partial_2\cong\mathbb Z^{48-37}=\mathbb Z^{11}\). After quotienting \(\ker\partial_1\) by \(\operatorname{im}\partial_2\), the cyclic case has trivial first homology; the Klein case has exactly one cyclic summand of order two. The verifier reconstructs both matrices and computes their integer Smith forms, not a finite-field proxy.

**4. Exact fundamental-group presentations.** Contract the deterministic spanning tree produced by the lexicographic union-find algorithm on the forty-eight edges. The tree has eleven edges, leaving 37 oriented non-tree generators. Each allowed triangle supplies a relator equal to its three oriented boundary-edge words, with tree edges omitted. This is a standard cellular van Kampen presentation, with 37 generators and 48 relators. Eliminate a generator whenever it occurs exactly once in some cyclically reduced relator: solving that relation and substituting it in every other relator is an elementary Tietze transformation. Free reductions and deletion of cyclic inverse boundary pairs preserve the conjugacy class of the relator.

The provided deterministic computation performs 37 such eliminations in the cyclic case, leaving no generators and no nontrivial relations; therefore \(\pi_1(X_{\mathbb Z/4})=1\). In the Klein case it performs 36 eliminations, leaving one generator \(t\) with two identical relators \(t^{-2}\). Consequently \(\pi_1(X_{(\mathbb Z/2)^2})\cong\langle t\mid t^2\rangle\cong\mathbb Z/2\). The complete original presentations, deterministic elimination rules, and assertions on surviving words are reproducible in `verify.py`, so the finite reductions are exact proofs for these finite objects.

**5. Homotopy consequence.** In the cyclic case the connected two-dimensional CW complex is simply connected and has reduced integral homology only in degree two, of rank eleven. Choose eleven based two-sphere maps realizing a basis of the second homology via the Hurewicz isomorphism. Their wedge induces an integral homology equivalence between simply connected CW complexes, hence is a homotopy equivalence by Whitehead's theorem. In the Klein case the order-two first-homology summand precludes a wedge-of-spheres homotopy type, since all integral homology groups of a wedge of spheres are torsion-free.

## Verification
Run `python3 verify.py` with Python 3 and SymPy from the directory containing the script. The verifier independently enumerates all 576 Latin squares, evaluates both full isotopy orbits (432 and 144 members), constructs the signed cellular boundaries, obtains integral Smith diagonals, and constructs and exactly simplifies both finite van Kampen presentations. Its full exact output is in `verifier_output.txt`. The checks are exhaustive for order four; no enumeration at other orders or extrapolation to arbitrary Latin squares is asserted.

## Relationship to prior work
Ayzenberg and Khoroshavkina's 2026 generalized-inflation theorem proves top-dimensional sphere wedges under **global sheaf flabbiness**. The two examples here violate that hypothesis and show that apparently identical surjective local restriction systems need not even agree on torsion or fundamental group. An earlier Latin-array inflation result retains only the positive Latin triangles and the entire lower-dimensional skeleton; it obtains a wedge of circles at three colours and is not a result about the **complement** of Latin triangles. A previously classified order-four *partial-transversal complex* has sixteen cell-vertices and different face rules; its torus-versus-circle-wedge classification does not imply the present twelve-vertex, torsion-versus-simply-connected classification. The exact differences in objects and invariant implications are essential. The present result should not be confused with the elementary statement that the two isotopy classes exist; it concerns the integral topology of a new associated family of complexes.

## Limitations
The result is an exact finite classification at Latin order four. It does not classify larger orders, the entire homotopy type of the Klein case, or all globally nonflabby diagrams. The group-presentation reductions and integer Smith computations are supplied as reproducible exact finite certificates, not as machine-independent formal proofs. Literature and database searching cannot exclude an unindexed equivalent treatment under another terminology; no independent mathematical audit or priority certification has been performed.

## References
1. A. Ayzenberg and N. Khoroshavkina, *Homotopy types of finite étale spaces and generalized inflations*, arXiv:2602.08694v1, first publicly posted 2026-02-09, https://arxiv.org/html/2602.08694 ; especially Theorem 1.2, Sections 2.8, 5, and 7.
2. *Latin-array inflations exhibit lower homotopy despite unique local lifting*, 2026-10-11, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-latin-array-inflations-exhibit-lower-homotopy-despite-unique-loc--12e4d5a0c16a/RESULT.md .
3. *Complete homotopy classification of order-four Latin-square partial-transversal complexes*, 2026-10-25, https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-complete-homotopy-classification-of-order-four-latin-square-part--04e84911035b/RESULT.md .
4. D. Guichard, *Combinatorics and Graph Theory*, §4.4, Latin-square isotopy counts, https://math.libretexts.org/Bookshelves/Combinatorics_and_Discrete_Mathematics/Combinatorics_and_Graph_Theory_%28Guichard%29/04%3A_Systems_of_Distinct_Representatives/4.04%3A_Latin_Squares . The two isotopy classes are independently enumerated here.
