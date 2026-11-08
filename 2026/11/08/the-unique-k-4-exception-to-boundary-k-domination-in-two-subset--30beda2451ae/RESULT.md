# The unique \(K_4\) exception to boundary \(k\)-domination in two-subset Kneser graphs

## Finding
For every integer \(k\ge2\), let \(n=2k+3\) and let \(KG(n,2)\) be the graph whose vertices are the two-element subsets of \([n]\), with adjacency defined by disjointness. A \(k\)-dominating set \(D\) requires at least \(k\) neighbors in \(D\) for every vertex outside \(D\); no condition is imposed on vertices belonging to \(D\). Its minimum cardinality is \(k+3\), as established in earlier work. The following classifies **all** minimum \(k\)-dominating sets:

* **Triangle and matching:** \(D\) consists of the three edges of a triangle on a three-element subset of \([n]\), together with a perfect matching on the remaining \(2k\) elements.
* **The unique exceptional type:** only when \(k=3\), \(D\) may instead consist of the six edges of a complete graph on a four-element subset of \([9]\), with the other five elements isolated in the underlying selected-edge graph.

Consequently the number of labelled minimum \(k\)-dominating sets is
\[
N_k=\binom{2k+3}{3}\frac{(2k)!}{2^k k!}+\mathbf 1_{\{k=3\}}\binom94.
\]
The first term has already been structurally characterized for **minimum \(k\)-tuple dominating sets**. In particular, the new distinction is that minimum ordinary \(k\)-dominating sets coincide with minimum \(k\)-tuple (and minimum \(k\)-tuple total) dominating sets except for exactly \(126\) additional sets when \(k=3\). At \(k=3\) the two counts are respectively \(1386\) and \(1260\).

## Assumptions and scope
All graphs are finite and simple. Vertices of \(KG(n,2)\) are unordered distinct pairs of elements of the fixed labelled set \([n]\). Identifying a family \(D\) of such pairs with the edge set of a simple graph \(H\) on \([n]\), write \(t=|E(H)|\) and \(d(v)=\deg_H(v)\). Ordinary \(k\)-domination is tested only outside \(D\); \(k\)-tuple domination requires at least \(k\) selected vertices in every closed neighborhood; \(k\)-tuple total domination requires at least \(k\) in every open neighborhood. Distinguishing these definitions is essential to the exception. We consider every integer \(k\ge2\) and the exact boundary \(n=2k+3\), not arbitrary Kneser parameters.

## Proof
**1. A degree-sum translation.** If a pair \(\{u,v\}\) is not in \(D\), precisely \(d(u)+d(v)\) selected edges meet that pair; therefore it has \(t-d(u)-d(v)\) neighbors in \(D\) in the Kneser graph. Thus \(D\) is an ordinary \(k\)-dominating set if and only if
\[
d(u)+d(v)\le t-k\quad\text{for every nonedge }uv\text{ of }H.\tag{1}
\]
If \(uv\) belongs to \(D\), it has \(t-d(u)-d(v)+1\) selected Kneser neighbors and \(t-d(u)-d(v)+2\) selected vertices in its closed Kneser neighborhood.

**2. Minimum size.** Suppose a \(k\)-dominating set has at most \(k+2\) members. Add arbitrary graph vertices to obtain a \(k\)-dominating set with exactly \(t=k+2\) members (adding selected vertices cannot destroy domination). Then (1) bounds the degree sum at each nonedge by \(2\). If \(H\) has a vertex of degree at least \(3\), that vertex must be adjacent to all \(n-1=2k+2\) other vertices, impossible because \(t=k+2<n-1\). If \(H\) has a vertex of degree \(2\), every nonneighbor of that vertex must be isolated. Hence all positive-degree vertices lie within its three-vertex closed neighborhood; a simple graph of maximum degree \(2\) on at most three nonisolated vertices has at most three edges, contradicting \(t=k+2\ge4\). Otherwise \(H\) is a matching and has at most \(\lfloor n/2\rfloor=k+1\) edges. Therefore \(t\ge k+3\).

**3. Classification at equality.** Let \(t=k+3\), so (1) bounds degree sums at nonedges by \(3\). A vertex of degree at least \(4\) would have no nonneighbors, forcing \(n-1\) edges, which is impossible since \(k+3<n-1\). Thus the maximum degree is at most \(3\).

