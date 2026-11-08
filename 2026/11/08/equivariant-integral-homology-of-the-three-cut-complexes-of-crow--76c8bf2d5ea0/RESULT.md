# Equivariant integral homology of the three-cut complexes of crown graphs

## Finding

For each integer \(n\geq5\), let \(C_n\) be the crown graph with vertices \(a_i,b_i\), \(1\leq i\leq n\), and edges \(a_i b_j\) precisely for \(i\ne j\). Its **ordinary three-cut complex** \(K_n=\Delta_3(C_n)\) is the complex whose facets are the complements of disconnected three-vertex induced subgraphs. Put
\[
B_n=1+\frac{n(n-5)(n-3)(n-2)}4.
\]
Then the complete reduced integral homology is
\[
\widetilde H_j(K_n;\mathbb Z)\cong
\begin{cases}
\mathbb Z^{B_n},&j=2n-6,\\
\mathbb Z^n,&j=2n-4,\\
0,&\text{otherwise}.
\end{cases}
\]
The complex is pure of dimension \(2n-4\), exactly \((2n-7)\)-connected, and **not shellable**. In particular the two nonzero reduced-homology degrees have a missing intervening degree. For \(n=5\) the ranks are \(1\) in degree \(4\) and \(5\) in degree \(6\); for \(n=6\) they are \(19\) in degree \(6\) and \(6\) in degree \(8\).

There is a natural faithful graph automorphism group \(G=S_n\times C_2\), where \(\sigma\in S_n\) acts simultaneously on the indices and \(\tau\in C_2\) exchanges the two vertex classes. In degree \(2n-4\), the integral \(G\)-module is the permutation lattice \(\mathbb Z^n\) on the indices, with \(\tau\) acting by the scalar \((-1)^{n+1}\). Thus its rational character is
\[
\chi_{2n-4}(\sigma)=f,\qquad
\chi_{2n-4}(\tau\sigma)=(-1)^{n+1}f,
\]
where \(f\) is the number of fixed indices of \(\sigma\).

The *complete rational character in the other nonzero degree* has the following closed form. Let \(f,t,u\) denote the numbers of cycles of lengths one, two and four in \(\sigma\). Define \(h=1-\lambda_0+\lambda_1-\lambda_2+\lambda_3\). For \(\sigma\) without a class swap, set
\[
\begin{aligned}
\lambda_0&=2f,\\
\lambda_1&=2f(f-1)-2t,\\
\lambda_2&=f(f-1)(f-2)-2tf,\\
\lambda_3&=\binom f2\binom{f-2}2-2t\binom f2+t(t-1).
\end{aligned}
\]
For \(\tau\sigma\), instead set
\[
(\lambda_0,\lambda_1,\lambda_2,\lambda_3)
=\left(0,-2t,0,4\binom t2-2u\right).
\]
Here \(\binom ab=0\) when \(a<b\), including negative upper indices. The characters are
\[
\boxed{\chi_{2n-6}(\sigma)=h(\sigma),\quad
\chi_{2n-6}(\tau\sigma)=(-1)^n h(\tau\sigma).}
\]
These expressions determine both nonzero rational representations of \(G\) for every \(n\ge5\). No equivariant homotopy decomposition or integral lattice decomposition in degree \(2n-6\) is asserted.

## Assumptions and scope

All graphs are finite, undirected, simple and labeled as above. The three-cut convention is that a facet is the complement of a **disconnected** induced triple, without requiring an edgeless triple. Homology and cohomology are reduced where indicated. The \(C_2\) generator exchanges every \(a_i\) with \(b_i\); it commutes with simultaneous index permutations. This statement begins at \(n=5\): the smaller \(n=4\) crown is the cube and has a distinct already studied cut-complex boundary case. Character formulas concern ordinary rational representations; the top-degree integral lattice is explicitly identified.

## Proof

**1. The exact Alexander dual.** Set \(Y_n=K_n^\vee\), the combinatorial Alexander dual relative to all \(2n\) vertices. A set \(S\) lies in \(Y_n\) if and only if every three-element subset of \(S\) induces a connected subgraph of \(C_n\). Since the crown graph is bipartite, no member of \(Y_n\) contains three vertices of either class. A three-element face having two vertices of one class and one of the other is present exactly when all three indices are distinct. A four-element face has two vertices of each class and is present exactly when its four indices are distinct. Every one- and two-element subset is automatically a face, including the \(n\) nonedge pairs \(\{a_i,b_i\}\); none of those \(n\) special edges belongs to any larger face.

