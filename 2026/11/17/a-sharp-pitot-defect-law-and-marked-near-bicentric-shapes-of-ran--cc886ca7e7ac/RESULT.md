# A sharp Pitot-defect law and marked near-bicentric shapes of random cyclic quadrilaterals

## Finding

Four independent arclength-uniform points on the unit circle, listed counterclockwise from a distinguished sampled point, form a strictly convex cyclic quadrilateral almost surely. Let \(a,b,c,d\) be its successive **central angular gaps**, adding to \(2\pi\); let \(\ell_1,\ldots,\ell_4\) be its successive Euclidean **side lengths**, with \(\ell_1=2\sin(a/2)\), etc. Define the signed Pitot defect
\[
\Delta=\ell_1+\ell_3-\ell_2-\ell_4.
\]
The classical Pitot converse says \(\Delta=0\) exactly when the convex quadrilateral admits an incircle touching all four sides. The following statements concern the **distance from that geometric condition**, not the classical equivalence itself.

Introduce
\[
u=\frac{a+c}{2},\quad v=\frac{a-c}{2},\quad w=\frac{b-d}{2},\quad
A=\cos(v/2),\quad B=\cos(w/2),\quad H=\sqrt{A^2+B^2},\quad
u_0(v,w)=2\arctan(B/A).
\]
Here \(u\) is written as \(\nu\) only to distinguish this angular coordinate from the four original arc endpoints. The exact global normal form is
\[
\boxed{\Delta=4H\sin\left(\frac{\nu-\nu_0}{2}\right).}
\]
For every \((v,w)\) with \(|v|+|w|<\pi\), exactly one admissible \(\nu\) is tangential, namely \(\nu_0\). Moreover every admissible cyclic quadrilateral satisfies
\[
\boxed{2|\nu-\nu_0|\le |\Delta|\le2\sqrt2|\nu-\nu_0|,}
\]
and both constants are best possible uniformly over nondegenerate quadrilaterals and their limits.

Write \(D=\{(v,w):|v|+|w|<\pi\}\). For \(0<t<4\), define
\[
h_t(v,w)=2\arcsin\!\left(\frac{t}{4H(v,w)}\right),
\]
and \([x]_+=\max\{x,0\}\). The **complete threshold probability** has the exact two-dimensional integral
\[
\boxed{\mathbb P(|\Delta|<t)=\frac{3}{2\pi^3}\int_D
\left[\min\{\pi-|w|,\nu_0+h_t\}-\max\{|v|,\nu_0-h_t\}\right]_+\,dv\,dw.}
\]
For \(t\ge4\) the probability equals one. As \(t\downarrow0\),
\[
\boxed{\mathbb P(|\Delta|<t)=C_{\rm P}\,t+o(t),\qquad
C_{\rm P}=\frac{3}{2\pi^3}\int_D\frac{dv\,dw}{\sqrt{\cos^2(v/2)+\cos^2(w/2)}}
=0.818543101136753\ldots.}
\]

There is also a **marked near-tangency law**. Given \(|\Delta|<t\), the triple \((v,w,\Delta/t)\) converges in **total variation** as \(t\downarrow0\) to \((V,W,Z)\), where \(Z\) is uniform on \((-1,1)\) and independent of \((V,W)\), whose density on \(D\) is
\[
\boxed{g(v,w)=\frac{1}{I H(v,w)},\qquad
I=\int_D H(v,w)^{-1}\,dv\,dw=16.919982579064538\ldots.}
\]
Thus conditioning on near-existence of an incircle biases the two gap-imbalance coordinates by the reciprocal transverse slope, while the normalized signed Pitot defect becomes uniform.

## Assumptions and scope

The circle has circumradius exactly one and four points are independent uniform in **angle**, equivalently in arclength. The distinguished point is one of the four independently sampled vertices, fixed before sorting the other three counterclockwise around it. This distinction gives a uniform Dirichlet law for the four circular gaps, unlike the end-gap of a sample sorted relative to a fixed external angular origin. Every strictly positive gap configuration gives a convex cyclic quadrilateral. Degenerate gap boundaries have probability zero; all densities and geometric uniqueness statements are for the open domains indicated.

The coordinate \(\nu\) ranges over \(|v|<\nu<\pi-|w|\) with \((v,w)\in D\). The signed defect depends on the distinguished vertex and flips sign after a one-vertex cyclic shift, but its absolute value and the near-bicentric event are invariant. The normalized shape law explicitly refers to the chosen distinguished cyclic ordering. For a circle of radius \(R>0\), side-length defects scale by \(R\), so replace \(t\) above by \(t/R\) to recover the probability for an unnormalized physical defect.

## Proof

