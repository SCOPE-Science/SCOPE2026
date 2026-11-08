# Complete hyperoctahedral character of four-cube independence homology

## Finding

Let \(Q_4\) be the graph on the sixteen vectors \(\mathbb F_2^4\), adjacent when they differ in one coordinate, and let \(X=\operatorname{Ind}(Q_4)\). The graph automorphism group \(B_4=\mathbb F_2^4\rtimes S_4\) has order \(384\). It acts on \(X\) and its reduced homology. The previously established nonequivariant homotopy type is \(X\simeq\bigvee^7S^3\); this is not the new claim.

Write \(T=\mathbb F_2^4\), write \(V\) for the three-dimensional standard rational representation of \(S_4\) (the sum-zero subspace of \(\mathbb Q^4\)), and write \(\varepsilon(p)=\operatorname{sgn}(p)\). Define a four-dimensional rational \(B_4\)-module \(M\) on basis \(e_1,\ldots,e_4\) by
\[
 t\cdot e_i=(-1)^{\sum_{j\ne i}t_j}e_i,\qquad
 p\cdot e_i=\operatorname{sgn}(p)e_{p(i)},
\]
for \(t\in T\) and \(p\in S_4\). Then the **complete rational homology representation** is
\[
 \widetilde H_3(X;\mathbb Q)\cong
 (\varepsilon\otimes V)_{\mathrm{infl}}\oplus M,
\]
where both summands are irreducible over \(\mathbb Q\), of dimensions three and four. All other reduced homology groups vanish, and \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z^7\).

For an automorphism \(g=(t,p)\), acting by \(v\mapsto p(v)+t\), put \(F(p)=\{i:p(i)=i\}\). Its complete degree-three character is
\[
 \operatorname{tr}(g\mid\widetilde H_3(X;\mathbb Q))
 =\operatorname{sgn}(p)\left(|F(p)|-1
 +\sum_{i\in F(p)}(-1)^{\sum_{j\ne i}t_j}\right).
\]
Thus the translation-fixed subspace has dimension three; the other four dimensions comprise the distinct weight-three Fourier characters of \(T\). No nonzero rational homology class is fixed by the entire \(B_4\).

## Assumptions and scope

The independence complex includes the empty face and contains exactly the subsets of \(\mathbb F_2^4\) with no pair at Hamming distance one. Integral homology is ordinary reduced simplicial homology. The automorphisms considered are **all** graph automorphisms, not merely a geometric subgroup. There are no limiting parameters or unverified infinite extrapolations: the object has sixteen vertices and the acting group has \(384\) elements. A four-by-four fully periodic square grid \(C_4\square C_4\) is graph-isomorphic to \(Q_4\), since \(C_4=K_2\square K_2\).

## Proof

**1. Exhaustive homotopy certificate.** Index cube vertices by integers \(0,\ldots,15\), with bitwise Hamming adjacency. Enumerating all nonzero sixteen-bit face masks and rejecting a mask whenever it contains a pair differing in exactly one bit gives \(742\) nonempty simplices. The face counts in dimensions zero through seven are, respectively, \((16,88,208,228,128,56,16,2)\).

At successive pivots \(v=0,\ldots,15\), pair every still-unmatched face \(a\) omitting \(v\) with \(a\cup\{v\}\) whenever the latter is still unmatched; remove both. This gives \(367\) disjoint matched pairs, with counts \((176,134,10,4,5,5,13,4,0,3,4,3,3,1,1,1)\). The eight unmatched masks are \(1,1680,2400,10370,17028,24600,33064,33096\): exactly one vertex and seven three-simplices. These counts can be reconstructed from the graph definition without external input.

To prove acyclicity rather than infer it from the counts, the included verifier enumerates **every** \(2816\) Hasse cover between nonempty faces, directs each cover from the larger to the smaller face except for reversed matched pairs, and performs a full topological sort of the directed graph. It visits all \(742\) faces. This is a finite exhaustive acyclicity certificate: a directed cycle would prevent a full topological sort. The discrete Morse theorem gives a CW complex with one zero-cell, seven three-cells, and no other cells, hence \(X\simeq\bigvee^7 S^3\). In particular the only nonzero reduced integral homology is free of rank seven in degree three.