Remove the interiors of the \(n\) special edges to obtain a subcomplex \(X_n\subset Y_n\). Its simplices are pairs of disjoint index sets \((I,J)\) satisfying \(|I|\le2\), \(|J|\le2\); its vertices carry the two colors \(a\) and \(b\). Thus \(X_n\) is precisely the multiple chessboard complex with \(n\) columns, two rows of capacities \((2,2)\), and column capacity one. This identification includes the empty face, every edge and all three- and four-vertex faces; it is an isomorphism of simplicial \(G\)-complexes.

**2. Integral homology of the dual.** The multiple chessboard shellability theorem of Jojić, Vrećica and Živaljević, Theorem 4.4 of arXiv:1412.0386, applies at \(n\ge2+2+2-1=5\). Consequently \(X_n\) is pure shellable of dimension three, hence homotopy equivalent to a wedge of three-spheres (possibly none), with free integral homology concentrated in degree three. Its numbers of nonempty faces by dimension are
\[
\begin{aligned}
f_0&=2n,& f_1&=2n(n-1),\\
f_2&=n(n-1)(n-2),& f_3&=\binom n2\binom{n-2}2.
\end{aligned}
\]
Euler characteristic gives the wedge rank \(1-(f_0-f_1+f_2-f_3)=B_n\). Adding the \(n\) special one-cells does not alter the higher-dimensional chain groups or differentials. Since \(X_n\) is connected and \(H_1(X_n;\mathbb Z)=0\), the long exact sequence for \((Y_n,X_n)\) gives
\[
H_1(Y_n;\mathbb Z)\cong H_1(Y_n,X_n;\mathbb Z)
\cong\mathbb Z^n,
\qquad H_3(Y_n;\mathbb Z)\cong\mathbb Z^{B_n},
\]
and vanishing reduced homology in the remaining degrees. These are torsion-free groups. The relative basis is given canonically by the oriented omitted-diagonal edges \(a_i\to b_i\).

**3. Alexander duality and connectivity.** Combinatorial Alexander duality gives, integrally,
\[
\widetilde H_j(K_n;\mathbb Z)\cong
\widetilde H^{2n-j-3}(Y_n;\mathbb Z).
\]
The preceding computation and universal coefficients yield precisely the two displayed nonzero reduced-homology groups. Every subset of at most \(2n-5\) vertices lies in \(K_n\): its complement has at least five vertices and therefore includes three from the same bipartition class, a disconnected triple. Thus \(K_n\) contains the full \((2n-6)\)-skeleton of the \((2n-1)\)-simplex, giving \((2n-7)\)-connectivity. Since \(B_n\ge1\), degree \(2n-6\) is nonzero, so this connectivity is sharp. A pure shellable complex has reduced homology only in its top dimension; the lower nonzero group rules out shellability.

**4. Equivariance in top degree.** The quotient relative chain group \(C_1(Y_n,X_n;\mathbb Z)\) has oriented basis \([a_i,b_i]\). Simultaneous index permutations permute this basis; the class swap reverses all orientations. The long exact sequence identifies this *integral* module with \(H_1(Y_n;\mathbb Z)\). Equivariant combinatorial Alexander duality contributes the sign of the permutation on all \(2n\) vertices. Simultaneously permuting both classes is even, whereas \(\tau\) is the product of \(n\) transpositions. The integral top-homology lattice is therefore the index permutation lattice, with the class swap multiplying by \((-1)^n(-1)=(-1)^{n+1}\).

