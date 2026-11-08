# Poisson walls and Dirichlet component spacings at the critical window of percolated cycle squares

## Finding
Let \(G_n\) be the random spanning subgraph of the square of the cycle \(C_n^2\), with every length-one or length-two edge retained independently with probability \(1-q_n\). If \(nq_n^3\to\lambda\in(0,\infty)\), then its number \(K_n\) of connected components satisfies
\[
K_n\ \Longrightarrow\ \max\{1,Z\},\qquad Z\sim\operatorname{Poisson}(\lambda).
\]
In particular,
\[
\Pr(G_n\text{ connected})\to e^{-\lambda}(1+\lambda),\qquad
\Pr(K_n=k)\to e^{-\lambda}\frac{\lambda^k}{k!}\quad(k\ge2).
\]
The disconnected components are asymptotically contiguous cyclic arcs. More precisely, the point process of completely unbridged consecutive-vertex gaps, scaled to the unit circle, converges to a homogeneous Poisson point process of intensity \(\lambda\). Conditional on \(K_n=k\) for any fixed \(k\ge2\), choose one such gap uniformly, list the \(k\) components clockwise starting immediately after it, and divide their vertex counts by \(n\). The resulting vector converges to the \(\operatorname{Dirichlet}(1,\ldots,1)\) distribution on \(k\) coordinates.

Consequently, conditional on \(K_n=k\ge2\), the largest-component fraction converges to a random variable with cumulative distribution
\[
F_k(x)=\sum_{j=0}^{k}(-1)^j\binom{k}{j}(1-jx)_+^{k-1},\qquad 0\le x\le1,
\]
where \(u_+=\max(u,0)\), and whose mean is \(H_k/k\) with \(H_k=\sum_{j=1}^{k}1/j\). This is the classical largest-spacing formula applied to the new component limit.

The central finite-volume estimate is explicit: for every \(n\ge10\), writing \(W_n\) for the number of completely unbridged gaps,
\[
\Pr\big\{K_n\ne\max(1,W_n)\big\}\ \le\ 35nq_n^4.
\]
This comparison is what transfers the Poisson geometry of the gaps to the component structure.

## Assumptions and scope
For an integer \(n\ge10\), let \(V=\mathbb Z/n\mathbb Z\). The host graph has exactly the undirected edges \(\{i,i+1\}\) and \(\{i,i+2\}\), one of each kind for each \(i\in V\). Each host edge is deleted independently with probability \(q_n\in[0,1]\). Let \(K_n\) include isolated vertices as components.

For the gap after \(i\), define its three bridging edges
\[
E_i=\big\{\{i,i+1\},\ \{i-1,i+1\},\ \{i,i+2\}\big\},
\]
with all indices modulo \(n\). Let \(B_i\) denote the event that all three edges of \(E_i\) are deleted, and set \(W_n=\sum_{i\in V}\mathbf1_{B_i}\). A gap is called a *wall* precisely when \(B_i\) occurs. We assume the stated critical-window scaling \(nq_n^3\to\lambda\in(0,\infty)\), which entails \(q_n\to0\) and \(nq_n^4\to0\). The limit results are in distribution or probability, not almost surely.

## Proof
**1. A deterministic local rigidity event.** Consider each cyclic window of five consecutive vertices. Exactly seven host edges have both endpoints in that window: four of length one and three of length two. Define \(\mathcal E_n\) to be the event that no such window contains four or more deleted host edges. Independence, a union bound over all \(n\) windows, and a union bound over the \(\binom74=35\) choices of four edges in a window give
\[
\Pr(\mathcal E_n^c)\le 35nq_n^4.
\]
We prove the deterministic identity \(K_n=\max(1,W_n)\) on \(\mathcal E_n\).

