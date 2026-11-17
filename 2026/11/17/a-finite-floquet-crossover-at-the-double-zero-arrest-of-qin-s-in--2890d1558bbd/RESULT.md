# A finite Floquet crossover at the double-zero arrest of Qin's invariant circle

## Finding
Consider Qin's quadratic planar flow
\[
\dot x=-y(ax+by+c)-(x^2+y^2-1),\qquad \dot y=x(ax+by+c).
\]
Fix any \(b>0\). For \(\varepsilon>0\) and \(\kappa\in\mathbb R\), set
\[
a=\kappa\sqrt\varepsilon,\quad R=\sqrt{a^2+b^2},\quad c=R+\varepsilon,\quad\Delta=\sqrt{c^2-R^2}.
\]
The invariant circle \(\Gamma=\{x^2+y^2=1\}\) is a periodic orbit with exact original-time minimal period and nontrivial transverse Floquet multiplier
\[
T=\frac{2\pi}{\Delta},\qquad
\mu=\exp\!\left(\frac{4\pi a}{\Delta(c+\Delta)}\right).
\]
As \(\varepsilon\downarrow0\), the *simultaneous* period and multiplier limits are
\[
\boxed{\sqrt\varepsilon\,T\longrightarrow\frac{2\pi}{\sqrt{2b}},\qquad
\mu\longrightarrow\exp\left(\frac{4\pi\kappa}{b\sqrt{2b}}\right).}
\]
Thus unbounded physical periods coexist with arbitrary prescribed positive limiting multiplier as \(\kappa\) ranges over \(\mathbb R\): attracting for \(\kappa<0\), repelling for \(\kappa>0\), and exactly neutral for \(\kappa=0\). At \(\kappa=0\) the circle is part of a local period annulus, not an isolated neutral cycle.

There is an accompanying universal occupation law. Write \(a=R\cos\phi\), \(b=R\sin\phi\) with \(0<\phi<\pi\), and put \(u=\operatorname{wrap}_{(-\pi,\pi)}(\theta-\phi-\pi)\), where \((x,y)=(\cos\theta,\sin\theta)\) on the circle. If a phase point is chosen uniformly in the **original physical time** along \(\Gamma\), then
\[
\boxed{u\sqrt{\frac{R}{2\varepsilon}}\ \xrightarrow{d}\ \operatorname{Cauchy}(0,1).}
\]
At \(\varepsilon=0\) and \(a=0,c=b\), the circle passes through a double-zero nilpotent equilibrium at \((0,-1)\), with Jacobian \(\left(\begin{smallmatrix}0&b+2\\0&0\end{smallmatrix}\right)\). Its complement in the circle is one nonstationary orbit homoclinic to that equilibrium. This endpoint is outside the periodic regime.

## Assumptions and scope
All parameters are real; \(b>0\) is fixed, \(\kappa\in\mathbb R\) is fixed when taking the limit, and \(\varepsilon>0\). Both \(a\) and \(c\) depend on \(\varepsilon\) as prescribed. No assertion is made for arbitrary paths in the two-parameter plane or for trajectories away from the invariant circle, except the local period annulus when \(\kappa=0\). The phase \(\theta\) is taken modulo \(2\pi\), and \(\mu\) denotes the scalar derivative of the Poincare first-return map transverse to \(\Gamma\), not the trivial tangential multiplier one.

