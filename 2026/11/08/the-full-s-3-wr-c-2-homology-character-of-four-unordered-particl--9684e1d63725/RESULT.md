# The full \(S_3\wr C_2\) homology character of four unordered particles on \(K_{3,3}\)

## Finding
Let \(G=K_{3,3}\) be the simple complete bipartite graph with two color classes of three vertices, and let \(B_4(G)\) be the space of four **unordered, pairwise distinct** points on its geometric realization. The full graph automorphism group is \(A=(S_3\times S_3)\rtimes C_2\), of order \(72\); the last factor interchanges the two color classes. Let \(T\), \(\varepsilon\), and \(W\) denote the trivial, sign, and two-dimensional standard rational representations of \(S_3\). For distinct irreducibles \(U,V\), put \(I(U,V)=\operatorname{Ind}_{S_3\times S_3}^{A}(U\boxtimes V)\). Let \(D^{\pm}(U)\) denote the two extensions of \(U\boxtimes U\) for which the color-class interchange acts by plus or minus the tensor-factor flip, respectively.

The complete rational homology representations are
\[
\begin{aligned}
H_1(B_4(G);\mathbb Q)&\cong D^-(W),\\
H_2(B_4(G);\mathbb Q)&\cong I(T,\varepsilon)\oplus 2I(\varepsilon,W)\oplus D^-(\varepsilon)\oplus 2D^-(W),\\
H_3(B_4(G);\mathbb Q)&\cong D^+(T)=\mathbb Q,
\end{aligned}
\]
with \(H_0\cong\mathbb Q\) trivial and no homology in degrees above three. In particular the fixed subspaces in degrees one and two vanish, whereas all of third rational homology is fixed by \(A\). The character in degree two, on nine conjugacy classes, is \((19,-5,1,-1,1,1,-5,1,1)\) in the explicitly reproducible class order below. The **representation refinements**, not the previously published Betti numbers, are the finding.

The full nine-class character data, with an automorphism written as the list of images of vertices \(0,1,2,3,4,5\) and vertices \(0,1,2\) in the first color class, are:

| Representative | Class size | \(\chi_1\) | \(\chi_2\) | \(\chi_3\) |
|:--|--:|--:|--:|--:|
| `(0,1,2,3,4,5)` | 1 | 4 | 19 | 1 |
| `(0,1,2,3,5,4)` | 6 | 0 | -5 | 1 |
| `(0,1,2,4,5,3)` | 4 | -2 | 1 | 1 |
| `(0,2,1,3,5,4)` | 9 | 0 | -1 | 1 |
| `(0,2,1,4,5,3)` | 12 | 0 | 1 | 1 |
| `(1,2,0,4,5,3)` | 4 | 1 | 1 | 1 |
| `(3,4,5,0,1,2)` | 6 | -2 | -5 | 1 |
| `(3,4,5,0,2,1)` | 18 | 0 | 1 | 1 |
| `(3,4,5,1,2,0)` | 12 | 1 | 1 | 1 |

## Assumptions and scope
We use ordinary singular homology of the collision-free unordered configuration space, not an ordered, sink, or discrete Morse complex. Coefficients for representations are \(\mathbb Q\); integral homology is used to control dimensions and action in the rank-one top degree. The action is induced by graph homeomorphisms, not by relabeling particles. All finite group representations are semisimple over \(\mathbb Q\). The first publicly verified foundational source for this archived graph-configuration direction is Farley–Sabalka's arXiv submission dated 2004-10-25; the equivariant refinement here is not attributed to that paper.

## Proof
**Chain model.** Enumerate the edges \(e_{ij}\) from \(i\in\{0,1,2\}\) to \(j\in\{3,4,5\}\). At each vertex \(v\), order its three incident halfedges \(h_{v,0},h_{v,1},h_{v,2}\), and write \(a_{v,k}=h_{v,k}-h_{v,0}\) for \(k\in\{1,2\}\). The integral reduced Świątkowski complex is the polynomial-edge module whose local factor at each vertex has degree-zero generator \(1\) and degree-one generators \(a_{v,1},a_{v,2}\), with at most one local factor chosen per vertex. Its differential satisfies \(\partial a_{v,k}=e(v,k)-e(v,0)\), the degree-one factors anticommute, and each edge variable and each local degree-one generator has particle weight one. By the functorial comparison theorem of An–Drummond-Cole–Knudsen, its weight-four subcomplex computes \(H_*(B_4(G);\mathbb Z)\) compatibly with every graph automorphism.

