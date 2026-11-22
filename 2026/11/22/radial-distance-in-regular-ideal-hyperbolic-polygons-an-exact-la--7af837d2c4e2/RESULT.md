# Radial distance in regular ideal hyperbolic polygons: an exact law and a logarithmic many-side limit

## Finding

In the complete hyperbolic plane of curvature \(-1\), let \(P_n\) be a **regular ideal** \(n\)-gon, for each integer \(n\ge3\). All vertices lie on the ideal boundary and the finite hyperbolic area is \((n-2)\pi\). Write \(o_n\) for its unique center, choose \(X_n\) uniformly by hyperbolic area in \(P_n\), and put \(R_n=d_{\mathbb H}(o_n,X_n)\). Set
\[
\phi_n=\pi/n,\quad a_n=\cos\phi_n,\quad \rho_n=\operatorname{artanh}(a_n),\quad
B_n(t)=\arccos\!\frac{a_n}{\tanh t},\quad
G_n(t)=\arccos\!\frac{\cot\phi_n}{\sinh t}.
\]
The last two functions are used only when \(t>\rho_n\), so their arguments lie strictly between zero and one. The **complete** cumulative distribution is
\[
\boxed{
F_n(t)=\Pr(R_n\le t)=\begin{cases}
0,&t\le0,\\[3pt]
\dfrac{2(\cosh t-1)}{n-2},&0<t\le\rho_n,\\[7pt]
\dfrac{2\pi(\cosh t-1)-2n\{\cosh t B_n(t)-G_n(t)\}}{(n-2)\pi},&t>\rho_n.
\end{cases}}
\]
Its density is the explicit continuous function
\[
\boxed{f_n(t)=\frac{2\sinh t}{n-2}\left(1-\frac n\pi B_n(t)\right),\quad t>\rho_n,}
\]
and equals \(2\sinh t/(n-2)\) on \((0,\rho_n]\). The exact incircle mass is
\[
\boxed{\Pr(R_n\le\rho_n)=\frac{2(\csc(\pi/n)-1)}{n-2}.}
\]
The two relevant endpoint behaviors are sharp. As \(h\downarrow0\), the first transition has a nonanalytic exponent \(3/2\):
\[
\boxed{F_n(\rho_n+h)=\frac{2(\cosh(\rho_n+h)-1)}{n-2}
-\frac{4n\sqrt{2\cos(\pi/n)}}{3(n-2)\pi}h^{3/2}+O_n(h^{5/2}).}
\]
For every fixed \(n\), the unbounded radial tail is
\[
\boxed{\Pr(R_n>t)\sim\frac{2n\cot(\pi/n)}{(n-2)\pi}e^{-t},\qquad t\to\infty.}
\]

The **many-side law** is nondegenerate under logarithmic centering. With \(W_n=R_n-\log n\), \(b=2/\pi\), and \(c=\log b\), we have \(W_n\Rightarrow W\), where
\[
\boxed{\Pr(W\le s)=H(s)=\begin{cases}
e^s,&s\le c,\\[3pt]
e^s-\sqrt{e^{2s}-b^2}+b\arccos(be^{-s}),&s\ge c.
\end{cases}}
\]
In particular, the limiting probability of lying inside the incentered disk is \(2/\pi\). The limiting distribution has a sharp \(3/2\)-order transition at \(c\), and its left and right tails obey \(H(s)=e^s\) for \(s\le c\) and
\[
\boxed{1-H(s)\sim\frac{2}{\pi^2}e^{-s},\qquad s\to+\infty.}
\]
These finite-polygon and many-side statements form one radial-geometry finding, with a natural incircle/free-cusp transition.

## Assumptions and scope

The polygon is deterministic and invariant under a rotation of order \(n\); it has \(n\) distinct ideal vertices and geodesic sides. Sampling is with respect to *hyperbolic area*, not Euclidean area in a disk model and not uniform on the ideal vertices. All radial distances are geodesic distances from the center. The curvature is fixed at \(-1\); all formulas scale appropriately after a change of curvature units. The random variables in different dimensions \(n\) need not be coupled, and convergence in distribution refers to their scalar laws. Hyperbolic area is finite even though the polygons are unbounded.

## Proof

**1. Inradius and the angular intersection formula.** Divide \(P_n\) into \(2n\) congruent hyperbolic right triangles by joining the center to the ideal vertices and to the closest points of the sides. Their center angle is \(\phi_n=\pi/n\). In an ideal right triangle, the right-triangle sine law yields \(\tanh\rho_n=\cos\phi_n\), hence \(\rho_n=\operatorname{artanh}(\cos\phi_n)\). Equivalently, each outward side normal at the center is at hyperbolic distance \(\rho_n\) from its corresponding side.

