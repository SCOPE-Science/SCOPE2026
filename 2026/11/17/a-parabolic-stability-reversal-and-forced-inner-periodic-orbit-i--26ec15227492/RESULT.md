# A parabolic stability reversal and forced inner periodic orbit in a quartic Kukles flow

## Finding
Consider, for every real parameter \(t>0\), the quartic polynomial vector field
\[
\dot x=-y,\qquad \dot y=x+t\,y(x^2+y^2-1)(x+y). \tag{1}
\]
Its unit circle \(\mathcal C=\{x^2+y^2=1\}\) is periodic with original-time period exactly \(2\pi\), and its nontrivial Floquet multiplier equals \(1\) for every \(t\). Define the positive-crossing section \(\{(x,0):x>0\}\) and its local one-turn map \(P_t\) in the coordinate \(s=x^2-1\). For each fixed \(t>0\), this map exists on a sufficiently small interval about \(s=0\) and satisfies
\[
P_t(s)=s+K(t)s^2+O_t(s^3),\qquad
K(t)=-2t^2\int_0^{2\pi}\sin^3\theta\cos\theta(\sin\theta+\cos\theta)^2\exp(tH(\theta))\,d\theta, \tag{2}
\]
where
\[
H(\theta)=\frac23\sin^3\theta+2\left(-\cos\theta+\frac13\cos^3\theta+\frac23\right). \tag{3}
\]
The coefficient \(K\) is continuous and obeys the two sharp asymptotics
\[
K(t)=-\frac\pi2t^2+O(t^3)\quad(t\downarrow0),\qquad
K(t)\sim2^{-1/4}\sqrt\pi\,t^{1/2}\exp\left[(\frac43+\sqrt2)t\right]\quad(t\to\infty). \tag{4}
\]
Consequently there exist \(0<t_{\mathrm{small}}<t_{\mathrm{large}}<\infty\) such that for all sufficiently small positive \(t\), the unit circle attracts locally from its exterior and repels from its interior, whereas for all sufficiently large \(t\), these two one-sided behaviors are reversed, despite its unchanging unit Floquet multiplier. At least one parameter between these regimes satisfies \(K(t)=0\); no uniqueness or higher-order multiplicity at those parameters is asserted.

**Forced inner recurrence.** For every sufficiently large \(t\), (1) has at least one additional periodic orbit strictly inside \(\mathcal C\). In particular, the invariant circle is not the only periodic orbit of (1) in the plane in this regime. No uniqueness, hyperbolicity or exact location of the additional orbit is claimed.

## Assumptions and scope
The parameter \(t\) is real and strictly positive. Time is the physical time of (1), without rescaling. The section is crossed with increasing \(y\); \(s=x^2-1\) is signed squared-radius displacement, not the ordinary radius. Statements about \(P_t\) are local near the circle and their error constants may depend on fixed \(t\). The additional periodic orbit is asserted for all sufficiently large \(t\), without an explicit numerical cutoff. The circle and the origin are the only *a priori* exhibited invariant sets; the existence proof below supplies the other periodic orbit without counting all others.

## Proof
**Exact circle and multiplier.** For \(s=x^2+y^2-1\), direct differentiation gives
\[
\dot s=2t\,s y^2(x+y). \tag{5}
\]
Thus \(s=0\) is invariant. On it, the dynamics is precisely \((\dot x,\dot y)=(-y,x)\), so it traverses once in \(2\pi\). The normal multiplier is
\[
\mu_t=\exp\!\left[2t\int_0^{2\pi}\sin^2\theta(\sin\theta+\cos\theta)\,d\theta\right]=1, \tag{6}
\]
since the two trigonometric integrals vanish.

