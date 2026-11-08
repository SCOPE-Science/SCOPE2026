# Exact two-total bondage and extremal deletion cuts in complete bipartite graphs

## Finding
For integers \(2\le a\le b\), let \(K_{a,b}\) be the labelled complete bipartite graph with parts \(A\) and \(B\), of orders \(a\) and \(b\). Define \(b_t^2(G)\) as the minimum number of edges that can be deleted, leaving no isolated vertices, to increase the total domination number by at least two. Let \(\mathcal N(a,b)\) count the distinct labelled edge-deletion sets attaining the minimum.

Then
\[
b_t^2(K_{a,b})=
\begin{cases}
b,&a=2,\\
\min\{b,2a\},&a\ge3.
\end{cases}
\]
Writing \(S(n,k)\) for a Stirling number of the second kind, the complete count of minimum deletion sets is
\[
\mathcal N(a,b)=
\begin{cases}
a!S(b,a), &a=2\ \text{or}\ (a\ge3\ \text{and}\ b<2a),\\
a!S(2a,a)+6\binom{2a}{3}S(a,3),&a\ge3,\ b=2a,\\
6\binom b3 S(a,3),&a\ge3,\ b>2a.
\end{cases}
\]
All minimizers have an explicit structural classification. In the *column-cover* regime, each vertex of \(B\) has exactly one deleted incident edge, and every vertex of \(A\) is incident to at least one deletion; these deletion sets are precisely the surjections \(B\to A\). In the *triangle* regime, three vertices \(x,y,z\) of \(B\) are distinguished, every vertex of \(A\) has exactly two of its incident edges to \(\{x,y,z\}\) deleted, and all three possible two-element deletion patterns occur. No other minimum deletion sets exist. The triangle regime occurs for \(a\ge3\) and \(b\ge2a\), whereas the column-cover regime is minimum precisely for \(a=2\) or \(b\le2a\). Both coexist at \(b=2a\) for \(a\ge3\).

## Assumptions and scope
All graphs are finite, simple, and undirected. Total domination requires every vertex, including every selected vertex, to have a neighbor in the chosen set. A candidate edge-deleted graph must contain no isolated vertices. The original complete bipartite graph has total domination number \(2\); therefore raising it by at least two means obtaining total domination number at least \(4\). Edge-deletion sets, graph vertices, and parts are labelled; two cuts are distinct when they differ as edge subsets. The claim applies to every pair of integers \(2\le a\le b\), including the boundary \(b=2a\) and the thin side \(a=2\).

## Proof
**1. Characterization of small total dominating sets.** Let \(H=K_{a,b}-F\) have no isolated vertices. Call a vertex *full* if it is adjacent to every vertex in the opposite part. A two-vertex total dominating set consists of one full vertex of each part. A three-vertex total dominating set must consist of either two vertices of \(A\) and one of \(B\), or one of \(A\) and two of \(B\): a set entirely in one bipartition class cannot totally dominate itself. The configuration with two vertices \(u,v\in A\) and one \(w\in B\) is total dominating exactly when \(w\) is full and \(N_H(u)\cup N_H(v)=B\); the opposite configuration is symmetric. This statement follows directly by checking the open neighborhoods on both sides.

**2. A sharp lower bound.** Suppose \(H\) has total domination number at least \(4\) and \(|F|<b\). Then some vertex \(w\in B\) is full, since otherwise every vertex of \(B\) would be incident to a deleted edge. By the characterization above, for every distinct \(u,v\in A\) there must be a vertex \(x\in B\) incident to *both* deleted edges \(ux\) and \(vx\). In other words, the missing-neighbor sets \(R(u)=\{x\in B:ux\in F\}\) meet pairwise.

If \(a=2\), a common missing neighbor of the only two vertices in \(A\) would be isolated in \(H\), impossible. Consequently \(|F|\ge b\) for \(a=2\).

For \(a\ge3\), every \(u\in A\) must satisfy \(|R(u)|\ge2\). Indeed, if \(R(u)\) were empty, it could not intersect another missing-neighbor set. If \(R(u)=\{x\}\), pairwise intersection would force \(x\in R(v)\) for every other \(v\in A\), isolating \(x\). Summing over \(A\) gives \(|F|=\sum_{u\in A}|R(u)|\ge2a\). Thus, whenever \(a\ge3\), \(|F|\ge\min\{b,2a\}\).

**3. Sharp constructions.** For every \(2\le a\le b\), choose any surjection \(g:B\to A\), and delete exactly \(g(x)x\) for each \(x\in B\). No vertex is isolated: each \(x\in B\) retains \(a-1\) neighbors and, because \(g\) is onto and \(a\ge2\), each vertex of \(A\) retains at least one neighbor. Neither part contains a full vertex, so the characterization in step 1 rules out total dominating sets of size two or three. This is a valid cut of size \(b\).

