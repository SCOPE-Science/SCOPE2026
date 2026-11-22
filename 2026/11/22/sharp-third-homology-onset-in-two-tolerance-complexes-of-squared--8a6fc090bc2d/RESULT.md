# Sharp third-homology onset in two-tolerance complexes of squared cycles

## Finding
For each integer \(7\le n\le12\), put \(G_n=C_n^2\), \(K_n=\operatorname{Cl}(G_n)\), and \(X_n=\mathcal T_2(K_n)\). The complete **integral homotopy types** are

| \(n\) | Integral homotopy type of \(|X_n|\) |
|---|---|
| 7 | \(\bigvee^{6}S^4\) |
| 8 | \(\bigvee^{13}S^4\) |
| 9 | \(\bigvee^{20}S^4\) |
| 10 | \(\bigvee^{2}S^3\vee\bigvee^{26}S^4\) |
| 11 | \(\bigvee^{12}S^3\vee\bigvee^{33}S^4\) |
| 12 | \(\bigvee^{33}S^3\vee\bigvee^{42}S^4\) |

Thus the first nonzero third integral homology in the stable triangle-clique regime occurs **at the sharp length ten**. For \(n=11,12\), an explicit geometrically defined family of top cycles coming from pairs of disjoint consecutive triangles is an integral basis for \(H_4\). This family is primitive but has rank one below \(H_4\) at \(n=10\). The length twelve is the first for which a tetrahedral face is absent: exactly three four-element independent sets of \(G_{12}\) occur.

## Assumptions and scope
All complexes are abstract simplicial complexes on the cyclic vertex set \(\mathbb Z/n\mathbb Z\), realized geometrically. Two vertices are adjacent in \(G_n\) precisely when their shortest cyclic distance is one or two; the clique complex contains all graph cliques as filled faces. For a complex \(K\), the two-tolerance complex consists of subsets \(\sigma\) admitting a deletion of at most two vertices that leaves a face of \(K\). Every group and homotopy equivalence in this result uses integral coefficients and ordinary, nonequivariant homotopy. The quantifier on \(n\) is the six-element interval \(7\le n\le12\), and not all cycle lengths.

## Proof
**1. Explicit simplices and the natural endpoint.** For \(n\ge7\), the maximal cliques in \(C_n^2\) are the \(n\) cyclic consecutive triples \(T_i=\{i,i+1,i+2\}\). In particular, there is no graph clique of size four. It follows directly from the tolerance definition that \(X_n\) contains every vertex set of size at most three; a four-set is a face precisely when it contains at least one graph edge; and a five-set is a face precisely when it contains a consecutive triple. There are no faces with six or more vertices. The graph has independent-set number \(\lfloor n/3\rfloor\), so every four-set is a face for \(7\le n\le11\). When \(n=12\), the three translates modulo 3 of \(\{0,3,6,9\}\) are exactly its missing four-sets. These observations explain why the complete initial regime naturally stops at the first missing tetrahedra rather than at an arbitrary length.

**2. Two-connectedness, without numerical inference.** The full two-skeleton makes \(|X_n|\) simply connected. To establish integral \(H_2=0\), consider the augmented simplicial chain complex of the complete simplex, written as \(\bigwedge^{k+1}\mathbb Z^n\) in simplicial dimension \(k\), with boundary contraction by the all-ones augmentation \(\varepsilon\). Let \(W=\ker\varepsilon\). Its two-cycles are exactly \(\bigwedge^3 W\). For a graph edge \(\{i,j\}\), the boundary of a tetrahedron on \(\{i,j,k,l\}\) is, up to sign,

\[
(e_i-e_j)\wedge(e_k-e_j)\wedge(e_l-e_j).
\]

As \(k,l\) vary, these boundaries span \((e_i-e_j)\wedge\bigwedge^2W\). The edge differences of the connected graph \(G_n\) span \(W\) integrally (take a spanning tree), so these graph-edge tetrahedral boundaries generate all of \(\bigwedge^3W\). Every one belongs to \(X_n\); consequently \(H_2(X_n;\mathbb Z)=0\). By Hurewicz, the complex is two-connected. This proof holds independently of the finite matrix checks.

**3. Exhaustive signed integer boundaries.** Order vertices increasingly and orient every face by increasing order. Build the full signed integral simplicial boundary \(\partial_4:C_4(X_n;\mathbb Z)\to C_3(X_n;\mathbb Z)\), with the \(j\)-th deleted vertex carrying coefficient \((-1)^j\), using zero-based positions. The independent checker `verify.py` generates all faces from the original tolerance definition, constructs the matrices over \(\mathbb Z\), checks \(\partial_3\partial_4=0\), and runs an exact integer Smith normal form. The complete finite computations are:

