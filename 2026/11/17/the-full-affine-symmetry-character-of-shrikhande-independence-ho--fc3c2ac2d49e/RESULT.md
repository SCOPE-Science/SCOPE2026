# The full affine symmetry character of Shrikhande independence homology

## Finding
Let \(S\) be the Shrikhande graph on \(T=(\mathbb Z/4\mathbb Z)^2\), with two vertices adjacent when their difference belongs to
\[
D=\{(\pm1,0),(0,\pm1),(1,1),(-1,-1)\}.
\]
Let \(X=\operatorname{Ind}(S)\). The entire graph automorphism group is \(G=T\rtimes D_6\) of order \(192\), where \(D_6\) is the dihedral group of order \(12\). The rational representation \(\widetilde H_2(X;\mathbb Q)\) has dimension \(23\), and its **complete character on every automorphism** is the explicit \(192\)-entry table in `character_table.csv`, with a self-contained formula and proof below. Every other reduced rational homology group vanishes.

The restriction to translations has the following structural decomposition:
\[
\boxed{\widetilde H_2(X;\mathbb Q)|_T\cong
\mathbb Q[T]\oplus\mathbb Q\oplus W_{1,1}\oplus W_{1,2}\oplus W_{2,1}.}
\]
Here \(\mathbb Q[T]\) is the regular rational translation module; \(\mathbb Q\) is trivial; and \(W_{p,q}\) is the two-dimensional rational module whose complexification is the sum of the characters \((a,b)\mapsto i^{pa+qb}\) and \((a,b)\mapsto i^{-pa-qb}\). Thus the \(T\)-fixed part has dimension \(2\). With
\[
r=\begin{pmatrix}0&1\\3&1\end{pmatrix},\qquad
s=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]
acting linearly modulo \(4\), the action on the \(T\)-fixed part splits as two lines: on both \(s\) acts by \(-1\), while on the first and second \(r\) acts by \(+1\) and \(-1\), respectively. In particular, this representation has no \(G\)-fixed vectors.

Consequently the finite symmetry quotients have **different rational cohomology rings**:
\[
\boxed{H^*(|X|/T;\mathbb Q)\cong H^*(S^2\vee S^2;\mathbb Q),\qquad
H^*(|X|/G;\mathbb Q)\cong\mathbb Q.}
\]
These ring identifications do not assert homotopy equivalences of the quotients. As a useful comparison, the \(4\times4\) rook graph has just one translation-invariant rational second-homology class under the same coordinatewise translation group; its distinct nonequivariant homotopy type and general chessboard-group representations are already known.

## Assumptions and scope
All complexes are finite abstract simplicial complexes, with the empty simplex included for reduced chains. The graph has vertices \((a,b)\) represented by \(4a+b\), with \(a,b\in\{0,1,2,3\}\). A simplex of \(X\) is any independent vertex set. For a matrix \(A=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\) with entries modulo \(4\), and a translation \(t=(u,v)\), the affine permutation \(g_{A,t}\) sends \(x\mapsto Ax+t\). The allowed twelve matrices are precisely those satisfying \(A(D)=D\); all their entries are listed in `character_table.csv`. The table has one row per \((A,t)\), sorted lexicographically by \((a,b,c,d,u,v)\), and the integer `trace` is the complete rational homology character at that element.

For an independent face \(F\) fixed setwise by \(g\), orient \(F\) by increasing labels and let \(\operatorname{sgn}(g|_F)\) be the sign of its induced permutation. Equivalently, let \(\mathcal O(g)\) be the disjoint cycles of the permutation on all \(16\) vertices, and say a union of cycles is independent if it is an independent subset in \(S\). The full character is therefore also given without a lookup table by
\[
\boxed{\chi(g)=-1+
\sum_{\substack{\varnothing\ne J\subseteq\mathcal O(g)\\
\bigcup_{C\in J}C\text{ is independent}}}(-1)^{|J|-1}.}
\]
This formula applies to all \(192\) affine automorphisms, including elements not lying in the translation subgroup.

