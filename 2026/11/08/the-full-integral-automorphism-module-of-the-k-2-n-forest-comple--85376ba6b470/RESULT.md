# The full integral automorphism module of the \(K_{2,n}\) forest complex

## Finding

For every integer \(n\ge3\), let \(X_n\) be the graphic-matroid independence complex of the simple complete bipartite graph \(K_{2,n}\): its vertices are the \(2n\) graph edges, and its simplices are **acyclic edge sets** (spanning forests, including the empty edge set). The entire graph automorphism group is \(G_n=S_2\times S_n\), where the first factor interchanges the two vertices of degree \(n\) and the second permutes the vertices of degree two.

Let \(A_{n-1}=\ker(\mathbb Z^n\xrightarrow{\sum}\mathbb Z)\), with its natural \(S_n\)-permutation action. Let \(\varepsilon\) be the one-dimensional integral character
\[\varepsilon(\tau,\sigma)=(-1)^{n\tau}\operatorname{sgn}(\sigma),\qquad \tau\in\{0,1\},\quad\sigma\in S_n.\]
Then, **as a full integral \(G_n\)-module**,
\[\widetilde H_j(X_n;\mathbb Z)\cong\begin{cases}A_{n-1}\otimes\mathbb Z_\varepsilon,&j=n,\\0,&j\ne n.\end{cases}\]
The ordinary (nonequivariant) homotopy type and complete top rational character are
\[X_n\simeq\bigvee^{n-1}S^n,\qquad \chi_n(\tau,\sigma)=(-1)^{n\tau}\operatorname{sgn}(\sigma)\bigl(\#\operatorname{Fix}(\sigma)-1\bigr).\]
In particular, the full finite symmetry quotient has only degree-zero rational cohomology:
\[H^*(|X_n|/G_n;\mathbb Q)\cong\mathbb Q.\]
The integral lattice also has the distinguishing invariant \(H^1(S_n,A_{n-1})\cong\mathbb Z/n\mathbb Z\). The new point is the **full integral automorphism lattice and its action**; the sphere-wedge count and rank are established in earlier general matroid literature.

## Assumptions and scope

All simplicial chains use integral coefficients and the usual oriented-simplex boundary. Here a forest means an edge set with no graph cycle; it is **not** the different complex of vertex subsets inducing forests. The group \(S_2\times S_n\) acts on the \(2n\) edges by \((\tau,\sigma):(i,s)\mapsto(\sigma(i),s+\tau\pmod2)\). For \(n\ge3\), the two bipartite vertex classes have different degrees, so this is exactly the full graph automorphism group. The assertions hold for every integer \(n\ge3\), not only for enumerated cases.

## Proof

Write \(a_i=(i,0)\) and \(b_i=(i,1)\) for the two edges incident with the \(i\)-th degree-two vertex, and define the zero-sphere \(S_i^0=\{\varnothing,\{a_i\},\{b_i\}\}\). Every simple cycle in \(K_{2,n}\) uses both vertices of its size-two part, exactly once, so it is a four-cycle on two distinct columns. Therefore an edge set is a forest precisely when **at most one index** \(i\) has both \(a_i\) and \(b_i\) present.

Set \(Q_n=S_1^0*\cdots*S_n^0\), the boundary of the \(n\)-dimensional crosspolytope, so \(|Q_n|\cong S^{n-1}\). For each index \(i\), put
\[B_i=\Delta(\{a_i,b_i\})*\mathop{*}_{j\ne i} S_j^0.\]
Since the join of an edge with an \((n-2)\)-sphere is an \(n\)-ball, \(B_i\) is a simplicial ball with its **entire** boundary equal to \(Q_n\). The four-cycle criterion gives
\[X_n=\bigcup_{i=1}^n B_i,\qquad B_i\cap B_j=Q_n\quad(i\ne j).\]
These are equalities of simplicial complexes. The first closed ball fills \(Q_n\) contractibly. Each subsequent ball is attached along \(Q_n\), whose inclusion into the preceding union is nullhomotopic since it factors through the first ball. Thus \(|X_n|\simeq\bigvee^{n-1}S^n\), including its claimed homology concentration and torsion-freeness.

To identify the **integral group action**, orient the fundamental class \(c\in\widetilde H_{n-1}(Q_n;\mathbb Z)\) by the ordered simplicial join of the \(n\) zero-cycles \([b_i]-[a_i]\). Swapping the two rows negates each zero-cycle, and permuting the \(n\) join factors induces the permutation sign. Consequently every \(g=(\tau,\sigma)\in G_n\) satisfies \(g(c)=\varepsilon(g)c\).

Each relative group \(H_n(B_i,Q_n;\mathbb Z)\) is infinite cyclic, and its connecting boundary map to \(\widetilde H_{n-1}(Q_n;\mathbb Z)\) is an isomorphism. Choose the unique generator \(\beta_i\) mapping to \(c\). Relative excision for the ball interiors and the long exact sequence for \((X_n,Q_n)\) give the **equivariant** exact sequence
\[0\longrightarrow\widetilde H_n(X_n;\mathbb Z)\longrightarrow\bigoplus_{i=1}^n\mathbb Z\beta_i\xrightarrow{\partial}\mathbb Zc\longrightarrow0,\qquad\partial(\beta_i)=c.\]
The action obeys \(g(\beta_i)=\varepsilon(g)\beta_{\sigma(i)}\) by equivariance of \(\partial\). Therefore the kernel of the coefficient-sum map is precisely \(A_{n-1}\otimes\mathbb Z_\varepsilon\), **as an integral \(G_n\)-module**. Its rational character is the stated formula, since the permutation module \(\mathbb Q^n\) has trace \(\#\operatorname{Fix}(\sigma)\).

For the quotient, rational cohomology of a finite simplicial-group orbit space agrees with the invariant cohomology after barycentric subdivision. When \(n\ge3\), the \(S_n\)-representation \(A_{n-1}\otimes\mathbb Q\) is the nontrivial standard representation, whose sign twist has no invariant vectors; hence all positive rational cohomology of \(|X_n|/G_n\) vanishes. Finally, from \(0\to A_{n-1}\to\mathbb Z^n\xrightarrow{\sum}\mathbb Z\to0\), taking \(S_n\)-invariants and first group cohomology gives \(H^1(S_n,A_{n-1})\cong\mathbb Z/n\mathbb Z\): the invariant map \(\mathbb Z\to\mathbb Z\) is multiplication by \(n\), while \(H^1(S_n,\mathbb Z^n)=0\) by the stabilizer permutation-module description and finiteness of \(S_{n-1}\).

## Verification

The included standalone `verify.py` exhaustively enumerates all forest faces for \(n=3,4,5,6\), confirms the exact face formula \((n+3)3^{n-1}\), the reduced Euler characteristic \((-1)^n(n-1)\), and compares signed simplicial Lefschetz characters with the theorem for **every** element of \(S_2\times S_n\). This comprises 1,740 distinct group-element cases, including all 1,440 cases at \(n=6\). All checks pass; the attached `verification_output.txt` is a reproducible output record. The uniform proof is the preceding ball-intersection and integral exact-sequence argument, not an inference from finite enumeration.

## Relationship to prior work

Kook's 2006 online article develops forest-complex homology and automorphism actions for **coned** graphs, a different graph family. Kook and Lee (2018), Theorem 5.3 and Theorem 5.5, construct a basis for complete-bipartite graphic-matroid homology and determine its signed permutation action under the **vertex-stabilizing** subgroup \(S_m\times S_k\subset S_{m+1}\times S_{k+1}\). Specialization to \(K_{2,n}\) gives the already-known rank \(n-1\) and restriction to \(S_{n-1}\), but it does not specify the integral action under the **full** \(S_2\times S_n\). Moci and Pezzoli's general matroid representation correspondence and their Section 6 similarly quote the smaller subgroup; those formulas do not themselves identify the full integral lattice. For example, the augmentation lattice \(A_{n-1}\) and the quotient lattice \(\mathbb Z^n/\mathbb Z(1,\dots,1)\) both restrict to permutation lattices under a point stabilizer \(S_{n-1}\), but are different as integral \(S_n\)-lattices; the explicit relative-ball construction resolves the full-lattice distinction. The ordinary wedge result alone is covered by classical matroid shellability.

## Limitations

The result concerns the graphic-matroid complex of \(K_{2,n}\), not general complete bipartite graphs \(K_{m,n}\) with both parts larger than two, induced-forest vertex complexes, Morse complexes, or integral cohomology of the orbit space. The quotient calculation is rational only. The explicit integral module is supported by a uniform proof and finite computational checks; no independent review has been performed. Unindexed equivalent literature remains a priority risk.

## References

1. W. Kook, *The homology of the cycle matroid of a coned graph*, European Journal of Combinatorics 28 (2007), 734–741, doi:10.1016/j.ejc.2006.01.001. Available online 9 March 2006.
2. W. Kook and K.-J. Lee, *Möbius coinvariants and bipartite edge-rooted forests*, European Journal of Combinatorics 71 (2018), 180–193, author manuscript: https://www.math.snu.ac.kr/~woongkook/201806MC.pdf, especially Theorems 5.3 and 5.5.
3. L. Moci and G. M. Pezzoli, *Representations of automorphism groups on the homology of matroids*, arXiv:2001.03760, especially Section 6, https://arxiv.org/html/2001.03760v3.
4. A. Björner, *The homology and shellability of matroids and geometric lattices*, in *Matroid Applications*, Cambridge University Press (1992), cited in references 1–3.