Consider a ray of length \(t\) from the center making signed angle \(\theta\) with such a normal. The right-triangle relation at its intersection with the supporting geodesic side is \(\cos\theta=\tanh\rho_n/\tanh t\). Consequently, if \(t\le\rho_n\), the complete geodesic circle is inside \(P_n\). If \(t>\rho_n\), the forbidden rays centered on each side normal form an angular interval of half-width \(B_n(t)\). Since \(B_n(t)<\phi_n\) for finite \(t\), these \(n\) forbidden intervals are disjoint. The allowed angular measure is exactly \(2\pi-2n B_n(t)\). Hyperbolic polar area has element \(\sinh t\,dt\,d\theta\). Thus the radial density is
\[
 f_n(t)=\frac{(2\pi-2nB_n(t))\sinh t}{(n-2)\pi},\quad t>\rho_n,
\]
with the full-circle expression at smaller \(t\). The denominator is \((n-2)\pi\) by the ideal-polygon Gauss--Bonnet area formula. This geometric slice derivation proves nonnegativity and normalization, including that the total probability tends to one as \(t\to\infty\).

**2. Elementary integration of the radial density.** Define \(G_n(t)\) as above. Since \(\sinh\rho_n=\cot\phi_n\), both \(B_n\) and \(G_n\) vanish at \(\rho_n\). Direct differentiation of \(\cos B_n=a_n\coth t\) and \(\cos G_n=\cot\phi_n/\sinh t\) gives
\[
 G_n'(t)=\cosh t\,B_n'(t),\qquad t>\rho_n.
\]
It follows that
\[
 \int_{\rho_n}^{t}\!\sinh u\,B_n(u)\,du=\cosh t\,B_n(t)-G_n(t).
\]
Integrating the radial density from zero to \(t\) yields the boxed piecewise CDF, with continuity at the transition. Substituting \(\cosh\rho_n=\csc\phi_n\) gives the exact incircle probability.

**3. Transition coefficient and infinite tail.** For \(h\downarrow0\), Taylor expansion of \(\cos B_n(\rho_n+h)=a_n\coth(\rho_n+h)\) gives
\[
 B_n(\rho_n+h)=\sin\phi_n\sqrt{\frac{2}{\cos\phi_n}}\,h^{1/2}+O_n(h^{3/2}).
\]
The excluded angle contributes \(2n\int_{\rho_n}^{\rho_n+h}\sinh t B_n(t)\,dt\). Because \(\sinh\rho_n=\cot\phi_n\), its leading value is \((4n/3)\sqrt{2\cos\phi_n}\,h^{3/2}\), with error \(O_n(h^{5/2})\). Divide by the polygon area to obtain the transition expansion.

As \(t\to\infty\), \(\coth t=1+2e^{-2t}+O(e^{-4t})\), so
\[
 B_n(t)=\phi_n-2\cot\phi_n\,e^{-2t}+O_n(e^{-4t}).
\]
The surviving angle is therefore \(4n\cot\phi_n e^{-2t}+O_n(e^{-4t})\), which multiplied by \(\sinh t\) and divided by \((n-2)\pi\) gives \(f_n(t)=\frac{2n\cot\phi_n}{(n-2)\pi}e^{-t}+O_n(e^{-3t})\). Integrating the density from \(t\) to infinity gives the stated tail.

**4. The many-side logarithmic law.** The inradius satisfies
\[
\rho_n=\log n+\log(2/\pi)+O(n^{-2}).
\]
Put \(t_n=\log n+s\) for fixed real \(s\). When \(s<c\), the point is inside the inradius for all sufficiently large \(n\), and the disk part of the CDF gives \(F_n(t_n)\to e^s\). When \(s>c\), use
\[
 n B_n(t_n)\longrightarrow\sqrt{\pi^2-4e^{-2s}},\qquad
 G_n(t_n)\longrightarrow\arccos\left(\frac{2e^{-s}}\pi\right),\qquad
 \frac{2\cosh t_n}{n-2}\longrightarrow e^s.
\]
Substitution into the exact CDF yields \(F_n(t_n)\to H(s)\) in its second branch. At \(s=c\), either branch gives \(2/\pi\), using continuity and a squeeze argument. The candidate CDF is nondecreasing, continuous, tends to zero as \(s\to-\infty\), and tends to one as \(s\to\infty\). Therefore the pointwise convergence of CDFs proves \(W_n\Rightarrow W\). Differentiation for \(s>c\) yields
\[
 H'(s)=e^s\left(1-\sqrt{1-b^2e^{-2s}}\right),
\]
which matches the left derivative \(e^c=b\) at \(c\) and establishes the \(3/2\)-power cusp there by expansion. Finally, \(\sqrt{e^{2s}-b^2}=e^s-b^2e^{-s}/2+O(e^{-3s})\) and \(\arccos(be^{-s})=\pi/2-be^{-s}+O(e^{-3s})\) give \(1-H(s)\sim (b^2/2)e^{-s}=2e^{-s}/\pi^2\). The exact incircle mass tends to \(2/\pi\) by \(\sin(\pi/n)\sim\pi/n\).

