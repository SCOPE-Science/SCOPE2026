# The index-sixteen integral gluing in the Picard torus of a complete quadrangle

## Finding
Let \(k=\mathbb F_q\) be any finite field of odd characteristic. Let \(P\subset\mathbb P^2_k\) be a Frobenius-stable reduced degree-four étale subscheme whose four geometric points form a projective frame (no three collinear), and let \(D\) be the reduced union of the six joining lines. Write \(T\) for the maximal torus quotient of \(\operatorname{Pic}^0(D)\). The geometric character lattice \(L=X^*(T_{\bar k})\) is a rank-six integral \(S_4\)-module, canonically obtained as the cycle lattice of the singular-point/line-branch incidence graph.

Let \(V_4\) denote the normal subgroup of the three double transpositions of \(S_4\), and let \(L_1,L_2,L_3\) be the intersections of \(L\) with the three distinct nontrivial rational \(V_4\)-character spaces. Then each \(L_i\) is primitive of rank two, but their direct sum fails to fill the integral character lattice by exactly
\[
L/(L_1\oplus L_2\oplus L_3)\cong(\mathbb Z/2\mathbb Z)^4.
\]
Thus the rational three-plane-pair decomposition hides an index-sixteen integral gluing. The index and quotient are independent of the chosen geometric frame.

For a finite field, the *actual isomorphism class* of \(T\), not just its isogeny class, depends on the cycle type of Frobenius \(\sigma\in S_4\) as follows. Put \(k_d=\mathbb F_{q^d}\), and \(R^1_{k_4/k_2}\mathbb G_m=\ker(N_{k_4/k_2}:\operatorname{Res}_{k_4/k_2}\mathbb G_m\to\mathbb G_m)\).

| Cycle type of \(\sigma\) | Torus over \(k\) | Finite abelian group \(T(k)\) |
|---|---|---|
| \(1^4\) | \(\mathbb G_m^6\) | \(C_{q-1}^6\) |
| \(2\,1^2\) | \((\operatorname{Res}_{k_2/k}\mathbb G_m)^3\) | \(C_{q^2-1}^3\) |
| \(2^2\) | \((\operatorname{Res}_{k_2/k}\mathbb G_m)^2\times(R^1_{k_2/k}\mathbb G_m)^2\) | \(C_{q^2-1}^2\times C_{q+1}^2\) |
| \(3\,1\) | \((\operatorname{Res}_{k_3/k}\mathbb G_m)^2\) | \(C_{q^3-1}^2\) |
| \(4\) | \(\operatorname{Res}_{k_4/k}\mathbb G_m\times\operatorname{Res}_{k_2/k}(R^1_{k_4/k_2}\mathbb G_m)\) | \(C_{q^4-1}\times C_{q^2+1}\) |

Here \(C_s\) is cyclic of order \(s\). The corresponding numbers of \(k\)-points of the singular plane curve \(D\), in the same row order, are \(6q-5\), \(2q+1\), \(2q+3\), \(1\), and \(1\), respectively.

## Assumptions and scope
All statements concern this fixed geometric six-line union and its forms arising from Frobenius permutations of the four base points. The base is perfect, and the arithmetic table is stated for odd prime powers. The point scheme \(P\) is assumed reduced étale and in geometric general position. The character lattice is an integral Galois module, with a distinguished full geometric \(S_4\) action independent of any one finite-field twist. A torus is described by its *integral* character lattice; equal rational characteristic polynomials do not suffice for these isomorphism claims.

The six lines are the unordered pairs \(\{i,j\}\subset\{0,1,2,3\}\). Their only singular points are four ordinary triple points indexed by \(i\) and three ordinary nodes indexed by partitions \(\{\{i,j\},\{u,v\}\}\) into two pairs. A line indexed by \(\{i,j\}\) has precisely three branches at singular points: at \(i\), at \(j\), and at the diagonal node whose partition contains \(\{i,j\}\). The graph \(\Gamma\) consequently has thirteen vertices, eighteen edges and first Betti number six. The plane curve has arithmetic genus ten; the unipotent quotient has dimension four. These other Picard factors are **not** claimed to be classified by the torus table.

