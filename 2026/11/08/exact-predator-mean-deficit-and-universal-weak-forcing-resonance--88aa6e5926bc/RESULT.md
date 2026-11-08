# Exact predator-mean deficit and universal weak-forcing resonance in a threshold predator–prey system

## Finding
Consider the smooth coexistence equations of the periodically forced threshold predator–prey model,
\[
\dot N=N\left(\rho(t)\left(1-\frac NK\right)-aP\right),
\qquad \dot P=P(abN-m),
\]
where \(a,b,m,K>0\), \(\rho(t)>0\) is \(T\)-periodic with mean \(r_0>0\), and \(0<N_*=m/(ab)<K\). Set
\[
P_* =\frac{r_0}{a}\left(1-\frac{N_*}{K}\right),
\qquad \langle f\rangle=\frac1T\int_0^T f(t)\,dt.
\]
Every strictly positive \(T\)-periodic solution, of arbitrary amplitude, obeys the **exact forced mean law**
\[
\boxed{\langle N\rangle=N_*,\qquad
P_*-\langle P\rangle
=\frac{\operatorname{Cov}_T(\rho,N)}{aK}
=\frac{\left\langle\rho(t)(N(t)-N_*)^2\right\rangle}{aK^2(1-N_*/K)}.}
\]
For any nonconstant \(\rho\), this defect is strictly positive: the periodic response has exactly the unforced prey mean but a strictly smaller predator mean. Equivalently, the forcing and prey abundance have strictly positive time covariance on every positive locked cycle.

There is an additional **universal weak-forcing resonance law**. Write \(\rho(t)=r_0+A\cos(\omega t)\) with \(\omega>0\), \(|A|\) sufficiently small, and set
\[
\gamma=\frac{r_0N_*}{K},\qquad
\Omega^2=mr_0\left(1-\frac{N_*}{K}\right)>0.
\]
For every fixed \(\omega>0\) a unique locally attracting \(2\pi/\omega\)-periodic solution exists near \((N_*,P_*)\), and its mean predator deficit has the expansion
\[
\boxed{\frac{P_*-\langle P\rangle}{P_*}=
\frac{A^2}{2r_0^2}\,
\frac{\gamma^2\omega^2}{(\Omega^2-\omega^2)^2+\gamma^2\omega^2}
+O_{\omega}(A^4).}
\]
The coefficient of \(A^2\), as a function of \(\omega\in(0,\infty)\), has a unique global maximum at **\(\omega=\Omega\)**. Its maximum is exactly \(1/(2r_0^2)\), independently of the other biological coefficients. Hence the peak leading fractional predator-mean reduction is \(A^2/(2r_0^2)\). This is an assertion about the **weak-forcing coefficient**, not the exact resonance frequency for finite amplitude.

For the motivating paper's parameters \(r_0=1.2\), \(K=6\), \(a=1.1\), \(b=0.32\), \(m=0.45\), the leading predator-mean resonance is at \(\Omega\approx0.651877\), corresponding to forcing period \(2\pi/\Omega\approx9.63861\). The free damped eigenfrequency is instead about \(0.639218\), with period about \(9.82948\); the two frequencies are not equal.

## Assumptions and scope
The first, exact theorem assumes a strictly positive, continuously differentiable \(T\)-periodic growth rate \(\rho(t)\) and a strictly positive \(T\)-periodic solution of the two equations displayed above. No smallness, stability, harmonic shape, or proximity-to-equilibrium assumption is required. The covariance convention is
\[
\operatorname{Cov}_T(f,g)=\langle fg\rangle-\langle f\rangle\langle g\rangle.
\]
The existence of a positive periodic orbit for arbitrary forcing is **not** asserted. In the full Filippov threshold model, this theorem applies to a trajectory only when its entire periodic orbit stays in the interior \(N(t)>N_a\), \(P(t)>P_a\), so that neither switching law is activated. It does **not** apply across threshold crossings or to the smoothed-Heaviside substitute model.

The weak-forcing statement assumes the same positive parameter conditions and a fixed frequency \(\omega>0\); its periodic branch is local in the amplitude \(A\) and is unique in a neighborhood of the unforced coexistence equilibrium. If the unforced equilibrium strictly exceeds both Filippov thresholds, then for sufficiently small \(|A|\) this periodic branch also lies entirely in the coexistence region, giving an actual solution of the full unsmoothed model. The \(O_{\omega}(A^4)\) bound is for each fixed frequency; no uniform remainder as \(\omega\to0\) or \(\infty\) is claimed.

