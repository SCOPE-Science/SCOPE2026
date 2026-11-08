# Two-clique rigidity and exact dual general-position enumerators for complete joins

## Finding

Let \(r\ge 2\), and let \(H_1,\ldots,H_r\) be finite, nonempty, simple, **noncomplete** graphs on pairwise disjoint vertex sets. Let \(J=H_1\vee\cdots\vee H_r\) denote their complete join. A dual general-position set \(X\subseteq V(J)\) is a set in general position whose complement is geodesically convex.

**Join rigidity theorem.** Every nonempty dual general-position set \(X\) of \(J\) is exactly one part of a partition of \(V(J)\) into two cliques: both \(J[X]\) and \(J[V(J)\setminus X]\) are complete. Conversely, every such two-clique partition gives a dual general-position set. Thus a nonempty dual general-position set exists if and only if \(\overline J\) is bipartite, equivalently if and only if each \(\overline{H_i}\) is bipartite.

For each connected component \(C\) of \(\overline J\), let \((a_C,b_C)\) be the two part sizes in its unique bipartition, whenever it is bipartite. An isolated component has sizes \((1,0)\). Write \(\mathcal B\) for this multiset of pairs. The full dual general-position cardinality polynomial, **including the empty set**, is

\[
D_J(z)=\begin{cases}
1+\displaystyle\prod_{(a,b)\in\mathcal B}(z^a+z^b),&\overline J\text{ bipartite},\\
1,&\overline J\text{ not bipartite}.
\end{cases}
\]

In the bipartite case the dual general-position number and number of nonempty dual general-position sets are
\[
\operatorname{gp}_{\mathrm d}(J)=\sum_{(a,b)\in\mathcal B}\max\{a,b\},\qquad
\#\{X\ne\varnothing:X\text{ dual general-position}\}=2^{|\mathcal B|}.
\]
The number of maximum-cardinality sets is \(2^e\), where \(e\) counts components with equal bipartition sizes. Every nontrivial component contributes two distinct orientations even when its part sizes coincide.

Let \(u\) count isolated vertices of \(\overline J\), and let \(\mathcal B_+\) contain the pairs belonging to its components with at least one edge. The cardinality polynomial of **nonempty, inclusion-maximal** dual general-position sets is
\[
Q_J(z)=z^u\prod_{(a,b)\in\mathcal B_+}(z^a+z^b).
\]
These inclusion-maximal configurations all have the same cardinality exactly when every nontrivial bipartite component of \(\overline J\) has equally sized color classes. For nonbipartite \(\overline J\), only the empty set is feasible; this formula for nonempty inclusion-maximal sets is then not invoked.

**Complete-first-factor lexicographic products.** Let \(m\ge2\), and let \(H\) be any noncomplete finite simple graph with at least two vertices. Since \(K_m\circ H\) is the complete join of \(m\) copies of \(H\), writing \(f_H(z)=\prod_{C\in\operatorname{cc}(\overline H)}(z^{a_C}+z^{b_C})\) when \(\overline H\) is bipartite, we obtain
\[
D_{K_m\circ H}(z)=\begin{cases}1+f_H(z)^m,&\overline H\text{ bipartite},\\1,&\text{otherwise},\end{cases}
\quad
\operatorname{gp}_{\mathrm d}(K_m\circ H)=\begin{cases}
m\sum_C\max\{a_C,b_C\},&\overline H\text{ bipartite},\\0,&\text{otherwise}.
\end{cases}
\]
For complete \(H\), which is deliberately outside the join theorem's noncomplete-factor hypothesis, \(K_m\circ H\) is itself complete and every vertex subset is dual general-position; its polynomial is \((1+z)^{m|V(H)|}\).

## Assumptions and scope

All graphs are finite, simple and undirected. A clique may contain one vertex or be empty. A vertex set \(X\) is **general position** when no selected vertex is internal to a shortest path between two distinct selected vertices. A set \(C\) is **geodesically convex** when every shortest path between two vertices of \(C\) lies in \(C\). A set is **dual general-position** when it is in general position and its complement is geodesically convex. The empty set qualifies. The full counting polynomial records one term \(z^{|X|}\) per labelled feasible set, not one term per graph-isomorphism class. For positive dual general-position sets, inclusion-maximality is with respect to ordinary set containment, not cardinality. The uniform complete-product specialization assumes at least two copies; the formula for complete \(H\) is supplied separately.

