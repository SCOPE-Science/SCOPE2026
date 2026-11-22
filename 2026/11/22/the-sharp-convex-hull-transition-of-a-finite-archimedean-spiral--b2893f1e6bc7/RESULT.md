# The sharp convex-hull transition of a finite Archimedean spiral

## Finding

For \(T>0\), set \(z(t)=t e^{it}\), \(0\le t\le T\), and let \(K_T\) be the closed Euclidean convex hull of this curve. There is a sharp transition at \(T=\pi\):

* For \(0<T\le\pi\), every point of the spiral is on the boundary, and the boundary closes with the radial chord from \(z(T)\) to \(0\).
* For \(T>\pi\), there is a unique \(u=u(T)\in(\max\{0,T-2\pi\},T-\pi)\) satisfying
\[
F_T(u)=T[\sin(T-u)-u\cos(T-u)]+u^2=0.
\]
The entire boundary is the spiral arc \(z([u,T])\) and a single segment from \(z(T)\) back to \(z(u)\), tangent to the spiral at \(z(u)\). No earlier winding is exposed. The exposed angular span lies strictly between \(\pi\) and \(2\pi\).

Write \(\ell(t)=\tfrac12[t\sqrt{1+t^2}+\operatorname{arsinh}(t)]\). The exact area \(A(T)\) and perimeter \(P(T)\) are
\[
(A,P)=\left(\frac{T^3}{6},\ell(T)+T\right),\qquad 0<T\le\pi,
\]
and for \(T>\pi\), with \(u=u(T)\),
\[
A(T)=\frac{T^3-u^3}{6}+\frac{Tu}{2}\sin(u-T),
\quad
P(T)=\ell(T)-\ell(u)+\sqrt{T^2+u^2-2Tu\cos(T-u)}.
\]
At the onset \(T=\pi+\delta\), as \(\delta\downarrow0\),
\[
u(T)=\frac{\delta}{2}+O(\delta^2),\quad
A(T)-\frac{T^3}{6}=\frac{\pi}{8}\delta^2+O(\delta^3),\quad
P(T)-[\ell(T)+T]=-\frac1{12}\delta^3+O(\delta^4).
\]
For long arcs \(T\to\infty\), put \(\epsilon(T)=2\pi-[T-u(T)]\). Then
\[
\epsilon(T)=2\sqrt{\frac\pi T}+O(T^{-3/2}),
\]
\[
A(T)=\pi T^2-2\pi^2T+\frac{4\pi^{3/2}}3\sqrt T+O(1),
\qquad
P(T)=2\pi T-2\pi^2+\frac{8\pi^{3/2}}{3\sqrt T}+O(T^{-1}).
\]
These formulas scale in the expected way for \(z_b(t)=bt e^{it}\): areas acquire a factor \(b^2\), perimeters a factor \(b\), and the contact parameters are unchanged.

## Assumptions and scope

The plane is Euclidean; \(T\) is any finite positive real number. \(K_T=\operatorname{conv}\{(t\cos t,t\sin t):0\le t\le T\}\), a compact full-dimensional planar convex body. The area is ordinary two-dimensional Lebesgue measure and perimeter is the length of its convex boundary. The contact at \(T=\pi\) is the initial point \(0\), which has a well-defined one-sided tangent. The \(O\)-constants at each displayed limit are absolute in the unit-scale normalization. The radial sector area \(T^3/6\) is used for comparison only at the first transition; it is not asserted to be the area of a simple region after multiple revolutions.

## Proof

**1. Curvature and support maxima.** The curve is regular, with \(z'(t)=(1+it)e^{it}\) and \(\Im(\overline{z'(t)}z''(t))=t^2+2>0\). Its outward normal angle is \(\nu(t)=t+\arctan t-\pi/2\), strictly increasing. The support of \(z(t)\) in the normal \(n(t)=e^{i\nu(t)}\) is \(q(t)=t^2/\sqrt{1+t^2}\), strictly increasing for \(t>0\). At any fixed direction, every interior local maximum of the support is attained at a parameter with normal angle congruent to that direction modulo \(2\pi\). Among such local maxima the latest parameter is largest because \(q\) increases. The opposite normal cannot support at an interior smooth point, by positive curvature.

