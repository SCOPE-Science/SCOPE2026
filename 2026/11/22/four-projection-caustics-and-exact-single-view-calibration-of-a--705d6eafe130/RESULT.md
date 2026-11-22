# Four projection caustics and exact single-view calibration of a quarter-turn swimmer

## Finding

Consider the stationary athermal planar particle
\[
\dot{\mathbf X}_t=-\mu\mathbf X_t+v_0\mathbf e_t,
\]
where \(\mu,v_0>0\), the propulsion direction \(\mathbf e_t\) belongs to the four cardinal unit vectors, and each permitted clockwise and counterclockwise quarter-turn has rate \(\gamma>0\). Put \(\beta=\gamma/\mu\) and \(R=v_0/\mu\). Let \(Z=X\cos\phi+Y\sin\phi\) be a stationary, unit-axis position projection. Define
\[
a=R\max\{|\cos(\phi-\pi/4)|,|\sin(\phi-\pi/4)|\},\qquad
b=R\min\{|\cos(\phi-\pi/4)|,|\sin(\phi-\pi/4)|\}.
\]
For every generic view \(0<b<a\) and every \(0<\beta<1/2\), the projected probability density has **exactly four divergent caustics**, at \(\pm(a+b)\) and \(\pm(a-b)\), and is smooth away from these four locations within its support. Put \(s=a+b\), \(h=a-b\), and \(B_\beta=B(1/2,\beta)\). Then
\[
p_Z(z)\sim C_{\rm out}(s-|z|)^{2\beta-1}\quad (|z|\uparrow s),\qquad
p_Z(z)\sim C_{\rm in}|z\mp h|^{2\beta-1}\quad (z\to\pm h),
\]
with the inner limit valid from either side, and
\[
C_{\rm out}=\frac{2^{2\beta-2}B(\beta,\beta)}{(ab)^\beta B_\beta^2},\quad
C_{\rm in}=\frac{2^{2\beta-2}B(\beta,1-2\beta)}{(ab)^\beta B_\beta^2},\quad
\boxed{\frac{C_{\rm in}}{C_{\rm out}}=\frac1{2\cos(\pi\beta)}}.
\]
Consequently, the four singularity locations together with their leading inner-to-outer amplitude ratio determine \(\beta\), the confinement length \(R\), and the view angle relative to the propulsion square, modulo its dihedral symmetry:
\[
a=\frac{s+h}{2},\quad b=\frac{s-h}{2},\quad
R=\sqrt{\frac{s^2+h^2}{2}},\quad
\beta=\frac1\pi\arccos\!\left(\frac{C_{\rm out}}{2C_{\rm in}}\right),\quad
\frac ba=\frac{s-h}{s+h}.
\]
At the critical \(\beta=1/2\), for \(0<b<a\), both inner divergences become logarithmic with coefficient \(1/(2\pi^2\sqrt{ab})\), and the outer density has a finite positive one-sided limit. For \(\beta>1/2\) all four corresponding density values are finite (and the density vanishes at its outer endpoints). If \(a=b>0\), the two inner caustics coalesce at zero, where their leading coefficients add; this nongeneric view is excluded from the four-location inversion.

## Assumptions and scope

There is no translational Brownian diffusion, no resetting, and no inertial term. Both quarter-turn directions occur at the same rate \(\gamma\) **each** (total orientation jump rate \(2\gamma\)); this rate convention fixes \(\beta\). Observations are taken in the unique stationary law. The theorem on four divergences and exact inversion requires \(0<\beta<1/2\) and \(0<b<a\). The critical and higher-rate boundary statements concern density limits only, not a classification of every finite local mode.

## Proof

Write \(U=(X+Y)/\sqrt2\), \(V=(X-Y)/\sqrt2\). Changing the orientation by \(90^\circ\) flips exactly one of the signs of the propulsion components in these coordinates. Each sign flips independently at rate \(\gamma\), so \(U/R\) and \(V/R\) are independent and identically distributed in stationarity, with density
\[
f_\beta(u)=\frac{(1-u^2)^{\beta-1}}{B(1/2,\beta)}\mathbf1_{(-1,1)}(u).
\]
This follows directly from the one-dimensional telegraph stationary forward equations, with zero stationary total spatial flux, or from the known exact decoupling. Reflections of the two independent symmetric variables absorb the signs of the projection coefficients. Therefore \(Z\stackrel d=aA+bB\), with \(A,B\) independent of common density \(f_\beta\), and
\[
p_Z(z)=\frac1b\int_{\max(-1,(z-b)/a)}^{\min(1,(z+b)/a)}
f_\beta(u)f_\beta((z-au)/b)\,du
\]
when the integration interval is nonempty. Its support is \([-s,s]\). The endpoints of the integration interval change their defining branch precisely at \(z=\pm s,\pm h\); standard smooth dependence after partitioning away from the four corners makes the density smooth elsewhere in the support.

