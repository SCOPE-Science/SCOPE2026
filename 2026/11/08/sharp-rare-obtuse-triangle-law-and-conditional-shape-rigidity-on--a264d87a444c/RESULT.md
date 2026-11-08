# Sharp rare-obtuse-triangle law and conditional shape rigidity on high-dimensional spheres

## Finding

Let \(X_d,Y_d,Z_d\) be independent, normalized-surface-area-uniform points on the unit sphere \(S^{d-1}\subset\mathbb R^d\). Let \(p_d\) be the probability that their Euclidean triangle has an angle strictly greater than \(\pi/2\). For integers \(d\to\infty\),

\[
p_d=\frac{27\sqrt6}{16\sqrt{\pi d}}\left(\frac{16}{27}\right)^{d/2}\left(1+O(d^{-1})\right).
\]

There is also **conditional shape rigidity**, including a Gaussian fluctuation. Write
\[
E_d=\bigl\{(Y_d-X_d)\cdot(Z_d-X_d)<0\bigr\},\qquad T_d=X_d\cdot Y_d.
\]
Under the conditional distribution given \(E_d\),
\[
(T_d,X_d\cdot Z_d,Y_d\cdot Z_d)\xrightarrow{\mathbb P}
\left(\frac13,\frac13,-\frac13\right),
\qquad
\sqrt d\left(T_d-\frac13\right)\xrightarrow{\mathrm d}N\left(0,\frac{16}{27}\right).
\]
Consequently the three squared side lengths \((\|X_d-Y_d\|^2,\|X_d-Z_d\|^2,\|Y_d-Z_d\|^2)\) converge in conditional probability to \((4/3,4/3,8/3)\). A rare obtuse triangle is asymptotically right isosceles, not approximately equilateral as a triple of typical almost-orthogonal sphere points would be. Relabeling the unique obtuse vertex as \(X_d\) transfers the shape statement to conditioning on the event defining \(p_d\).

## Assumptions and scope

The ambient dimension is an integer \(d\ge3\), and all three points are independently distributed according to normalized surface area on the Euclidean unit sphere. Angle refers to the Euclidean angle of the chordal triangle, not a spherical geodesic angle. The limit concerns a **single three-point sample as dimension tends to infinity**, not a growing point cloud. The remainder \(O(d^{-1})\) is relative to the displayed asymptotic, with an absolute implied constant; the Gaussian limit concerns the first displayed dot product conditional on an obtuse angle at the named vertex. The boundary case of an exactly right angle has probability zero.

## Proof

**1. Exact one-dimensional reduction.** For a fixed unit vector, the dot product with an independent uniform point on \(S^{d-1}\) has density
\[
h_d(t)=c_d(1-t^2)^m,\quad -1<t<1,\qquad
m=\frac{d-3}{2},\quad c_d=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)}.
\]
Set \(T=X\cdot Y\), \(u=(Y-X)/\|Y-X\|\), and \(s(t)=\sqrt{(1-t)/2}\). Conditional on \(T=t\), the independent point \(Z\) is uniform on the sphere; because \(u\cdot X=-s(t)\),
\[
E_d\quad\Longleftrightarrow\quad u\cdot Z<-s(t).
\]
By reflection, the conditional probability is \(c_d I_m(s(t))\), with
\[
I_m(s)=\int_s^1(1-v^2)^m\,dv.
\]
At most one angle of a nondegenerate triangle can be obtuse, and exchangeability gives exactly
\[
\tag{1}
p_d=3c_d^2\int_{-1}^1(1-t^2)^m I_m(s(t))\,dt.
\]
This integral representation is consistent with the earlier spherical-cap formula of Drivas and Retakh, which is credited below.

