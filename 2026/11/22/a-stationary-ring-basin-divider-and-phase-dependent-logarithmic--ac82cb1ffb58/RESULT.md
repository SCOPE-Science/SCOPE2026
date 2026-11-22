# A stationary-ring basin divider and phase-dependent logarithmic exit clock in a chemical two-cycle oscillator

## Finding

The planar polynomial chemical oscillator of Craciun and Erban [1] contains a distinguished, rotationally symmetric quartic member. Its invariant geometry and physical-time dynamics are different questions: although its two cycle radii are known, its mobility factor breaks the time-rotation symmetry. The following single theorem resolves its invariant sets, exact basins, two real-time periods, transverse multipliers, and critical exit delay in an explicit physically positive disk.

For \(\varepsilon>0\) define
\[
 u=x-2,\quad v=y-2,\quad s=u^2+v^2,\quad h(s)=16s^2-25s+9=16(s-9/16)(s-1),
\]
\[
 \dot x=xy(-h\,h_x-\varepsilon h_y),\qquad
 \dot y=xy(-h\,h_y+\varepsilon h_x).\tag{1}
\]
This is exactly the originating system [1, equations (5.13)–(5.19)] for the quartic coefficient \(\mu=32\), not a modified vector field. Work on the open disk \(\mathcal D=\{(x,y):s<4\}\subset(0,\infty)^2\). Put \(s_-=9/16\), \(s_*=25/32\), \(s_+=1\).

**Complete dynamics.** The stationary set in \(\mathcal D\) consists precisely of \((2,2)\) and the entire circle \(s=s_*\). The only nonconstant periodic orbits are the two circles \(s=s_-\) and \(s=s_+\), each hyperbolically attracting. All other solutions are forward complete and, in set-distance, tend to the inner cycle if \(0<s(0)<s_*\) and to the outer cycle if \(s_*<s(0)<4\). Thus the equilibrium ring is the precise basin separator. An initial state on the ring stays at that state. The center is stationary.

**Exact original-time clocks and spectra.** In the same order, the minimal periods \(T_\pm\) and the nontrivial Floquet multipliers \(\rho_\pm\) are
\[
\boxed{T_-=\frac{256\pi}{833\sqrt{55}\,\varepsilon},\quad
 T_+=\frac{4\pi}{49\sqrt3\,\varepsilon};\qquad
 \rho_-=\exp\!\left(-\frac{63\pi}{4\varepsilon}\right),\quad
 \rho_+=\exp\!\left(-\frac{28\pi}{\varepsilon}\right).}\tag{2}
\]

**Phase-sensitive escape from the stationary ring.** Fix \(0<\eta<7/32\). For a nonzero displacement \(\delta\) with \(0<|\delta|<\eta\), choose initial polar angle \(\theta(0)=\phi\) and squared radius \(s(0)=s_*+\delta\). Let \(\tau_\eta(\delta,\phi)\) be the first physical time the solution reaches \(s=s_*+\operatorname{sgn}(\delta)\eta\). Write \(r_*=\sqrt{s_*}=5/(4\sqrt2)\) and
\[w_*(\phi)=(2+r_*\cos\phi)(2+r_*\sin\phi).\]
Then, uniformly for \(\phi\in\mathbb R/(2\pi\mathbb Z)\),
\[
\boxed{\tau_\eta(\delta,\phi)=\frac{16}{1225\,w_*(\phi)}\log\frac1{|\delta|}+O_{\eta,\varepsilon}(1),\qquad\delta\to0.}\tag{3}
\]
The leading coefficient is not angle-independent. In particular, angularly different initial concentrations at the same small radial displacement can have different leading escape times, even though \(h\) is radial. The equilibrium ring is normally repelling with positive normal eigenvalue \(1225\,w_*(\phi)/16\) at phase \(\phi\).

As an elementary geometric consequence, uniform-area initial data on the disk have inner- and outer-basin probabilities \(25/128\) and \(103/128\), respectively (the stationary subsets have area zero). The disk is used solely as an exact invariant positive observation region; there is no assertion for all positive-quadrant initial data.

## Assumptions and scope

All statements concern finite \(\varepsilon>0\) held fixed, the exact original polynomial flow (1), physical time as displayed, and classical real trajectories starting in \(\mathcal D\). Polar angle \(\theta=\operatorname{arg}(u+iv)\) is used only away from the center, with any continuous local lift when calculating travel time. \(O_{\eta,\varepsilon}(1)\) means a bound independent of \(\delta\) and the initial angle, for each fixed permitted \(\eta\) and \(\varepsilon\). The numerical value \(\eta<7/32\) keeps both target circles strictly between the stationary ring and their respective attracting cycles. Floquet multipliers mean the nontrivial multipliers of the planar first-return map on a transverse section, in original physical time.

## Proof

