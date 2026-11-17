# A three-regime extreme-area transition for triangles sampled on a circular arc

## Finding

Let three independent angles be uniform on a fixed circular arc of angular length \(0<L\le 2\pi\) on the unit circle, and let \(A\) be the Euclidean area of their inscribed triangle. Set \(L_0=4\pi/3\), \(s_*=\min\{L,L_0\}\), and \(M_L=\sin(s_*/2)(1-\cos(s_*/2))\). The exact area maximum is \(M_L\). For fixed \(L\), as \(\varepsilon\downarrow0\),

\[
\Pr\{A>M_L-\varepsilon\}\sim
\begin{cases}
\displaystyle\frac{16}{5L^3p_L^2\sqrt{q_L}}\varepsilon^{5/2},&0<L<L_0,\\[3pt]
\displaystyle\frac{18}{3^{3/4}\pi^3}\varepsilon^{3/2},&L=L_0,\\[3pt]
\displaystyle\frac{16\pi(L-L_0)}{L^3}\varepsilon,&L_0<L\le2\pi,
\end{cases}
\]

where \(p_L=(1-\cos(L/2))(1+2\cos(L/2))/2>0\) and \(q_L=\sin(L/2)/2>0\) in the first branch.

These three exponents reflect an abrupt change from an isolated, endpoint-pinned maximizer, through a degenerate pinned maximizer, to a positive-length family of interior equilateral maximizers. All three regimes have explicit *conditional geometric* limits in total variation, as detailed in the proof.

## Assumptions and scope

The angular sampling measure is normalized Lebesgue measure on \([0,L]\), and the three angles are independent. A unit circle is used; for circle radius \(R\), all areas and area deficits are multiplied by \(R^2\). The conclusions are for each fixed \(L\), not for \(L\) approaching \(L_0\) jointly with \(\varepsilon\). At \(L=2\pi\) the arc covers the complete circle, with its endpoints identified, a null event under the sampling law.

Write ordered sampled angles as \(0\le\theta_1<\theta_2<\theta_3\le L\), and define

\[
u=\theta_1,\qquad s=\theta_3-\theta_1,\qquad t=\theta_2-(\theta_1+\theta_3)/2.
\]

Their joint density is \(6/L^3\) on \(0<s<L\), \(0<u<L-s\), and \(|t|<s/2\). Define \(F(s)=\sin(s/2)(1-\cos(s/2))\), and set \(a_0=3\sqrt3/16\) and \(b_0=\sqrt3/4\).

## Proof

**1. Exact triangle identity, maxima, and finite-threshold probability.** A shoelace calculation gives

\[
A=\sin(s/2)\bigl(\cos t-\cos(s/2)\bigr),
\qquad F(s)-A=\sin(s/2)(1-\cos t).
\]

