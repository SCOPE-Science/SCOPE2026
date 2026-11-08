# Isolation-only tomography and the exact percolation-parameter ambiguity

## Finding

Let \(G=(V,E)\) be any finite labelled simple graph with \(n=|V|\ge 1\), and let \(p\in(0,1)\) be unknown. In independent site percolation, each vertex is retained with probability \(p\). The sole observed data from each trial are the labelled indicators \(I_v\) that vertex \(v\) is *retained and isolated in the induced graph*. In particular, an unretained vertex is recorded as zero, and neither the retained set nor the sampled edges are observed.

**Exact covariance and graph recovery.** Write \(q=1-p\), \(d_v=|N(v)|\), \(c_{uv}=|N(u)\cap N(v)|\), and \(\mu_v=\mathbb E I_v\). For distinct \(u,v\),
\[
\mu_v=pq^{d_v},\qquad
\operatorname{Cov}(I_u,I_v)=
\begin{cases}
-\mu_u\mu_v,&uv\in E,\\
\mu_u\mu_v(q^{-c_{uv}}-1),&uv\notin E.
\end{cases}
\]
Consequently, **negative covariance identifies exactly the edges**, positive covariance identifies exactly the nonadjacent distance-two pairs, and zero covariance identifies exactly the pairs at distance at least three (including pairs in different components). The graph is thus identified by its labelled covariance matrix even though \(p\) is unknown.

**Complete joint identifiability.** The vector of first and second moments \((\mathbb EI_v,\mathbb EI_uI_v)\) uniquely identifies both \(G\) and \(p\), except precisely when \(G\) is a disjoint union of copies of one clique \(K_k\) with \(k\ge2\) and \(p\ne1/k\). In this exceptional case there are *exactly two* possible percolation probabilities, the distinct solutions in \((0,1)\) of
\[
t(1-t)^{k-1}=p(1-p)^{k-1},
\]
and **even the full joint law** of all the isolation indicators cannot distinguish the two probabilities. For \(p=1/k\), the probability remains uniquely determined. All-edgeless graphs, including a single vertex, are identifiable.

**Finite-sample recovery.** Given \(m\) independent isolation-indicator vectors, classify \(uv\) as an edge precisely when no sample has \(I_u=I_v=1\). With \(\Delta=\max_v d_v\), for \(n\ge2\),
\[
\Pr(\widehat E=E)\ \ge\ 1-\binom n2\exp\!\bigl(-mp^2(1-p)^{2\Delta}\bigr).
\]
The decoder does not need to know \(p\) or \(\Delta\); they appear only in the performance guarantee. This is a sufficient, not an asserted minimax-optimal, bound.

## Assumptions and scope

The graph is arbitrary, simple, finite and labelled, with no graph-distribution assumption. Retention marks at distinct vertices and across trials are independent and identically distributed Bernoulli with a common unknown \(p\in(0,1)\). Isolation means degree zero *within the retained induced subgraph*, not within the original graph. The observed vector includes a zero coordinate for every missing or nonisolated vertex; labels are aligned across trials. No edge observation, sampled-set observation, knowledge of degrees, or knowledge of \(p\) is used to recover the host adjacency. All identifiability statements refer to exact population laws or moments; finite samples carry the explicitly stated uncertainty.

## Proof

**1. Isolation products.** Let \(B_v\) be the Bernoulli retention indicators. Independence gives
\[
I_v=B_v\prod_{w\in N(v)}(1-B_w),\qquad
\mathbb E I_v=pq^{d_v}.
\]
If \(uv\in E\), then \(I_uI_v=0\) identically because the two retained endpoints cannot each be isolated. If \(uv\notin E\), simultaneous isolation requires both endpoints retained and all vertices in \(N(u)\cup N(v)\) absent. Hence
\[
\mathbb E[I_uI_v]=p^2q^{d_u+d_v-c_{uv}}.
\]
Subtracting \(\mu_u\mu_v=p^2q^{d_u+d_v}\) proves the covariance identity. Since \(0<q<1\), the three stated signs are strict in their respective cases; in particular no positive and negative cases can cancel.

**2. Recovering \(p\) when a distance-two pair exists.** From the negative-covariance positions the labelled graph, all degrees, and all common-neighbor numbers are known. If two nonadjacent vertices have \(c_{uv}\ge1\), the positive joint moment gives
\[
\frac{\mathbb E[I_uI_v]}{\mu_u\mu_v}=q^{-c_{uv}},\qquad
p=1-\left(\frac{\mathbb E[I_uI_v]}{\mu_u\mu_v}\right)^{-1/c_{uv}}.
\]
All quantities are well defined, as every \(\mu_v>0\). This determines \(p\) uniquely.

**3. The remaining graphs are exactly unions of cliques.** A connected component which is not complete contains a shortest path between some nonadjacent vertices; its first three vertices form a distance-two pair. Conversely there is no distance-two pair in a disjoint union of cliques. Therefore failure of Step 2 forces every component to be complete.

