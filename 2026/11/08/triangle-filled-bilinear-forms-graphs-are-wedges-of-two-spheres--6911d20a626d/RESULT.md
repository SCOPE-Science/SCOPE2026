# Triangle-filled bilinear-forms graphs are wedges of two-spheres

## Finding
Fix a prime power \(q\) and integers \(a,b\geq2\). Let \(G=\mathrm{Bil}_q(a,b)\) have the \(a\times b\) matrices over \(\mathbb F_q\) as vertices, adjacent precisely when their difference has rank one. Let \(T=\operatorname{skel}_2\operatorname{Cl}(G)\), the simplicial complex containing every vertex, edge, and triangle of the graph, but no higher-dimensional faces. Define
\[
V=q^{ab},\qquad d=\frac{(q^a-1)(q^b-1)}{q-1},\qquad
E=\frac{Vd}{2},\qquad F=\frac{Vd(q^a+q^b-q-2)}{6}.
\]
Then \(T\) is simply connected and has the **integral** homotopy type
\[
\boxed{|T|\simeq\bigvee^{\,V-E+F-1}S^2.}
\]
Consequently Lewis's second girth of \(G\), defined by filling all graph triangles, is \(g_2(G)=3\). In particular, for \((q,a,b)=(2,2,2)\) the complex is a wedge of \(39\) two-spheres; for \((2,2,3)\) it is a wedge of \(1183\) two-spheres.

## Assumptions and scope
All statements hold for every finite field \(\mathbb F_q\), including nonprime-order fields, and all integers \(a,b\geq2\). The simplicial complex is **only the two-skeleton** of the clique complex; the full clique complex generally contains tetrahedra and higher-dimensional faces and is not assigned this homotopy type. The wedge is an ordinary nonequivariant integral homotopy equivalence. A null backtrack is allowed in the standard edge-path homotopy of a simplicial complex.

## Proof
**1. A presentation for triangular edge paths.** Put \(H=(\mathbb F_q^{a\times b},+)\), and let \(\mathcal R\) be its nonzero rank-one elements. Introduce a group \(P\) with generators \(x_R\), one for each \(R\in\mathcal R\), and relations
\[
x_{-R}=x_R^{-1},\qquad x_Rx_S=x_{R+S}\quad\text{if }R,S,R+S\in\mathcal R.
\]
There is an evaluation homomorphism \(\epsilon:P\to H\), \(x_R\mapsto R\). A walk in \(G\), beginning at the zero matrix, is encoded by its rank-one increments. Triangle moves replace consecutive increments \(R,S\) by \(R+S\) precisely when the three increments are rank one; cancellation of a backtrack corresponds to \(x_Rx_{-R}=1\). Because the same relations can be applied after translation to any starting matrix, \(\pi_1(T,0)\) is canonically the kernel of \(\epsilon\): a based loop has total increment zero, and a word trivial in \(P\) is reducible by lifted triangle and backtrack moves. This argument uses edge paths directly and does not require a free action on geometric simplex interiors (important in characteristic two).

**2. The rank-one commutation identity.** If \(R,S\in\mathcal R\) share a left factor or share a right factor, their sum has rank one unless it is zero. The triangle relation, or the inverse relation when their sum is zero, gives \(x_Rx_S=x_Sx_R\). Otherwise write two arbitrary rank-one increments with independent left and right factors as \(C=uy^{\mathsf T}\) and \(D=xv^{\mathsf T}\), where \(u,x\) are independent and \(v,y\) are independent. Set \(A=uv^{\mathsf T}\), \(B=xy^{\mathsf T}\), and \(W=(u+x)(v+y)^{\mathsf T}\). Every matrix \(A,B,C,D,W\) and each required paired sum is nonzero rank one. The same rank-one matrix has two valid rank-one decompositions, giving in \(P\)
\[
\begin{aligned}
x_W&=x_{A+C}x_{D+B}=x_Ax_Cx_Dx_B,\\
x_W&=x_{A+D}x_{C+B}=x_Ax_Dx_Cx_B.
\end{aligned}
\]
Cancelling the outer generators proves \(x_Cx_D=x_Dx_C\). Hence *all* generators of \(P\) commute, including those with independent row and column directions.

**3. The presentation contains no extra relations.** Let \(E_{ij}\) be the matrix units. For fixed \((i,j)\), the triangle and inverse relations show that \(t\mapsto x_{tE_{ij}}\), with \(x_0=1\), is a homomorphism from \((\mathbb F_q,+)\) into \(P\). Every rank-one matrix \(uv^{\mathsf T}\) is a sum of coordinate rank-one matrices, in two stages using first a fixed left factor and then fixed right factors; at each stage nonzero partial sums have rank one. Thus \(x_{uv^{\mathsf T}}\) equals the corresponding product of coordinate generators. Since \(P\) is abelian, these coordinate homomorphisms combine to a surjection \(H\to P\), and its composite with \(\epsilon\) is the identity on \(H\). Therefore \(\epsilon:P\to H\) is an isomorphism and \(\pi_1(T)=1\).

