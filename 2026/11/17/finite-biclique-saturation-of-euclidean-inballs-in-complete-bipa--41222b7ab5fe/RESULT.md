# Finite biclique saturation of Euclidean inballs in complete-bipartite forest polytopes

## Finding

Let \(2\le p\le q\) be integers and put \(G=K_{p,q}\). The **forest independence polytope** is
\[
\mathcal F_{p,q}=\operatorname{conv}\{\mathbf1_{E(F)}:F\text{ is a spanning forest of }G\}\subset\mathbb R^{pq}.
\]
The coordinates are labeled by the edges of \(G\), and distances use the *unweighted ambient Euclidean metric*, not the intrinsic metric of a spanning-tree face. Define
\[
f_p(b)=\frac{p+b-1}{pb+\sqrt{pb}},\qquad
B_p=2(p-1)(2p^2-2p+1),\qquad
T_{p,q}=\begin{cases}\{q\},&q<B_p,\\\{B_p-1,B_p\},&q\ge B_p.\end{cases}
\]
When \(q<B_p\), the integer \(q\) is at least \(p\), as assumed above. Set \(r_{p,q}=\min_{b\in T_{p,q}}f_p(b)\) and \(\mathcal B_{p,q}=\{b\in T_{p,q}:f_p(b)=r_{p,q}\}\). Then:

1. The maximum radius of an ambient Euclidean ball contained in \(\mathcal F_{p,q}\) is exactly \(r_{p,q}\), and its **unique** center is \(r_{p,q}\mathbf1_{pq}\).
2. For \((p,q)\ne(2,2)\), the facets touched by that ball are precisely the \(pq\) coordinate facets \(x_e=0\), together with the induced-biclique rank facets
\[
\sum_{e\in E(K_{p,S})}x_e\le p+|S|-1,
\qquad S\subseteq[q],\quad |S|\in\mathcal B_{p,q},
\]
where \(K_{p,S}\) uses the entire part of size \(p\). Their number is
\[
pq+\sum_{b\in\mathcal B_{p,q}}\binom qb.
\]
For \((p,q)=(2,2)\), there are nine contacting facets: four nonnegativity facets, four individual-edge upper facets, and the full four-edge rank facet.
3. For every fixed \(p\ge2\), the radius is **independent of \(q\) for all \(q\ge B_p\)**, although the dimension \(pq\) grows without bound. The determining biclique has at most \(B_p\) vertices in the larger part, with \(B_p=4p^3-8p^2+6p-2\).
4. In the first nontrivial strip \(p=2\), the cutoff is sharp and the formula simplifies to
\[
r_{2,q}=\begin{cases}
\displaystyle\frac{q+1}{2q+\sqrt{2q}},&2\le q\le9,\\[4pt]
\displaystyle\frac{11}{20+\sqrt{20}},&q\ge10.
\end{cases}
\]
For every \(q\ge10\), the *unique* active upper-facet cardinality is \(10\), so the number of tangent facets is exactly \(2q+\binom q{10}\). In particular, the insphere is eventually stationary in radius while the count of tangent facets grows polynomially of degree ten.

This result concerns **forest** polytopes, not the codimension-one spanning-tree polytope obtained by fixing the total edge count.

## Assumptions and scope

For a finite graph \(G=(V,E)\), a spanning forest means an acyclic subset of \(E\), with isolated vertices allowed. The standard graphic-matroid independence polytope is full-dimensional in \(\mathbb R^E\). The complete-bipartite coordinate incidence representation is fixed; arbitrary affine transformations do not preserve the claimed radii.

The inequalities of the forest polytope are \(x_e\ge0\) and
\[
x(E(U))\le |U|-1\qquad (U\subseteq V,\ E(U)\ne\varnothing),
\]
where \(E(U)\) is the set of edges whose endpoints both belong to \(U\). It suffices for the present graph to take \(U\) containing \(a\) vertices from the first part and \(b\) from the second, with \(1\le a\le p\), \(1\le b\le q\): its induced edge set is a complete biclique of size \(ab\), and its rank is \(a+b-1\). This is the established graphic-matroid rank description, not a new facet theorem.

## Proof

