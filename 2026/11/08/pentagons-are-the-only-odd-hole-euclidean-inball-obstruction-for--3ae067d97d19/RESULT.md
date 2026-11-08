# Pentagons are the only odd-hole Euclidean inball obstruction for h-perfect stable-set polytopes

## Finding
Let \(G=(V,E)\) be any finite nonempty simple **h-perfect graph**, let \(n=|V|\), and put \(q=\omega(G)\). In the standard characteristic-vector realization \(P=\operatorname{STAB}(G)\subset\mathbb R^V\), the exact Euclidean inradius is
\[
\boxed{r(P)=\begin{cases}\displaystyle\frac{2}{5+\sqrt5},&q=2\text{ and }G\text{ contains a five-cycle},\\[3pt]\displaystyle\frac{1}{q+\sqrt q},&\text{otherwise}.\end{cases}}
\]
The vector \(r(P)\mathbf1\) is always an incenter. In particular, every h-perfect graph with clique number at least three obeys the same radius law as a perfect graph, even if it is itself nonperfect; among triangle-free h-perfect graphs, precisely those containing a pentagon have a smaller radius than the clique-only prediction. No odd hole of length at least seven ever controls the inradius.

Let \(r=r(P)\), and write \(x(S)=\sum_{v\in S}x_v\). The **full set** of centers of radius-\(r\) balls is the explicit polytope
\[
\mathcal I(P)=\{c\in\mathbb R^V:\ c_v\ge r\ (v\in V),\quad c(K)+r\sqrt{|K|}\le1\ (K\text{ a clique}),\quad c(C)+r\sqrt{|C|}\le(|C|-1)/2\ (C\text{ an odd cycle of length at least five})\}.
\]
For the following definition, let \(U\subseteq V\) be the union of the vertex sets of **all five-cycles** when \(q=2\) and at least one exists; in every other case let \(U\) be the union of all maximum cliques. Then
\[
\boxed{\dim\mathcal I(P)=n-|U|,\qquad \mathcal I(P)\text{ is a singleton}\iff U=V.}
\]
At the specific uniform incenter \(r\mathbf1\), all \(n\) nonnegativity facets touch the ball. The **only other tangent facets** are all five-cycle facets in the exceptional case and all maximum-clique facets otherwise. Hence the total tangent-facet count is \(n+h_5\) in the exceptional case, where \(h_5\) is the number of distinct five-cycles, and \(n+m_q\) otherwise, where \(m_q\) counts maximum cliques.

## Assumptions and scope
A graph is h-perfect if its stable-set polytope is exactly the intersection of nonnegativity, clique, and odd-cycle inequalities. The latter are \(x(C)\le(|C|-1)/2\) for each odd cycle \(C\); it suffices to use chordless odd cycles of length at least five, together with maximal cliques. This is the standard description recalled in Miyazaki (2020), Definition 2.3 and Lemma 3.4. Every graph under consideration is finite, simple, and nonempty, and the standard Euclidean metric is imposed on the full coordinate space \(\mathbb R^V\). No quotient or affine distortion is used. Here a maximum clique has size \(q\), while an inclusion-maximal clique need not be maximum.

The theorem uses every **distinct vertex set** of a five-cycle as one pentagonal facet in the exceptional triangle-free case; different cyclic orderings of the same five vertices are not counted multiple times. The description of \(\mathcal I(P)\) may equivalently restrict its clique constraints to inclusion-maximal cliques and odd-cycle constraints to chordless odd cycles. Its dimension is intrinsic affine dimension, not number of inequalities.

