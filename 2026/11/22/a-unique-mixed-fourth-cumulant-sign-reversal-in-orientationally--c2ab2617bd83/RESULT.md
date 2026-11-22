# A unique mixed-fourth-cumulant sign reversal in orientationally reset active Brownian motion

## Finding
For a freely translating planar active Brownian swimmer whose *orientation alone* is reset to a fixed laboratory direction at independent Poisson times, the long-time connected fourth displacement correlation between the longitudinal and transverse coordinates has exactly one positive resetting-rate sign reversal. This crossover is not visible from the two marginal variances and does not rely on positional resetting.

Let \(D_{\mathrm{rot}}>0\) be rotational diffusivity, \(r>0\) orientational reset rate, \(v>0\) swimming speed, and \(D_T\ge0\) independent isotropic translational diffusivity. Write \(q=r/D_{\mathrm{rot}}\) and
\[
P(q)=461q^5+6696q^4+28515q^3+30686q^2-26586q-9072.
\]
Let \(\kappa_{2,2}(t)=\operatorname{cum}(X_t,X_t,Y_t,Y_t)\) denote the joint fourth cumulant of the displacement measured along and transverse to the reset direction. Then, for every permitted parameter choice and from any fixed initial angular distribution,
\[
\boxed{\lim_{t\to\infty}\frac{\kappa_{2,2}(t)}{t}
=\frac{16v^4}{D_{\mathrm{rot}}^3}\,
\frac{P(q)}{(q+1)^5(q+4)^3(q+9)^2(q+16)}.}
\]
The polynomial has exactly one positive root \(q_*=0.716876436691030\ldots\), strictly between \(0.71687\) and \(0.71688\). Therefore the limit is strictly negative for \(0<q<q_*\), zero precisely at \(q=q_*\), and strictly positive for \(q>q_*\). The root is simple. Its location and the whole sign classification are independent of \(v\) and \(D_T\). There is no claim that a zero asymptotic cumulant rate means stochastic independence or vanishing finite-time covariance.

When the angle initially has its invariant law, reflection in the horizontal axis yields \(\mathbb E Y_t=\operatorname{Cov}(X_t,Y_t)=0\) for all times, so the cumulant is exactly the covariance of the two **centered squared displacements**, \(\kappa_{2,2}(t)=\operatorname{Cov}[(X_t-\mathbb E X_t)^2,Y_t^2]\). Its sign here is characterized only in the long-time linear growth coefficient.

## Assumptions and scope
The angle \(\Theta_t\) takes values on the circle \(\mathbb R/(2\pi\mathbb Z)\) and between resets obeys \(d\Theta_t=\sqrt{2D_{\mathrm{rot}}}\,dW_t\). At the epochs of an independent rate-\(r\) Poisson process it is set to angle zero. There is no angular drift or chirality and no spatial confinement. The planar displacement, relative to its initial position, is
\[
\begin{aligned}
dX_t&=v\cos(\Theta_t)\,dt+\sqrt{2D_T}\,dB_t^x,\\
dY_t&=v\sin(\Theta_t)\,dt+\sqrt{2D_T}\,dB_t^y,
\end{aligned}
\]
with independent Brownian noises. Position is never reset, and the result concerns cumulant rates \(t\to\infty\) for fixed parameters, not the instantaneous cumulants at finite \(t\). The orientation may start stationary or from any deterministic angle (more generally, any fixed angular probability law). The admissible diffusion parameters include \(D_T=0\).

