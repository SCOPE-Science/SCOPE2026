# A spectral discriminator for semi-Markov switching harmonic traps

## Finding

For a stationary Brownian particle in a harmonic trap alternating between two **strictly positive** stiffnesses, the integrated position autocovariance is an explicit rational expression in the two residence-time means and the residence-time Laplace transforms evaluated at the first and second harmonic relaxation rates. In contrast, the stationary state-conditioned second moments and average switching work depend only on the means and the transforms at the *second* relaxation rates.

This distinction is genuine: two explicit, nonexponential switching protocols have identical mean residence times, stationary occupations, state-conditioned position second moments, mean potential energy and average injected work, but have **strictly different zero-frequency position power spectra**. The exact spectral separation is \(682008/(919602257\log 2)\) in the two-sided spectral-density convention defined below.

## Assumptions and scope

Let \(A_1,A_2\) denote alternating positive sojourn times. Consecutive sojourns are independent, each phase's sojourns are identically distributed, and the distributions may be discrete, continuous, or mixed. Assume \(0<\tau_i=\mathbb E A_i<\infty\). Construct the two-sided stationary alternating-renewal process \(J_t\in\{1,2\}\) with successive holding times having those laws, independent of a two-sided standard Brownian motion \(B_t\). For arbitrary \(D>0\) and \(\kappa_1,\kappa_2>0\), let the stationary solution be
\[
 dX_t=-\kappa_{J_t}X_t\,dt+\sqrt{2D}\,dB_t.
\]
The strict positivity of both stiffnesses ensures unique finite-variance stationary dynamics and integrable covariance, including for heavy-tailed but finite-mean sojourns. We use \(C(t)=\mathbb E[X_0X_t]\) (the stationary mean vanishes), \(\mathcal I=\int_0^\infty C(t)\,dt\), and the two-sided Fourier convention \(S_X(0)=\int_{-\infty}^{\infty}C(t)\,dt=2\mathcal I\).

For \(i=1,2\), define
\[
 q_i=\frac D{\kappa_i},\quad g_i=\mathbb E e^{-\kappa_i A_i},\quad \ell_i=\mathbb E e^{-2\kappa_i A_i},\quad h_i=\frac{1-g_i}{\kappa_i},\quad T=\tau_1+\tau_2.
\]
Write \(j=3-i\). Define the birth-time second moments
\[
 b_1=q_1+(q_2-q_1)\frac{1-\ell_2}{1-\ell_1\ell_2},\qquad
 b_2=q_2+(q_1-q_2)\frac{1-\ell_1}{1-\ell_1\ell_2},
\]
the fresh-sojourn time-integrated attenuation
\[
 H_1=\frac{h_1+g_1h_2}{1-g_1g_2},\qquad H_2=\frac{h_2+g_2h_1}{1-g_1g_2},
\]
and the auxiliary quantities
\[
 M_i=q_i\tau_i+(b_i-q_i)\frac{1-\ell_i}{2\kappa_i},\qquad
 J_i=q_ih_i+(b_i-q_i)\frac{g_i-\ell_i}{\kappa_i}.
\]
Then the exact zero-frequency response is
\[
 \boxed{\mathcal I=\frac1T\sum_{i=1}^2\left[\frac{M_i}{\kappa_i}+\left(H_{3-i}-\frac1{\kappa_i}\right)J_i\right].}
\]
The state-conditioned stationary second moments are \(M_i/\tau_i\), the total positional variance is \((M_1+M_2)/T\), the phase occupation probabilities are \(\tau_i/T\), and the mean power injected by instantaneous stiffness changes is
\[
 \overline{\dot W}=\frac{(\kappa_1-\kappa_2)(b_1-b_2)}{2T}.
\]
The mean potential energy is exactly \(\mathbb E[\kappa_{J_t}X_t^2/2]=D/2\). In particular, all these static/energetic observables are independent of \(g_1,g_2\) once the means and \(\ell_1,\ell_2\) are fixed, while the spectral response generally is not.

