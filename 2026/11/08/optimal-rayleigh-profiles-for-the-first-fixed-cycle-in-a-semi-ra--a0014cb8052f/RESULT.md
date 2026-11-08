# Optimal Rayleigh profiles for the first fixed cycle in a semi-random graph

## Finding

**Theorem.** Fix an integer \(\ell\geq3\). In the online semi-random graph process on \(n\) labelled vertices, each round independently offers a uniformly random vertex \(U\); observing \(U\) and the existing graph, Builder chooses any other vertex \(V\) and adds edge \(UV\). Let \(T_{n,\ell}\) be the first round in which a (not necessarily induced) simple cycle \(C_\ell\) is present. The supremum ranges over all adaptive (including randomized) strategies.

For every real \(x\geq0\),

\[
\lim_{n\to\infty}\sup_{\mathcal A}\Pr_{\mathcal A}\{T_{n,\ell}\le\lfloor x\sqrt n\rfloor\}
=1-\exp\!\left(-\frac{\ell-1}{2\ell-3}x^2\right).
\]

For every fixed \(L>0\), uniformly over integer \(0\leq t\leq L\sqrt n\), the error in the corresponding finite-\(n\) survival law is \(O_{\ell,L}(n^{-1/2})\). One deterministic online strategy achieves this bound simultaneously for all those horizons.

**Sharp exposure lemma.** For any finite simple graph \(G\), let \(a_\ell(G)\) be the number of vertices that are endpoints of a simple path with exactly \(\ell-1\) edges. Then

\[
a_\ell(G)\le\frac{2\ell-2}{2\ell-3}|E(G)|.\]

Equality holds for every disjoint union of \((2\ell-2)\)-vertex paths. In a \(C_\ell\)-free graph, these exposed vertices are exactly the offered vertices from which Builder can complete \(C_\ell\) in one added edge.

## Assumptions and scope

The graph starts with no edges. The new offer at each round is independent and uniform on the same fixed \(n\)-point vertex set. Builder has arbitrary adaptive choice of the second endpoint, subject only to choosing a distinct vertex. Multiple edges are irrelevant: ignoring multiplicity only decreases the number of distinct edges available for path formation. The target \(\ell\) is fixed while \(n\to\infty\); the theorem does not assert uniformity in a growing \(\ell\), uniqueness of optimal strategies, or a hitting-time law under a fixed restricted partner set.

A vertex is **exposed** if it is an endpoint of some simple path of length \(\ell-1\) in the current underlying simple graph. While the graph is \(C_\ell\)-free, adding an edge from an exposed vertex to the opposite endpoint of such a path creates the desired cycle. Conversely, every newly formed \(C_\ell\) contains the added edge, so its offered endpoint was exposed before the round.

Put \(r=2\ell-3\) and \(c=(r+1)/r\).

## Proof

**Step 1: exposure inequality, including the sharp boundary.** Partition \(G\) into connected components. An isolated vertex has no exposure. In any component containing a cycle, the number of vertices does not exceed the number of edges, hence its exposed-vertex count is at most its edge count.

Consider a tree with \(e\) edges. If \(e\leq2\ell-4\), its diameter is at most \(2\ell-4\); a central vertex has eccentricity at most \(\ell-2\). This central vertex cannot begin a simple path of length \(\ell-1\). Thus at most \(e\) of its \(e+1\) vertices are exposed. If \(e\geq2\ell-3=r\), all exposed vertices number at most \(e+1\leq(1+1/r)e\). Summing componentwise gives \(a_\ell(G)\leq c|E(G)|\). The path with \(r\) edges has \(r+1\) vertices, every one of which starts a path of length \(\ell-1\), so equality is attained (also by disjoint unions).

**Step 2: universal survival lower bound.** Prior to a successful round, the current graph has at most \(j\) distinct edges after \(j\) rounds. From Step 1, the conditional probability of success at round \(j+1\) is at most \(cj/n\). Therefore, for integer \(t\leq L\sqrt n\) and large \(n\), every strategy satisfies

\[
\Pr(T_{n,\ell}>t)\geq Q_n(t):=\prod_{j=0}^{t-1}\left(1-\frac{cj}{n}\right).
\]

The product has \(\log Q_n(t)=-ct(t-1)/(2n)+O_L(t^3/n^2)\), uniformly over these horizons.

**Step 3: sharp constructive policy.** Keep a distinguished family of vertex-disjoint paths, each of exactly \(r\) edges (completed templates), together with at most one currently growing path of fewer than \(r\) edges. Whenever the offered vertex is exposed, join it to a suitable path endpoint and stop. Otherwise, if the offered vertex has never appeared in an edge, use it to advance the growing path: if no partial path exists, join the offered vertex to a second unused vertex; otherwise join it to one endpoint of the partial path. When the partial path reaches \(r\) edges, declare it a completed template and begin a new one. If the offered vertex already appeared in an edge but is not exposed, join it to any unused vertex, calling that round wasted. All these additions are to a previously unused vertex, hence no cycle is created before a deliberate success; completed templates remain present, although they may acquire auxiliary pendant edges. Sufficient unused vertices exist throughout the \(O(\sqrt n)\) window.