In degree \(k\in\{0,1,2,3,4\}\), the weight-four integral free chain group has rank \(\binom{6}{k}2^k\binom{12-k}{8}\), giving \((495,1980,2700,1440,240)\). Boundary columns are explicitly constructed from the above formula. Both consecutive boundary compositions are identically zero. Integer unit-pivot Schur eliminations, each a unimodular row/column operation, yield Smith invariant factors: \(\partial_1\): 494 units; \(\partial_2\): 1,481 units followed by one factor two; \(\partial_3\): 1,199 units; \(\partial_4\): 240 units, and all other invariant factors zero. In the second matrix, after 1,481 unit cancellations, the 82 remaining nonzero columns are equal or opposite and each has four entries of absolute value two; hence the residual matrix has rank one and nonzero Smith factor two. The other reduced matrices vanish. These facts prove, including integrality, that \(H_0\cong\mathbb Z\), \(H_1\cong\mathbb Z^4\oplus\mathbb Z/2\), \(H_2\cong\mathbb Z^{19}\), \(H_3\cong\mathbb Z\), and higher homology vanishes. These nonequivariant ranks are corroborations of prior literature, not novel assertions.

**First and top characters.** The natural map sending an infinitesimal particle trajectory to the sum of the paths traveled by all particles gives an \(A\)-equivariant map \(H_1(B_4(G);\mathbb Q)\to H_1(G;\mathbb Q)\). It is onto: each four-cycle of \(K_{3,3}\) can be traversed by one particle while the other three sit at distinct interior points of the complementary edge, which is disjoint from that cycle. Four-cycles span the four-dimensional graph cycle space. Since the source also has dimension four, the map is an isomorphism. Thus \(\chi_1(g)=\operatorname{tr}(g\mid C_1(G;\mathbb Q))-\operatorname{tr}(g\mid C_0(G;\mathbb Q))+1\), with graph edges oriented consistently from the first to the second color class.

To determine \(\chi_3\), exact boundary ranks establish that third integral homology is \(\mathbb Z\), so each automorphism acts by \(\pm1\). Over \(\mathbb F_{101}\), the computed kernel of \(\partial_3\) has dimension 241 and \(\operatorname{im}\partial_4\) has dimension 240. An explicit non-boundary cycle is extracted by column elimination; for every one of the 72 automorphisms, its image is congruent to itself modulo the 240-dimensional boundary image. This proves that each integral action is \(+1\), since \(-1\) is distinct from \(+1\) modulo 101. Thus \(\chi_3=1\) on the whole group.

**Second character by Lefschetz.** For each \(g\in A\), let \(\mathcal O_V(g)\) and \(\mathcal O_E(g)\) be its orbits on vertices and edges. At a vertex, let \(T_v\) be the rank-two span of halfedge differences. For vertex orbit \(O\) of length \(\ell_O\), let \(M_O\) be the return map \(g^{\ell_O}\) on \(T_v\). Since each vertex contributes at most one degree-one factor, and each edge contributes arbitrary nonnegative polynomial weight, the alternating character series of the entire reduced complex is
\[
\sum_{n\ge0}L_n(g)t^n=
\frac{\prod_{O\in\mathcal O_V(g)}(1-\operatorname{tr}(M_O)t^{\ell_O})}{\prod_{O\in\mathcal O_E(g)}(1-t^{|O|})}.
\]
The desired \(L(g)\) is the coefficient of \(t^4\). This formula was evaluated independently of direct basis enumeration for all 72 transformations, and all coefficients matched the signed direct chain traces. Equivariant Euler–Poincaré now gives \(\chi_2(g)=L(g)-1+\chi_1(g)+\chi_3(g)=L(g)+\chi_1(g)\). Conjugacy classes and representatives are exhaustively obtained from the 72-element permutation group, producing the table in the Finding section.

