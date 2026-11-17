# Shore-exchange fixed forests and the integral topological trace of balanced bicliques

## Finding
For every integer \(n\ge2\), the genuine geometric fixed space of the side-exchanging involution on the graphic forest complex of \(K_{n,n}\) admits an explicit \(S_n\)-equivariant PL identification
\[
|\mathcal F(K_{n,n})|^{\langle\tau\rangle}\cong_{\mathrm{PL}}|\mathcal F(K_{n+1})|.
\]
The extra vertex on the right is fixed by \(S_n\). Write \(T_G(x,y)\) for the ordinary graphic Tutte polynomial and put \(a_n=T_{K_{n,n}}(0,1)\), \(b_n=T_{K_{n+1}}(0,1)\). The fixed space is a wedge of \(b_n\) spheres of dimension \(n-1\), whereas the ambient forest complex is a wedge of \(a_n\) spheres of dimension \(2n-2\). The involution acts on the ambient reduced rational top homology with exact trace
\[
\operatorname{tr}(\tau\mid\widetilde H_{2n-2}(\mathcal F(K_{n,n});\mathbb Q))=(-1)^{n-1}b_n.
\]
Its \(+1\) and \(-1\) eigenspaces have dimensions \((a_n+(-1)^{n-1}b_n)/2\) and \((a_n-(-1)^{n-1}b_n)/2\), respectively. The ordinary geometric quotient by \(\tau\) has reduced rational homology only in degree \(2n-2\), of dimension \((a_n+(-1)^{n-1}b_n)/2\). These are claims about rational eigenspaces; no integral direct-sum decomposition is asserted.

## Assumptions and scope
The graph \(K_{n,n}\) has vertex classes \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), with edges \(a_ib_j\) for all indices. Its forest complex \(\mathcal F(K_{n,n})\) is the abstract simplicial complex whose vertices are graph edges and whose simplices are acyclic sets of those edges. The involution \(\tau\) exchanges \(a_i\) with \(b_i\), hence sends \(a_ib_j\) to \(a_jb_i\). Geometric fixed points are points in the realization, not only setwise fixed faces. The parameter range is every \(n\ge2\). The group \(S_n\) simultaneously permutes indices on both shores; it commutes with \(\tau\).

## Proof
**1. The actual geometric fixed-space triangulation.** Every \(\tau\)-orbit of an edge is either a singleton \(d_i=\{a_ib_i\}\) or a pair \(q_{ij}=\{a_ib_j,a_jb_i\}\) with \(i<j\). A fixed barycentric point has equal coefficients on edges in each orbit. It therefore has unique coordinates on the barycenters of those edge-orbits; collections of orbit-barycenters span a simplex exactly when the union of their original edges is a forest. The simplexwise linear map sending each orbit vertex to its normalized orbit barycenter gives a PL-homeomorphism onto the fixed space, with an explicit inverse summing the coefficients over each orbit. This construction commutes with simultaneous index relabeling.

**2. Exact classification of orbit-forest faces.** Map each \(d_i\) to the edge \(0i\) of \(K_{n+1}\) on \(\{0,1,\ldots,n\}\), and each \(q_{ij}\) to the edge \(ij\). For a choice of off-diagonal orbits, let \(F\) be its graph on \(\{1,\ldots,n\}\). If \(F\) has a cycle, its two-sheet lift in \(K_{n,n}\) contains a cycle (of the same length for even base cycles, and of twice that length for odd base cycles). If \(F\) is a forest, its lifted graph consists of two disjoint tree copies of each component: choose a bipartition of each base tree to trivialize the alternating-sheet lift. Adding a singleton diagonal edge \(d_i\) joins the two lifted copies of its component, so there is no cycle precisely when at most one such diagonal edge is chosen in each component of \(F\). Those are exactly the conditions that the graph with edges \(F\cup\{0i:d_i\text{ chosen}\}\) on \(\{0,1,\ldots,n\}\) be a forest. Thus the orbit-barycenter simplicial complex is literally \(\mathcal F(K_{n+1})\). This proves the PL statement and its \(S_n\)-equivariance.

