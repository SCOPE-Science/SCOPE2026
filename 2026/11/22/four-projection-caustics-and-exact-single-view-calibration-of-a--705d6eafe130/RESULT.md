# Four projection caustics and exact single-view calibration of a quarter-turn swimmer

## Finding

Consider the stationary athermal planar particle
\[
\dot{\mathbf X}_t=-\mu\mathbf X_t+v_0\mathbf e_t,
\]
where \(\mu,v_0>0\), the propulsion directions \(\mathbf e_t\) are the four cardinal **unit** vectors, and each permitted clockwise and counterclockwise quarter-turn has rate \(\gamma>0\). Put \(\beta=\gamma/\mu\), \(R=v_0/\mu\). For a unit viewing axis, let \(Z=X\cos\phi+Y\sin\phi\) be the stationary projected position. Define
\[
a=\frac{R}{\sqrt2}\max\{|\cos(\phi-\pi/4)|,|\sin(\phi-\pi/4)|\},\qquad
b=\frac{R}{\sqrt2}\min\{|\cos(\phi-\pi/4)|,|\sin(\phi-\pi/4)|\}.
\]
For each generic view \(0<b<a\) and \(0<\beta<1/2\), the density of \(Z\) has exactly four divergent caustics, at \(\pm s\) and \(\pm h\) with \(s=a+b\) and \(h=a-b\), and is smooth elsewhere in its support. Equivalently, \(s=R\max(|\cos\phi|,|\sin\phi|)\) and \(h=R\min(|\cos\phi|,|\sin\phi|)\). Write \(B_\beta=B(1/2,\beta)\). Then
\[
p_Z(z)\sim C_{\rm out}(s-|z|)^{2\beta-1}\quad (|z|\uparrow s),\qquad
p_Z(z)\sim C_{\rm in}|z\mp h|^{2\beta-1}\quad (z\to\pm h),
\]
where each inner limit holds on both sides and
\[
C_{\rm out}=\frac{2^{2\beta-2}B(\beta,\beta)}{(ab)^\beta B_\beta^2},\qquad
C_{\rm in}=\frac{2^{2\beta-2}B(\beta,1-2\beta)}{(ab)^\beta B_\beta^2},\qquad
\frac{C_{\rm in}}{C_{\rm out}}=\frac{1}{2\cos(\pi\beta)}.
\]
The measured locations and ratio determine \(\beta,R\), and the viewing angle modulo the dihedral symmetries of the propulsion square:
\[
a=\frac{s+h}{2},\quad b=\frac{s-h}{2},\quad R=\sqrt{s^2+h^2},\quad
\beta=\frac{1}{\pi}\arccos\!\left(\frac{C_{\rm out}}{2C_{\rm in}}\right),\quad
\frac{b}{a}=\frac{s-h}{s+h}.
\]
The angle relative to the rotated axes has representative \(\arctan(b/a)\in(0,\pi/4)\).

At \(\beta=1/2\) and \(0<b<a\), each inner density is \(\frac{1}{2\pi^2\sqrt{ab}}\log(1/|z\mp h|)+O(1)\) (with any fixed length scale inside the logarithm), and the outer one-sided limit is \(1/(2\pi\sqrt{ab})\). For \(\beta>1/2\) the inner density limits are finite and the outer endpoint limits are zero. If \(a=b>0\), the inner caustics merge at zero and the two leading divergent contributions add. Neither \(a=b\) nor \(b=0\) belongs to the four-location inverse theorem.

## Assumptions and scope

There is no translational Brownian diffusion, resetting, or inertia. Each allowed turn has rate \(\gamma\) (total orientation jump rate \(2\gamma\)). Observations are in the unique stationary law. The boundary statements concern density limits, not whether there are other finite local modes.

## Proof

