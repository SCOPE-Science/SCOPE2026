# Dimension-three rigidity and inverse laws for central line intercepts of solid ring tori

## Finding
Let \(d\ge3\) be an integer, let \(0<r<R\), and let a Haar-uniform unoriented line through the origin probe the solid circular toroidal tube
\[
T_{R,r}^{(d)}=\{(x,z)\in\mathbb R^{d-1}\times\mathbb R:(\|x\|_2-R)^2+z^2\le r^2\}.
\]
Write \(L\) for the **total one-dimensional length** of its intersection with the solid (two disjoint segments, when nonempty). Put \(s=r/R\), and define \(I_x(a,b)=B_x(a,b)/B(a,b)\), the regularized incomplete beta function. Then
\[
\Pr(L>0)=I_{s^2}\left(\frac12,\frac{d-1}2\right).
\]
Conditional on a positive intercept, the normalized length \(Y=L/(4r)\) has exact CDF
\[
\boxed{F_{d,s}(y)=1-\frac{I_{s^2(1-y^2)}(1/2,(d-1)/2)}{I_{s^2}(1/2,(d-1)/2)}},\qquad 0\le y\le1.
\]
The unconditional law has the stated atom at zero and its continuous portion is given by this conditional CDF. The conditional law is **independent of the torus aspect ratio precisely in dimension three**. In that exceptional case, \(\Pr(L>0)=s\), \(F_{3,s}(y)=1-\sqrt{1-y^2}\), and \(\mathbb E[L\mid L>0]=\pi r\).

For every fixed integer \(d\ge4\), the conditional second normalized moment
\[
M_d(s)=\mathbb E[Y^2\mid L>0]
=\frac{\int_0^1(1-u^2)(1-s^2u^2)^{(d-3)/2}\,du}{\int_0^1(1-s^2u^2)^{(d-3)/2}\,du}
\]
is strictly increasing for \(0<s<1\), with endpoint limits \(M_d(0^+)=2/3\) and \(M_d(1^-)=1-1/d\). Knowing dimension and the full conditional length distribution therefore uniquely recovers \(r\) from the right endpoint \(4r\), then \(R=r/s\) from \(M_d(s)\). In dimension three that conditional law cannot recover \(R\); the missing information is supplied exactly by the hit probability \(r/R\).

There is also an exact high-dimensional transition. For fixed \(\kappa>0\), if \(s_d=\kappa/\sqrt d\) and \(d\) grows through integers with \(s_d<1\), then
\[
\Pr(L>0)\longrightarrow\operatorname{erf}(\kappa/\sqrt2),
\qquad
\mathcal L(Y\mid L>0)\xrightarrow{\mathrm{TV}}\mathcal L\left(\sqrt{1-(|G|/\kappa)^2}\mid |G|\le\kappa\right),
\]
where \(G\) is a standard normal random variable. The limiting CDF is
\[
1-\frac{\operatorname{erf}(\kappa\sqrt{1-y^2}/\sqrt2)}{\operatorname{erf}(\kappa/\sqrt2)},\quad 0\le y\le1.
\]

## Assumptions and scope
The toroidal solid is the radius-\(r\) Euclidean neighborhood of the radius-\(R\) sphere in the horizontal subspace \(\mathbb R^{d-1}\times\{0\}\), with \(d\ge3\) and \(R>r>0\). A random line passes exactly through the origin and its direction has rotationally invariant measure on projective directions (a uniform point on \(S^{d-1}\) modulo antipodes). This is neither a motion-invariant random *affine* line nor a line selected using the torus surface area. The full intersection has two intervals of equal length when hit; counting only one interval halves every positive length. Equalities at tangency and tangent directions have measure zero. Dimension is known for the inverse statement. An infinite-dimensional or varying-core family is not covered.

## Proof
**Radial equation and complete intercept.** Parametrize an oriented direction by \(v=(v_x,v_z)\in S^{d-1}\), and write \(\mu=|v_z|\). On a positive ray \(tv\) the defining inequality is
\[
t^2-2Rt\sqrt{1-\mu^2}+(R^2-r^2)\le0.
\]
Its roots are real precisely when \(\mu\le r/R=s\), in which case
\[
t_\pm=R\sqrt{1-\mu^2}\pm\sqrt{r^2-R^2\mu^2}.
\]
Their product is \(R^2-r^2>0\) and their sum is positive, so both are strictly positive. The negative ray supplies the reflected interval, establishing
\[
L=4\sqrt{(r^2-R^2\mu^2)_+}
\]
with the convention \(L=0\) outside the hit event. This is a geometric identity, not a probabilistic approximation.

**Exact distribution.** Uniformity on \(S^{d-1}\) gives the standard coordinate-square density
\[
\mu^2\sim\operatorname{Beta}\left(\frac12,\frac{d-1}2\right).
\]
For \(y\in[0,1]\), the conditional event \(Y\le y\) is \(s\sqrt{1-y^2}\le\mu\le s\). Taking the ratio of beta distribution probabilities proves the claimed CDF and atom. For \(d=3\), \(\mu\) is uniform on \([0,1]\), so \(Y\) has CDF \(1-\sqrt{1-y^2}\) independently of \(s\). Integration using \(\int_0^1\sqrt{1-u^2}\,du=\pi/4\) gives \(\mathbb E[L\mid L>0]=\pi r\).

