# Mixed-dimensional homotopy and integral symmetries of higher independence complexes of clique windmills

## Finding
For integers \(k,s\ge2\), form the generalized windmill \(G_{k,s}=K_1\vee(kK_s)\): a universal hub \(c\) joined to \(k\) pairwise disjoint \(s\)-cliques \(L_1,\ldots,L_k\). Put \(m=ks\). Let \(X_r=\operatorname{Ind}_r(G_{k,s})\) be the simplicial complex of vertex sets whose induced graph has every connected component of cardinality at most \(r\). For **every** integer \(r\ge1\), the ordinary integral homotopy classification is

\[
X_r\simeq
\begin{cases}
\{\mathrm{pt}\}\sqcup \bigvee^{(s-1)^k} S^{k-1},&r=1,\\
\bigvee^{\binom{m-1}{r-1}}S^{r-1}\ \vee\ \bigvee^{\binom{s-1}{r}^{k}}S^{kr-1},&2\le r<s,\\
\bigvee^{\binom{m-1}{r-1}}S^{r-1},&s\le r\le m,\\
\{\mathrm{pt}\},&r\ge m+1.
\end{cases}
\]

In the disconnected case the isolated point is the hub, and the other component is the indicated bouquet. In particular, the family includes an open mixed-dimensional phase \(2\le r<s\). All integral homology is free abelian.

There is also a canonical **integral**, not merely rational, automorphism-module classification. The hub is uniquely determined and \(\operatorname{Aut}(G_{k,s})=S_s\wr S_k\). Let \(U=\ker(\mathbb Z[L_1\sqcup\cdots\sqcup L_k]\xrightarrow{\varepsilon}\mathbb Z)\), and \(U_i=\ker(\mathbb Z[L_i]\xrightarrow{\varepsilon}\mathbb Z)\), with ordinary vertex permutation actions. For \(2\le r\le m\),

\[
\widetilde H_{r-1}(X_r;\mathbb Z)\cong\bigwedge^{r-1}U.
\]

If additionally \(r<s\),

\[
\widetilde H_{kr-1}(X_r;\mathbb Z)\cong\bigotimes_{i=1}^k\bigwedge^{r}U_i,
\]

where a permutation of the clique blocks transports tensor factors with Koszul sign \((-1)^r\) for each block transposition. For \(r=1\) the reduced degree-zero module is \(\mathbb Z\) with trivial action, and the degree-\(k-1\) module is the displayed top tensor construction with \(r=1\). All other reduced modules vanish. These module statements are canonical; the displayed nonequivariant wedge splitting is not asserted to be equivariant.

## Assumptions and scope
All graphs are finite, undirected and simple. A \(q\)-skeleton of a simplex on vertex set \(S\), written \(\operatorname{sk}_{q}\Delta(S)\), consists of subsets of cardinality at most \(q+1\), including the empty face. The \(r\)-independence convention here is **maximum component size \(r\)**, as in Deshpande--Singh and Sawant; some commutative-algebra papers use subscript \(t=r+1\). Empty bouquets of spheres are points. At \(r=1\), \(\{\emptyset\}\) is treated as a combinatorial \((-1)\)-sphere, not an ordinary nonempty space.

## Proof
**1. Exact decomposition.** Write \(L=\bigsqcup_iL_i\) and \(m=|L|\). When the hub is absent, an induced component is precisely the nonempty selection from one leaf clique; thus the leaf-only subcomplex is
\[
B=\bigast_{i=1}^k\operatorname{sk}_{r-1}\Delta(L_i).
\]
When the hub is present, all selected vertices lie in one connected component, and the allowed leaf subsets have cardinality at most \(r-1\). Consequently
\[
X_r=B\cup(c*K),\qquad K=\operatorname{sk}_{r-2}\Delta(L),\qquad B\cap(c*K)=K.
\]
This equality is an equality of simplicial complexes, not merely an equality of Euler characteristics. In particular \(X_r\) is the (unreduced) homotopy cofiber of \(K\hookrightarrow B\) when \(r\ge2\).

**2. Elementary simplex skeleton lemma.** For a set \(S\) of \(n\) vertices and \(1\le q<n\), the complex of subsets of size at most \(q\) is a bouquet of \(\binom{n-1}{q}\) copies of \(S^{q-1}\). Its top reduced integral homology is canonically \(\bigwedge^q\ker(\mathbb Z[S]\xrightarrow{\varepsilon}\mathbb Z)\). To see this, identify the augmented simplicial chain complex of the full simplex with exterior powers of \(\mathbb Z[S]\), whose boundary is the degree-minus-one derivation induced by augmentation. Splitting \(\mathbb Z[S]=\mathbb Ze\oplus\ker\varepsilon\) using any vertex \(e\) identifies the kernel of the top boundary with the claimed exterior power. For the homotopy type, the case \(q=1\) is the discrete \(n\)-point complex and the case \(n=q+1\) is the boundary of a \(q\)-simplex. For \(q\ge2\) and \(n>q+1\), delete one vertex: the deletion is the \((q-1)\)-skeleton on \(n-1\) vertices, and the link is the \((q-2)\)-skeleton on \(n-1\) vertices. By induction the deletion is \((q-2)\)-connected, whereas the link has dimension \(q-2\); the attaching inclusion is therefore nullhomotopic. Its mapping cone is a wedge of the deletion and the suspension of the link. Pascal's identity gives the multiplicity \(inom{n-1}{q}\). This is also the standard uniform-matroid-skeleton theorem.

