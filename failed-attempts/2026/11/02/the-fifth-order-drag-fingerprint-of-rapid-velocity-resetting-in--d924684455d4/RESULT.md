# The fifth-order drag fingerprint of rapid velocity resetting in a persistent active particle

## Finding
Let the velocity of an inertial run-and-tumble particle be reset to zero at independent Poisson rate \(r\), *without resetting its dichotomous propulsive force*. Suppose its odd drag law has the local expansion
\[
g(v)=\gamma v+\kappa v^3+O(v^5),\qquad \gamma>0.
\]
For fixed propulsion magnitude \(a>0\) and orientation-switching rate \(\lambda>0\), the effective spatial diffusivity \(D_g(r)\) obeys the sharp comparison
\[
\boxed{D_g(r)-D_{\gamma}(r)=-\frac{6\kappa a^4}{\lambda r^5}+O(r^{-6})}\qquad(r\to\infty),
\]
where \(D_{\gamma}\) is the diffusivity of the **linear** drag \(g(v)=\gamma v\), evaluated at the same \(r,a,\lambda\). The linear reference is exactly
\[
\boxed{D_{\gamma}(r)=\frac{a^2}{(r+\gamma)(r+\gamma+2\lambda)}\left(\frac{2}{r+2\gamma}+\frac{1}{2\lambda}\right).}
\]
Consequently, for two admissible drag functions with the same linear coefficient and cubic coefficients \(\kappa_1,\kappa_2\), their diffusivities agree through orders \(r^{-2},r^{-3},r^{-4}\), while
\[
\lim_{r\to\infty}r^5\bigl(D_{g_1}(r)-D_{g_2}(r)\bigr)=-\frac{6a^4}{\lambda}(\kappa_1-\kappa_2).
\]
In particular, for equal \(a\in(0,1)\), \(\lambda>0\), and the shear-thickening and shear-thinning examples \(g_+(v)=\tan v\), \(g_-(v)=\tanh v\),
\[
\boxed{\lim_{r\to\infty}r^5(D_{\tan}(r)-D_{\tanh}(r))=-\frac{4a^4}{\lambda}<0.}
\]
This identifies the *first* term in the rapid-reset expansion which distinguishes two media sharing the same linearized friction.

## Assumptions and scope
The process on \(\mathbb R\times\{\pm1\}\) is defined by \(\dot v_t=a\sigma_t-g(v_t)\) between jumps. The independent symmetric two-state Markov chain \(\sigma_t\) flips at rate \(\lambda\). At Poisson rate \(r\), only \(v_t\) is replaced by zero: \(\sigma_t\) is unchanged. The position satisfies \(\dot X_t=v_t\). Assume \(g\) is odd, locally Lipschitz, nonnegative for nonnegative velocities, has the expansion displayed above with a locally bounded fifth-order remainder, and admits a compact forward-invariant velocity interval \([-b,b]\), where \(b>0\) and \(g(b)>a\). The hypotheses hold for the linear law, for \(\tan v\) (choose \(b\in(\arctan a,\pi/2)\)), and for \(\tanh v\) when \(0<a<1\) (choose \(b>\operatorname{artanh}a\)). All parameters except \(r\) are fixed and positive. The stationary dynamics is unique and is invariant under \((v,\sigma)\mapsto(-v,-\sigma)\); the velocity is centered. The diffusion coefficient is
\[
D_g(r)=\lim_{T\to\infty}\frac{\operatorname{Var}(X_T-X_0)}{2T}=\int_0^\infty\mathbb E[v_0v_t]\,dt,
\]
with the velocity-orientation process initialized stationarily. The integral is finite by exponential coupling: couple the finite-state orientation chains, then at their next common velocity reset both velocity states coincide.

