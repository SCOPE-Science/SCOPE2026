# Exact radial occupation and sharp moment transition at a nonhomogeneous quartic rigid center

## Finding
For fixed \(a>0\) and \(b>0\), consider the planar polynomial differential equation
\[
\dot x=-y+x^2\bigl(b+a(x^2+y^2)\bigr),\qquad
\dot y=x+xy\bigl(b+a(x^2+y^2)\bigr).
\]
This is a nonhomogeneous quartic rigid flow. In polar coordinates \(r>0\), \(\theta\in\mathbb R/2\pi\mathbb Z\), define
\[
J(r)=\frac{\sqrt a}{b^{3/2}}\left(w-\arctan w\right),\qquad
w=\frac{\sqrt{b/a}}r.
\]
The quantity \(C=J(r)+\sin\theta\) is conserved. Its levels with \(C>1\) are precisely the noncentral complete periodic orbits; each has least original-time period \(2\pi\). Write \(C=1+\delta\), where \(\delta>0\), and sample the radial coordinate \(R_\delta\) at a uniformly random *physical time* on the orbit.

Set \(G(y)=0\) for \(y\le0\), \(G(y)=\arccos(1-y)/\pi\) for \(0<y<2\), and \(G(y)=1\) for \(y\ge2\). For **every** \(r>0\) and \(\delta>0\), its exact survival function is
\[
\boxed{\Pr(R_\delta>r)=G\bigl(J(r)-\delta\bigr).}
\]
As \(\delta\downarrow0\), these distributions converge to a finite almost-sure random radius \(R_0\) with survival \(G(J(r))\), and
\[
\boxed{\Pr(R_0>r)\sim\frac1\pi\sqrt{\frac{2}{3a}}\,r^{-3/2}}
\qquad(r\to\infty).
\]
In particular, the heavy-tail coefficient is independent of the lower-order coefficient \(b\). For every fixed real \(p>0\), define \(M_p(\delta)=\mathbb E[R_\delta^p]\). Then the full moment trichotomy is
\[
\boxed{\begin{aligned}
0<p<3/2:&\quad M_p(\delta)\longrightarrow \mathbb E[R_0^p]<\infty,\\
p=3/2:&\quad M_{3/2}(\delta)=\frac{\log(1/\delta)}{\pi\sqrt{6a}}+O_{a,b}(1),\\
p>3/2:&\quad M_p(\delta)\sim
\frac{(3a)^{-p/3}}{\sqrt{2\pi}}
\frac{\Gamma(p/3-1/2)}{\Gamma(p/3)}\,
\delta^{1/2-p/3}.
\end{aligned}}
\]
The limits hold as \(\delta\downarrow0\) with \(a,b,p\) fixed. Thus the positive moments of the limiting radius are finite **exactly** below order \(3/2\). In particular, the enclosed Euclidean orbit area \(\mathcal A_\delta=\pi M_2(\delta)\) obeys
\[
\boxed{\mathcal A_\delta\sim
\sqrt{\frac\pi2}\,(3a)^{-2/3}
\frac{\Gamma(1/6)}{\Gamma(2/3)}\,\delta^{-1/6}.}
\]

## Assumptions and scope
The coefficients satisfy \(a,b>0\); no positivity restrictions are imposed on the Cartesian state \((x,y)\). The origin is the unique equilibrium, and the theorem concerns noncentral periodic levels. The random variable \(R_\delta\) is the radius of a point chosen uniformly along *original physical time*, not by Euclidean area and not along an artificial clock. All asymptotic parameters are explicit: the orbit label is the difference \(\delta=C-1>0\) from the sharp periodicity boundary, and \(a,b\) remain fixed. The result does not claim phase-space mixing or stochastic forcing; randomness is solely the selection of orbital sampling time.

## Proof
**1. Exact first integral and dynamical boundary.** Direct polar differentiation yields
\[
\dot\theta=1,\qquad \dot r=r^2(b+ar^2)\cos\theta.
\]
Because
\[
J'(r)=-\frac{1}{r^2(b+ar^2)},
\]
we have \(d(J(r)+\sin\theta)/dt=-\cos\theta+\cos\theta=0\). The function \(J:(0,\infty)\to(0,\infty)\) is a strictly decreasing bijection, with \(J(r)\to\infty\) as \(r\downarrow0\) and \(J(r)\to0\) as \(r\to\infty\). Thus an orbit of level \(C\) is exactly
\[
r(\theta)=J^{-1}(C-\sin\theta)
\]
for as long as \(C-\sin\theta>0\). The initial condition enforces \(C>-1\). If \(C>1\), the inverse is defined at all angles, and angular speed one makes the orbit complete and periodic with least period \(2\pi\). If \(-1<C\le1\), the argument reaches zero at a finite future angle, and \(r\to\infty\) in finite original time; hence there are no other noncentral complete periodic orbits.

