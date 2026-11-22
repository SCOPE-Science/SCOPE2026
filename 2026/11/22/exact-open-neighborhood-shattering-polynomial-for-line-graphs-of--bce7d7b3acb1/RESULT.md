# Exact open-neighborhood shattering polynomial for line graphs of finite trees

## Finding
Let \(T\) be any finite simple tree with at least two vertices and let \(G=L(T)\). Associate each tree edge with one vertex of \(G\), with distinct edges adjacent in \(G\) exactly if they meet in \(T\). A set \(S\subseteq E(T)\) is **shattered** if each \(X\subseteq S\) equals \(N_G(e)\cap S\) for some edge \(e\in E(T)\). The witness edge may lie in \(S\); importantly, \(N_G(e)\) excludes \(e\) itself.

Let \(s_j(T)\) be the number of shattered \(j\)-element sets and let \(P_T(z)=\sum_{j\ge0}s_j(T)z^j\). Then
\[
P_T(z)=1+s_1(T)z+s_2(T)z^2+s_3(T)z^3,
\]
where the following finite explicit expressions determine every coefficient.

For each \(u\in V(T)\), set \(d_u=\deg_T(u)\), \(a_u=|\{v\in N_T(u):d_v\ge2\}|\), and
\[
b_u=|\{v\in N_T(u):\exists w\in N_T(v)\setminus\{u\},\ d_w\ge2\}|.
\]
Thus \(a_u\) counts branches extending at least two edges from \(u\), and \(b_u\) counts branches extending at least three. Set
\[
B_u=\begin{cases}
\binom{d_u}{2},&a_u=0,\\
d_u-1,&a_u=1\text{ and }b_u=0,\\
1,&a_u=2\text{ and }b_u=0,\\
0,&\text{otherwise}.
\end{cases}
\]
Then \(s_1(T)=0\) for the single-edge tree and \(s_1(T)=|E(T)|\) otherwise. For the pairs,
\[
s_2(T)=\sum_{u:d_u\ge3}\left(\binom{d_u}{2}-B_u\right)
 +\sum_{\substack{x-u-v-y\\\text{unoriented simple three-edge paths}}}
\mathbf1_{\{d_x+d_u\ge4\}}\mathbf1_{\{d_v+d_y\ge4\}}.
\]
Every unoriented simple three-edge path contributes once. For triples,
\[
s_3(T)=\sum_{u:d_u\ge4}\left(\binom{a_u}{3}-\mathbf1_{\{a_u=3,b_u=0\}}\right).
\]
All \(s_j(T)\) for \(j\ge4\) vanish. Hence \(\operatorname{VCdim}(L(T))\le3\) for every tree. The bound is attained by a nine-vertex tree consisting of a central vertex and four length-two arms. No smaller tree can attain three.

## Assumptions and scope
All trees are undirected, finite, loopless, connected, and acyclic; the two-vertex tree is included. Open neighborhoods are computed in the **line graph**, not in the original tree. Witnesses range over all line-graph vertices, including the queried support itself. The parameters \(d_u,a_u,b_u\) and the paths in the formulas all belong to the original tree. Formulas count **support subsets**, not distinct realized traces, and do not assume a labeling or uniform degree.

## Proof
**1. Singles.** For a support containing one tree edge \(f\), the trace empty is realized by \(f\) itself. The singleton trace exists precisely when some other tree edge meets \(f\). In a connected tree with at least two edges, this holds for every edge. A one-edge tree has no such witness.

**2. Adjacent pairs.** Suppose support edges \(f_1,f_2\) meet at \(u\). The trace consisting of \(f_1\) alone is witnessed by \(f_2\), and conversely. The trace containing both is realized precisely if \(d_u\ge3\), since any common neighbor distinct from the support edges must be another edge at \(u\) (a triangle in a tree is impossible). An empty-trace witness is an edge disjoint from both support edges.

Fix \(u\) with \(d_u\ge3\) and any two incident edges as support. An edge disjoint from both exists if and only if either (i) some **unchosen** branch from \(u\) continues for a second edge, or (ii) some branch continues to distance at least three from \(u\) (even if it is chosen). This condition fails for every pair if \(a_u=0\), for precisely \(d_u-1\) pairs if \(a_u=1,b_u=0\), and for exactly one pair if \(a_u=2,b_u=0\); it never fails otherwise. These exclusions give \(\binom{d_u}{2}-B_u\).

**3. Disjoint pairs.** If support edges \(xu\) and \(vy\) are disjoint, their own vertices witness the empty trace. A common line-graph neighbor exists precisely when there is an edge joining an endpoint of one to an endpoint of the other, so the tree contains the unique simple path \(x-u-v-y\) of three edges with middle edge \(uv\). A singleton trace for \(xu\) exists precisely when some edge other than \(xu,uv,vy\) meets \(xu\); this is equivalent to \(d_x+d_u\ge4\). Similarly the singleton trace for \(vy\) exists precisely when \(d_v+d_y\ge4\). Thus disjoint shattered pairs correspond bijectively to three-edge paths meeting both degree tests. Combining with step 2 proves \(s_2\).