Thus \(t=0\) maximizes area at fixed \(s\). Differentiation yields \(F'(s)=(1-\cos(s/2))(1+2\cos(s/2))/2\), positive for \(0<s<L_0\) and negative for \(L_0<s<2\pi\). Therefore \(M_L=F(s_*)\). If \(L<L_0\), the sole maximizer has sorted angles \((0,L/2,L)\). At \(L=L_0\) it is the endpoint equilateral triangle. If \(L>L_0\), all and only maximizers have angles \((u,u+2\pi/3,u+4\pi/3)\), \(0\le u\le L-L_0\).

For every \(0<\varepsilon<M_L\), put \(h=M_L-\varepsilon\). Integrating the exact \(t\)-threshold produces the finite-threshold formula

\[
\Pr(A>h)=\frac{12}{L^3}\int_{\{0<s<L:F(s)>h\}}
(L-s)\arccos\!\left(\cos(s/2)+\frac{h}{\sin(s/2)}\right)ds.
\]

Indeed, the arccosine is defined between zero and \(s/2\) on the integration domain, and \(u\) ranges over an interval of length \(L-s\). This exact integral is also suitable for independent numerical verification.

**2. Endpoint-pinned regime.** Assume \(L<L_0\), set \(\delta=L-s\), and retain \(u\). Uniform Taylor expansion at \((\delta,t)=(0,0)\) gives

\[
M_L-A=p_L\delta+q_Lt^2+O_L(\delta^2+\delta t^2+t^4).
\]

The event \(A>M_L-\varepsilon\) forces \(\delta=O_L(\varepsilon)\), \(|t|=O_L(\sqrt\varepsilon)\), and \(0\le u\le\delta\). Rescaling \(\delta=\varepsilon x/p_L\), \(t=\sqrt{\varepsilon/q_L}\,y\), and using the exact density gives the limiting volume

\[
\frac{6}{L^3}\frac{\varepsilon^{5/2}}{p_L^2\sqrt{q_L}}
\int_0^1 2x\sqrt{1-x}\,dx
=\frac{16}{5L^3p_L^2\sqrt{q_L}}\varepsilon^{5/2}.
\]

(Here \(\int_0^1x\sqrt{1-x}\,dx=4/15\).) More precisely, conditionally on this event, the triple

\[
\left(\frac{p_Lu}{\varepsilon},\frac{p_L(\delta-u)}{\varepsilon},\frac{q_Lt^2}{\varepsilon}\right)
\]

converges in total variation to the first three coordinates of a \(\operatorname{Dirichlet}(1,1,1/2,1)\) vector. The sign of \(t\) is an independent fair sign, both before and after taking the limit. The fourth Dirichlet coordinate is the limiting normalized unused quadratic-deficit budget.

**3. Critical arc.** If \(L=L_0\), then \(F'(L_0)=0\), \(F''(L_0)=-3\sqrt3/8\). For \(\delta=L_0-s\ge0\),

\[
M_{L_0}-A=a_0\delta^2+b_0t^2+O(\delta^3+\delta t^2+t^4).
\]

The density includes the factor \(\delta\) from the allowable starting-angle interval. Therefore

\[
\Pr(A>M_{L_0}-\varepsilon)
\sim\frac6{L_0^3}\int_0^{\sqrt{\varepsilon/a_0}}\!
2\delta\sqrt{\frac{\varepsilon-a_0\delta^2}{b_0}}\,d\delta
=\frac4{L_0^3a_0\sqrt{b_0}}\varepsilon^{3/2}
=\frac{18}{3^{3/4}\pi^3}\varepsilon^{3/2}.
\]

Conditionally, \((a_0\delta^2/\varepsilon,b_0t^2/\varepsilon)\) converges in total variation to the first two coordinates of \(\operatorname{Dirichlet}(1,1/2,1)\). Moreover \(u/\delta\) is exactly uniform on \((0,1)\) and independent of \((\delta,t)\), and the sign of \(t\) is exactly independent and fair.

**4. Equilateral-orbit regime.** When \(L>L_0\), put \(x=s-L_0\). Then uniformly near the entire maximizing segment,

\[
M_L-A=a_0x^2+b_0t^2+O(|x|^3+|x|t^2+t^4).
\]

Since \(0<u<L-s\), the normalized mass is the orbit length \(L-L_0\) times the limiting elliptic disk area:

\[
\Pr(A>M_L-\varepsilon)
\sim\frac6{L^3}(L-L_0)\frac{\pi\varepsilon}{\sqrt{a_0b_0}}
=\frac{16\pi(L-L_0)}{L^3}\varepsilon.
\]

Conditionally, \(((s-L_0)\sqrt{a_0/\varepsilon},t\sqrt{b_0/\varepsilon})\) converges in total variation to the uniform law on the Euclidean unit disk; jointly \(u\) converges to an independent uniform variable on \((0,L-L_0)\).

**5. Total-variation justification.** In all three regimes, strict maximality away from the displayed optimizer set confines the conditioning event to the stated shrinking neighborhoods. The indicated affine or square-root changes of variables turn the joint densities into explicit Jacobian-weighted densities on bounded rescaled regions. Taylor remainders converge uniformly there; the only nonbounded weight is the integrable factor \(z^{-1/2}\) in squared-offset coordinates. Dominated convergence followed by normalization establishes \(L^1\) convergence of the rescaled densities, equivalent to total-variation convergence. Where a limiting Dirichlet vector is mentioned, the displayed coordinates are the indicated marginals, so no claim is made that finite-\(\varepsilon\) points lie exactly on the limiting simplex.

## Verification

The standalone `checker.py` independently computes triangle areas by the shoelace formula, verifies their equality with the analytic coordinate identity, checks the location of the global maximum by bounded numerical optimization, and numerically integrates the exact one-dimensional tail formula for one arc in each of the three regimes. The output `FIXED_CIRCULAR_ARC_AREA_PHASE_CHECKS_OK` was obtained. For \(\varepsilon=8\cdot10^{-5}\), the exact-tail-to-asymptotic ratios were approximately \(0.99998975\), \(1.00002617\), and \(1.00001711\) for \(L=2.8\), \(L=L_0\), and \(L=5.2\), respectively. These finite numerical checks are corroborative, not a proof of the infinite limits.

## Relationship to prior work

Böröczky, Fodor and Hug (2011) analyze expectations of intrinsic volumes for the convex hull of a *growing number* of independent points on the **entire boundary** of a convex body; their hypotheses and limiting operation do not yield this three-point, fixed-arc, conditional upper-area law. The MathWorld *Circle Triangle Picking* treatment considers full-circle sampling and supplies the classical trigonometric area identity and expected-area calculation. The complete-circle specialization of the last branch is therefore presented as a consistency case, not as a standalone novelty claim. Finch and Jones (2010) address intrinsic spherical triangles formed from points on the two-sphere, with a different metric and sampling space. Related published findings concerning a threefold-deformed **closed** planar oval and disk-interior triangles likewise do not imply the arc-width bifurcation. No examined source states the simultaneous three-exponent transition and its marked conditional limits. Unexamined historical treatments of random triangles constrained to arcs remain a possible priority risk.

## Limitations

The theorem is for exactly three independent uniform-angular points on a unit circular arc, and each arc length \(L\) is held fixed as the rare-event threshold vanishes. It does not establish the joint critical crossover when \(L-L_0\) and \(\varepsilon\) vanish together, nor nonuniform angular densities, higher polygon vertex counts, or an elementary closed form for the entire area distribution. The results have not received independent mathematical audit. The finite computations cannot substitute for proof.

## References

1. K. J. Böröczky, F. Fodor, and D. Hug, *Intrinsic volumes of random polytopes with vertices on the boundary of a convex body*, arXiv:1103.4978, first public version March 25, 2011, https://arxiv.org/html/1103.4978v1 .
2. E. W. Weisstein, *Circle Triangle Picking*, MathWorld, https://mathworld.wolfram.com/CircleTrianglePicking.html .
3. S. R. Finch and A. J. Jones, *Random Spherical Triangles*, arXiv:1009.5329, first public version September 27, 2010, https://arxiv.org/html/1009.5329v3 .