## Proof
**Geometry and normalization.** A projective frame can be sent to \([1:0:0],[0:1:0],[0:0:1],[1:1:1]\). The six line product is \(XYZ(X-Y)(X-Z)(Y-Z)\). Pairwise intersections are exactly the four triple points and the three intersections of opposite sides, none coincident in the stated characteristics. At an ordinary triple point the delta invariant is three and its three normalization branches contribute two toric dimensions and one unipotent dimension; at an ordinary double point the delta invariant and toric contribution are both one. Hence \(p_a(D)=4\cdot3+3-6+1=10\). The normalization is six rational curves, so the maximal torus is dual to the free integral cycle lattice
\[
L=\ker\!\left(\partial:\mathbb Z^{18}\longrightarrow\mathbb Z^{13}\right),\qquad \operatorname{rank}L=18-13+1=6.
\]
The signed boundary \(\partial\) sends an oriented flag to its singular-point vertex minus its line vertex, and \(S_4\) acts on flags, reversing orientation when necessary. This description follows directly from the normalization gluing sequence for units; it is also compatible with Geisser's general identification of Picard-torus cocharacters with integral étale cohomology.

**The integral gluing.** Orient each graph edge by lexicographic order of the vertex names, and choose the breadth-first spanning tree rooted at the first line vertex, with neighbors sorted lexicographically. The six edges outside the tree are, in order, the flags
\[
(02,2),\ (03,3),\ (12,03|12),\ (12,2),\ (13,02|13),\ (13,3).
\]
Each non-tree edge, oriented positively, and the uniquely closing tree path is an integral fundamental cycle; this defines basis \(e_1,\dots,e_6\) of \(L\). Write the three double transpositions as \(d_1=(01)(23), d_2=(02)(13), d_3=(03)(12)\). For \(i=1,2,3\), \(L_i\) is the common \(+1\)-eigensublattice for \(d_i\) and common \(-1\)-eigensublattice for the other two. In the displayed fundamental-cycle basis, integral bases of these three eigensublattices are the columns of
\[
W_1=\begin{pmatrix}0&1\\1&0\\0&0\\1&0\\0&0\\0&1\end{pmatrix},\quad
W_2=\begin{pmatrix}0&-1\\-1&0\\0&0\\1&0\\0&-2\\0&1\end{pmatrix},\quad
W_3=\begin{pmatrix}0&-1\\-1&0\\-2&0\\1&0\\0&0\\0&1\end{pmatrix}.
\]
Direct signed edge permutation verifies the claimed eigencharacters. Each \(W_i\) has a two-by-two minor of determinant \(\pm1\), hence is the entire primitive rank-two eigensublattice, not a proper sublattice. With \(W=(W_1\ W_2\ W_3)\), exact integer arithmetic gives \(|\det W|=16\) and \(2W^{-1}\in M_6(\mathbb Z)\). Therefore the quotient has order sixteen and exponent at most two; necessarily it is \((\mathbb Z/2)^4\). This proves an integral statement not visible from the rational \(S_4\)-character. The full action on the canonical graph makes the result independent of frame labels.

**Five cyclic Frobenius classes.** Let \(F\) be the signed action of a chosen permutation in the same six-cycle basis. The standalone checker constructs \(F\) from the eighteen graph flags and provides integral changes of basis with determinant \(\pm1\), conjugating \(F\) to the following blocks. Here \(P_d\) is the \(d\)-cycle permutation matrix and \(R=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\).
\[
\begin{array}{c|c}
1^4&I_6\\
2\,1^2&P_2\oplus P_2\oplus P_2\\
2^2&P_2\oplus P_2\oplus(-1)\oplus(-1)\\
3\,1&P_3\oplus P_3\\
4&P_4\oplus R
\end{array}
\]
For the three-cycle one unimodular basis is \(a,Fa,F^2a,b,Fb,F^2b\) with \(a=e_1\), \(b=e_2\); for the four-cycle it is \(a,Fa,F^2a,F^3a,b,Fb\) with basis coordinates \(a=(-1,-1,-1,-1,1,-1)\), \(b=(-1,-1,-1,0,0,0)\). The transposition and double-transposition changes use signed reorderings of the fundamental basis, fully specified in the verifier. Thus these are integral, not just rational normal forms. The equivalence between integral Frobenius lattices and finite-field tori yields the table. In particular the \(P_d\)-blocks yield Weil restrictions of \(\mathbb G_m\), the \(-1\) blocks yield quadratic norm-one tori, and the \(R\) block yields the quadratic Weil restriction of the relative norm-one torus from \(k_4\) to \(k_2\).

