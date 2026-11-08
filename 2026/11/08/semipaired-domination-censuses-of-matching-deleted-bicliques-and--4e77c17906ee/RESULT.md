# Semipaired-domination censuses of matching-deleted bicliques and an edge-restoration crossover

## Finding

Let \(a,b\ge3\) and \(0\le t\le\min(a,b)\) be integers. Let \(G_{a,b,t}\) be the graph obtained from the complete bipartite graph \(K_{a,b}\) by removing a matching of size \(t\). All vertices are labeled. A semipaired dominating set is a dominating vertex set admitting a partition into pairs whose members have graph distance at most two. Let \(\mathcal S_{a,b,t}(z)\) enumerate **all** semipaired dominating sets by size, and \(\mathcal M_{a,b,t}(z)\) enumerate all **inclusion-minimal** semipaired dominating sets by size.

Write \(A(z)=(1+z)^a-1-az\) and \(B(z)=(1+z)^b-1-bz\). Define
\[
\begin{aligned}
D_{a,b,t}(z)={}&A(z)B(z)+(a-t)zB(z)+(b-t)zA(z)\\
&+tz^2\big((1+z)^{a-1}+(1+z)^{b-1}-2\big)\\
&+\big((a-t)(b-t)+t\big)z^2+z^a+z^b.
\end{aligned}
\]
Then \(D_{a,b,t}\) is the ordinary all-dominating-set cardinality polynomial, and
\[
\boxed{\mathcal S_{a,b,t}(z)=\frac{D_{a,b,t}(z)+D_{a,b,t}(-z)}2-tz^2.}
\]

With \(\binom uv=0\) whenever \(v<0\) or \(v>u\), put
\[
\begin{aligned}
q_4(a,b,t)={}&\binom t2\binom b2+\binom a2\binom t2-\binom t2^2\\
&+t\left(\binom{a-1}2+\binom{b-1}2\right)
 +(a+b-2t)\binom t3\\
&+\mathbf1_{\{a=4\}}+\mathbf1_{\{b=4\}}.
\end{aligned}
\]
The **complete inclusion-minimal polynomial** is
\[
\boxed{\mathcal M_{a,b,t}(z)=(a-t)(b-t)z^2+q_4(a,b,t)z^4
 +\mathbf1_{\{a\ge6,\,a\text{ even}\}}z^a
 +\mathbf1_{\{b\ge6,\,b\text{ even}\}}z^b.}
\]
Coincident exponents are combined. In particular, the only possible inclusion-minimal cardinalities are \(2\), \(4\), and the orders of the even bipartition shores of size at least six. The minimum semipaired domination number is two exactly when both shores contain an unmatched vertex, and otherwise four.

There is a sharp *edge-restoration crossover*. In the balanced case write \(q_n(t)=q_4(n,n,t)\). The exact identity
\[
\boxed{q_n(n-1)-q_n(n)=\frac{(n-1)(n^2-11n+15)}3}
\]
shows that restoring a single edge to the crown graph \(G_{n,n,n}\) decreases the number of four-vertex inclusion-minimal semipaired dominating sets for \(3\le n\le9\), but increases it for every \(n\ge10\). For even \(n\ge6\), the crown graph has inclusion-minimal cardinality spectrum exactly \(\{4,n\}\), with \(n-5\) missing consecutive intermediate cardinalities.

## Assumptions and scope

All graphs are finite, simple, undirected, and labeled. Fix disjoint shores \(U=\{u_1,\dots,u_a\}\) and \(V=\{v_1,\dots,v_b\}\); the deleted edges are \(u_iv_i\) for \(1\le i\le t\). The word *minimal* always means inclusion-minimal among semipaired dominating sets, not minimum cardinality. A selected vertex dominates itself and its neighbors. Distances for semipairing are distances in the **original whole graph**, not in the induced selected subgraph. The constant coefficient is zero. We require both shore orders at least three; the formulas are not claimed at smaller shore orders.

## Proof

**Distances and allowable pairings.** Every two distinct vertices on the same shore have a common neighbor on the other shore: at most two candidates are forbidden by the deleted matching, and the opposite shore has at least three vertices. A cross-shore pair has distance one unless it is one of the \(t\) deleted pairs, in which case its distance is exactly three (a three-edge path exists using distinct auxiliary indices). Thus the graph joining pairs at distance at most two is a complete graph with \(t\) independent edges removed. In any even selected set of at least four vertices, an arbitrary pairing containing a forbidden pair can be repaired by exchanging partners with any other pair. The two new pairs are allowed since each vertex has at most one nonneighbor in this auxiliary graph; the number of forbidden pairs decreases. Consequently **every even set of cardinality at least four can be semipaired**, and a two-vertex set can be semipaired precisely when it is not a deleted matching pair.

**Dominating-set classification.** For selected subsets \(X\subseteq U\), \(Y\subseteq V\), write \(x=|X|\), \(y=|Y|\). If \(x=0\), domination holds precisely when \(Y=V\); symmetrically, \(y=0\) forces \(X=U\). If \(x,y\ge2\), domination always holds because an omitted vertex has at most one nonneighbor on the selected opposite shore. If \(x=1\), \(y\ge2\), domination holds precisely when the unique member of \(X\) is unmatched, or its deleted-matching partner belongs to \(Y\). The symmetric assertion holds if \(y=1\), \(x\ge2\). Finally, when \(x=y=1\), domination occurs exactly for a pair of unmatched vertices, one on each shore, or for one of the \(t\) deleted matching pairs. These categories are disjoint and exhaustive.

