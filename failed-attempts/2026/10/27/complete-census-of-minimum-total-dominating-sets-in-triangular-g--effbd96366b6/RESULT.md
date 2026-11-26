# Complete census of minimum total dominating sets in triangular graphs

## Finding

For every integer \(n\ge4\), consider the Johnson graph \(J(n,2)\) with vertices the two-element subsets of \([n]=\{1,\ldots,n\}\), adjacent when they intersect in one element. A *total dominating set* \(D\) is a subset of its vertices such that every vertex, including those in \(D\), has a distinct adjacent vertex in \(D\). Define \(A_n\) to be the number of total dominating sets of minimum cardinality, with the labels \([n]\) fixed.

**Theorem (classification and enumeration).** Write \(n=3k+r\), where \(0\le r\le2\). For every \(n\ge4\),

\[
\gamma_t(J(n,2))=\left\lceil\frac{2(n-1)}3\right\rceil,
\]

and

\[
A_n=\frac{n!}{2^k k!}\begin{cases}
1+\dfrac{25}{6}k(k-1)+\dfrac{16}{9}k(k-1)(k-2),&r=0,\\[4pt]
1,&r=1,\\[4pt]
\dfrac{4k}{3},&r=2.
\end{cases}
\]

There is also an exact classification of the sets counted. Interpret \(D\) as the edge set of a simple graph \(H_D\) on the fixed vertex set \([n]\). When \(n=3k\), \(H_D\) is either a disjoint union of \(k\) copies of the three-vertex path \(P_3\), or has one isolated vertex together with either one tree on five vertices and \(k-2\) copies of \(P_3\), or two trees on four vertices and \(k-3\) copies of \(P_3\). Impossible alternatives with negative component counts are omitted. When \(n=3k+1\), it has one isolated vertex and \(k\) copies of \(P_3\). When \(n=3k+2\), it has one isolated vertex, one tree on four vertices and \(k-1\) copies of \(P_3\). Every graph in this list corresponds to a distinct minimum total dominating set; every minimum total dominating set arises this way.

In particular, an isolated underlying vertex occurs in every minimum set if \(n\not\equiv0\pmod3\). If \(n=3k\), the proportion of minimum sets with no isolated underlying vertex is exactly

\[
\left(1+\frac{25}{6}k(k-1)+\frac{16}{9}k(k-1)(k-2)\right)^{-1},
\]

which tends to zero as \(k\to\infty\).

## Assumptions and scope

Graphs are finite, simple and undirected. Vertices of \(J(n,2)\) are named two-subsets, so different edge subsets of the labelled complete graph \(K_n\) are counted separately. A forest's isolated vertices are retained even when they do not occur in any selected edge. The symbol \(P_3\) denotes the path with three vertices and two edges. “Tree on four/five vertices” includes **every** labelled tree of that order; there is no restriction to stars or paths.

## Proof

**1. Exact admissibility criterion.** Regard any \(D\subseteq V(J(n,2))\) as an edge subset of \(K_n\), and put \(H=([n],D)\). We claim that \(D\) totally dominates \(J(n,2)\) if and only if (i) \(H\) has at most one isolated vertex, and (ii) \(H\) has no component consisting of a single edge \(K_2\).

For necessity, two isolated vertices \(u,v\) produce the undominated Johnson vertex \(\{u,v\}\); the unique selected edge of a \(K_2\) component has no **other** selected edge sharing an endpoint, so it too is undominated. Conversely suppose (i) and (ii). For an unselected pair \(\{u,v\}\), not both endpoints are isolated; a selected edge incident with one nonisolated endpoint is necessarily a *different* pair and dominates it. For a selected pair \(\{u,v\}\), absence of an isolated-edge component ensures that one endpoint meets another selected edge, which dominates it. This proves the equivalence without assuming minimality.

**2. The sharp component bound.** Let \(i\in\{0,1\}\) be the number of isolated vertices in an admissible graph \(H\). Let \(t=n-i\) be its number of covered vertices, \(c\) the number of its nontrivial connected components, and \(m=|E(H)|\). Each component has at least three vertices by the criterion, so \(c\le\lfloor t/3\rfloor\). Connectivity within each component yields

\[
m\ge t-c\ge t-\left\lfloor\frac t3\right\rfloor
=\left\lceil\frac{2t}3\right\rceil
\ge\left\lceil\frac{2(n-1)}3\right\rceil.
\]

The classified forests described in the theorem exist for every \(n\ge4\), satisfy both admissibility conditions, and have exactly the final number of edges. Therefore the lower bound is attained. This recovers the previously known minimum size, while the equality analysis below identifies all minimizers.