## Proof

**1. A distance-two obstruction in a join.** A nonedge of \(J\) necessarily has both endpoints in a single factor \(H_i\). Given any such nonadjacent vertices \(p,q\in H_i\) and any vertex \(w\) of a different factor, the path \(p-w-q\) has length two and is a shortest path. Every pair of vertices in different factors is adjacent. Consequently every graph distance in \(J\) is at most two.

**2. Every nonempty feasible set meets every factor.** Let \(X\ne\varnothing\) be dual general-position, and put \(C=V(J)\setminus X\). If \(X\cap V(H_i)=\varnothing\), then \(H_i\subseteq C\). Since \(H_i\) is noncomplete, choose nonadjacent \(p,q\in V(H_i)\). Any \(x\in X\) lies outside \(H_i\), so \(p-x-q\) is a shortest path with endpoints in \(C\) but internal vertex outside \(C\). This contradicts convexity. Therefore \(X\) meets every factor.

**3. Both colors induce cliques.** Fix any \(i\). Because \(r\ge2\), choose \(j\ne i\) and \(x\in X\cap V(H_j)\) using Step 2. If two nonadjacent vertices \(p,q\in X\cap V(H_i)\) existed, \(p-x-q\) would contradict the general-position property of \(X\). If two nonadjacent vertices \(p,q\in C\cap V(H_i)\) existed, the same path would contradict convexity of \(C\). Thus \(X\cap V(H_i)\) and \(C\cap V(H_i)\) are both cliques in \(H_i\). All cross-factor pairs are adjacent, so \(X\) and \(C\) are cliques in \(J\). Conversely, a clique \(X\) is necessarily in general position, and a clique \(C\) is convex because the shortest path between any two of its distinct vertices is their single edge. This proves the exact characterization. It also shows each factor contributes vertices to both colors, since a noncomplete factor cannot be entirely one clique.

**4. Complement colorings and polynomial.** A partition into two cliques of \(J\) is exactly a proper vertex two-coloring of \(\overline J\), with the first color denoting \(X\). Since the complement of a complete join is the disjoint union \(\overline{H_1}\sqcup\cdots\sqcup\overline{H_r}\), such a coloring exists precisely when all complement components are bipartite. Each connected bipartite component with part sizes \((a,b)\) admits precisely two color orientations, giving terms \(z^a\) and \(z^b\). Isolated components give \(1+z\). Choices across components are independent, yielding the displayed product. All factors are noncomplete, so at least one complement edge lies in each; every proper two-coloring selects vertices in every factor and therefore is nonempty. Accordingly the empty dual general-position set is a separate term \(1\), not counted by the product. Taking degree and evaluating at \(z=1\) proves the largest size and nonempty count. A factor has two maximizing orientations precisely when its bipartition classes have equal size, proving the maximum-set multiplicity.

**5. Inclusion maximality.** In each nontrivial connected bipartite component of \(\overline J\), a proper two-coloring gives each vertex a neighbor of the opposite color; moving only one vertex from one class to the other violates proper coloring. The only vertices whose inclusion in \(X\) can be toggled without losing feasibility are the isolated vertices of \(\overline J\). Consequently a nonempty feasible set is inclusion-maximal precisely when every isolated complement vertex is in \(X\). The product for \(Q_J\) follows. Varying the orientation of a nontrivial connected component changes the cardinality by \(|a-b|\); since the orientations are independent, all inclusion-maximal sets have equal size if and only if every nontrivial component is balanced.

**6. One-vertex-toggle structure.** As an additional structural consequence, let a graph have one vertex for each dual general-position set and edges for symmetric differences of size one. In the bipartite case the induced graph on nonempty solutions is the disjoint union of \(2^{|\mathcal B_+|}\) copies of the \(u\)-dimensional hypercube \(Q_u\), one per orientation of the nontrivial complement components. The empty solution is an isolated vertex: every nonempty solution contains at least one vertex in each of the \(r\ge2\) noncomplete join factors, so no singleton solution exists. In the nonbipartite case it is the sole vertex.