## Proof
**Automorphism group.** Exactly twelve linear maps of \(T\) preserve \(D\), and all sixteen translations preserve the Cayley adjacency; hence they give \(192\) distinct automorphisms. The six neighbors of \((0,0)\) induce a cycle \(C_6\). The other nine nonzero vertices have pairwise distinct intersections (each a two-element set) with these six neighbors. An automorphism fixing \((0,0)\) and its six neighbors pointwise must therefore fix every vertex. Its vertex stabilizer injects into the order-twelve automorphism group of \(C_6\), giving at most \(16\cdot12=192\) automorphisms. Thus the affine list is complete. The displayed \(r,s\) satisfy \(r^6=s^2=1\) and \(srs=r^{-1}\).

**Homology degree.** The graph has exactly \(16\) independent vertices, \(72\) independent pairs, \(96\) independent triples and \(16\) independent quadruples, with no larger independent faces. A complete acyclic discrete-Morse matching pairs \(88\) of the \(200\) nonempty faces, leaving one critical vertex and \(23\) critical two-cells. Its precise greedy vertex-toggling construction and an exhaustive acyclicity check of all \(496\) face-poset incidences are implemented in `verify.py`. By the finite discrete-Morse theorem, \(X\simeq\bigvee^{23}S^2\). This nonequivariant fact has been computed previously; it is established here solely to justify the homological concentration used in the equivariant calculation. Exact mod-two boundary ranks \((1,15,57,16)\) independently corroborate the reduced Betti numbers but are not substituted for the integral Morse proof.

**Complete character.** On reduced simplicial chains, the augmented degree-minus-one chain contributes trace \(-1\). In each nonnegative degree, a fixed face contributes the signed permutation of its ordered vertices. Since only \(\widetilde H_2(X;\mathbb Q)\) is nonzero, the alternating trace identity gives the character. Every invariant face is a union of vertex cycles of \(g\). If such a face is a union of \(k\) cycles, the product of its homological alternating sign and its orientation sign is \((-1)^{k-1}\); this yields the boxed fixed-cycle formula. The standalone verifier applies two different algorithms to all \(192\) elements: signed fixed-face traces and independent-cycle enumeration. All results agree exactly with `character_table.csv`. Thus the table specifies the character of the full rational representation, not just its dimension or a subgroup restriction.

**Translation decomposition.** Every independent quadruple is a coset of one of the four order-four subgroups
\[
\begin{aligned}
H_0&=\{(0,0),(2,0),(0,2),(2,2)\},\\
H_1&=\langle(1,2)\rangle,\quad
H_2=\langle(2,1)\rangle,\quad
H_3=\langle(1,3)\rangle.
\end{aligned}
\]
The sixteen cosets are distinct and exhaust the independent quadruples. For the identity translation, the reduced Euler trace is \(-1+16-72+96-16=23\). For each of the three nonzero order-two translations there are eight invariant independent pairs and eight invariant quadruples, contributing \(-1+8-8=-1\). For the six generators of \(H_1,H_2,H_3\), a translation fixes exactly four independent quadruples and no smaller nonempty independent face, giving trace \(3\). The other six order-four translations fix no nonempty face, giving trace \(-1\). Taking the exact discrete Fourier transform on \(T\) yields the multiplicity matrix, with \((p,q)\) indexing the row and column,
\[
\left(\begin{array}{rrrr}
2&1&1&1\\1&2&2&1\\1&2&1&2\\1&1&2&2
\end{array}\right).
\]
Its entries consist of one copy of every complex character, an extra trivial character, and three conjugate pairs. This is exactly the displayed rational \(T\)-module decomposition.

