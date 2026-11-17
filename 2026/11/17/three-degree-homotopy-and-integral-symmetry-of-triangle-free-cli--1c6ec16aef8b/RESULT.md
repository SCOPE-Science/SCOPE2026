# Three-degree homotopy and integral symmetry of triangle-free clique-join complexes

## Finding

For integers \(s\ge2\), \(n\ge2\), and \(q_i\ge3\) for \(1\le i\le n\), take the graph
\[G=K_s\vee(K_{q_1}\sqcup\cdots\sqcup K_{q_n}).\]
Here \(\vee\) denotes graph join, and \(\sqcup\) disjoint union. Its triangle-free clique complex \(X=\mathsf{CF}_3(G)\) is the simplicial complex of vertex subsets that induce no triangle. Set
\[a=\prod_{i=1}^{n}\binom{q_i-1}{2},\qquad b=\prod_{i=1}^{n}(q_i-1).\]
Then the **integral homotopy type** is
\[X\simeq \bigvee^{\binom{s}{2}}S^1\;\vee\;\bigvee^{sb}S^n\;\vee\;\bigvee^{a}S^{2n-1}.\]
All three displayed degrees are distinct and occur with positive multiplicity. For example, \(\mathsf{CF}_3(K_2\vee(K_3\sqcup K_3))\simeq S^1\vee\bigvee^8S^2\vee S^3\).

The full integral automorphism modules, as well as the rational homology of the automorphism quotient, are determined in the next sections.

## Assumptions and scope

Let \(S\) denote the \(s\)-vertex clique of universal vertices and \(L_i\) the \(q_i\)-vertex outer clique, with no edges between distinct \(L_i\). Write \(P_S=\mathbb Z[S]\) and \(V_i=\ker(\mathbb Z[L_i]\xrightarrow{\mathrm{sum}}\mathbb Z)\). Since \(n\ge2\), precisely the vertices of \(S\) are universal. Thus the full automorphism group preserves \(S\) and the collection of outer cliques, permuting equal-sized cliques. The symbols \(S^j\) denote ordinary topological spheres; all homotopy equivalences in the stated wedge formula are nonequivariant.

For every graph automorphism, the **nonzero integral reduced homology modules** are naturally
\[\begin{aligned}
\widetilde H_1(X;\mathbb Z)&\cong\bigwedge^2 P_S,\\
\widetilde H_n(X;\mathbb Z)&\cong P_S\otimes\bigotimes_{i=1}^{n}V_i,\\
\widetilde H_{2n-1}(X;\mathbb Z)&\cong\bigotimes_{i=1}^{n}\bigwedge^2V_i.
\end{aligned}\]
Permuting outer cliques in degree \(n\) includes the sign of the block permutation; permuting them in degree \(2n-1\) does not. Within each outer clique, use the natural action on its augmentation lattice. These conventions completely specify the integral representation, including for unequal \(q_i\). All other reduced integral groups vanish.

## Proof

**1. Decompose faces by universal vertices.** Put \(D_i=\mathrm{skel}_1\Delta^{q_i-1}\), the complete graph on the vertex set \(L_i\), and \(E_i=\mathrm{skel}_0\Delta^{q_i-1}\), the discrete complex with \(q_i\) vertices. Set \(A=D_1*\cdots*D_n\) and \(B=E_1*\cdots*E_n\), where \(*\) is simplicial join. A triangle-free face containing no vertex of \(S\) meets each \(L_i\) in at most two vertices, hence belongs to \(A\). A face containing exactly one vertex of \(S\) meets each \(L_i\) in at most one vertex, hence belongs to \(S_0*B\), where \(S_0\) is the discrete complex consisting of the \(s\) central vertices. A face containing two central vertices contains no outer vertex; any triple of central vertices is forbidden. Therefore
\[X=X_0\cup E_S,\qquad X_0=A\cup_B(S_0*B),\]
where \(E_S\) denotes the extra \(\binom{s}{2}\) central edges and their endpoints, and their interiors occur in no higher simplex. Both inclusions \(B\hookrightarrow A\) and \(B\hookrightarrow S_0*B\) are simplicial cofibrations.

**2. Compute the two joins.** Each \(D_i\) is a connected graph with \(q_i\) vertices and \(\binom{q_i}{2}\) edges, so \(D_i\simeq\bigvee^{\binom{q_i-1}{2}}S^1\). Each \(E_i\) is a wedge of \(q_i-1\) copies of \(S^0\), in the based homotopy sense. Joins give
\[A\simeq\bigvee^aS^{2n-1},\qquad B\simeq\bigvee^bS^{n-1},\qquad S_0*B\simeq\bigvee^{(s-1)b}S^n.\]
In particular, \(B\) is connected because \(n\ge2\); \(A\) is \((2n-2)\)-connected.

**3. Both attaching maps are null.** Since \(B\) has dimension \(n-1\), the map \(B\to A\) is nullhomotopic by the stated connectivity (including the boundary \(n=2\)). The inclusion \(B\to S_0*B\) is nullhomotopic because \(B\) lies in the cone \(\{v\}*B\) for any central vertex \(v\). The homotopy pushout of two nullhomotopic cofibrations over connected \(B\) is a wedge of the targets and \(\Sigma B\). Therefore
\[X_0\simeq A\vee(S_0*B)\vee\Sigma B\simeq\bigvee^aS^{2n-1}\vee\bigvee^{sb}S^n.\]
The complex \(X_0\) is simply connected, because \(n\ge2\). Attaching each of the \(\binom{s}{2}\) center edges between vertices already connected in \(X_0\), with no new higher simplices, wedges on one circle per edge. This proves the claimed homotopy equivalence over the integers.