## Proof
**1. Analytic cumulant eigenvalue.** Rescale time by \(D_{\mathrm{rot}}\) and consider the generator on twice continuously differentiable periodic functions,
\[
(Lf)(\theta)=f''(\theta)+q[f(0)-f(\theta)].
\]
At zero tilt this has a simple zero eigenvalue with remaining spectrum in the left half-plane, bounded away from zero: for each nonzero Fourier mode the triangular Fourier representation has diagonal \(-(q+n^2)\). For sufficiently small complex \((u,w)\), the bounded analytic perturbation \(L+u\cos\theta+w\sin\theta\) consequently has a unique simple analytic principal eigenvalue \(\Lambda_q(u,w)\) satisfying \(\Lambda_q(0,0)=0\). Positivity of the circle heat kernel with renewal resets and spectral isolation give a nonvanishing spectral projection of the initial density. Feynman–Kac therefore implies uniform analytic convergence of the cumulant-generating function per unit time to this eigenvalue on a neighborhood of zero. Differentiating four times is legitimate. Independent spatial Brownian motion adds only \(D_T(k_x^2+k_y^2)\) to the physical eigenvalue, whose mixed fourth derivative vanishes. Dimensional rescaling yields
\[
\lim_{t\to\infty}\frac{\operatorname{cum}(X_t,X_t,Y_t,Y_t)}t
=\frac{v^4}{D_{\mathrm{rot}}^3}
\left.\partial_u^2\partial_w^2\Lambda_q(u,w)\right|_{u=w=0}.
\]

**2. Exact finite harmonic perturbation.** Let \(h_+=(u-iw)/2\) and \(h_-=(u+iw)/2\). Expand the normalized right eigenfunction in angular Fourier series, \(\psi(\theta)=\sum_{n\in\mathbb Z}c_n e^{in\theta}\), normalized by \(\psi(0)=\sum_n c_n=1\). Use homogeneous-degree expansions \(\Lambda_q=\sum_{j\ge1}\Lambda^{[j]}\), \(c_n=\sum_{j\ge0}c_n^{[j]}\), with \(c_0^{[0]}=1\) and other degree-zero coefficients zero. Multiplication by \(u\cos\theta+w\sin\theta\) sends the Fourier coefficient at \(n\) to \(h_+c_{n-1}+h_-c_{n+1}\). The nonzero angular frequencies obey, for \(m\ge1\),
\[
 c_n^{[m]}=\frac{h_+c_{n-1}^{[m-1]}+h_-c_{n+1}^{[m-1]}
 -\sum_{j=1}^{m-1}\Lambda^{[j]}c_n^{[m-j]}}{q+n^2},\qquad n\ne0.
\]
The normalization and zero-frequency equation give
\[
\begin{aligned}
c_0^{[m]}&=-\sum_{n\ne0}c_n^{[m]},\\
\Lambda^{[m]}&=q\sum_{n\ne0}c_n^{[m]}+h_+c_{-1}^{[m-1]}+h_-c_1^{[m-1]}
-\sum_{j=1}^{m-1}\Lambda^{[j]}c_0^{[m-j]}.
\end{aligned}
\]
At degree \(m\), only \(|n|\le m\) are accessible from the constant unperturbed eigenfunction. Consequently computing through degree four uses **exactly finitely many Fourier coefficients**, with no unproved truncation of the infinite generator. Exact symbolic reduction gives
\[
[ u^2w^2 ]\,\Lambda^{[4]}
=4\frac{P(q)}{(q+1)^5(q+4)^3(q+9)^2(q+16)}.
\]
Here \([u^2w^2]\) denotes the coefficient of the indicated monomial, so applying \(\partial_u^2\partial_w^2\) introduces a factor four. This proves the displayed formula. As a check against established transport, the same recurrence gives \(\partial_u\Lambda_q(0)=q/(q+1)\), longitudinal variance growth \(2v^2(2+5q)/[D_{\mathrm{rot}}(q+1)^3(q+4)]\) before adding \(2D_T\), and transverse variance growth \(4v^2/[D_{\mathrm{rot}}(q+1)(q+4)]\) before adding \(2D_T\).

**3. Exact uniqueness of the crossover.** The sequence of coefficients of \(P(q)\) in descending order is positive, positive, positive, positive, negative, negative. It has exactly one sign change; by Descartes' rule of signs the polynomial has at most one positive real root, counted with multiplicity. Direct exact rational substitutions verify
\[
P(71687/100000)<0,\qquad P(71688/100000)>0.
\]
Continuity supplies a positive root in that interval, and Descartes' count forces the root to be the only positive root and to be simple. The denominator is positive for every \(q>0\). The negative sign at zero and positive leading coefficient then prove the global negative–zero–positive classification. The boundary values are \(\lim_{q\downarrow0}\partial_u^2\partial_w^2\Lambda_q=-7/4\) and \(\lim_{q\to\infty}q^6\partial_u^2\partial_w^2\Lambda_q=7376\). They are separate limiting checks, not additional claims of a uniform two-parameter limit.