**2. Exact occupation.** On level \(C=1+\delta\), let \(U\) be uniform on \([0,2\pi)\). Since \(\dot\theta=1\), the law of a random physical-time radius is exactly
\[
R_\delta=J^{-1}(\delta+1-\sin U).
\]
For \(0<y<2\), uniform angular measure gives
\[
\Pr(1-\sin U<y)=\frac{\arccos(1-y)}\pi.
\]
Because \(J^{-1}\) is decreasing, \(R_\delta>r\) precisely when \(1-\sin U<J(r)-\delta\). This gives the complete piecewise survival formula. The support is the compact interval
\[
\bigl[J^{-1}(\delta+2),J^{-1}(\delta)\bigr],
\]
and in its interior the density can, if desired, be differentiated as
\[
f_\delta(r)=\frac{1}{\pi r^2(b+ar^2)
\sqrt{(J(r)-\delta)(2-J(r)+\delta)}}.
\]
For each angle except the unique maximum of \(\sin U\), the radii \(R_\delta\) increase to a finite value \(R_0\) as \(\delta\downarrow0\), proving almost-sure and hence distributional convergence under the common phase coupling.

**3. Sharp limiting tail.** Taylor expansion of \(\arctan w\) at zero gives
\[
J(r)=\frac{1}{3ar^3}-\frac{b}{5a^2r^5}+O_{a,b}(r^{-7}),
\qquad r\to\infty.
\]
The elementary expansion \(\arccos(1-y)=\sqrt{2y}\,[1+O(y)]\) as \(y\downarrow0\) implies
\[
G(J(r))=\frac{1}{\pi}\sqrt{\frac{2}{3a}}\,r^{-3/2}
\left(1+O_{a,b}(r^{-2})\right).
\]
The tail integral identity \(\mathbb E[R_0^p]=p\int_0^\infty r^{p-1}\Pr(R_0>r)\,dr\) then gives precisely the moment threshold \(p=3/2\). For \(p<3/2\), monotone convergence in the coupling of step 2 gives \(M_p(\delta)\uparrow\mathbb E[R_0^p]\).

**4. Uniform inverse approximation.** Inverting the expansion of \(J\) near zero yields, for \(z\downarrow0\),
\[
\bigl(J^{-1}(z)\bigr)^p=(3az)^{-p/3}
\bigl(1+O_{a,b,p}(z^{2/3})\bigr).
\]
Set \(\phi=U-\pi/2\), modulo \(2\pi\), and note \(1-\sin U=1-\cos\phi=\phi^2/2+O(\phi^4)\). Away from \(\phi=0\), all moments have uniformly bounded contributions as \(\delta\downarrow0\).

**5. Power-divergent moments.** If \(p>3/2\), put \(q=p/3>1/2\) and rescale \(\phi=\sqrt{2\delta}\,t\) in the local integral for \(M_p\). The normalized integrand converges pointwise to \((1+t^2)^{-q}\). A bound by a constant multiple of \((1+t^2)^{-q}\) follows from the positive quadratic comparison \(c_1\phi^2\le1-\cos\phi\le c_2\phi^2\) on a fixed neighborhood, together with the two-sided inverse-power bounds of step 4. Dominated convergence gives
\[
M_p(\delta)\sim\frac{(3a)^{-p/3}}{2\pi}\sqrt2\,
\delta^{1/2-p/3}\int_{-\infty}^{\infty}(1+t^2)^{-q}\,dt.
\]
The integral equals \(\sqrt\pi\,\Gamma(q-1/2)/\Gamma(q)\). This proves the stated explicit constant for every fixed \(p>3/2\).

**6. Logarithmic boundary case.** For \(p=3/2\), the contribution of a fixed small neighborhood of \(\phi=0\) is
\[
\frac{(3a)^{-1/2}}{2\pi}
\int_{-\eta}^{\eta}(\delta+\phi^2/2)^{-1/2}\,d\phi
+O_{a,b,\eta}(1).
\]
The error is uniformly bounded: the inverse-function remainder is dominated by \(O(z^{1/6})\), and replacing \(1-\cos\phi\) by \(\phi^2/2\) changes the singular integrand by an integrable \(O(|\phi|)\). The displayed integral equals \(\sqrt2\log(1/\delta)+O_\eta(1)\). Multiplication produces the coefficient \(1/(\pi\sqrt{6a})\).

