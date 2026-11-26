# A sharp one-ninth duty-cycle threshold for weak flashing-potential diffusion enhancement

## Finding

The **quadratic weak-force correction** to the effective diffusivity of a Brownian particle in a Poisson-redrawn on/off sinusoidal force is positive for some redraw rate if and only if the on-state duty fraction is strictly below \(1/9\). For each such fraction, the rates with positive quadratic correction form a bounded open interval. Equal-duty flashing has a strictly negative quadratic correction at every positive redraw rate.

More precisely, let \(a=Dk^2\), \(z=r/a\). For fixed \(D,k,r>0\) and \(q\in(0,1)\),
\[
D_{\mathrm{eff}}(\varepsilon)=D+\varepsilon^2 A_2(q,z)+O_{D,k,r,q}(\varepsilon^4),\qquad
A_2(q,z)=\frac{q}{2a}\left[-q+\frac{(1-q)(z-1)}{(z+1)^2}\right].
\]
For each \(q\), the unique maximizer of \(A_2\) over \(z>0\) is \(z=3\), with value \(q(1-9q)/(16a)\). If \(q<1/9\), then \(A_2>0\) precisely for \(z_-<z<z_+\), with
\[
z_\pm=\frac{1-3q\pm\sqrt{(1-q)(1-9q)}}{2q}.
\]
The coefficient vanishes at those endpoints and is negative outside the closed interval. If \(q>1/9\), it is negative for every \(z>0\). If \(q=1/9\), it is negative except at \(z=3\), where it is zero.

Where \(A_2\ne0\), its sign determines the sign of \(D_{\mathrm{eff}}-D\) for all sufficiently small nonzero \(\varepsilon\) at the given parameters. No sign conclusion for \(D_{\mathrm{eff}}-D\) follows from this quadratic theorem where \(A_2=0\). The maximizing rate stated above is for \(A_2\), not for finite nonzero amplitudes.

## Assumptions and scope

The unwrapped position solves
\[
dX_t=\varepsilon S_t\sin(kX_t)\,dt+\sqrt{2D}\,dB_t.
\]
Here \(B_t\) is standard Brownian motion. Independent of it, \(S_t\in\{0,1\}\) is redrawn at the events of a Poisson process of rate \(r\); each draw is independently one with probability \(q\). Events that leave \(S_t\) unchanged are allowed. The actual state-transition rates are \(rq\) for \(0\to1\) and \(r(1-q)\) for \(1\to0\). The effective diffusivity is \(\lim_{t\to\infty}\operatorname{Var}(X_t)/(2t)\), from any fixed initial state. Effective drift is zero. The expansion is pointwise as \(\varepsilon\to0\), holding all other parameters fixed.

## Proof

**1. Periodic generator and symmetries.** Put \(L=2\pi/k\), \(\pi=(1-q,q)\), and fold position modulo \(L\). For periodic functions \(g=(g_0,g_1)\) the backward generator is
\[
(\mathcal L_\varepsilon g)_s=D\partial_x^2g_s+\varepsilon s\sin(kx)\partial_x g_s+r\left(\sum_u\pi_u g_u-g_s\right).
\]
The elliptic, irreducibly switching system on the compact circle has a unique smooth invariant probability density \(\rho_{\varepsilon,s}\). At zero force the only zero eigenvalue corresponds to a common constant, and on the complementary modes the generator is bounded away from zero: the nonzero spatial modes have decay rates \(D m^2 k^2\) or \(D m^2 k^2+r\), and the nonconstant internal mode at spatial frequency zero decays at rate \(r\). Analytic perturbation of the normalized stationary and centered Poisson equations near zero force gives analytic densities and correctors. The reflection \(x\mapsto-x\) leaves the folded dynamics invariant and reverses the local drift, so the invariant mean drift is zero. Translation by \(\pi/k\) changes \(\varepsilon\) to \(-\varepsilon\) and leaves asymptotic variance unchanged.

**2. First-order fields.** Let
\[
C_s=\frac q a+\frac{s-q}{a+r},\qquad aC_s+r\left(C_s-\sum_u\pi_u C_u\right)=s .
\]
The first-order stationary forward equation and the Poisson equation \(-\mathcal L_\varepsilon\chi_{\varepsilon,s}=\varepsilon s\sin(kx)\) then give
\[
\rho_{\varepsilon,s}=\frac{\pi_s}{L}\,[1-\varepsilon kC_s\cos(kx)]+O(\varepsilon^2),\qquad
\chi_{\varepsilon,s}=\varepsilon C_s\sin(kx)+O(\varepsilon^2).
\]
For the stationary equation this follows by division by \(\pi_s/L\), since Poisson refresh is reversible with respect to \(\pi\) and the forcing of the forward equation is a cosine. In the backward equation the right-hand side is a sine. The expansions hold in periodic norms controlling the derivatives used below.

