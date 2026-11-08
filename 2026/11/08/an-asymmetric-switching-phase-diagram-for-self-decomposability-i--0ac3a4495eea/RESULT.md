# An asymmetric-switching phase diagram for self-decomposability in intermittent harmonic traps

## Finding
Consider a Brownian particle in an intermittently active isotropic harmonic trap, with *different* exponential on-to-off and off-to-on switching rates. Its stationary position distribution is infinitely divisible in every finite dimension, for all strictly positive switching rates. Yet it admits an ordinary isotropic Lévy-driven Ornstein–Uhlenbeck representation only in a sharply classified part of the two-rate parameter plane. In a scalar observation the exact boundary is curved, whereas in any dimension at least two it is a horizontal line.

Precisely, let \(d\in\{1,2,\ldots\}\), \(u,v>0\), let \(S_t\in\{0,1\}\) jump from \(1\) to \(0\) at rate \(u\), and from \(0\) to \(1\) at rate \(v\), independently of standard Brownian motion \(W_t\in\mathbb R^d\). The normalized position obeys
\[
dZ_t=-S_tZ_t\,dt+\sqrt2\,dW_t.
\]
There is a unique stationary position law \(\mu_{u,v,d}\), with characteristic function
\[
\phi_{u,v,d}(q)=e^{-|q|^2/2}
\left(1+\frac{|q|^2}{u+v}\right)
\left(1+\frac{|q|^2}{v}\right)^{-1-u/2}.
\tag{1}
\]
It is infinitely divisible for all \(d,u,v\), and its self-decomposability has the **complete exact classification**
\[
\boxed{d=1:\quad \mu_{u,v,1}\in L\ \Longleftrightarrow\ v\ge\frac4{u+4}},
\qquad
\boxed{d\ge2:\quad \mu_{u,v,d}\in L\ \Longleftrightarrow\ v\ge2}.
\tag{2}
\]
Here \(L\) denotes the class of self-decomposable probability distributions. In particular, for \(d\ge2\) and
\[
\frac4{u+4}\le v<2,
\]
every one-dimensional linear projection of \(\mu_{u,v,d}\) is self-decomposable, although the *joint* stationary law is not. The threshold for the joint law depends solely on the off-to-on rate \(v\), even if the on-to-off rate \(u\) is arbitrarily different.

Whenever the appropriate inequality in (2) holds, \(\mu_{u,v,d}\) is explicitly the invariant distribution of
\[
dY_t=-Y_t\,dt+\sqrt2\,dB_t+dC_t,
\tag{3}
\]
where \(C\) is an independent isotropic compound-Poisson process with activity \(u\) and an explicitly nonnegative, normalized jump density below. If (2) fails, there is no scalar-drift Lévy-driven Ornstein–Uhlenbeck process with this stationary law. These are claims only about stationary *one-time laws*, not equivalence of trajectories.

## Assumptions and scope
All rates \(u,v\) are strictly positive, and \(d\) is a positive integer. The Brownian diffusion matrix is a multiple of the identity, and the switching chain is independent of the Brownian motion. The trap is either fully off or has positive linear restoring drift. If the physical equation is \(dX_t=-\kappa S_t X_t\,dt+\sqrt{2D}\,dW_t\), with physical switching rates \(r_{1\to0},r_{0\to1}>0\), set \(Z=X\sqrt{\kappa/D}\), \(u=r_{1\to0}/\kappa\), \(v=r_{0\to1}/\kappa\). The assertions concern the resulting stationary position marginal, not the joint process including \(S\), and not a time-dependent distribution.

Define \(\omega_d=2\pi^{d/2}/\Gamma(d/2)\), \(\nu=d/2\), and for \(c,r>0\) define the strictly positive radial kernel
\[
F_{c,d}(r)=\frac{2}{(2\pi)^{d/2}}
\left(\frac{\sqrt c}{r}\right)^{d/2}
K_{d/2}(\sqrt c\,r),
\tag{4}
\]
where \(K_\nu\) is the modified Bessel function of the second kind. Put \(A=1+u/2\) and
\[
\ell_{u,v,d}(r)=AF_{v,d}(r)-F_{u+v,d}(r),\qquad
k_d(r)=r^d\ell_{u,v,d}(r).
\tag{5}
\]

## Proof
**1. Existence and the exact Fourier transform.** A stationary version exists as the pathwise Gaussian stochastic convolution over the infinite past because the ergodic two-state chain spends a strictly positive fraction \(v/(u+v)\) of time in its restoring state. Its conditional variance integral is almost surely finite. Contractivity of the same linear equation driven with common noise and switching yields uniqueness.