Use orthonormal coordinates \(U=(X+Y)/\sqrt2\), \(V=(X-Y)/\sqrt2\). Each projected propulsion component is a sign times \(v_0/\sqrt2\). For any sign pair, one permitted quarter-turn flips the first sign and the other flips the second. Equal per-transition rates therefore give the generator of two independent two-state sign chains, each flipping at rate \(\gamma\). With the stable linear filter defining stationary positions, this makes \(A=\sqrt2\,U/R\) and \(B=\sqrt2\,V/R\) independent. Each normalized variable follows the one-dimensional dynamics \(\dot u=\mu(\sigma-u)\) with sign \(\sigma\). Its stationary total density is
\[
f_\beta(u)=\frac{(1-u^2)^{\beta-1}}{B_\beta}\mathbf 1_{(-1,1)}(u).
\]
Indeed the stationary forward equations for the two conditional state-resolved densities \(g_\pm\) give zero total flux, so \((1-u)g_+=(1+u)g_-\). Writing \(f=g_++g_-\) in either equation yields \(((1-u^2)f)'=-2\beta u f\). The normalized solution above, with vanishing endpoint fluxes, gives an invariant law; uniqueness follows by expressing the stable coordinates as exponentially weighted integrals of the unique stationary sign chains. The rotating basis yields projection coefficients \((R/\sqrt2)\cos(\phi-\pi/4)\) and \(-(R/\sqrt2)\sin(\phi-\pi/4)\), so reflections and exchange of the independent variables give \(Z\stackrel d=aA+bB\). Also \(a^2+b^2=R^2/2\), yielding the displayed inversion for \(R\).

The pushforward density has support \([-s,s]\). Its defining integral over the square \([-1,1]^2\) is over the line \(au+bv=z\) with the Jacobian of either coordinate eliminated. Away from line hits at a corner, a local partition uses either smooth interior factors or a single integrable endpoint factor of exponent \(\beta-1>-1\). In the latter neighborhoods one integrates using the endpoint coordinate as the fixed integration variable; the other factor is smooth with bounded derivatives locally in \(z\). Differentiating there establishes smoothness away from the four corner values.

At \(z=s-\varepsilon\), coordinates \(U_1=1-u\), \(V_1=1-v\) give \(aU_1+bV_1=\varepsilon\). The two density factors have respective leading terms \(2^{\beta-1}U_1^{\beta-1}/B_\beta\) and \(2^{\beta-1}V_1^{\beta-1}/B_\beta\), with uniform relative error tending to zero on that line segment. The Jacobian and scaling yield the convolution integral prefactor \((ab)^{-\beta}\varepsilon^{2\beta-1}\) times \(\int_0^1 t^{\beta-1}(1-t)^{\beta-1}\,dt=B(\beta,\beta)\). This yields \(C_{\rm out}\), and by reflection the negative endpoint. It also yields the critical and higher-rate endpoint limits.

At \(z=h+\delta\) use \(U_1=1-u\), \(V_1=1+v\) at the applicable corner, so \(bV_1-aU_1=\delta\). Write \(x=aU_1\) and \(bV_1=x+\delta\) if \(\delta>0\); for \(\delta<0\) exchange the roles of the two scaled coordinates. After factoring out \(2^{2\beta-2}(ab)^{-\beta}/B_\beta^2\), the local integrand has leading part \(x^{\beta-1}(x+|\delta|)^{\beta-1}\), multiplied by a bounded smooth factor equal to one at the corner. At subcritical \(\beta\), scaling \(x=|\delta|t\) and dominated convergence give coefficient integral
\[
\int_0^\infty t^{\beta-1}(1+t)^{\beta-1}\,dt=B(\beta,1-2\beta).
\]
It is integrable at zero because \(\beta>0\) and at infinity because \(2\beta-2<-1\). At the critical point the integral up to any fixed small \(L>0\) equals \(2\operatorname{arsinh}\sqrt{L/|\delta|}\) with the smooth factor set to one. Restoring the smooth factor changes it by a bounded amount, since the error is \(O(x+|\delta|)\). This gives the logarithmic coefficient. Above threshold, in the same unscaled integral an integrable majorant is a constant times \(x^{2\beta-2}\) for \(1/2<\beta<1\), or a constant times \(x^{\beta-1}\) for \(\beta\ge1\). The contribution away from the corner is smooth locally and hence bounded. Reflection gives the other inner point; when \(a=b\) the two disjoint corner neighborhoods contribute at the same location and add.

Euler reflection gives
\[
\frac{B(\beta,1-2\beta)}{B(\beta,\beta)}=
\frac{\Gamma(2\beta)\Gamma(1-2\beta)}{\Gamma(\beta)\Gamma(1-\beta)}=
\frac{\sin(\pi\beta)}{\sin(2\pi\beta)}=\frac1{2\cos(\pi\beta)}.
\]
This is strictly increasing for \(0<\beta<1/2\), and the locations give the stated geometric inversion. The ratio and exponent are sharp ideal-law quantities; practical recovery from noisy estimates of the density is not asserted.

## Verification

Run `python3 CHECK.py` using Python 3 and `mpmath`. It checks two physical projection geometries against the four projected cardinal vertices, four reflection ratios, 24 subcritical density comparisons near the caustics, and six critical logarithmic-increment or endpoint comparisons. For example, \(R=1\), \((\cos\phi,\sin\phi)=(4/5,3/5)\) gives \((a,b)=(7/10,1/10)\) and caustics at \(\pm4/5,\pm3/5\). Finite quadrature is corroborative; the quantified result follows from the proof.

## Relationship to prior work

Smith, Le Doussal, Majumdar and Schehr establish the full two-dimensional stationary beta-product law and its rotated-coordinate independence, including the special Cartesian marginal in Appendix B. Their equation (10) writes the physical speed as \(\sqrt2\) times their parameter denoted \(v_0\); here \(v_0\) is the physical speed itself. Their equations (18)–(23) thus have rotated half-width \(R/\sqrt2\) in the present notation. Basu, Majumdar, Rosso, Sabhapandit and Schehr establish the related special Cartesian projection via a three-state kinetic model; their rate parameter is the total turn rate, and their critical origin logarithm corresponds to \(\beta=1/2\) in the merged case \(a=b\). Neither the product law nor the axis case is claimed here as new. The claim concerns the distinct generic projections, their two-sided inner and outer leading coefficients, and the resulting exact single-view calibration. The known product law is the starting point of the calculation rather than a new stationary law.

## Limitations

The four divergent locations and inverse reconstruction are restricted to an athermal stationary law, a generic view, equal per-direction turning rates and \(0<\beta<1/2\). Diffusion smooths the caustics. Without separately knowing \(\mu\), \(\gamma\) and \(v_0\) are not separately identified from \(\beta\) and \(R\). No finite-data performance or global unimodality statement is made.

## References

- N. R. Smith, P. Le Doussal, S. N. Majumdar, G. Schehr, *Exact position distribution of a harmonically-confined run-and-tumble particle in two dimensions*, https://arxiv.org/abs/2207.10445.
- U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit, G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, https://arxiv.org/abs/1910.10083.
