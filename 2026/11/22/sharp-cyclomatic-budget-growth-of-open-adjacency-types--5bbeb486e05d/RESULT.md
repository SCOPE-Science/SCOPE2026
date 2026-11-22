# Sharp cyclomatic-budget growth of open-adjacency types

## Finding

Let \(G=(V,E)\) be any finite simple undirected graph, \(A\subseteq V\) a nonempty set of marked vertices, \(m=|A|\), and \(\kappa(G)\) the number of connected components of \(G\). The cyclomatic number (feedback-edge number) is \(\beta(G)=|E|-|V|+\kappa(G)\). Write
\[
\tau(G,A)=\bigl|\{N_G(v)\cap A:v\in V\}\bigr|.
\]
All neighborhoods here are **open**, and witnesses may be in or outside \(A\). These are the realizable quantifier-free one-variable adjacency types over the named parameter set \(A\), when equality-to-a-parameter is not part of the type.

For every \(m\ge1\),
\[
\boxed{\tau(G,A)\le \min\{2^m,\ 2m+\beta(G)\}.}
\]
The coefficient and additive budget are jointly sharp: for every integer \(c\ge0\) and every \(m\ge\max\{1,3c\}\), the maximum of \(\tau(G,A)\) over finite simple graphs with \(\beta(G)\le c\) equals exactly \(2m+c\). Equality is attained by a **connected cactus** with precisely \(c\) vertex-disjoint triangular cycles.

## Assumptions and scope

The graphs are finite, undirected, and simple; isolated vertices and disconnected graphs are allowed for the upper bound. The marked set is nonempty. \(N_G(v)\) excludes \(v\). The sharpness assertion has the explicit stable parameter range \(m\ge\max\{1,3c\}\); it does not assert an exact formula for smaller marked sets or for fixed graph order. A cactus is a graph in which each edge belongs to at most one simple cycle. The bound concerns one-variable quantifier-free adjacency observations, not arbitrary higher-quantifier first-order types.

## Proof

**Upper bound.** Put \(H=G[A]\), let \(e=|E(H)|\), and let \(p\) count marked vertices of internal degree at least two in \(H\). The handshaking lemma gives \(2e=\sum_{a\in A}\deg_H(a)\ge2p\), hence \(e\ge p\).

Let \(Q=\{v\in V\setminus A:|N_G(v)\cap A|\ge2\}\) and \(q=|Q|\). The induced subgraph \(J=G[A\cup Q]\) has \(m+q\) vertices and at least \(e+2q\) edges: the \(e\) marked–marked edges and at least two distinct marked–unmarked edges per vertex of \(Q\). Its cycle-space dimension is at most that of \(G\), namely \(\beta(J)\le\beta(G)\), because the cycle space of a subgraph injects into that of \(G\). Since \(J\) is nonempty, \(\kappa(J)\ge1\). Euler's cycle-rank identity therefore implies
\[
 e+2q\le |E(J)|=m+q-\kappa(J)+\beta(J)
 \le m+q-1+\beta(G),
\]
so \(q\le m-1+\beta(G)-e\). Consequently
\[
 p+q\le m-1+\beta(G).
\]
There is at most one empty trace and at most \(m\) singleton traces. Every trace of size at least two is produced by a vertex counted in \(p\) or \(q\), so there are at most \(p+q\) such traces. Therefore
\[
\tau(G,A)\le1+m+p+q\le2m+\beta(G).
\]
Every trace is a subset of \(A\), giving the additional \(2^m\) bound.

**Simultaneous sharpness.** Fix \(c\ge0\) and \(m\ge\max\{1,3c\}\). Start with \(c\) pairwise disjoint triangles, whose \(3c\) vertices are marked, and \(m-3c\) additional isolated marked vertices. There are exactly \(h=m-2c\) marked connected components. Choose one marked vertex as a representative of each component, order the components, and join each consecutive pair of representatives via a distinct new unmarked vertex on a path of length two. This produces a connected cactus, with exactly the original \(c\) cycles. Attach to each marked vertex a new private pendant leaf. Finally attach one further unmarked leaf to the private leaf of any marked vertex.

