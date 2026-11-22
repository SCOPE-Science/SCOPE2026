# Complete open-neighborhood homotopy and symmetry of clique prisms

## Finding
For every integer \(n\ge4\), let \(G_n=K_2\square K_n\) be the graph consisting of two complete \(n\)-vertex graphs connected by a matching, and let \(X_n=\mathcal N(G_n)\) be its ordinary **open** Lovász neighborhood complex. Then there is a nonequivariant integral homotopy equivalence
\[
\boxed{X_n\simeq S^{n-2}\vee S^{n-2}\vee\bigvee^{n^2-3n+1}S^2.}
\]
For \(n=4\) this is a bouquet of seven two-spheres. For \(n\ge5\), the two nonzero reduced integral homology groups have ranks \(n^2-3n+1\) in degree \(2\) and \(2\) in degree \(n-2\); there is no torsion, and \(X_n\) is simply connected.

There is also a complete integral description of the natural \(\operatorname{Aut}(G_n)=S_n\times C_2\) action when \(n\ge5\). Define the lattice
\[
W_n=\{(x_{ij})\in\mathbb Z^{n\times n}:x_{ii}=0,\ \sum_jx_{ij}=0,\ \sum_ix_{ij}=0\}.
\]
Then \(\widetilde H_2(X_n;\mathbb Z)\cong W_n\), where \(S_n\) acts by simultaneous permutation of row and column indices and the \(C_2\) generator acts by matrix transposition. Furthermore
\[
\widetilde H_{n-2}(X_n;\mathbb Z)\cong\operatorname{sgn}_{S_n}\otimes\mathbb Z[C_2],
\]
with the regular two-point permutation lattice for \(C_2\). In particular, if \(f(\sigma)\) and \(t(\sigma)\) count the fixed points and the two-cycles of \(\sigma\in S_n\), respectively, the character of degree-two homology is
\[
\operatorname{tr}((\sigma,0)|\widetilde H_2)=f(\sigma)^2-3f(\sigma)+1,
\qquad
\operatorname{tr}((\sigma,1)|\widetilde H_2)=2t(\sigma)-1.
\]
Here \(0\) and \(1\) denote absence and presence of the layer-swap. The top-degree character is \(2\operatorname{sgn}(\sigma)\) without layer-swap and \(0\) with layer-swap. Thus the quotient by the **full** graph automorphism group has vanishing reduced rational homology in every degree:
\[
\widetilde H_*(X_n/(S_n\times C_2);\mathbb Q)=0,\qquad n\ge5.
\]
Rational acyclicity does not assert contractibility of the quotient.

## Assumptions and scope
All graphs are finite, simple and loopless. Name the vertices \(a_1,\ldots,a_n,b_1,\ldots,b_n\). Distinct vertices are adjacent exactly when they lie in the same lettered clique or form the pair \(a_i,b_i\). A nonempty vertex set is a simplex in \(X_n\) precisely when it is contained in the open neighborhood of some vertex; the witnessing vertex itself is excluded. The integer bound \(n\ge4\) is essential to the simple-connectivity argument for the covering subcomplexes. The equivariant descriptions start at \(n\ge5\) so that their homology degrees are distinct. All group actions are induced by actual graph automorphisms, without choosing an equivariant wedge splitting.

## Proof
**1. Two natural subcomplexes.** Put \(A=\{a_i:1\le i\le n\}\), \(B=\{b_i:1\le i\le n\}\), and
\[
U=\bigcup_{i=1}^n\Delta((A\setminus\{a_i\})\cup\{b_i\}),\qquad
V=\bigcup_{i=1}^n\Delta((B\setminus\{b_i\})\cup\{a_i\}).
\]
By the explicit open neighborhoods, \(X_n=U\cup V\). Every \(b_i\) occurs in exactly one facet of \(U\), so that facet is a cone on \(\Delta(A\setminus\{a_i\})\) with a private apex. It simplicially collapses onto its base without changing any other facets. Repeating for all \(i\) leaves exactly the boundary \(\partial\Delta(A)\). Likewise \(V\) collapses to \(\partial\Delta(B)\). Therefore \(U\simeq V\simeq S^{n-2}\).

**2. Exact intersection.** No edge \(a_i b_i\) is in either \(U\) or \(V\). For \(i\ne j\), the cross edge \(a_i b_j\) is in the neighborhood simplices centered at \(a_j\) and \(b_i\), so it lies in both. Every face of \(U\) containing a vertex from \(B\) has only one such vertex; every face of \(V\) containing a vertex from \(A\) has only one such vertex. A face supported entirely on \(A\) can meet \(V\) in at most one vertex, and conversely. Hence \(H=U\cap V\) is **exactly** the one-dimensional crown graph \(K_{n,n}\) with the diagonal perfect matching deleted. It has \(2n\) vertices and \(n(n-1)\) edges; for \(n\ge3\) it is connected. Its first Betti number is therefore
\[
\beta_1(H)=n(n-1)-2n+1=n^2-3n+1.
\]

**3. Full homotopy type.** For \(n\ge4\), the spheres \(U\simeq S^{n-2}\) and \(V\simeq S^{n-2}\) are simply connected. Since \(H\) is a connected graph, each inclusion \(H\to U\) and \(H\to V\) is nullhomotopic (choose any spanning tree and contract the finitely many remaining loops). The inclusions of simplicial subcomplexes are cofibrations, so their union is a homotopy pushout. The homotopy pushout of two nullhomotopic maps from connected \(H\) is \(U\vee V\vee\Sigma H\). Since \(H\simeq\bigvee^{n^2-3n+1}S^1\), its suspension is \(\bigvee^{n^2-3n+1}S^2\). This proves the claimed integral homotopy type uniformly for all \(n\ge4\), with no appeal to finite sampling.