**3. Complete homotopy types.** The forest complex of a graph is the independence complex of its cycle matroid. For \(n\ge2\), both complete graphs \(K_{n+1}\) and complete bicliques \(K_{n,n}\) are connected and have no bridge; their cycle matroids are coloopless of ranks \(n\) and \(2n-1\). Matroid-independence shellability yields wedges of spheres in precisely the dimensions \(n-1\) and \(2n-2\), with multiplicities \(T(0,1)\) as stated. In particular all reduced integral homology is torsion-free and concentrated in the indicated dimensions. An independent finite combinatorial expression for \(b_n\) is
\[
b_n=(-1)^n\sum_{F\subseteq E(K_{n+1}),\ F\mathrm{\ forest}}(-1)^{|F|}.
\]
This follows from the augmented simplicial Euler characteristic. Explicit values \(b_2,b_3,b_4,b_5\) are \(1,6,51,560\).

**4. Ambient involution trace and quotient.** For any finite simplicial action, the reduced Lefschetz number of a finite-order map equals the reduced Euler characteristic of its geometric fixed locus. Thus
\[
\sum_i(-1)^i\operatorname{tr}(\tau\mid\widetilde H_i(\mathcal F(K_{n,n});\mathbb Q))
=\widetilde\chi(|\mathcal F(K_{n,n})|^{\tau})=(-1)^{n-1}b_n.
\]
Only the even degree \(2n-2\) survives for the ambient complex, proving the trace formula. Since \(\tau^2=1\), rational homology splits into \(\pm1\) eigenspaces with the asserted dimensions. Finite-group transfer over \(\mathbb Q\) identifies the quotient's rational homology with the invariant part, proving the final claim. No transfer conclusion over \(\mathbb Z\) is invoked.

## Verification
The included standalone Python 3 script enumerates all \(2^{n(n+1)/2}\) collections of edge-orbits for every \(n=2,3,4,5\) and independently tests acyclicity both upstairs in \(K_{n,n}\) and downstairs in \(K_{n+1}\), with complete agreement. It checks Cayley's spanning-tree facet counts, and obtains \(b_n=1,6,51,560\). A second pass enumerates every original forest for \(n=2,3,4\), computes the signed trace on oriented simplicial faces (including the augmented chain), and independently obtains ambient top-homology ranks \(a_n=1,20,1071\) with involution traces \(-1,6,-51\). The corresponding \((+,-)\) rational dimensions are \((0,1),(13,7),(510,561)\). The verifier requires no nonstandard packages and records exact integers. These finite checks support, but do not replace, the universal argument in the proof.

## Relationship to prior work
The matroid-independence shellability and \(T(0,1)\)-sphere-count theorems are established results, explicitly used rather than claimed as new. Ardila, Castillo and Samper give an explicit shelling theorem for independence complexes; see arXiv:1410.3870, Theorem 1.3 and the introduction. Király, Rosen and Theran treat graph-symmetric matroids and define an orbit construction on whole independent subsets (arXiv:1312.3777, Definition 2.17), but distinguish \(\mathcal P(E)/G\) from \(\mathcal P(E/G)\); their construction does not identify the face system of the geometric fixed space analyzed here. A related complete-graph paired-involution forest calculation produces a quotient with two parallel edges per pair; its sphere multiplicity does not determine the present one-edge-per-pair subcomplex or this complete-bipartite involution's rational character. The claimed contribution is the specific equivariant PL identification and consequent exact complete-bipartite trace and quotient homology formulas, not general matroid shellability or ordinary Tutte identities.

## Limitations
The PL identification is for the designated *side-exchanging* involution, not all automorphisms of \(K_{n,n}\). Only the two rational eigenspace dimensions are classified; integral \(\mathbb Z[C_2]\)-lattice extensions and torsion in the geometric quotient are not determined. The finite verification range is not a proof for higher parameters. While searched sources did not yield an equivalent statement, an older signed-graphic/covering-graph formulation may exist.

## References
1. F. Ardila, F. Castillo and J. A. Samper, *The topology of the external activity complex of a matroid*, arXiv:1410.3870 (first posted October 14, 2014), especially the independence-complex shellability theorem and introduction; https://arxiv.org/abs/1410.3870.
2. F. J. Király, Z. Rosen and L. Theran, *Algebraic Matroids with Graph Symmetry*, arXiv:1312.3777 (first posted December 13, 2013), Definition 2.17 and the distinction between orbit subsets and subsets of orbits; https://arxiv.org/abs/1312.3777.
3. A. Björner, *The homology and shellability of matroids and geometric lattices*, in *Matroid Applications* (1992), a foundational cited predecessor of reference 1. Its original complete text was not independently inspected here.
