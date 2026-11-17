# Log-periodic backward blow-up and the attracting-cycle amplitude echo in homogeneous star-node flows

## Finding

For a planar polynomial star-node flow with strictly contracting homogeneous nonlinearity and strictly positive angular drift, every orbit outside its unique attracting limit cycle blows up at a **finite backward physical time**. The blow-up has infinitely many turns and a precise type-I profile. Unexpectedly, its phase-resolved amplitude is determined by the *same periodic radial graph* as the forward attracting limit cycle. For all exterior initial points, the scaled amplitude has the same complete interval of accumulation values; changing the starting point changes only its phase on logarithmic time.

The exact statement is as follows. For every integer \(p\ge1\), every \(\lambda>0\), and every homogeneous polynomial vector field \(Q:\mathbb R^2\to\mathbb R^2\) of degree \(2p+1\), suppose
\[
f(\theta)=\langle u_\theta,Q(u_\theta)\rangle<0,\qquad
g(\theta)=\langle Ju_\theta,Q(u_\theta)\rangle>0
\]
for all \(\theta\), where \(u_\theta=(\cos\theta,\sin\theta)\), \(J(x,y)=(-y,x)\). Consider the original physical-time system
\[
\dot z=\lambda z+Q(z).
\]
Define
\[
a(\theta)=\frac{2pf(\theta)}{g(\theta)},\qquad
\rho(\theta)=\exp\!\left(\int_0^\theta a(s)\,ds\right),\qquad
\Lambda=-\int_0^{2\pi}a(s)\,ds>0,
\]
and the positive \(2\pi\)-periodic functions
\[
w_*(\theta)=2p\lambda\rho(\theta)
\int_{-\infty}^\theta\frac{ds}{g(s)\rho(s)},\qquad
K(\theta)=\frac{w_*(\theta)}{2p\lambda}.
\]
The unique attracting periodic orbit has radial graph \(r_*(\theta)=w_*(\theta)^{1/(2p)}\). For an initial polar state \((r_0,\theta_0)\), use a real angular lift and define
\[
C=\frac{r_0^{2p}-w_*(\theta_0)}{\rho(\theta_0)}.
\]
Exactly three cases occur: \(C=0\) gives the periodic orbit; \(C<0\) gives a backward-complete orbit approaching the origin as physical time tends to \(-\infty\); and \(C>0\) gives a unique finite backward endpoint \(t_-\) at which the radius diverges and the angle makes infinitely many clockwise turns.

For every exterior orbit \(C>0\), putting \(\Delta=t-t_-\), one has the **phase-resolved universal law**
\[
\boxed{\ \Delta\,r(t)^{2p}=K(\theta(t))+O(\Delta)\ },\qquad
\theta(t)=\frac{2\pi}{\Lambda}\log\Delta+O(1),
\quad\Delta\downarrow0.
\]
Moreover, \(\Phi(\theta)=\log(K(\theta)/\rho(\theta))\) is a strictly increasing bijection of the real line satisfying \(\Phi(\theta+2\pi)=\Phi(\theta)+\Lambda\). Consequently
\[
\boxed{\ \Delta^{1/(2p)}r(t)=
\mathcal B(\log(C\Delta))+O(\Delta),\qquad
\mathcal B(s)=K(\Phi^{-1}(s))^{1/(2p)}\ },
\]
where \(\mathcal B\) is a positive continuous \(\Lambda\)-periodic function. Its range, independent of initial condition, is exactly
\[
\left[\min_\theta K(\theta)^{1/(2p)},\ \max_\theta K(\theta)^{1/(2p)}\right].
\]
The profile is nonconstant exactly when \(f\) is nonconstant. In that case the scaled radius does **not** converge to one constant: it has genuine logarithmic-phase oscillations.

## Assumptions and scope

All statements concern the autonomous planar real polynomial ODE above, in **unrescaled physical time**. The strict conditions \(f<0\) and \(g>0\) are required on every angle, and the initial state is nonzero. The opposite uniform angular orientation \(g<0\) is equivalent after reversing the angular lift. The graph \(r_*(\theta)\) is measured from the origin and is periodic in \(\theta\), not in a reparametrized clock. No assumption of circular symmetry is made. The logarithmic phase \(\log(C\Delta)\) uses \(\rho(0)=1\) and the given real lift of \(\theta\). A different lift rephases the same periodic function and does not change the theorem or its amplitude range.

The origin is a hyperbolic source in forward time. The periodic orbit divides the punctured plane into two invariant parts. A state is called exterior when \(r_0>r_*(\theta_0)\). The positive constant \(C\) is precisely this exterior condition; negative \(C\) identifies interior states. The temporal big-O constants may depend on the vector field and the exterior initial point but are uniform across all sufficiently negative angular revolutions along that orbit.

## Proof

