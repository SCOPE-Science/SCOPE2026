# Integral homology of two-geodesic visibility complexes of arbitrary complete multipartite graphs

## Finding
Let \(t\ge4\), \(n_1,\ldots,n_t\ge5\), and \(G=K_{n_1,\ldots,n_t}\) with part sets \(P_i\) of cardinality \(n_i\); write \(N=\sum_i n_i\). Let \(\mathcal F(G)\) be the abstract simplicial complex of vertex subsets \(S\subseteq V(G)\) for which each nonadjacent pair \(u,v\in S\) admits two internally vertex-disjoint shortest paths with no internal vertex in \(S\). Let \(\mathcal A=\mathcal F(G)^*\) be the Alexander dual on the same \(N\)-vertex ground set, namely \(T\in\mathcal A\) precisely when \(V(G)\setminus T\notin\mathcal F(G)\).

The complete **integral homotopy type of the Alexander dual** is
\[
|\mathcal A|\simeq
\bigvee^{\binom{t-1}{2}}S^1\ \vee\
\bigvee^{\sum_{i<j}(n_i-1)(n_j-1)}S^2\ \vee\
\bigvee_{i=1}^t\bigvee^{(n_i-1)(N-n_i-1)}S^{n_i-2}.
\]
Consequently \(\mathcal F(G)\) has torsion-free reduced integral homology supported precisely in the following degrees, with coincident terms added:
\[
\begin{aligned}
\operatorname{rank}\widetilde H_{N-4}(\mathcal F(G);\mathbb Z)&=\binom{t-1}{2},\\
\operatorname{rank}\widetilde H_{N-5}(\mathcal F(G);\mathbb Z)&=\sum_{i<j}(n_i-1)(n_j-1),\\
\operatorname{rank}\widetilde H_{q}(\mathcal F(G);\mathbb Z)&=\sum_{\{i:N-n_i-1=q\}}(n_i-1)(N-n_i-1)\quad(q=N-n_i-1).
\end{aligned}
\]
All other reduced integral homology groups vanish. Since \(n_i\ge5\), the first two displayed degrees never coincide with a degree of the third kind.

For \(G=K_{5,5,5,5}\), the three reduced homology groups are \(\mathbb Z^{224}\), \(\mathbb Z^{96}\), and \(\mathbb Z^3\) in degrees \(14,15,16\), respectively. This gives a four-part phenomenon outside the earlier three-part classification.

## Assumptions and scope
Graphs are finite, simple and complete multipartite with **at least four nonempty parts of sizes at least five**. A shortest path joining two same-part vertices has length two and passes through one vertex outside that part. Such paths with distinct middle vertices are internally disjoint. Every selected adjacent pair satisfies the condition vacuously. A simplicial join includes the empty simplex, and a wedge \(\bigvee^m S^d\) denotes \(m\) copies of the based \(d\)-sphere. Homology has integral coefficients unless another coefficient ring is explicitly specified.

## Proof
**1. Exact Alexander-dual face condition.** For a selected set \(S\), let \(T=V(G)\setminus S\). The two-clear-path condition fails at part \(P_i\) exactly if \(S\cap P_i\) has at least two vertices and fewer than two unselected vertices lie outside \(P_i\). Equivalently,
\[
T\in\mathcal A\quad\Longleftrightarrow\quad
\exists i:\ |T\cap P_i|\le n_i-2\text{ and }|T\setminus P_i|\le1.
\]
This is an equivalence, not only a necessary condition.

**2. Decomposition into pair spaces.** Let \(D_i\) be the discrete zero-dimensional complex on \(P_i\). Let \(K_i=\operatorname{sk}_{n_i-3}(\Delta^{n_i-1})\), the complex of subsets of \(P_i\) of size at most \(n_i-2\). For \(i<j\), put
\[
X_{ij}=(K_i*D_j)\cup(K_j*D_i).
\]
The face characterization in step 1 shows \(\mathcal A=\bigcup_{i<j}X_{ij}\): every nonempty face lies in at most two parts, and when two parts occur at least one contributes only a single vertex. If two distinct pair spaces share an index \(i\), their intersection is exactly \(K_i\); pair spaces with disjoint indices have disjoint geometric realizations. All triple and higher intersections belonging to a common star remain \(K_i\). Thus this is a graph-of-spaces gluing over the complete graph on the part indices.

**3. Each pair-space homotopy type.** The simplex-skeleton formula gives
\[
|K_i|\simeq\bigvee^{n_i-1}S^{n_i-3}.
\]
Consequently \(|K_i*D_j|\simeq\bigvee^{(n_i-1)(n_j-1)}S^{n_i-2}\), and likewise with \(i,j\) reversed. Their intersection is \(D_i*D_j\), the complete bipartite graph \(K_{n_i,n_j}\), homotopy equivalent to \(\bigvee^{(n_i-1)(n_j-1)}S^1\). Because \(n_i,n_j\ge5\), both join spaces are simply connected. Therefore both maps from their connected one-dimensional intersection are nullhomotopic. As these inclusions are simplicial cofibrations, the homotopy pushout is the wedge of the two join spaces and the suspension of the intersection. Hence
\[
|X_{ij}|\simeq
\bigvee^{(n_i-1)(n_j-1)}S^{n_i-2}
\vee\bigvee^{(n_i-1)(n_j-1)}S^{n_j-2}
\vee\bigvee^{(n_i-1)(n_j-1)}S^2.
\]