**3. Homotopy types.** If \(r\ge s\), every factor in \(B\) is a simplex, hence \(B\) is contractible. For \(s\le r\le m\), the cofiber is homotopy equivalent to \(\Sigma K\), which is the stated bouquet of \(S^{r-1}\)'s by Step 2. If \(r\ge m+1\), the hub is a genuine cone point in the entire complex, so \(X_r\) is contractible. If \(2\le r<s\), each factor of \(B\) is a bouquet of \(\binom{s-1}{r}\) copies of \(S^{r-1}\), so the iterated join is a bouquet of \(\binom{s-1}{r}^k\) spheres of dimension \(kr-1\). It is \((kr-2)\)-connected. Since \(\dim K=r-2\) and \(kr-2>r-2\), the inclusion \(K\hookrightarrow B\) is nullhomotopic by cellular approximation, so its mapping cone splits as \(B\vee\Sigma K\). If \(r=1\), the only face containing the hub is its singleton; the disjoint leaf component \(B\) is the join of \(k\) discrete sets of size \(s\), hence a bouquet of \((s-1)^k\) spheres of dimension \(k-1\). This covers every integer parameter and all boundary regimes.

**4. Integral symmetry.** All operations in Step 1 are equivariant under the wreath-product automorphism group. In the Mayer--Vietoris long exact sequence, \(K\) has reduced homology only in degree \(r-2\), and for \(2\le r<s\) the only positive-degree reduced homology of \(B\) occurs in degree \(kr-1>r-1\). Hence the connecting homomorphism is a canonical equivariant isomorphism \(\widetilde H_{r-1}(X_r;\mathbb Z)\to\widetilde H_{r-2}(K;\mathbb Z)\). The same statement holds for \(r\ge s\), because \(B\) is contractible. The augmented chain calculation in Step 2 identifies this with \(\bigwedge^{r-1}U\). In the mixed range, inclusion of \(B\) identifies top homology canonically with the join-homology tensor product \(\bigotimes_i\bigwedge^rU_i\). A block transposition exchanges two reduced chain factors of degree \(r-1\) in a join, and the Eilenberg--Zilber join sign is \((-1)^{(r-1+1)^2}=(-1)^r\). The \(r=1\) case is an isolated fixed hub and a connected permuted leaf component, giving its trivial \(\widetilde H_0\) module and the same tensor sign in degree \(k-1\).

## Verification
The reproducible script `verify.py` constructs each induced graph directly from edge data; it never invokes the structural decomposition to enumerate faces. It checks exactly \(47\) parameter triples with \(2\le k\le4\), \(2\le s\le4\), \(1+ks\le11\), \(1\le r\le ks+1\), independently computing all reduced mod-two homology groups. For each parameter triple it also computes signed simplicial Lefschetz numbers for four distinct wreath-group permutations and compares with the exterior-power module characters; \(188\) character checks passed. The exact recorded stdout is in `verify_output.txt`. These finite checks corroborate, but do not replace, Steps 1--4, which prove all parameters and integral assertions.

## Relationship to prior work
Deshpande and Singh (arXiv:2001.05448) classify higher independence complexes for complete multipartite graphs, fully whiskered graphs, paths, cycles, and perfect trees. The present connected block graph \(K_1\vee(kK_s)\) for \(k,s\ge2\) is neither complete multipartite nor a fully whiskered graph; their listed classifications do not imply this precise mixed-dimensional homotopy type or the integral wreath-product module. Sawant's 2026 theorem (arXiv:2605.25150) proves vertex decomposability for **trees**, not these clique windmills. Das, Roy, and Saha (arXiv:2501.01112) establish algebraic regularity and projective-dimension identities for chordal graphs, not this explicit topology or symmetry lattice; their indexing \(t\) equals our \(r+1\). Patra and Roy (arXiv:2311.07308), Theorem 3.8, give general **field-valued graded Betti numbers** for ideals of graph joins, hence may provide an alternative route to the nonequivariant **dimensions** by Hochster's formula after specialization. They do not establish the asserted homotopy splitting or the integral automorphism modules. A prior general chordal-graph wedge theorem supplies existence of some sphere wedge, not the two distinct dimensions and exact group modules. An accessible earlier statement about \(t\)-clique-free complexes on the same windmills forbids selected \(t\)-cliques, a different face condition from bounding **all connected-component cardinalities** by \(r\); it does not imply the present conclusion.

## Limitations
This is an ordinary (nonequivariant) homotopy classification together with an integral equivariant **homology** classification, not an equivariant homotopy equivalence or canonical equivariant wedge decomposition. The result covers equal clique sizes \(s\ge2\) and \(k\ge2\), not arbitrary block graphs or unequal block sizes. Generic graded Betti formulas may subsume some nonequivariant ranks; novelty asserted here is the explicit full phase classification and integral group action together. The finite verifier uses mod-two ranks and Lefschetz character computations; integral torsion-freeness and module formulas come from the displayed chain and homotopy proof, not from these checks. Independent external audit has not occurred.

## References
- R. Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, arXiv:2605.25150, first posted 2026-05-24. https://arxiv.org/abs/2605.25150
- P. Deshpande and A. Singh, *Higher Independence Complexes of Graphs and Their Homotopy Types*, arXiv:2001.05448, first posted 2020-01-15. https://arxiv.org/abs/2001.05448
- S. K. Patra and A. Roy, *Graded Betti Numbers of a Hyperedge Ideal Associated to Join of Graphs*, arXiv:2311.07308, first posted 2023-11-13. https://arxiv.org/abs/2311.07308
- K. K. Das, A. Roy and K. Saha, *Stanley-Reisner Ideals of Higher Independence Complexes of Chordal Graphs*, arXiv:2501.01112, first posted 2025-01-02. https://arxiv.org/abs/2501.01112
