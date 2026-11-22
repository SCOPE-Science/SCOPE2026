# Cayley rigidity of maximal open-adjacency types in finite forests

## Finding

Let \(F=(V,E)\) be any nonempty finite undirected simple forest, let \(A\subseteq V\) have \(m\geq1\) individually named vertices, and let
\[
\mathcal T_F(A)=\{N_F(v)\cap A:v\in V\}
\]
be the family of distinct quantifier-free open-adjacency one-point traces over \(A\). Let \(t(F,A)\) be the number of connected components of the induced forest \(F[A]\) containing at least two vertices. Then
\[
\left|\mathcal T_F(A)\right|\leq 2m-t(F,A)\leq2m.
\]
Both inequalities are sharp. Equality \(\left|\mathcal T_F(A)\right|=2m\) holds **if and only if** there exists a spanning tree \(T\) on the labelled vertex set \(A\) such that
\[
\mathcal T_F(A)=\{\varnothing\}\ \cup\ \big\{\{a\}:a\in A\big\}\ \cup\ \big\{\{a,b\}:\{a,b\}\in E(T)\big\}.
\]
For \(m=1\), the edge family is empty and equality simply means that both possible traces occur.

For \(m\geq2\), the distinct maximum-cardinality trace families on a fixed labelled parameter set \(A\) are therefore in bijection with its labelled spanning trees; there are exactly \(m^{m-2}\) such families. Any forest realizing \(2m\) traces has at least \(3m-1\) vertices. At that minimum order, its connected graph is forced, up to an isomorphism fixing each marked vertex, to be the graph obtained from the corresponding spanning tree on \(A\) by subdividing every edge once and attaching one new leaf to each vertex of \(A\). This construction also works for \(m=1\), where it is a single edge with one marked endpoint. In particular, the classwide open-neighborhood shatter function for finite forests and for finite trees is exactly \(2m\) for every \(m\geq1\), and equals \(1\) for \(m=0\) when the graph is nonempty.

## Assumptions and scope

All graphs are finite, simple, loopless and undirected; a forest has no cycles. The parameter set \(A\) is named, so two trace families differing by a permutation of \(A\) count as different. A type is a subset of \(A\), interpreted as the exact truth set of the adjacency atoms \(E(x,a)\); no higher-quantifier or closed-neighborhood types are asserted to satisfy these formulas. The host forest may have arbitrarily many vertices or components. The equality characterization concerns the *trace family*, not the uniqueness of a larger host; arbitrary additional vertices may be present if they introduce no new traces and preserve acyclicity.

## Proof

**1. Acyclicity budget for external patterns.** Let \(i\) be the number of isolated components of \(F[A]\), \(t=t(F,A)\) the number of its nontrivial components, and \(c=i+t\) the total number of components of \(F[A]\). Let \(W\) consist of unmarked vertices adjacent to at least two vertices of \(A\). No member of \(W\) can be adjacent to two vertices in the same component of \(F[A]\), since the path between them in that component together with the two incident edges would form a cycle. Contract every component of \(F[A]\), retain all vertices of \(W\), and retain only edges between these contracted components and \(W\). The resulting bipartite graph is a forest because contraction and deletion cannot create a cycle from a forest. Every \(w\in W\) has degree \(d_A(w)=|N_F(w)\cap A|\geq2\) in this graph. Therefore
\[
\sum_{w\in W}\big(d_A(w)-1\big)\leq c-1,
\qquad |W|\leq c-1.
\]
The number of distinct external traces of cardinality at least two is at most \(|W|\).

**2. Internal pattern budget.** Each nontrivial component of \(F[A]\) on \(s\geq2\) vertices is a tree with at least two leaves, so it has at most \(s-2\) vertices of degree at least two within \(F[A]\). There are thus at most \(m-i-2t\) marked vertices whose traces have size at least two. Every trace of size zero contributes at most one type, and every singleton trace contributes at most \(m\) types. Consequently
\[
\begin{aligned}
|\mathcal T_F(A)|
&\leq1+m+|W|+(m-i-2t)\\
&\leq1+m+(i+t-1)+(m-i-2t)=2m-t.
\end{aligned}
\]
This holds also when \(W\) is empty or \(F[A]\) consists entirely of isolated vertices. The term for absent empty or singleton traces is merely an upper bound.

