# Weak-chirality rotational-inertia resonance for a free active Brownian swimmer

## Finding
For a planar free swimmer whose stationary angular velocity is a mean-drifting Ornstein–Uhlenbeck process, finite angular inertia has a sharp singular transport optimum as imposed chirality vanishes. For every fixed nonzero angular drift \(\Omega\), the long-time one-coordinate effective diffusivity \(D_{\mathrm{eff}}(\tau,\Omega)\) has at least one **finite, strictly positive global maximizing** angular relaxation time \(\tau\). Every choice \(\tau_*(\Omega)\) of global maximizer satisfies
\[
\lim_{|\Omega|\downarrow0}\frac{\Omega^2\tau_*(\Omega)}{D_r}=1,
\qquad
\lim_{|\Omega|\downarrow0}\frac{2|\Omega|}{v^2}\bigl(\max_{\tau>0}D_{\mathrm{eff}}(\tau,\Omega)-D_0\bigr)=\sqrt{\frac{\pi}{2e}}.
\]
For exactly zero chirality, \(D_{\mathrm{eff}}(\tau,0)\) is instead strictly increasing in \(\tau\) and diverges as \(D_0+\frac{v^2}{2}\sqrt{\pi\tau/(2D_r)}\). This distinguishes a sharp optimization law from finite-parameter uniqueness, which is *not* claimed.

## Assumptions and scope
Fix \(D_r>0\), swimmer speed \(v>0\), independent translational diffusivity \(D_0\ge0\), angular drift \(\Omega\in\mathbb R\), and angular-velocity relaxation time \(\tau>0\). The stationary process has an angle uniform modulo \(2\pi\), independent of its angular-velocity fluctuation at the initial time, and evolves by
\[
d\theta_t=\omega_t\,dt,\qquad
d\omega_t=-\frac{\omega_t-\Omega}{\tau}\,dt+\frac{\sqrt{2D_r}}{\tau}\,dW_t,
\qquad
dX_t=v\cos(\theta_t)\,dt+\sqrt{2D_0}\,dB_t.
\]
Here \(W\) and \(B\) are independent standard real Brownian motions, and initially \(\omega_0\sim N(\Omega,D_r/\tau)\). Define \(D_{\mathrm{eff}}=\lim_{T\to\infty}\operatorname{Var}(X_T-X_0)/(2T)\), with this limit finite for every finite \(\tau\). This is a dilute, noninteracting, free-space angular-inertia model; it does not include boundaries, resetting, interactions, or angular acceleration feedback from translation.

## Proof
**1. Exact Green–Kubo kernel.** The stationary velocity fluctuation \(\omega_t-\Omega\) has covariance \((D_r/\tau)e^{-|t|/\tau}\). Direct integration gives
\[
\operatorname{Var}(\theta_t-\theta_0-\Omega t)
=2D_r\bigl[t-\tau(1-e^{-t/\tau})\bigr].
\]
Its characteristic function and rotational stationarity imply the exact coordinate-velocity covariance
\[
\operatorname{Cov}(v\cos\theta_t,v\cos\theta_0)
=\frac{v^2}{2}\,C_\tau(t)\cos(\Omega t),\quad
C_\tau(t)=\exp\bigl(-D_r[t-\tau(1-e^{-t/\tau})]\bigr).
\]
Since \(C_\tau(t)\le e^{D_r\tau}e^{-D_rt}\), this is integrable. Consequently
\[
D_{\mathrm{eff}}(\tau,\Omega)=D_0+\frac{v^2}{2}K(\tau,\Omega),\qquad
K(\tau,\Omega)=\int_0^\infty C_\tau(t)\cos(\Omega t)\,dt.
\]
The Green–Kubo identity proves \(K\ge0\); the integrand itself need not be nonnegative when \(\Omega\ne0\).

