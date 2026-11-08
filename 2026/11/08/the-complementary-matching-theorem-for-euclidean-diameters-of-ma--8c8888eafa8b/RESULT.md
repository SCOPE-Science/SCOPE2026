# The complementary matching theorem for Euclidean diameters of Marion central polytopes

## Finding
For every integer \(N\ge2\), consider the canonical regular-simplex realization
\[
P_N=\left\{x\in\mathbb R_{\ge0}^N:\ \sum_{i=1}^N x_i=1,\quad x_i\le2x_j\ \text{for all }i,j\right\},
\]
with the metric induced from the usual Euclidean metric on \(\mathbb R^N\). Its vertices are precisely
\[
v_S=\frac{\mathbf1+\mathbf1_S}{N+|S|},\qquad \varnothing\ne S\subsetneq[N].
\]
Its squared Euclidean diameter is
\[
\boxed{\operatorname{diam}_2(P_N)^2=\begin{cases}
\dfrac4{9N},&N\text{ even},\\[2mm]
\dfrac{36N(N^2-1)}{(9N^2-1)^2},&N\text{ odd}.
\end{cases}}
\]
Every unordered diametral pair is \(\{v_S,v_{[N]\setminus S}\}\) for a partition into two maximally balanced, nonempty pieces:
\[
\{|S|,N-|S|\}=\{\lfloor N/2\rfloor,\lceil N/2\rceil\}.
\]
There are exactly \(\tfrac12\binom N{N/2}\) unordered diametral pairs for even \(N\), and \(\binom N{(N-1)/2}\) for odd \(N\). No other pair of points in the polytope attains the diameter. Hence its vertex diameter graph is a matching on its middle two cardinality layers, with all other vertices isolated. In odd \(N\), the squared diameter is strictly below the universal continuous upper envelope \(4/(9N)\).

## Assumptions and scope
The trisection construction is formed inside the regular \((N-1)\)-simplex with vertices \(e_1,\dots,e_N\), whose side length is \(\sqrt2\). Its central region is the intersection of all halfspaces \(x_i\le2x_j\) in the affine hyperplane \(\sum_i x_i=1\). The metric is **not** an arbitrary affine-invariant metric on a general simplex: the theorem uses this regular realization. For a regular simplex of side length \(L\), both formulas for squared diameter must be multiplied by \(L^2/2\). Nothing here asserts the same diameter for arbitrary nonregular simplices.

A diametral pair means any pair of points in the entire convex body, not just of its vertices. The graph has all polytope vertices as nodes and joins two nodes when their Euclidean distance equals the diameter of the whole polytope. Every combinatorial count refers to distinct unordered geometric pairs.

## Proof
**1. Vertex classification.** The ratio constraints force all coordinates positive. A vertex must have at least one tight inequality, since otherwise it is interior relative to \(\sum_i x_i=1\). Write \(m=\min_i x_i\), \(M=\max_i x_i\). Tightness implies \(M=2m\), and the tight equalities involve only coordinates attaining \(m\) or \(M\). If any coordinate lies strictly between these values, the active equalities leave at least one positive-dimensional affine freedom (one common lower value and at least one unconstrained middle coordinate, subject to one sum constraint), so the point is not a vertex. If the low and high classes are both nonempty and exhaust all \(N\) coordinates, the active complete bipartite family \(x_i=2x_j\) fixes all coordinates once their sum is fixed; this point is a vertex. Solving gives \(v_S\) as displayed, with \(S\) the high-coordinate class.

**2. Pair distances and uncrossing.** For \(k=|S|\), \(l=|T|\), \(j=|S\cap T|\), a direct inner-product calculation gives
\[
D_N(k,l,j):=\|v_S-v_T\|_2^2=
\frac{N+3k}{(N+k)^2}+\frac{N+3l}{(N+l)^2}
-\frac{2(N+k+l+j)}{(N+k)(N+l)}.
\]
For fixed \(k,l\), this decreases strictly with \(j\). The minimum possible overlap is \(j_0=\max(0,k+l-N)\), and that overlap is always attainable. Thus every diametral vertex pair has overlap \(j_0\).

**3. Exact two-chamber optimization.** Treat \(k,l\) temporarily as real numbers strictly between zero and \(N\). Put \(t=(k+l)/2\) and \(u=(k-l)/2\). Substitution of the minimal overlap into the formula above yields
\[
D_{\le}(t,u)=\frac{2\{t(N+t)^2-(4N+t)u^2\}}{\{(N+t)^2-u^2\}^2},\qquad 2t\le N,
\]
and
\[
D_{\ge}(t,u)=\frac{2\{(N-t)(N+t)^2-(5N-t)u^2\}}{\{(N+t)^2-u^2\}^2},\qquad 2t\ge N.
\]
The restrictions from positive nontrivial subset sizes ensure the denominators are positive. Each expression is strictly decreasing in \(z=u^2\): after removing the common positive factor \(2/((N+t)^2-z)^3\), its derivative numerator equals
\[
((N+t)^2)(t-4N)-(4N+t)z<0
\]
in the first chamber, and
\[
-((N+t)^2)(3N+t)-(5N-t)z<0
\]
in the second. Consequently the balanced real choice \(u=0\) is the unique maximum for each fixed sum \(k+l\). The resulting upper-envelope functions are
\[
F_{\le}(t)=\frac{2t}{(N+t)^2},\quad(t\le N/2),
\qquad F_{\ge}(t)=\frac{2(N-t)}{(N+t)^2},\quad(t\ge N/2).
\]
The first increases strictly with \(t\) on this range, and the second decreases strictly. Their common maximum is \(4/(9N)\), attained only when \(k=l=N/2\) over real parameters. This pair of integer sizes is feasible if and only if \(N\) is even. In that case \(j_0=0\), so \(T=[N]\setminus S\), and both the formula and equality classification follow.