**Irreducibles.** The three rational irreducibles of \(S_3\) are \(T,\varepsilon,W\), with character values \(1\), permutation sign, and number of fixed points minus one. The nine irreducibles of \(S_3\wr C_2\) are the three induced modules \(I(U,V)\), for unordered distinct pairs, and the six flip extensions \(D^{\pm}(U)\). On elements preserving the color classes, their characters are respectively \(\chi_U(a)\chi_V(b)+\chi_V(a)\chi_U(b)\) and \(\chi_U(a)\chi_U(b)\). On elements interchanging classes, the induced characters vanish, while the flip-extension character is \(\pm\chi_U(ba)\). Their character norms are each 72 in the group order-72 inner product and they are mutually orthogonal. Exact inner products of the computed homology characters produce multiplicities \(1\) for \(D^-(W)\) in degree one; multiplicities \(1,2,1,2\) for \(I(T,\varepsilon),I(\varepsilon,W),D^-(\varepsilon),D^-(W)\) in degree two; and \(1\) for \(D^+(T)\) in degree three. All other multiplicities vanish. Orthogonality gives the invariant-subspace statements.

## Verification
The included programs use Python 3 standard library only. Running `python try_k33_4.py` enumerates the four-weight complex, verifies all boundary compositions, and computes modular ranks at primes 2, 3, and 101. Running `python k33_smith_assert.py` executes exact integer unit reductions and checks every claimed Smith invariant. Running `python try_k33_char.py` computes all 72 signed chain actions, derives a non-boundary top cycle, verifies top-homology action and records full character data in `k33four_chars.json`. Running `python k33_chaincheck.py` verifies chain-map commutation on **every** basis element in all positive degrees for five generators of the group. Running `python k33_lformula.py` separately evaluates the vertex/edge-orbit Lefschetz coefficient and agrees with all 72 direct traces. Running `python k33_irreps.py` calculates all nine irreducible inner products, conjugacy classes, and invariant dimensions. Output files record complete actual console checks, and `k33four_chars.json` gives all 72 permutations and values. All code and needed data are included alongside this document.

## Relationship to prior work
Farley and Sabalka (2004 preprint, 2005 journal article) provide foundational discrete Morse methods for unordered graph configurations. An, Drummond-Cole and Knudsen (2017 preprint) prove the functorial Świątkowski comparison used here. Most closely, Maciążek and Sawicki (2018 preprint; 2019 journal article), Section 5.5, **already derive the complete nonequivariant ranks** for \(B_4(K_{3,3})\), including 19 two-cycles and the exceptional one-dimensional third homology; they give geometric product-cycle generators and relations. These results, including the degree-three rank, are prior knowledge. Their analysis does not display or calculate the complete induced action of all 72 graph symmetries on the second and third homology, the nine-class character, or its irreducible decomposition. Ramos and Yun (2026) address representation stability for other graph/particle families, chiefly two-particle cases, not the present four-point automorphism character. The distinction is in the *representation under graph relabelings*, not in dimensions alone.

## Limitations
This determines rational representation isomorphism classes for exactly four **unordered** points on \(K_{3,3}\); it does not classify integral equivariant lattices, cup products, fundamental-group representations, equivariant homotopy types, or general graph families. The integral homology ranks and the product-cycle presentation are already published. These generators may provide an alternative route to deducing the representation; a complete exhaustive publication-priority guarantee is not claimed. The mod-101 top-cycle computation is used only after proving integral rank one and relies on its resulting possible signs \(\pm1\). All checks reported are reproducible mathematical computations and analyses, not third-party independent audit.

## References
1. D. Farley and L. Sabalka, *Discrete Morse theory and graph braid groups*, arXiv:math/0410539, first posted 2004-10-25, *Algebraic & Geometric Topology* 5 (2005), 1075–1109. https://arxiv.org/abs/math/0410539
2. B. H. An, G. C. Drummond-Cole and B. Knudsen, *Subdivisional spaces and graph braid groups*, arXiv:1708.02351, first posted 2017-08-08; especially the comparison theorem and reduced chain model. https://arxiv.org/abs/1708.02351
3. T. Maciążek and A. Sawicki, *Non-abelian Quantum Statistics on Graphs*, arXiv:1806.02846, first posted 2018-06-07; *Communications in Mathematical Physics* 371 (2019), 921–973, Section 5.5. https://doi.org/10.1007/s00220-019-03583-5
4. E. Ramos and C. He Yun, *Computing stable homology representations of graph configuration spaces*, arXiv:2606.13813, first posted 2026-06-11. https://arxiv.org/abs/2606.13813