**2. Candidate contact and uniqueness.** With \(\phi=T-t\), the support excess of \(z(t)\) over the terminal point \(z(T)\), multiplied by \(\sqrt{1+t^2}\), is exactly
\[
F_T(t)=t^2(1-\cos\phi)+t(\sin\phi-\phi\cos\phi)+\phi\sin\phi.
\]
All three terms are positive for \(0<\phi<\pi\), because \(\sin\phi-\phi\cos\phi>0\) there. At a zero with \(\pi<\phi<2\pi\), the secant is tangent: \(z(T)-z(t)=\lambda z'(t)\), and its imaginary component after rotation by \(e^{-it}\) gives \(\lambda=T\sin\phi/t<0\). Differentiating the cross product \(F_T(t)=\Im(\overline{z'(t)}[z(T)-z(t)])\) at such a zero yields
\[
F_T'(t)=-\lambda(t^2+2)>0.
\]
Thus every interior zero in that angular range crosses from negative to positive; there can be at most one. If \(\pi<T<2\pi\), \(F_T(0)=T\sin T<0\); at \(T=2\pi\), \(F_T(0)=0\) but \(F_T(t)<0\) for small \(t>0\); and if \(T>2\pi\), \(F_T(T-2\pi)=-2\pi(T-2\pi)<0\). On the other hand \(F_T(T-\pi)>0\), and no zero occurs with \(0<\phi<\pi\). The intermediate value theorem and upward-crossing property therefore produce the unique \(u\) in the asserted interval. For \(T\le\pi\), \(F_T(t)>0\) for all \(0<t<T\), so no contact truncation occurs.

**3. Global exposure, including earlier turns.** If \(T>\pi\), the outward normal turn from \(u\) to \(T\) is strictly less than \(2\pi\). Otherwise there would be \(v\in[u,T)\) with \(\nu(v)=\nu(T)-2\pi\). The terminal support \(q(T)>q(v)\) at their common normal would imply \(F_T(v)<0\), contradicting the unique-root sign \(F_T(v)\ge0\). Consequently every \(t\in(u,T)\) is the latest stationary support maximum at its normal; it beats the terminal point because \(F_T(t)>0\), all earlier stationary maxima because \(q\) increases, and the origin because \(q(t)>0\). It is therefore exposed. For \(t\in[\max\{0,T-2\pi\},u)\), the terminal point strictly beats its tangent support because \(F_T(t)<0\), so such a point cannot be exposed. If \(t+2\pi\le T\), then \(z(t)=\frac{t}{t+2\pi}z(t+2\pi)\), so every earlier winding lies on a radial segment between the origin and a later point. The origin belongs to the interior of the convex hull of the exposed arc, since that arc has positive radii in an angular interval longer than \(\pi\); no open semicircle can contain all its directions. Hence no earlier winding contributes boundary. At \(u\), the endpoint and tangent contact tie, yielding exactly one flat boundary chord. If \(T\le\pi\), the outward normal turn is less than \(2\pi\) and the same support argument exposes the whole arc; the two endpoints are joined by its radial chord. This determines all boundary pieces, not just a candidate supporting line.