For each triangle, its three marked vertices have three pairwise different two-element marked-neighborhood traces, giving \(3c\) traces. Each of the \(h-1\) joining vertices has the trace of the two representatives it joins, giving further distinct two-element traces; these span distinct marked components and hence do not coincide with any triangular trace. Each private leaf has a different singleton trace, giving \(m\) more traces. The final leaf has the empty trace. No unlisted vertex produces a new trace: the marked isolated vertices also give the empty trace. Thus the total number of traces is
\[
3c+(h-1)+m+1=3c+(m-2c-1)+m+1=2m+c.
\]
This equality also shows the elementary \(2^m\) ceiling does not interfere in the claimed parameter range. The graph is connected and has exactly \(c\) edge-disjoint and vertex-disjoint triangular cycles; hence \(\beta(G)=c\). This proves sharpness simultaneously for every allowed \(c,m\). \(\square\)

## Verification

Run `python3 artifacts/verify.py` from the directory containing this file. The checker independently computes graph cycle rank using disjoint-set components, constructs the set of open-neighborhood traces directly, and exhaustively evaluates every finite simple graph on \(1\) to \(6\) labelled vertices with every nonempty marked subset: \(2{,}097{,}151\) graph/marked-set instances. It checks the stated inequality without using the proof's intermediate quantities. Separately, it constructs and verifies \(81\) sharp cactus witnesses for \(0\le c\le8\) and nine successive marked-set sizes starting at \(\max\{1,3c\}\). The expected result is `VERIFY_OK`. Exhaustive small cases and finite witness samples are supplemental only; the all-size result follows from the displayed proof and symbolic construction.

## Relationship to prior work

Dreier, Mählmann, McCarty, Pilipczuk and Toruńczyk (2026; arXiv:2607.10941) establish almost-linear **open**-neighborhood complexity on monadically dependent graph classes. Their general asymptotic theorem does not state an exact additive bound determined by cycle-space dimension or a sharp cactus witness for every cycle budget. Beaudou, Bok, Foucaud, Quiroz and Raymond (2025; arXiv:2501.08895) prove general bounds for distance-profile complexity and closed radius-\(r\) neighborhoods in tree-structured graphs, not exact open traces classified by the cyclomatic number. Berthe, Foucaud, Lehtilä and Parreau (2026; arXiv:2607.16889) give tight treewidth/pathwidth bounds, but explicitly count **closed** neighborhoods \(N_G[v]\cap A\) rather than the open-neighborhood types here. Their forest and higher-treewidth theorems cannot be substituted for the present claim without additional arguments. Reidl, Sánchez Villaamil and Stavropoulos (2016/2019; arXiv:1603.09532) characterize bounded expansion through qualitative linear neighborhood complexity; that statement leaves the sharp \(2m+c\) coefficient and additive cycle-budget dependence unspecified. The \(c=0\) case is a forest estimate and is not claimed as a separately novel discovery; the positive-cycle sharpness is the new part.

## Limitations

The proof does not classify all equality graphs and does not determine the exact extremal trace function when \(m<\max\{1,3c\}\). The type count ignores equality predicates and does not extend to quantifier-rank-positive formulas. Existing literature was compared by statements and accessible primary text, but historical priority should be confirmed independently; recent arXiv texts are preprints. No independent validation or formal proof certification has been performed.

## References

1. J. Dreier, N. Mählmann, R. McCarty, M. Pilipczuk, S. Toruńczyk, *Neighborhood Complexity and Radius-1 Merge-Width in Monadically Dependent Graph Classes*, arXiv:2607.10941 (first public 2026-07-12), https://arxiv.org/abs/2607.10941.
2. G. Berthe, F. Foucaud, T. Lehtilä, A. Parreau, *Neighbourhood complexity and identification problems for graphs of bounded treewidth and pathwidth*, arXiv:2607.16889 (first public 2026-07-18), https://arxiv.org/abs/2607.16889.
3. L. Beaudou, J. Bok, F. Foucaud, D. A. Quiroz, J.-F. Raymond, *Profile and neighbourhood complexity of graphs excluding a minor and tree-structured graphs*, arXiv:2501.08895 (first public 2025-01-15), https://arxiv.org/abs/2501.08895.
4. F. Reidl, F. Sánchez Villaamil, K. Stavropoulos, *Characterising Bounded Expansion by Neighbourhood Complexity*, arXiv:1603.09532 (2016; journal 2019), https://arxiv.org/abs/1603.09532.