**1. Exact polar reduction and radial invariant regions.** Since \(h_s=32s-25\), the gradient is \(\nabla h=2(32s-25)(u,v)\). Put
\[
 w(s,\theta)=(2+\sqrt{s}\cos\theta)(2+\sqrt{s}\sin\theta).
\]
For \(0<s<4\), this weight is smooth and strictly positive. Direct scalar and angular products of (1) give the *exact original-time* identities
\[
\boxed{\dot s=-4w(s,\theta)s\,h(s)(32s-25),\qquad
\dot\theta=2\varepsilon w(s,\theta)(32s-25).}\tag{4}
\]
The vector field is zero exactly at \(s=0\) and \(s=s_*\), since \(xy>0\) and its radial and angular components can both vanish only when \(\nabla h=0\). The circles \(s=s_-\) and \(s=s_+\) have \(h=0\) but \(h_s\ne0\), so they are periodic orbits, with nowhere vanishing angular velocity. Their invariance and the fact that the circle \(s=s_*\) consists of equilibria imply no orbit can cross any of them.

The signs of \(h(s)(32s-25)\), on successive intervals separated by \(0,s_-,s_*,s_+\), are \(-,+,-,+\). Thus \(\dot s\) is strictly positive on \((0,s_-)\), negative on \((s_-,s_*)\), positive on \((s_*,s_+)\), and negative on \((s_+,4)\). Every initial state stays between invariant levels inside the compact positive disk of radius at most \(\max\{\sqrt{s(0)},1\}<2\), and therefore exists for all forward time. The monotone radial coordinate has a limit, which must be the appropriate attracting endpoint: otherwise the positive continuous \(w\), bounded uniformly away from zero on the compact trapping annulus, would force a nonvanishing radial derivative. The only possibilities are convergence to \(s_-\) or \(s_+\). There is no other periodic orbit because its radial coordinate would have to be constant and equations (4) exhaust the nonstationary constant levels. As \(s\to s_\pm\), \(|\dot\theta|\) is bounded away from zero, so each nonstationary trajectory's omega-limit set is the entire appropriate circle. This gives the global description *within* \(\mathcal D\).

**2. Exact angular quadrature.** On a periodic circle of squared radius \(a\in\{9/16,1\}\), the angular speed magnitude is \(14\varepsilon w(a,\theta)\), because \(|32a-25|=7\). Therefore its minimal physical-time period is
\[
T(a)=\frac{1}{14\varepsilon}I(a),\qquad
I(a)=\int_0^{2\pi}\frac{d\theta}{(2+\sqrt a\cos\theta)(2+\sqrt a\sin\theta)}.\tag{5}
\]
To evaluate the integral without a time reparametrization, for \(0\le a<4\) put \(\Delta=\sqrt{4-a}\) and \(q=-\sqrt a/(2+\Delta)\). The uniformly convergent Fourier expansion
\[
\frac1{2+\sqrt a\cos\theta}=\frac1\Delta\left(1+2\sum_{n=1}^{\infty}q^n\cos(n\theta)\right)
\]
and its quarter-turn translate for the sine denominator give by orthogonality
\[
I(a)=\frac{2\pi}{\Delta^2}\left(1+2\sum_{n\ge1}q^{2n}\cos(n\pi/2)\right)
=\frac{2\pi}{\Delta^2}\frac{1-q^4}{1+q^4}
=\frac{8\pi}{(8-a)\sqrt{4-a}}.\tag{6}
\]
Substituting \(a=9/16\) and \(a=1\) in (5)–(6) proves the periods (2).

**3. Exact transverse multipliers.** Near either attracting circle \(s=a\), linearize the first equation (4) in \(\sigma=s-a\). As \(h(a)=0\), the normal linear variational equation is
\[
\dot\sigma=-4a(32a-25)^2w(a,\theta(t))\sigma=-196a\,w(a,\theta(t))\sigma.\tag{7}
\]
Over one physical period of either cycle, irrespective of its orientation, \(\int_0^{T(a)}w(a,\theta(t))dt=2\pi/(14\varepsilon)=\pi/(7\varepsilon)\). Integrating (7) hence gives \(\log\rho(a)=-28\pi a/\varepsilon\). The two strict negative exponents yield (2) and hyperbolic attraction. Note that the \(xy\) mobility influences the periods, but cancels from the multiplier integral.