**2. Small-inertia gain.** Extend \(K\) continuously to \(\tau=0\) by \(K(0,\Omega)=D_r/(D_r^2+\Omega^2)\). The identity
\[
C_\tau(t)=e^{-D_rt}\exp\bigl[D_r\tau(1-e^{-t/\tau})\bigr]
\]
with its uniform exponential bound shows, as \(\tau\downarrow0\),
\[
K(\tau,\Omega)=\frac{D_r}{D_r^2+\Omega^2}+
\tau\frac{D_r^2}{D_r^2+\Omega^2}+O(\tau^2).
\]
Indeed the first-order remainder from the factor \(e^{-t/\tau}\) integrates to \(O(\tau^2)\). Thus every finite chirality initially benefits strictly from increasing angular inertia.

**3. Large-inertia cutoff for nonzero chirality.** Put \(g_\tau(t)=D_r[t-\tau(1-e^{-t/\tau})]\) and \(f_\tau(t)=-C_\tau'(t)=D_r(1-e^{-t/\tau})e^{-g_\tau(t)}\). The logarithmic derivative of \(f_\tau\) decreases strictly from positive infinity to negative \(D_r\), so \(f_\tau\) has one maximum and vanishes at both endpoints. Twice integrating by parts, using \(C_\tau'(0)=0\), gives
\[
|K(\tau,\Omega)|\le \frac{\int_0^\infty|C_\tau''(t)|dt}{\Omega^2}
=\frac{2\max_{t\ge0}f_\tau(t)}{\Omega^2},\quad\Omega\ne0.
\]
For \(0\le t\le\tau\), the inequality \(g_\tau(t)\ge D_rt^2/(3\tau)\) and \(1-e^{-t/\tau}\le t/\tau\) show
\[
f_\tau(t)\le\frac{D_rt}{\tau}\exp\bigl(-D_rt^2/(3\tau)\bigr)
\le\sqrt{\frac{3D_r}{2e\tau}}.
\]
For \(t\ge\tau\), monotonicity of \(g_\tau\) gives \(f_\tau(t)\le D_re^{-D_r\tau/e}\). Hence \(\max f_\tau=O(\sqrt{D_r/\tau})\) as \(\tau\to\infty\), so \(K(\tau,\Omega)\to0\) for every fixed \(\Omega\ne0\). Continuity, positivity at \(\tau=0\), and the strict small-\(\tau\) gain now imply at least one interior finite global maximizer for every \(\Omega\ne0\).

**4. Zero-chirality divergence.** Since \(t-\tau(1-e^{-t/\tau})\) is strictly decreasing in \(\tau\) for each \(t>0\), \(K(\tau,0)=\int C_\tau\) is strictly increasing. Rescaling \(t=s\sqrt{\tau/D_r}\) and using \(g_\tau(t)\to s^2/2\), with the Gaussian bound on \(t\le\tau\) and the exponential tail on \(t\ge\tau\), gives
\[
K(\tau,0)\sim\sqrt{\frac{\pi\tau}{2D_r}}.
\]

**5. Global weak-chirality resonance.** Let \(\varepsilon=|\Omega|\to0\) and set \(\tau=D_rx/\varepsilon^2\) with fixed \(x>0\). After \(t=s/\varepsilon\),
\[
\varepsilon K(D_rx/\varepsilon^2,\varepsilon)
=\int_0^\infty e^{-g_{D_rx/\varepsilon^2}(s/\varepsilon)}\cos s\,ds
\longrightarrow F(x)=\int_0^\infty e^{-s^2/(2x)}\cos s\,ds
=\sqrt{\frac{\pi x}{2}}e^{-x/2}.
\]
The convergence is uniform for \(x\) in any compact subinterval of \((0,\infty)\): on \(t\le\tau\) one has the Gaussian integrable envelope, and the contribution of \(t\ge\tau\) is uniformly exponentially small. To rule out maximizers escaping to \(x=0\), split the integral at \(t=\tau\) to obtain the uniform estimate
\[
0\le K(\tau,\varepsilon)\le\int_0^\infty C_\tau(t)\,dt
\le\sqrt{\frac{3\pi\tau}{4D_r}}+\frac{1}{D_r(1-e^{-1})};
\]
hence \(\varepsilon K\le\sqrt{3\pi x/4}+O(\varepsilon)\). To rule out escape to \(x=\infty\), use Step 3: \(\varepsilon |K|\le 2\max f_\tau/\varepsilon=O(x^{-1/2})\) when \(\tau=D_rx/\varepsilon^2\to\infty\). The function \(F(x)\) has a unique strict global maximum at \(x=1\), with value \(\sqrt{\pi/(2e)}\). Uniform compact convergence plus both tail bounds force every global optimizer to satisfy \(\varepsilon^2\tau_*/D_r\to1\) and the optimum value claimed above. No uniqueness assertion is made at any fixed nonzero \(\varepsilon\).

