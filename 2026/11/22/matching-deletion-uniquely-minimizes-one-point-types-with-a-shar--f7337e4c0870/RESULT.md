# Matching deletion uniquely minimizes one-point types, with a sharp second gap

## Finding
Let \(A\) and \(B\) be two disjoint, pointwise-named antichains of cardinalities \(a,b\geq1\). Delete exactly \(k\) cross-relations from the complete height-two order \(A\oplus B\), where \(0\leq k\leq\min(a,b)\), and retain every other relation from \(A\) to \(B\). Let \(F\) be the bipartite graph of *deleted* cross-relations, and let \(\tau(F)\) denote the number of complete nonalgebraic one-point types over the resulting parameter poset in the countable universal homogeneous partial order.

**Sharp first minimum.** For all these parameters,
\[
\tau(F)\geq M(a,b,k):=3^k2^{a+b-2k}+2^a+2^b+2k-2.
\]
Equality holds if and only if \(F\) is a matching, including the empty matching for \(k=0\).

**Sharp second minimum.** If \(k\geq2\) and \(F\) is not a matching, then
\[
\tau(F)\geq M(a,b,k)+2+3^{k-2}2^{a+b-2k}.
\]
Equality holds if and only if \(F\), after discarding isolated vertices, is the disjoint union of a two-edge star and \(k-2\) isolated edges. The equality configuration exists for every stated \(a,b,k\) with \(k\geq2\); therefore the displayed bound is the exact second distinct attainable count.

In particular, for the standard-example poset \(S_n\) on \(2n\) named elements, where exactly the \(n\) diagonal cross-relations are deleted,
\[
\tau(S_n)=3^n+2^{n+1}+2n-2.
\]
For comparison, the complete two-level order on the same two sets has \(2^{2n}+2^{n+1}-2\) nonalgebraic types; their ratio is asymptotic to \((3/4)^n\). This quantifies the exponential reduction in types associated with deleting a perfect matching of comparabilities.

## Assumptions and scope
The old vertices are all named individually, so extensions differing at a named vertex represent different types. Each relation is a strict partial order. No comparabilities occur within \(A\) or within \(B\); the only possible comparabilities are directed from \(A\) to \(B\). The deleted-incidence graph \(F\) has exactly \(k\) simple edges; isolated vertices are permitted. The bound restricts \(k\) to at most the smaller side so its matching equality case is attainable. The count excludes types identifying the new vertex with an old named vertex. The age of the homogeneous universal poset contains every finite partial order and has the one-point extension property; consequently the legal finite one-point diagrams are exactly the complete nonalgebraic types counted here.

## Proof
**1. Exact reduction to independent sets and bicliques.** Let \(G=K_{a,b}\setminus F\) be the bipartite comparability graph of the parameter order. Write \(i(H)\) for the number of independent vertex sets of a graph \(H\), including the empty set. An inserted point \(x\) determines a lower ideal \(L=\{p:p<x\}\) and an upper filter \(U=\{p:x<p\}\). These sets must be disjoint and satisfy \(L<U\) elementwise, and these conditions are sufficient. Profiles with \(L=\varnothing\) or \(U=\varnothing\) contribute \(2i(G)-1\), since an ideal (or a filter) of a height-two order corresponds to an independent set of \(G\) by complementing its lower (or upper) level. If both are nonempty, then \(L\subseteq A\), \(U\subseteq B\), and every pair in \(L\times U\) must be a comparison in \(G\), equivalently a nonedge of \(F\). These profiles contribute \(i(F)-2^a-2^b+1\). Therefore
\[
\tau(F)=2i(G)+i(F)-2^a-2^b.
\]
Let \(q(F)\) be the number of pairs \((I,J)\) of nonempty sets \(I\subseteq A\), \(J\subseteq B\) such that every edge in \(I\times J\) belongs to \(F\); thus \(q(F)\) counts nonempty labelled complete bipartite subgraphs of \(F\), not necessarily induced ones. Every independent set of \(G\) is either contained in one side or consists of one of these nonempty biclique pairs. Hence \(i(G)=2^a+2^b-1+q(F)\), giving the exact identity
\[
\boxed{\tau(F)=i(F)+2^a+2^b-2+2q(F).}\tag{1}
\]

**2. Universal lower bound and matching equality.** Give each vertex of \(F\) an independent fair binary choice. For each edge \(e\), the event that its two endpoints are not both chosen is decreasing and has probability \(3/4\). Harris's product-measure correlation inequality for decreasing events gives
\[
i(F)\geq2^{a+b}(3/4)^k=3^k2^{a+b-2k}.
\]
Every missing edge supplies one biclique pair of singleton sides, so \(q(F)\geq k\). Equality holds simultaneously for a matching: its \(k\) edge events are independent and its only nonempty bicliques are its individual edges. Conversely, if any two edges share a vertex, they create a biclique with one side of size one and the other of size two, so \(q(F)>k\). Identity (1) proves the first minimum and its complete equality characterization.