If \(H\) has a vertex of degree \(3\), every nonneighbor must be isolated. All selected edges therefore lie on that vertex and its three neighbors, a set of four vertices. Since \(k+3\ge5\), a five-edge graph on those vertices is \(K_4\) minus one edge, whose unique missing edge has endpoints of degrees \(2\) and \(2\), violating (1). The only possible case is all six \(K_4\) edges, which forces \(k+3=6\), i.e. \(k=3\). Conversely, this graph satisfies (1): an omitted edge has degree sum at most \(3\).

Otherwise \(H\) has maximum degree at most \(2\). Let \(a\) vertices have degree \(2\) and \(b\) have degree \(1\). The degree sum and vertex count imply
\[
2a+b=2k+6,\qquad a+b\le2k+3,\qquad a\ge3.
\]
Any two degree-two vertices must be adjacent: if not, their nonedge would have degree sum \(4>3\). Since maximum degree is \(2\), there can be at most three such vertices. Hence \(a=3\), these three form a triangle, and \(b=2k\). No vertices are isolated, and all remaining edges form a perfect matching on the other \(2k\) vertices. Conversely, for this triangle-plus-matching graph, every nonedge has degree sum at most \(3\), so it satisfies (1).

The two structural types are distinct. Choosing the triangle and matching gives \(\binom{2k+3}{3}(2k)!/(2^k k!)\) labelled configurations; the exceptional complete four-vertex graph gives \(\binom94=126\) at \(k=3\), proving the formula.

**4. The distinction from tuple domination.** In the triangle-plus-matching type, a selected triangle edge has exactly \(k\) selected **open** Kneser neighbors (the \(k\) matching edges); a selected matching edge has \(k+2\). The outside-vertex inequalities have already been proved, so every such set is \(k\)-tuple totally dominating and hence \(k\)-tuple dominating. In the exceptional \(K_4\) type at \(k=3\), a selected edge is disjoint from only one other selected edge, yielding one selected open neighbor and two selected closed-neighborhood vertices: the exception fails both tuple conditions. Since every tuple or total tuple set is also an ordinary \(k\)-dominating set, the classification is complete for all three variants. The shared minimum size \(k+3\) is thereby independently recovered; it is not claimed as a new scalar result.

## Verification
Run the accompanying standard-library program with `python verify.py`. It tests the literal Kneser-neighborhood definitions, not just the degree-sum shortcut. It exhausts all \(\binom{21}{4}=5985\) and \(\binom{21}{5}=20349\) candidate sets for \(k=2\), and all \(\binom{36}{5}=376992\) and \(\binom{36}{6}=1947792\) candidate sets for \(k=3\). It finds respectively \(105\) and \(1386\) ordinary minima, with exactly \(126\) exceptional \(K_4\) configurations in the second case; tuple and total-tuple counts are \(105\) and \(1260\). It also directly checks the two construction types where relevant for \(2\le k\le14\). These finite tests do not prove the unrestricted theorem; Steps 1–4 provide its proof.

## Relationship to prior work
Cornet and Torres [1, Theorem 20 and the paragraph following its proof] established that at this boundary all minimum **\(k\)-tuple** dominating sets have the triangle-plus-matching form up to automorphism. This entire form and its counting consequence are acknowledged as already implied by [1]. Brešar, Cornet, Dravec and Henning [2, Proposition 9] proved that the three numerical minimum cardinalities all equal \(k+3\), and constructed a triangle-plus-matching set. The new result concerns the **complete ordinary \(k\)-domination minimizer family**, and in particular the exceptional six-edge \(K_4\) family at exactly \(k=3\), which fails tuple domination despite attaining the same cardinality. No claim is made that the general degree-occurrence method or the scalar threshold is new.

## Limitations
The theorem is restricted to two-subset Kneser graphs at \(n=2k+3\), with \(k\ge2\). It does not enumerate nonminimum dominating sets or general \(KG(n,r)\). The literature comparison does not establish publication priority against all unindexed publications; the structural distinction should receive external mathematical review before a priority claim. Computational verification is finite, not an independent proof.

## References
[1] M. G. Cornet and P. Torres, *\(k\)-tuple domination on Kneser graphs*, arXiv:2308.15603, first posted 2023-08-29; Theorem 20 and the following classification. https://arxiv.org/abs/2308.15603

[2] B. Brešar, M. G. Cornet, T. Dravec and M. A. Henning, *\(k\)-Domination invariants on Kneser graphs*, arXiv:2312.15464, first posted 2023-12-24; Definition in Section 1, Theorem 7 and Proposition 9 in Section 3. https://arxiv.org/abs/2312.15464