## Verification
Run `python3 verify.py` from this package. It independently computes the time-integrated OU covariance by two elementary integrals, checks the kernel against direct quadrature, checks the derivative at zero inertia, and numerically compares finite-chirality optima with the rigorous weak-chirality constants. These finite checks support—but do not establish—the asymptotic and global-maximum proof.

## Relationship to prior work
Scholz, Jahanshahi, Ldov and Löwen (arXiv:1807.04357, first public 2018-07-11), Eqs. (3), (8) and (9), **already establish the full chirality-dependent orientation kernel and an exact incomplete-gamma expression for the long-time diffusivity**, with both angular drift and rotational inertia. Neither this kernel, its exact quadrature, nor the basic presence of a finite-parameter diffusion peak is claimed new. The present evaluated step is instead the global existence theorem for every nonzero chirality, the singular small-chirality asymptotic of **all** global maximizers, and the universal sharp maximum coefficient, established using localization bounds that are not supplied by the prior closed expression. Tiwari, Singh and Winkler (arXiv:2606.10486, first public 2026-06-09), Section V, revisit rotational-inertia persistence and its exact nonchiral double-exponential correlation; their diffusivity asymptotics concern zero chirality. Pattanayak, Roy and Chaudhuri (arXiv:2511.18361, first public 2025-11-23), analyze chirality with translational, but overdamped rotational, dynamics, so they do not supply the angular-inertia optimization. Ai, Guo, Zeng and He (Phys. Rev. E **109**, 064902, 2024) already report qualitative nonmonotone diffusion versus rotational inertia in interacting chiral systems; that observation is not claimed new. The 2024 full text could not be obtained for exhaustive comparison, leaving a substantive priority risk concerning any unindexed explicit singular-limit analysis.

## Limitations
The statement is for the exactly specified planar free-space SDE with stationary angular velocity and independent translational Brownian noise. It does not assert a unique finite-chirality optimizer, a result for interacting/dense suspensions, an effective response tensor under external force, or a finite-size experimental optimum at arbitrarily small chirality. In particular, the free-swimmer asymptotic is not a theorem about the 2024 interacting glass model. Full-text priority against that closely relevant source remains unresolved; an independent scientific audit has not been performed.

## References
- C. Tiwari, S. P. Singh and R. G. Winkler, *Virial Stress in Systems of Active Brownian Particles in the Presence of Translational and Rotational Inertia*, arXiv:2606.10486 (first public 2026-06-09), https://arxiv.org/abs/2606.10486, especially Section V.
- A. Pattanayak, S. Roy and A. Chaudhuri, *Inertia-chirality interplay in active Brownian motion: exact dynamics and phase maps*, arXiv:2511.18361 (2025-11-23), https://arxiv.org/abs/2511.18361.
- B.-q. Ai, R.-x. Guo, C.-h. Zeng and Y.-f. He, *Rotational inertia-induced glassy transition in chiral particle systems*, Phys. Rev. E **109**, 064902 (2024), https://doi.org/10.1103/PhysRevE.109.064902.
- C. Scholz, S. Jahanshahi, A. Ldov and H. Löwen, *Inertial delay of self-propelled particles*, Nat. Commun. **9**, 5156 (2018), https://doi.org/10.1038/s41467-018-07596-x.