**2. Group and character.** Each cube automorphism is of the form \(g(v)=p(v)+t\), because the image of the zero vertex and the permutation of its four neighbors determine an automorphism uniquely. All \(16\cdot24=384\) such maps preserve graph adjacency. For a nonempty simplex \(\sigma\) fixed *setwise* by \(g\), its contribution to the reduced simplicial Lefschetz number is \((-1)^{\dim\sigma}\) times the sign of the permutation induced by \(g\) on its ordered vertices. Include the empty simplex's contribution \(-1\). Only degree-three reduced homology survives, so \(\operatorname{tr}(g\mid\widetilde H_3)=-\widetilde L(g)\). The verifier evaluates this signed sum directly for all \(384\) automorphisms on all \(742\) faces, and independently checks each against the displayed character formula. The resulting character takes values \(-3,-1,1,3,5,7\) with respective multiplicities \(24,161,188,6,4,1\) among the group elements.

**3. Identification of the irreducible summands.** Let \(\chi\) denote that character and let \(T\) be the normal translation subgroup. The exact Fourier multiplicity formula
\[
 m_a=\frac1{16}\sum_{t\in T}\chi(t,1)(-1)^{\langle a,t\rangle}
\]
gives \(m_0=3\), \(m_a=1\) if \(a\) has Hamming weight three, and \(m_a=0\) otherwise. The \(T\)-invariant three-dimensional summand is therefore preserved by \(S_4\). Its character on \(p\in S_4\), computed by averaging \(\frac1{16}\sum_t\chi(t,p)\), is \(\operatorname{sgn}(p)(|F(p)|-1)\), the character of \(\varepsilon\otimes V\). On the remaining four weight-three translation-character lines, \(S_4\) permutes the weights transitively. Their character agrees on all group elements with the explicit module \(M\) above. Maschke's theorem and character uniqueness over characteristic zero give the claimed rational module isomorphism. The three-dimensional inflated standard module is irreducible; \(M\) is irreducible since its four distinct one-dimensional \(T\)-weight spaces are permuted transitively by \(S_4\). The first has no \(S_4\)-fixed vector and the second has no \(T\)-fixed vector, proving absence of \(B_4\)-invariants.

## Verification

Run `python3 verify_q4_character.py` from a directory containing the standalone script. It requires only Python's standard library and recomputes all face masks, pivot pairs, oriented Hasse covers, \(384\) signed Lefschetz traces and the translation Fourier multiplicities. The recorded `verification_output.txt` contains the actual output. The verifier and recorded output were also extracted from the final embedded JSONL row and replayed, with identical results.

The complete certificate is the reconstruction-and-check algorithm, not merely a list of ranks: the directed acyclicity test visits every face and the character test compares all group elements. It proves this finite case only.

## Relationship to prior work

Bousquet-Mélou, Linusson and Nevo [1] develop discrete-Morse methods for square-grid independence complexes and analyze open and cylindrical boundaries; their introduction says the toric case lies beyond their main homotopy methods. Jonsson [2] treats periodic grids through cross-cycles and explicitly notes that these need not span full homology. Adamaszek [3] studies independence homology of lattice families and cross-cycles, but neither provides this \(B_4\)-character. A publicly posted computation [4] establishes exactly the seven-sphere homotopy type of this sixteen-vertex complex; the present proof rechecks that prerequisite independently, and the **new** assertion is its full automorphism-group action with rational irreducible splitting and translation Fourier support. The homotopy type alone has no information about this character. Results on hypercube Čech nerves, total-cut complexes or higher-independence complexes describe different simplicial face conditions and do not imply this representation merely because they use the same graph.

## Limitations

This classifies rational representations, not the isomorphism class of the full integral \(\mathbb Z[B_4]\)-lattice or any equivariant homotopy type. The no-torsion statement concerns abelian integral homology only. It makes no claim for higher-dimensional cubes or larger toroidal grids. Existing literature indexed under different terminology could contain an equivalent representation calculation; absence from consulted sources is not proof of global publication priority. There has been no independent mathematical audit.

## References

[1] M. Bousquet-Mélou, S. Linusson and E. Nevo, *On the independence complex of square grids*, arXiv:math/0701890, first posted 2007-01-30; published in J. Algebraic Combin. 27 (2008), 423–450. https://arxiv.org/abs/math/0701890

[2] J. Jonsson, *Certain Homology Cycles of the Independence Complex of Grid Graphs*, publicly dated author preprint 2008-10-19, later published Discrete Comput. Geom. 43 (2010), 927–950. https://people.kth.se/~jakobj/doc/papers/crosstorus.pdf

[3] M. Adamaszek, *Special cycles in independence complexes and superfrustration in some lattices*, arXiv:1109.4914, first posted 2011-09-22. https://arxiv.org/abs/1109.4914

[4] *The four-cube independence complex is a wedge of seven three-spheres*, publicly posted research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-four-cube-independence-complex-is-a-wedge-of-seven-three-sph--9947aaad144c