## Verification
Run `python checker.py` with Python 3 and the packages `sympy` and `numpy`. The script reconstructs the bivariate fourth-order Fourier recursion from the generator, verifies the full exact rational identity, independently obtains all three projected fourth cumulants on the longitudinal, transverse and diagonal axes by separate univariate eigenfunction recurrences, and recovers the mixed cumulant using the fourth-order polarization identity. It also performs exact Descartes/root-bracket checks, boundary limits, the known second-cumulant normalizations, and diagnostic Fourier-matrix Cauchy integrals at five distinct rates. The standalone code passed 26 assertions. The Cauchy-integral finite matrix tests are diagnostic only; the analytic spectral argument, exact degree-four finite recurrence and Descartes theorem establish the infinite-time and global-parameter claims.

## Relationship to prior work
Baouche, Franosch, Meiners and Kurzthaler (2024) study precisely this orientation-only resetting process and derive the intermediate scattering function and separate horizontal and vertical low-order moments, including marginal fourth moments. The intermediate scattering function in principle encodes all joint cumulants, but the inspected main text and appendices do not state the mixed fourth-cumulant coefficient or its global one-root classification. Kumar, Sadekar and Basu (2020) treat orientation-only resetting and the transition to long-time Gaussian displacement, focusing on separate marginal observables and second moments. Gaussian central-limit behavior does not force the sign of a fourth-cumulant *linear growth rate*.

A published result on the same active model establishes two sign changes of the *sixth longitudinal* cumulant, but not the fourth *mixed longitudinal–transverse* cumulant. A separate published result derives a *mixed third* cumulant and a different off-axis angular optimization threshold. Another study proves fourth-cumulant angular isotropy for a *passive anisotropic* Brownian particle whose diffusivity tensor, rather than active propulsion, couples to its reset orientation. These distinct observables and dynamics do not imply the present explicit mixed-fourth sign reversal. Nevertheless, the source's broad characteristic-function representation is prior coverage of the full law, and equivalent unindexed differentiations remain a publication-priority risk.

## Limitations
The theorem concerns long-time cumulant slopes at each fixed strictly positive reset rate; it makes no claim that the finite-time cumulant has the same sign, that the coordinates become independent at the threshold, or that the zero fourth cumulant rate makes the full law Gaussian. The local angular state is renewed to a deterministic heading at Poisson times; alternative angular laws, chiral drift, interactions, varying speeds, correlated translational/rotational noise and positional resetting are not covered. At extremely fast resetting, the positive signal becomes small, with decay proportional to the sixth inverse power of \(r/D_{\mathrm{rot}}\), making finite-sample estimation harder. The original model and its general transform are established prior work; priority of this exact specialization has not undergone independent audit.

## References
1. Y. Baouche, T. Franosch, M. Meiners and C. Kurzthaler, *Active Brownian particle under stochastic orientational resetting*, arXiv:2405.06769v1, first public 2024-05-10, https://arxiv.org/abs/2405.06769 .
2. V. Kumar, O. Sadekar and U. Basu, *Active Brownian Motion in two-dimensions under Stochastic Resetting*, arXiv:2008.03294v1 (2020), https://arxiv.org/abs/2008.03294 .
3. *Exactly two sign reversals of the sixth displacement cumulant under orientational resetting* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exactly-two-sign-reversals-of-the-sixth-displacement-cumulant-un--e5c2b28f4c35 .
4. *A sharp off-axis third-cumulant transition for orientationally reset active Brownian motion* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-off-axis-third-cumulant-transition-for-orientationally-r--feb740e47874 .
5. *Sharp fourth-cumulant isotropy under orientation-only resetting of an anisotropic Brownian particle* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-fourth-cumulant-isotropy-under-orientation-only-resetting--403d011b461a .