| \(n\) | \((f_0,f_1,f_2,f_3,f_4)\) | \(\operatorname{rank}\partial_3\) | Nonzero Smith diagonal of \(\partial_4\) | \((\beta_3,\beta_4)\) |
|---|---|---:|---|---|
| 7 | \((7,21,35,35,21)\) | 20 | fifteen 1s | \((0,6)\) |
| 8 | \((8,28,56,70,48)\) | 35 | thirty-five 1s | \((0,13)\) |
| 9 | \((9,36,84,126,90)\) | 56 | seventy 1s | \((0,20)\) |
| 10 | \((10,45,120,210,150)\) | 84 | one hundred twenty-four 1s | \((2,26)\) |
| 11 | \((11,55,165,330,231)\) | 120 | one hundred ninety-eight 1s | \((12,33)\) |
| 12 | \((12,66,220,492,336)\) | 165 | two hundred ninety-four 1s | \((33,42)\) |

The second-column ranks \(\operatorname{rank}\partial_3=\binom{n-1}{3}\) also follow from step 2, because the full simplex has exactly that many independent two-cycles. Every nonzero Smith diagonal entry of \(\partial_4\) is a unit; hence its image is primitive in \(C_3\), so \(H_3\) has no torsion. The top homology, a subgroup of the free group \(C_4\), is also free. The table gives their exact ranks; every other positive-degree homology group is zero.

**4. Upgrade from homology to homotopy.** The three-skeleton is two-connected by step 2 and has dimension three. Its integral third homology is free, so the Hurewicz map and Whitehead theorem identify it up to homotopy with a wedge of three-spheres. Each four-cell attaches by an element of \(\pi_3\) of that wedge, and the integer degree matrix is exactly the displayed signed \(\partial_4\). Unimodular changes of the degree bases realize its Smith diagonal; all nonzero invariant factors are 1, so the corresponding three/four-cell pairs cancel up to homotopy, while the zero attachments become four-spheres. The resulting homotopy type has exactly \(\beta_3\) three-spheres and \(\beta_4\) four-spheres, proving the six asserted classifications.

**5. Primitive geometric top cycles.** If consecutive triangles \(T_i,T_j\) are vertex-disjoint, their six-vertex union \(S\) has all six five-vertex deletions in \(X_n\): deleting from either triangle leaves the other intact. Therefore the alternating boundary \(z_S=\partial[S]\) of the *formal* five-simplex is a genuine integral four-cycle in \(X_n\). The checker builds the integer matrix of these cycles inside \(C_4(X_n)\). At \(n=10\), the 25 distinct cycles have 25 unit Smith factors, leaving one free top-homology direction. At \(n=11\), 33 such cycles have 33 unit factors, exactly the full rank of \(H_4\); at \(n=12\), the corresponding values are 42 and 42. Primitivity in the full chain lattice and equality of ranks imply that these cycles form actual integral bases of \(H_4\) for 11 and 12. No unverified extrapolation to larger lengths is used.

## Verification
Run `python verify.py` with Python 3 and SymPy installed. The full deterministic output is embedded in `verification_output.txt`, and independent execution against the packaged `verify.py` reproduced it. The code uses the tolerance definition, exact signed integral matrices and exact Smith forms, **not** floating-point homology or a finite-field-only substitute. It also checks mod-two ranks, signs, \(\partial_3\partial_4=0\), missing tetrahedra and primitive carrier saturation. All six cases are exhaustively enumerated, so these finite computations establish the stated finite-range theorem; they do not imply the same pattern at any untested length.

## Relationship to prior work
Kim and Lew introduced tolerance complexes and proved general Leray-number bounds, rather than these specific homotopy types. Selvaraja (first public version 10 November 2026) studies sharp Leray/collapsibility and top-dimensional nonvanishing; the paper's general top-dimensional theorem requires nonzero top homology of the input. Here the clique complex \(K_n\) has no top-dimensional homology: each triangle has its unique cyclic distance-two edge, so no nontrivial two-cycle exists. Its general bounds therefore do not supply this exact classification. The distinct ordinary cut complexes, two-independence complexes and one-tolerance complexes previously studied on squared cycles do not use the same face condition; their Betti counts cannot simply be carried over. The exact first nonzero third-homology threshold and the integral primitive top-basis transition are not consequences of those results as inspected.

## Limitations
The classification covers only \(7\le n\le12\), not arbitrary squared-cycle lengths, and the primitive canonical basis is established here only at lengths 11 and 12. The proof uses finite exact integer computations for \(\partial_4\); its code and output are included, but there is no claim of independent audit. Priority against inaccessible or unindexed equivalent publications cannot be ruled out. Equivariant homotopy and integral symmetry representations are not computed.

## References
1. S. Selvaraja, *Tolerance complexes of chordal graphs and squarefree symbolic powers*, arXiv:2611.14384v1, publicly posted 10 November 2026, https://arxiv.org/html/2611.14384v1.
2. M. Kim and A. Lew, *Leray numbers of tolerance complexes*, arXiv:2109.03030v1, first posted 7 September 2021, https://arxiv.org/abs/2109.03030; published in *Combinatorica*, DOI:10.1007/s00493-023-00044-5.