**4. Intrinsic volumes.** On the spiral \(\Im(\overline{z}z')=t^2\) and \(|z'|=\sqrt{1+t^2}\). Green's theorem on the positively oriented spiral arc and return segment yields \(\tfrac12\int_u^Tt^2dt+\tfrac12\Im(\overline{z(T)}z(u))\), which simplifies to the stated area formula. Integrating the speed and adding the Euclidean chord length gives the perimeter. At \(u=0\), this reduces to the first regime.

**5. Sharp first transition.** Put \(T=\pi+\delta\) and solve the analytic tangent equation at \((t,\delta)=(0,0)\). Its derivative in \(t\) equals \(2\pi\), and its derivative in \(\delta\) is \(-\pi\); the implicit function theorem gives \(u=\delta/2+O(\delta^2)\). Taylor expansion of the exact area and perimeter formulas gives respectively \(\pi\delta^2/8+O(\delta^3)\) and \(-\delta^3/12+O(\delta^4)\) relative to the untruncated spiral and its radial closing segment. Both leading coefficients are nonzero, proving the powers sharp.

**6. Long-arc asymptotics.** Write \(u=T-2\pi+\epsilon\), where \(0<\epsilon<\pi\). The tangent equation reads
\[
0=T[-\sin\epsilon-(T-2\pi+\epsilon)\cos\epsilon]+(T-2\pi+\epsilon)^2.
\]
It implies \(\epsilon\to0\) as \(T\to\infty\) (otherwise its positive leading \(T^2(1-\cos\epsilon)\) cannot be canceled). Setting \(h=T^{-1/2}\) and expanding gives \(0=-2\pi+\epsilon^2/(2h^2)+O(h^2)\) after the leading cancellation, and matching the next orders yields \(\epsilon=2\sqrt\pi h+(\pi^{3/2}/3)h^3+O(h^4)\). Substitute this in the exact intrinsic-volume expressions, expanding \(\ell(T)-\ell(u)=\tfrac12(T^2-u^2)+\tfrac12\log(T/u)+O(T^{-3})\). Termwise Taylor expansion yields the two stated three-term asymptotics, with the remainders shown.

## Verification

The standalone `CHECK.py` compares the exact closed formulas with numerical convex hulls of 30,001 separately generated planar spiral points for eleven arc lengths, checks tangency and the direction of the return chord, and checks the first-transition and long-arc coefficients. It prints `ARCHIMEDEAN_SPIRAL_HULL_CHECKS_OK` on success. The mathematical proof above, not the finite computation, establishes the global claims. Run with `python3 CHECK.py` using Python with NumPy and SciPy installed.

## Relationship to prior work

The polar equation, classical spiral area and arclength primitives are documented in Archimedes' *On Spirals* and standard accounts including MathWorld. The geometrical model in Homan et al. (arXiv:1504.04996, originally posted April 20, 2015) uses precisely the linearly growing radial law and constant spacing between successive turns, but does not determine convex-hull exposed boundary, contact transition, or exact intrinsic volumes. An independently published result on Gaussian Fock coherent-state rotation overlaps proves a comparable arc-plus-tangent-chord description for a **logarithmic** spiral, with exponentially changing radius (published-finding corpus identifier below). That result does not contain the \(r=t\) Archimedean family or its finite-length \(T=\pi\) transition and large-\(T\) coefficients; the present argument uses a different monotone increasing sequence of normal-support maxima. A literature search found no matching formula for the complete linear-radius family, but this does not prove absolute historical novelty.

## Limitations

This is an exact planar convex-hull theorem for \(r=bt\) on a finite interval starting at its pole. It is not a theorem for logarithmic, affine-shifted, or general power-law spirals, nor for nonconvex geometric metrics. Numerical tests only check selected values and cannot certify universal quantifiers. Historical priority, especially older treatises on spiral tangents and supporting lines, remains incompletely assessed; the separately published logarithmic-spiral result was read in full and is a significant methodological antecedent. Independent mathematical audit has not been performed.

## References

1. W. Homan, L. Decin, A. de Koter, A. J. van Marle, R. Lombaert, W. Vlemmings, *Simplified models of stellar wind anatomy for interpreting high-resolution data: Analytical approach to embedded spiral geometries*, arXiv:1504.04996 (first public version April 20, 2015), especially Section 2.1. https://arxiv.org/abs/1504.04996
2. E. W. Weisstein, *Archimedes' Spiral*, MathWorld (classical curvature and arclength formula). https://mathworld.wolfram.com/ArchimedesSpiral.html
3. *Exact convexified Gaussian Fock coherent-state overlap geometry*, published mathematical research record (logarithmic spiral boundary and area/perimeter), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-convexified-gaussian-fock-coherent-state-overlap-geometry--efc09784f30f .
4. Archimedes, *On Spirals*, Proposition 24 (classical first-turn polar-sector area; historical date only approximate).