Let \(W_j\) count wasted rounds among the first \(j\) unsuccessful rounds, and set it to zero after a success for the purpose of expectation bounds. Before step \(i\), at most \(2(i-1)\) vertices have appeared in edges. Thus the probability of a wasted round, even conditional on a history of no success, is bounded by \(2(i-1)/n\), and

\[
\mathbb E W_t\leq\frac{t(t-1)}n=O_L(1).
\]

On a surviving history after \(j\) rounds, at least \(\lfloor(j-W_j)/r\rfloor\) completed path templates exist. All their \((r+1)\) distinct vertices remain exposed. Hence the current exposure count \(a_j\) obeys

\[
 c j-cW_j-(r+1)\leq (r+1)\Big\lfloor\frac{j-W_j}{r}\Big\rfloor\leq a_j\leq cj.
\]

**Step 4: uniform error control.** Let \(S_j=\Pr(T_{n,\ell}>j)\) under the constructive strategy. The conditional success probability is exactly \(a_j/n\) along a surviving history. Therefore

\[
 S_{j+1}=S_j\Big(1-\frac{cj}{n}\Big)
 +\frac1n\mathbb E\big[\mathbf1_{\{T_{n,\ell}>j\}}(cj-a_j)\big].
\]

By Step 3, the final term lies between zero and \([c\mathbb E W_j+(r+1)]/n\). Combining the recurrence with the product for \(Q_n\), using all factors at most one, shows

\[
0\leq S_t-Q_n(t)\leq\frac{1}{n}\sum_{j=0}^{t-1}\left(c\frac{j(j-1)}n+r+1\right)
=O_{\ell,L}(n^{-1/2}).
\]

Finally, \(Q_n(\lfloor x\sqrt n\rfloor)\to\exp(-cx^2/2)\), and \(c/2=(\ell-1)/(2\ell-3)\). Step 2 makes this optimal for *every* strategy; Steps 3–4 provide one policy attaining the same profile. This proves the theorem. \(\square\)

## Verification

The accompanying standard-library checker `verify.py` exhaustively tests the sharp graph inequality on all labelled graphs of orders two through six and all allowable target lengths; verifies the explicit path equality case for target lengths three through seventeen; and checks finite hazard-product approximations. Reproduce with `python3 verify.py`. These finite assertions do not replace Steps 1–4, which prove the theorem for arbitrary graph order and fixed \(\ell\).

## Relationship to prior work

The full-choice semi-random process was introduced by Ben-Eliezer et al. [1]. Behague et al. [2, Theorems 1.1–1.2] establish the fixed-subgraph appearance scale determined by degeneracy; Gao and Koerts [3, Corollary 1] establish the square-root scale for cyclic targets in the pre- and post-positional variants. Akhmejanova and Kupavskii [4, Section 4] study local subgraph appearance under limited partner choices, in particular triangles and cliques. These works identify models or first-order scales but do not state the above sharp constant and Rayleigh profile for *every fixed cycle length*.

The triangle specialization \(\ell=3\) is also a previously documented special case. The contribution here is the full all-length theorem, based on a sharp exposure classification for both tree and cyclic components, and the explicit online path-template construction. No novelty is claimed for \(\ell=3\) alone.

## Limitations

A complete earlier theorem in the wider adaptive-random-graph literature could subsume this all-cycle profile, and historical priority therefore remains provisional. The present claim covers simple cycles of one fixed length, complete endpoint choice, and the \(\sqrt n\) window only. It does not cover induced cycles, target lengths increasing with \(n\), restricted choices, or quenched variants. The finite checker validates only small cases. Independent mathematical audit has not been performed.

## References

1. O. Ben-Eliezer, D. Hefetz, G. Kronenberg, O. Parczyk, C. Shikhelman and M. Stojaković, *Semi-random graph process*, arXiv:1805.02259, first posted 2018-05-06. https://arxiv.org/html/1805.02259v2
2. N. C. Behague, T. G. Marbach, P. Prałat and A. Ruciński, *Subgraph Games in the Semi-Random Graph Process and Its Generalization to Hypergraphs*, arXiv:2105.07034, first posted 2021-05-14. https://arxiv.org/html/2105.07034v4
3. P. Gao and H. Koerts, *On the Pre- and Post-Positional Semi-Random Graph Processes*, *Journal of Graph Theory*, first published 2024-12-12. https://doi.org/10.1002/jgt.23202
4. M. Akhmejanova and A. Kupavskii, *Between the Semi-Random Process and G(n,p)*, arXiv:2610.33854, first posted 2026-10-24. https://arxiv.org/html/2610.33854v1
