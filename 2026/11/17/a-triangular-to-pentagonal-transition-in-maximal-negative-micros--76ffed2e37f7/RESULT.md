# A triangular-to-pentagonal transition in maximal negative microscopic mass of Euclidean bipyramids

## Finding

Fix any integer \(n\ge3\). Let \(X_{n,u,v}\subset\mathbb R^3\) be the \(n+2\) distinct vertices of the right regular \(n\)-gonal bipyramid having an equatorial regular polygon of circumradius one in the plane \(z=0\) and apices at heights \(u>0\) and \(-v<0\). Equip this finite set with ordinary Euclidean chord distance. Its microscopic weighting is a uniquely defined signed measure of total mass one. Let \(N_n(u,v)\) denote the sum of the absolute values of its negative point masses.

Set
\[
 a_n=\frac{2}{n}\cot\left(\frac{\pi}{2n}\right),\qquad
 B(a)=\frac{a+2-2\sqrt2}{2(2\sqrt2-1-a)},\qquad
 C(a)=\frac{a^2-1}{3-a^2}.
\]
The exact sharp negative-mass law is
\[
 \boxed{\sup_{u,v>0} N_n(u,v)=\max\{B(a_n),C(a_n)\}.}
\]
For \(n=3,4\), \(B(a_n)>C(a_n)\). The supremum is **not attained** by any genuine bipyramid and is approached only when \((u,v)\to(0,1)\) or \((u,v)\to(1,0)\), up to interchanging the apices. For every \(n\ge5\), \(C(a_n)>B(a_n)\); the maximum **is attained uniquely** at the symmetric bipyramid
\[
 \boxed{u=v=\frac{a_n^2-1}{2a_n}.}
\]
In particular, optimal negative mass switches from a boundary-asymmetric regime to an attained, strictly symmetric regime between quadrilateral and pentagonal equators. Every vertex of every bipyramid under consideration is exposed, including every negative-mass vertex.

The complete point-weight formula is also explicit. Put
\[
 x=\sqrt{1+u^2}-u,\qquad y=\sqrt{1+v^2}-v,
 \qquad H=1+x^2+xy+y^2-a_n(x+y).
\]
The mass of each equatorial vertex, the upper apex, and the lower apex, respectively, equals
\[
 \boxed{\frac{(x+y)^2}{2nH},\quad
 \frac{1+y^2-a_n(x+y)}{2H},\quad
 \frac{1+x^2-a_n(x+y)}{2H}.}
\]
Here \(0<x,y<1\), \(1<a_n<4/\pi<\sqrt2\), and \(H>0\), so every equatorial mass is positive. In the attained regime, the two apices each have mass \((1-a_n^2)/(2(3-a_n^2))\). As \(n\to\infty\), the maximal negative mass tends to \((16/\pi^2-1)/(3-16/\pi^2)=0.4504724627\ldots\), and the optimal height tends to \((16-\pi^2)/(8\pi)\).

## Assumptions and scope

For a finite metric space \(X=\{z_1,\dots,z_m\}\), let \(D=(d(z_i,z_j))\), and for \(t>0\) let \(Z_t=(\exp(-td(z_i,z_j)))\). The microscopic weighting is the componentwise limit of \(Z_t^{-1}\mathbf1\) as \(t\downarrow0\), when it exists. By Roff and Willerton's strict-negative-type theorem, for distinct Euclidean points this limit exists, has total mass one, and is the unique vector \(w\) satisfying \(\mathbf1^Tw=1\) and \(Dw=\lambda\mathbf1\) for a scalar \(\lambda\). The negative-mass functional is \(N(w)=\sum_i\max\{0,-w_i\}\), not the total variation norm itself (which equals \(1+2N(w)\)). No probability positivity is assumed.

The result concerns all \(n\ge3\), all strictly positive finite \(u,v\), and the ambient Euclidean chord metric in three dimensions. Multiplying all coordinates by a common positive scale does not change microscopic weights; hence equatorial circumradius one is without loss for similarity-invariant statements. The optimization is only over the two apex heights for a fixed regular equator.