**4. Odd integer dimensions.** If \(N\) is odd, the only closest-to-balanced integer sizes on the boundary \(k+l=N\) are \(k=(N-1)/2\), \(l=(N+1)/2\) in either order. Their squared distance, with \(j=0\), is
\[
D_*=\frac{36N(N^2-1)}{(9N^2-1)^2}.
\]
All pairs with \(k+l\le N-1\) satisfy the strict bound
\[
D_N(k,l,j)\le F_{\le}((N-1)/2)=\frac{4(N-1)}{(3N-1)^2}<D_*,
\]
because the ratio of the proposed value to this upper bound is
\[
\frac{D_*}{4(N-1)/(3N-1)^2}=\frac{9N(N+1)}{(3N+1)^2}>1.
\]
All pairs with \(k+l\ge N+1\) are bounded by \(F_{\ge}((N+1)/2)=4(N-1)/(3N+1)^2\), which is even smaller. For \(k+l=N\), the strict decrease in \(u^2\) leaves exactly the two adjacent sizes above. This proves both sharpness and all equality cases for odd \(N\).

**5. Passing from vertices to the whole convex body.** For distinct points \(a,b\) and any fixed \(y\), strict convexity of squared Euclidean distance gives
\[
\|\lambda a+(1-\lambda)b-y\|_2^2
=\lambda\|a-y\|_2^2+(1-\lambda)\|b-y\|_2^2
-\lambda(1-\lambda)\|a-b\|_2^2,
\]
strictly below the maximum of the endpoint distances when \(0<\lambda<1\). Every nonvertex of a polytope is a nontrivial convex combination of vertices; therefore no nonvertex can occur in a diametral pair. The classification of all diametral pairs is now complete. Complements occur in unique pairs, which yields the matching graph and the stated counts.

## Verification
The independent finite verifier `verify.py` uses rational arithmetic from Python's standard library. It evaluates all feasible intersection-cardinality orbits of vertex pairs for every \(2\le N\le50\), checks the exact predicted maximum and all equality orbit types, and separately enumerates every pair of distinct vertices for \(2\le N\le9\), computing squared distances directly from coordinate vectors. The verifier completed with 506298 assertions. These finite checks are supplementary evidence; the above continuous two-chamber inequalities and the odd-integer comparison prove the theorem for unbounded \(N\).

Run with `python3 verify.py` from the directory containing this file. The statement concerns the canonical regular-simplex realization and not arbitrary affine images.

## Relationship to prior work
Kazakov (2026, arXiv:2606.02087, Sections 2–4 and Appendices A–C) defined the trisection central polytope, proved its affine-invariant volume ratio, and described its two-level vertices and face structure. The present proof rederives the vertex representation and determines instead the complete **metric diameter graph** of the canonical regular realization, including sharp odd–even formulas and the fact that diameter edges form a matching. Neither the source's volume formula nor its two-level vertex enumeration alone implies the global distance maximization or the equality classification.

The related ratio-bounded family for arbitrary ratio \(c>1\) has previously been studied through polar volume and Santaló volume products. Those invariants do not determine the diameter, and the present theorem does not claim new volume formulas. General results on graph diameter of polytopes are distinct: they measure shortest paths in the one-skeleton rather than Euclidean distances between arbitrary points.

## Limitations
The exact matching statement is proved only for the edge-*trisection* ratio \(2\), not all other cutting ratios. The canonical Euclidean metric matters; an arbitrary original simplex need not have the displayed diameter. The historical-novelty conclusion is provisional, as equivalent formulations in the literature on bounded-ratio probability vectors may not be indexed in the sources searched. No independent external mathematical audit or formal proof verification is claimed.

## References
- Yu. V. Kazakov, *Generalization of Marion's Theorem: Volumes of Central Polytopes Obtained by Trisecting the Edges of Simplices*, arXiv:2606.02087v1 (first public June 1, 2026), https://arxiv.org/abs/2606.02087 .
- W. Marion, *The hexagon theorem*, College Mathematics Journal 24 (1993), 218–221 (historical planar antecedent).
- H. Narayanan, R. Shah, N. Srivastava, *A Spectral Approach to Polytope Diameter*, ITCS 2022, doi:10.4230/LIPIcs.ITCS.2022.108 (graph-diameter context only, not an equivalent Euclidean theorem).