**1. Exact angular dynamics and periodic graph.** Homogeneity gives the polar system
\[
\dot r=\lambda r+f(\theta)r^{2p+1},\qquad
\dot\theta=g(\theta)r^{2p}.
\]
Since \(g>0\), angle is strictly increasing on every nonzero trajectory. For \(w=r^{2p}>0\), differentiation with respect to angle is exact:
\[
\frac{dw}{d\theta}=
\frac{2p}{g(\theta)}\bigl(\lambda+f(\theta)w\bigr)
=a(\theta)w+\frac{2p\lambda}{g(\theta)}.
\]
Because \(a<0\) is periodic, \(\rho(\theta)\) tends to infinity exponentially as \(\theta\to-\infty\), to zero exponentially as \(\theta\to+\infty\), and satisfies \(\rho(\theta+2\pi)=e^{-\Lambda}\rho(\theta)\). Thus the displayed improper integral for \(w_*\) converges absolutely. Differentiation proves that \(w_*\) solves the angular equation. Periodicity follows by shifting its integral by one full turn. It is positive and bounded above and below away from zero. The difference between any two solutions of the linear angular equation is a constant times \(\rho\), establishing
\[
w(\theta)=w_*(\theta)+C\rho(\theta).
\]
The periodic graph is therefore unique. Every other nonzero orbit converges by successive forward turns to it, recovering the established forward limit cycle.

**2. Backward classification.** The quotient \(w_*(\theta)/\rho(\theta)\) is strictly increasing, as
\[
\frac{d}{d\theta}\frac{w_*}{\rho}
=\frac{2p\lambda}{g(\theta)\rho(\theta)}>0.
\]
It tends to zero as \(\theta\to-\infty\) and to infinity as \(\theta\to+\infty\). For \(C<0\), the unique backward angular endpoint \(\theta_-\) satisfies \(w_*(\theta_-)/\rho(\theta_-)=-C\), and \(w\) has a simple zero there. Since
\[
w(\theta)=\frac{2p\lambda}{g(\theta_-)}(\theta-\theta_-)
+O((\theta-\theta_-)^2),\qquad
\frac{dt}{d\theta}=\frac{1}{g(\theta)w(\theta)},
\]
physical time tends to \(-\infty\) at that zero, and \(r(t)\) approaches zero with asymptotic exponential rate \(\lambda\). At \(C=0\), \(w=w_*\) gives the periodic orbit. For \(C>0\), \(w>w_*>0\) for all backward angles and \(w(\theta)\sim C\rho(\theta)\) as \(\theta\to-\infty\). The integral of \(dt/d\theta=1/(g w)\) over \(( -\infty,\theta_0]\) is finite because \(\rho^{-1}\) decays exponentially there. Thus the backward maximal time is finite, the radius diverges, and there are infinitely many turns as this time is approached. No other nonzero backward behavior is possible.

**3. The periodic amplitude echo.** For an exterior orbit define its exact remaining time from the backward endpoint by
\[
\Delta(\theta)=\int_{-\infty}^\theta
\frac{ds}{g(s)[w_*(s)+C\rho(s)]}.
\]
The first-order expansion of the integrand is uniform for sufficiently negative angles because \(w_*\) is bounded, \(g\) is bounded below and \(\rho(s)\ge\rho(\theta)\) whenever \(s\le\theta\). Moreover the periodic strict negativity of \(a\) gives an exponential integral estimate for the remainder. Hence
\[
\Delta(\theta)=\frac1C\int_{-\infty}^\theta
\frac{ds}{g(s)\rho(s)}+O(\rho(\theta)^{-2})
=\frac{K(\theta)}{C\rho(\theta)}+O(\rho(\theta)^{-2}).
\]
Since \(K\) is bounded above and below by positive constants, \(\Delta=\Theta(\rho^{-1})\). Multiplication by \(w=w_*+C\rho\) yields
\[
\Delta(\theta)w(\theta)=K(\theta)+O(\rho(\theta)^{-1})
=K(\theta)+O(\Delta),
\]
which proves the first boxed law. The leading function is exactly \(w_*/(2p\lambda)\): no separate balance-profile construction is required.

