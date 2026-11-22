# Non-contingency introspection on all orientations of finite trees: independent branching and a bivariate labelled census

## Finding

Let a finite **oriented forest** be obtained by orienting each edge of a finite simple undirected forest in exactly one direction, with no loops or opposite paired arcs. In its ordinary Boolean Kripke semantics put \(\Delta\varphi:=\Box\varphi\lor\Box\neg\varphi\), with vacuous truth at vertices with no successors. The formula \(\Delta p\to\Delta\Delta p\) is valid at all vertices under every valuation if and only if the set \(B=\{v:d^+(v)\ge2\}\) is independent in the underlying forest.

The criterion has an exact **branch-refined labelled census**. For each integer \(n\ge1\), let \(t_n(q)\) be the polynomial summing \(q^{|B|}\) over all valid orientations of all trees whose vertices are labelled by \(\{1,\ldots,n\}\). Let
\[
T(z,q)=\sum_{n\ge1}t_n(q)\frac{z^n}{n!}.
\]
There is a unique quadruple of formal power series \(A,B_1,C,D\in\mathbb Q[q][[z]]\), all with zero constant coefficient, determined by
\[
\begin{aligned}
A&=z\exp(A+B_1),\\
B_1&=zq\exp(A)(\exp(C)-1),\\
C&=z\exp(A+B_1)(1+C+D),\\
D&=zq\exp(A)(\exp(C)-1-C).
\end{aligned}
\]
The complete census is given by
\[
\boxed{z\frac{\partial T}{\partial z}=C+D.}
\]
In particular, the unweighted counts \(t_n(1)\) for \(1\le n\le9\) are
\[
1,\ 2,\ 12,\ 128,\ 1940,\ 38292,\ 937048,\ 27442816,\ 937015920.
\]
For every \(n\ge1\), the constant coefficient is exactly \([q^0]t_n(q)=n^{n-1}\). Moreover, **five** is the smallest order with a failing oriented tree, with exactly \(60\) failing labelled orientations at that order.

## Assumptions and scope

All structures in the criterion are finite, irreflexive, simple, and have an undirected forest underlying graph. Validity is for **every** Boolean valuation of \(p\), not an average or a prescribed valuation. The number of labelled trees is \(n^{n-2}\) for \(n\ge2\); the sum defining \(t_n(q)\) counts each edge orientation separately, not only isomorphism classes. The mark \(q\) counts vertices having at least two outgoing arcs, restricted to those orientations satisfying the modal formula. Exponentials are formal power-series exponentials; the equations determine all coefficients inductively because of their leading factor \(z\).

## Proof

**1. Functional vertices.** If \(d^+(v)\le1\), then \(v\models\Delta\psi\) for every formula \(\psi\) and valuation: all zero or one successors agree vacuously. Consequently \(v\models\Delta\Delta p\) whenever \(d^+(v)\le1\).

**2. Sufficiency of independence.** If \(B\) is independent, take a vertex \(v\) with at least two successors. Every successor \(u\) satisfies \(d^+(u)\le1\), so each satisfies \(\Delta p\). Therefore \(v\models\Delta\Delta p\) regardless of its truth value for \(\Delta p\). The case \(d^+(v)\le1\) is covered by Step 1.

**3. Necessity and a distinguishing valuation.** Suppose \(B\) contains adjacent vertices. Write their uniquely oriented edge as \(v\to u\), so \(d^+(v)\ge2\) and \(d^+(u)\ge2\). Choose a second successor \(w\ne u\) of \(v\) and two distinct successors \(a,b\) of \(u\). Because the underlying graph is a forest, the sets of successors of \(u\) and \(w\) are disjoint, and neither contains a successor of \(v\). Make \(p\) true at every successor of \(v\), make \(p\) true at \(a\) and false at \(b\), and make \(p\) constant at the successors of \(w\). These prescriptions are compatible. Then \(v\models\Delta p\), while \(u\not\models\Delta p\) and \(w\models\Delta p\); hence \(v\not\models\Delta\Delta p\). The characterization follows.

**4. Four planted classes.** To enumerate the valid orientations, root an undirected labelled tree at a distinguished vertex, adjoin a *formal parent edge*, and let \(a\in\{0,1\}\) indicate whether the edge points from the vertex to its parent (contributing \(a\) to its outdegree). Let \(F_{a,b}\) count the planted structures, with \(b\in\{0,1\}\) indicating whether its outdegree is at least two; every pair of adjacent branching vertices is forbidden. We set \(A=F_{1,0}\), \(B_1=F_{1,1}\), \(C=F_{0,0}\), and \(D=F_{0,1}\). A nonbranching vertex with \(a=1\) has no outgoing-child edges, whose incoming-child contributions form an arbitrary labelled set drawn from \(A+B_1\); this gives \(A=z\exp(A+B_1)\). A branching vertex with \(a=1\) has at least one outgoing-child edge and cannot have any branching child. Its incoming children are of type \(A\), outgoing children of type \(C\), giving \(B_1=zq\exp(A)(\exp(C)-1)\). With \(a=0\), a nonbranching vertex has zero or one outgoing child, giving \(C=z\exp(A+B_1)(1+C+D)\). A branching vertex with \(a=0\) requires at least two outgoing children, none branching, giving \(D=zq\exp(A)(\exp(C)-1-C)\). The exponential factors count unordered sets of distinctly labelled children. Each child is counted exactly once, with the direction of its parent edge fixed by its state.