**1. Sampling density and coordinates.** Conditional on a sampled vertex's angle, the other three relative angles are i.i.d. uniform on \([0,2\pi)\). Their ordered gaps satisfy
\[
(a,b,c,d)/(2\pi)\sim\operatorname{Dirichlet}(1,1,1,1).
\]
The density of \((a,b,c)\) is \(6/(2\pi)^3=3/(4\pi^3)\). The inverse coordinate transform is
\[
a=\nu+v,\quad c=\nu-v,\quad b=\pi-\nu+w,\quad d=\pi-\nu-w.
\]
Its absolute Jacobian is \(2\), hence \((\nu,v,w)\) has constant density \(3/(2\pi^3)\) on \(\{(v,w)\in D,\ |v|<\nu<\pi-|w|\}\). The diamond \(D\) comes from \(|v|<\pi-|w|\).

**2. Exact transverse normal form and the tangential locus.** Pairing the half-angle sines gives
\[
\ell_1+\ell_3=4\sin(\nu/2)\cos(v/2),\qquad
\ell_2+\ell_4=4\cos(\nu/2)\cos(w/2).
\]
Thus \(\Delta=4[A\sin(\nu/2)-B\cos(\nu/2)]\). Both \(A,B>0\) on \(D\); writing \(\nu_0=2\arctan(B/A)\) yields the boxed sine normal form. To see that the zero lies strictly inside the feasible interval, put \(x=|v|/2\) and \(y=|w|/2\), with \(x+y<\pi/2\). Then \(B/A>\tan x\) is equivalent to \(\cos y>\sin x\), and \(B/A<\cot y\) is equivalent to \(\cos x>\sin y\). Both hold strictly. Consequently \(|v|<\nu_0<\pi-|w|\). The normal form is strictly increasing in \(\nu\) on the feasible interval, giving a unique Pitot-zero configuration, which is bicentric by the classical converse.

**3. Quantitative stability.** Differentiate at fixed \((v,w)\):
\[
\frac{\partial\Delta}{\partial\nu}
=2\{A\cos(\nu/2)+B\sin(\nu/2)\}.
\]
Because \(|v|<\nu\) and \(|w|<\pi-\nu\), one has \(A>\cos(\nu/2)\) and \(B>\sin(\nu/2)\), implying \(\partial_\nu\Delta>2\). Conversely \(A,B\le1\) and \(\sin(\nu/2)+\cos(\nu/2)\le\sqrt2\), so \(\partial_\nu\Delta\le2\sqrt2\). Integrating between \(\nu\) and \(\nu_0\), whose whole interval is feasible, gives the global stability estimate. The upper constant is attained infinitesimally at \(v=w=0\), \(\nu=\nu_0=\pi/2\) (the square). The lower constant is approached along \(v=w\uparrow\pi/2\), \(\nu=\nu_0=\pi/2\), corresponding to admissible quadrilaterals with two vanishing gaps; therefore neither constant can be improved.

**4. Exact threshold.** On the feasible interval, \(|\nu-\nu_0|<\pi\), so the sine normal form yields \(|\Delta|<t\) precisely when \(|\nu-\nu_0|<2\arcsin(t/(4H))\) for \(0<t<4\). Here \(H\ge1\), because for \(x+y<\pi/2\) the identity \(\cos^2x+\cos^2y=1+\cos(x+y)\cos(x-y)\ge1\) applies. Intersecting this interval with \((|v|,\pi-|w|)\) gives the displayed clipped integration formula. The derivative estimate also gives \(|\Delta|\le4\) globally by the chord-length bound or directly from the pair sums; hence larger thresholds have probability one.

**5. Small-defect coefficient.** For each fixed point of \(D\) the zero \(\nu_0\) lies strictly inside the feasible interval. Therefore as \(t\downarrow0\) the integrand is eventually \(2h_t\), and \(2h_t/t\to1/H\). Since \(H\ge1\) and, for \(t\le1\), \(2h_t/t\le(4/\sqrt{15})\) is a uniform bound (an inessential bound can be replaced by any larger constant), dominated convergence over finite-area \(D\) gives the coefficient \(C_{\rm P}\). The numerical decimal is quadrature, not a closed-form claim.

**6. Total-variation marked limit.** On \(|\Delta|<t\), set \(z=\Delta/t\in(-1,1)\). The normal form gives
\[
\nu=\nu_0+2\arcsin\left(\frac{tz}{4H}\right),\qquad
\frac{d\nu}{dz}=\frac{t}{2H\sqrt{1-(tz/(4H))^2}}.
\]
For sufficiently small \(t\), this parametrizes the event exactly, subject to the feasible-interval indicator. Dividing the joint density by \(\mathbb P(|\Delta|<t)\) gives a density on \(D\times(-1,1)\) converging almost everywhere to \(1/(2I H(v,w))\). The factor in the Jacobian is bounded uniformly for \(0<t\le1\), since \(H\ge1\); the feasible indicator tends to one at each interior \((v,w)\). The limiting density integrates to one, so Scheffé's lemma gives convergence in total variation. Its product form proves independence and the uniform limit of \(z\).

