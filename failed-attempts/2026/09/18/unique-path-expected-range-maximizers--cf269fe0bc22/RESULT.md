# Unique BHM maximizers and a quantitative standard-to-lazy gap transfer

## Definitions

Let \(G\) be a finite connected simple graph and fix a root \(o\in V(G)\). For a connected bipartite graph let \(\mathcal H(G,o)\) be the integer-valued functions with \(f(o)=0\) and
\[
 |f(u)-f(v)|=1\qquad(uv\in E(G)),
\]
and write
\[
 \widehat h(G)=\mathbb E_{f\in\mathcal H(G,o)}(\max f-\min f).
\]
For every connected graph let \(\mathcal L(G,o)\) be the analogous set with \(|f(u)-f(v)|\le1\), and write \(h(G)\) for its expected range. Both expectations are root-independent.

Yinfeng Zhu proved in 2026 that \(\widehat h(G)\le \widehat h(P_n)\) for every connected bipartite \(n\)-vertex graph and deduced \(h(G)\le h(P_n)\) for every connected \(n\)-vertex graph. The new contribution here is (i) the equality classification for Zhu's all-connected-bipartite BHM theorem and (ii) a quantitative standard-to-lazy gap transfer. The lazy-model uniqueness statement is included as a corollary, but is **not** claimed as a wholly new theorem: Wu--Xu--Zhu (2016) already proved equality iff the tree is a path for both tree inequalities, while Zhu (2026) proves strictness for lazy height when a cycle is present.

## Theorem 1: equality in the BHM expectation theorem

For every finite connected bipartite simple graph \(G\) on \(n\) vertices,
\[
\boxed{\widehat h(G)=\widehat h(P_n)\quad\Longleftrightarrow\quad G\cong P_n.}
\]

### Single-class equality criterion

Write \(G=(B,W;E)\). Following Zhu, form the auxiliary graph \(S_B\) on \(B\), joining two vertices when they have a common neighbour in \(W\). Restriction to \(B\), with the standard rescaling, gives the weighted lazy model used in Zhu's proof. If \(K_B\) is the number of components of its full zero-edge subgraph and \(b_j=\widehat h(P_{j+1})\), Zhu compares \(\mathbb E b_{K_B-1}\) to the fair-binomial path expression.

Equality in this single-class comparison holds if and only if

1. \(S_B\) is a tree (including the one-vertex case), and
2. every edge of \(S_B\) has exactly one common neighbour in \(W\).

Indeed, Zhu's cyclic-auxiliary-graph case is strict. If \(S_B\) is a tree, every \(w\in W\) has at most two neighbours in \(B\). For an auxiliary edge \(e=uv\), let \(t_e\) be the number of vertices of \(W\) with neighbourhood exactly \(\{u,v\}\). In the weighted lazy model the edge increment is nonzero with probability
\[
 p_e=\frac{2}{2^{t_e}+2}\le\frac12,
\]
and the tree edge increments are independent. Thus \(K_B-1\) is a sum of independent Bernoulli variables with parameters \(p_e\), coupled coordinatewise below fair Bernoulli variables. Since \(b_j\) is strictly increasing, equality in expectation occurs exactly when every \(p_e=1/2\), equivalently every \(t_e=1\). The same criterion holds with \(B,W\) interchanged.

### Completion of the classification

Zhu's standard expected-range proof is a sum of the two bipartition-class comparisons, so global equality forces equality in both. Hence both \(S_B\) and \(S_W\) are trees and every auxiliary edge has opposite-class codegree one. The neighbours of any vertex form a clique in the opposite auxiliary graph; because that auxiliary graph is a tree, no vertex of \(G\) can have degree at least three. Thus \(\Delta(G)\le2\), and connectedness leaves a path or an even cycle.

For \(C_{2m}\) with \(m\ge3\), each same-class auxiliary graph is a cycle, contradicting the tree criterion. For \(C_4\), each auxiliary graph is \(K_2\), but its sole edge has two common neighbours, contradicting the codegree-one criterion. Therefore only a path attains equality. Conversely a path makes both single-class comparisons exact.

## Theorem 2: quantitative standard-to-lazy gap transfer

