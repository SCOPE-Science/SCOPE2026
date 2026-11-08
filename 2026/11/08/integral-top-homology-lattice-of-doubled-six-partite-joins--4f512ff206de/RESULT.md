# Integral top-homology lattice of doubled six-partite joins

## Finding
Let \(A_1,\ldots,A_6\) be disjoint finite sets with \(n_i=|A_i|\geq2\). Put \(X=A_1*\cdots*A_6\), the five-dimensional simplicial join of six discrete vertex sets, and let \(Y=D^2(X)\) be its **double** in the sense of Lesh–Schreiner–Wahl: a vertex of \(Y\) is an edge of \(X\), and a set of such edges spans a simplex precisely when their endpoint sets are disjoint and have simplex union in \(X\).

For \(i<j\), write \(P_{ij}=A_i\times A_j\), and define the integral augmentation lattice
\[
L_{ij}=\ker\big(\mathbb Z[P_{ij}]\xrightarrow{\varepsilon}\mathbb Z\big),\qquad \varepsilon([a,b])=1.
\]
Let \(\mathscr M\) be the fifteen perfect matchings of the **six color labels** \(\{1,\dots,6\}\). The group \(\Gamma=\prod_{i=1}^{6}\mathfrak S(A_i)\) acts by permuting the vertices inside each color class. Then the following is an integral \(\Gamma\)-module isomorphism, canonical with respect to the six specified color classes:
\[
\boxed{H_2(Y;\mathbb Z)\cong_{\mathbb Z[\Gamma]}\bigoplus_{M\in\mathscr M}\ \bigotimes_{\{i,j\}\in M}L_{ij}.}
\]
Tensor factors are ordered by lexicographic color pairs to fix the chain orientation. Equivalently, this identifies all integral top-homology generators and their complete part-preserving symmetry action. In particular, \(H_2\) is free of rank
\[
b_2=\sum_{M\in\mathscr M}\prod_{\{i,j\}\in M}(n_i n_j-1).
\]
For \(g=(g_1,\ldots,g_6)\in\Gamma\), with \(f_i\) vertices fixed by \(g_i\), the character is
\[
\mathrm{tr}(g\mid H_2(Y;\mathbb Z))=\sum_{M\in\mathscr M}\prod_{\{i,j\}\in M}(f_if_j-1).
\]
The rank and character are consequences of the **integral lattice identification**, not separate novelty claims.

## Assumptions and scope
The join \(X\) contains exactly the subsets with at most one vertex in each \(A_i\). An edge type is an unordered pair of color indices \(e=\{i,j\}\), and the vertices in \(Y\) of type \(e\) form the discrete set \(P_e\) of size \(n_i n_j\). Two vertices of \(Y\) are adjacent exactly when their color types are disjoint, irrespective of which elements of their sets were chosen. A two-simplex consists of three vertices, with pairwise disjoint types covering the six color indices. No simplex has dimension greater than two. The action is \(\Gamma\), not the larger group permuting color classes of equal size; no larger equivariance is claimed.

## Proof
**1. An integral, invariant block decomposition.** Each two-simplex of \(Y\) specifies a unique perfect matching \(M\in\mathscr M\) of the six colors. More importantly, each one-simplex of \(Y\), which consists of two disjoint color types, also specifies a unique \(M\): the third pair is the two unused colors. Consequently, both the free integral two-chain group and the free integral one-chain group are direct sums indexed by \(\mathscr M\), and the signed simplicial differential \(\partial_2:C_2(Y;\mathbb Z)\to C_1(Y;\mathbb Z)\) respects these blocks. Each block is exactly the corresponding degree-two boundary of
\[
J_M= P_{e_1}*P_{e_2}*P_{e_3},\qquad M=\{e_1,e_2,e_3\},\quad e_1<e_2<e_3.
\]
The three sets \(P_e\) in this expression are discrete zero-dimensional complexes. Since \(Y\) has no three-simplices, \(H_2(Y;\mathbb Z)=\ker\partial_2\). Hence, *integrally and \(\Gamma\)-equivariantly*,
\[
H_2(Y;\mathbb Z)=\bigoplus_{M\in\mathscr M}\widetilde H_2(J_M;\mathbb Z).
\]
The decomposition uses no projection, averaging, choice of field, or semisimplicity assumption.

**2. Calculate each lattice without losing integrality.** The reduced augmented integral chain complex of a nonempty discrete vertex set \(P\) has its only reduced homology in degree zero, naturally equal to \(L(P)=\ker(\mathbb Z[P]\to\mathbb Z)\). The chain-level join tensor identity shifts total homological degree by two for three factors. The integral Künneth theorem has no Tor terms here, since the lattice factors are free. Thus
\[
\widetilde H_2(P_{e_1}*P_{e_2}*P_{e_3};\mathbb Z)\cong L_{e_1}\otimes_{\mathbb Z}L_{e_2}\otimes_{\mathbb Z}L_{e_3}.
\]
This identification is natural under every permutation of vertices *within* the three sets, and therefore under \(\Gamma\). Combine with step 1.

For a direct integral basis certificate, choose one distinguished vertex \(b_e\in P_e\) for each type \(e\). In the block for \(M=\{e_1,e_2,e_3\}\), the \((|P_{e_1}|-1)(|P_{e_2}|-1)(|P_{e_3}|-1)\) cycles
\[
([a_1]-[b_{e_1}])*([a_2]-[b_{e_2}])*([a_3]-[b_{e_3}]),
\qquad a_k\in P_{e_k}\setminus\{b_{e_k}\},
\]
are eight-term oriented integral two-cycles. They form a \(\mathbb Z\)-basis by the augmentation-kernel basis and join tensor identity. Thus the display is an isomorphism of actual integral lattices, not merely a rational character equality. The distinguished vertices are a device to display a basis; the lattice isomorphism itself is independent of these choices.