**Explicit same-static-statistics, different-spectrum pair.** Set \(D=1\), \(\kappa_1=2\), \(\kappa_2=1\), and \(c=\log 2\). In both protocols, \(A_1=c\) deterministically. In state 2, \(A_2\) takes values \(c,2c,3c,4c\) with, respectively, probabilities
\[
 P=(1/4,1/4,1/4,1/4),\qquad Q=(9/40,16/40,1/40,14/40).
\]
Both have \(\tau_1=c\), \(\tau_2=5c/2\), \(\ell_1=1/16\), \(\ell_2=85/1024\) and the same birth moments \(b_1=10441/10866\), \(b_2=2873/5433\). Their \(g_2\) values differ: \(15/64\) for \(P\) versus \(19/80\) for \(Q\). The common mean position variance and injected switching power are
\[
 \mathbb E[X^2]=\frac67-\frac{1565}{50708\log2},\qquad
 \overline{\dot W}=\frac{1565}{25354\log2},
\]
while the integrated covariances are exactly
\[
 \mathcal I_P=\frac{11}{14}-\frac{2407701}{24441256\log2},\quad
 \mathcal I_Q=\frac{11}{14}-\frac{2995809}{30526216\log2},
\]
so that
\[
 \boxed{\mathcal I_Q-\mathcal I_P=\frac{341004}{919602257\log2}>0.}
\]
In numerical units, \(\mathcal I_P\approx0.6435948180141233\) and \(\mathcal I_Q\approx0.6441297936255668\).

## Proof

1. **Birth variance recursion.** Within state \(i\), the conditional second moment at elapsed age \(u\) from a switching event is \(V_i(u)=q_i+(b_i-q_i)e^{-2\kappa_i u}\). The current sojourn is independent of the prior birth position, and averaging over its duration yields \(b_{3-i}=q_i+(b_i-q_i)\ell_i\). Solve the two linear equations; the displayed formulas for \(b_i\) follow. Since \(0<\ell_i<1\), all denominators are positive.

2. **Forward attenuation of initial position.** Variation of constants gives \(X_{t+s}=\exp[-\int_t^{t+s}\kappa_{J_v}\,dv]X_t+Z_{t,s}\), where future Brownian increments have conditional mean zero and are independent of the initial position. Thus \(C(s)\) is the stationary expectation of \(X_0^2\exp[-\int_0^s\kappa_{J_v}\,dv]\). Integrating in \(s\) and applying Tonelli is justified because the integrand is nonnegative and bounded in expectation by \(\mathbb E X_0^2e^{-s\min(\kappa_1,\kappa_2)}\).

3. **Fresh-sojourn susceptibility.** From a new entry to phase \(i\), integrate the exponential attenuation up to the next switch and then recursively over subsequent sojourns. This gives \(H_i=h_i+g_iH_{3-i}\), whose unique solution is the displayed \(H_i\) because \(g_1g_2<1\).

4. **Stationary renewal reward.** For a time \(u\) inside a phase-\(i\) sojourn of total length \(a\), the future integrated attenuation equals
\[
 F_i(u,a)=\frac{1-e^{-\kappa_i(a-u)}}{\kappa_i}+e^{-\kappa_i(a-u)}H_{3-i}.
\]
The stationary alternating-renewal reward formula therefore gives
\[
 \mathcal I=\frac1T\sum_i\mathbb E\int_0^{A_i}V_i(u)F_i(u,A_i)\,du.
\]
It requires only finite mean residence durations: the integrand is bounded by \(D/\kappa_{\min}^2\) plus the finite birth-variance contribution. Direct evaluation yields \(\mathbb E\int_0^{A_i}V_i(u)du=M_i\) and
\[
 \mathbb E\int_0^{A_i}V_i(u)e^{-\kappa_i(A_i-u)}du
 =q_ih_i+(b_i-q_i)(g_i-\ell_i)/\kappa_i=J_i.
\]
Substitution proves the boxed formula, with no requirement for differentiable waiting-time densities.