**5. Removing the root and the zero-branch coefficient.** At an actual root there is no parent edge, so the rooted-tree EGF is \(C+D\). A labelled unrooted oriented tree on \(n\) vertices has exactly \(n\) choices of distinguished root and the root does not change its orientation. Therefore its EGF satisfies \(z\partial T/\partial z=C+D\). If \(|B|=0\), every vertex has outdegree at most one; the sum of outdegrees is \(n-1\), so there is exactly one sink. Conversely, choosing any sink in an undirected tree and orienting all edges toward it yields exactly one such orientation. By Cayley's formula there are \(n\cdot n^{n-2}=n^{n-1}\) zero-branch orientations for \(n\ge2\), also valid at \(n=1\).

**6. First failure.** Adjacent vertices of outdegree at least two require at least five vertices: if the connecting edge is \(v\to u\), then \(v\) needs one further outgoing neighbour and \(u\) needs two further outgoing neighbours, all distinct in a forest. At order five, the only underlying tree supporting such an arc has adjacent vertices of undirected degrees two and three, with their remaining neighbours leaves. Exactly one edge orientation makes both centres have outdegree at least two. There are \(5\cdot4\cdot3=60\) labelled copies of that tree, yielding exactly sixty invalid labelled orientations at order five. The general equations establish all remaining coefficients for every order.

## Verification

An executable standard-library Python checker is provided as `verify.py`. It computes the formal labelled EGFs through order nine, independently enumerates all \(n^{n-2}\) labelled trees and their \(2^{n-1}\) edge orientations through order seven using Prüfer codes, and compares the branch-independence criterion against literal all-valuation Kripke semantics through order six. It also checks the branch-refined polynomials through order seven against independently obtained finite counts. All assertions pass. The infinite-domain statement for each \(n\) is proved in the preceding six steps; finite checks provide only reproducible stress tests.

The computed polynomials for orders five through seven are
\[
\begin{aligned}
t_5(q)&=625+1255q+60q^2,\\
t_6(q)&=7776+26196q+4320q^2,\\
t_7(q)&=117649+599529q+216510q^2+3360q^3.
\end{aligned}
\]

## Relationship to prior work

Zolin's 1999 characterization of frames validating \(\Delta p\to\Delta\Delta p\) (Theorem 4.1, the \(4^\flat\) condition) is a **general prior frame-correspondence theorem**. The forest branching-independence condition is a special case of that broader correspondence, presented here only to identify the exact combinatorial objects being counted, **not** as an independent novelty claim. Earlier work has also counted the much narrower class of outward-oriented rooted trees satisfying a related branching exclusion. Neither inspected source supplies the all-orientations, rooted-and-unrooted, branch-refined labelled EGF above. General orientation-enumeration literature, including noncrossing tree outdegree enumerations and forbidden-orientation asymptotics, treats different families or statistics. The proposed contribution is specifically the exact all-labelled-tree bivariate modal-validity census, including the zero-branch coefficient and the first failure order.

## Limitations

The implicit formal-series system is exact but not claimed to be rational, algebraic, or asymptotically analyzed. Nothing here extends to directed graphs with cycles or multiple arcs. The first-order modal correspondence itself is known from Zolin. The full text of one plausibly related previously published enumeration on outward rooted trees was not available to this inspection, so its precise technical details could not be compared beyond its accessible published summary. Other historical priority gaps may remain; no independent validation has been performed.

## References

1. E. E. Zolin, *Completeness and Definability in the Logic of Non-contingency*, Notre Dame Journal of Formal Logic 40(4) (1999), 533–547. DOI: https://doi.org/10.1305/ndjfl/1012429717 . Open-access PDF: https://www.cs.man.ac.uk/~ezolin/pub/zolin_1999_NDJFL.pdf .
2. Y. Wang and L. Zenger, *Proof Theory for Non-Contingency Logic*, arXiv:2609.38975, first public version 2026-09-30. https://arxiv.org/abs/2609.38975 .
3. *Noncontingency introspection on finite out-trees: forbidden branches and exact labelled enumeration*, published research record (2026-11-02), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-noncontingency-introspection-on-finite-out-trees-forbidden-branc--abc4d74cf085 . Only its published search summary was accessible during this comparison.
4. I. O. Okoth and S. Wagner, *Locally Oriented Noncrossing Trees*, Electronic Journal of Combinatorics 22(3) (2015), article P3.36. https://doi.org/10.37236/5164 .
5. *Counting H-free orientations of graphs*, Mathematical Proceedings of the Cambridge Philosophical Society (2022). https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/counting-hfree-orientations-of-graphs/A6A40824A87BECB72C1402A11FD83EE1 .
