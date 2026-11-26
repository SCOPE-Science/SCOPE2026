# Two-vertex domination and diameter laws for random interval graphs

## Finding
Let \(G_n\) be the intersection graph of \(n\ge2\) independently sampled closed intervals, each obtained by sorting two independent draws from a common atomless real probability distribution. Let \(U_n\) be the number of universal vertices, \(\gamma_n\) the ordinary domination number, and \(\gamma_{t,n}\) the total domination number (set to \(\infty\) if the graph has an isolated vertex). Let \(\gamma_{c,n}\) be the connected domination number (set to \(\infty\) if the graph is disconnected), and let \(D_n\) be the diameter (\(\infty\) for disconnected graphs).

For \(n\ge9\), set \(\varepsilon_n=8(\log n)^2/n+2/n^2\). With probability at least \(1-\varepsilon_n\), **two adjacent sampled intervals together dominate every vertex**. Consequently,
\[
\Pr(\gamma_{t,n}=2)\ge1-\varepsilon_n,
\qquad \Pr(\gamma_{c,n}\le2)\ge1-\varepsilon_n,
\qquad\Pr(D_n\le3)\ge1-\varepsilon_n.
\]
For all \(n\ge2\) the following exact finite identities hold:
\[
\Pr(\gamma_n=1)=\Pr(U_n>0)=\Pr(D_n\le2)=\frac23,
\]
\[
\Pr(D_n=1)=\Pr(G_n\text{ is complete})=\frac{2^n}{\binom{2n}{n}},
\qquad\Pr(D_n=2)=\frac23-\frac{2^n}{\binom{2n}{n}}.
\]
Thus
\[
\Pr(\gamma_n=2)\longrightarrow\frac13,
\qquad \Pr(D_n=3)\longrightarrow\frac13,
\qquad\Pr(D_n=2)\longrightarrow\frac23,
\]
with both corresponding missing masses bounded by \(\varepsilon_n\), up to the exponentially small complete-graph probability for the diameter. The same asymptotic \(1/3\)-versus-\(2/3\) split holds for \(\gamma_{c,n}\). These statements are distribution-free among common atomless endpoint laws.

## Assumptions and scope
The \(2n\) endpoints are independent draws from one common atomless distribution; interval endpoints within each pair are sorted. Intervals share an edge exactly when they intersect. A dominating set uses closed neighborhoods. Total domination requires each vertex to have a neighbor in the chosen set; connected domination requires the chosen vertices to induce a connected subgraph. We define the diameter and connected domination number as \(\infty\) for a disconnected graph and total domination as \(\infty\) when isolated vertices occur. The quantitative inequality applies for \(n\ge9\); the exact identities apply for all \(n\ge2\). Probability integral transformation reduces the atomless case to iid uniform endpoints without changing endpoint order almost surely.

## Proof
**Adjacent dominating pair.** Work in uniform-quantile coordinates. Write intervals \([L_i,R_i]\), set \(t=\min_iR_i\) and \(M=\max_iL_i\), and fix \(0<b<1/2\). Except on events of total probability at most \(2nb^2\), we have \(t\ge b\) and \(M\le1-b\): each \(R_i<b\) requires both endpoints below \(b\), and each \(L_i>1-b\) requires both endpoints above \(1-b\). An interval with \(L_i\le b\) and \(R_i\ge1/2\) has probability exactly \(b\), as does one with \(L_i\le1/2\) and \(R_i\ge1-b\). By independence across intervals, the probability that either type is missing is at most \(2(1-b)^n\). On the complementary event select intervals \(I\) and \(J\) of the respective types. They are distinct or identical; if identical it is universal and one can use it together with any overlapping interval (for \(n\ge2\)) whenever such an interval is present. To avoid this edge case, observe that the two types are disjoint for \(b<1/2\) **unless** one sampled interval spans from at most \(b\) to at least \(1-b\); if this occurs, that interval is universal on the extremal-bound event and every other interval overlaps it. If no interval has both types, choose distinct \(I,J\). They intersect since \(R_I\ge1/2\ge L_J\). Their union is one interval containing \([t,M]\) whenever \(t\le M\), since \(L_I\le b\le t\) and \(R_J\ge1-b\ge M\). Every observed interval intersects \([t,M]\), hence meets \(I\) or \(J\). When \(t>M\), all observed intervals pairwise intersect, and any two distinct vertices dominate each other and the graph. In all cases an adjacent dominating pair exists. Therefore
\[
\Pr(\text{no adjacent dominating pair})\le 2nb^2+2e^{-nb}.
\]
For \(n\ge9\), the choice \(b=2\log(n)/n<1/2\) gives \(\varepsilon_n\).

