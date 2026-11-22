# Sharp wavelength-selective overaccumulation and polarization peaks under exponential speed memory

## Finding

An exact weak-landscape response theory is obtained for a one-dimensional run-and-tumble swimmer whose positive speed relaxes exponentially toward a spatial activity profile. A finite reaction time selectively strengthens long-wavelength density accumulation while suppressing short-wavelength accumulation, with a sharp crossover and a different exact polarization-optimal time.

Let a circle have circumference \(L>0\). Let \(v>0\), the orientation-flipping rate \(\alpha>0\), and the speed-memory time \(\tau>0\) be fixed. For a real, mean-zero trigonometric polynomial \(h(x)\), consider the stationary Markov process

\[
\dot X_t=\sigma_t S_t,\qquad
\dot S_t=\frac{v+\varepsilon h(X_t)-S_t}{\tau},\qquad
\sigma_t\in\{-1,+1\},
\]

where the orientation changes sign at independent exponential waiting times of rate \(\alpha\), and \(|\varepsilon|\lVert h\rVert_\infty<v\). Put \(k_n=2\pi n/L\) and \(h_n=L^{-1}\int_0^L h(x)e^{-ik_nx}\,dx\). For any stationary law \(\mu_\varepsilon\) supported on the invariant speed interval and any nonzero Fourier index \(n\), the following limits hold, independently of the selection of stationary laws:

\[
\lim_{\varepsilon\to0}\frac{\mathbb E_{\mu_\varepsilon}[e^{-ik_nX}]}{\varepsilon}
=-\frac{h_n}{v}\frac{1+4\alpha\tau}{1+2\alpha\tau+(k_nv\tau)^2},
\]

\[
\lim_{\varepsilon\to0}\frac{\mathbb E_{\mu_\varepsilon}[\sigma e^{-ik_nX}]}{\varepsilon}
=ik_nh_n\frac{\tau}{1+2\alpha\tau+(k_nv\tau)^2}.
\]

For any present harmonic \(h_n\ne0\), its density contrast relative to instantaneous motility adaptation is amplified **if and only if**

\[
0<\tau<\tau_{\mathrm{cross},n}=\frac{2\alpha}{k_n^2v^2}.
\]

At equality it is unchanged to first order; for longer positive memory it is strictly suppressed. Its contrast has a **unique positive global maximizer**

\[
\tau_{\mathrm{density},n}^{*}=
\frac{\sqrt{1+8\alpha^2/(k_n^2v^2)}-1}{4\alpha}.
\]

In contrast, the modulus of the orientation-polarization harmonic has its unique positive maximum at

\[
\tau_{\mathrm{polar},n}^{*}=\frac1{|k_n|v},
\]

**independent of the flipping rate**. The polarization optimum lies in the density-enhanced region exactly when \(2\alpha>|k_n|v\), on its boundary at equality, and beyond it otherwise. These are statements about the first derivative at zero landscape amplitude, not claims of all-amplitude optimization.

## Assumptions and scope

The model has a smooth periodic activity landscape with finite Fourier support, no translational Brownian diffusion, unbiased symmetric direction flips, and an exponentially adapting positive scalar speed. The mathematical observation is the invariant one-point distribution on the circle together with its orientation-resolved first Fourier coefficients; the model does not assert the absence of nonzero current at higher orders in \(\varepsilon\). All claims hold for each fixed \(v,\alpha,\tau,L>0\). \(\varepsilon\) tends to zero with those parameters fixed. No statement of uniformity in \(\tau\to0\), \(\tau\to\infty\), or harmonic index is needed.

For every admissible nonzero \(\varepsilon\), at least one stationary law exists on the compact state space with \(S\in[v-|\varepsilon|\lVert h\rVert_\infty,v+|\varepsilon|\lVert h\rVert_\infty]\). The stationary response formula holds for all such laws; uniqueness at nonzero amplitude is not assumed.

## Proof

Write \(\eta=1/\tau\), \(k=k_n\ne0\), and \(z=(S-v)/\varepsilon\). Since \(\dot S=\eta(v+\varepsilon h(X)-S)\), every invariant law satisfies \(|z|\le\lVert h\rVert_\infty\). At \(\varepsilon=0\), the speed converges deterministically to \(v\). The remaining telegraph process on a circle has unique invariant law: position is uniform, and both orientations have probability \(1/2\). To see uniqueness directly, its stationary Fourier equations at nonzero \(k\) form an invertible two-by-two system, while the zero Fourier mode has equal state masses. Weak compactness and invariance then show that every \(\mu_\varepsilon\) converges weakly to this law as \(\varepsilon\to0\).

Introduce \(p_\pm=\mathbb E[e^{-ikX}\mathbf1_{\{\sigma=\pm1\}}]\) and \(b_\pm=\mathbb E[ze^{-ikX}\mathbf1_{\{\sigma=\pm1\}}]\). Stationarity applied to \(ze^{-ikX}\mathbf1_{\{\sigma=\pm1\}}\) gives, because \(z\) is uniformly bounded and the position–orientation marginal tends to the uniform telegraph law,

\[
(\eta+\alpha+ikv)b_+-\alpha b_-=\eta h_n/2+o(1),
\qquad
(\eta+\alpha-ikv)b_--\alpha b_+=\eta h_n/2+o(1).
\]

Both systems are nonsingular since \(\eta>0\), \(\alpha>0\), and \(k\ne0\). Let \(b_T=b_++b_-\), \(b_D=b_+-b_-\), and \(\mathcal D=\eta(\eta+2\alpha)+(kv)^2>0\). Adding and subtracting yields