Color each vertex by the label of its connected component. If there were a cyclic *singleton run* of one color at a vertex \(i\), the two edges \(\{i-1,i\},\{i,i+1\}\) must be deleted. In addition, among \(\{i-2,i-1\}\) and \(\{i-2,i\}\) at least one edge joins distinct components and must be deleted: if \(i-2\) has the label of \(i\), the first edge crosses, and otherwise the second crosses. The analogous reasoning on the right gives one more deleted edge among \(\{i+1,i+2\}\) and \(\{i,i+2\}\). These four edges are distinct and all occur in the window \(i-2,\ldots,i+2\), contradicting \(\mathcal E_n\). Thus, on \(\mathcal E_n\), every cyclic run of a component label has length at least two (except the trivial one-component case).

At every boundary between two such runs, the two vertices on each side lie in two different components. All three edges crossing that boundary therefore are deleted: it is a wall. Conversely, two distinct walls block every host edge between the two cyclic arcs they delimit, hence force disconnection. On \(\mathcal E_n\), if there is more than one component, every component-label run is bounded by walls, and the arcs delimited by successive walls cannot split further into smaller components: a hypothetical split would produce another component-label boundary, hence another wall inside that arc. Therefore the components coincide with these successive arcs and their number equals \(W_n\). A connected graph has at most one wall, since two walls would disconnect it, so \(K_n=1=\max(1,W_n)\) in this case. This proves the finite-volume bound and the claimed arc decomposition.

**2. A Poisson point process of walls.** Each wall has probability \(q_n^3\). Two distinct wall indicators are independent unless their gaps are adjacent in the cyclic order. Adjacent wall events share precisely one deleted edge and therefore have joint probability \(q_n^5\). Nonadjacent walls use disjoint edge sets and have joint probability \(q_n^6\). In particular
\[
\mathbb EW_n=nq_n^3,\qquad
\operatorname{Var}(W_n)=nq_n^3(1-q_n^3)+2n(q_n^5-q_n^6).
\]
For completeness, a multivariate factorial-moment calculation proves the point-process limit. Consider any fixed total \(r\) of distinct requested gap locations. Partition these locations into \(c\) maximal adjacency clusters. If the cluster sizes sum to \(r\), their required deleted-edge sets jointly contain \(2r+c\) distinct edges. For any fixed cluster shape there are \(O_r(n^c)\) position choices, and their combined probability is \(q_n^{2r+c}\). For \(c<r\), their total contribution is bounded by
\[
O_r(n^cq_n^{2r+c})=O_r((nq_n^3)^c q_n^{2(r-c)})=o(1).
\]
For \(c=r\) the requested locations are pairwise nonadjacent, and their probabilities factor as \(q_n^{3r}\). Counting those locations in disjoint rescaled arcs and using \(nq_n^3\to\lambda\) yields the joint factorial moments of the independent Poisson counts with respective means \(\lambda\) times the arc lengths. The bounds also give tightness, since total expected wall count is bounded. Thus the point process \(\sum_{i\in V}\mathbf1_{B_i}\delta_{i/n}\) converges to the homogeneous Poisson point process on the unit circle and \(W_n\Rightarrow Z\sim\operatorname{Poisson}(\lambda)\).

**3. Component counts and spacings.** The probability of \(\mathcal E_n^c\) tends to zero, so the deterministic identity in Step 1 and the convergence in Step 2 imply \(K_n\Rightarrow\max(1,Z)\), with the stated point probabilities. The connectivity limit is \(\Pr(Z\le1)=e^{-\lambda}(1+\lambda)\).