**Second return variation.** Put \(x=\sqrt{1+s}\cos\theta\), \(y=\sqrt{1+s}\sin\theta\), and \(B(\theta)=\sin\theta+\cos\theta\). The angular velocity and radial equation are exactly
\[
\dot\theta=1+t\,s\sqrt{1+s}\sin\theta\cos\theta B(\theta),\quad
\dot s=2t\,s(1+s)^{3/2}\sin^2\theta B(\theta). \tag{7}
\]
For each fixed \(t\), \(\dot\theta>0\) in a collar of the unit circle. Division and Taylor expansion give, uniformly in \(\theta\),
\[
\frac{ds}{d\theta}=L_t(\theta)s+Q_t(\theta)s^2+O_t(s^3),\quad
L_t=2t\sin^2\theta B,\quad
Q_t=3t\sin^2\theta B-2t^2\sin^3\theta\cos\theta B^2. \tag{8}
\]
Let \(h(\theta)=\exp(tH(\theta))\). Since \(H'=2\sin^2\theta B\), the first variation is \(s(\theta)=h(\theta)s_0+O_t(s_0^2)\). Moreover \(H(0)=H(2\pi)=0\), and variation of constants gives the quadratic coefficient
\[
K(t)=\int_0^{2\pi} Q_t(\theta)h(\theta)\,d\theta. \tag{9}
\]
Here the \(3t\sin^2\theta B\) part integrates to \(\frac32\int_0^{2\pi}h'(\theta)\,d\theta=0\), proving (2). The integral defines a continuous, indeed real-analytic, function of \(t\).

**Small coupling.** The integral at zero exponent is exact:
\[
\int_0^{2\pi}\sin^3\theta\cos\theta(\sin\theta+\cos\theta)^2\,d\theta=\frac\pi4. \tag{10}
\]
Dominated Taylor expansion in (2) yields the first part of (4).

**Strong coupling.** The only zeros of \(H'=2\sin^2\theta(\sin\theta+\cos\theta)\) on the circle occur at \(\theta=0,\pi,3\pi/4,7\pi/4\) (with endpoints identified). Comparing values and monotonicity intervals shows that the **unique global maximum** is \(\theta_*=3\pi/4\); there
\[
H_*=H(\theta_*)=\frac43+\sqrt2,\qquad H''(\theta_*)=-\sqrt2. \tag{11}
\]
Let \(\delta=\theta-\theta_*\). The signed amplitude in (2) has the local expansion
\[
-2\sin^3\theta\cos\theta B(\theta)^2=\delta^2+O(\delta^3). \tag{12}
\]
The usual Laplace method with a quadratic-zero amplitude (dominated Gaussian rescaling \(u=\sqrt t\,\delta\) and exponential suppression away from the unique maximum) gives
\[
K(t)\sim t^2e^{tH_*}\int_{-\infty}^{\infty}\delta^2e^{-(\sqrt2/2)t\delta^2}\,d\delta
=2^{-1/4}\sqrt\pi\,t^{1/2}e^{tH_*}. \tag{13}
\]
This proves eventual positivity without assuming a numerical quadrature or an unproved threshold. Together with eventual negativity and continuity, the intermediate value theorem gives at least one zero of \(K\). The sign of \(K\) determines the direction of displacement \(P_t(s)-s\) for both signs of sufficiently small \(s\), establishing the one-sided reversal.

**An attracting origin and an interior periodic orbit.** The origin is the only equilibrium: \(\dot x=0\) forces \(y=0\), then \(\dot y=x=0\). In ordinary radius \(r\) near the origin, the angular equation has \(\dot\theta=1+O_t(r)\) and
\[
\frac{dr}{d\theta}=-t r^2\sin^2\theta B(\theta)-t^2r^3\sin^3\theta\cos\theta B(\theta)^2+O_t(r^4). \tag{14}
\]
The first-order scalar field has zero integral over a revolution, and its self-interaction in the cubic return coefficient vanishes because it is the square of that zero mean. Equation (10) therefore gives the origin's radial return map
\[
r_{\mathrm{next}}=r-\frac\pi4t^2r^3+O_t(r^4). \tag{15}
\]
Thus for every fixed \(t>0\) the origin is locally asymptotically stable. For all sufficiently large \(t\), \(K(t)>0\), so (2) makes the unit circle locally asymptotically attracting **from its interior**. The open disk is invariant under the flow (orbits cannot cross its invariant boundary), and trajectories there remain bounded and exist for all positive and negative times. Inside the disk there are then two disjoint nonempty open forward basins: the origin basin and the collar attracted to the circle. The boundary of the origin basin relative to the disk is nonempty, invariant, compactly separated from both the origin (which has an attracting neighborhood) and the unit circle (which has an interior attracting collar), and contains no equilibrium. Choosing any point on this boundary, its nonempty omega-limit set is compact and contains no equilibrium. The planar Poincaré–Bendixson theorem implies that omega-limit set is a periodic orbit wholly in the open unit disk. This is the asserted additional orbit.

## Verification
The supplied standalone Python script \(\texttt{verify.py}\) checks the polynomial cofactor, Taylor algebra, the exact trigonometric moment in (10), the critical-point and local-amplitude identities, and numerical values of (2) at representative coupling strengths. Only (5), (7)–(15), continuity and the planar trapping argument prove the infinite and all-parameter claims. Finite quadrature does **not** establish eventual positivity or an exhaustive periodic-orbit count. Run \(\texttt{python verify.py}\) using Python with SymPy and mpmath installed.

## Relationship to prior work
J. Mujica, *Small- and large-amplitude limit cycles in Kukles systems with algebraic invariant curves* (arXiv:2201.03264v1, publicly released 10 January 2022), Section 4, studies the three-parameter family \(\dot y=x+y(x^2+y^2-1)(ax+by+c)\). Its Lemma 4.1 supplies the invariant circle and Theorem 4.4 studies the origin's weak-focus stability. Its Theorem 4.7 states exactly one limit cycle for nonzero \(a,b\), based on a second-order Melnikov calculation; the analysis there does not give the exact finite-coupling parabolic return coefficient, its strong-coupling Laplace law, or the consequent second periodic orbit. The asserted uniqueness should not be inferred globally from a finite-order perturbative calculation. Our claim of a second **periodic orbit** is made without assuming all its possible isolation or multiplier properties. The related published published-finding corpus result *Polar Dulac rigidity and exact multiplicity of an invariant circle* (2026-10-11) concerns a different coupled-radius angular form \(\dot S=2S(1-S)U(\theta),\ \dot\theta=SU(\theta)-V(\theta)\) with sign-definite quadratic displacement; (7) has nontrivial square-root radial dependence in both equations and exhibits both signs of its second return coefficient. No implication from that theorem to the present strong-coupling reversal has been identified.

## Limitations
The theorem does not specify the first zero of \(K\), its uniqueness, the multiplicity at its zeros, the number of additional periodic orbits, or their hyperbolicity. The existence statement requires sufficiently large positive \(t\) without a numerical threshold. The published 1987 work of Gasull–Llibre–Sotomayor on vector fields of the form \(Av+f(v)Bv\) is structurally relevant but its complete text was unavailable for this comparison; a stronger prior result or an equivalent unpublished derivation remains a publication-priority risk. Independent external mathematical validation has not been performed.

## References
1. J. Mujica, *Small- and large-amplitude limit cycles in Kukles systems with algebraic invariant curves*, arXiv:2201.03264v1 (10 January 2022), especially Section 4, https://arxiv.org/html/2201.03264v1 .
2. A. Gasull, J. Llibre, J. Sotomayor, *Limit cycles of vector fields of the form \(X(v)=Av+f(v)Bv\)*, Journal of Differential Equations 67 (1987), 90–110. Full text not inspected.
3. *Polar Dulac rigidity and exact multiplicity of an invariant circle*, published-finding corpus record 2026/10/11/SCOPE-polar-dulac-rigidity-and-exact-multiplicity-of-an-invariant-circ--a6f982503591, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-polar-dulac-rigidity-and-exact-multiplicity-of-an-invariant-circ--a6f982503591 .