**7. Area corollary.** Each finite-\(\delta\) orbit is a positive radial graph over the angular circle, so its enclosed Euclidean area is \(\frac12\int_0^{2\pi}r(\theta)^2\,d\theta=\pi M_2(\delta)\). Apply step 5 at \(p=2\) and simplify. This yields the stated exact area-divergence coefficient.

## Verification
A standalone standard-library checker, `verify_rigid_occupation.py`, verifies the derivative of \(J\) against the exact radial vector field at multiple positive parameter choices, numerically inverts \(J\), and tests the invariant along representative periodic states. It checks the limiting survival prefactor at two large radii and verifies the predicted \(p=2\) power scale and \(p=3/2\) logarithmic increment using fixed-angle midpoint quadrature. Execution from the standalone package produces `RIGID_QUARTIC_OCCUPATION_MOMENTS_OK`. The checker is a finite reproducibility aid and not a proof of the universal or asymptotic assertions; the proof is given above. The differential identity was independently simplified to zero in symbolic algebra before packaging.

## Relationship to prior work
Álvarez, Bravo and Calderón [1] introduce and analyze the general quartic rigid polynomial family containing the present nonhomogeneous reversible system, including its polar reduction and qualitative center criteria. Those are prior results, as are general isochronicity and phase-portrait classifications. Itikawa and Llibre [2] classify global phase portraits of nonhomogeneous quartic isochronous centers; this topological classification does not by itself specify the physical-time radial sampling law or the sharp full moment spectrum. Their complete article was not obtained for line-by-line comparison, and an unstated computation there remains a priority risk. Their homogeneous quartic classification [3] is also related but does not specialize to \(b>0\).

The public result [4] determines sharp Euclidean area-growth powers of the **entire periodicity basin** and critical original-time blow-up exponents for homogeneous cubic radial nonlinearities only (zero linear term). Its proof uses \(r^{-3}\) as a radial variable and does not state the nonhomogeneous exact phase-sampled survival or moment transition. The present radial variable \(J(r)\) is instead nonhomogeneous, the measured object is one orbit's distribution under its original physical clock, and the distinct, explicit gamma-function moment constants are not entailed by the homogeneous basin-area result. A separate time-sampling law [5] treats a different cubic global center with a different moment threshold. Searches for inverse-Abel, time-occupation, critical-orbit radial moments, and analogous reparameterizations found no statement covering this exact theorem; search absence is not treated as proof of priority.

## Limitations
Only the two-parameter strictly positive coefficient subfamily \(F(x,y)=x\bigl(b+a(x^2+y^2)\bigr)\) is addressed. The result is a deterministic orbital sampling theorem, not a claim about noisy trajectories or arbitrary invariant probability measures. The moment coefficients are for the chosen invariant label \(\delta=C-1\), not an unspecified geometric distance to the boundary. The underlying center and polar reduction are previously known. The complete 2015 nonhomogeneous phase-portrait paper was not accessible for full-text inspection, and unindexed equivalent calculations remain possible. No independent mathematical audit has been performed.

## References
1. M. J. Álvarez, J. L. Bravo, L. A. Calderón, *Quartic Rigid Systems in the Plane and in the Poincaré Sphere*, arXiv:2310.05509, first submitted 2023-10-09, https://arxiv.org/abs/2310.05509; *Qualitative Theory of Dynamical Systems* 23 (2024), article 226, https://doi.org/10.1007/s12346-024-01083-z (open full article).
2. J. Itikawa, J. Llibre, *Phase portraits of uniform isochronous quartic centers*, *Journal of Computational and Applied Mathematics* 287 (2015), 98–114, https://doi.org/10.1016/j.cam.2015.02.046 (abstract and bibliographic description inspected; full text not obtained).
3. J. Itikawa, J. Llibre, *Global phase portraits of uniform isochronous centers with quartic homogeneous polynomial nonlinearities*, *Discrete and Continuous Dynamical Systems B* 21 (2016), 121–131, https://doi.org/10.3934/dcdsb.2016.21.121.
4. *Two sharp area-growth exponents at quartic rigid isochronous centers* (2026), public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-two-sharp-area-growth-exponents-at-quartic-rigid-isochronous-cen--b12cd55905aa .
5. *Cauchy time concentration and the order-one moment threshold in a cubic global center* (2026), public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-cauchy-time-concentration-and-the-order-one-moment-threshold-in--0ac06783efe2 .