Let \(F_1(\rho)\) and \(F_0(\rho)\) be the stationary partial characteristic functions weighted by the trap state, where \(\rho=|q|\). The generator and radial symmetry yield
\[
0=-\rho F_1'(\rho)-\rho^2F_1(\rho)-uF_1(\rho)+vF_0(\rho),
\]
\[
0=-\rho^2F_0(\rho)+uF_1(\rho)-vF_0(\rho).
\]
The second equation gives \(F_0=uF_1/(v+\rho^2)\). Substitution and the stationary trap-state probability \(F_1(0)=v/(u+v)\) give
\[
F_1(\rho)=\frac{v}{u+v}e^{-\rho^2/2}
\left(1+\frac{\rho^2}{v}\right)^{-u/2}.
\]
Adding \(F_0\) proves (1) for every integer \(d\ge1\).

**2. A positive multivariate Lévy measure.** The negative logarithm of (1) is
\[
\Psi(q)=\frac{|q|^2}{2}+A\log\left(1+\frac{|q|^2}{v}\right)
-\log\left(1+\frac{|q|^2}{u+v}\right).
\tag{6}
\]
Use the heat kernel \(p_t(x)=(4\pi t)^{-d/2}e^{-|x|^2/(4t)}\) and
\[
\log(1+|q|^2/c)=\int_0^\infty(1-e^{-t|q|^2})e^{-ct}\,\frac{dt}{t},
\]
which gives \(F_{c,d}(|x|)=\int_0^\infty e^{-ct}p_t(x)\,dt/t\). Thus the Lévy measure in (6) has the radial Lebesgue density \(\ell_{u,v,d}(|x|)\). It is strictly positive because \(A>1\), \(F_{v,d}>F_{u+v,d}\), and the kernels are positive. It satisfies the Lévy integrability condition, either directly by the Gaussian subordination integral or by standard Bessel asymptotics. The Gaussian covariance component is the identity. This proves infinite divisibility for every allowed parameter.

**3. The exact self-decomposability criterion.** The classical isotropic polar form of the self-decomposability criterion states that a rotationally invariant infinitely divisible law with radial Lévy *Lebesgue* density \(\ell(r)\) is self-decomposable exactly when \(r^d\ell(r)\) is nonincreasing on \((0,\infty)\). It applies here because (5) is smooth for \(r>0\). The Bessel identity
\[
\frac{d}{dz}\big[z^\nu K_\nu(z)\big]=-z^\nu K_{\nu-1}(z)
\tag{7}
\]
reduces this condition to a scalar sign test.

For \(d=1\), \(F_{c,1}(r)=e^{-\sqrt c\,r}/r\), so
\[
k_1(r)=Ae^{-\sqrt v\,r}-e^{-\sqrt{u+v}\,r}.
\]
Its derivative is nonpositive at every \(r>0\) exactly if \(A\sqrt v\ge\sqrt{u+v}\). To see necessity, send \(r\downarrow0\); for sufficiency, factor out the more slowly decaying exponential. Squaring and simplifying with \(A=1+u/2\), using \(u>0\), gives \(v\ge4/(u+4)\), proving the first boundary in (2).

For \(d\ge2\), set \(\nu=d/2\ge1\), \(a=\sqrt v\), \(b=\sqrt{u+v}\), \(t=b/a>1\), and \(x=ar\). By (7), the ratio of the negative radial derivatives of \(r^dF_{u+v,d}(r)\) and \(r^dF_{v,d}(r)\) is
\[
R_{\nu,t}(x)=t^{\nu+1}\frac{K_{\nu-1}(tx)}{K_{\nu-1}(x)}.
\]
For \(\eta=\nu-1\ge0\), the function \(z^\eta K_\eta(z)\) decreases strictly: its derivative is \(-z^\eta K_{\eta-1}(z)<0\). Consequently \(R_{\nu,t}(x)<t^2\) for every \(x>0\). As \(x\downarrow0\), the ratio tends to \(t^2\): for \(\eta>0\) this follows from \(K_\eta(z)\sim2^{\eta-1}\Gamma(\eta)z^{-\eta}\), and for \(\eta=0\) from \(K_0(z)\sim-\log z\). Hence \(\sup_{x>0}R_{\nu,t}(x)=t^2\). Nonincrease of \(k_d\) is exactly \(A\ge t^2=(u+v)/v\), equivalently (because \(u>0\)) to \(v\ge2\). This proves the second boundary.

All one-dimensional projections have the one-dimensional Fourier law (1) with the same rates, because (1) is radial. Thus the projection-versus-joint separation follows immediately by combining the two necessary-and-sufficient conditions. For example \(u=3\), \(v=1\), and \(d=3\) lies strictly in this gap.