## Proof
**1. Radius reduction to normalized facet barriers.** If a Euclidean ball \(B(c,r)\) lies in \(P\), each coordinate lower inequality forces \(c_v\ge r\). For a clique \(K\) of size \(s\), the Euclidean norm of the facet normal \(\mathbf1_K\) is \(\sqrt s\), so \(c(K)+r\sqrt s\le1\). Combining with \(c(K)\ge sr\) yields
\[
 r\le f(s):=\frac1{s+\sqrt s}.
\]
For an odd cycle \(C\) of length \(\ell\ge5\), similarly \(c(C)+r\sqrt\ell\le(\ell-1)/2\) and \(c(C)\ge\ell r\), whence
\[
 r\le g(\ell):=\frac{\ell-1}{2(\ell+\sqrt\ell)}=\frac12\left(1-\frac1{\sqrt\ell}\right).
\]
The clique function \(f(s)\) is strictly decreasing in \(s\ge1\); the odd-cycle function \(g(\ell)\) is strictly increasing in \(\ell\ge5\). In the absence of any odd cycle of length at least five, only \(f(q)\) matters. If such a cycle exists, its smallest possible length is at least five, and
\[
 g(5)=\frac2{5+\sqrt5}<f(2)=\frac1{2+\sqrt2}<g(7),\qquad f(3)<g(5).
\]
Thus for \(q\ge3\), all odd-cycle constraints have weaker radius bounds than \(f(q)\). For \(q=2\), a five-cycle is the unique possible strongest odd-cycle obstruction, and absent five-cycles the remaining odd-cycle constraints give weaker bounds than \(f(2)\). For \(q=1\), the graph is edgeless and has no cycles. This establishes the asserted universal upper bound.

Now take \(c=r\mathbf1\) with \(r\) equal to the displayed bound. For every nonnegativity constraint, the ball has distance exactly \(r\). A clique of size \(s\le q\) satisfies \(r(s+\sqrt s)\le1\), and an odd cycle of length \(\ell\) satisfies \(r(\ell+\sqrt\ell)\le(\ell-1)/2\), by the comparisons above. Therefore the full radius-\(r\) Euclidean ball lies in every defining halfspace, proving the inradius and existence of the uniform center. The same inequalities for a general center prove the exact formula for \(\mathcal I(P)\).

**2. Forced coordinates and complete incenter dimension.** In the exceptional regime, each five-cycle \(C\) has \(r=g(5)\). Every incenter satisfies \(c_v\ge r\) and \(c(C)+r\sqrt5\le2\). The latter right-hand side equals \(5r\), so \(c(C)=5r\) and every \(c_v=r\) on \(C\). Thus all coordinates in \(U\) are fixed. In every other regime, a maximum clique \(K\) of size \(q\) has \(r=f(q)\); combining \(c(K)\ge qr\) with \(c(K)+r\sqrt q\le1=qr+r\sqrt q\) similarly forces \(c_v=r\) for all \(v\in K\). This proves \(\dim\mathcal I(P)\le n-|U|\) in both regimes.

Every constraint not defining these critical supports is **strict** at \(c=r\mathbf1\). Indeed, a noncritical clique is smaller than \(q\) except in the exceptional pentagon regime, where even size-two cliques are strictly slack; and a noncritical odd-cycle has length at least seven in the exceptional regime or has \(g(\ell)>r\) otherwise. There are finitely many such inequalities. Consequently sufficiently small, simultaneous, independently variable positive perturbations \(c_v=r+\varepsilon_v\) on the coordinates outside \(U\), leaving \(c_v=r\) on \(U\), preserve them all. The resulting \((n-|U|)\)-dimensional box lies in \(\mathcal I(P)\). Hence \(\dim\mathcal I(P)=n-|U|\), including the uniqueness criterion.

**3. Exact tangencies and irredundancy.** The uniform center lies at distance exactly \(r\) from every coordinate facet \(x_v=0\). Noncritical clique and odd-cycle halfspaces are at strictly larger normalized distance by Step 1, while every critical one is at distance exactly \(r\). It remains to check that critical hyperplanes are genuine facets, rather than merely a potentially redundant inequality system.

Each coordinate inequality is a facet: the origin and the \(n-1\) singleton stable-set points other than \(e_v\) affinely span its supporting hyperplane. For a maximal clique \(K\) of size \(s\), the \(s\) singleton points \(e_u\), \(u\in K\), and for each \(w\notin K\) a point \(e_w+e_{u(w)}\) with \(u(w)\in K\) nonadjacent to \(w\), lie on \(x(K)=1\). Such \(u(w)\) exists by maximality, and the \(n\) points are affinely independent using the coordinates outside \(K\), followed by the coordinates within \(K\). Thus all maximum-clique hyperplanes are facets, including the singleton cliques in an edgeless graph.