**2. Uniform cap asymptotic at its relevant threshold.** Integrating the derivative of \((1-v^2)^{m+1}\) gives, for \(0<s<1\),
\[
\tag{2}
I_m(s)=\frac{(1-s^2)^{m+1}}{2(m+1)s}
-\frac{1}{2(m+1)}\int_s^1\frac{(1-v^2)^{m+1}}{v^2}\,dv.
\]
Thus \(I_m(s)\le(1-s^2)^{m+1}/[2(m+1)s]\). On every compact subinterval of \((0,1)\), the discarded term divided by the first is \(O(m^{-1})\), uniformly as \(m\to\infty\): indeed \(v^{-2}\le s^{-2}\), and applying the same upper bound with exponent \(m+1\) gives an error ratio at most \((1-s^2)/[2(m+2)s^2]\). It follows that
\[
\tag{3}
I_m(s)=\frac{(1-s^2)^{m+1}}{2(m+1)s}\bigl(1+O(m^{-1})\bigr)
\]
uniformly for \(s\) in a fixed compact interval inside \((0,1)\).

**3. Global saddle and correct exponential rate.** Put
\[
F(t)=(1-t^2)(1-s(t)^2)=\frac{(1-t)(1+t)^2}{2},\qquad
g(t)=\frac{1-s(t)^2}{s(t)}=\frac{1+t}{\sqrt{2(1-t)}}.
\]
The upper bound following (2) majorizes the integrand of (1) by
\(F(t)^m g(t)/[2(m+1)]\). The function \(F\) is positive in \((-1,1)\), vanishes at both ends, and has a unique global maximum at \(t_*=1/3\), where
\[
\tag{4}
F(t_*)=\frac{16}{27},\quad g(t_*)=\frac{2\sqrt3}{3},\quad
-\bigl(\log F\bigr)''(t_*)=\frac{27}{8}=:\kappa.
\]
The amplitude \(g\) is integrable at both endpoints (in particular its \((1-t)^{-1/2}\) singularity at \(1\) is integrable). Since \(F\) has a strict unique interior maximum, the integral outside any fixed small neighborhood of \(t_*\) is exponentially smaller than \(F(t_*)^m m^{-1/2}\). On that neighborhood, (3) applies uniformly. Therefore (1) reduces, up to relative \(O(m^{-1})\), to
\[
p_d=\frac{3c_d^2}{d-1}\int_{-1}^1F(t)^m g(t)\,dt\,\bigl(1+O(m^{-1})\bigr).
\]
The ordinary interior Laplace expansion for smooth \(F,g\) near \(t_*\) gives
\[
\tag{5}
\int_{-1}^1F(t)^m g(t)\,dt
=\left(\frac{16}{27}\right)^m\frac{2\sqrt3}{3}
\sqrt{\frac{2\pi}{m(27/8)}}\bigl(1+O(m^{-1})\bigr).
\]
Finally, by the gamma-ratio expansion \(c_d^2/(d-1)=1/(2\pi)(1+O(d^{-1}))\) and \(m=(d-3)/2\), equations (4)–(5) simplify to
\[
p_d=\frac{27\sqrt6}{16\sqrt{\pi d}}
\left(\frac{16}{27}\right)^{d/2}\bigl(1+O(d^{-1})\bigr).
\]
In particular, substituting the *typical* dot product \(T\approx0\) into the cap tail is exponentially inaccurate: the rare event tilts the pair to \(T\approx1/3\).

**4. Conditional central limit theorem.** Under \(E_d\), the density of \(T\) is proportional to the integrand of (1), without its factor \(3\). The preceding global localization and uniform cap estimate show that, in a fixed neighborhood of \(t_*\), this density is asymptotic to a normalized \(F(t)^m g(t)\). Taylor's formula gives
\[
\log F(t)-\log F(t_*)=-\frac\kappa2(t-t_*)^2+O(|t-t_*|^3).
\]
Laplace localization, with \(t=t_*+y/\sqrt d\) and \(m/d\to1/2\), yields a centered Gaussian density proportional to \(\exp(-\kappa y^2/4)\), hence variance \(2/\kappa=16/27\). In particular, \(T\to1/3\) in probability under \(E_d\).

