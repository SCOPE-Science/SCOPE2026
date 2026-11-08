# Eventual exactness and rigidity of multipartite global coalition partitions

## Finding

Let \(r\ge4\) be an integer and let \(G=K_{n_1,\ldots,n_r}\) be a finite, simple, complete multipartite graph with labelled vertex set partitioned into nonempty parts \(V_1,\ldots,V_r\), where \(|V_i|=n_i\). Put \(N=\sum_{i=1}^r n_i\), \(m=\min_i n_i\), and \(Q=r(r-2)\).

**Theorem.** If \(m\ge3r-6\), then the global coalition number satisfies
\[
GC(G)=N-Q=N-r(r-2).
\]
If, in addition, \(m\ge3r-4\), every maximum global coalition partition has precisely \(r\) nonsingleton classes \(H_1,\ldots,H_r\), where \(H_i\) contains exactly one vertex of each \(V_j\) with \(j\ne i\) and no vertex of \(V_i\). All remaining classes are singletons. Consequently the exact number of maximum partitions (unordered classes, vertices labelled) is
\[
\prod_{i=1}^r (n_i)_{r-1},
\qquad (n)_k:=n(n-1)\cdots(n-k+1).
\]
The second assertion counts partitions, not ordered lists of classes; each nonsingleton class is canonically identified by its unique omitted part.

For example, \(K_{8,9,10,11}\) has global coalition number \(30\) and exactly \(120708403200\) maximum partitions.

## Assumptions and scope

A set \(S\subseteq V(G)\) *globally dominates* \(G\) if it dominates both \(G\) and its complement, using closed-neighbourhood domination. A *global coalition partition* is a partition \(\pi\) into nonempty classes such that no class globally dominates, but every class has a **distinct** partner class whose union with it globally dominates. Write \(GC(G)\) for the maximum number of classes. Graphs here are finite, simple, undirected, and labelled; the number \(r\) of parts and their sizes are arbitrary subject to the stated lower bounds. No regularity or equality of the part sizes is assumed.

For a complete multipartite graph with \(r\ge2\), a set globally dominates exactly when it meets every part. Indeed, the complement is a disjoint union of the \(r\) cliques induced by the parts, so domination of the complement requires meeting every part; such a transversal also dominates the original complete multipartite graph. Accordingly, two classes form a global coalition exactly when neither meets every part but their union does.

## Proof

**1. The deficit and a structural accounting inequality.** Fix an arbitrary global coalition partition \(\pi\) with \(k\) classes and define its nonnegative integer excess
\[
E:=N-k=\sum_{A\in\pi}(|A|-1).
\]
Let \(J\subseteq\{1,\ldots,r\}\) be the part indices having at least one singleton class \(\{v\}\subseteq V_i\), and put \(s:=|J|\). For each \(i\in J\), choose one such singleton and one of its coalition partners \(H_i\). Since \(H_i\cup\{v\}\) meets all \(r\) parts while \(H_i\) itself is not a transversal, the support of \(H_i\) is exactly \(\{1,\ldots,r\}\setminus\{i\}\). In particular, \(|H_i|\ge r-1\). The classes \(H_i\) for distinct \(i\in J\) are distinct, because their uniquely omitted parts differ. Since \(r\ge4\), none of these partner classes is a singleton.

In each \(H_i\), mark one selected vertex from every part other than \(V_i\), so exactly \(r-1\) vertices are marked in each chosen partner class. Its contribution to \(E\) is
\[
|H_i|-1=(r-2)+(|H_i|-(r-1)).
\]
Thus the \(s\) chosen partner classes contribute a base excess \(s(r-2)\), plus one unit for every unmarked vertex in those classes. Every other nonsingleton class \(A\) contributes \(|A|-1\ge |A|/2\) to \(E\); singleton classes contribute zero.

For each \(j\notin J\), no vertex of \(V_j\) belongs to a singleton class. Exactly \(s\) of its vertices were marked (one in each of the \(s\) chosen partner classes), so its remaining \(n_j-s\) vertices are unmarked and lie in nonsingleton classes. Charging a half unit to each of these vertices, and the full extra unit to each unmarked vertex of the chosen partner classes, proves
\[
\boxed{E\ \ge\ s(r-2)+\frac12\sum_{j\notin J}(n_j-s)
\ \ge\ s(r-2)+\frac{(r-s)(m-s)}2.}\tag{1}
\]
This argument also covers \(s=0\): every class is then nonsingleton and \(E\ge N/2\). If \(s=r\), the empty sum in (1) gives \(E\ge r(r-2)=Q\).

**2. The upper bound for all sufficiently large parts.** Suppose \(m\ge3r-6\). If \(s\le r-2\), then \(m-s\ge 2r-4=2(r-2)\), so (1) gives \(E\ge Q\). If \(s=r-1\), then \(m-s\ge 2r-5\), so (1) gives \(E\ge Q-\tfrac12\). Since \(E\) is an integer, again \(E\ge Q\). The case \(s=r\) was already settled. Consequently every global coalition partition satisfies \(k=N-E\le N-Q\).