**4. Explicit jump density and rate.** In the self-decomposable parameter region, define for \(x\ne0\)
\[
g_{u,v,d}(x)=-\frac{k_d'(|x|)}{u\,|x|^{d-1}}.
\tag{8}
\]
The preceding proof gives pointwise nonnegativity. The small-radius Bessel asymptotics yield
\[
\omega_d\lim_{r\downarrow0}r^dF_{c,d}(r)=2,
\qquad
\omega_dk_d(0+)=2(A-1)=u.
\]
Also \(k_d(r)\to0\) as \(r\to\infty\). Therefore polar integration gives \(\int_{\mathbb R^d}g_{u,v,d}(x)\,dx=\omega_d\int_0^\infty(-k_d'(r))/u\,dr=1\). The canonical Lévy measure of the stationary law is
\[
\ell(r)\,dx=\frac{k_d(r)}{r^d}\,dx,
\]
which is exactly the integral under unit OU contraction of the compound-Poisson Lévy density \(u g\,dx\): the jump contribution is \(\int_0^\infty u e^{ds}g(e^s x)\,ds=k_d(r)/r^d\), by change of radial variable. The Brownian OU part contributes stationary covariance \(I_d\). Hence (3) has law (1) at equilibrium. Conversely any stationary law of a scalar-drift Lévy-driven OU process is self-decomposable by splitting the stochastic convolution in time. Therefore failure of (2) rules out such a representation.

## Verification
The packaged \(\texttt{CHECKER.py}\) performs 917 deterministic finite checks, including numerical integration of the one-dimensional Lévy–Khintchine exponent, finite-difference Bessel derivative tests in dimensions one through four, sign tests across both boundaries, and stationary second-moment identities. Execute \(\texttt{python CHECKER.py}\) with Python 3 and SciPy installed. Its exact output is \(\texttt{CHECKER PASSED: 917 finite numerical / arithmetic assertions}\). The analytical proof above, including the supremum of the Bessel ratio, is necessary for the quantified all-dimensional result; finite parameter grids are not a substitute for it.

The variance from (1) is, for every unit direction, \(\mathbb E[(e\cdot Z)^2]=1-2/(u+v)+(u+2)/v\). On the diagonal \(u=v=\alpha\), (1) specializes exactly to the equal-rate characteristic function already available in the literature. No originality is claimed for that restriction.

## Relationship to prior work
Alston, Cocconi and Bertrand (2022) study exactly this physical on/off harmonic trap with unequal switching rates, but their full-text asymmetric subsection addresses entropy production, not infinitely divisible or class-\(L\) characterizations. Frydel (2024) gives the equal-rate characteristic function, a Gaussian-mixture construction, and extensions in dimension, but does not classify class \(L\). Existing equal-rate self-decomposability results already give scalar and vector thresholds on the diagonal \(u=v\); that diagonal is explicitly treated as prior coverage. The new statement is the **entire off-diagonal two-rate plane**, the rate-independent multivariate boundary \(v=2\), the curved projection boundary \(v=4/(u+4)\), and the associated explicit jump-driving law. Classical Lévy and self-decomposability results, including the radial monotonicity criterion, provide the proof methods and are not themselves claimed as new. A published self-decomposability threshold for Gaussian compound-Poisson perturbations of variance-gamma laws treats a different characteristic exponent and does not imply these two-rate trap thresholds.

## Limitations
The theorem assumes a fully inactive off state, constant isotropic diffusivity, two exponential switching clocks, and a linear trap in the on state. It does not address anisotropic drift, three-state environments, nonexponential renewal switching, or finite-time joint laws. The Lévy-driven OU equivalence is one-time stationary equivalence and not equality of stochastic trajectories, entropy production, temporal correlations, or a Markovian realization of the physical switching model. The original physical dynamics is not a scalar-drift Lévy OU process merely because its marginal law is self-decomposable. The published exact same-object literature and a semantic research database were checked for implications, but unindexed class-\(L\) results or multivariate generalized gamma convolution results could still reduce publication priority. No independent audit has been performed.

## References
1. H. Alston, L. Cocconi and T. Bertrand, *Non-equilibrium thermodynamics of diffusion in fluctuating potentials*, arXiv:2202.02630v1 (first posted 2022-02-05), especially Section 4.2.1 and Appendix A. https://arxiv.org/html/2202.02630v1
2. D. Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap*, arXiv:2407.12213v2 (2024), especially Equation (20), Section V. https://arxiv.org/html/2407.12213v2
3. K.-I. Sato, *Lévy Processes and Infinitely Divisible Distributions*, Cambridge University Press, 1999, canonical Lévy-density criteria for class \(L\).
4. D. Applebaum, *Infinite dimensional Ornstein–Uhlenbeck processes driven by Lévy processes*, Probability Surveys **12** (2015), 33–54. https://doi.org/10.1214/14-PS249
5. D. Frydel, *Semi-Markovian switching in a fluctuating harmonic trap: an age-structured formulation*, arXiv:2607.05173 (2026), comparison of switching-time formulations. https://arxiv.org/abs/2607.05173