**3. Rank and trace.** The rank of \(L_{ij}\) is \(|P_{ij}|-1=n_i n_j-1\). A permutation of \(P_{ij}\) has \(f_i f_j\) fixed points, and the augmentation map splits after tensoring with \(\mathbb Q\), so its trace on \(L_{ij}\) is \(f_i f_j-1\). Tensor-product traces multiply and direct-sum traces add. This yields the displayed rank and character formulas. Both remain valid for all integer parameters within the stated scope.

**4. Already-covered nonequivariant consequences (not claimed as discoveries).** There are \(15\) color-pair types, \(45\) edges between them, and \(15\) color-perfect-matching triangles in the base complex \(\mathcal M(K_6)\). Each edge belongs to one triangle, so deleting all fifteen triangles with one free edge each gives a connected graph with \(15\) vertices, \(30\) edges and first Betti number \(16\). Moreover, the link in \(\mathcal M(K_6)\) of a type vertex is \(\mathcal M(K_4)\), a union of three disjoint edges, hence has two independent reduced degree-zero classes. The link of a type-edge is one vertex; the link of a type-triangle is empty. Applying the established inflation theorem of Björner–Wachs–Welker (Theorem 6.2) to the vertex inflation of \(\mathcal M(K_6)\) gives
\[
Y\simeq\left(\bigvee^{\,2\sum_{i<j}n_i n_j-14}S^1\right)\vee\left(\bigvee^{\,b_2}S^2\right).
\]
This nonequivariant homotopy classification, its Betti numbers and torsion-freeness are **already implied by that general theorem** and are included only to position the new integral symmetry-lattice result. The corresponding rational equivariant character is also within reach of their Corollary 8.5 and is not asserted as an independent discovery.

## Verification
A standalone Python 3 standard-library program `verify.py` reconstructs all faces directly from six color classes, constructs the signed \(\partial_2\) matrix, performs modular Gaussian elimination at primes \(2,3\) on its feasible test instances, explicitly tests all eight signed faces of each exhibited integral generator, and checks distinct unit pivots. It also builds actual vertex permutations, determines their signed traces on every simplicial chain group, computes diagonal coefficients of the induced action on the integral cycle basis, and checks the stated trace. All checks completed successfully with `ALL_VERIFY_OK` and `ALL_ACTIONS_OK`.

For six two-element classes, the independent reconstruction gives \((f_0,f_1,f_2)=(60,720,960)\), \(\operatorname{rank}\partial_2=555\), \(b_1=106\), \(b_2=405\). A single within-class transposition has trace \(-135\) on \(H_2\). Tests also include the profile \((2,3,2,2,2,2)\), with \(675\) explicit integral top cycles and direct three-cycle and transposition action checks. Run `python3 verify.py` and compare with `verify_output.txt`. These finite tests corroborate, but do not replace, the general chain argument.

## Relationship to prior work
Lesh–Schreiner–Wahl (arXiv:2506.10436, first publicly submitted June 12, 2025) introduced the doubling operation, explicitly identifying the simplex case with graph matching complexes, and proved general connectivity bounds; the available full paper does not state this six-partite top integral symmetry-lattice decomposition. Björner–Wachs–Welker, *Poset fiber theorems* (2005), Theorem 6.2 and Corollary 6.3, **already cover the nonequivariant wedge decomposition and integral ranks** via vertex inflation. Their Corollary 8.5 provides an equivariant homology decomposition *over a field* in its stated hypotheses, strongly overlapping with any proposed rational character result. Those stronger prior implications have been taken out of the originality claim. Ayzenberg–Khoroshavkina (arXiv:2602.08694, February 9, 2026) generalize inflation homotopy decompositions to finite étale spaces; this does not give the present canonical integral top-cycle block lattice. The new assertion is precisely the integral \(\Gamma\)-equivariant identification in the boxed formula and its explicit cycle-basis construction.

## Limitations
Only the six-color partition and its within-class permutation action are covered. No decomposition of the integral first-homology representation is claimed. The theorem does not assert a \(\Gamma\)-equivariant splitting of the full homotopy type and does not classify arbitrary \(r\)-tuplings. Rational representation data can follow from existing inflation theory; its presence here is explanatory rather than novel. A logically equivalent integral lattice decomposition may exist in unindexed literature; the search cannot prove absolute uniqueness.

## References
1. Kathryn Lesh, Bridget Schreiner, and Nathalie Wahl, *The double of a simplicial complex*, arXiv:2506.10436, initial public version 2025-06-12. https://arxiv.org/abs/2506.10436
2. Anders Björner, Michelle L. Wachs, and Volkmar Welker, *Poset fiber theorems*, Transactions of the American Mathematical Society **357** (2005), 1877–1899, especially Theorem 6.2, Corollaries 6.3 and 8.5. https://doi.org/10.1090/S0002-9947-04-03496-8
3. Anton Ayzenberg and Nadya Khoroshavkina, *Homotopy types of finite étale spaces and generalized inflations*, arXiv:2602.08694, 2026-02-09. https://arxiv.org/abs/2602.08694