At \(z=s-\varepsilon\), put \(A=1-u\), \(B=1-v\), so \(aA+bB=\varepsilon\). The endpoint density factors are \(2^{\beta-1}A^{\beta-1}/B_\beta\) and \(2^{\beta-1}B^{\beta-1}/B_\beta\), to relative error tending to zero. The resulting positive simplex integral is
\[
\int_{A,B\ge0}A^{\beta-1}B^{\beta-1}
\delta(\varepsilon-aA-bB)\,dA\,dB
=(ab)^{-\beta}B(\beta,\beta)\varepsilon^{2\beta-1}.
\]
This gives \(C_{\rm out}\), and reflection gives the negative endpoint.

At \(z=h+\delta\), the relevant corner is \((u,v)=(1,-1)\); write \(u=1-A\), \(v=-1+B\), giving \(\delta=bB-aA\). For \(\delta>0\), the local integral becomes
\[
(ab)^{-\beta}\delta^{2\beta-1}
\int_0^\infty t^{\beta-1}(1+t)^{\beta-1}\,dt
=(ab)^{-\beta}B(\beta,1-2\beta)\delta^{2\beta-1}.
\]
This improper integral is finite exactly when \(\beta<1/2\). For \(\delta<0\), interchange the nonnegative corner variables; the coefficient is the same. The opposite inner caustic follows by reflection. On a fixed neighborhood of each corner, rescaling and dominated convergence prove the stated equivalents; the remainder stays bounded and hence is negligible against the divergence. The four caustics are distinct when \(a>b>0\).

The Euler reflection identity gives
\[
\frac{B(\beta,1-2\beta)}{B(\beta,\beta)}
=\frac{\Gamma(2\beta)\Gamma(1-2\beta)}{\Gamma(\beta)\Gamma(1-\beta)}
=\frac{\sin(\pi\beta)}{\sin(2\pi\beta)}
=\frac1{2\cos(\pi\beta)}.
\]
This ratio is strictly increasing on \((0,1/2)\); the displayed algebra then proves the inversion, with the unavoidable square symmetries. When \(\beta=1/2\), the corner integral is logarithmic with coefficient \(2^{2\beta-2}(ab)^{-\beta}/B_\beta^2\) at \(\beta=1/2\), namely \(1/(2\pi^2\sqrt{ab})\). The outer-endpoint beta integral gives its finite value. For \(\beta>1/2\) the corner integral is locally integrable and the outer asymptotic has positive exponent; thus no density divergence remains at these four locations. At \(a=b\), the inner corners coincide and both leading contributions add.

## Verification

Run `python CHECK.py` with Python 3 and `mpmath`. It checks 23 Beta-identity, positive/negative local asymptotic, critical logarithmic increment, and inversion-geometry assertions. For example, \(a=4/5\), \(b=3/5\), \(\beta=1/4\) give four caustics at \(\pm7/5\), \(\pm1/5\) and \(C_{\rm in}/C_{\rm out}=1/\sqrt2\). The finite-precision quadrature is corroborative, not a substitute for the corner-integral proof. No exhaustive simulation or external certification is claimed.

## Relationship to prior work

Smith, Le Doussal, Majumdar and Schehr (2022), arXiv:2207.10445, establish the full two-dimensional stationary beta-product law and its rotated-coordinate independence, including the special Cartesian marginal in Appendix B. Basu, Majumdar, Rosso, Sabhapandit and Schehr (2019), arXiv:1910.10083, establish the related special Cartesian projection via a three-state kinetic model and its shape transition under a different angular-rate convention. These prior distribution formulas and axis-projection results are **not** claimed here as new. The result assessed here is the arbitrary-generic-angle four-caustic asymptotic, universal inner/outer coefficient identity, and exact one-view inverse identification; the known full joint law already contains the requisite information implicitly, so publication-priority review must check for prior derivations of these consequences.

## Limitations

The divergence and inversion assertions fail as written with translational thermal diffusion, which smooths the caustics, and do not address finite data, nonstationary transients, or unspecified angular-turn mechanisms. The inverse view angle is identifiable only modulo the symmetries of the square. Higher-rate conclusions do not assert global unimodality. Claims of experimental resolution, entropy production, or independent external verification are not made.

## References

- N. R. Smith, P. Le Doussal, S. N. Majumdar, G. Schehr, *Exact position distribution of a harmonically-confined run-and-tumble particle in two dimensions*, arXiv:2207.10445, first posted 2022-07-21, https://arxiv.org/abs/2207.10445.
- U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit, G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083, first posted 2019-10-22, https://arxiv.org/abs/1910.10083.