**3. Variance formula.** The lifted coordinate \(X_t+\chi_{\varepsilon,S_t}(X_t)\) differs from \(X_t\) by a bounded term and has zero drift by the Poisson equation. Its predictable quadratic variation consists of a continuous part from \(B_t\) and a squared jump at each redraw. Dividing its variance by \(2t\) and taking the ergodic limit gives
\[
D_{\mathrm{eff}}=D\sum_s\int_0^L\rho_{\varepsilon,s}(1+\partial_x\chi_{\varepsilon,s})^2\,dx+
\frac r2\sum_{s,u}\pi_u\int_0^L\rho_{\varepsilon,s}(\chi_{\varepsilon,u}-\chi_{\varepsilon,s})^2\,dx.
\]
The bounded corrector does not affect the limit: its variance is bounded, and its covariance with the martingale is \(O(\sqrt{t})\). Periodic derivatives integrate to zero against the unperturbed spatially constant density. At order two the term linear in the derivative and the squared derivative give, respectively, \(-a\mathbb E_\pi C_S^2\) and \(a\mathbb E_\pi C_S^2/2\); the jump contribution is \(r\operatorname{Var}_\pi(C_S)/2\). The factor \(1/2\) from spatial averaging is the mean of the squared sine or cosine. Thus
\[
A_2=\frac12[-a\mathbb E_\pi C_S^2+r\operatorname{Var}_\pi(C_S)]
=-\frac{q^2}{2a}+\frac{q(1-q)(r-a)}{2(a+r)^2}.
\]
This is the claimed coefficient. Analyticity and the half-period translation eliminate odd powers, giving the stated remainder.

**4. Sign and maximum.** The sign is the sign of \(-P_q(z)\), where \(P_q(z)=qz^2+(3q-1)z+1\). The discriminant is \((1-q)(1-9q)\). For \(0<q<1/9\) the two roots are distinct and positive (their sum and product are positive), giving precisely the indicated positive-coefficient interval. For \(q>1/9\) the polynomial is positive, and for \(q=1/9\) it is \((z-3)^2/9\). Finally,
\[
\frac{d}{dz}\left[-q+\frac{(1-q)(z-1)}{(1+z)^2}\right]=\frac{(1-q)(3-z)}{(1+z)^3}.
\]
The bracket increases up to \(3\) and decreases afterwards; its value there is \((1-9q)/8\). This proves all claims about \(A_2\).

## Verification

`CHECK.py` in the accompanying original package (unchanged) constructs the two-state stationary forward operator and solves the backward Poisson equation by Fourier collocation. It includes redraw jumps in the computed diffusivity. For example, when \(D=k=1, q=1/20,r=3\), the exact quadratic coefficient is \(0.00171875\), which the quotients at successive small amplitudes approximate. These finite checks corroborate the analytic expansion and do not certify a finite-amplitude sign diagram.

## Relationship to prior work and limits

Frydel [1] gives a general homogenization and stochastic-duality framework for Poisson-redrawn force states, including an equal-duty triangular on/off example without observed enhancement in the studied parameter range. The general method is not claimed as new. The calculation here resolves the unequal-duty single-sinusoid quadratic response explicitly: the static mean-force correction is negative and competes with the variance-driven dynamic correction. The known results for symmetric switching between opposite signed potentials [2] concern a different model; the centered response alone lacks the static mean term. The claim is only the exact quadratic sign and rate classification for Bernoulli-redrawn on/off sine forcing, not a claim for other spatial profiles, switches, force amplitudes, or simultaneous parameter limits. Priority against equivalent analyses outside the checked literature remains open.

## References

1. D. Frydel, *A new representation of effective diffusion in fluctuating periodic potentials through stochastic duality*, arXiv:2611.13526, especially Secs. II–III, XI and the zero-current representation in Sec. XII. https://arxiv.org/abs/2611.13526
2. B. Spagnolo and A. Dubkov, *Diffusion in Flashing Periodic Potentials*, arXiv:cond-mat/0510170, Sec. III. https://arxiv.org/abs/cond-mat/0510170
3. S. Lifson and J. L. Jackson, *On the self-diffusion of ions in a polyelectrolyte solution*, J. Chem. Phys. 36, 2410 (1962), fixed-potential comparison. https://doi.org/10.1063/1.1732899