**Rational points of the singular curve.** For every finite extension, normalization gives
\[
\#D(k_n)=\#\widetilde D(k_n)-\#\widetilde\Sigma(k_n)+\#\Sigma(k_n),
\]
where \(\Sigma\) is the seven-point singular locus and \(\widetilde\Sigma\) its eighteen normalization branches. Counting fixed line components, fixed singular points and fixed flags gives \((6,7,18)\), \((2,3,4)\), \((2,3,2)\), \((0,1,0)\), \((0,1,0)\) for the five classes, hence the point-count assertions. The line components are genus-zero forms over finite fields and therefore contribute \(q+1\) points when fixed.

## Verification
Execute `python3 verify_quadrangle.py` from the containing directory with SymPy 1.12 or newer. The script creates the thirteen vertices and eighteen branches without reading external data, constructs an integral fundamental cycle basis, checks the boundary equation and all \(24\) permutation matrices together with their \(576\) multiplication identities, then checks each eigenspace, its primitive minors, \(|\det W|=16\), the two-torsion bound, and all five unimodular Frobenius conjugacies. It independently checks Smith forms at seven numerical values \(q=2,3,5,7,11,13,17\) and reconstructs the five fixed-point incidence triples. The exact output terminates with `QUADRANGLE_FROBENIUS_INTEGRAL_LATTICE_OK`. These numerical checks corroborate, but do not replace, the symbolic integral-basis proof.

## Relationship to prior work
The six-side/four-triple/three-node geometry is classical and explicitly recorded by Holzapfel in his study of the related blowup and ball quotient, without a Picard-torus calculation. Geisser proves a general cocharacter/cohomology identification for the affine part of Picard schemes; that theorem provides the *method* but not the evaluated \(S_4\) integral module, index-sixteen congruence or five explicit isomorphism classes. A published six-chord-*conic* arrangement theorem instead studies a degree-eight curve with an added conic and four quadruple points, not the present six-line degree-six curve. An independently published fifteen-line Igusa boundary torus theorem treats an unrelated \(S_6\)-configuration. The present conclusion is the specific integral gluing and complete arithmetic torus classification for the classical six-side boundary. Search-based priority claims are provisional, particularly for older integral-representation and graph-lattice literature.

## Limitations
This does not classify Picard schemes of arbitrary six-line arrangements or the non-toric affine factors beyond their dimension. The split torus table is confined to the indicated Frobenius action and finite fields of odd characteristic; extension to arbitrary Galois fields would require using the full displayed integral \(S_4\)-module rather than the cyclic table. The index-sixteen claim concerns a *canonical rational isotypic decomposition* and not an assertion of a canonical decomposition of the lattice itself. No independent mathematical validation or historical priority certification has been performed.

## References
- T. Geisser, *The affine part of the Picard scheme*, arXiv:0704.0479, first posted 2007-04-04, Theorem 1 and §2. https://arxiv.org/abs/0704.0479
- R.-P. Holzapfel, *Complex Hyperbolic Surfaces of Abelian Type*, dated 2013-09-10, pp. 26–27 (six-line complete quadrangle, four triple points, three nodes). https://www.math.hu-berlin.de/~zyska/Holzapfel/Articles/2004.pdf
- *Complete moduli, uniform freeness, and symmetry jumps of the six-chord conic arrangements*, published RESULT, 2026-10-12, specifically the proof's six-line subarrangement (different degree-eight curve). https://github.com/published-finding corpus/2026/blob/main/2026/10/12/SCOPE-complete-moduli-uniform-freeness-and-symmetry-jumps-of-the-six-c--11b4e246d3c7/RESULT.md
- *Finite-field twists and integral Picard tori of the fifteen-line Igusa boundary*, published RESULT, 2026-11-02 (different configuration). https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-finite-field-twists-and-integral-picard-tori-of-the-fifteen-line--71e0231fbb0b/RESULT.md