\[
 b_T\to\frac{\eta(\eta+2\alpha)h_n}{\mathcal D},\qquad
 b_D\to-\frac{ikv}{\eta+2\alpha}\frac{\eta(\eta+2\alpha)h_n}{\mathcal D}.
\]

Stationarity for \(e^{-ikX}\mathbf1_{\{\sigma=\pm1\}}\), with \(p_T=p_++p_-\) and \(p_D=p_+-p_-\), gives exactly

\[
 ik(vp_D+\varepsilon b_D)=0,\qquad
 ik(vp_T+\varepsilon b_T)+2\alpha p_D=0.
\]

Therefore \(p_D/\varepsilon\to-b_D/v\) and \(p_T/\varepsilon\to-b_T/v+2\alpha b_D/(ikv^2)\). Substituting the two limiting \(b\) expressions gives precisely the stated polarization and density multipliers after dividing numerator and denominator by \(\eta^2\). This derivation uses no closure approximation, ergodic simulation or assumption of smooth stationary densities.

Let \(K=|k|v>0\), \(Q(\tau)=1+2\alpha\tau+K^2\tau^2\), and \(H(\tau)=(1+4\alpha\tau)/Q(\tau)\). The instantaneous-adaptation law has density proportional to \((v+\varepsilon h)^{-1}\), so its first-order contrast multiplier is \(1\). Algebra gives

\[
H(\tau)-1=\frac{\tau(2\alpha-K^2\tau)}{Q(\tau)},\qquad
H'(\tau)=\frac{2\alpha-2K^2\tau-4\alpha K^2\tau^2}{Q(\tau)^2}.
\]

The numerator of \(H'\) decreases strictly from a positive value to a negative value, giving exactly one positive optimizer and the displayed closed form. For polarization, \(G(\tau)=\tau/Q(\tau)\), and

\[
G'(\tau)=\frac{1-K^2\tau^2}{Q(\tau)^2}.
\]

This establishes its unique optimum at \(1/K\); comparing it with \(2\alpha/K^2\) gives the rate-dependent ordering of the two clocks.

## Verification

The companion `checker.py` independently solves the two complex Fourier resolvent systems at 72 parameter choices, integrates the unperturbed telegraph characteristic function, and checks the symbolic factorization and optimizer formulas. All checks passed. A separate `simulation.py` uses a numerical particle trajectory with exponentially relaxing speed and randomly switching orientation: at \(v=\alpha=|k|=1\) and modulation amplitude \(\varepsilon=0.08\), the observed cosine-density and sine-polarization coefficients agreed approximately with the linear theory for four distinct memory times. These computations corroborate but do not replace the proof.

For a cosine landscape with \(v=\alpha=|k|=1\), the density contrast optimum is \((\sqrt9-1)/4=1/2\), the density enhancement boundary is \(2\), and the polarization optimum is \(1\). The distinct optima demonstrate that optimizing accumulation need not optimize polarization.

## Relationship to prior work

Rein, Kroy and Holubec (arXiv:2608.03906, August 2026) analyze delayed motility in periodic activity landscapes including exponentially adapting speed and run-and-tumble motion. Their main results concern diffusion enhancement, current rectification and reversal. This work retains their physically natural exponential speed-memory model but addresses a different observable: the exact, all-memory-time, first-order **stationary Fourier density and polarization response**, together with sharp mode-by-mode thresholds.

Holubec et al. (arXiv:2505.11042) analyze delayed active swimmers, primarily with deterministic time delay and angular Brownian reorientation, obtaining short-delay and long-delay density/polarization descriptions. Töpfer et al. (arXiv:2505.15396) experimentally and numerically report sensory-delay-induced localization enhancements; Garcés et al. (arXiv:2604.25745) study effective diffusivity, density scaling and sensory delay in active colloids. Thus *qualitative over-localization and existence of optimal response times are already known* and are not claimed as original. The distinction is the exact rational susceptibility of the exponential-memory telegraph model for every spatial Fourier mode, and the sharp contrast–polarization clocks. Generic Fourier diagonalization is also standard; the physical model-specific law and its classifications are the proposed new contribution.

## Limitations

The result is linear response in a weak periodic landscape. It does not determine finite-amplitude stationary distributions, the effective diffusivity, rectified current at higher order, or systems with additional translational diffusion. The mathematical proof does not assert strict uniqueness of finite-amplitude invariant laws. The most relevant recent preprint has supplemental calculations on delayed transport that were not fully available for inspection; an equivalent unpublished derivation or unindexed source remains possible. No independent scientific audit has been performed.

## References

- C. Rein, K. Kroy and V. Holubec, *Reaction Delays Boost, Rectify, and Reverse Motility in Activity Landscapes*, arXiv:2608.03906 (first public 2026-08-04), https://arxiv.org/abs/2608.03906.
- V. Holubec, A. Fischer, G. Volpe and F. Cichos, *Delayed Active Swimmer in a Velocity Landscape*, arXiv:2505.11042 (first public 2025-05-16), https://arxiv.org/abs/2505.11042.
- U. Töpfer, M. R. Bailey, S. Schreiber, F. Paratore and L. Isa, *Density modulations in active colloidal systems through orthogonal propulsion control and sensory delays*, arXiv:2505.15396 (first public 2025-05-21), https://arxiv.org/abs/2505.15396.
- A. Garcés et al., *Universal transport of active colloids with sensory delay in motility landscapes*, arXiv:2604.25745 (first public 2026-04-28), https://arxiv.org/abs/2604.25745.