**5. The remaining two dot products.** Conditional on \(T=t\) and \(E_d\), the coordinate \(V=u\cdot Z\) has density proportional to \((1-v^2)^m\) on \((-1,-s(t))\). On each compact neighborhood of \(t_*\), for every \(\varepsilon>0\), the ratio of cap integrals \(I_m(s(t)+\varepsilon)/I_m(s(t))\to0\) exponentially where \(s(t)+\varepsilon<1\). Therefore \(V+s(T)\to0\) in conditional probability. Let \(w=(X+Y)/\|X+Y\|\); then \(u\perp w\) and \(q(t)=\sqrt{(1+t)/2}\) satisfies
\[
X=-s(T)u+q(T)w,\qquad Y=s(T)u+q(T)w.
\]
Given \(V\), the remaining direction of \(Z\) is uniform in the sphere orthogonal to \(u\), and \(\mathbb E[(w\cdot Z)^2\mid V]=(1-V^2)/(d-1)\le1/(d-1)\). Consequently \(w\cdot Z\to0\) in conditional probability. It follows that
\[
X\cdot Z=-s(T)V+q(T)(w\cdot Z)\to\frac13,
\quad Y\cdot Z=s(T)V+q(T)(w\cdot Z)\to-\frac13,
\]
while \(X\cdot Y=T\to1/3\). Applying the chord identity \(\|A-B\|^2=2-2A\cdot B\) completes the shape statement. \(\square\)

## Verification

A self-contained numerical checker `verify.py` independently integrates the exact beta-cap representation in (1), verifies the known \(d=3\) sphere value \(p_3=1/2\) and the exact \(d=5\) value \(p_5=17/70\), compares large-dimensional probabilities to the stated sharp constant, tests the conditional variance prediction, and performs a seeded direct sphere-point simulation. It also checks the saddle identities symbolically. These finite computations are diagnostics, **not** substitutes for the proof of asymptotics or conditional limits.

## Relationship to prior work

Drivas and Retakh (2025) derive the exact cap-integral law for obtuse triangles from sphere-surface-uniform points and propose a high-dimensional approximation based on a *typical* pairwise angle. The present result uses that geometric reduction but identifies the different, exponentially tilted saddle \(T=1/3\), proves the exact exponential decay and prefactor, and proves the new conditional Gaussian fluctuation and isosceles-right shape concentration. The earlier finite-dimensional integral is a genuine broader representation of the probability, but **does not itself state these sharp asymptotic or conditional-shape theorems**. The distinction rests on the additional global saddle analysis rather than a change of sampling convention.

Cai–Fan–Jiang (2013) describe concentrations and extremes of **central angles between pairs** of spherical points, whereas the present event is a rare **Euclidean three-point angle** involving dependent chord directions. Edelman–Strang (2015) and the Gaussian-triangle result credited to Eisenberg–Sullivan (1996) use Gaussian point coordinates, not sphere-surface-uniform points. An attempted review of the complete Eisenberg–Sullivan text was not successful, so the possibility of additional related historical content cannot be wholly eliminated.

## Limitations

The theorem concerns independent unit-sphere surface sampling, fixed sample size three and large ambient dimension. The asymptotic relative error is \(O(d^{-1})\) but no explicit universal finite-dimensional error constant is provided. It does not give an analogous result for uniform **volume** sampling, Gaussian coordinate sampling, or spherical geodesic triangles. The Gaussian limit is stated for the distinguished dot product, not as an unproved multivariate central limit theorem for all three dot products. The current literature comparison is substantive but not an independent historical priority certification; a plausible older paper was not available in full text.

## References

1. Tony Cai, Jianqing Fan, Tiefeng Jiang, *Distributions of Angles in Random Packing on Spheres*, arXiv:1306.0256, first public June 2, 2013, https://arxiv.org/abs/1306.0256.
2. Alan Edelman, Gilbert Strang, *Random Triangle Theory with Geometry and Applications*, arXiv:1501.03053, first public January 2015, https://arxiv.org/abs/1501.03053.
3. Theodore D. Drivas, Michael Retakh, *How doth the random triangle*, arXiv:2508.18414, first public August 25, 2025, https://arxiv.org/abs/2508.18414; in particular the sphere-sampling cap law, pp. 8–9.
4. B. Eisenberg, R. Sullivan, *Random Triangles in n Dimensions*, American Mathematical Monthly 103 (1996), 308–318, DOI:10.2307/2975187; full text unavailable for inspection.