**Strict inverse rigidity.** Conditioned on a hit, put \(U=\mu/s\in[0,1]\). Its density is proportional to \((1-s^2u^2)^k\), with \(k=(d-3)/2\). If \(k>0\) and \(s_2>s_1\), the density ratio
\[
\left(\frac{1-s_2^2u^2}{1-s_1^2u^2}\right)^k
\]
is strictly decreasing in \(u\in(0,1)\). Two normalized positive densities with a strictly decreasing likelihood ratio have strictly ordered expectations of every nonconstant increasing continuous statistic; equivalently, one can integrate the covariance with the decreasing ratio. Thus the expectation of the strictly decreasing statistic \(1-U^2=Y^2\) is strictly **larger** at \(s_2\). When \(k=0\), the conditional density of \(U\) is uniform for every \(s\). These two cases prove the claimed dimension-three equivalence. As \(s\downarrow0\) the conditional density of \(U\) approaches the uniform density, giving \(M_d(0^+)=2/3\). As \(s\uparrow1\), the conditioning disappears and \(U\) has the law of the absolute last coordinate of a sphere-uniform vector, with second moment \(1/d\). Hence \(M_d(1^-)=1-1/d\). The positive-length support has essential supremum \(4r\), so the stated reconstruction follows.

**Gaussian crossover and convergence mode.** For sphere-uniform \(v\) write \(W_d=\sqrt d\,|v_z|\). Its density is
\[
h_d(w)=\frac{2\Gamma(d/2)}{\sqrt{\pi d}\,\Gamma((d-1)/2)}\left(1-\frac{w^2}{d}\right)^{(d-3)/2}\mathbf1_{\{0\le w\le\sqrt d\}}.
\]
The gamma quotient asymptotic and exponential limit give pointwise convergence to \(\sqrt{2/\pi}e^{-w^2/2}\) on \([0,\infty)\). Since all are probability densities, Scheffé's lemma makes this convergence total variation. Now \(\mu\le s_d\) is \(W_d\le\kappa\). The limiting event has positive probability \(\operatorname{erf}(\kappa/\sqrt2)\), so conditioning preserves total-variation convergence. Applying the fixed measurable map \(w\mapsto\sqrt{1-(w/\kappa)^2}\) on \([0,\kappa]\) cannot increase total-variation distance. This gives the asserted limiting law and its CDF.

## Verification
A standalone numerical diagnostic script `check.py` is included. Execute `python check.py` with Python, NumPy, and SciPy. It verifies root geometry against direct point-to-torus membership at thousands of sampled directions and multiple dimensions and shape ratios; beta hit probabilities and the three-dimensional conditional CDF; monotonicity samples of the normalized second moment; and finite-dimensional convergence toward the Gaussian crossover. The script was executed successfully with 1070 reported assertion groups. These tests are illustrative, not a proof of strict monotonicity for all aspect ratios or of convergence in total variation; the analytic arguments above establish those claims.

## Relationship to prior work
Gille (2005) established chord-length laws for a hemisphere under an isotropic-uniform *affine chord* model, a different probe measure and body. García Monera and Monterde (2011) studied exact central planar torus sections and special Villarceau circles. Their geometry supplies the classical torus setting but not the origin-passing random-line distribution or its all-dimensional inverse dichotomy. Cychosz (1991) describes ray–torus intersection algorithms: the algebraic line-intersection step is therefore classical and is not claimed as novel. A published study of Haar central-plane *area* and topology (2026) treats plane sections instead of line-intercept lengths; a separate torus-shadow study (2026) treats orthographic projections. Similarly, published chord-moment reconstruction for two independent random points on a ring-torus surface has a different random observable. The contribution claimed here is the *joint exact centered-probe probability family, the exceptional three-dimensional conditional-law invariance, the strictly invertible higher-dimensional second moment, and the marked Gaussian transition*, not the ray intersection polynomial. The historical priority of this combined statement remains provisional.

## Limitations
These are the laws of origin-passing Haar-direction lines, not Euclidean-motion-invariant affine chords or general stereological sampling. The interior hole assumption \(0<r<R\) matters: when the torus degenerates to a horn or spindle, the ray-intercept geometry changes. The dimension-three nonidentifiability concerns the conditional **length** distribution without hit frequencies; the unconditional distribution does identify both parameters. The high-dimensional scaling fixes \(\kappa>0\); no uniformity for \(\kappa\to0\) or \(\kappa\to\infty\) is asserted. An older ray–torus article remained inaccessible in full, leaving a historical-priority risk; no independent mathematical audit has been performed.

## References
1. W. Gille, *Chord Length Distributions of the Hemisphere*, Journal of Mathematics and Statistics 1 (2005), 24–28, first published 31 March 2005. https://doi.org/10.3844/jmssp.2005.24.28
2. M. García Monera and J. Monterde, *Building a Torus with Villarceau Sections*, Journal for Geometry and Graphics 15 (2011), 93–99. https://www.heldermann-verlag.de/jgg/jgg15/j15h1mone.pdf
3. J. Cychosz, *Intersecting a Ray with an Elliptical Torus* (1991), in *Graphics Gems II*. https://doi.org/10.1016/B978-0-08-050754-5.50054-2
4. *Logarithmic area cusp and Haar topology law at the Villarceau transition* (2026), published technical note. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-logarithmic-area-cusp-and-haar-topology-law-at-the-villarceau-tr--3f2e0b5e194a
5. *Two visibility transitions and a critical hole-area tail for torus shadows* (2026), published technical note. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-two-visibility-transitions-and-a-critical-hole-area-tail-for-tor--128776cbdf5e
6. *Sharp two-moment ambiguity and three-moment reconstruction of ring-torus surfaces* (2026), published technical note. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-two-moment-ambiguity-and-three-moment-reconstruction-of-ri--99081f2abf19