**3. Exhausting equality cases.** Set \(m=\lceil2(n-1)/3\rceil\) and suppose an admissible \(H\) has exactly \(m\) edges. If \(n=3k\), then \(m=2k\). With \(i=0\), the bounds \(3k-m\le c\le k\) force \(c=k\); all components have three vertices and all are trees, hence are \(P_3\)'s. With \(i=1\), the bounds \((3k-1)-m\le c\le k-1\) force \(c=k-1\) and \(m=t-c\), so every component is a tree. The total number of vertices above three per component is \((3k-1)-3(k-1)=2\). The only distributions of this surplus are one component of order five or two components of order four.

If \(n=3k+1\), then \(m=2k\). With \(i=0\), the component inequality demands \(c\ge k+1>\lfloor(3k+1)/3\rfloor\), which is impossible. Thus \(i=1\). We get \(t=3k\) and \(c=k\), forcing \(k\) tree components of order three.

If \(n=3k+2\), then \(m=2k+1\). Again \(i=0\) would require \(c\ge k+1>\lfloor(3k+2)/3\rfloor\), so \(i=1\). Now \(t=3k+1\) and \(c=k\); equality in \(m\ge t-c\) makes all components trees, and precisely one component has four vertices, the rest three. These arguments prove both necessity and sufficiency of the announced classification.

**4. Counting labelled components.** The number of trees on a specified \(s\)-element labelled vertex set is \(s^{s-2}\), for example by the Prüfer correspondence. If there are \(i\) isolated vertices and \(a_s\) tree components of each size \(s\ge3\), the number of labelled forests with that profile is

\[
\frac{n!}{i!}\prod_{s\ge3}\frac{(s^{s-2})^{a_s}}{(s!)^{a_s}a_s!},
\quad i+\sum_{s\ge3}sa_s=n.
\]

For \(n=3k\), the three disjoint profiles in Step 3 contribute respectively

\[
\frac{n!}{2^k k!},\qquad
\frac{125n!}{5!\,2^{k-2}(k-2)!},\qquad
\frac{16^2n!}{2!(4!)^2\,2^{k-3}(k-3)!},
\]

where a term is omitted when its factorial index is negative. Their sum simplifies to the first displayed piece. For \(n=3k+1\) the single profile contributes \(n!/(2^kk!)\). For \(n=3k+2\), it contributes \(16n!/(4!\,2^{k-1}(k-1)!)\), giving the third piece. Since a labelled edge subset specifies a unique \(H\), no configuration is counted more than once. The isolation proportion follows immediately. This completes the proof.

## Verification

The standalone source `verify.cpp` performs direct exhaustive testing of every subset of \(\binom n2\) Johnson vertices of minimum size for \(4\le n\le10\). For each candidate, it checks adjacency in the original Johnson graph to a **different** chosen vertex for every Johnson vertex, then records the component-size profile. It evaluated \(10{,}198{,}617\) candidates in total and obtained the sequence of counts

\[
(A_4,A_5,A_6,A_7,A_8,A_9,A_{10})
=(12,80,840,630,13440,277200,75600).
\]

The independent `check_formula.py` implementation counts labelled forest component profiles using factorials and Prüfer numbers and compares those counts against the simplified closed formulas for every \(4\le n\le100\). Both checks succeeded; exact per-order direct-search counts are preserved in `exhaustive_results.txt`. These finite tests are reproducibility checks only. The proof of the infinite classification is Steps 1–4 above.

## Relationship to prior work

Cornet, Dravec and Torres proved \(\gamma_t(J(n,2))=\lceil2(n-1)/3\rceil\) in their 2026 work (Theorem 14, pages 11–12). That exact minimum size is explicitly credited here, not claimed as new. Their inspected proof gives an incidence-counting lower bound and an example attaining it; the present result determines **every** minimum configuration, its labelled multiplicity and the asymptotic isolation phenomenon. Pan, Yang, Li and Xu give the equivalent total-edge-domination terminology and general complexity/tree theory, not this complete-graph census in the inspected material. Searches were made under both terminologies and the triangular-graph alias; an older equivalent census has not been ruled out conclusively.

## Limitations

This theorem classifies **minimum** total dominating sets, not all total dominating sets or the full total-domination polynomial. The object is the two-subset Johnson graph only; no formula is asserted for \(J(n,s)\) with \(s\ge3\). No independent mathematical audit has been performed. Search-index gaps or an unlocated result on total edge domination of complete graphs remain historical-priority risks.

## References

1. M. G. Cornet, T. Dravec, P. Torres, *Domination and Total Domination in Johnson graphs*, arXiv:2610.04675v1 (first public posting 2026-10-03), Theorem 14, pp. 11–12. https://arxiv.org/pdf/2610.04675v1
2. Z. Pan, Y. Yang, X. Li, S.-J. Xu, *The complexity of total edge domination and some related results on trees*, arXiv:1910.02431v2 (2019). https://arxiv.org/pdf/1910.02431
3. The classical Prüfer sequence correspondence for labelled trees, yielding \(s^{s-2}\) trees on \(s\) fixed labels.