## Proof
Write \(e(v)=g(v)-\gamma v\), \(M=\mathbb E[v\sigma]\), \(V=\mathbb E[v^2]\), and \(c=\mathbb E[\sigma e(v)]\), \(h=\mathbb E[v e(v)]\), under the stationary law. Stationarity of the test functions \(v\sigma\) and \(v^2\) gives the exact identities
\[
M=\frac{a-c}{r+\gamma+2\lambda},\qquad V=\frac{2aM-2h}{r+2\gamma}.
\]
For the autocovariance \(C(t)=\mathbb E[v_0v_t]\), the two-state noise identity \(\mathbb E[v_0\sigma_t]=M e^{-2\lambda t}\) and the velocity generator give
\[
D_g(r)=\frac{V+aM/(2\lambda)-I}{r+\gamma},\qquad I=\int_0^\infty\mathbb E[v_0e(v_t)]\,dt. \tag{1}
\]
These identities use no renewal approximation and preserve the propulsive state across each velocity reset.

For a stationary Poisson clock let \(A\) denote the age since its last reset, independent of the orientation process. Then \(A\sim\operatorname{Exp}(r)\). Dissipativity ensures \(|v|\le aA\) pathwise (the force is bounded by \(a\) and friction acts toward zero). Thus, for every fixed integer \(k\ge1\), \(\mathbb E|v|^k\le a^k k!r^{-k}\). During a fresh, reset-free excursion of age \(t\) from \(v=0\), the no-flip trajectory has \(v_t=a\sigma_0t+O(t^2)\), while a flip occurs with probability \(O(t)\). Uniformly in the two starting orientations this yields
\[
\mathbb E_{0,+}[e(v_t)]=\kappa a^3t^3+O(t^4),\qquad
\mathbb E_{0,\mathrm{stat}}[\sigma_t e(v_t)]=\kappa a^3t^3+O(t^4).
\]
(The subscript \(0\) signifies that velocity starts from zero; \(\mathrm{stat}\) gives equal initial orientation probabilities.) Integrating against the exponential age law gives
\[
c=\frac{6\kappa a^3}{r^3}+O(r^{-4}),\qquad h=O(r^{-4}),\qquad
J=\int_0^\infty e^{-rt}\mathbb E_{0,+}[e(v_t)]\,dt=\frac{6\kappa a^3}{r^4}+O(r^{-5}). \tag{2}
\]
Here, \(v_t\) inside \(J\) follows the dynamics **without any velocity resets** after its zero-velocity initial state. All error bounds follow from uniform fifth-order Taylor control on the invariant interval, the age moment bounds, and exponential tails of the reset clock.

We evaluate the time-correlation contribution \(I\) by an exact first-reset decomposition. Let \(S\sim\operatorname{Exp}(r)\) be the first reset after time zero, and let \(b(t)=\mathbb E_{(0,+)}[e(v_t)]\) be the evolution *with* resets, initialized with zero velocity and positive orientation. By odd symmetry, starting with negative orientation changes \(b\) to \(-b\). Conditioning on the first reset and using \(\mathbb E[v_0\sigma_S]=Me^{-2\lambda S}\) yields
\[
I=I_{\mathrm{nr}}+\frac{rM}{r+2\lambda}\int_0^\infty b(u)\,du,
\]
where \(I_{\mathrm{nr}}=\int_0^\infty e^{-rt}\mathbb E[v_0e(v_t^{\mathrm{noreset}})]\,dt\). Starting afresh from \((0,+)\), first-reset renewal with the still-evolving orientation gives
\[
b(t)=e^{-rt}\mathbb E_{0,+}[e(v_t)]+\int_0^t r e^{-(r+2\lambda)s}b(t-s)\,ds.
\]
Integrating this identity gives \(\int_0^\infty b(u)du=(r+2\lambda)J/(2\lambda)\). Hence the **exact** correlation decomposition is
\[
I=I_{\mathrm{nr}}+\frac{rM}{2\lambda}J. \tag{3}
\]
Before the first reset, \(|v_t|\le |v_0|+at\). Using \(|e(v)|\le C|v|^3\) on the accessible interval and the stationary age-moment bounds,
\[
|I_{\mathrm{nr}}|\le C\int_0^\infty e^{-rt}\mathbb E\{|v_0|(|v_0|+at)^3\}\,dt=O(r^{-5}).
\]
Equations (2)–(3), together with \(M=a/r+O(r^{-2})\), imply
\[
I=\frac{3\kappa a^4}{\lambda r^4}+O(r^{-5}). \tag{4}
\]
Subtract the identities for the reference linear drag, where \(e=c=h=I=0\). Equations (2) and the stationary moment equations give
\[
M-M_{\gamma}=-\frac{6\kappa a^3}{r^4}+O(r^{-5}),\qquad V-V_{\gamma}=O(r^{-5}).
\]
Substituting these and (4) into (1) yields
\[
D_g-D_{\gamma}=\frac{1}{r+\gamma}\left[O(r^{-5})-\frac{3\kappa a^4}{\lambda r^4}-\frac{3\kappa a^4}{\lambda r^4}+O(r^{-5})\right]
=-\frac{6\kappa a^4}{\lambda r^5}+O(r^{-6}).
\]
For the linear case, solving its two stationary moment equations and setting \(I=0\) gives the displayed rational formula for \(D_{\gamma}\). Finally, \(\tan v=v+v^3/3+O(v^5)\) and \(\tanh v=v-v^3/3+O(v^5)\), proving the stated difference.