## Proof
**1. A locked prey mean.** On any strictly positive periodic orbit,
\[
\frac d{dt}\log P=abN-m.
\]
Its mean over a full period vanishes. Thus
\[
\langle N\rangle=\frac m{ab}=N_*.
\]
Likewise,
\[
\frac d{dt}\log N=\rho(t)\left(1-\frac NK\right)-aP.
\]
Average this identity, use \(\langle\rho\rangle=r_0\), and compare with \(aP_*=r_0(1-N_*/K)\). The result is
\[
a(P_*-\langle P\rangle)=\frac1K\bigl(\langle\rho N\rangle-r_0N_*\bigr)
=\frac1K\operatorname{Cov}_T(\rho,N).
\]

**2. A positive, exact variance identity.** Define the standard Volterra-type function
\[
V(N,P)=b\left(N-N_*-N_*\log\frac N{N_*}\right)
+P-P_*-P_*\log\frac P{P_*}.
\]
Its derivative along the *forced* vector field is **exactly**
\[
\dot V=b(N-N_*)\left[
(\rho-r_0)\left(1-\frac{N_*}{K}\right)
-\frac{\rho}{K}(N-N_*)\right].
\]
This follows by differentiating the two logarithmic terms, then cancelling the opposite predation fluxes with \(abN_*=m\) and \(aP_*=r_0(1-N_*/K)\); the standalone checker verifies the algebra symbolically. Integrating the derivative over the period yields
\[
\left(1-\frac{N_*}{K}\right)
\operatorname{Cov}_T(\rho,N)
=\frac1K\left\langle\rho(t)(N-N_*)^2\right\rangle.
\]
The right-hand side is nonnegative because \(\rho(t)>0\). It can vanish only when \(N(t)\equiv N_*\). The predator equation then makes \(P\) constant, and the prey equation forces \(\rho\) constant. Thus for every nonconstant growth forcing the right-hand side is **strictly** positive. Substitution into Step 1 gives all three equalities and the strict mean-predator inequality.

**3. Existence of the local forced cycle.** At \(A=0\), the coexistence equilibrium has Jacobian
\[
J=\begin{pmatrix}-\gamma&-aN_*\\abP_*&0\end{pmatrix},
\qquad \operatorname{tr}J=-\gamma<0,
\qquad \det J=a^2bN_*P_*=\Omega^2>0.
\]
Both eigenvalues have strictly negative real parts. For each fixed \(\omega>0\), the derivative of the \(2\pi/\omega\)-return map at the unforced equilibrium is \(e^{J(2\pi/\omega)}\), whose eigenvalues have modulus less than one. The implicit function theorem therefore gives a unique nearby analytic fixed point of the return map for all sufficiently small \(|A|\). It is a locally attracting locked periodic solution. Positivity and any strict threshold inequalities persist by continuity.

**4. Linear harmonic response.** Put \(g=N_*(1-N_*/K)\). Expanding the periodic branch in \(A\), its first-order deviations \(n_1,p_1\) satisfy
\[
\dot n_1=-\gamma n_1-aN_*p_1+g\cos(\omega t),
\qquad \dot p_1=abP_*n_1.
\]
For the periodic solution, complex harmonic notation gives
\[
n_1(t)=\Re\left(
\frac{ig\omega}{\Omega^2-\omega^2+i\gamma\omega}\,e^{i\omega t}
\right).
\]
Therefore
\[
\left\langle\cos(\omega t)n_1(t)\right\rangle
=\frac{g\gamma\omega^2}{2\bigl[(\Omega^2-\omega^2)^2+\gamma^2\omega^2\bigr]}.
\]
In the exact covariance identity from Step 1, \(\rho-r_0=A\cos\omega t\), so the leading deficit is obtained by multiplying this expression by \(A^2/(aK)\). Dividing by \(P_*=r_0(1-N_*/K)/a\), and using \(\gamma=r_0N_*/K\), gives the displayed fractional-deficit coefficient.

Why is the remainder fourth order? A half-period translation changes the sign of the forcing amplitude. By uniqueness of the small periodic branch, its period mean is unchanged under \(A\mapsto -A\). Analytic dependence on \(A\) thus makes the mean predator an even analytic function, excluding all odd powers, so the error after the quadratic term is \(O_{\omega}(A^4)\).