**The remaining symmetry and quotients.** Average the complete character over the normal translation subgroup to obtain the character on \(\widetilde H_2(X;\mathbb Q)^T\): for \(A\in D_6\) its value is \(16^{-1}\sum_{t\in T}\chi(g_{A,t})\). For the generators \(r,s\) above, the twelve values are \(1+(-1)^j\) at \(r^j\) and \(-1-(-1)^j\) at \(sr^j\), for \(0\le j<6\). Therefore this two-dimensional module is the sum of the two specified sign lines, neither of which is invariant under \(s\). A finite simplicial group action becomes without inversions after barycentric subdivision, so rational cochains on its quotient compute the invariant cochains. Averaging over the finite group makes invariants exact. It follows that rational quotient cohomology is the invariant cohomology upstairs, proving both ring statements. The ring product of two degree-two classes vanishes because the upstairs complex has no cohomology in degree four.

## Verification
`verify.py` and `character_table.csv` are provided together. Run `python3 verify.py` in their directory with ordinary Python 3. No external libraries, data downloads or symbolic algebra systems are required. The output must match `verification_output.txt`, ending in `FULL_SHRIKHANDE_CHARACTER_VERIFIED_192_PASS`. The program exhaustively enumerates all \(2^{16}\) subsets, all \(192\) affine automorphisms, all fixed simplicial traces by two methods, the acyclic matching and topological sort, the Fourier multiplicities, and the fixed-subgroup character. It separately checks the rook comparison, which is not a new novelty assertion.

## Relationship to prior work
The Shrikhande graph and its full symmetry group are classical. Peeters (1997, with earlier 1993 research-memorandum version) describes four-cocliques of the graph, including two geometric types. The classification of maximal independent sets and their colorings is therefore prior work and **not** claimed new here. Shareshian and Wachs (2004), with the earlier Friedman–Hanlon results they cite, study chessboard homology and its symmetric-group representations; these cover the rook graph component of the comparison, not the nonisomorphic Shrikhande independence complex. Barmak (2010) treats topological methods for independence complexes but does not compute the Shrikhande affine homology character.

A published 2026 result explicitly calculates \(\operatorname{Ind}(S)\simeq\bigvee^{23}S^2\) and the corresponding rook-graph wedge; its accessible full `RESULT.md` gives the nonequivariant Morse matching and does not determine an action of the \(192\) automorphisms. The exact new assertion here is the full affine character, its rational \(T\)-module and \(D_6\)-module structure, and the contrasting symmetry-quotient cohomology. Published graph-parameter and maximum-coclique results alone do not imply those equivariant statements. A recent book on the Shrikhande graph has an accessible outline but an inaccessible full chapter on automorphisms; equivalent unindexed computations are a residual publication-priority risk.

## Limitations
The character determines the rational homology representation, not the full integral automorphism-module lattice or equivariant homotopy type. The rational cohomology of a quotient does not determine its integral cohomology or its homotopy type. No uniform result for larger Doob graphs is asserted. Independent mathematical review and a definitive publication-priority determination have not been performed.

## References
1. R. Peeters, *Strongly Regular Graphs that are Locally a Disjoint Union of Hexagons*, European Journal of Combinatorics 18 (1997), 579–588; earlier Tilburg research memorandum FEW 625 (1993), https://paperzz.com/doc/7134087/strongly-regular-graphs-that-are-locally-a-disjoint-union... .
2. J. Shareshian and M. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, first posted 2004-09-03, arXiv:math/0409054v1, https://arxiv.org/html/math/0409054v1 .
3. J. A. Barmak, *Star clusters in independence complexes of graphs*, first posted 2010-07-02, arXiv:1007.0418v1, https://arxiv.org/html/1007.0418v1 .
4. *Independence complexes of the Shrikhande and \(4\times4\) rook graphs have different sphere-wedge homotopy types*, available 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-independence-complexes-of-the-shrikhande-and-4-times4-rook-graph--41bf4d1d3187 .
5. P. J. Cameron, A. Lakshmanan S. and A. Vijayakumar, *The Shrikhande Graph: A Window on Discrete Mathematics*, Cambridge University Press (2026), https://doi.org/10.1017/9781009709118 (full chapter text not inspected).
6. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