**3. Construction attaining the bound.** As \(m\ge3r-6\ge r-1\), for every \(j\) choose \(r-1\) distinct vertices of \(V_j\) and assign one to each of the labels \(i\ne j\). For every \(i\), let \(H_i\) contain the vertex assigned label \(i\) from each \(V_j\), \(j\ne i\). The \(H_i\) are pairwise disjoint, each has \(r-1\) vertices, and each omits exactly one part. Partition all unused vertices into singleton classes. For each \(i\), every singleton from \(V_i\) forms a coalition with \(H_i\), while \(H_i\) forms a coalition with any \(H_j\), \(j\ne i\). The construction has
\[
r+\sum_{i=1}^r(n_i-r+1)=N-r(r-2)=N-Q
\]
classes, proving the exact formula.

**4. Rigidity and exact counting.** Now assume \(m\ge3r-4\) and let \(\pi\) be any maximum partition. By the first part, \(E=Q\). If \(s<r\), then \(m-s\ge(3r-4)-(r-1)=2r-3>2(r-2)\). Inequality (1) gives \(E>Q\), a contradiction. Therefore \(s=r\), and the \(r\) distinct chosen partner classes contribute at least \(r(r-2)=Q\) to the excess. Equality leaves no room for additional vertices in these partners or for any other nonsingleton class. Hence every \(H_i\) contains exactly one vertex of each other part, all remaining classes are singletons, and these are all possible maximum partitions.

For a fixed part \(V_j\), the vertices going into \(H_i\), \(i\ne j\), form an injection from the \(r-1\) distinguishable hub labels into the \(n_j\) labelled vertices. There are \((n_j)_{r-1}\) choices. Choices in different parts are independent, and no two choices give the same unordered partition because \(H_i\) is identified by the uniquely omitted part \(V_i\). Multiplying proves the stated count. This completes the proof.

## Verification

The included standard-library Python script `verify.py` performs (i) exhaustive enumeration of all unlabeled vertex partitions of five small complete multipartite graphs (including four- and five-part examples), (ii) direct graph-level checking of the transversal characterization for all vertex subsets in selected small graphs, (iii) exact numerical checks of the deficit inequality at the two thresholds for \(4\le r\le24\), (iv) explicit large-instance coalition constructions, and (v) exhaustive injective-allocation checks of the canonical counting bijection for \(K_{3,3,3}\) and \(K_{3,3,3,3}\). It prints `VERIFY_OK` when all checks pass. Execute `python3 verify.py` in the directory containing this file. These are finite corroborations; the quantifiers over all \(r\) and part sizes follow from the proof, not from enumeration.

## Relationship to prior work

Anholcer, Besharati, Mojdeh and Samadzadeh, *Global coalitions in graphs*, arXiv:2509.15386, first made public on 18 September 2025, give the definitions and a general lower bound for complete multipartite graphs (Proposition 6, arXiv version 4). Their Theorem 7 determines the number for at most three parts. Their Conjecture 54 explicitly asks whether the lower bound is always exact. Taking the number of construction blocks equal to \(r\) in Proposition 6 gives the lower bound \(N-r(r-2)\), but it supplies no matching upper bound for arbitrary \(r\ge4\). The present theorem proves equality whenever the minimum part has size at least \(3r-6\) and additionally classifies and enumerates all maximizers at \(3r-4\). It is a partial, not a complete, resolution of that conjecture.

The paper also observes that the global coalition number of a complete multipartite graph equals the ordinary coalition number of the complementary disjoint union of cliques. Thus the same formulas hold for that ordinary-coalition problem under the complementary convention. The introductory coalition framework of Haynes, Hedetniemi, Hedetniemi, McRae and Mohan (2020) does not supply the stated multipartite upper bound or rigidity enumeration.

## Limitations

The lower-size thresholds \(3r-6\) and \(3r-4\) are sufficient, not claimed sharp. Exactness for smaller parts and the full Conjecture 54 remain open here; no assertion is made about optimal-partition counts below the rigidity threshold. The theorem is for complete multipartite graphs with at least four nonempty parts, under the precise global-coalition convention above. The small-instance checks do not constitute an infinite proof or an independent audit. Historical priority against unpublished or unindexed equivalent results remains uncertain.

## References

1. M. Anholcer, N. Besharati, D. A. Mojdeh, and M. R. Samadzadeh, *Global coalitions in graphs*, arXiv:2509.15386 (first public version 18 September 2025; version 4 dated 25 October 2026), https://arxiv.org/abs/2509.15386. Relevant: Definition 2, Proposition 6, Theorem 7, Corollary 18, Conjecture 54.
2. T. W. Haynes, J. T. Hedetniemi, S. T. Hedetniemi, A. A. McRae, and R. Mohan, *Introduction to coalitions in graphs*, AKCE International Journal of Graphs and Combinatorics 17 (2020), 653–659, https://doi.org/10.1080/09728600.2020.1832874.