## Proof

**Distance gauging.** The sum of the \(n-1\) nonzero equatorial chord lengths from any equatorial vertex is \(A_n=2\cot(\pi/(2n))=na_n\). Let \(s=\sqrt{1+u^2}\), \(t=\sqrt{1+v^2}\), and \(L=u+v\). Cyclic symmetry and uniqueness imply that all equatorial weights coincide; call their individual mass \(w\), and call the upper and lower apex masses \(p,q\). The equations defining the microscopic gauging reduce exactly to
\[
 nw+p+q=1,\qquad
 A_nw+sp+tq=nsw+Lq=ntw+Lp.
\]
Substitute \(x=s-u\), \(y=t-v\). These lie in \((0,1)\) and invert as \(s=(1+x^2)/(2x)\), \(u=(1-x^2)/(2x)\), and analogously for \(t,v\). Solving the three linear equations gives the three displayed masses. Direct substitution verifies both equal-potential equations and total mass. In particular, writing \(z=(x+y)/2\) and \(d=(x-y)/2\),
\[
 H=1+3z^2+d^2-2a_nz\ge1-a_n^2/3>0.
\]
Strict negative type supplies uniqueness, so there are no hidden alternative solutions.

**The two-negative sector.** Since equatorial weights are positive, if both apex weights are negative then
\[
 N_n(u,v)=-(p+q)=\frac{2z^2}{1+3z^2+d^2-2a_nz}-1.
\]
For any fixed \(z>0\), removing \(d^2\) from the denominator can only increase this expression, strictly unless \(d=0\). The derivative of \(2z^2/(1+3z^2-2a_nz)\) has the sign of \(1-a_nz\), so its unique maximum for \(0<z<1\) occurs at \(z=1/a_n\). This yields \(N_n\le C(a_n)\), with equality exactly when \(x=y=1/a_n\). Inverting \(x,y\) gives the claimed common positive height. At that point both apex masses are strictly negative, so the bound is actually attained in the two-negative sector.

**The one-negative sector.** By symmetry it suffices to bound \(-p\). For fixed \(0<x\le1\), direct differentiation gives
\[
 \frac{\partial p}{\partial y}=\frac{x(2xy+y^2-1)}{2H^2}.
\]
Thus \(p\) is uniquely minimized over \(0<y\le1\) at \(y_*(x)=\sqrt{1+x^2}-x\). Along this minimizing curve, the derivative with respect to \(x\), multiplied by the strictly positive \(2H^2\), equals
\[
 \frac{(1+y_*^2)\bigl(a_n(1+y_*^2)-4y_*\bigr)}{4y_*^2}<0.
\]
Indeed \(\sqrt2-1\le y_*<1\), so \(4y_*/(1+y_*^2)\ge\sqrt2>a_n\). Hence the global minimum of \(p\) on the closed parameter square is uniquely at \(x=1,y=\sqrt2-1\), where \(-p=B(a_n)\). At this boundary point the other apex weight is positive, since its numerator is \(2-\sqrt2a_n>0\). The original domain has \(x,y<1\), so the bound on a single negative weight is strict for genuine bipyramids; nevertheless it is approached as \(u\downarrow0\), \(v\to1\). Thus every one-negative configuration satisfies \(N_n<B(a_n)\), and this bound is sharp as a supremum.