**3. Equality rigidity.** Suppose \(|\mathcal T_F(A)|=2m\). The strengthened bound forces \(t=0\): the marked vertices are pairwise nonadjacent. Every marked vertex then has the empty trace, so equality requires all \(m\) singleton traces and exactly \(m-1\) further distinct traces. Those further traces must be realized by members of \(W\). By the first budget, \(|W|\leq m-1\); hence \(|W|=m-1\), each member gives a distinct trace, and every \(d_A(w)\) equals \(2\), because the sum of \(d_A(w)-1\) is bounded above by \(m-1\). The contracted incidence forest has \(m+(m-1)\) vertices and \(2(m-1)\) edges, so it is connected and thus a tree. Suppressing the \(m-1\) degree-two external vertices yields a spanning tree \(T\) on \(A\). Its edges are exactly the two-element traces, proving the necessary form.

Conversely, for any tree \(T\) on \(A\), subdivide each edge once, with a distinct new vertex per edge, and attach one new pendant vertex at every marked vertex. This is a tree. Its marked vertices see no marked neighbors, the pendant vertices produce all singletons, and the subdivision vertices produce precisely the edges of \(T\). Hence it has exactly \(1+m+(m-1)=2m\) different traces.

**4. Enumeration and minimum size.** Every extremal trace family determines \(T\) by its two-element members, and every labelled tree \(T\) produces an extremal family. Cayley's labelled-tree theorem gives \(m^{m-2}\) distinct families when \(m\geq2\). Since \(A\) is independent at equality, the \(m\) singleton traces must be realized by \(m\) distinct unmarked vertices, and the \(m-1\) two-element traces by further distinct unmarked vertices. Thus \(|V(F)|\geq m+m+(m-1)=3m-1\). The construction has this size. At equality in the vertex bound, the required \(3m-2\) edges already form the connected subdivision-and-leaves tree on all vertices, leaving no additional edges or vertices. The case \(m=1\) follows directly from the same construction and the two possible traces.

## Verification

The self-contained Python standard-library checker `CHECK.py` enumerates every labelled simple forest on up to six vertices and all nonempty marked subsets. For each it checks the stronger inequality, and for equality verifies independence of the marked set, the recovered spanning-tree trace family and the size bound. It separately checks explicit witnesses up to seventeen marked vertices and enumerates all Prüfer trees for labelled marked sets of sizes two through five, comparing the number of distinct trace families with Cayley's formula. Invoke from a directory containing `CHECK.py` using `python3 CHECK.py`; it prints `ALL_CHECKS_OK` when the checks pass. These finite tests corroborate the all-order proof but do not replace it.

## Relationship to prior work

Sylvester, Zamaraev and Zhukovskii (2026, arXiv:2611.15299) prove that every small hereditary graph class has *linear* open-neighborhood complexity. That includes forests but supplies neither the exact coefficient, the equality classification nor the count of extremal trace families. Berthe, Foucaud, Lehtilä and Parreau (2026, arXiv:2607.16889, Section 3) prove the sharp \(\lfloor 7m/3\rfloor\) bound for *closed* neighborhoods in forests; their construction and counting are different, and the closed-neighborhood result does not imply the present open-neighborhood equality form. Beaudou et al. (2025, arXiv:2501.08895) study larger-radius neighborhood and distance-profile complexity, primarily via asymptotic parameterized bounds. The incidence-forest reduction is related to the component-contraction idea in Berthe et al.; no originality is claimed for contraction itself or for Cayley's theorem.

## Limitations

This result concerns only one-step, open-adjacency, quantifier-free one-point types, not general first-order types or closed neighborhoods. The minimum-host uniqueness requires that the marked vertices be fixed pointwise; unrestricted graph isomorphism counts differ. The literature comparison establishes an evidence-based distinction from inspected formulations, not a guarantee that no historically equivalent formula appears elsewhere. The Beaudou et al. full text was not materially inspected, so an unnoticed special case in older work remains a residual priority risk. Finite computations do not verify the infinite range; the proof does.

## References

1. John Sylvester, Viktor Zamaraev and Maksim Zhukovskii, *Small classes have linear neighbourhood complexity*, arXiv:2611.15299, first public November 11, 2026, https://arxiv.org/abs/2611.15299.
2. Gaétan Berthe, Florent Foucaud, Tuomo Lehtilä and Aline Parreau, *Neighbourhood complexity and identification problems for graphs of bounded treewidth and pathwidth*, arXiv:2607.16889, first public July 18, 2026, https://arxiv.org/abs/2607.16889.
3. Laurent Beaudou, Jan Bok, Florent Foucaud, Daniel A. Quiroz and Jean-Florent Raymond, *Profile and neighbourhood complexity of graphs with excluded minors and tree-structured graphs*, arXiv:2501.08895, first public January 15, 2025, https://arxiv.org/abs/2501.08895.
4. A. Cayley, *A theorem on trees*, Quarterly Journal of Mathematics 23 (1889), 376–378 (classical labelled-tree formula).