**1. Exact radius as a finite biclique minimum.** Let a ball of radius \(r\) have center \(z\). The group \(S_p\times S_q\) acts transitively on edge coordinates and preserves the polytope. The set of centers admitting radius \(r\) is convex (it is an intersection of inward-translated halfspaces), so averaging \(z\) produces another such center \(c\mathbf1_{pq}\). Each coordinate inequality forces \(c\ge r\). The rank inequality for a chosen \(K_{a,b}\), with Euclidean normal norm \(\sqrt{ab}\), forces
\[
ab c+r\sqrt{ab}\le a+b-1.
\]
As \(c\ge r\), necessarily
\[
r\le g(a,b):=\frac{a+b-1}{ab+\sqrt{ab}}
\qquad(1\le a\le p,\ 1\le b\le q).
\]
Conversely, if \(r\) is the minimum of these values, the ball centered at \(r\mathbf1\) satisfies every nonnegativity and rank inequality, hence is contained in \(\mathcal F_{p,q}\). Therefore the exact inradius is the minimum of \(g(a,b)\).

**2. All minimizing bicliques use the full smaller part.** The function \(g\) is symmetric. For any real \(b\ge2\), let \(t=\sqrt a\). Apart from a positive denominator, the derivative of \(g(t^2,b)\) with respect to \(t\) has sign
\[
t^2-2\sqrt b(b-1)t-(b-1),
\]
which is strictly negative for \(1\le t\le\sqrt b\). Thus \(g(a,b)\) strictly decreases as the smaller of its two arguments rises toward the larger one, except that the exceptional comparison \(g(1,1)=g(2,2)=1/2\) allows a tie when both sides are of size two. Further,
\[
g(k,k)=\frac{2k-1}{k(k+1)}
\]
is nonincreasing for integer \(k\ge1\), strictly so after \(k=2\). Given \(a\le p\), \(b\le q\), if \(b\ge p\) increase \(a\) to \(p\); if \(b<p\), first increase the smaller argument to the larger and then both to \(p\). These operations never increase \(g\). Consequently
\[
r_{p,q}=\min_{p\le b\le q}f_p(b).
\]
For \((p,q)\ne(2,2)\), equality among all biclique rank bounds can occur only when \(a=p\) and \(b\) minimizes this one-variable function. For \((2,2)\), the four singleton-edge bounds also tie.