For any fixed \(k\ge2\), point-process convergence and the fact that the limiting process is simple imply convergence of the ordered cyclic spacings conditional on exactly \(k\) walls. Conditional on that count, the Poisson points are \(k\) independent uniform points on the circle. After choosing one of them uniformly as the start, the \(k\) consecutive cyclic spacings have the symmetric \(\operatorname{Dirichlet}(1,\ldots,1)\) law. On \(\mathcal E_n\) the vertex counts of the components are precisely the integer wall spacings, and after division by \(n\) their rounding error is at most \(1/n\) per coordinate. Since \(K_n=W_n\) whenever \(K_n\ge2\) on \(\mathcal E_n\), the conditional limit follows. The maximum-spacing cumulative distribution follows by inclusion–exclusion on the uniform simplex: for any specified set of \(j\) coordinates the event that they all exceed \(x\) has probability \((1-jx)_+^{k-1}\). Integrating its complementary tail gives \(\mathbb E[\max(U_1,\ldots,U_k)]=H_k/k\).

## Verification
The standalone script `verify.py` requires Python 3 standard library only and executes with `python3 verify.py`. It exhaustively enumerates every labelled subgraph of the cycle-square host on seven and eight vertices, checking the deterministic component-wall identity whenever no five-vertex window contains four deleted edges. It independently checks exact wall overlap sizes, their second factorial moment and their variance for selected rational edge-deletion probabilities. Its most recent execution reported `VERIFICATION_OK total_checks=8935 valid_configuration_checks_n7=2186 valid_configuration_checks_n8=6622`. These enumerations concern smaller finite graphs and do not prove the infinite-volume limit, which is established by the preceding analytic steps. The theorem is stated for \(n\ge10\), and the checked local combinatorics are the same there.

## Relationship to prior work
Chakraborty, Luh and Singh (arXiv:2610.42107v1, first posted October 30, 2026) derive the Poisson-isolated-vertex connectivity window when the band width grows faster than \(\log n\), and explicitly ask for the small-bandwidth critical component laws in their Section 7. Their results do not cover fixed band width two.

Federico (2024, DOI:10.1007/s11565-024-00508-6) analyzes **the same finite-range cycle model in a more general distance-dependent parametrization**. In particular the location of the connectivity threshold, the distinction between isolated vertices and completely unbridged gaps, the three-edge nature of an unbridged gap at range two, and the existence of a cut-dominated regime are already known and are not claimed as new. Federico's Theorem 2.1 and Propositions 3.1 and 4.1 are zero-one laws away from the critical window. The inspected complete article does not state the critical Poisson component count law, the connectivity value \(e^{-\lambda}(1+\lambda)\), the quantitative \(35nq_n^4\) comparison, or the Dirichlet component-spacing law. The new assertions are these sharper distributional and geometric conclusions, not the threshold itself.

Wilsher, Dettmann and Ganesh (2020) study related one-dimensional soft random geometric graphs with random vertex positions, a different underlying probability space; their published abstract emphasizes isolated vertices and uncrossed gaps. Poisson approximation and uniform-Poisson spacings are standard probabilistic tools; the new work is their application through an exact connectivity-to-wall reduction in this discrete critical regime.

## Limitations
This theorem covers the unweighted, fixed range-two cycle power with independent and identically retained edges; it does not resolve the corresponding critical laws for general fixed ranges, nonidentical probabilities, or band widths growing with \(n\). The limiting component-size vector conditional on at least two components is specified with a uniformly sampled starting wall; an arbitrary deterministic choice of starting location yields a different size-biased cyclic ordering. The historical-priority assessment cannot rule out an equivalent result under a different name, particularly within older one-dimensional network reliability literature. No independent mathematical audit has been performed.

## References
- S. Chakraborty, K. Luh and R. P. Singh, *Band Random Graphs: Connectivity, Geometry, and Transport*, arXiv:2610.42107v1, October 30, 2026. https://arxiv.org/html/2610.42107v1
- L. Federico, *Connecting probability for random bounded-range one-dimensional network*, Annali dell'Università di Ferrara 70, 1389–1403 (2024). https://doi.org/10.1007/s11565-024-00508-6
- M. Wilsher, C. P. Dettmann and A. Ganesh, *Connectivity in One-Dimensional Soft Random Geometric Graphs*, Physical Review E 102, 062312 (2020). https://arxiv.org/abs/2007.06301
