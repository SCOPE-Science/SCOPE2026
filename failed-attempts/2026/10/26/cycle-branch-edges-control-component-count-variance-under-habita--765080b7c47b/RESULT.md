# Cycle–branch edges control component-count variance under habitat-site retention

## Finding

**Theorem (unicyclic habitat variance comparison and sharp quota).** Let \(G\) and \(H\) be connected simple unicyclic habitat networks, each on \(n\ge 3\) vertices, with equal degree multisets and unique cycles of the same length \(\ell\). Write \(B(G)\) for the number of edges joining a cycle vertex to a noncycle vertex. A retained habitat component is a nonempty connected component of the subgraph induced by the surviving sites; the count is zero if no sites survive. Denote its count by \(C_G\) or \(C_H\).

**Independent-site protocol.** Every vertex survives independently with common probability \(p\in(0,1)\). Then
\[
\mathbb E C_G=\mathbb E C_H=np-np^2+p^\ell,
\]
and
\[
\operatorname{Var}(C_G)-\operatorname{Var}(C_H)
=-2\bigl(B(G)-B(H)\bigr)p^{\ell+1}(1-p).
\]
In particular, the strict ordering of the two variance curves never changes with \(p\), and the variance detects the difference in numbers of cycle–branch edges even though mean component counts and degree multisets agree.

**Fixed-quota protocol.** Choose exactly \(k\) of the \(n\) vertices uniformly without replacement. For every integer \(j\ge0\), set \(a_j=\binom{n-j}{k-j}/\binom nk\) when \(j\le k\), and \(a_j=0\) when \(j>k\) (so all out-of-range intersection probabilities are zero). For every integer \(0\le k\le n\),
\[
\mathbb E C_G=\mathbb E C_H=k-na_2+a_\ell,
\quad
\operatorname{Var}(C_G)-\operatorname{Var}(C_H)
=-2\bigl(B(G)-B(H)\bigr)(a_{\ell+1}-a_{\ell+2}).
\]
When \(n\ge\ell+2\) and \(B(G)\ne B(H)\), the fixed-quota variance difference is exactly zero for \(k\le\ell\) and is strictly nonzero, with the opposite sign to \(B(G)-B(H)\), for every \(\ell+1\le k\le n-1\). Thus \(k=\ell+1\) is a sharp sampling-budget threshold for distinguishing the branch-boundary count by component-count variance within degree-matched unicyclic networks of known girth.

**Sharp network-order witness.** At least six vertices are needed for two such networks with different \(B\). At six, the edge lists
\[
E(G)=\{02,12,13,14,24,35\},\qquad
E(H)=\{01,02,03,34,35,45\}
\]
(where \(uv\) denotes the edge between vertices \(u\) and \(v\)) give connected unicyclic networks with degree multiset \((1,1,2,2,3,3)\) and \(\ell=3\), but \(B(G)=2\) and \(B(H)=1\). At independent retention \(p=1/2\) they have identical mean \(13/8\) and variances \(27/64\) and \(31/64\), respectively. Under fixed retention of \(k=4\) vertices their variances are \(32/75\) and \(14/25\), respectively, whereas all variances coincide at \(k\le3\).

## Assumptions and scope

Networks are finite, labeled, simple, undirected, connected and unicyclic; all potential habitat edges are immutable. Sites are either independently retained with homogeneous probability or chosen uniformly subject to an exact retained-site census. Surviving habitat components use **induced** surviving edges, with no secondary species dispersal, rescue, or demographic dynamics. The two compared networks have identical vertex counts, degree multisets, and cycle lengths. The theorem does not require isomorphism or the same attachment sites. The quota threshold requires \(n\ge\ell+2\); without enough noncycle sites, different branch-boundary counts cannot be realized by degree-matched pairs.

## Proof

Write \(X\) for the number of retained vertices, \(Y\) for the number of edges whose two endpoints survive, and \(Z\) for the indicator that **all** vertices of the unique cycle survive. Every induced subgraph of a unicyclic graph is a forest unless it contains that entire unique cycle, in which case its cycle rank equals one. Euler's component identity therefore holds pointwise:
\[
C=X-Y+Z.
\]
For exchangeable vertex retention, let \(a_j\) denote the probability that an arbitrary prescribed set of \(j\) distinct vertices all survive. For the Bernoulli protocol \(a_j=p^j\); for the fixed-quota protocol these are the hypergeometric probabilities in the finding. A unicyclic graph has exactly \(n\) edges. Consequently
\[
\mathbb E C=\mathbb E X-na_2+a_\ell.
\]

Expand the variance:
\[
\operatorname{Var}(C)=\operatorname{Var}(X-Y)+\operatorname{Var}(Z)
+2\operatorname{Cov}(X,Z)-2\operatorname{Cov}(Y,Z).
\]
The first term is determined by \(n\), the edge count \(n\), and \(\sum_v\binom{\deg(v)}2\): \(Y\) is a sum of edge-survival indicators, and two distinct edges involve either three distinct endpoints when incident or four when disjoint. The mixed moments of \(X,Y\) similarly depend only on numbers of incident vertex–edge pairs (there are \(2n\)) and all other pairs. Therefore \(\operatorname{Var}(X-Y)\) agrees for the degree-matched graphs, for **either** sampling protocol. The Bernoulli probability that all cycle sites survive is \(a_\ell\), as is its fixed-quota counterpart. The variance of \(Z\), and \(\operatorname{Cov}(X,Z)\), depend only on \(n\), \(\ell\), and the \(a_j\), since \(\mathbb E XZ=\ell a_\ell+(n-\ell)a_{\ell+1}\); thus these terms agree too.