## Proof
1. Put \(f=x^2+y^2-1\). Direct differentiation gives \(\dot f=-2xf\). Thus \(\Gamma\) is invariant. On it, \(\dot\theta=c+a\cos\theta+b\sin\theta=c+R\cos(\theta-\phi)>0\), since \(c>R\). The circle is traversed exactly once in every minimal period.
2. The classical tangent-half-angle integral yields \(T=\int_0^{2\pi}(c+R\cos v)^{-1}dv=2\pi/\Delta\). The normalized original-time phase distribution therefore has density \(\Delta/[2\pi(c+R\cos v)]\). With \(\rho=R/(c+\Delta)\), its Fourier coefficients are \(\mathbb E e^{imv}=(-\rho)^{|m|}\) for every integer \(m\). In particular \(\mathbb E\cos\theta=-a/(c+\Delta)\). These identities also follow by a one-pole contour integral.
3. Since the defining function \(f\) is regular on \(\Gamma\), its variational equation \(\dot{\delta f}=-2\cos\theta(t)\delta f\) gives the transverse Floquet multiplier: \(\log\mu=-2T\mathbb E\cos\theta=2aT/(c+\Delta)=4\pi a/[\Delta(c+\Delta)]\). This establishes the exact expression and the strict stability sign when \(a\ne0\).
4. Along the stated two-parameter path, \(R\to b\), \(c\to b\), and \(\Delta/\sqrt\varepsilon=\sqrt{2R+\varepsilon}\to\sqrt{2b}\). Substitution into the two exact expressions gives both boxed limits. Their ratio also gives \(\log\mu/T=2a/(c+\Delta)\to0\) in this double scaling; the multiplier remains nontrivial because the period diverges.
5. Center the physical-time density at the slowing point \(\theta=\phi+\pi\), so that it becomes \(\Delta/[2\pi(\varepsilon+R(1-\cos u))]\). Set \(z=u\sqrt{R/(2\varepsilon)}\). Its transformed density converges pointwise to \(1/[\pi(1+z^2)]\). On any fixed compact set this convergence is uniform; the mass outside any fixed \([-K,K]\) is uniformly bounded by a multiple of \(1/K\) for all sufficiently small \(\varepsilon\), since \(1-\cos u\ge2u^2/\pi^2\) for \(|u|\le\pi\). Hence the probability laws converge weakly to standard Cauchy.
6. If \(\kappa=0\), then \(a=0\) and \(g=c+by\) is strictly positive in a whole annulus around \(\Gamma\) (because \(c>b\)). The smooth function \(J=f\,g^{2/b}\) is a first integral there: \(\dot g=bxg\), so \(\dot J=0\). Since \(\nabla J\ne0\) along \(\Gamma\), nearby regular levels are closed periodic curves, and the return map is locally the identity.
7. At \((a,c)=(0,b)\), direct differentiation at \((0,-1)\) gives the displayed rank-one nilpotent Jacobian. The angular equation on the circle is \(\dot\theta=b(1+\sin\theta)\), strictly positive except at \(\theta=3\pi/2\), where it has a quadratic zero. Both forward and backward times to this point diverge, proving that the remaining circle is one homoclinic trajectory.

## Verification
The standalone `checker.py` verifies the cofactor identity \(\dot f=-2xf\), the angular identity, the nilpotent Jacobian, both exact integral formulas with 40-digit agreement at a noncritical parameter, and three decreasing parameter scales against the limiting constants. Run `python checker.py` with SymPy and mpmath installed. Its final message is `QIN_DOUBLE_ZERO_CROSSOVER_CHECK_OK`. Finite evaluations are corroborative; proof steps 1–7 establish the quantifiers and infinite limits analytically.

## Relationship to prior work
Qin's classical quadratic invariant circle and its isolated existence conditions predate this result. Giacomini and Grau (2005) established the general cofactor formula for characteristic multipliers and discuss Qin's pre-existing hyperbolicity. Gasull and Giacomini (arXiv:2210.15803, first posted 2022-10-27; published 2023), Section 4, reproduce the Qin family and prove absence of additional limit cycles. The angular restriction is conjugate to the textbook Adler phase oscillator: its single-parameter period divergence and phase concentration are not themselves new. The claim here is the **joint nilpotent/annulus double-scaling classification with its exact transverse multiplier crossover**, which is not a consequence of angular dynamics alone; the planar cofactor and its degeneration must enter simultaneously.

## Limitations
No independent mathematical audit has been performed. The result does not establish a universal codimension-two normal form, off-circle global attraction, convergence rates for the full planar flow, or a classification of other parameter paths. A pre-existing computation of this exact two-parameter Qin crossover outside the inspected literature remains possible. The 1958 Qin original was not available in full and was not used to infer absence of prior calculations.

## References
- A. Gasull and H. Giacomini, *Number of Limit Cycles for Planar Systems with Invariant Algebraic Curves*, arXiv:2210.15803 (first posted 2022-10-27), *Qualitative Theory of Dynamical Systems* 22, article 44 (2023), DOI:10.1007/s12346-023-00746-7, Section 4, Case 1.
- H. Giacomini and M. Grau, *On the stability of limit cycles for planar differential systems*, arXiv:math/0505027 (2005), Section 3, Theorem 6 and the cofactor-multiplier identity; *Journal of Differential Equations* 213 (2005), 368–388.
- Y.-X. Qin (Ch'in Yuan-shun), *On the algebraic limit cycles of second degree of the differential equation*, *Acta Mathematica Sinica* 8 (1958), 23–35; historical model reference identified in the preceding two papers.