**4. Face enumeration.** Every nonzero rank-one matrix is \(uv^{\mathsf T}\) with \(u,v\ne0\), and each has exactly \(q-1\) such representations. Therefore each graph vertex has degree \(d\), and \(G\) has \(V\) vertices and \(E=Vd/2\) edges. For adjacent vertices \(0\) and \(R=uv^{\mathsf T}\), a common neighbor \(Z\) has rank one and \(Z-R\) has rank one. Two rank-one matrices have rank-one difference exactly when their column spaces or row spaces agree (apart from zero differences). Thus \(Z\) belongs to the union of the two linear rank-one flats \(u\mathbb F_q^b\) and \(\mathbb F_q^a v^{\mathsf T}\), which contain \(q^b\) and \(q^a\) elements and intersect in the \(q\)-element line \(\mathbb F_q R\). Removing \(0,R\) yields precisely \(\lambda=q^a+q^b-q-2\) common neighbors. Each triangle is counted at its three edges, so \(F=E\lambda/3\).

**5. Integral homotopy conclusion.** Matrix units connect the graph, hence \(T\) is connected. The simply connected finite two-dimensional CW complex has \(H_1(T;\mathbb Z)=0\), no homology in dimensions above two, and free \(H_2(T;\mathbb Z)\) because it is a subgroup of the free cellular two-chain group. The Euler relation gives its rank \(\beta=V-E+F-1\). By the Hurewicz isomorphism \(\pi_2(T)\cong H_2(T;\mathbb Z)\), choose based sphere maps representing an integral basis and wedge them. The resulting map \(\bigvee^\beta S^2\to T\) is an integral homology isomorphism between simply connected CW complexes; the homological Whitehead theorem makes it a homotopy equivalence. Since triangles exist and their attaching maps kill \(\pi_1(G)\), Lewis's invariant is \(g_2(G)=3\).

## Verification
Run `python3 verify_bilinear_triangle.py`. The accompanying `verify_bilinear_triangle_output.txt` records an actual independent construction for \((q,a,b)=(2,2,2),(2,2,3),(2,3,3),(3,2,2)\). The program computes rank-one adjacency from matrix entries, enumerates common-neighbor triangles, and reduces the complete triangle-to-edge boundary matrix over \(\mathbb F_2\). It verifies \(\widetilde H_1(-;\mathbb F_2)=0\) and the predicted second Betti number in all four cases. It does not prove integral simple connectivity or the all-prime-power theorem; those follow from the preceding group-presentation proof.

## Relationship to prior work
Burkey, Martin, and Oulon (arXiv:2610.33869v1, first available October 24, 2026) study Lewis's homotopy and prove second-girth values for Johnson and Hamming graphs and folded counterparts. Their full accessible preprint does not address bilinear-forms graphs or a two-skeleton wedge classification. Cioabă and Mim (arXiv:2606.27328) investigate first clique homology of strongly regular graphs over fields; even vanishing first homology is weaker than simple connectivity and an integral wedge decomposition, and the bilinear-forms family is not treated explicitly in the inspected text. Cioabă, Guo, Ji, and Mim (arXiv:2508.05871) investigate clique Laplacians and first cohomology for other families. The present argument constructs a nonabelian triangle-path presentation and proves it collapses to the additive matrix group, which is the critical new step.

## Limitations
The result concerns the two-skeleton, not the full clique complex or persistent homology in higher filtration scales. It does not determine the automorphism action on the second integral homology lattice. Searches and available primary-source inspections did not find the same all-parameter statement; equivalent unindexed geometric-combinatorial results remain a novelty risk. The finite verifier examines prime fields only, whereas the proof applies to every prime power. Independent review has not been performed.

## References
1. M. Burkey, W. J. Martin, and F. Oulon, *On Lewis's homotopy in distance-regular graphs*, arXiv:2610.33869v1 (2026-10-24), https://arxiv.org/html/2610.33869v1.
2. S. M. Cioabă and M. Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328 (2026-06-25), https://arxiv.org/abs/2606.27328.
3. S. M. Cioabă, K. Guo, C. Ji, and M. Mim, *Clique complexes of strongly regular graphs, their eigenvalues, and cohomology groups*, arXiv:2508.05871 (2025-08-07), https://arxiv.org/abs/2508.05871.
4. A. L. Gavrilyuk and J. H. Koolen, *A Characterization of the Graphs of Bilinear (d×d)-Forms over F₂*, Combinatorica 39 (2019), 289–321; earlier arXiv:1511.09435 (2015-11-30), https://arxiv.org/abs/1511.09435.