**3. Exact second gap.** Suppose \(k\geq2\) and \(F\) is not a matching. Select two edges sharing an endpoint. The probability that neither of these edges is fully chosen is \(5/8\), not \((3/4)^2\). Applying Harris's inequality first to their joint decreasing event and then to the remaining \(k-2\) edge-avoidance events yields
\[
i(F)\geq2^{a+b}(5/8)(3/4)^{k-2}
=3^k2^{a+b-2k}+3^{k-2}2^{a+b-2k}.
\]
The selected pair also produces a non-singleton biclique, so \(q(F)\geq k+1\). Substitution into (1) gives the second inequality. If equality holds, \(q(F)=k+1\). Every pair of edges sharing a vertex produces a *different* non-singleton biclique; thus exactly one unordered pair of edges can share a vertex. This forces \(F\), apart from isolated vertices, to be one two-edge star and \(k-2\) disjoint edges. Conversely, for exactly this configuration, the three-vertex star component has five independent sets, every isolated edge has three, and the remaining isolated vertices each have two. Consequently its independent-set count is exactly \(2^{a+b}(5/8)(3/4)^{k-2}\) and \(q(F)=k+1\), so equality holds. Because \(k\leq\min(a,b)\), the star and matching components fit on the two sides. This proves sharpness and the classification.

**4. Standard-example consequence.** The standard-example order has exactly one deleted cross-relation at each old lower and upper vertex, hence the missing graph is a perfect matching. Set \(a=b=k=n\) in the first equality formula. The complete order is the case \(k=0\), and the asymptotic ratio follows since \(3^n\) dominates the remaining terms in the matched-deletion count, while \(4^n\) dominates the complete-order count.

## Verification
The standalone Python 3 script `artifacts/verify.py` enumerates finite extension diagrams by explicitly adding a new vertex and computing the entire transitive closure, not by applying (1). It compares these independent counts with both independent-set and biclique enumerations for 255 small height-two examples. It checks the exact matching formula for all \(1\leq a,b\leq7\), all feasible matching sizes, and exhaustively checks the first and second minima and their equality classes for \((a,b,k)=(2,2,2),(3,3,3),(3,4,3),(4,4,4)\). Recorded output is `artifacts/verification_output.txt`. These finite computations corroborate the proof; the Harris inequality and the biclique equality argument establish the infinite statements.

## Relationship to prior work
The ideal/filter characterization of one-point extensions is classical. Previously published work on finite-base types of the countable homogeneous poset gives the general identity \(\tau(P_G)=2i(G)+i(\overline G)-2^{|A|}-2^{|B|}\), and separate published results classify the *single-edge* change in the type count, including the case of one deleted relation. These broader counting tools and the one-deletion count are acknowledged as prior mathematics. Neither their stated results nor the other examined indexed work gives the exact sharp global minimum among *all* deletion patterns with a prescribed number of missing cross-relations, or the sharp second value with its complete equality classification. The extra ingredients here are the joint biclique decomposition, a correlation inequality, and the equality analysis for interacting deleted edges. The standard-example exact formula is a specialization of the new extremal formula, not an independent separate claim.

## Limitations
The extremal theorem concerns two prescribed antichain levels and exactly \(k\) deleted cross-comparisons, not arbitrary finite partial orders or arbitrary changes of the order relation. The ordinary numerical type count does not reconstruct the parameter poset. The derivation uses known independent-set and correlation results; there is no claim that those component results are new. Historical priority remains provisional, especially for specialized literature on insertion positions and extremal independent sets of bipartite graphs. Independent mathematical assessment has not been performed.

## References
- I. Dolinka and D. Mašulović, *A universality result for endomorphism monoids of some ultrahomogeneous structures*, arXiv:1009.2892v1 (first public 2010-09-15); the ideal/filter description is a known finite-extension framework.
- O. Pretzel, *A construction for partially ordered sets*, Discrete Mathematics 32 (1980), 59–68, DOI:10.1016/0012-365X(80)90100-4 (insertion-position background; complete text not inspected).
- T. E. Harris, *A lower bound for the critical probability in a certain percolation process*, Proc. Cambridge Philos. Soc. 56 (1960), 13–20 (positive correlation in independent product measures).
- *Sharp one-comparability sensitivity and local counting hardness for random-poset one-types*, publicly available mathematical record (2026), identifier `9c2af418ff79` (general type identity and local response, previously established).
- *One comparability can increase finite-poset one-point type counts exponentially*, publicly available mathematical record (2026), identifier `828ff1d8f784` (one deleted relation, previously established).
- *Five-statistic convex-set polynomial and defect localization for standard-example posets*, publicly available mathematical record (2026), identifier `84ba1197a0d2` (different convex-subset polynomial).
