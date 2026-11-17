# Exact fort-transversal relaxation and packing gap on wheel graphs

## Finding
For each integer \(n\ge3\), let \(W_{n+1}=K_1\vee C_n\), with one hub and \(n\) cyclically labelled rim vertices. A **fort** is a nonempty set \(F\) of vertices for which every vertex outside \(F\) has either zero or at least two neighbors in \(F\). Let \(\mathcal F_{\min}\) be its inclusion-minimal forts. Define the fort-packing number \(\operatorname{ft}(W_{n+1})\) as the maximum number of pairwise disjoint forts and the fractional fort-transversal number
\[
Z^*(W_{n+1})=\min\left\{\sum_v w_v:w_v\ge0,\ \sum_{v\in F}w_v\ge1\text{ for all }F\in\mathcal F_{\min}\right\}.
\]
Then, with \(a=\lceil n/2\rceil\) and \(b=\lceil n/3\rceil\),
\[
\boxed{\operatorname{ft}(W_{n+1})=2,\qquad Z^*(W_{n+1})=1+\frac{n-b}{a},\qquad Z(W_{n+1})=3.}
\]
Here \(Z\) is the ordinary zero-forcing number. An optimal fractional transversal places weight \(1/a\) at every rim vertex and \(1-b/a\) at the hub. The equality \(Z^*=\operatorname{ft}=2\) holds exactly at \(n\in\{3,4,5,7\}\); for every \(n\ge8\), \(2<Z^*<3\), and \(Z-Z^*\to2/3\).

The **complete size-refined minimal-fort generating functions** of wheel graphs, including the hub-containing count sequence, were established earlier in [3] and are **not** claimed here. The present assertion is the sharp all-order fort-transversal and packing-law separation, not an original enumeration theorem or a new asymptotic fort-count formula.

## Proof
Call the hub \(h\). For an inclusion-minimal fort avoiding \(h\), its rim complement is a maximal independent set of \(C_n\) [3]. Therefore the smallest such fort has exactly \(a=\lceil n/2\rceil\) rim vertices, because a largest independent set has size \(\lfloor n/2\rfloor\). If an inclusion-minimal fort contains \(h\), it is \(\{h\}\cup D\), where \(D\) is a minimal dominating set of \(C_n\), excluding the two alternating configurations when \(n\) is even [3]. Every such \(D\) has size at least \(b=\lceil n/3\rceil\). There exists one of size exactly \(b\) for all \(n\ge3\): choose a minimum dominating set, and when \(n=4\) select two adjacent vertices instead of an alternating pair. This produces an actual minimal hub-containing fort of size \(b+1\).

Because rim rotations preserve the set of minimal forts, averaging any fractional transversal over all these rotations preserves feasibility and total weight. Thus an optimum exists with weight \(u\ge0\) on each rim vertex and \(v\ge0\) on the hub. The preceding two minimum-size witnesses show that its complete constraints reduce to
\[
au\ge1,\qquad v+bu\ge1.
\]
Conversely these two inequalities imply every minimal-fort constraint by the same lower bounds on rim counts. Since \(b\le a<n\), minimizing \(nu+v\) gives \(u=1/a\) and \(v=1-b/a\); every increase of \(u\) above \(1/a\) raises the objective even after the best admissible decrease of \(v\). Consequently \(Z^*=n/a+1-b/a\).

Any two disjoint hub-free forts would need at least \(2a\) rim vertices; three disjoint forts are impossible since at most one may use the hub and \(2a\ge n\). For even \(n\), the two alternating rim sets are disjoint forts, showing \(\operatorname{ft}\ge2\). For odd \(n\), take a maximum independent set \(I\) of \(C_n\); the sets \(V(C_n)\setminus I\) and \(\{h\}\cup I\) are disjoint forts. Hence \(\operatorname{ft}=2\). Every vertex in \(W_{n+1}\) has degree at least three (also for \(n=3\)), so two initially colored vertices cannot cause a first zero-forcing move. The hub and two adjacent rim vertices do force all other rim vertices successively for \(n\ge4\), and at \(n=3\) the graph is \(K_4\), for which three initial vertices force the last. Thus \(Z=3\).

Finally, substitute the ceiling functions and compare integers. Equality \(1+(n-b)/a=2\) is equivalent to \(n=a+b\), which holds precisely at \(n=3,4,5,7\). For \(n\ge8\), \(a+b<n\) and \(n-b<2a\), yielding \(2<Z^*<3\). Dividing by \(n\) gives \(Z^*\to 1+(2/3)/(1/2)=7/3\), so \(Z-Z^*\to2/3\).

## Scope, verification and prior mathematical work
The fractional parameter is the LP transversal of the **minimal-fort hypergraph**, not a different three-color zero-forcing game. The proof applies to every labelled ordinary wheel, including the triangular-rim case; finite enumeration is corroboration and not a substitute for the all-order graph/LP argument. Direct independent exhaustive fort tests for rim sizes 3 through 9 found the asserted tight size classes and feasible rational weights. The base 2018 fort formulation, its LP version, and structural results for other graph families are earlier work [1]. The 2024 wheel paper [2] proves partial wheel counts and lists the central-hub sequence. Crucially, [3] already proves the **entire** wheel minimal-fort cardinality polynomial and the rational generating function for that sequence; those previously established results are not treated as new here. No inspected earlier source supplies the exact fraction \(1+(n-\lceil n/3\rceil)/\lceil n/2\rceil\) together with the all-order packing separation. An unindexed wheel LP calculation remains a historical-priority risk. No generalization to other cone graphs or other fractional forcing definitions is asserted.

## References
1. T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal, H. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904 (2023).
2. P. Becker, T. R. Cameron, D. Hanely, B. Ong, J. P. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963 (2024), especially Section 5.1.
3. *Complete minimal-fort polynomials of wheel graphs*, mathematical result dated November 2, 2026, https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-complete-minimal-fort-polynomials-of-wheel-graphs-and-a-rational--6c829f2312f9/RESULT.md .