**4. Integrable angular drift and the logarithmic exit clock.** For a trajectory off the equilibrium and periodic circles, divide the equations (4) to eliminate the positive mobility factor and the factor \(32s-25\):
\[
\frac{d\theta}{ds}=-\frac{\varepsilon}{2s h(s)}.\tag{8}
\]
In a neighborhood of \(s_*\) this right-hand side is smooth; it extends continuously through \(s_*\) as a function of the radial coordinate, even though physical trajectories cannot cross the stationary ring. One exact antiderivative (up to an additive constant) is
\[
G(s)=\varepsilon\left(-\frac1{18}\log s+\frac8{63}\log|s-9/16|-\frac1{14}\log|s-1|\right).\tag{9}
\]
Thus along any orbit in a collar avoiding the two periodic circles, \(\theta(s)=\phi+G(s)-G(s_*+\delta)\). Uniformly in \(\phi\) and \(\delta\), this implies \(\theta(s)=\phi+O_{\varepsilon}(|s-s_*|+|\delta|)\). Smoothness of \(w\) in this positive compact collar yields
\[w(s,\theta(s))=w_*(\phi)+O_{\varepsilon}(|s-s_*|+|\delta|),\]
with \(\inf_\phi w_*(\phi)>0\). Since
\[
h(s_*)=-49/64,\quad s_*=25/32,\quad 32s-25=32(s-s_*),
\]
we obtain from (4) the uniform asymptotic radial velocity
\[
\dot s=\frac{1225}{16}\,w_*(\phi)(s-s_*)\bigl[1+O_{\eta,\varepsilon}(|s-s_*|+|\delta|)\bigr]\tag{10}
\]
for sufficiently small fixed \(\eta\), with the higher-order statement justified also by smoothness on the full fixed collar. More explicitly, the exact reciprocal integrand differs from \(16/[1225w_*(\phi)|s-s_*|]\) by a term bounded in absolute value by \(C_{\eta,\varepsilon}(1+|\delta|/|s-s_*|)\). The physical time from \(|s-s_*|=|\delta|\) to \(|s-s_*|=\eta\) is therefore
\[
\tau_\eta=\int_{|\delta|}^{\eta}\left[\frac{16}{1225\,w_*(\phi)z}+O_{\eta,\varepsilon}(1+|\delta|/z)\right]dz,
\]
which is exactly (3), because the remainder integrates to a bounded value. Differentiating (4) at a point on the equilibrium circle gives one zero tangential eigenvalue and the positive normal eigenvalue \(1225w_*(\phi)/16\), establishing normal repulsion. As \(w_*\) is nonconstant, the logarithmic coefficient is genuinely phase-dependent.

**5. Area fractions.** The equilibrium circle encloses area \(\pi s_*=25\pi/32\) inside the disk of area \(4\pi\). The ratio is \(25/128\). Its complement, up to measure-zero invariant sets, has probability \(103/128\). This is only a consequence of the already-proved exact radial basins, not a stochastic kinetic claim.

## Verification

The accompanying standalone program `check_two_cycle_basin.py` symbolically recomputes both polar identities and the critical radial coefficient; checks the quartic roots; compares the physical-time period quadrature with the closed formula at the two cycles and the equilibrium ring; checks the sign of transverse exponents; and integrates several near-ring initial conditions to confirm the angle-sensitive logarithmic slopes. A successful execution prints `TWO_CYCLE_BASIN_CHECK_OK`. These computations test the identities and finite cases; the uniform all-angle convergence and global phase portrait follow from the arguments above, not the numerical diagnostics. The checker requires Python with SymPy and SciPy and can be run with `python check_two_cycle_basin.py`.

## Relationship to prior work

Craciun and Erban [1] introduced the *identical* ninth-degree mass-action vector field (1), its algebraic cofactor, and the two invariant concentric circles at \(\mu=32\) in Lemma 13(iv), proving the existence and stability of the algebraic cycles using their general Theorem 3. Those cycles and the cofactor identity are explicitly prior, not newly discovered. The new theorem instead identifies an additional continuous circle of stationary chemical states, proves the **complete** disk-level basin separator, evaluates both exact original-time periods and transverse multipliers, and proves a **uniform, phase-sensitive logarithmic exit-time law** from the equilibrium ring. These statements are not provided by the source's existence/stability criterion. General invariant-algebraic-curve and cofactor methods from Gasull and Giacomini [2] are relevant methodology, but their principal explicit applications concern different low-degree systems and do not supply the exact original-time clock (3) for this ninth-degree vector field. Related numerical and analytical studies of the original four-oval regime \(\mu>337/9\) concern a different nonisotropic phase-space geometry, not the normally repelling equilibrium ring at \(\mu=32\).

## Limitations

The complete basin classification is proved only in the disk \(s<4\), entirely within the positive quadrant; no global assertion beyond that disk, for zero \(\varepsilon\), or for anisotropic \(\mu\ne32\) is made. The stationary ring is a nonhyperbolic continuum of equilibria with a positive *normal* exponent, not a periodic orbit. The logarithmic clock concerns the fixed first-exit level \(\eta\) as \(\delta\to0\), not stochastic first passages, sampling noise, or chemical experiments. The original two stable cycle radii and the vector field are known results; novelty is restricted to the particular basin, quantitative spectral, and original-time phase-delay statements. Equivalent unindexed or unpublished analyses of this special member could affect priority. Independent mathematical validation has not been performed.

## References

[1] G. Craciun and R. Erban, *Planar chemical reaction systems with algebraic and non-algebraic limit cycles*, arXiv:2406.05057, first public version June 7, 2024, https://arxiv.org/abs/2406.05057 ; published as *Journal of Mathematical Biology* 90, 64 (2025), DOI:10.1007/s00285-025-02221-0. See equations (5.13)–(5.19), Theorem 3, and Lemma 13(iv).

[2] A. Gasull and H. Giacomini, *Number of limit cycles for planar systems with invariant algebraic curves*, arXiv:2210.15803 (2022), *Qualitative Theory of Dynamical Systems* 22, 44 (2023), DOI:10.1007/s12346-023-00746-7. See the introduction and Theorem 2.1 on cofactor methods and absence of extraneous cycles.