**5. Exact optimization of the quadratic coefficient.** Let \(z=\omega^2>0\). Apart from positive constants, the frequency-dependent factor is
\[
F(z)=\frac{z}{(\Omega^2-z)^2+\gamma^2z}.
\]
Direct differentiation gives
\[
F'(z)=\frac{\Omega^4-z^2}
{\bigl[(\Omega^2-z)^2+\gamma^2z\bigr]^2}.
\]
It is strictly increasing until \(z=\Omega^2\), strictly decreasing thereafter, and vanishes at the two ends in the relevant limit. At \(z=\Omega^2\), the frequency-dependent fraction in the boxed mean-deficit formula is exactly one. Thus the unique optimal frequency for the quadratic predator deficit is \(\omega=\Omega\), with universal normalized peak \(1/(2r_0^2)\).

## Verification
Running `python verify.py` with NumPy, SciPy and SymPy performs exact symbolic checks of the forced Volterra derivative and the resonance derivative, followed by 16 numerical periodic shooting/integration cases at the motivating parameters (four small amplitudes times four frequencies). Period integrals independently check the equal prey mean and both formulas for the predator deficit; the smallest-amplitude cases also check the quadratic response. It prints `PASS: 2 symbolic identities and 16 periodic shooting/integration cases` when complete. Numerical tests of finitely many cases are **not** proofs of the universal result; the proof is the algebra, period integration, implicit-function argument, and rational optimization above.

## Relationship to prior work
Gao, Poloni, Wang and Lewis introduce the same piecewise-smooth predator–prey equations, display the coexistence equilibrium and damped eigenfrequency, use a Volterra function for *unforced* global stability, and numerically show frequency-selective amplification and threshold-induced tipping. Their primary text, including the subsystem analysis and appendix, does **not** present the forced periodic mean/covariance defect or the weak-forcing optimal **mean-predator-loss** frequency and universal coefficient. Our local response result concerns the mean of the periodic coexistence branch, not their peak/trough tipping threshold; it should not be mistaken for a new tipping theorem. The authors' damped eigenfrequency \(\sqrt{\Omega^2-\gamma^2/4}\) describes free oscillations, whereas our distinct \(\Omega\) maximizes the quadratic mean-deficit response.

Classical Volterra averaging and linear response provide prior components of the method; their general existence is acknowledged. Other exact average identities for autonomous/delayed predator–prey equations have different vector fields or a different mechanism (for example, nonlinear reciprocal predation or gestation delays), and do not directly imply a strictly positive forcing–prey covariance and universal quadratic mean-deficit optimum for this periodically forced smooth coexistence system. Taylor, Sherratt and White (2013) study seasonal forcing in predator–prey systems, with an abstract emphasizing bifurcation and simulation; their full manuscript was not accessible during this review, so potential detailed overlap remains a declared priority risk. Related stochastic-resonance work concerns different forcing regimes and observables. A complete worldwide priority claim is not made.

## Limitations
The exact identities constrain positive periodic solutions but do not establish that every forcing produces one, nor characterize quasiperiodicity, chaos, threshold impacts, transient behavior or extinction. Strict mean loss requires **nonconstant** forcing; constant forcing gives zero defect. The weak-forcing solution is proved only locally around coexistence and at fixed frequency; the location of the optimal mean-response frequency for a **finite** amplitude may shift. The proof does not extend to solutions that cross Filippov switching thresholds or to the sigmoid-smoothed model. The primary literature comparison includes a specifically identified inaccessible, highly relevant 2013 seasonal forcing paper, leaving residual historical-priority uncertainty.

## References
1. S. Gao, S. Poloni, H. Wang and M. Lewis, “Frequency-induced Tipping: Resonance-Driven Tipping in a Threshold Predator-Prey System,” arXiv:2610.39113v1, first publicly submitted 2026-10-29, primary MSC2020 37G35. https://arxiv.org/abs/2610.39113
2. R. A. Taylor, J. A. Sherratt and A. White, “Seasonal forcing and multi-year cycles in interacting populations: lessons from a predator-prey model,” *Journal of Mathematical Biology* 67 (2013), 1741–1764. DOI: 10.1007/s00285-012-0612-z.
3. E. Benincà, V. Dakos, E. H. Van Nes, J. Huisman and M. Scheffer, “Resonance of Plankton Communities with Temperature Fluctuations,” *The American Naturalist* 178 (2011), 398–410. DOI: 10.1086/661902.
4. D. Bai and X. Zhang, “Dynamics of a Predator–Prey Model with the Additive Predation in Prey,” *Mathematics* 10 (2022), 655. DOI: 10.3390/math10040655. (Distinct delayed-system comparison.)