5. **Identical stationary observables but different spectra.** The stationary occupation, second moments, and switching power follow from the same renewal reward identity and from the two stiffness jumps per cycle. The mean potential energy follows independently by stationarity of \(X_t^2\): \(0=-2\mathbb E[\kappa_{J_t}X_t^2]+2D\). For the two specified protocols, the rational relations for their means and transforms are checked exactly. Substitution into the formula yields the displayed rational coefficients and strictly positive spectral difference. Thus neither the set of state-conditioned position variances nor the average switching work identifies the zero-frequency covariance.

## Verification

Run \(\texttt{python verify.py}\) using Python, NumPy and the standard library. The program checks the exact rational two-protocol identities, the birth variance recursions, the equal-stiffness limit, and 240 independent exponential-sojourn comparisons against direct two-state Markov matrix resolvents; all checks passed. The code reconstructs its own formulas and does not require a previously generated file. Exact fraction arithmetic certifies the witness difference; floating-point tests are only corroboration of the general formula and are not its proof.

## Relationship to prior work

Frydel (2026) develops the same semi-Markov two-state fluctuating harmonic trap and gives exact stationary second moments, potential energy and switching work (in particular Eqs. (22)–(25) and (35)–(38)); that stationary and energetic groundwork is not claimed as new. The distinct object here is the *time-integrated stationary two-time position covariance*, together with its explicit dependence on the **additional first-rate transforms** and a pair of holding-time protocols invisible to those previously evaluated observables. The source's complete open-access text focuses on stationary and birth distributions and contains no two-time autocovariance or zero-frequency spectrum theorem.

Behme, Di Tella and Sideris (2022/2024) derive autocovariances for Markov-additive and finite-state Markov-modulated generalized Ornstein–Uhlenbeck processes; memoryless exponential switching is therefore existing ground, and we check that specialization independently. Their finite-state Markov modulator assumption excludes arbitrary nonexponential two-phase waiting laws in the original two-state representation; this finding instead gives a simple closed form for those arbitrary laws. Gupta and Klapp (2025) study continuously Ornstein–Uhlenbeck-modulated stiffness, and Biroli et al. (2023/2024) study stationary *between-particle* correlations under constant-rate dichotomous switching. Neither was identified as stating this semi-Markov zero-frequency formula or the exact spectral non-identifiability witness. General response and renewal theory might yield the expression by further derivation: methodological ancestry is not a claim of originality.

## Limitations

Both stiffnesses must be strictly positive, and each sojourn distribution must have a finite nonzero mean. The free-diffusion or infinite-mean holding-time limits require separate treatment. The asserted non-identifiability is only relative to stationary occupations, state-conditioned **second** moments, potential energy, and mean switching work; the full stationary position distributions and higher moments can differ. No claim of uniqueness against all published or unpublished literature is made. Neither a full frequency-resolved spectrum nor optimal experimental discrimination is established.

## References

- D. Frydel, *Semi-Markovian switching in a fluctuating harmonic trap: An age-structured formulation*, arXiv:2607.05173 (first public version July 6, 2026); *Physical Review E* **114**, 024105 (2026), DOI: 10.1103/7pxv-tg3b. https://arxiv.org/abs/2607.05173 and https://journals.aps.org/pre/pdf/10.1103/7pxv-tg3b
- A. Behme, P. Di Tella and A. Sideris, *On moments of integrals with respect to Markov additive processes and of Markov modulated generalized Ornstein–Uhlenbeck processes*, arXiv:2207.11093 (first public version July 22, 2022), https://arxiv.org/html/2207.11093v2
- D. Gupta and S. H. L. Klapp, *Non-equilibrium fluctuations in a harmonic trap with annealed stochastic stiffness*, *Journal of Statistical Mechanics* 103204 (2025), DOI: 10.1088/1742-5468/ae09a5. https://doi.org/10.1088/1742-5468/ae09a5
- M. Biroli, M. Kulkarni, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570 (2023), https://arxiv.org/abs/2312.02570
