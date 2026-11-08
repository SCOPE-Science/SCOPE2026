# Laboratory-clock Floquet memory and a sharp reset–detuning window in a driven quantum lattice

## Finding

**Theorem (phase-resolved weak-reset crossover).** Let a particle move on the infinite one-dimensional tight-binding lattice, driven by a sinusoidal external force whose laboratory clock **does not restart** when the particle is reset. At each independent Poisson event of rate \(\lambda>0\), replace the particle state by the origin state \(\lvert0\rangle\). For any fixed drive phase \(\theta\), the long-time site distribution exists as a \(2\pi\)-periodic function of the observation phase, and has the exact formula
\[
\Pi_m^{(\lambda,z)}(\theta)=\int_0^\infty \lambda e^{-\lambda a}
J_m^2\!\left(\frac{\Delta}{\omega}\left|\int_{\theta-\omega a}^\theta
 e^{iz\sin u}\,du\right|\right) da,\qquad m\in\mathbb Z.
\]
This generally differs from a phase-independent reset-age stationary profile.

Let \(z_*\) be any **positive simple zero** of \(J_0\), and put \(\rho=\lambda/\omega\). Define the zero-mean periodic primitive and its variance by
\[
A_z(\phi)=\sum_{k\in\mathbb Z\setminus\{0\}}
\frac{J_k(z)}{ik}e^{ik\phi},\qquad
V_z=\frac1{2\pi}\int_0^{2\pi}|A_z(\phi)|^2\,d\phi
=2\sum_{k=1}^\infty\frac{J_k(z)^2}{k^2}.
\]
If \(z=z(\rho)=z_*+\xi\rho+o(\rho)\) for a fixed real \(\xi\), let \(v=\xi J_0'(z_*)\), \(X\sim\mathrm{Exp}(1)\), and \(U\sim\mathrm{Unif}[0,2\pi)\), with \(X\) and \(U\) independent. Then, at each fixed phase \(\theta\), the **entire probability law on** \(\mathbb Z\) converges in total variation:
\[
\boxed{\quad\Pi_m^{(\lambda,z(\rho))}(\theta)\ \longrightarrow\ 
\mathbb E\left[J_m^2\left(\frac\Delta\omega
\left|vX+A_{z_*}(\theta)-A_{z_*}(U)\right|\right)\right].\quad}
\]
The second moments also converge, with the explicit value
\[
\boxed{\quad \lim_{\rho\downarrow0}\sum_{m\in\mathbb Z}m^2\Pi_m^{(\lambda,z(\rho))}(\theta)
=\frac{\Delta^2}{2\omega^2}
\left(2v^2+2v\operatorname{Re}A_{z_*}(\theta)
+|A_{z_*}(\theta)|^2+V_{z_*}\right).\quad}
\]
Averaging this limit uniformly over the observation phase gives \(\Delta^2(v^2+V_{z_*})/\omega^2\).

The width of this localization window is **sharp**: for any \(z(\rho)\to z_*\), the stationary-position second moments at a fixed phase stay bounded as \(\rho\downarrow0\) if and only if \(|z(\rho)-z_*|=O(\rho)\). If \(|z(\rho)-z_*|/\rho\to\infty\), then
\[
\sum_{m\in\mathbb Z}m^2\Pi_m^{(\lambda,z(\rho))}(\theta)
\sim \frac{\Delta^2 J_0(z(\rho))^2}{\lambda^2}\ \longrightarrow\infty.
\]
The phase-specific limiting second moment is minimized at
\(\xi_*(\theta)=-\operatorname{Re}A_{z_*}(\theta)/(2J_0'(z_*))\), so optimal detuning need not coincide with the bare Floquet zero for a fixed observation phase.

For the first positive Bessel zero and \(\Delta=\omega=1\), the exactly resonant limiting second moments at \(\theta=0\) and \(\theta=\pi/2\) are approximately \(1.0142692754\) and \(0.3207903662\), respectively; the phase average is \(0.6415807324\). Thus the limiting law retains visible laboratory-phase memory.

## Assumptions and scope

On \(\ell^2(\mathbb Z)\), let \(T\lvert n\rangle=\lvert n+1\rangle\), \(N\lvert n\rangle=n\lvert n\rangle\), and
\[
H(t)=-\frac{\Delta}{2}(T+T^\dagger)+F_0\cos(\omega t)N,
\qquad \Delta,\omega>0,\quad F_0\in\mathbb R,\quad z=F_0/\omega.
\]
We use units \(\hbar=1\). Reset events are independent of the unitary dynamics and of one another; their counting process has intensity \(\lambda\). At each event the particle is replaced by the pure state \(\lvert0\rangle\langle0\rvert\). Crucially, the force \(F_0\cos(\omega t)\) is a prescribed function of **absolute time**, not of the age since the last reset. The statement concerns measured *site probabilities*, not trace-norm convergence of all off-diagonal density matrix elements. The observation-phase limit is evaluated along any times \(t\to\infty\) with \(\omega t\equiv\theta\pmod{2\pi}\), or against the periodic family at each time with uniform exponential transient error. The weak-reset limits hold at each fixed \(\theta\) and with \(\Delta,\omega\) fixed.

## Proof

**1. Unitary evolution between resets.** A diagonal gauge transformation removing the force changes the two hopping terms into scalar multiples of \(T\) and \(T^\dagger\). Because these shifts commute with each other, the interaction-picture time-ordered exponential reduces to an ordinary exponential. A particle placed at the origin at physical time \(s\) therefore has position probability
\[
\mathbb P(X_t=m\mid \text{origin at }s)
=J_m^2\left(\Delta\left|\int_s^t
 e^{iz\sin(\omega u)}\,du\right|\right).
\]
The final gauge multiplies site amplitudes by phases only. Bessel normalization \(\sum_{m\in\mathbb Z}J_m^2(b)=1\) holds for every real \(b\).

**2. Exact phase-resolved renewal law.** For a Poisson clock, the probability that the last reset precedes \(t\) by an age in \((a,a+da)\), with \(0<a<t\), is \(\lambda e^{-\lambda a}da\); the remaining probability of no reset is \(e^{-\lambda t}\). Substituting \(s=t-a\) yields the displayed integral truncated at \(t\). Completing the mixture to infinite age changes its \(\ell^1\) norm by at most \(2e^{-\lambda t}\) after including the no-reset contribution. Because the force has unchanged laboratory phase, the infinite-age expression is \(2\pi\)-periodic in \(\theta=\omega t\), not generally constant.

**3. Exact Floquet decomposition.** The Jacobi–Anger series gives
\[
e^{iz\sin\phi}=J_0(z)+\sum_{k\ne0}J_k(z)e^{ik\phi}=J_0(z)+A_z'(\phi).
\]
For real \(z\) the Bessel coefficients are superexponentially small in \(|k|\) on compact \(z\)-ranges; hence this and all differentiated series converge absolutely and uniformly. Consequently, with \(\theta=\omega t\),
\[
\omega\int_{t-a}^{t}e^{iz\sin(\omega u)}\,du
=J_0(z)\,\omega a+A_z(\theta)-A_z(\theta-\omega a).
\]
Parseval gives the stated identity for \(V_z\), and the periodic mean of \(A_z\) is zero.

**4. Two-scale weak-reset law.** Draw \(X\) from the unit-rate exponential law and set \(a=X/\lambda\). The argument of the conditional Bessel probability, multiplied by \(\omega/\Delta\), is exactly
\[
B_\rho(X,\theta)=\frac{J_0(z(\rho))}{\rho}X
+A_{z(\rho)}(\theta)-A_{z(\rho)}(\theta-X/\rho).
\]
The simple-zero expansion implies \(J_0(z(\rho))/\rho\to v\). The uniform convergence of the Fourier primitives implies \(A_{z(\rho)}\to A_{z_*}\) uniformly. For every nonzero integer \(k\) and bounded continuous \(f\),
\[
\int_0^\infty e^{-x}f(x)e^{ik(\theta-x/\rho)}\,dx\to0
\quad(\rho\downarrow0)
\]
by the Riemann–Lebesgue lemma. Approximation by trigonometric polynomials yields joint weak convergence of \((X,\theta-X/\rho\bmod 2\pi)\) to \((X,U)\) with independent uniform \(U\). Therefore \(B_\rho\Rightarrow vX+A_{z_*}(\theta)-A_{z_*}(U)\). For every integer \(m\), the bounded continuous map \(b\mapsto J_m^2((\Delta/\omega)|b|)\) gives pointwise convergence of the site probabilities. Both the prelimit and limiting sequences are probability mass functions (by Bessel normalization). Hence discrete Scheffé's lemma proves their **total-variation convergence on all sites**, with no finite-site truncation hypothesis.

**5. Second moments and phase memory.** The standard Bessel moment identity is \(\sum_{m\in\mathbb Z}m^2J_m^2(b)=b^2/2\). For \(z(\rho)=z_*+\xi\rho+o(\rho)\), the bound \(|B_\rho|\le C(1+X)\) is uniform for small \(\rho\). Since the exponential law has all polynomial moments, \(|B_\rho|^2\) is uniformly integrable. Taking expectations in the Bessel moment identity and using \(\mathbb EX=1\), \(\mathbb EX^2=2\), \(\mathbb EA(U)=0\) and \(\mathbb E|A(U)|^2=V_{z_*}\) yields the exact displayed limiting moment. Its uniform phase average follows from \(\int A=0\) and Parseval. Minimizing the quadratic expression in \(v=\xi J_0'(z_*)\) gives the stated optimum.

**6. Sharpness.** For arbitrary \(z(\rho)\to z_*\), write \(c_\rho=J_0(z(\rho))/\rho\) and \(D_\rho=A_{z(\rho)}(\theta)-A_{z(\rho)}(\theta-X/\rho)\). The periodic primitive is uniformly bounded, so \(\mathbb E|D_\rho|^2\le C\). The \(L^2\) reverse triangle inequality applied to \(B_\rho=c_\rho X+D_\rho\) gives bounded moments only if \(c_\rho\) is bounded. Conversely bounded \(c_\rho\) yields bounded second moment by the ordinary triangle inequality. Since \(J_0'(z_*)\ne0\), bounded \(c_\rho\) is equivalent to \(|z(\rho)-z_*|=O(\rho)\). When \(|c_\rho|\to\infty\), \(\mathbb E|B_\rho|^2=2c_\rho^2+O(|c_\rho|)+O(1)\), proving the asymptotic \(\Delta^2J_0(z(\rho))^2/\lambda^2\). This remains uniform in observation phase.

## Verification

`CHECK.py` independently evaluates the periodic-primitive series and the force integral, compares the exact age mixture with a geometrically blocked representation, checks the detuning crossover against direct quadrature, and verifies the limiting site-mass and second-moment identities. The extracted standalone checker passed 86 finite assertions on numerical ranges including \(\rho=0.4,0.2,0.1,0.06\) and approaching the critical window. To reproduce, use Python 3 with NumPy and SciPy and execute `python CHECK.py` in the directory containing this document. The numerical checks corroborate the formulas; they are neither exhaustive nor a substitute for the infinite-parameter arguments above.

## Relationship to prior work

The driven tight-binding reset study of Dattagupta, Das and Gupta (2022) [1] supplies the physically natural model and the non-driven Floquet \(J_0\)-zero mechanism. Their examined late-time formulas write the Bessel phase integral with a reset-age lower endpoint, and do not give a laboratory-clock phase-resolved weak-reset/detuning law. Acharya and Gupta (2023) [2] use a resetting tight-binding chain, including periodic fields, but the inspected Floquet formulas likewise depend on time since reset and do not state the present absolute-clock joint asymptotics. The mathematical distinction is that the external drive is here explicitly not restarted at a reset, which forces the endpoint term \(A_z(\theta)-A_z(\theta-\omega a)\). The earlier quantum-reset spectral work [3] and related quantum-reset dynamics [4] supply general background, not this site-law limit. Dynamical localization at zeros of \(J_0\) is classical Floquet physics [5] and is **not** claimed as new. The claimed contribution is the phase-resolved periodic law and the exact, sharp laboratory-clock reset-rate/detuning crossover, not generic renewal or Floquet identities.

## Limitations

The theorem assumes an infinite translation-invariant chain, uniform sinusoidal external forcing, resets always to the origin, independent exponential reset times, a fixed observation phase and simple Bessel zeros. It does not cover non-Poisson resetting, phase-reset forcing, finite boundaries, interacting particles or arbitrary driven Hamiltonians. The total-variation conclusion concerns the **site measurement law**, not convergence of density operators in trace norm. The quoted decimals are numerical illustrations, not exact algebraic constants. The literature comparison is based on accessible inspected sources and database queries, not a proof of universal publication priority; phase-dependent extensions of general Floquet-reset theory might subsume the result.

## References

[1] S. Dattagupta, D. Das, S. Gupta, “Stochastic resets in the context of a tight-binding chain driven by an oscillating field,” arXiv:2209.14117, first posted 2022-09-28, https://arxiv.org/abs/2209.14117.

[2] A. Acharya, S. Gupta, “Tight-binding model subject to conditional resets at random times,” arXiv:2308.14040, first posted 2023-08-27, https://arxiv.org/abs/2308.14040.

[3] D. C. Rose, H. Touchette, I. Lesanovsky, J. P. Garrahan, “Spectral properties of simple classical and quantum reset processes,” arXiv:1806.01298, https://arxiv.org/abs/1806.01298.

[4] B. Mukherjee, K. Sengupta, S. N. Majumdar, “Quantum dynamics with stochastic reset,” arXiv:1806.00019, https://arxiv.org/abs/1806.00019.

[5] D. H. Dunlap, V. M. Kenkre, “Dynamic localization of a charged particle moving under the influence of an electric field,” Phys. Rev. B 34, 3625 (1986), https://doi.org/10.1103/PhysRevB.34.3625.