**4. The integral symmetry lattices.** When \(n\ge5\), Mayer–Vietoris for the same cover has natural isomorphisms
\[
\widetilde H_2(X_n;\mathbb Z)\xrightarrow{\ \partial_{MV}\ }H_1(H;\mathbb Z),\qquad
H_{n-2}(U;\mathbb Z)\oplus H_{n-2}(V;\mathbb Z)\xrightarrow{\ \cong\ }H_{n-2}(X_n;\mathbb Z).
\]
Orient each crown edge from \(a_i\) to \(b_j\). An integral crown one-cycle is exactly an off-diagonal coefficient matrix with all row and column sums zero, proving the lattice identification. A simultaneous index permutation acts by permuting both indices of this matrix. The layer-swap sends the oriented crown edge \(a_i\to b_j\) to \(b_i\to a_j\), which is the negative of \(a_j\to b_i\). Meanwhile the Mayer–Vietoris connecting homomorphism changes sign when the two cover pieces are exchanged: this follows directly from the standard inclusion \(C_*(H)\to C_*(U)\oplus C_*(V)\), \(c\mapsto(c,-c)\). The two minus signs cancel, giving **transposition** on \(\widetilde H_2(X_n;\mathbb Z)\). The two fundamental cycles of the oriented simplex boundaries transform by the sign of a common index permutation, and layer-swap interchanges them. This proves the top lattice assertion.

**5. Character and quotient.** On the crown graph, the Lefschetz identity gives \(\operatorname{tr}(\sigma|H_1(H))=f(f-1)-2f+1=f^2-3f+1\). With layer-swap, the induced action on \(W_n\) is transpose followed by the simultaneous index permutation. Exactly \(2t(\sigma)\) directed off-diagonal positions are fixed by that combined operation; the induced trace on the \((2n-1)\)-dimensional row-and-column incidence image is \(1\), yielding \(2t(\sigma)-1\). The top character follows from the two sign-twisted boundary-sphere generators. An \(S_n\)-invariant element of \(W_n\otimes\mathbb Q\) has constant off-diagonal entries, so its zero row sum forces it to vanish. The sign-twisted top module likewise has no \(S_n\)-invariant vectors. After barycentric subdivision, finite-group averaging identifies the rational homology of the orbit space with invariant rational homology. This establishes rational acyclicity.

## Verification
The standalone standard-library Python file `verify_clique_prism.py` independently reconstructs the open-neighborhood simplices from the two facet families; for \(n=4,5,6,7,8\), it checks that the intersection has precisely the crown edges, that each side consists of the claimed simplex boundary with private coned facets, and that all mod-two simplicial boundary ranks match the integral theorem. It records full face vectors. For \(n=5,6\), it tests the predicted **equivariant Lefschetz number of every element** of \(S_n\times C_2\), totaling \(240+1440=1680\) elements, against directly enumerated signed simplex traces. The recorded output ends in `ALL_CHECKS_PASS`. These computations corroborate the all-parameter proof; they are not claimed to establish it by enumeration.

## Relationship to prior work
Kahle [1] gives the classical neighborhood-complex framework and complete-clique boundary example, but does not treat two cliques linked by a matching. Matsushita [2] gives a fundamental-group description of open neighborhood complexes; it does not determine their full homotopy types or their higher homology representations. Shukla [3] treats bounded-degree and selected circulant families, not the all-parameter \((n\text{-regular})\) clique prisms for \(n\ge5\). Matsushita [4, Example 3.5] computes the **closed**, not open, neighborhood complex of arbitrary rook graphs, so its two-dimensional sphere wedge cannot imply the mixed-dimensional open result. The published row–column theorem [5] concerns the **open** rook complex only when both board dimensions are at least three, and determines a higher-degree homology/cofiber description rather than the present two-row complete homotopy and full symmetry representation. The published clique–cycle theorem [6] assumes a cycle factor of length at least five, and its circle stage is not present here; the two-layer factor \(K_2\) is outside its hypotheses. The present full homotopy and symmetry statement is outside the hypotheses of [5] and [6].

## Limitations
The homotopy equivalence is nonequivariant. The symmetry description classifies integral homology modules, **not** an equivariant homotopy decomposition. The quotient theorem concerns rational homology only; no claim of quotient contractibility, integral quotient homology, or an all-parameter statement for the exceptional \(n=3\) case is made. The literature comparisons cannot rule out all unindexed equivalent treatments; independent verification and publication-priority review remain outstanding.

## References
[1] M. Kahle, *The neighborhood complex of a random graph*, first public arXiv version 2005-12-04, arXiv:math/0512077, especially Section 1 and the complete-clique example.

[2] T. Matsushita, *Fundamental groups of neighborhood complexes*, first public arXiv version 2012-10-10, arXiv:1210.2803, especially Theorem 1.1.

[3] S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, first public 2018-02-13.

[4] T. Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608, first public 2025-11-16, Definition 1.1 and Example 3.5.

[5] *Row–column boundary spheres control higher neighborhood homology of rook graphs*, publicly available research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-row-column-boundary-spheres-control-higher-neighborhood-homology--f09a20a3ee45 .

[6] *Mixed-dimensional neighborhood homotopy of complete-graph cycle products*, publicly available research record, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-mixed-dimensional-neighborhood-homotopy-of-complete-graph-cycle--3a53c8927b3c .