## Verification

The standalone implementation `checks/regular_ideal_polygon.py` was executed successfully with Python 3 and mpmath. It independently integrates the *angular-slice density* and compares it with the antiderivative-based CDF at several thresholds for seven side counts \(n=3,4,5,7,12,32,256\), checks the incircle transition and its \(3/2\) coefficient, and tests convergence of \(F_n(\log n+s)\) to \(H(s)\) for six values of \(s\) and up to \(n=10000\). In a separate sampling diagnostic, it constructs \(150000\) independent area-uniform points in the ideal triangle with vertices \(0,1,\infty\) via its upper-half-plane area density and independently calculates hyperbolic distance from the incenter; five empirical probabilities agree with the analytical CDF within 0.013. Successful final message: `REGULAR_IDEAL_POLYGON_CHECKS_OK`. Finite sampling and quadrature support the result but do not establish the analytic identities or infinite limits; the proof above does.

Reproduction: install `mpmath` for Python 3 and run `python checks/regular_ideal_polygon.py` from the extracted artifact root. The pseudo-random seed is fixed.

## Relationship to prior work

Binbin Xu (2014) derives an Ambartzumian–Pleijel identity and distributions of **Liouville-geodesic chord lengths** in ideal hyperbolic polygons. A random complete geodesic and an area-uniform random point are different sampling spaces: Xu's chord-length distribution neither specifies a point's radial distance to a fixed center nor the logarithmically centered many-side law. Classical hyperbolic circle-area and ideal-triangle area/inradius formulas are used as known geometric ingredients, not claimed as discoveries.

*The logarithmic boundary-distance law and a renormalized shape invariant for ideal hyperbolic polygons* studies distance to the **nearest side** of a fixed ideal polygon. The present observable is instead distance to its **center** and has an unbounded support even for an ideal triangle, whereas nearest-side distance is bounded by the inradius. The earlier complete ideal-triangle nearest-side law and polygonal renormalized perimeter do not imply the stated radial CDF or its \(n\)-dependent limit.

*Exact incenter and phase laws for boundary-uniform ideal hyperbolic triangles* samples **three ideal vertices** independently and studies the resulting **random triangle's incenter**. Here the polygon is deterministic and the **point inside it** is area-random. The location laws are distinct and do not subsume one another. *A critical logarithmic-radius crossover for random hyperbolic cyclic-polygon area* concerns the **area of a random finite-radius hull**, not the radial distribution of an interior-uniform point in a deterministic ideal polygon. Comparisons were made at the level of the probability space and exact assertions, not merely titles.

The exact radial formula is a direct but nontrivial geometric pushforward; the singular incircle boundary and the explicit nondegenerate logarithmic many-side limit are the central new contributions proposed here. Historical priority over unindexed earlier geometry literature remains provisional.

## Limitations

Only geodesic regular ideal polygons in the curvature-\(-1\) hyperbolic plane and area-uniform interior points are covered. The finite-\(n\) exponential tail and the many-side limit have different orders of limits and cannot be interchanged without a separate uniform argument. The proof does not address arbitrary nonregular ideal polygons, random polygons, fluctuations of empirical quantiles, or finite-sample estimation. Independent mathematical audit and exhaustive historical priority verification have not been conducted.

## References

1. B. Xu, *On the Ambartzumian-Pleijel identity in hyperbolic geometry*, arXiv:1410.4052 (first submitted 2014-10-15), https://arxiv.org/abs/1410.4052 . Relevant: distribution of Liouville-geodesic intersection lengths with ideal polygons.
2. *The logarithmic boundary-distance law and a renormalized shape invariant for ideal hyperbolic polygons*, public research record, 2026-11-08, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-the-logarithmic-boundary-distance-law-and-a-renormalized-shape-i--1d7379fbdbb6/RESULT.md . Relevant: exact fixed-polygon nearest-side clearance distribution.
3. *Exact incenter and phase laws for boundary-uniform ideal hyperbolic triangles*, public research record, 2026-11-17, https://github.com/published-finding corpus/2026/blob/main/2026/11/17/SCOPE-exact-incenter-and-phase-laws-for-boundary-uniform-ideal-hyperbo--1559b103bd4b/RESULT.md . Relevant: different boundary-vertex sampling model.
4. *A critical logarithmic-radius crossover for random hyperbolic cyclic-polygon area*, public research record, 2026-11-17, https://github.com/published-finding corpus/2026/blob/main/2026/11/17/SCOPE-a-critical-logarithmic-radius-crossover-for-random-hyperbolic-cy--a2dad3e05c2a/RESULT.md . Relevant: an unrelated log-scale transition for area of random finite-radius hulls.
5. *The circumference and area of hyperbolic circles*, University of Glasgow mathematical notes, https://www.maths.gla.ac.uk/wws/cabripages/hyperbolic/circleformulae.html . Relevant: the classical hyperbolic disk area formula.
