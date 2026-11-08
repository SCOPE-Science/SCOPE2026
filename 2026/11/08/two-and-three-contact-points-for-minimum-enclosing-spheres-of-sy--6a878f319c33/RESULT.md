# Two and three contact points for minimum enclosing spheres of symmetric moment-curve hulls

## Finding

Let \(d\ge2\) be an integer and \(a>0\). Write
\[
\gamma_d(t)=(t,t^2,\ldots,t^d)\in\mathbb R^d,
\qquad -a\le t\le a.
\]
For **every** compact parameter set \(T\subseteq[-a,a]\) containing \(-a,0,a\), let \(P_d(T)=\operatorname{conv}\{\gamma_d(t):t\in T\}\). The same formulas hold for the full convex hull \(P_d([-a,a])\). Distances are the unweighted ambient Euclidean distances in these displayed coordinates.

Let \(M=a^2\), let \(E\in\mathbb R^d\) have even coordinates \(E_{2j}=a^{2j}\) and all odd coordinates zero, and set
\[
A=\|E\|^2=\sum_{j=1}^{\lfloor d/2\rfloor}M^{2j},\qquad
S=\sum_{j=1}^{\lceil d/2\rceil}M^{2j-1}.
\]
For odd \(d\), the **unique** minimum enclosing ball is
\[
\boxed{c=E,\qquad R^2=S.}
\]
It meets the hull exactly at \(\gamma_d(-a)\) and \(\gamma_d(a)\), regardless of the intermediate parameters.

For even \(d=2k\), the unique minimum enclosing ball has the following sharp two-regime center and radius:
\[
\boxed{
(c,R^2)=
\begin{cases}
(E,S),&0<a\le1,\\[2mm]
\bigl(\lambda E,\lambda^2 A\bigr),&a>1,\quad
\lambda=\dfrac{M+1}{2M}.
\end{cases}}
\]
For \(0<a<1\), precisely the two endpoint curve points contact. At \(a=1\), precisely the endpoints and the point \(\gamma_d(0)=0\) contact, even though the same center formula \(c=E\) still applies. For \(a>1\), precisely these same three points contact. **Every other point of the full curve, and hence every other point of either convex hull, lies strictly inside the ball.**

Thus adding arbitrarily many interior-parameter vertices to a symmetric cyclic polytope leaves its unique enclosing ball completely unchanged. The metric contact number is at most three in every dimension. In the canonical integer realization with \(T=\{-m,\dots,m\}\) and \(m\ge d\), odd dimensions have two contacts and even dimensions three.

## Assumptions and scope

The theorem is for polynomial moment-curve coordinates \(\gamma_d(t)\) exactly as written. Changing the scale of \(t\) changes the relative coordinate weights nonuniformly, so the transition at \(a=1\) is meaningful in this fixed realization. Replacing this curve by a trigonometric or normalized spherical moment curve, or applying an arbitrary nonorthogonal affine map, changes the metric problem. No assumption of equally spaced parameters, integrality, or full dimension is needed. When \(T\) has at least \(d+1\) distinct values, \(P_d(T)\) is a full-dimensional cyclic \(d\)-polytope by the Vandermonde determinant. For all compact \(T\), the hull is compact.

A contact is a point of the convex hull whose Euclidean distance to the stated center equals \(R\). The claimed contact counts are numbers of distinct points, not just of indexing parameters.

## Proof

**1. Symmetry and the endpoint geometry.** Let \(p_\pm=\gamma_d(\pm a)\). The diagonal reflection changing signs of odd coordinates maps \(p_+\) to \(p_-\). Their midpoint is precisely \(E=(p_++p_-)/2\). Their half-difference \(O=(p_+-p_-)/2\) is supported on odd coordinates. Thus \(E\perp O\) and \(\|O\|^2=S\). Every ball containing \(p_-\) and \(p_+\) has radius at least \(\sqrt S\). The unique ball of this minimum radius for those two points is centered at \(E\).

Put \(u=t^2\) and \(x=u/M\in[0,1]\). The identities below are exact for every real \(t\) with \(|t|\le a\), not only for finitely many sampled parameters.

**2. Even dimension and \(M\le1\).** For \(d=2k\), the squared distance to \(E\) is
\[
\|\gamma_d(t)-E\|^2
=\sum_{j=1}^{k}
\left[M^{2j}(1-x^j)^2+M^{2j-1}x^{2j-1}\right].
\]
For every \(0\le x\le1\) and integer \(j\ge1\),
\[
(1-x^j)^2\le1-x^{2j-1};
\]
indeed, after subtracting the left side, the right side equals \(x^j(2-x^j-x^{j-1})\ge0\). Since \(M\le1\), each bracket in the squared distance is at most \(M^{2j-1}\). Summing gives \(\|\gamma_d(t)-E\|^2\le S\), so the endpoint-diameter lower bound is attained. When \(0<x<1\), the inequality is strict; at \(x=0\) there is equality exactly when \(M=1\). This proves the center, radius, and curve contacts for \(a\le1\).