**4. Triples.** If three support edges are shattered, an all-three witness meets them. That witness has only two tree endpoints, so the support is either (a) three edges at a common vertex \(u\), or (b) two edges at one endpoint and the third at the other endpoint of the witness. In (b), a trace containing the third support edge and exactly one of the two first support edges is impossible: the unique tree edge connecting both sides is the all-three witness. Therefore every shattered triple is a three-edge star at one common center \(u\).

For three edges at \(u\), an all-three witness requires \(d_u\ge4\); each two-element subtrace is witnessed by the corresponding omitted support edge. To realize each singleton one needs a second edge extending from that support edge's outer endpoint, so all three chosen neighbors must have degree at least two. Hence there are \(\binom{a_u}{3}\) candidates. The empty trace exists if an unchosen branch continues two edges from \(u\), or any branch continues three edges from \(u\). Precisely when \(a_u=3\), \(b_u=0\), and the selected triple consists of the three extending branches, neither option exists; there is then exactly one excluded candidate. This proves \(s_3\).

**5. Four or more points and sharpness.** If four support edges were shattered, some witness would meet all four, so at least two of them would meet one endpoint of that witness. If some also meet its other endpoint, a mixed partial trace (one from each side but not all the support) cannot be realized: the edge between the two endpoints is the only possible joint neighbor. If all four meet a single common center, every witness either meets at most one support edge, is one of the support edges (then meets the other three), or is an additional edge at that center (then meets all four). In particular a two-element trace is impossible. Thus no four-support is shattered, and the same holds for larger sets by heredity of shattering.

A shattered three-support needs all eight Boolean patterns, hence at least eight distinct witness vertices of \(L(T)\), i.e., at least eight edges and nine vertices in \(T\). The tree with a central vertex and four length-two arms has nine vertices, has \(a_u=4\) at its center, and therefore shatters \(\binom43=4\) triples. This proves both optimality claims.

## Verification
The self-contained standard-library script `verify.py` directly enumerates open-neighborhood trace families on all labeled Prüfer-sequence trees of orders two through seven, as well as deterministic pseudorandom trees of orders eight through twenty-one, and independently calculates the proposed coefficients. It also checks absence of shattered four-sets and the explicit nine-vertex example. The script's successful output was `VERIFY_OK 18948 trees; four-support checks and nine-vertex extremizer`.

A separate exhaustive unlabeled-tree check using nonisomorphic trees of orders two through thirteen confirmed the same coefficient formulas on 2,287 isomorphism classes. These finite computations corroborate the explicit all-tree proof; they are not used as an infinite proof.

## Relationship to prior work
Dreier, Mählmann, and Toruńczyk (2026, arXiv:2611.08143) motivate the study of bounded first-order types on dependent graph classes. In the line graph, the adjacency predicate has as its one-parameter traces exactly the open neighborhoods counted here. Benediktsson, Macpherson, and Adler (2020, arXiv:2007.16042) prove the general VC-dimension upper bound four for induced subgraphs of Johnson graphs; \(L(T)\) is an induced subgraph of \(J(|V(T)|,2)\), so the old result supplies a four-bound, not the present exact three-degree polynomial or its coefficients. Berthe, Foucaud, Lehtilä, and Parreau (2026, arXiv:2607.16889) study **closed-neighborhood** complexity in bounded-treewidth and forest graphs; those theorems concern a different family and do not determine this open-neighborhood support census. Prior complete triangular-graph shattering results count \(L(K_n)\), which is not a tree line graph for \(n\ge3\). The local form also differs from geodesic-halfspace shattering on trees.

## Limitations
The result is restricted to open neighborhoods of line graphs of trees; it does not cover arbitrary block graphs or line graphs of cyclic graphs, and it makes no classification of finite-model theories of larger quantifier rank. An exhaustive historical-priority guarantee is not claimed. A related older work on graph-defined VC set systems was encountered only in abstract, and could contain an alternate formulation. Independent mathematical and literature audits are not performed.

## References
1. J. Dreier, N. Mählmann, S. Toruńczyk, *First-Order Model Checking on Monadically Dependent Graph Classes*, arXiv:2611.08143, submitted November 5, 2026, https://arxiv.org/abs/2611.08143.
2. B. G. Benediktsson, D. Macpherson, I. Adler, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042, 2020, https://arxiv.org/abs/2007.16042.
3. G. Berthe, F. Foucaud, T. Lehtilä, A. Parreau, *Neighbourhood complexity and identification problems for graphs of bounded treewidth and pathwidth*, arXiv:2607.16889, July 18, 2026, https://arxiv.org/abs/2607.16889.
4. L. Beaudou et al., *Bounding the order of a graph using its diameter and metric dimension: a study through tree decompositions and VC dimension*, arXiv:1610.01475, 2016, https://arxiv.org/abs/1610.01475.