When \(a\ge3\) and \(b\ge2a\), choose three distinct vertices \(x,y,z\in B\), and partition \(A\) into three nonempty classes indexed by \(x,y,z\). For \(u\) in the class indexed by \(x\), delete \(uy\) and \(uz\), and analogously in the other two classes. This deletes exactly \(2a\) edges. Every one of \(x,y,z\) has at least one retained neighbor, while every other vertex of \(B\) remains full; each vertex of \(A\) retains \(b-2\) neighbors. Any two vertices of \(A\) share a missing neighbor among \(x,y,z\), so no two such vertices dominate all of \(B\). No vertex of \(A\) is full. Step 1 therefore forbids total dominating sets of sizes two or three. The lower bounds are attained, proving the minimum formula.

**4. Every minimum cut and its multiplicity.** First assume \(a=2\), or \(a\ge3\) and \(b<2a\). A minimum cut has size \(b\). If it had any full vertex of \(B\), step 2 would either yield an impossibility for \(a=2\) or force at least \(2a>b\) deletions. Thus every vertex of \(B\) loses exactly one edge. If some vertex \(u\in A\) were full, then two vertices \(x,y\in B\) with different missing neighbors would exist (otherwise their common missing neighbor in \(A\) would be isolated). Their neighborhoods together cover \(A\); combined with the full vertex \(u\), they form a three-vertex total dominating set. Hence all vertices of \(A\) must be hit by deletions, giving exactly the surjections \(B\to A\) and \(a!S(b,a)\) cuts.

Now assume \(a\ge3\) and \(b\ge2a\). A minimum cut has size \(2a\). If some vertex of \(B\) is full, the lower-bound proof forces \(|R(u)|=2\) for every \(u\in A\), and all these two-element missing-neighbor sets must intersect pairwise. An elementary intersection lemma states that a family of pairwise-intersecting two-element sets either has a common element or consists solely of the three edges of a triangle. To see this, take distinct sets \(\{x,y\}\) and \(\{x,z\}\): a set not containing \(x\) must be \(\{y,z\}\), which then forces every set to be one of these three. A common element would correspond to a vertex of \(B\) missing *all* its incident edges, which is disallowed. Therefore all three two-element subsets of one triple occur. Choosing the triple and assigning each vertex of \(A\) surjectively to one of its three missing pairs gives exactly \(\binom b3\,3!S(a,3)\) triangle cuts.

If \(b>2a\), some vertex of \(B\) necessarily remains full, so these are all minimum cuts. If \(b=2a\), there may instead be no full vertex in \(B\); then \(2a=b\) deletions force exactly one missing edge per vertex of \(B\), producing the column-cover surjections from the preceding paragraph. The two cut families are disjoint, and their counts add. This proves all three counting cases and the structural classification. \(\square\)

## Verification
The standalone script `verify.py`, using only the Python standard library, directly enumerates edge-deletion sets and independently checks all two- and three-vertex candidate total dominating sets. It exhaustively verifies the optimum and number of optimal labelled cuts for \((a,b)\) equal to \((2,2)\) through \((2,6)\), \((3,3)\) through \((3,8)\), and \((4,4),(4,5),(4,6)\). It also exhausts small pair-cover instances and checks both construction families over additional parameter pairs. Run `python3 verify.py` in the directory containing this document. The full result for unbounded \(a,b\) follows from the written proof, not extrapolation from finite tests.

## Relationship to prior work
Appel, Fischberg, Kelley, Shank, and Sosis introduce the \(k\)-total bondage framework and give, for complete bipartite graphs, the upper bound \(b_t^2(K_{a,b})\le2a\) when \(a\ge3\) (their Theorem 12), the complementary construction bound (their Theorem 13), and the exact value \(b_t^2(K_{a,b})=b\) for \(2\le a\le b\le2a\) (their Theorem 14). The scalar answer in that already-solved region is not claimed here as new. The present result supplies the matching unrestricted lower bound for \(b>2a\), handles the thin-side regime \(a=2,b>4\), and classifies and counts **all** optimal labelled cuts in every regime, including the previously covered scalar cases. Prior work on ordinary total bondage concerns the one-unit increase and does not imply these two-unit cut multiplicities.

## Limitations
The result is specific to the increase by two in complete bipartite graphs; it does not determine general \(k\)-total bondage for \(k\ge3\), or the analogous invariant for arbitrary bipartite graphs. The minimal-cut enumeration is for labelled edge subsets, not graph-isomorphism classes. The literature comparison supports provisional priority only; the 2026 journal version of the primary paper was not accessible in full during the comparison, although the complete arXiv version was inspected.

## References
1. J.-P. Appel, G. Fischberg, K. Kelley, N. Shank, E. Sosis, *The \(k\)-Total Bondage Number of a Graph*, arXiv:2506.07000v1 (first public 2025-06-08), Sections 1 and 3.4, Theorems 11–14. https://arxiv.org/html/2506.07000v1
2. Same authors, *The \(k\)-Total Bondage Number of a Graph*, *Theory & Applications of Graphs* 13(1), article 3 (2026), DOI:10.20429/tag.2026.130103. https://digitalcommons.georgiasouthern.edu/tag/vol13/iss1/3/
3. V. R. Kulli and D. K. Patwari, *The total bondage number of a graph*, *Advances in Graph Theory* (1991), pp. 227–235; bibliographic details reported in reference [16] of Appel et al.