**5. Equivariance in the lower degree.** On the three-dimensional shellable complex \(X_n\), ordinary homology is only \(H_0\cong\mathbb Q\) and \(H_3\cong\mathbb Q^{B_n}\). For \(g\in G\) let \(\lambda_j(g)\) be the signed trace of the induced action on oriented simplicial \(j\)-chains. The Hopf trace identity yields
\[
\operatorname{tr}(g\mid H_3(X_n;\mathbb Q))
=1-\lambda_0(g)+\lambda_1(g)-\lambda_2(g)+\lambda_3(g).
\]
For an index permutation, a fixed oriented face consists of fixed vertices and pairs of vertices transposed in a two-cycle; their signs give exactly the four formulas displayed in the Finding. For a color-swapping element, fixed faces must have equal numbers of both colors. There are no fixed vertices or triangles, the two cross-edges supplied by every index two-cycle each contribute \(-1\), and the fixed tetrahedra consist of four choices from each pair of distinct two-cycles (positive orientation) or two opposite-index choices from each four-cycle (negative orientation). Hence the color-swapping formulas. These exhaust all fixed face types because a face has at most two vertices of either color.

The integral identification \(H_3(Y_n)\cong H_3(X_n)\) is equivariant. Applying equivariant Alexander duality again gives the orientation-sign twist \((-1)^n\) under the class swap and no sign twist under simultaneous permutations. Rational dualization has the same character as the original rational representation, completing the stated formulas for degree \(2n-6\).

## Verification

`VERIFY.py` independently builds both the multiple chessboard complex and its extra-edge enlargement, checks the dual face predicate by exhaustively examining all subsets for \(n=4,5,6\), checks exact mod-two boundary ranks for \(4\le n\le8\), and compares the closed signed-trace formula with direct oriented-simplex traces on every permutation for \(n=5,6\) and deterministic samples for \(n=7,8\). Its execution output is `VERIFY_OUTPUT.txt`. The finite tests corroborate the argument but do **not** replace the published shellability theorem or the general combinatorial and equivariant-duality proof. The latter supplies the integral infinite-family result. No independence from published literature is certified by software.

## Relationship to prior work

Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram and Xue introduced and studied ordinary cut complexes in arXiv:2304.13675 (first posted April 26, 2023). Their Theorem 7.4 determines equivariant homology for complete bipartite graphs; their Section 7.3 treats prisms over cliques. The matching-deleted bipartite crown has a different connectivity-triple hypergraph from both families; these theorems do not state its two-degree homology or its simultaneous permutation and part-flip characters.

The *ordinary, nonequivariant homotopy type* of the associated multiple chessboard subcomplex \(X_n\) is already covered by the shellability theorem in arXiv:1412.0386; **that theorem is a premise, not a new claim here**. The independent 2026 paper arXiv:2610.37827 announces general homotopy classifications of multiple chessboard complexes, strengthening the background. It is not treated as novel to determine only the homology of \(X_n\). The claim here concerns the original crown **cut** complex, its integral homology in two separated dimensions, its sharp connectivity/non-shellability, and its full \(S_n\times C_2\) rational homology characters. Those characteristics are not supplied by a homotopy type of \(X_n\) alone.

Related indexed computations include the cube three-cut complex (the smaller \(n=4\) crown), and three-cut complexes of rook graphs. They have distinct underlying graphs or parameter ranges and do not state the formula for the present full family.

## Limitations

The result asserts integral homology groups and a top-degree integral symmetry lattice, **not** the full homotopy type of \(K_n\), not an integral decomposition of its lower-degree symmetry lattice, and not equivariant homotopy equivalence. The 2026 chessboard manuscript was available in indexed abstract form but its full text could not be accessed for direct line-by-line comparison; an unindexed independent character computation remains a possible priority risk. The verification program tests finitely many cases; the infinite claim rests on the cited, applicable shellability theorem and on the written duality and fixed-face arguments. Independent mathematical validation is not performed.

## References

1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first posted 2023-04-26), https://arxiv.org/abs/2304.13675 .
2. D. Jojić, S. T. Vrećica, R. T. Živaljević, *Multiple Chessboard Complexes and the Colored Tverberg Problem*, arXiv:1412.0386 (first posted 2014-12-01), Theorem 4.4, https://arxiv.org/abs/1412.0386 .
3. I. Limonchenko, S. Yu, *Homotopy Types and Torsion in Homology of Generalized Chessboard Complexes*, arXiv:2610.37827 (first posted 2026-10-27; indexed abstract consulted), https://arxiv.org/abs/2610.37827 .