If clique components have two different orders, choose vertices of distinct degrees \(d_u\ne d_v\). The positive means imply
\[
q^{d_u-d_v}=\frac{\mu_u}{\mu_v},
\]
which determines \(q\) uniquely, hence \(p\). In particular, if any isolated host vertex coexists with a larger clique then the means distinguish the parameter. If every component has order one, \(\mu_v=p\) directly.

It remains that all components are copies of \(K_k\) for the same \(k\ge2\). In each clique the isolation-vector state is either zero at every coordinate, or one at exactly one coordinate; the probability of the latter event at each specified vertex is \(f_k(p)=p(1-p)^{k-1}\). Different components contribute independent such categorical vectors. Thus the **entire observed joint law** depends on \(p\) only through the scalar \(f_k(p)\). Its derivative is
\[
f'_k(p)=(1-p)^{k-2}(1-kp).
\]
Hence it increases strictly on \((0,1/k)\), decreases strictly on \((1/k,1)\), and tends to zero at both endpoints. Every value strictly between zero and its maximum has exactly two preimages; only the maximum, at \(p=1/k\), has one. This proves necessity, sufficiency, and the exact twofold ambiguity. Since the graph was already recovered from pairwise covariance, no different graph can share the same isolation-vector law.

**4. Sample size.** For a true edge, simultaneous isolated retention is impossible, so the decoder never deletes it. For a nonedge,
\[
\beta_{uv}=\Pr(I_u=I_v=1)
=p^2q^{d_u+d_v-c_{uv}}\ge p^2q^{2\Delta}>0.
\]
The probability that it remains undetected after \(m\) independent repetitions is \((1-\beta_{uv})^m\le e^{-m\beta_{uv}}\). A union bound over at most \(\binom n2\) nonedges proves the displayed guarantee. No independent-pair assumption is needed.

## Verification

The standalone Python 3 checker `verify.py` enumerates **every labelled simple graph through five vertices** and **every vertex-retention subset** at the exact rational probabilities \(p=2/5\) and \(p=3/7\). It independently evaluates moments and signs from direct enumeration, compares them to the analytic equations, tests the clique/distance-two equivalence, and checks the identification-case partition. It records 102,616 passed assertions, with two final floating-point diagnostics for the nontrivial second parameter of \(K_3\). Run `python verify.py`; the expected final line begins with `VERIFY_OK 102616`. The proof above covers arbitrary graph size; finite enumeration is only a consistency check.

## Relationship to prior work

Chakraborty (2017, arXiv:1712.03334) analyzes the sizes of components after site percolation on pseudorandom host graphs, rather than recovery of an arbitrary fixed host from isolated retained vertices. Klusowski and Wu (2018, arXiv:1802.07773; and 2018, arXiv:1801.04339) develop graph-motif and component estimators from sampled subgraphs; their observation scheme and questions differ from repeated isolation-only labelled vectors. McGregor and Sengupta (2024, arXiv:2405.04261) reconstruct graphs from **unlabelled, potentially noisy subgraph traces** using pairing of vertices across traces; this does not imply the stated unknown-parameter identification classification in the weaker but labelled isolation-only observation model. A published note on singleton slices of Bernoulli products identifies a related two-root ambiguity in a homogeneous product model; that observation covers the equal-clique scalar mechanism but not the all-host graph recovery or exact graph-family classification. These distinctions concern the actual implications of the results, not merely title matches.

## Limitations

The theorem requires aligned vertex labels and independent repetitions of site percolation; it does not address unlabelled trace reconstruction, dependent sampling, noisy isolation indicators, heterogeneous vertex retention probabilities, or an unknown changing host. Recovery can require exponentially many repetitions in the maximal degree if \(p\) stays fixed, so the sample bound is not necessarily practical on dense graphs. The bound is sufficient, not optimal. The isolation-vector law does not resolve the explicitly characterized equal-clique probability ambiguity. A complete historical-priority search is not established; particularly, a general prior probabilistic-graphical-model identifiability theorem could contain the result implicitly. No independent mathematical validation is claimed.

## References

1. S. Chakraborty, *Site percolation on non-regular pseudo-random graphs* (arXiv:1712.03334, first posted December 9, 2017). https://arxiv.org/abs/1712.03334
2. J. M. Klusowski and Y. Wu, *Counting Motifs with Graph Sampling* (arXiv:1802.07773, first posted February 21, 2018). https://arxiv.org/abs/1802.07773
3. J. M. Klusowski and Y. Wu, *Estimating the Number of Connected Components in a Graph via Subgraph Sampling* (arXiv:1801.04339, first posted January 12, 2018). https://arxiv.org/abs/1801.04339
4. A. McGregor and R. Sengupta, *Graph Reconstruction from Noisy Random Subgraphs* (arXiv:2405.04261, first posted May 7, 2024). https://arxiv.org/abs/2405.04261
5. *Sharp identifiability boundary for singleton slices of Bernoulli products* (published result note). https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-identifiability-boundary-for-singleton-slices-of-bernoulli--452fbc6c21c4
