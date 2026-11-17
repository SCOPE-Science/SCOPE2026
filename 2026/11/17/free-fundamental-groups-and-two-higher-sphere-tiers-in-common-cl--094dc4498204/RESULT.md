# Free fundamental groups and two higher sphere tiers in common-clique books

## Finding
Let \(S,P_1,\ldots,P_r\) be pairwise disjoint finite vertex sets, with \(|S|=s\ge3\), \(r\ge3\) and \(|P_i|=q_i\ge3\) for every \(i\). Let \(G\) have exactly those edges contained in the complete graphs on \(S\cup P_i\); there are no edges between different private sets. Write \(X=\mathsf{CF}_3(G)\) for the simplicial complex of vertex subsets containing no three-vertex clique, and put
\[
B=\prod_{i=1}^{r}(q_i-1),\qquad A=\prod_{i=1}^{r}\binom{q_i-1}{2}.
\]
There is an integral, nonequivariant homotopy equivalence
\[
\boxed{|X|\simeq\left(\bigvee^{\binom{s}{2}}S^1\right)\vee\left(\bigvee^{sB}S^r\right)\vee\left(\bigvee^{A}S^{2r-1}\right).}
\]
Thus \(\pi_1(|X|)\cong F_{\binom{s}{2}}\) is nonabelian and free, and the only nonzero reduced integral homology groups are free of ranks \(\binom{s}{2}\), \(sB\), and \(A\) in degrees \(1,r,2r-1\), respectively. For \(s=r=q_1=q_2=q_3=3\), the homotopy type is \(\bigvee^3S^1\vee\bigvee^{24}S^3\vee S^5\).

The symmetry statement is integral. Let \(U_q=\ker(\mathbb Z^q\xrightarrow{\sum}\mathbb Z)\). The natural automorphisms permuting the \(s\) common vertices, permuting private vertices within each block, and exchanging blocks with equal cardinality act as
\[
\begin{aligned}
\widetilde H_1(X;\mathbb Z)&\cong \bigwedge^2\mathbb Z^S,\\
\widetilde H_r(X;\mathbb Z)&\cong\mathbb Z^S\otimes\bigotimes_{i=1}^r U_{q_i},\\
\widetilde H_{2r-1}(X;\mathbb Z)&\cong\bigotimes_{i=1}^r\bigwedge^2 U_{q_i}.
\end{aligned}
\]
In the first line, \(\mathbb Z^S\) denotes the vertex permutation lattice; the exterior-square basis corresponds to oriented edges on \(S\). On the second line, a transposition of two equal private blocks exchanges the corresponding tensor factors with an additional sign \(-1\). On the third line no additional block-exchange sign occurs. The core-vertex permutations act only on the \(\mathbb Z^S\) factors, and internal private permutations act by the indicated exterior-power or augmentation-lattice representations. These are canonical homology-module identifications; no equivariant homotopy splitting is claimed.

## Assumptions and scope
All graphs are finite and simple. A face \(F\) belongs to \(X\) if and only if, for each \(i\),
\[
|F\cap S|+|F\cap P_i|\le2.
\]
The hypotheses \(r,s,q_i\ge3\) intentionally separate this result from the known two-clique and shared-edge cases. In particular, the common clique contains triangles and the graph contains induced diamonds formed by two common vertices and one private vertex from each of two different blocks.

For an integer \(j\ge0\), write \(E_j(P)\) for the simplicial complex on \(P\) containing exactly the subsets of cardinality at most \(j\), with its empty face. For a disjoint family of complexes, their join is denoted by \(*\).

## Proof
**1. An exact cover determined by the common clique.** Define
\[
K=\mathop{*}_{i=1}^{r}E_2(P_i),\qquad L=\mathop{*}_{i=1}^{r}E_1(P_i)\subseteq K,
\]
and let \(Q=E_2(S)\) be the complete graph on the common vertices regarded as a one-dimensional complex (not its clique complex). The face condition implies the exact simplicial equality
\[
X=K\ \cup\ \bigcup_{u\in S}(u*L)\ \cup\ Q.
\]
Indeed, a face with no common vertex uses at most two vertices from each private block, a face with exactly one common vertex uses at most one per private block, a face with exactly two common vertices has no private vertices, and a face with three common vertices is forbidden. Each intersection in this equality is already correctly represented by the common subcomplexes.

**2. The two join factors.** The complex \(E_2(P_i)\) is the complete graph on \(q_i\) vertices, with first integral homology the free lattice \(\bigwedge^2U_{q_i}\) of rank \(\binom{q_i-1}{2}\). It is a wedge of that many circles. The complex \(E_1(P_i)\) consists of \(q_i\) isolated points, with reduced zeroth integral homology \(U_{q_i}\) of rank \(q_i-1\). Iterating the join equivalence for based finite complexes yields
\[
K\simeq\bigvee^{A}S^{2r-1},\qquad L\simeq\bigvee^{B}S^{r-1}.
\]
The same conclusion follows directly from reduced join chain complexes. Since \(r\ge3\), \(K\) is \((2r-2)\)-connected, whereas \(L\) has dimension \(r-1\). Therefore the inclusion \(L\hookrightarrow K\) is nullhomotopic: a map from an \((r-1)\)-dimensional CW complex to an \((r-1)\)-connected space is nullhomotopic. This argument also covers the small cases \(q_i=3\).