**3. Even dimension and \(M>1\).** Let \(\lambda=(M+1)/(2M)\in(1/2,1)\) and \(c=\lambda E\). For \(j=1,\ldots,k\), exact expansion gives
\[
\begin{aligned}
\lambda^2 A-\|\gamma_d(t)-c\|^2
&=\sum_{j=1}^{k}M^{2j}x^j
\left(1+\frac1M-x^j-\frac{x^{j-1}}{M}\right).
\end{aligned}
\]
Every summand is nonnegative on \([0,1]\), and every summand is strictly positive when \(0<x<1\). Equality holds exactly for \(x=0\) or \(x=1\); thus the only curve contacts are \(0,p_-,p_+\). Furthermore,
\[
c=(1-\lambda)\,0+\frac{\lambda}{2}p_-+\frac{\lambda}{2}p_+,
\]
with strictly positive weights, and all three displayed contact points have squared distance \(\lambda^2A\). For an arbitrary center \(z\), the weighted average of the squared distances from \(z\) to these three contacts is \(\lambda^2A+\|z-c\|^2\). Consequently every enclosing ball has radius squared at least \(\lambda^2A\), with strict inequality if its center is not \(c\). Thus the asserted ball is minimal and unique.

**4. Odd dimension.** Write \(d=2k+1\), with \(k\ge1\). The squared distance to \(E\) is
\[
\|\gamma_d(t)-E\|^2
=\sum_{j=1}^k M^{2j}(1-x^j)^2
+\sum_{j=0}^k M^{2j+1}x^{2j+1}.
\]
If \(M\le1\), pair the even-power term indexed \(j\) with the *preceding* odd-power term \(M^{2j-1}x^{2j-1}\). The inequality of Step 2 makes each such pair at most \(M^{2j-1}\). The remaining highest odd-power term satisfies \(M^{2k+1}x^{2k+1}\le M^{2k+1}\), strictly when \(x<1\).

If \(M\ge1\), pair that same even-power term instead with the *following* odd-power term \(M^{2j+1}x^{2j+1}\). Now
\[
(1-x^j)^2+x^{2j+1}\le1,
\]
because \(x^{2j+1}\le x^j\) and \((1-x^j)^2+x^j\le1\). Therefore each pair is at most \(M^{2j+1}\). The remaining first odd-power term is \(Mx\le M\), strictly for \(x<1\). Either grouping yields \(\|\gamma_d(t)-E\|^2\le S\), with equality only at \(|t|=a\). The endpoint-diameter lower bound from Step 1 again proves the unique optimum.

**5. Passing from the curve to the hull.** In all cases, the curve is contained in the stated closed ball. Convexity contains its entire convex hull. Conversely, every hull contains the active contact points used in Steps 1 or 3, so no smaller enclosing ball is possible. Strict convexity of the squared Euclidean norm ensures that a nontrivial convex combination of two distinct ball points lies strictly inside; hence no convex-hull point other than a displayed curve contact can lie on the sphere. This completes the proof.

## Verification

The self-contained standard-library script `VERIFY.py` performs exact rational checks in dimensions \(2\le d\le18\), using eight rational positive endpoint parameters on both sides of the transition and a symmetric rational grid of 61 curve parameters in each case. It checks the formula, all alleged and excluded curve contacts, endpoint orthogonality, and the explicit positive barycenter certificate. It reports 136 parameter cases and 17,308 rational assertions. These checks are supplementary: Steps 1–5 prove the claim for every permitted real parameter and every compact index set.

For example, at \(d=4\), \(a=2\), the center is \((0,5/2,0,10)\), the squared radius is \(425/4\), and the only curve contacts are \(\gamma_4(-2),\gamma_4(0),\gamma_4(2)\). For \(d=3\), \(a=2\), the center is \((0,4,0)\) and squared radius \(68\), with only endpoint contacts.

## Relationship to prior work

Konoike's 2026 work treats the Ehrhart polynomials of cyclic polytopes with integer moment-curve parameters through an average of zonotope Ehrhart polynomials; it motivates asking about the geometry of this canonical embedding. The new result concerns **Euclidean minimum enclosing balls**, a metric datum not given by the reported Ehrhart averaging identity. The standard cyclic-polytope theory and Gale evenness criterion describe combinatorics, not this exact metric contact transition. The classical algorithm of Elzinga and Hearn finds enclosing spheres of polyhedra algorithmically but is not a parametric formula for this family. Spherical realizations of cyclic polytopes are metrically different embeddings and do not imply the asserted ball for polynomial coordinates.

Targeted record and literature searches for equivalent smallest-enclosing-ball formulations produced no identified coverage; this is **not** a proof of worldwide novelty. The full text of Konoike's most directly related manuscript was not obtainable through the available routes; a secondary exposition of its formulas and its abstract were inspected. This limits the historical-priority assessment, even though the stated mathematical proof stands independently.

## Limitations

The theorem uses the specified Euclidean coordinate embedding, symmetric endpoint range, and a parameter set containing the midpoint parameter zero. It does not claim the same formulas for arbitrary asymmetric parameter sets or affine images. Priority is provisional pending wider/full-text literature inspection. The finite exact tests do not certify an infinite theorem by themselves; the written inequalities and contact certificates do.

## References

- M. Konoike, *Ehrhart polynomials of cyclic polytopes as averages of zonotope Ehrhart polynomials*, arXiv:2609.28417, first public September 23, 2026, https://arxiv.org/abs/2609.28417 .
- E. W. Weisstein, *Cyclic Polytope*, MathWorld, https://mathworld.wolfram.com/CyclicPolytope.html (accessed November 7, 2026 UTC).
- J. Elzinga and D. W. Hearn, *The minimum sphere covering a convex polyhedron*, Naval Research Logistics 21 (1974), 715–718, https://doi.org/10.1002/nav.3800210414 .
- *Literature Review: Ehrhart polynomials of cyclic polytopes as averages of zonotope Ehrhart polynomials*, secondary methodological synopsis, https://www.themoonlight.io/en/review/ehrhart-polynomials-of-cyclic-polytopes-as-averages-of-zonotope-ehrhart-polynomials (accessed November 7, 2026 UTC).