## Verification

Run `python3 artifacts/check_bicentric.py` using only the Python 3 standard library. With fixed random seed it checks 16,000 Dirichlet quadruples against both the direct chord formula and the normal form, exact feasibility of the bicentric projection, the global stability inequalities, and the clipped threshold integral against independent Monte Carlo frequencies. A deterministic midpoint Riemann sum verifies the leading coefficient to the displayed numerical precision appropriate to its grid. An independent higher-precision two-dimensional integration gives \(I=16.91998257906453868083\ldots\) and \(C_{\rm P}=0.81854310113675320157\ldots\). These finite computations corroborate but do not replace the analytic proof, and the higher-precision decimal is not required to establish any theorem.

## Relationship to prior work

Pitot's side-sum criterion and its converse are classical: they characterize exact tangency, but neither give a metric transverse coordinate nor a random-near-tangency law. Josefsson's 2012 *Similar Metric Characterizations of Tangential and Extangential Quadrilaterals* treats exact tangency and excircle characterizations of arbitrary convex quadrilaterals; it does not compute the random cyclic Pitot-defect distribution. Finch's 2016 *Random Cyclic Quadrilaterals* analyzes side and angle distributions of circle-sampled quadrilaterals but not the alternating opposite-side-sum defect or its near-zero conditional shape. Izmestiev's 2014 work treats a projective porism for cyclic quadrilaterals, not this sampling law.

A related published analysis of bicentric Poncelet families [5] fixes both circle radii and parametrizes two incircle tangency chords. Its exact family formulas do not imply a signed Pitot-defect law over all cyclic quadrilaterals, whose inradii generally are undefined. Published computations of random cyclic-quadrilateral perimeter–area moments [6], a fixed-side-variance area stability law [8], and area laws conditional on diagonal angle [7] concern different observables and do not determine the distribution of \(\ell_1+\ell_3-\ell_2-\ell_4\). The claimed contribution is precisely the global transverse normal form and its sharp stability, the exact all-threshold Pitot-proximity probability, and the marked total-variation limit. No originality is claimed for Pitot's theorem, elementary Dirichlet gap sampling, chord identities, or a generic smooth coarea principle. Broader unlocated reformulations in older quadrilateral literature remain possible.

## Limitations

Only four independent angular-uniform samples from a single Euclidean circle are covered. The side-sum defect measures deviation from the Pitot condition; it is not asserted to equal Hausdorff distance, a Euclidean vertex displacement, an incircle-radius deficit, or a statistical estimator with finite-sample accuracy. The canonical projection keeps the two imbalance coordinates fixed and is not claimed optimal under other metrics. The decimal coefficient requires numerical integration; the rigorous result is its exact absolutely convergent integral. Historical priority is best knowledge only, not independent certification. In particular Beardon's 2021 treatment of the deterministic Pitot theorem was accessible only by abstract/extract, not its full paper.

## References

1. M. Josefsson, *Similar Metric Characterizations of Tangential and Extangential Quadrilaterals*, Forum Geometricorum 12 (2012), 63–77, original publication date 4 April 2012. Open-access article copy: https://dynamicmathematicslearning.com/similar-metrics-tangential-extangential-quads-josefsson-FG2012.pdf
2. S. R. Finch, *Random Cyclic Quadrilaterals*, arXiv:1610.00510 (first posted 3 October 2016). https://arxiv.org/abs/1610.00510
3. I. Izmestiev, *A porism for cyclic quadrilaterals, butterfly theorems, and hyperbolic geometry*, arXiv:1408.2247 (first posted 10 August 2014). https://arxiv.org/abs/1408.2247
4. A. F. Beardon, *Pitot's theorem, dynamic geometry and conics*, The Mathematical Gazette 105 (2021), 52–60, doi:10.1017/mag.2021.7. Full text not inspected. https://doi.org/10.1017/mag.2021.7
5. *Tangency-chord linearization of the bicentric Poncelet family*, published-finding corpus, 2026/9/20. https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-tangency-chord-linearization-bicentric-poncelet-family--b2160f03c98b
6. *Exact perimeter–area second moments of a random cyclic quadrilateral*, published-finding corpus, 2026/10/12. https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-exact-perimeter-area-second-moments-of-a-random-cyclic-quadrilat--1c13b772d78d
7. *Conditional area law for random cyclic quadrilaterals at a fixed diagonal angle*, published-finding corpus, 2026/10/25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-conditional-area-law-for-random-cyclic-quadrilaterals-at-a-fixed--e05b854129e9

8. *Sharp lower area profile and reverse stability for cyclic quadrilaterals*, published-finding corpus, 2026/9/21. https://github.com/published-finding corpus/2026/tree/main/2026/9/21/SCOPE-sharp-quadrilateral-area-profile-side-variance--d2b02c4fa49a
