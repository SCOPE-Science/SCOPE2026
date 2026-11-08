# Integral neighborhood homotopy and bridge persistence for partially matched clique pairs

## Finding
For every integer \(m\ge4\), let \(G_{m,t}\) have two disjoint \(m\)-vertex cliques \(A=\{a_1,\ldots,a_m\}\) and \(B=\{b_1,\ldots,b_m\}\), together with just the cross edges \(a_i b_i\) for \(1\le i\le t\), where \(0\le t\le m\). Write \(X_t=\mathcal N(G_{m,t})\) for the **open** Lovász neighborhood complex. The nested complexes \(X_0\subseteq X_1\subseteq\cdots\subseteq X_m\) have the integral homotopy types
\[
X_t\simeq
\begin{cases}
S^{m-2}\sqcup S^{m-2},&t=0,\\
S^{m-2}\vee S^{m-2}\vee S^1,&t=1,2,\\
S^{m-2}\vee S^{m-2}\vee\displaystyle\bigvee^{t^2-3t+1}S^2,&3\le t\le m.
\end{cases}
\]
The homotopy equivalences need not commute with the filtration, but the **complete reduced integral persistence module** splits into the following intervals, with endpoints included in the discrete indexing set \(\{0,\ldots,m\}\): one \([0,0]\) in degree zero; one \([1,2]\) in degree one; two \([0,m]\) in degree \(m-2\); and, in degree two, one \([3,m]\) together with \(2s-4\) intervals \([s,m]\) for each \(4\le s\le m\). When \(m=4\), the two permanent degree-two intervals and the new degree-two intervals are counted together. All unspecified reduced integral homology modules vanish. In particular the first three matching bridges induce a two-component-to-circle-to-two-sphere transition, while each later bridge adds \(2t-4\) persistent two-dimensional generators at stage \(t\).

## Assumptions and scope
Every graph is finite, simple, and loopless. The open neighborhood of a vertex \(v\) is \(N_G(v)=\{w:\{v,w\}\in E(G)\}\) and **does not contain** \(v\). The faces of \(\mathcal N(G)\) are all vertex subsets lying in some \(N_G(v)\), including the empty face. Geometric realizations are understood, reduced homology has \(\mathbb Z\)-coefficients, and interval \([p,q]\) means that the indicated free generator exists at indices \(p,p+1,\ldots,q\) with identity transition maps and is zero elsewhere. No claim is made below \(m=4\), where the simply-connected-cover argument changes.

## Proof
**1. Natural cover.** For each \(t\), let \(U_t\) be the union of the simplices on the open neighborhoods of the \(a_i\), and \(V_t\) the analogous union for \(b_i\). Then \(X_t=U_t\cup V_t\), with
\[
U_t=\partial\Delta(A)\cup\bigcup_{i=1}^t\Delta((A\setminus\{a_i\})\cup\{b_i\}),\qquad
V_t=\partial\Delta(B)\cup\bigcup_{i=1}^t\Delta((B\setminus\{b_i\})\cup\{a_i\}).
\]
In \(U_t\), every \(b_i\) for \(i\le t\) is a private cone apex over the facet \(A\setminus\{a_i\}\) of \(\partial\Delta(A)\). The cone simplex collapses onto its full base, using its faces containing this private apex, without removing any other face. Consequently \(\partial\Delta(A)\hookrightarrow U_t\) is a homotopy equivalence for every \(t\), and the same holds for \(\partial\Delta(B)\hookrightarrow V_t\). These boundary spheres have dimension \(m-2\ge2\), so both cover pieces are path-connected and simply connected. Their fundamental classes are compatible with all inclusions indexed by \(t\).

**2. Exact intersections.** For \(t=0\), the cover pieces are disjoint. If \(t\ge1\), a vertex in \(U_t\cap V_t\) must be one of the matched vertices \(a_i,b_i\) with \(i\le t\). A cross edge \(a_i b_j\) belongs to both pieces precisely when \(i\ne j\), with \(i,j\le t\); no face with two vertices of each letter can occur in both. Thus \(I_t=U_t\cap V_t\) is exactly the one-dimensional graph \(K_{t,t}\) with its diagonal matching removed: for \(t=1\), two isolated vertices; for \(t=2\), two disjoint edges; for \(t\ge3\), a connected graph with \(2t\) vertices and \(t(t-1)\) edges. The connected cases have
\[
H_1(I_t;\mathbb Z)\cong\mathbb Z^{\mu_t},\qquad \mu_t=t(t-1)-2t+1=t^2-3t+1.
\]
Inclusions \(I_t\subset I_{t+1}\) are graph inclusions. For \(t\ge3\), their induced maps on integral first homology are injective with primitive images: the cycle lattice is the kernel of the incidence boundary inside the free abelian edge-chain group, and the quotient injects into the free group on newly introduced edges.