**Distance and universality.** If \(t\ge M\), all intervals cover the common segment \([M,t]\), so the graph is complete. If \(t<M\), an interval \(A\) with right endpoint \(t\) and an interval \(B\) with left endpoint \(M\) are disjoint. Any common neighbor of \(A\) and \(B\) must have left endpoint at most \(t\) and right endpoint at least \(M\), so it intersects every observed interval and is universal. Hence \(D_n\le2\) holds **if and only if** a universal vertex exists, including the disconnected case under the stated convention. An adjacent dominating pair forces every graph distance to be at most three and the graph to be connected. A pair of adjacent dominating vertices is also a total dominating set.

**Exact terms.** The classical random-interval universal-vertex identity \(\Pr(U_n>0)=2/3\), valid for every \(n\ge2\), is due to Justicz, Scheinerman and Winkler and is restated in the review of Diaconis, Holmes and Janson. We use this known theorem rather than claim it as new. For completeness, all intervals intersect pairwise if and only if they share a common point (the one-dimensional Helly property). In the uniformly random matching of the \(2n\) ordered endpoint ranks this means all \(n\) matching pairs cross the cut between ranks \(n\) and \(n+1\). Exactly \(n!\) of the \((2n-1)!!\) matchings do, proving the displayed exact complete-graph probability. The previous paragraph yields \(\Pr(D_n=2)=2/3-\Pr(D_n=1)\). Finally, the high-probability adjacent-dominating-pair event forces \(\gamma_n\le2\), \(\gamma_{c,n}\le2\), \(\gamma_{t,n}=2\) and \(D_n\le3\). Combining this with the exact \(\Pr(\gamma_n=1)=2/3\) and the deterministic distance equivalence proves the asserted two-point limits and quantitative error bounds.

## Verification
The standalone Python 3 program `check.py` exhaustively enumerates the \((2n-1)!!\) equally likely endpoint pairings for each \(2\le n\le7\) (in total 146,598 pairings). It independently forms the interval-overlap graph, computes connectivity and diameter by breadth-first search, enumerates adjacent dominating pairs, checks the exact \(2/3\) universal-vertex probability and complete-graph probability, and tests the deterministic interval-covering implication on rational endpoint grids. Run `python3 check.py` in the directory containing this document. These finite checks corroborate but do not establish the arbitrary-size theorem; the proof above supplies the infinite quantifiers.

## Relationship to prior work
Justicz, Scheinerman and Winkler (1990) established the exact \(2/3\) universal-vertex law and studied disjoint interval packing. Diaconis, Holmes and Janson (2012) summarize their theorem and other random-interval-graph properties. Those known results supply the one-vertex mass and familiar model; they do not, from the accessible text inspected, provide the two-adjacent-vertex total-domination tail or the full two/three diameter law. This note does not claim discovery of the \(2/3\) law, the interval-graph representation, or the deterministic Helly property.

## Limitations
The quantitative error bound is not asserted sharp. The 1990 original article was not accessible in full; it may contain equivalent domination or diameter statements not evident in its abstract or the accessible 2012 survey. The model requires a common atomless endpoint law; no claim is made for heterogeneous, dependent or fixed-length intervals. The exact \(2/3\) identity is a cited, independently published premise, not a newly derived identity. No independent audit has been performed.

## References
1. J. Justicz, E. R. Scheinerman, P. M. Winkler, *Random Intervals*, American Mathematical Monthly 97 (1990), 881–889, DOI: 10.1080/00029890.1990.11995679.
2. P. Diaconis, S. Holmes, S. Janson, *Interval Graph Limits*, Annals of Combinatorics 17 (2013), 27–52; first available online 2012-11-21, DOI: 10.1007/s00026-012-0175-0, https://pmc.ncbi.nlm.nih.gov/articles/PMC4578824/.
3. E. R. Scheinerman, *Random interval graphs*, Combinatorica 8 (1988), 357–371, DOI: 10.1007/BF02189092.