**3. A uniform cubic cutoff.** With \(t=\sqrt b\), the sign of \(f_p'(b)\) is the sign of
\[
t^2-2\sqrt p(p-1)t-(p-1).
\]
Its unique positive zero occurs at \(b=b_p^*\), where
\[
b_p^*=\left(\sqrt p(p-1)+\sqrt{(p-1)(p^2-p+1)}\right)^2.
\]
Thus \(f_p\) strictly decreases up to \(b_p^*\) and increases thereafter. Write \(A=p^2-p+1/2\). Direct squaring and rationalization give
\[
B_p-b_p^*=\frac{p-1}{2\bigl(A+\sqrt{A^2-1/4}\bigr)}.
\]
For every integer \(p\ge2\), this lies strictly between \(0\) and \(1/4\). Hence
\[
B_p-1<b_p^*<B_p,
\]
and the minimizing integer in \([p,q]\) is \(q\) if \(q<B_p\), and otherwise belongs to \(\{B_p-1,B_p\}\). This proves the claimed two-term closed formula and finite saturation threshold; it does not presume which of the last two expressions wins in every order.

For \(p=2\) the threshold is \(B_2=10\) and \(b_2^*=5+2\sqrt6\in(9,10)\). The only remaining comparison is
\[
f_2(9)>f_2(10)
\iff 2+20\sqrt5>33\sqrt2,
\]
which holds (square the positive sides). The strict one-variable monotonicity proves that the unique minimizing index is \(\min(q,10)\). This establishes the explicit strip law.

**4. Uniqueness and all contacting facets.** Let \(r=r_{p,q}\) and choose any minimizing cardinality \(b\). At any center \(z\) of an inscribed radius-\(r\) ball, each coordinate facet gives \(z_e\ge r\). For every induced \(K_{p,S}\) with \(|S|=b\), the corresponding rank inequality, shifted inward by the norm of its normal, gives
\[
\sum_{e\in E(K_{p,S})}z_e\le p+b-1-r\sqrt{pb}=pb\,r.
\]
The left side consists of \(pb\) terms each at least \(r\), so every involved term equals \(r\). Each edge of \(K_{p,q}\) belongs to at least one such induced biclique. Thus \(z=r\mathbf1\), proving uniqueness.

At this center, a rank plane for \(K_{a,b}\) has distance exactly \(r\) if and only if \(g(a,b)=r\). A full-dimensional graphic-matroid independence polytope has as its upper facets the inequalities of indecomposable flats. The induced \(K_{a,b}\) is an indecomposable flat whenever \(a,b\ge2\), because its edges are connected through four-cycles; a single edge also gives an upper facet. Induced stars with more than one edge give redundant aggregate inequalities. Step 2 therefore identifies all upper contacting facets. Every coordinate facet contacts because \(z_e=r\), yielding the stated count and the exceptional nine contacts for \(K_{2,2}\).

## Verification

The standalone `verify.py` reconstructs all induced-biclique rank inequalities for twelve pairs \((p,q)\) with \(2\le p\le4\), \(p\le q\le6\), and independently solves the ambient inball linear program (with every biclique inequality, not merely the predicted active ones). It checks the unique uniform center, facet slack bounds and predicted radius against the numerical optimizer. Other loops compare the two-term cutoff and original two-variable finite minimum across multiple orders, verify the cubic cutoff against the continuous critical point, and check the exact index-10 strip behavior through \(q=44\). The completed script reports 3,133 grouped checks. The infinite claims follow from Steps 1–4, not from the tested finite cases.

Replay with `python3 verify.py` in a Python 3 environment with NumPy and SciPy.

## Relationship to prior work

Coons, Hollering and Chakrabarty Paul (arXiv:2611.09633, publicly posted 2026-11-06), Proposition 3.8, identify the indegree-one characteristic imset polytope with the **complete-graph** graphic-matroid forest polytope and give the established rank inequalities. Their Section 3 and preceding matroid facet theorem motivate the present metric question. The specific object here is the complete-*bipartite* forest independence polytope, and the new subject is its exact ambient insphere, local rank-facet contacts, and cubic saturation threshold.

A separate published result, *Sharp Euclidean inball phases of complete-bipartite spanning-tree polytopes*, treats the **spanning-tree base polytope** in its codimension-one affine hyperplane. Its projected-normal distances, nonunique-incenter regimes and asymptotic crossover do not determine the inball of the full-dimensional forest polytope. Another published result, *Sharp minimum-sphere bounds for matroid independence polytopes*, determines **minimum enclosing balls**; circumspheres do not imply the present largest inscribed-ball or biclique saturation formulas. These are related but mathematically distinct objects and extremal questions. No exhaustive bibliographic uniqueness claim is made.

## Limitations

The theorem is restricted to full-dimensional graphic-matroid independence polytopes of **unweighted** complete bipartite graphs and the ambient Euclidean metric. It does not determine the inball of weighted forests, arbitrary graphs, or their spanning-tree faces. The general \(p\) cutoff uses an exact two-value minimum; no universal tie-free preference between \(B_p-1\) and \(B_p\) is claimed beyond the fully resolved \(p=2\) strip. Finite linear programs are corroboration, not a substitute for the proof. An independent mathematical audit has not been performed, and earlier unindexed formulations may remain.

## References

1. J. I. Coons, B. Hollering, N. Chakrabarty Paul, *Polyhedral Geometry of Degree-Bounded Characteristic Imset Polytopes*, arXiv:2611.09633 (v1 2026-11-06), https://arxiv.org/abs/2611.09633. Section 3, especially Theorem 3.7 and Proposition 3.8.
2. J. Edmonds, *Matroids and the greedy algorithm*, Mathematical Programming **1** (1971), 127–136. Graphic-matroid rank inequalities (established input).
3. *Sharp Euclidean inball phases of complete-bipartite spanning-tree polytopes*, 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-euclidean-inball-phases-of-complete-bipartite-spanning-tre--40615d09964e.
4. *Sharp minimum-sphere bounds for matroid independence polytopes distinguish uniform density from arboricity two*, 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-minimum-sphere-bounds-for-matroid-independence-polytopes-d--8fea8c7015da.