Examples: for \(H=P_3\), \(\overline H\cong K_2\sqcup K_1\), so \(D_{K_m\circ P_3}(z)=1+[2z(1+z)]^m\); for \(H=C_4\), \(\overline H\cong2K_2\), so \(D_{K_m\circ C_4}(z)=1+4^m z^{2m}\); for \(H=P_5\), \(\overline H\) contains a triangle and the only solution is empty. For \(H=K_p\sqcup K_q\) with \(p,q\ge1\), the nonempty polynomial is \((z^p+z^q)^m\), exhibiting a nonconstant maximal-size spectrum when \(p\ne q\).

## Verification

The attached standard-library Python program reconstructs every edge of each complete join, tests the original geodesic condition directly using all distance-two paths, enumerates every candidate vertex set, and independently compares with both a two-clique partition test and a two-coloring cardinality polynomial. It checks 1,085 labelled graph profiles (including nonuniform joins) and 139,216 candidate subsets, obtaining exactly 7,525 feasible subsets. Its terminal output is:

```text
VERIFY_OK graph_profiles=1085 vertex_subsets=139216 admissible_sets=7525 independent_geodesics=PASS complementary_coloring_polynomials=PASS complete_join_equivalence=PASS
```

Run \(`python3 verify.py`\) with the program in the same folder. The brute-force range is finite, whereas the preceding argument proves all stated quantifiers. All computations are exact integer and Boolean operations.

## Relationship to prior work

Tian and Klavžar introduced dual general-position sets and established the characterization by convex complements in their preprint of 27 February 2024 [1]. Their treatment includes the special case \(P_n\vee 2K_1\) for \(n\ge5\), where the dual general-position number vanishes; the current theorem recovers that case but also establishes an all-set equivalence and polynomial for all joins of noncomplete factors. Anand, Changat, Klavžar and Peterin had already determined geodesically convex sets of lexicographic products [2], including conditions that force nontrivial convex subsets to be cliques for noncomplete second factors. Dokyeesun, Klavžar, Kuziak and Tian [3] studied dual general-position in lexicographic products but did not provide the complete-first-factor formula above. The expanded journal discussion explicitly lists the dual general-position number of \(K_m\circ G\) among its remaining questions [4]. The current result supplies an exact set-system classification, full polynomial, and inclusion-maximal counts for this family.

The previously documented complete-multipartite dual general-position formulas (including the case of independent second factors) are consistent with and are special cases of the present theorem; the new scope includes arbitrary internal edges and co-bipartite fibers such as paths and cycles. No priority beyond the inspected literature is asserted.

## Limitations

No claims are made about lexicographic products with arbitrary first factor, mixed joins containing a complete factor, or infinite graphs. This theorem concerns only dual general-position sets; it is not a statement about ordinary, outer or total general-position polynomials. A two-clique partition is a proper coloring of the complement, not a proper coloring of the original graph. In particular, the empty solution must be counted separately when the factors are noncomplete. A finite verifier does not certify the general case. Publication priority remains subject to additional literature review, especially formulations using geodesic convexity or two-clique covers; the result has not undergone an independent mathematical audit.

## References

[1] Jing Tian and Sandi Klavžar, *Variety of general position problems in graphs*, arXiv:2402.17338v1, submitted 27 February 2024. https://arxiv.org/abs/2402.17338

[2] B. S. Anand, M. Changat, S. Klavžar and I. Peterin, *Convex Sets in Lexicographic Products of Graphs*, Graphs and Combinatorics 28 (2012), 77–84, DOI:10.1007/s00373-011-1031-4. https://doi.org/10.1007/s00373-011-1031-4

[3] P. Dokyeesun, S. Klavžar, D. Kuziak and J. Tian, *General position problems in strong and lexicographic products of graphs*, arXiv:2408.15951v1, submitted 28 August 2024. https://arxiv.org/abs/2408.15951

[4] Same authors, journal version, *Computational and Applied Mathematics* 45, article 97 (2026), first published online 15 December 2025, Section 6. https://doi.org/10.1007/s40314-025-03547-7
