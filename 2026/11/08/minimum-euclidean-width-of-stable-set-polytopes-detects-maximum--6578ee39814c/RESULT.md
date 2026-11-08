# Minimum Euclidean width of stable-set polytopes detects maximum cliques

## Finding
For every nonempty finite simple graph \(G=(V,E)\) with \(\chi(G)=\omega(G)=q\), the standard stable-set polytope \(K=\operatorname{STAB}(G)\subseteq\mathbb R^V\) has **minimum Euclidean directional width**
\[
\operatorname{width}_{\min}(K)=\frac1{\sqrt q}.
\]
Moreover, the **entire set of unit directions attaining this minimum** is
\[
\left\{\frac{\mathbf1_C}{\sqrt q},-\frac{\mathbf1_C}{\sqrt q}:\ C\subseteq V\text{ is a clique of size }q\right\}.
\]
Hence there are exactly twice as many oriented minimizing directions as there are maximum cliques. The conclusion covers perfect graphs, but only the equality of the chromatic and clique numbers for \(G\), not perfection of all induced subgraphs, is required.

The minimizing directions are quantitatively rigid. For a unit vector \(u\), write \(w=W_K(u)\) and \(\delta=qw^2-1\ge0\). If \(q\ge2\) and \((q-1)w^2<1\), then some maximum clique \(C\) and sign \(\sigma\in\{-1,1\}\) satisfy
\[
\left\|u-\sigma\frac{\mathbf1_C}{\sqrt q}\right\|_2
\le\sqrt{\delta+\frac{\delta^2}{w^2}}+\sqrt q\left(w-\frac1{\sqrt q}\right).
\]
For \(q=1\), this bound holds unconditionally (without the displayed small-excess condition). In particular, for a fixed graph, unit directions whose widths converge to the minimum must converge to the finite set of maximum-clique normals; the displayed inequality gives an explicit universal modulus independent of graph order.

## Assumptions and scope
A stable set is a vertex set containing no edge of \(G\). The canonical realization \(K\) is the convex hull of \(\mathbf1_I\in\{0,1\}^V\) over **all** stable sets \(I\), including the empty set. All metric statements use the standard coordinate Euclidean inner product, not an affine-invariant metric. The polytope is full dimensional since it contains \(0\) and every standard basis vector.

For nonzero \(u\in\mathbb R^V\), let \(h_K(u)=\max_{x\in K}\langle u,x\rangle\) and \(W_K(u)=h_K(u)+h_K(-u)\). The minimum in the finding is taken over \(\|u\|_2=1\). A clique contains every edge between its distinct vertices. The assumptions are only that \(V\) is finite and nonempty, \(G\) has no loops or multiple edges, and \(\chi(G)=\omega(G)\); perfection implies but is not required for that equality.

For the comparability graph of a nonempty finite poset \(P\), \(K\) is Stanley's chain polytope \(\mathcal C(P)\). Its clique number is poset height \(h(P)\), while the poset rank-level partition is a proper coloring into \(h(P)\) antichains. Consequently \(\operatorname{width}_{\min}(\mathcal C(P))=1/\sqrt{h(P)}\), and its minimum-width directions are exactly the signed normalized indicators of longest chains. This includes the ordinal-sum ranked posets in the cited 2023 preprint.

## Proof
**1. A coloring yields a sharp lower bound.** Choose a proper coloring with precisely \(q\) nonempty stable color classes \(A_1,\ldots,A_q\). Fix a unit direction \(u\) and set \(w=W_K(u)\). In any color class, its positively weighted vertices and negatively weighted vertices are both stable sets, so
\[
 w=h_K(u)+h_K(-u)\ge\sum_{v\in A_j}|u_v|=:L_j.
\]
Let \(Q_j=\sum_{v\in A_j}u_v^2\). Then \(0\le Q_j\le L_j^2\le w^2\). Summing gives
\[
1=\sum_{j=1}^qQ_j\le qw^2,
\]
so \(w\ge1/\sqrt q\). For any clique \(C\) of size \(q\), every stable set meets \(C\) in at most one vertex. Thus \(h_K(\mathbf1_C/\sqrt q)=1/\sqrt q\) and \(h_K(-\mathbf1_C/\sqrt q)=0\), proving sharpness and its signed counterpart.

**2. Every equality direction is a signed clique indicator.** Suppose \(w=1/\sqrt q\). Equality throughout \(Q_j\le L_j^2\le w^2\) for all \(j\) forces exactly one nonzero coordinate \(u_{v_j}\) in every color class, of magnitude \(w\). If two of the selected vertices \(v_i,v_j\) are nonadjacent and have the same sign, the two-element stable set \(\{v_i,v_j\}\) gives directional width at least \(2w\). If their signs are opposite, the singleton stable sets \(\{v_i\}\) and \(\{v_j\}\) give opposite support extrema and again width at least \(2w\), independently of adjacency. Hence all selected vertices have the same sign and are pairwise adjacent. Their set is a maximum \(q\)-clique, as claimed. The argument also covers \(q=1\): with only one color class, equality forces one nonzero coordinate.