**4. Logarithmic phase and universality.** Define \(\Phi(\theta)=\log(K(\theta)/\rho(\theta))\). Differentiating \(K=w_*/(2p\lambda)\) and using its linear ODE gives
\[
\Phi'(\theta)=\frac{1}{g(\theta)K(\theta)}>0.
\]
This derivative is positive, continuous and periodic; hence \(\Phi\) is a diffeomorphism of the real line onto itself. Its shift is \(\Phi(\theta+2\pi)=\Phi(\theta)+\Lambda\). From the expansion for \(\Delta\),
\[
\log(C\Delta)=\Phi(\theta)+O(\Delta).
\]
Because \(\Phi'\) is bounded away from zero, its inverse is globally Lipschitz. Therefore
\[
\theta=\Phi^{-1}(\log(C\Delta))+O(\Delta).
\]
The smooth periodicity of \(K\) upgrades the first boxed law to the second, with error \(O(\Delta)\) in the rescaled radius. A periodic function of \(\theta\) also shows \(\Phi(\theta)=\Lambda\theta/(2\pi)+O(1)\); inversion proves the exact logarithmic winding coefficient. Every negative infinite angular tail visits every phase infinitely often, so the complete accumulation-value interval is the range of \(\mathcal B\).

**5. Exact criterion for a nonconstant profile.** The profile \(\mathcal B\) is constant if and only if \(K\), equivalently \(w_*\), is constant. If \(w_*\equiv w_0\), the angular differential equation gives \(0=2p(\lambda+f(\theta)w_0)/g(\theta)\), requiring \(f\) to be constant. Conversely, if \(f\equiv-f_0\) with \(f_0>0\), \(w_*\equiv\lambda/f_0\) is the unique periodic solution. Thus any genuine angular variation in radial contraction creates a nonconstant log-periodic blow-up amplitude.

**6. Explicit polynomial witness.** Take any \(\lambda,\omega>0\) and \(0<|\varepsilon|<1\), and set
\[
Q(x,y)=-\bigl[x^2+y^2+\varepsilon(x^2-y^2)\bigr](x,y)
+\omega(x^2+y^2)(-y,x).
\]
Then \(p=1\), \(f(\theta)=-(1+\varepsilon\cos2\theta)<0\), and \(g(\theta)=\omega>0\). The forward attracting orbit is noncircular, and every exterior orbit has a nonconstant log-periodic type-I backward blow-up profile. Because \(f\) has period \(\pi\), the function \(\mathcal B\) has logarithmic period \(2\pi/\omega\), corresponding to half a spatial turn. This example supplies a concrete nontrivial polynomial realization of the oscillatory profile, rather than merely a generic qualitative scenario.

## Verification

The companion `check.py` independently derives the Cartesian radial and angular identities symbolically for the explicit cubic family and evaluates the periodic variation-of-constants integral numerically. It checks the phase-resolved identity \(\Delta r^2\to w_*/(2\lambda)\), the geometric ratio between consecutive half-turn times, positivity and nonconstancy of the periodic graph. Run `python3 check.py` from a directory with `sympy`, `numpy`, and `scipy`; success prints `STAR_NODE_PHASE_BLOWUP_PROFILE_OK`. The finite tests are not used to establish the arbitrary-degree or all-time assertions, which follow from the analytic proof above.

## Relationship to prior work

Alarcón, Castro and Labouriau (2023/2024) established global attraction to an invariant circle and the qualitative division between attracting cycles and equilibrium polycycles for contracting homogeneous star-node systems. Bendjeddou, Llibre and Salhi (2013) already derived the linear angular radial-power reduction and studied integrability and periodic-orbit existence. The previously available exact-angular-return result gives the affine return, original-time forward period, and transverse Floquet multiplier in the strict-rotation subclass. Those forward results, the polar reduction, and the existence and uniqueness of the cycle are **not** claimed as new here.

The new statement concerns **complete backward classification and physical-time scaling**, including the finite backward blow-up of *every* exterior orbit, its universal infinite-turn logarithmic clock, and identification of its nonconstant blow-up amplitude with the specific positive radial graph of the forward attracting cycle. This is stronger than general planar periodic-balance-profile theorems, which address conditional existence or local type-I blow-up without these global initial-condition, angular-phase and amplitude-identification formulas.

## Limitations

The theorem requires everywhere strict radial contraction and nonzero angular drift. It does not address the equilibrium-polycycle regime, points where the angular drift vanishes, nonhomogeneous perturbations or the number of distinct cycles outside this class. The statement gives a full positive continuous periodic profile and exact accumulation range, not an assertion that the scaled radius converges to a single constant unless radial contraction is angle-independent. The logarithmic period \(\Lambda\) is a guaranteed period, not always the minimal one. Absolute publication priority cannot be guaranteed against unpublished or unindexed equivalent arguments, particularly because the underlying angular linearization has long been known. Independent validation has not been performed.

## References

1. B. Alarcón, S. B. S. D. Castro and I. S. Labouriau, *Global planar dynamics with a star node and contracting nonlinearity*, arXiv:2307.16020v1, first publicly available 2023-07-29; published in *Research in the Mathematical Sciences* 11 (2024), article 21, DOI:10.1007/s40687-024-00427-0.
2. B. Alarcón, S. B. S. D. Castro and I. S. Labouriau, *Qualitative planar dynamics with star nodes and homogeneous nonlinearities: beyond Hilbert's 16th problem*, arXiv:2106.07516v1, first publicly available 2021-06-14.
3. A. Bendjeddou, J. Llibre and T. Salhi, *Dynamics of the polynomial differential systems with homogeneous nonlinearities and a star node*, *Journal of Differential Equations* 254 (2013), 3530–3537, DOI:10.1016/j.jde.2013.01.032; author preprint https://ddd.uab.cat/pub/artpub/2013/gsduab_3507/BenLliSal2013_Preprint.pdf.
4. *Exact angular return and physical-time Floquet rigidity for contracting homogeneous star-node cycles*, archived mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-angular-return-and-physical-time-floquet-rigidity-for-cont--7c00337eaa41.
5. *Planar periodic balance profiles automatically generate type-I oscillatory blow-up*, archived mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-planar-periodic-balance-profiles-automatically-generate-type-i-o--849c44b10231.