**Comparing the two regimes.** The average chord length \(a_n\) increases strictly with integer \(n\), because \(x\cot x\) strictly decreases as \(x\) increases over \((0,\pi/6]\). Its range is \(2/\sqrt3\le a_n<4/\pi\). Put \(F(a)=C(a)-B(a)\). Then
\[
 F'(a)=\frac{4a}{(3-a^2)^2}-\frac1{2(2\sqrt2-1-a)^2}>0
 \quad(2/\sqrt3\le a<4/\pi).
\]
For a fully explicit sign check, the first term is at least \(72/(25\sqrt3)\), while the second is at most \(1/[2(2\sqrt2-1-4/\pi)^2]\); the first lower bound exceeds the second upper bound. This strict comparison follows, for example, by the rational enclosures \(\sqrt2>707/500\), \(\sqrt3<1733/1000\), and \(\pi>157/50\). Direct exact substitution at \(a_4=(1+\sqrt2)/2\) yields \(F(a_4)<0\), whereas at \(a_5=(2/5)\sqrt{5+2\sqrt5}\) it yields \(F(a_5)>0\). Hence \(B(a_n)>C(a_n)\) precisely for \(n=3,4\), with the opposite strict inequality for \(n\ge5\). Combining the three possible signs of \(p,q\) proves the claimed global classification, uniqueness, and nonattainment assertions. Taking the limit \(a_n\to4/\pi\) proves the asymptotics.

**Exposedness.** A positive-height upper apex uniquely maximizes the vertical coordinate and the negative-height lower apex uniquely minimizes it. For each equatorial vertex, the horizontal radial functional pointing at that vertex uniquely maximizes over all the equatorial vertices and is zero at both apices. Therefore all \(n+2\) vertices are exposed for every \(u,v>0\).

## Verification

The standalone file `verify.py` checks symbolic normalization, both distance-gauging equations after the height substitution, the derivative identities, and the exact \(n=4,5\) comparison signs. It also checks the fully rational enclosure ensuring \(F'>0\), independently solves full Euclidean distance-matrix systems for \(n=3,\dots,20\) and seven different height pairs, and evaluates the negative-mass bound on deterministic two-parameter samples for several values of \(n\). Run `python verify.py` with Python 3, NumPy, SymPy and mpmath. In the actual run it passed 1,862 assertions. Numerical experiments do not establish infinitely many \(n\) or continuum sharpness; the proof above supplies those statements.

## Relationship to prior work

Roff and Willerton [1, especially Theorem 4.11] introduced microscopic weightings and proved existence and the gauging characterization for finite Euclidean subsets. The new question here is the **sharp maximal negative mass** of those weightings over the two genuinely geometric apex-height parameters of a regular bipyramid, including the nonattainment/attainment transition at \(n=5\). Kamiyama [2, Definition 2.6] studies different two-chunk cyclic distance arrays with constant intrachunk distances and specific cross-block patterns; neither an arbitrary regular polygonal equator with two unequally high apices nor this sharp optimization follows from that construction. The published record [3] identifies negative microscopic masses at exposed vertices of staggered planar polygons, but its two concentric, staggered vertex orbits and radius threshold are not an implication for the nonplanar two-apex extremal-mass problem. These distinctions concern implications, not merely title differences.

## Limitations

No assertion is made about general convex polyhedra, irregular equatorial polygons, larger collections of apex points, geodesic surface metrics, or fixed-volume optimization. The optimal boundary-asymmetric configuration for \(n=3,4\) is a limiting *degenerate* shape, not an attained genuine bipyramid. The relation to all historical magnitude calculations cannot be exhaustively certified by search, and no independent audit has been performed.

## References

[1] E. Roff and S. Willerton, *The microscopic weighting on a metric space*, arXiv:2607.05349 (first posted 2026-07-06; version 2 posted 2026-11-04), https://arxiv.org/html/2607.05349v2.

[2] T. Kamiyama, *Small-scale magnitude below one for cyclic two-chunk finite metric spaces*, arXiv:2606.00707 (first posted 2026-05-30), https://arxiv.org/html/2606.00707v1.

[3] *Negative microscopic weights at exposed vertices of staggered regular polygons*, published mathematical research record 2026/11/1/SCOPE-negative-microscopic-weights-at-exposed-vertices-of-staggered-re--9ce6bbdc7f59, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-negative-microscopic-weights-at-exposed-vertices-of-staggered-re--9ce6bbdc7f59.