## Verification
The accompanying `verify.py` uses exact rational arithmetic to check the linear reference law and the separate cubic-drag first-variation obtained by closing the linear reference generator on polynomial test functions. It checks parameter families, signs and the fifth-order coefficient; execute with `python3 verify.py` using only the Python standard library. The script verifies algebraic consequences, while the preceding first-reset identities and error estimates prove the asymptotic theorem.

## Relationship to prior work
Howlader, Mondal and Das (2026, arXiv:2606.00560) established the velocity-only-reset, persistent-orientation model and numerically found the universal \(r^{-2}\) decay of effective diffusion for both shear-thickening and shear-thinning drag. Those facts, the model, and the linearization explanation are prior work. The finding here determines the *first medium-sensitive term*, proves its coefficient and specifies the exact reference diffusivity; the motivating paper does not report these asymptotic coefficients. The no-reset nonlinear-drag diffusivity quadratures of Howlader–Mondal–Das (2025, arXiv:2507.12313) and Mondal–Das (2025, arXiv:2504.11683) have different (zero-reset) scope. Olsen–Löwen (2024, arXiv:2401.12685) derive general renewal formulas when the reset renews all relevant hidden dynamics; their stated renewal assumptions explicitly do not cover a propulsion-state Markov process that survives the velocity reset. The present calculation instead retains the orientation through resets and uses a first-reset identity for its covariance.

## Limitations
The assertion is for fixed \(a,\lambda,\gamma\) with \(r\to\infty\); it is not uniform as \(\lambda\to0\) and does not cover a simultaneous small-flip-rate limit. It assumes odd dissipative drag and a compact invariant velocity interval, so it does not address unbounded self-accelerating or nonsymmetric forces. It establishes a bulk diffusion coefficient, not a full displacement large-deviation law, an independent publication-priority certification, or rates for general renewal (non-Poisson) reset clocks.

## References
1. S. Howlader, S. Mondal, P. Das, *Velocity Resetting of Inertial Run-and-Tumble Particles in Non-Newtonian Media: Velocity Distribution, Diffusion and First-Passage Time*, arXiv:2606.00560 (first posted 2026-05-30), https://arxiv.org/abs/2606.00560.
2. K. S. Olsen, H. Löwen, *Dynamics of inertial particles under velocity resetting*, arXiv:2401.12685 (2024), https://arxiv.org/abs/2401.12685.
3. S. Howlader, S. Mondal, P. Das, *Velocity Distribution and Diffusion of an Athermal Inertial Run-and-Tumble Particle in a Shear-Thickening Medium*, arXiv:2507.12313 (2025), https://arxiv.org/abs/2507.12313.
4. S. Mondal, P. Das, *Velocity Distribution and Diffusion of an Athermal Inertial Run-and-Tumble Particle in a Shear-Thinning Medium*, arXiv:2504.11683 (2025), https://arxiv.org/abs/2504.11683.