In the exceptional case \(q=2\), \(G\) is triangle-free. Let \(C\) be any five-cycle. Its five stable-set pairs \(\{j,j+2\}\), with indices modulo five, all lie on \(x(C)=2\) and their incidence vectors are linearly independent: the associated cyclic matrix \(I+P^2\) is invertible because five is odd. For any outside vertex \(w\), the neighbors of \(w\) inside \(C\) are independent (otherwise there would be a triangle), hence there are at most two. The other at least three cycle vertices contain a stable pair \(\{a,b\}\), so \(e_w+e_a+e_b\) also lies on \(x(C)=2\). Taking one such point for every \(w\notin C\) extends the five independent face points to \(n\) affinely independent face points, since the outside coordinates form an identity block. The five-cycle inequality therefore defines a facet. Distinct five-vertex sets give distinct facet normals. This proves the complete tangent-facet classification and the count.

## Verification
The analytical proof covers all finite h-perfect graphs; no computational enumeration or graph-recognition oracle is needed for its universal validity. The code `verify.py` re-derives the candidate radius from clique sizes and five-cycles and independently maximizes the largest ball radius by linear programming against every coordinate, clique, and odd-cycle inequality for 14 test graph profiles, including isolated vertices, odd cycles of lengths five, seven, and nine, and disjoint unions of odd cycles with cliques. It verifies the uniform ball against the same halfspaces, and numerically checks the normalized odd-cycle threshold sequence. One successful execution reported `HPERFECT_EUCLIDEAN_INBALL_CHECKS_PASSED profiles= 14 cliques= 169 odd_cycles= 15 coordinates= 85`.

This finite check is **not** an exhaustive search over h-perfect graphs, nor does it certify the symbolic theorem. Some graph-profile cycle enumeration in the checker retains one cycle per vertex set, which is sufficient for the selected test families but not a general representation of arbitrary graphs. The proof is the certification for its universal quantifiers.

## Relationship to prior work
Miyazaki's 2020 article (arXiv:2005.03259) explicitly supplies the h-perfect inequality description, in particular its Lemma 3.4 identifying maximal-clique and chordless-odd-cycle barriers. Its stated results concern Ehrhart rings and Gorenstein properties, not Euclidean inballs; its characterization is used here, not rederived or claimed as original.

The published result *Clique number controls the exact Euclidean inradius of every perfect stable-set polytope* (2026) proves the clique-radius formula and center rigidity **for perfect graphs**. The current claim agrees completely on perfect graphs; that special case is established prior work. The substantive extension is to possibly nonperfect h-perfect graphs, with a single explicit geometric obstruction at five-cycles when the clique number is two, and a full contact/incenter-dimension classification including that obstruction. The nonperfect graph \(C_5\) shows the perfect-graph proof cannot simply be asserted for h-perfect graphs without the pentagon distinction. The 2026 fractional-coloring formula for Minkowski asymmetry of stable-set polytopes concerns an affine-invariant asymmetry, not this Euclidean radius. The 2021 convex-hull study by Bärmann and Schneider treats odd-hole inequalities but does not assert an insphere classification.

## Limitations
The metric is tied to the canonical incidence-vector embedding and changes under nonorthogonal affine transformations. For non-h-perfect graphs, non-clique and non-odd-cycle inequalities can change the inradius; no assertion is made about them. The complete incenter formula is a finite inequality description, not a closed vertex enumeration in general. The facet count concerns the **uniform** optimal center, not the potentially additional tangencies at other optimal centers. Originality beyond the inspected literature is provisional: a prior equivalent statement in general Chebyshev-center or polyhedral graph theory literature cannot be excluded merely by unsuccessful searches.

## References
1. Mitsuhiro Miyazaki, *On the Gorenstein property of the Ehrhart ring of the stable set polytope of an h-perfect graph*, arXiv:2005.03259, first public version 2020-05-07, International Electronic Journal of Algebra 30 (2021), 269–284, DOI: 10.24330/ieja.969935. Definition 2.3 and Lemma 3.4.
2. *Clique number controls the exact Euclidean inradius of every perfect stable-set polytope*, 2026, publicly available mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-clique-number-controls-the-exact-euclidean-inradius-of-every-per--922955df9a90 .
3. Andreas Bärmann and Oskar Schneider, *Set characterizations and convex extensions for geometric convex-hull proofs*, 2021; study of odd-hole inequalities.
4. Václav Chvátal, *On Certain Polytopes Associated with Graphs*, Journal of Combinatorial Theory, Series B 18 (1975), 138–154; foundational stable-set polytope description.