For connected bipartite \(G\), let
\[
 p_G=\frac{|\mathcal H(G,o)|}{|\mathcal L(G,o)|},
\]
the probability that a uniform lazy height function has no zero edge. Then
\[
\boxed{
 h(P_n)-h(G)\ge p_G\bigl(\widehat h(P_n)-\widehat h(G)\bigr).
}
\]
For an \(n\)-vertex tree, independent lazy edge increments give \(p_G=(2/3)^{n-1}\).

### Proof

For a uniform lazy height function \(f\), let \(A_f\) be its full set of zero edges and let \(K\) be the number of components of \((V(G),A_f)\). Contracting the zero-edge components gives a connected bipartite graph \(G/A_f\) on \(K\) vertices, and Zhu's contraction identity gives
\[
 h(G)=\mathbb E\,\widehat h(G/A_f).
\]
Applying the BHM inequality to each quotient,
\[
 \mathbb E b_{K-1}-h(G)
 =\mathbb E\bigl[b_{K-1}-\widehat h(G/A_f)\bigr]\ge0.
\]
On the event \(A_f=\varnothing\), of probability \(p_G\), we have \(K=n\) and \(G/A_f=G\). Keeping only this nonnegative contribution gives
\[
 \mathbb E b_{K-1}-h(G)
 \ge p_G\bigl(\widehat h(P_n)-\widehat h(G)\bigr).
\]
Zhu's contraction comparison also gives \(\mathbb E b_{K-1}\le h(P_n)\), proving the theorem.

## Corollary 3: lazy-model unique maximizer

For every finite connected simple \(n\)-vertex graph,
\[
 h(G)=h(P_n)\quad\Longleftrightarrow\quad G\cong P_n.
\]

This equality statement is not claimed here as wholly original. Wu--Xu--Zhu, *Average Range of Lipschitz Functions on Trees* (2016), Corollaries 2.6 and 2.12, already show for every tree that both the lazy height \(h\) and the standard/bipartite height \(\widehat h\) are maximized uniquely by the path. Zhu's 2026 proof of the LNR inequality is strict whenever \(G\) contains a cycle. Those two prior facts already yield the displayed all-connected lazy equality classification. Theorem 2 above nevertheless gives a new quantitative implication in the bipartite setting and an alternative proof for nonpath trees.

## Relation to prior work and originality scope

- Yinfeng Zhu, *Paths maximize the expected range of graph-indexed random walks* (arXiv:2609.19728v1), proves the BHM expectation inequality for every connected bipartite graph and derives the LNR inequality for every connected graph, with strictness in the lazy model for graphs containing a cycle. Zhu does not state the complete BHM equality classification above.
- Yaokun Wu, Zeying Xu, and Yinfeng Zhu, *Average Range of Lipschitz Functions on Trees* (Moscow Journal of Combinatorics and Number Theory 6(1), 2016, 96--116), prove the two conjectured inequalities for trees and explicitly state equality iff the tree is the path in Corollaries 2.6 and 2.12. Those tree equality cases are prior work and are no longer claimed as a residual uncertainty.
- Bok and Nešetřil extend the inequalities to unicyclic graphs. The theorem here is different in scope: it classifies equality for every connected bipartite graph in the newly proved BHM theorem and gives a quantitative gap transfer for every connected bipartite graph.

Targeted searches did not locate the all-connected-bipartite equality criterion or the displayed quantitative gap-transfer inequality before this record. Originality is asserted only for those two contributions.

## Limitations

- The equality result concerns the expectation form of BHM, not the stronger stochastic-domination conjecture.
- The gap-transfer factor \(p_G\) can be exponentially small; no sharp graph-independent stability gap is claimed.
- The lazy unique-maximizer statement is retained as a corollary for completeness but is not claimed as new after correcting the 2016 attribution.
- The 2026 motivating source is very recent, so contemporaneous unindexed work remains a residual originality risk.

## Sources

1. Y. Zhu, *Paths maximize the expected range of graph-indexed random walks*, arXiv:2609.19728v1, 2026. https://arxiv.org/abs/2609.19728
2. Y. Wu, Z. Xu, Y. Zhu, *Average Range of Lipschitz Functions on Trees*, Moscow J. Combin. Number Theory 6(1) (2016), 96--116. https://zhuyinfeng.org/Data/Preprints/MJCNT16.pdf
3. J. Bok, J. Nešetřil, *Graph-indexed random walks on pseudotrees*, Electronic Notes in Discrete Mathematics 68 (2018), 263--268. https://doi.org/10.1016/j.endm.2018.06.045