**4. Determine the integral automorphism modules.** The augmented chain complex of the graph \(D_i\) identifies \(\widetilde H_1(D_i;\mathbb Z)\) with \(\bigwedge^2V_i\) inside the oriented-edge module \(\bigwedge^2\mathbb Z[L_i]\): the boundary is contraction by coordinate summation. Also \(\widetilde H_0(E_i;\mathbb Z)=V_i\). The join Künneth isomorphism is integral because every factor is free abelian. Reordering factors of a join acts with sign \((-1)^{(d_i+1)(d_j+1)}\) on reduced homology classes in degrees \(d_i,d_j\), giving sign \(-1\) for two \(E\)-factors and \(+1\) for two \(D\)-factors.

Consider the invariant pair \((X_0,A)\). The quotient \(X_0/A\cong(S_0*B)/B\) is a one-point union of \(s\) suspensions of \(B\), indexed by the central vertices. Since \(\widetilde H_n(A)=\widetilde H_{n-1}(A)=0\), the relative homology sequence supplies the natural identification
\[\widetilde H_n(X_0;\mathbb Z)\cong \mathbb Z[S]\otimes\widetilde H_{n-1}(B;\mathbb Z)\cong P_S\otimes\bigotimes_iV_i.\]
Also \(\widetilde H_{2n-1}(A)\to\widetilde H_{2n-1}(X_0)\) is an isomorphism, giving the asserted tensor of exterior-square lattices. Attaching one-dimensional center edges does not change these degrees. Finally, from the invariant pair \((X,X_0)\), since \(X_0\) is connected with \(H_1(X_0)=0\), the relative sequence identifies \(H_1(X)\cong H_1(X,X_0)\), the free oriented-edge module on the central edges, namely \(\bigwedge^2P_S\). This proves all representation statements without choosing a nonequivariant wedge splitting equivariantly.

**5. Rational automorphism quotient.** For a finite group acting simplicially on a finite complex, barycentric subdivision removes inversions; transfer then identifies rational homology of its orbit space with invariant rational homology. The augmentation module \(V_i\otimes\mathbb Q\) has no \(\mathfrak S_{q_i}\)-invariants. Likewise, \(\bigwedge^2\mathbb Q[L_i]\) has no invariants under its full symmetric group, because the transposition of the endpoints of an oriented edge reverses that edge. Thus neither the middle nor the upper homology has invariants under the product of within-clique symmetric groups. Similarly \(\bigwedge^2\mathbb Q[S]\) has no \(\mathfrak S_s\)-invariants. It follows that
\[\widetilde H_*(|X|/\operatorname{Aut}(G);\mathbb Q)=0.\]
This does **not** imply that the quotient is contractible.

## Verification

The standalone script `verify_clique_join.py` uses only the Python standard library. It independently forms all graph triangles from the edge set, enumerates all triangle-avoiding faces for six separate parameter choices, calculates every reduced mod-two boundary rank by exact bitset elimination, and computes oriented signed simplicial Lefschetz traces for automorphisms. The finite cases span two and three outer blocks, equal and unequal block sizes, and central cliques of sizes two, three, and four. For the smallest case it checks all \(144\) graph automorphisms, not just generators.

Run `python3 verify_clique_join.py` in the directory containing the script. The recorded output is `verification_output.txt`, whose first line must read `TRIANGLE_FREE_CLIQUE_JOIN_EXACT_PASS`. Results: six cases, \(1,751\) enumerated faces including empty faces, and \(255\) signed Lefschetz comparisons. All checked degrees agree with the theorem. These finite tests do not prove the unrestricted statement, which rests on the five-step homotopy and integral-chain argument above.

## Relationship to prior work

Ghosh and Selvaraja introduced and studied \(t\)-clique-free complexes and proved shellability for \(t\)-diamond-free chordal graphs. The graphs here are chordal, but **contain induced diamonds**: select two distinct central vertices and one vertex from each of two distinct outer blocks. Hence the cited shellability theorem does not apply, and its statements do not determine the three sphere multiplicities or the integral symmetry modules.

Namiq's 2026 work gives homotopy and Betti results for skeleta of chordal **clique complexes** and their Alexander duals; these are different simplicial functors from the triangle-free subset complex \(\mathsf{CF}_3(G)\). Work on edge-ring Betti tables for generalized split-join graphs concerns independence-complex data, not this explicit integral homotopy and automorphism-module calculation. A formula for a single universal vertex does not imply the additional \(\binom{s}{2}\) circles or the \(P_S\)-tensor representation when \(s\ge2\).

## Limitations

The theorem is limited to \(s\ge2\), \(n\ge2\), \(q_i\ge3\), and triangle avoidance (not all higher clique thresholds). The wedge splitting is nonequivariant; the homology modules are equivariant. No integral quotient-homology, equivariant homotopy type, or quotient contractibility is claimed. The finite computer checks are corroborative rather than a proof for infinitely many parameters. Equivalent unindexed or inaccessible literature remains a possible originality risk.

## References

1. R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1 (first public February 10, 2026), https://arxiv.org/abs/2602.09623.
2. M. R. Namiq, *Explicit Betti Numbers for Skeletons of Chordal Clique Complexes and Their Alexander Duals*, arXiv:2603.17776v2 (first public March 18, 2026), https://arxiv.org/abs/2603.17776.
3. B. A. Rather, *Graded Betti Numbers of Generalized Split--Join Graphs and Applications*, arXiv:2606.24822 (first public June 23, 2026), https://arxiv.org/abs/2606.24822. Only bibliographic and abstract evidence was accessible for this last source.