The generating functions of the \(x,y\ge2\) category give \(A(z)B(z)\). The singleton/opposite-at-least-two categories contribute \((a-t)zB(z)+(b-t)zA(z)\), and the cases requiring a deleted partner contribute \(tz^2((1+z)^{a-1}+(1+z)^{b-1}-2)\). The two-singleton and single-shore categories yield the remaining terms. This proves the displayed formula for \(D\). Taking its even part and removing exactly the \(t\) dominating but non-semipairable deleted pairs proves \(\mathcal S\).

**Inclusion-minimal classification.** Every semipaired dominating pair consists of one unmatched vertex from each shore, so there are \((a-t)(b-t)\) such pairs. All dominating four-sets are semipaired by the pairing lemma. Such a four-set is inclusion-minimal if and only if it contains no unmatched cross-shore pair, since a semipaired proper subset of a four-set must have cardinality two.

For a four-set with two vertices from each shore, the absence of an unmatched cross pair means that *all selected vertices of the first shore are matched* or *all selected vertices of the second shore are matched*. Inclusion-exclusion gives \(\binom t2\binom b2+\binom a2\binom t2-\binom t2^2\). For a four-set with three vertices in \(U\) and one in \(V\), either the unique \(V\)-vertex is unmatched and the other three selected vertices must be matched (\((b-t)\binom t3\) sets), or the unique \(V\)-vertex is matched and its partner must be in the selected triple (\(t\binom{a-1}2\) sets). Interchanging shores gives the other two terms. A four-set wholly contained in one shore dominates precisely if it is the entire shore, yielding the two size-four indicator terms. This proves \(q_4\).

Now let a semipaired dominating set have at least six vertices and meet both shores. If it meets each shore at least twice, a selected \(2+2\) subset already dominates and is semipaired. If it meets one shore once, then domination forces that singleton either to be unmatched or to have its deleted partner selected on the opposite shore. In either case it admits a dominating \(1+3\) subset, which is semipaired. Thus no such set is inclusion-minimal. A dominating set contained in just one shore must be that entire shore; it is semipaired exactly when its size is even, and is inclusion-minimal because any proper subset of it leaves an unselected same-shore vertex undominated. This proves the complete formula for \(\mathcal M\).

**One-edge crossover.** When \(a=b=n\) and \(t=n\), the two size-four indicators cancel in the difference, and
\[
q_n(n)=\binom n2^2+2n\binom{n-1}2.
\]
At \(t=n-1\), use \(\binom n2-\binom{n-1}2=n-1\) to obtain
\[
q_n(n-1)=\binom n2^2-(n-1)^2+2(n-1)\binom{n-1}2+2\binom{n-1}3.
\]
Subtracting reduces to \((n-1)(n^2-11n+15)/3\), whose sign is negative at integers \(3\le n\le9\) and positive at integers \(n\ge10\). For a full deleted matching and even \(n\ge6\), no unmatched cross pair exists, size four is attainable, and exactly two entire shores supply the higher cardinality \(n\); the displayed gap follows.

## Verification

The standalone file `verify_matching_bicliques.py` builds graph adjacency independently for \(G_{a,b,t}\), computes graph distances by breadth-first search, tests dominating sets by closed-neighborhood coverage, tests partnerability by an independent recursive perfect-matching search, and tests inclusion-minimality against **every nonempty proper subset**, not just one-vertex deletions. It compares the resulting three complete coefficient dictionaries (domination, semipaired domination, inclusion-minimal semipaired domination) with the proposed expressions.

The command `python verify_matching_bicliques.py` returned `VERIFY_OK instances=61 subsets=58819 all_domination_semipaired_minimal_polynomials=PASS`. The 61 instances have shores at least three, include both balanced and unequal orders, and cover deleted matching sizes from zero up to full matching. The finite checks corroborate the proof but cannot establish its unrestricted quantifiers. The crossover identity is proved algebraically above, not inferred from computational interpolation.

## Relationship to prior work

Haynes and Henning introduced semipaired domination and studied inequalities and extremal cases. Henning, Pandey, and Tripathi (arXiv:1904.00964, first posted 2019-04-01) develop algorithms and complexity results, including bipartite NP-completeness; their full accessible manuscript does not present the matching-deleted biclique distributions. Their follow-up (arXiv:2008.13491, first posted 2020-08-31) addresses chordal, split, and block graphs and subcubic complexity, without the present family-specific censuses. Later work addresses semipaired minimization on further graph classes. The complete multipartite paired-domination enumerator, by contrast, concerns **paired** domination and does not imply the semipaired even-shore families or the edge-restoration crossover. Exact novelty cannot be inferred from absence of search results; the scope of this claim is limited to the explicit formulas, classification, and crossover proved here.

## Limitations

The theorem assumes \(a,b\ge3\) and that the removed edges are a matching. It does not treat arbitrary missing-edge bipartite graphs or ordered pairing counts. No new general-purpose algorithm for arbitrary graphs is asserted. Previously published sources may contain unindexed equivalent formulas; independently established publication priority remains unverified. The finite verifier does not certify the infinite statement. No independent mathematical audit has been performed.

## References

1. T. W. Haynes and M. A. Henning, *Semipaired domination in graphs*, Journal of Combinatorial Mathematics and Combinatorial Computing 104 (2018), 93–109. Bibliographic record: https://dc.etsu.edu/etsu-works/10335/.
2. M. A. Henning, A. Pandey, and V. Tripathi, *Complexity and Algorithms for Semipaired Domination in Graphs*, arXiv:1904.00964 (initial posting 2019-04-01), https://arxiv.org/abs/1904.00964.
3. M. A. Henning, A. Pandey, and V. Tripathi, *Semipaired Domination in Some Subclasses of Chordal Graphs*, arXiv:2008.13491 (initial posting 2020-08-31), https://arxiv.org/abs/2008.13491.