**3. Homotopy types.** For \(t=0\), the two boundary spheres are disjoint. For \(t=1,2\), the intersection has exactly two contractible connected components. Gluing two simply connected cover pieces along such an intersection yields their wedge with one circle. For \(t\ge3\), the intersection is a connected graph, and each inclusion \(I_t\to U_t,V_t\) is nullhomotopic, since the target is simply connected and every connected graph is homotopy equivalent to a wedge of circles. Simplicial subcomplex inclusions are cofibrations, so the homotopy pushout of the null maps is
\[
U_t\vee V_t\vee\Sigma I_t\simeq S^{m-2}\vee S^{m-2}\vee\bigvee^{\mu_t}S^2.
\]
This also proves that all integral homology is torsion-free; an abstract Betti-number check alone is not being used as a homotopy proof.

**4. Persistence maps over \(\mathbb Z\).** The Mayer–Vietoris long exact sequences of the covers form a commutative diagram under \(t\mapsto t+1\). The boundary-sphere inclusions \(\partial\Delta(A)\subset U_t\subset U_{t+1}\) and analogously for \(B\) preserve two independent classes in degree \(m-2\) for every index. At \(t=1,2\), the Mayer–Vietoris connecting map identifies \(H_1(X_t;\mathbb Z)\) with \(\widetilde H_0(I_t;\mathbb Z)\cong\mathbb Z\). The inclusion \(I_1\hookrightarrow I_2\) preserves its two components and hence the circle class; \(I_2\hookrightarrow I_3\) merges them and kills it. Likewise \(t=0\to1\) kills the one reduced degree-zero class.

For \(t\ge3\) and \(m\ge5\), Mayer–Vietoris identifies \(H_2(X_t;\mathbb Z)\) naturally with \(H_1(I_t;\mathbb Z)\), while the two boundary spheres contribute degree \(m-2\). When \(m=4\), the same sequence instead gives a naturally compatible short exact sequence
\[
0\longrightarrow\mathbb Z^2\longrightarrow H_2(X_t;\mathbb Z)\longrightarrow H_1(I_t;\mathbb Z)\longrightarrow0.
\]
The left copy of \(\mathbb Z^2\) is generated by the two permanent boundary spheres. The cycle groups \(H_1(I_t;\mathbb Z)\) embed primitively as \(t\) grows, so bases may be extended at every step; the same is true after adjoining the fixed two-dimensional lattice when \(m=4\). Hence the persistence modules split over \(\mathbb Z\) into the stated intervals. Since \(\mu_3=1\) and \(\mu_s-\mu_{s-1}=2s-4\) for \(s\ge4\), the barcode multiplicities follow. This argument proves the integral inclusion maps, not just the stagewise ranks.

## Verification
The standalone standard-library script `verify_filtration.py` independently enumerates all open neighborhoods and all simplices for every \(4\le m\le8\), \(0\le t\le m\). It checks nesting, computes mod-two chain-boundary ranks at every stage, and carries out an independent simplicial persistent-homology matrix reduction using the first appearance of each simplex. Every computed reduced barcode agrees with the theorem. The numbers of nonempty simplices at the final stage are 72, 190, 466, 1092, and 2484 for \(m=4,5,6,7,8\), respectively. The recorded run ends with `ALL_MATCHED_CLIQUE_NEIGHBORHOOD_CHECKS_PASS`. These finite calculations are corroboration; Steps 1–4 above establish the theorem for every integer \(m\ge4\).

## Relationship to prior work
Kahle's 2005 public preprint [1] introduces the open-neighborhood formalism, identifies the boundary-sphere neighborhood complex of a complete clique, and establishes broader topological behavior for random graphs. It contains no controlled two-clique matching-bridge filtration. Shukla [2] treats graphs of maximum degree at most three and certain four-regular circulants; its stated classes do not provide the present arbitrarily large \(m\) matched-clique filtration. Matsushita and Wakatsuki [3] study Alexander duality with dominance complexes, not these inclusion-induced persistent modules.

The full-matching endpoint \(t=m\) has also been calculated previously, including its integral homotopy type and symmetry representation. That endpoint is **not** asserted to be new here. Likewise a previously studied neighborhood complex of \(K_m\square C_n\) for \(n\ge5\) features crown-graph interface calculations, but its cyclic-layer topology and hypotheses do not state the partial-matching progression. The additional result here is the **entire edge-addition filtration**, including the exceptional disconnected and circle stages, the exact integer inclusion maps, and the complete barcode for all \(m\ge4\). A relevant indexed cyclic-product treatment could not be inspected in full; any unpublished treatment of intermediate bridge counts remains a priority risk.

## Limitations
The stagewise wedge equivalences are nonequivariant and not asserted to give a compatible wedge splitting of spaces; it is the **integral homology persistence module** that splits into intervals. There is no claim for rectangular unequal cliques, for \(m\le3\), or for arbitrary nonmatching bridge patterns. The proof gives full homotopy types and integral persistence but not explicit higher homotopy-group representations. Published and indexed comparisons cannot establish absolute publication priority; independent mathematical review remains outstanding.

## References
[1] M. Kahle, *The neighborhood complex of a random graph*, arXiv:math/0512077, first public submission 2005-12-04; especially the definition and the complete-graph sphere in Section 1, and the random-graph theorems of Section 2. https://arxiv.org/html/math/0512077v4

[2] S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526 (2018), *Electronic Journal of Combinatorics* 26(2), P2.4 (2019). https://arxiv.org/abs/1802.04526

[3] T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:2312.02639 (2023). https://arxiv.org/abs/2312.02639