There are exactly \(\ell\) edges with two cycle endpoints, exactly \(B(G)\) edges with one cycle endpoint, and \(n-\ell-B(G)\) edges with no cycle endpoint. Thus
\[
\mathbb E(YZ)=\ell a_\ell+B(G)a_{\ell+1}
+(n-\ell-B(G))a_{\ell+2}.
\]
Since \(\mathbb E Y=na_2\) and \(\mathbb E Z=a_\ell\) agree for both graphs, the difference of \(\operatorname{Cov}(Y,Z)\) equals \((B(G)-B(H))(a_{\ell+1}-a_{\ell+2})\). The displayed variance differences follow immediately. In the independent model, \(a_{\ell+1}-a_{\ell+2}=p^{\ell+1}(1-p)>0\). With fixed quota \(k\le\ell\) both probabilities vanish. If \(n\ge\ell+2\) and \(\ell+1\le k\le n-1\), then
\[
a_{\ell+1}-a_{\ell+2}
=a_{\ell+1}\frac{n-k}{n-\ell-1}>0,
\]
proving the exact quota boundary.

For sharpness in network order, if \(n\le5\), every unicyclic graph has at most two vertices outside its unique cycle. With none, \(B=0\); with one, necessarily \(B=1\). With two, there are just two structural patterns: two separate cycle-attached leaves give \(B=2\) and **two** degree-one vertices, whereas a two-edge pendant path gives \(B=1\) and **one** degree-one vertex. Hence degree-matched networks with the same cycle length cannot have different \(B\) when \(n\le5\). The two explicit six-vertex graphs have the stated adjacency sets, a three-cycle, the same degree multiset, and different branch-boundary counts, completing the sharpness proof.

## Verification

Run `python3 verify.py` using the Python standard library; it writes exact rational component moments and checks all supplied formulas against complete enumeration of retained subsets for the two six-vertex witnesses at every fixed budget and five distinct Bernoulli probabilities. It also exhaustively inspects all labeled connected unicyclic graphs on three through five vertices, groups them by degree multiset and cycle length, and checks the variance comparison within every group at each internal quota and at Bernoulli probability \(1/2\). The saved output `verification.json` records inputs and exact fractions. The analytical proof establishes the all-order, all-probability theorem independently of the finite tests.

## Relationship to prior work

Keitt, Urban and Milne (1997) motivate graph-based analysis of landscape fragmentation and connectivity at multiple spatial scales. Hoyle (2005) empirically emphasizes spatial aggregation and disconnected habitat communities. Those publications motivate the **component-count observable**, not the stated site-percolation variance comparison. Dossou-Olory (2019) studies the total number of connected induced subgraphs and unicyclic extrema; that quantity differs from the number of connected components of a **random** induced subgraph. Classical runs-on-a-circle distributions cover a pure cycle under uniform Bernoulli or quota sampling, but a pure cycle has \(B=0\); they do not supply the degree-matched, boundary-edge-sensitive unicyclic comparison presented here. Prior work on component–triangle covariance under **bond** percolation addresses a different random object. Originality is a literature comparison, not a certification of absence from all mathematics literature.

## Limitations

The observable is an idealized, exactly known population variance, not a noisy empirical estimator. Degree multiset, cycle length, and retained-site protocol must be known. Only **differences** in \(B\) are identified from pairwise variance comparisons under the stated matching conditions; the theorem does not identify a full graph, attachment placement, component-size distribution, or the number of noncycle vertices attached at a particular cycle site. Networks with \(B(G)=B(H)\) have equal variances even if they are nonisomorphic. Dependence between surviving sites, general graphs with multiple cycles, time-dependent colonization, and unknown sampling probabilities are outside scope. Independent literature validation has not been performed.

## References

1. Keitt, T. H., Urban, D. L., and Milne, B. T. (1997). *Detecting Critical Scales in Fragmented Landscapes*. Conservation Ecology 1(1), article 4. https://ecologyandsociety.org/vol1/iss1/art4/
2. Hoyle, M. (2005). *Experimentally fragmented communities are more aggregated*. Journal of Animal Ecology 74(3), 430–442. First published 23 May 2005. https://doi.org/10.1111/j.1365-2656.2005.00938.x
3. Dossou-Olory, A. A. V. (2019). *Cut and pendant vertices and the number of connected induced subgraphs of a graph*. arXiv:1910.04552. https://arxiv.org/abs/1910.04552
4. Inoue, K. and Aki, S. (2010). *On the conditional and unconditional distributions of the number of success runs on a circle with applications*. Statistics & Probability Letters 80(9–10), 874–885. https://doi.org/10.1016/j.spl.2010.01.022. Bibliographic comparison only; full text not verified.