**3. Cone attachments and the fundamental group.** Set \(T=K\cup\bigcup_{u\in S}(u*L)\). Each cone on \(L\) is attached along the same inclusion \(L\hookrightarrow K\). Since that inclusion is nullhomotopic, each mapping-cone attachment adds one unreduced suspension of \(L\) up to homotopy; the inclusion remains null after earlier cone attachments because it factors through \(K\). Thus
\[
T\simeq K\vee\bigvee^{s}\Sigma L\simeq\bigvee^{A}S^{2r-1}\vee\bigvee^{sB}S^r.
\]
In particular, \(T\) is connected and simply connected. Every edge of \(Q\) joins two vertices already connected by paths in \(T\). No two-simplex of \(X\) contains any edge of \(Q\), since it would have two common vertices and a third vertex. Attaching these \(\binom{s}{2}\) edges to connected \(T\), with no further cells, therefore wedges on precisely \(\binom{s}{2}\) circles. The displayed homotopy equivalence follows integrally. The application of the cone splitting is nonequivariant; the group actions are considered separately below.

**4. Integral symmetry modules.** Identify the first homology of \(K\) in each graph factor through the augmented graph boundary \(\bigwedge^2\mathbb Z^{P_i}\to U_{q_i}\), whose kernel is naturally \(\bigwedge^2 U_{q_i}\). The reduced zeroth homology of each discrete \(E_1(P_i)\) is exactly \(U_{q_i}\). The join Künneth isomorphism is integral and natural. Exchanging two factors with reduced degrees \(d,e\) contributes the Koszul sign \((-1)^{(d+1)(e+1)}\), hence sign \(-1\) for two discrete factors and sign \(+1\) for two complete-graph factors.

Before adding the common edges, the relative group \(H_r(T,K;\mathbb Z)\) is the direct sum of the \(s\) independent shifted reduced homology groups \(\widetilde H_{r-1}(L;\mathbb Z)\). As \(H_{r}(K)=H_{r-1}(K)=0\), the relative long exact sequence gives \(H_r(T)\cong\mathbb Z^{S}\otimes\bigotimes_i U_{q_i}\) naturally for all the indicated automorphisms. Higher homology \(H_{2r-1}(T)\) is inherited from \(K\) because the cones have dimension at most \(r\). The final common edges do not change these groups.

Finally, the long exact sequence for the pair \((X,T)\) shows \(H_1(X;\mathbb Z)\cong H_1(X,T;\mathbb Z)\), since \(T\) is simply connected and its zeroth homology maps isomorphically to that of \(X\). The relative one-chains are freely generated by the oriented core edges, with no relative two-chains. Thus \(H_1(X)\cong\bigwedge^2\mathbb Z^S\) as an integral permutation module, proving the full symmetry assertions.

## Verification
The standalone `verify.py` reconstructs the graph from the stated complete blocks, enumerates every triangle, and enumerates every simplicial face by the defining avoidance condition. It calculates boundary ranks over the field of two elements and checks all predicted reduced Betti numbers and reduced Euler characteristics. It separately computes orientation-aware fixed-simplex Lefschetz numbers for a common-vertex transposition, an internal private-block transposition and (when permitted) an exchange of two equal pages. The resulting traces are compared with the stated integral homology characters. Nine parameter cases pass, including the four-page case \((s;q_1,q_2,q_3,q_4)=(3;3,3,3,3)\) and unequal page sizes. Five two-page controls check compatibility with existing results. These finite tests corroborate, but do not replace, the all-parameter proof.

## Relationship to prior work
Ghosh and Selvaraja (2026) introduced a systematic study of shellability of clique-free complexes. Their theorem for diamond-free chordal graphs does not apply here: two distinct pages together with two common vertices form an induced diamond, and the theorem gives neither the present homotopy type nor integral symmetry modules. The present family is a natural multi-page, multi-vertex-overlap chordal boundary outside that shellability hypothesis.

A previously published calculation for **two** complete graphs meeting in a common clique allows arbitrary core size and all thresholds but gives only integral homology and rational representation data; it does not treat three or more private pages. A separate published result for **arbitrarily many** cliques sharing one **edge** proves a three-tier homotopy splitting and integral modules but fixes the common overlap to two vertices; there the fundamental group is cyclic, unlike the present unbounded-rank nonabelian case. These are statement-and-implication comparisons, not claims that a title search proves novelty. The proof here develops the common-core cone decomposition with unrestricted private block sizes simultaneously in both parameters.

## Limitations
The result concerns exactly triangle avoidance for complete pages with a common clique, without edges between private blocks, and with \(r,s,q_i\ge3\). It does not classify higher clique thresholds, arbitrary chordal graphs, or multi-clique arrangements with nonidentical pairwise intersections. The wedge equivalence is nonequivariant; only the induced integral homology representations are determined. The formula uses standard cone and join methods, so an equivalent unindexed formulation under polyhedral joins or Stanley–Reisner terminology remains possible. Independent mathematical validation has not been performed.

## References
1. R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623v1 (first public version 2026-02-10), https://arxiv.org/html/2602.09623v1.
2. *Integral homology staircase and rational symmetry of two-clique sums*, publicly accessible 2026 research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-integral-homology-staircase-and-rational-symmetry-of-two-clique--2c130c6d765f.
3. *A persistent circle and two sphere families in clique-free complexes of edge-glued complete graphs*, publicly accessible 2026 research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-persistent-circle-and-two-sphere-families-in-clique-free-compl--deda11c4cbed.
4. A. Hatcher, *Algebraic Topology*, Cambridge University Press (2002), Chapters 0–2 (standard CW attachment and join arguments).