**4. Graph-of-spaces gluing.** For every incidence \(i\in\{i,j\}\), the map \(K_i\hookrightarrow X_{ij}\) is nullhomotopic: choose a vertex of \(D_j\) and cone off \(K_i\) inside \(K_i*D_j\). The ordinary union in step 2 is homotopy equivalent to the homotopy colimit of its vertex/edge incidence diagram, since all the relevant subcomplex inclusions (including the disjoint union \(K_i\sqcup K_j\hookrightarrow X_{ij}\)) are cofibrations. Replace the incidence maps by homotopic constant maps. For a connected graph with vertex spaces \(K_i\), edge spaces \(X_{ij}\), and null incidence maps, the graph-of-spaces mapping-cylinder construction splits as the wedge of its edge spaces, \(\deg(i)-1\) suspensions of each vertex space, and one circle per independent cycle of the underlying graph. This follows by first attaching the edge spaces along a spanning tree, using the null-map homotopy-pushout formula at each attachment, and then attaching each remaining edge; the latter creates one additional circle. For the complete graph on \(t\) vertices, \(\deg(i)=t-1\) and the cycle rank is \(\binom{t-1}{2}\). Therefore
\[
|\mathcal A|\simeq
\bigvee_{i<j}|X_{ij}|\ \vee\
\bigvee_{i=1}^t\bigvee^{(t-2)(n_i-1)}S^{n_i-2}\ \vee\
\bigvee^{\binom{t-1}{2}}S^1.
\]
In degree \(n_i-2\), the sum of its pair-space and vertex-suspension multiplicities is
\[
(n_i-1)\Big(\sum_{j\ne i}(n_j-1)+(t-2)\Big)=(n_i-1)(N-n_i-1).
\]
This proves the displayed integral homotopy decomposition of \(\mathcal A\).

**5. Integral Alexander duality.** For any simplicial complex on an \(N\)-vertex set, combinatorial Alexander duality yields \(\widetilde H_q(\mathcal F(G);\mathbb Z)\cong\widetilde H^{N-q-3}(\mathcal A;\mathbb Z)\). Since \(\mathcal A\) is an explicit wedge of spheres, its cohomology is free abelian and has exactly the ranks indicated in the finding. Translating degrees proves all the integral claims. This step does not claim that \(\mathcal F(G)\) is itself a wedge of spheres.

## Verification
The standalone `verify.py` enumerates the Alexander-dual faces by the exact face criterion, builds signed-free mod-two simplicial boundary matrices, and independently computes their ranks by bit-vector elimination. It verifies five samples: part-size tuples \((5,5,5)\), \((4,4,4,4)\), \((5,5,5,5)\), \((5,6,5,5)\), and \((5,5,5,5,5)\). The first two are boundary/consistency checks beyond the new theorem's stated domain. It also enumerates **every one of the \(2^{20}=1,048,576\) vertex subsets** of \(K_{5,5,5,5}\) using the direct shortest-path condition and checks agreement with the dual face predicate. The recorded output is in `VERIFIER_OUTPUT.txt`. The finite checks test the combinatorial setup and predicted mod-two ranks; they do not certify an infinite family or establish integral torsion-freeness. The proof above supplies those unrestricted assertions.

## Relationship to prior work
Cicerone, Di Stefano, Klavžar and Zhang introduced fault-tolerant mutual visibility and studied extremal cardinalities and graph classes; their publicly available full text defines the clear-geodesic condition but does not state a homotopy or all-degree homology calculation for complete multipartite visibility complexes [1]. Previously derived cases of the two-geodesic complex include arbitrary complete bipartite graphs and **balanced three-part graphs**; neither implies the additional \(\binom{t-1}{2}\) one-sphere summands in the dual nor unequal part-size contributions at \(t\ge4\). Published classifications of *total* mutual-visibility complexes concern a distinct predicate (requiring every geodesic to be unobstructed, rather than requiring two clear geodesics) and hence do not imply this result. Related multishore path-free and cut complexes also have different face predicates. The constructive graph-of-spaces decomposition is the new step beyond those cases. Searches of the available research index and mathematical literature did not identify an equivalent broader theorem; this is not proof of absolute novelty.

## Limitations
The theorem concerns **one-fault tolerance**, meaning two clear, internally disjoint shortest paths, and requires \(t\ge4\) with each part size at least five. Different fault thresholds and smaller shores can change the dual decomposition. The homotopy classification is for the Alexander dual; only integral homology, not the full homotopy type, is asserted for the original visibility complex. No equivariant refinement or persistence calculation is asserted. Unindexed work may contain an equivalent statement; independent mathematical verification has not been carried out.

## References
[1] S. Cicerone, G. Di Stefano, S. Klavžar, G. Zhang, *Fault-tolerant mutual-visibility: complexity and solutions for grid-like networks*, arXiv:2512.01978 (first public version 2025-12-01), https://arxiv.org/abs/2512.01978 ; *Networks* (2026), https://doi.org/10.1002/net.70074.

[2] A. Björner and M. Tancer, *Combinatorial Alexander duality—a short and elementary proof*, Discrete & Computational Geometry 42 (2009), 586–593, https://arxiv.org/abs/0710.1172.

[3] Standard elementary facts used in the proof: simplex-skeleton homotopy decomposition, null-map homotopy pushouts along subcomplex cofibrations, and graph-of-spaces homotopy-colimit splitting. These are proved or specialized explicitly in steps 3–4.