**3. Quantitative rigidity.** For arbitrary unit \(u\), set \(d_j=w^2-Q_j\ge0\). Then
\[
\sum_jd_j=qw^2-1=\delta.
\]
In each color class, choose a coordinate \(v_j\) having maximum absolute value \(m_j=|u_{v_j}|\). Since \(Q_j\le m_jL_j\le m_jw\),
\[
 m_j\ge w-\frac{d_j}{w}.
\]
Also the squared mass off this selected coordinate in class \(j\) is
\[
 Q_j-m_j^2\le Q_j\left(1-\frac{Q_j}{w^2}\right)\le d_j.
\]
Let \(z\) be the vector with coordinate \(w\operatorname{sgn}(u_{v_j})\) at each selected \(v_j\) and zero elsewhere. Then
\[
\|u-z\|_2^2\le \sum_j\left(d_j+\frac{d_j^2}{w^2}\right)
\le\delta+\frac{\delta^2}{w^2}.
\]
If \(q\ge2\) and \((q-1)w^2<1\), then \(\delta=qw^2-1<w^2\); in particular all \(m_j\) are positive. For distinct \(i,j\),
\[
m_i+m_j\ge2w-\frac{d_i+d_j}{w}\ge2w-\frac\delta w>w.
\]
As in Step 2, a nonadjacent same-sign pair or any opposite-sign pair would give width at least \(m_i+m_j>w\), which is impossible. Therefore the selected vertices form a maximum clique \(C\) and their signs agree, say \(\sigma\). The vector \(z=\sigma w\mathbf1_C\) then satisfies
\[
\left\|z-\sigma\frac{\mathbf1_C}{\sqrt q}\right\|_2
=\sqrt q\left(w-\frac1{\sqrt q}\right).
\]
The preceding estimate on \(\|u-z\|_2\) and the triangle inequality yield the displayed quantitative bound. If \(q=1\), the single selected vertex is automatically a maximum clique and the same calculation works without a small-excess assumption. This completes the proof.

## Verification
The standalone script `checks/graph_width_checker.py` independently enumerates stable sets and cliques of 810 finite graphs, with vertex counts from 1 through 9 and five graph-generation families: random comparability, complete multipartite, disjoint-clique, bipartite, and interval graphs. For each graph it separately computes the chromatic number, checks the formula on every maximum clique, checks the universal lower bound on 23,936 sampled integer directions, and checks the quantitative distance estimate in 7,284 qualifying cases. The resulting output is `STABLE_SET_MINIMUM_WIDTH_CHECKS_PASSED graphs,directions,near_cases,clique_contacts= 810 23936 7284 2391`.

These are **finite consistency tests only**. The all-order result, the complete equality classification, and the universal quantitative bound are proved analytically above. No external independent audit has been performed.

## Relationship to prior work
Stanley's chain polytope construction and the clique description of stable-set polytopes of perfect graphs are established foundations; no claim is made to those constructions. Ahmad--Fourier--Joswig (first public version 2023) and Freij-Hollanti--Lundström (first public version 2023) develop face-structure and \(f\)-vector theory of order/chain polytopes, with full-text sections inspected. Their theorems do not supply the present minimum-Euclidean-width characterization, list of all minimizing normal directions, or near-minimizer estimate. Hu--Laurent (2018) addresses linear extension complexity of stable-set polytopes for perfect graphs and the known clique inequalities, rather than Euclidean width.

Related results on maximal-inscribed-ball radii of perfect stable-set polytopes, and on the Minkowski asymmetry of such polytopes, concern different geometric invariants. The minimum directional width and all of its minimizing directions do not follow from those radius or asymmetry identities alone. The proof here needs only the equality \(\chi(G)=\omega(G)\); it therefore includes nonperfect graphs that nevertheless satisfy this equality.

## Limitations
For graphs with \(\chi(G)>\omega(G)\), the proof only yields the bounds \(1/\sqrt{\chi(G)}\le\operatorname{width}_{\min}(K)\le1/\sqrt{\omega(G)}\), and no equality or rigidity assertion is made. The quantitative inequality assumes \((q-1)w^2<1\) when \(q\ge2\); it is a sufficient near-minimum condition, not asserted sharp. An equivalent historical theorem under convex thickness, blocking polytope, or weighted stable-set support terminology may exist beyond the inspected sources. Bibliographic originality is provisional until independent literature review.

## References
1. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9--23. Original order/chain-polytope definitions.
2. I. Ahmad, G. Fourier and M. Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626, first submitted 2023-09-04. https://arxiv.org/abs/2309.01626
3. R. Freij-Hollanti and T. Lundström, *\(f\)-vector inequalities for order and chain polytopes*, arXiv:2312.13890, first submitted 2023-12-21. https://arxiv.org/abs/2312.13890
4. S. Hu and M. Laurent, *On the linear extension complexity of stable set polytopes for perfect graphs*, European Journal of Combinatorics (2018), DOI:10.1016/j.ejc.2018.02.014. https://doi.org/10.1016/j.ejc.2018.02.014
