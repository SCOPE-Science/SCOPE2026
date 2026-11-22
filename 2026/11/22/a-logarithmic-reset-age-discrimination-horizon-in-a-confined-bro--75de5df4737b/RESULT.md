# A logarithmic reset-age discrimination horizon in a confined Brownian gas

## Finding

One simultaneous snapshot of a harmonically confined Brownian gas can distinguish two candidate times since its last common reset only up to a sharp logarithmic age scale. The snapshot is conditionally Gaussian; a precisely specified binary experiment yields both an exact finite-population optimal error and a universal Gaussian transition. Averaging **calibrated binary errors** over the stationary distribution of the reference age produces an explicit, noninteger finite-population power law.

Fix positive parameters \(\kappa,D,r,\Delta\), and let \(N\ge1\) be an integer. Suppose an observer is supplied a reference age \(t\ge0\) and knows that the actual time since the last common reset is either \(t\) or \(t+\Delta\), with equal prior probabilities. The observer sees one simultaneous \(N\)-particle position snapshot, but not which of these two candidate ages generated it. Let \(R_N(t)\) be the minimum achievable total misclassification probability, averaged over the two hypotheses.

For \(t>0\), define
\[
q_t=\frac{1-e^{-2\kappa(t+\Delta)}}{1-e^{-2\kappa t}}>1,\qquad
\ell_t=\frac{\log q_t}{q_t-1}.
\]
Then, with \(F_N\) the cumulative distribution function of a chi-square variable with \(N\) degrees of freedom,
\[
\boxed{R_N(t)=\frac12\left[1-F_N(Nq_t\ell_t)+F_N(N\ell_t)\right].}\tag{1}
\]
At \(t=0\), \(R_N(0)=0\). In all cases \(0\le R_N(t)\le1/2\). The optimal test depends on the snapshot only through its squared radius.

Write \(c=1-e^{-2\kappa\Delta}\in(0,1)\). For **every** sequence of reference ages \(t_N\ge0\), the exact detectability classification is
\[
\begin{array}{lll}
\sqrt N e^{-2\kappa t_N}\to\infty &\Longrightarrow& R_N(t_N)\to0,\\
\sqrt N e^{-2\kappa t_N}\to0 &\Longrightarrow& R_N(t_N)\to\frac12,\\
\sqrt N e^{-2\kappa t_N}\to\eta\in(0,\infty)
&\Longrightarrow& R_N(t_N)\to\Phi\!\left(-\frac{c\eta}{2\sqrt2}\right).
\end{array}\tag{2}
\]
Thus the sharp crossover window is \(t_N=(\log N)/(4\kappa)+s\), with fixed \(s\in\mathbb R\), and its limiting risk is
\[
\boxed{R_N\!\left(\frac{\log N}{4\kappa}+s\right)
\longrightarrow\Phi\!\left(-\frac{1-e^{-2\kappa\Delta}}{2\sqrt2}e^{-2\kappa s}\right).}\tag{3}
\]
Here \(\Phi\) is the standard normal distribution function. The transition is independent of the thermal diffusivity \(D\).

Finally, draw the **reference** age \(T\) from the stationary common-reset age distribution \(\operatorname{Exp}(r)\). The binary test remains calibrated to this revealed reference \(T\): the two equally likely alternatives are \(T\) and \(T+\Delta\). Define its mean optimal error
\[
\overline R_N=\mathbb E_T R_N(T)=\int_0^\infty re^{-rt}R_N(t)\,dt.
\]
With \(p=r/(2\kappa)>0\),
\[
\boxed{\overline R_N\sim\frac{2^{2p-1}\Gamma((p+1)/2)}{\sqrt\pi\,(1-e^{-2\kappa\Delta})^p}
N^{-p/2}\qquad(N\to\infty).}\tag{4}
\]
The averaging is over tests with a *known* reference age; it is **not** the Bayes risk for a single test with an unobserved nuisance age or for the unconditional stationary mixture versus a shifted mixture.

## Assumptions and scope

There are \(N\) noninteracting particles on the real line, driven by independent standard Brownian motions. Between resets, for \(i=1,\ldots,N\),
\[
dX_i(u)=-\kappa X_i(u)\,du+\sqrt{2D}\,dB_i(u).
\]
An independent common rate-\(r\) Poisson clock resets all coordinates to zero at each ring. The process has a unique stationary regenerative law. Starting from a common reset, the conditional distribution at age \(t\) is the independent product \(\mathcal N(0,v(t))^{\otimes N}\) with
\[
v(t)=\frac{D}{\kappa}(1-e^{-2\kappa t}).
\]
The binary experiment uses two known candidate ages and equal prior probabilities. All fixed parameters are strictly positive; the large-population limits fix \(\kappa,D,r,\Delta\). No claim is made for an unknown/hidden reference age, unknown diffusion or confinement parameters, non-Gaussian noises, interacting particles, or incomplete observations. The chi-square formula is exact for every finite \(N\) and strictly positive reference age, with the degenerate \(t=0\) limit handled separately.

## Proof

**Exact optimal test.** For fixed \(t>0\), let \(v_0=v(t)\), \(v_1=v(t+\Delta)=q_tv_0\). The conditional joint densities for the snapshot \(x=(x_1,\ldots,x_N)\) are centered Gaussian products. Their log likelihood ratio (second age against first) is
\[
\log\frac{f_1(x)}{f_0(x)}=-\frac N2\log q_t
+\frac12\left(\frac1{v_0}-\frac1{v_1}\right)\sum_{i=1}^N x_i^2.
\]
With equal priors, Neyman–Pearson chooses the older age when \(\sum_i x_i^2>Nv_0q_t\log q_t/(q_t-1)\). Under the younger hypothesis, the squared radius divided by \(v_0\) is \(\chi_N^2\); under the older hypothesis, division by \(v_1\) gives the same chi-square law. Averaging the two error tails proves (1). At zero age the younger law is a point mass at the origin while the older law is absolutely continuous, giving zero error.

**A uniform vanishing-error bound.** Put \(z=e^{-2\kappa t}\in(0,1)\), so
\[
q_t=1+\frac{cz}{1-z}.
\]
The Hellinger affinity between the two product Gaussian laws is \(H_N=h^N\), where
\[
h=\left(\frac{2\sqrt{q_t}}{1+q_t}\right)^{1/2},\qquad
h^4=1-\left(\frac{cz}{2-(2-c)z}\right)^2.
\]
Since \(-\log(1-y)\ge y\) for \(0\le y<1\), and the denominator in the displayed fraction does not exceed two, the optimal risk obeys the **global bound**
\[
0\le R_N(t)\le\frac12H_N\le\frac12\exp\!\left(-\frac{Nc^2e^{-4\kappa t}}{16}\right).\tag{5}
\]
This includes the \(t=0\) case by continuity. If \(\sqrt N e^{-2\kappa t_N}\to\infty\), the right side tends to zero. If instead \(\sqrt N e^{-2\kappa t_N}\to0\), then \(z_N\to0\) and \(N(q_{t_N}-1)^2\to0\). The exact affinity formula gives \(H_N\to1\). The elementary Hellinger/total-variation inequality \(\|P_0-P_1\|_{\mathrm{TV}}\le\sqrt{1-H_N^2}\), together with \(R_N=(1-\|P_0-P_1\|_{\mathrm{TV}})/2\), proves convergence to \(1/2\).

**Critical Gaussian window.** Suppose \(\sqrt N z_N\to\eta\in(0,\infty)\). Then \(q_{t_N}=1+c\eta/\sqrt N+o(N^{-1/2})\). Taylor expansion at one gives
\[
\frac{\log q}{q-1}=1-\frac{q-1}{2}+O((q-1)^2),\quad
\frac{q\log q}{q-1}=1+\frac{q-1}{2}+O((q-1)^2).
\]
Therefore the two chi-square cutoffs in (1), centered at \(N\) and divided by \(\sqrt{2N}\), tend respectively to \(c\eta/(2\sqrt2)\) and \(-c\eta/(2\sqrt2)\). The chi-square central limit theorem implies (2) in the critical case; substitution of \(t_N=(\log N)/(4\kappa)+s\) proves (3). The first two regimes and the critical regime cover every claimed sequence.

**Stationary-age average.** The backward age of a homogeneous Poisson clock is exponentially distributed with rate \(r\). Put \(p=r/(2\kappa)>0\) and substitute \(u=\sqrt N e^{-2\kappa t}\). Then exactly
\[
N^{p/2}\overline R_N
=p\int_0^{\sqrt N}u^{p-1}R_N\!\left(\frac{\log(\sqrt N/u)}{2\kappa}\right)du.
\]
For every fixed \(u>0\), the critical-window theorem makes the risk inside the integral tend to \(\Phi(-cu/(2\sqrt2))\). Bound (5) dominates the whole integrand by \((1/2)u^{p-1}e^{-c^2u^2/16}\), integrable on \((0,\infty)\) for every \(p>0\). Dominated convergence yields
\[
\lim_{N\to\infty}N^{p/2}\overline R_N
=p\int_0^\infty u^{p-1}\Phi\!\left(-\frac{cu}{2\sqrt2}\right)du.
\]
Interchange the Gaussian-tail integral using Tonelli to obtain
\[
p\int_0^\infty u^{p-1}\Phi(-Cu)du
=C^{-p}\int_0^\infty y^p\frac{e^{-y^2/2}}{\sqrt{2\pi}}dy
=\frac{2^{2p-1}\Gamma((p+1)/2)}{\sqrt\pi\,c^p},\quad C=\frac c{2\sqrt2}.
\]
This positive finite value proves the complete equivalent (4), not merely an upper or lower order bound.

## Verification

The standalone `verify.py` requires Python 3, SciPy and its NumPy dependency. Running `python3 verify.py` reproduces exact chi-square likelihood thresholds, checks the location and profile of the Gaussian window against large finite populations, and numerically evaluates the stationary-age integral against the exact asymptotic coefficient across three distinct parameter regimes. It also checks the exponential affinity bound and the Gaussian-tail integral for the analytic constant. A successful execution prints `PASS`. These are finite numerical checks complementing the analytic proof; no numerical experiment is used as an infinite-population proof.

## Relationship to prior work

De Mauro, Majumdar and Schehr (arXiv:2606.31634, first public posting 2026-06-30) establish the shared-Poisson-reset Brownian gas under harmonic confinement and its stationary conditionally independent joint law, positional correlations and extreme/gap statistics. The conditional centered Gaussian mixture and reset-age distribution used here are **known** from that work. The assessed claim instead concerns a pairwise age-classification experiment: optimal snapshot decisions, the sharp \((\log N)/(4\kappa)\) time-resolution threshold, its full Gaussian profile and the stationary-reference-age averaged exponent and coefficient.

Two closely related accessible mathematical-physics findings analyze (a) the stationary collective energy beta law and covariance, and (b) collective-energy rare tails near the equilibrium edge, both using the same age-mixture model. Their full `RESULT.md` statements were inspected. They do not state the age-classification likelihood test or its calibrated Bayes-error law, and the collective-energy marginal tail alone does not determine the optimal likelihood boundary between two *fixed* conditional ages. Standard Neyman–Pearson testing of centered Gaussians, the chi-square central limit theorem, and Hellinger inequalities are classical and fully credited as proof ingredients; novelty is not asserted for these generic tools, the model, or the stationary mixture.

## Limitations

The average in (4) is over **calibrated binary tests**: a fresh reference age is drawn from the stationary reset-age distribution and revealed to the observer before discrimination between that age and the age offset by \(\Delta\). This average must not be misidentified with hidden-age estimation or an unconditional mixture-against-mixture Bayes risk. The snapshot contains all particle positions, the thermal diffusivity and harmonic relaxation are known, the candidate ages are exact, and the two hypotheses have equal priors. The result does not quantify robustness to measurement noise, incomplete particle sampling, model mismatch, or inference of the reset rate itself. The full 67-page primary preprint could not be materially inspected in this check despite attempts to access open versions; its public abstract, scientific summaries and closely related full results were inspected. A prior publication or supplemental discussion stating the same discrimination theorem could therefore supersede the originality assessment. Independent scientific and priority validation has not been performed.

## References

1. G. de Mauro, S. N. Majumdar and G. Schehr, *Effects of confinement in a Brownian gas with simultaneous stochastic resetting and dynamically emergent correlations*, arXiv:2606.31634 (first submitted 2026-06-30), https://arxiv.org/abs/2606.31634.
2. P. C. Bressloff, *Global density equations for interacting particle systems with stochastic resetting: from overdamped Brownian motion to phase synchronization*, arXiv:2401.03501 (first submitted 2024-01-07), https://arxiv.org/abs/2401.03501.
3. G. de Mauro, M. Biroli, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658 (2025), https://arxiv.org/abs/2509.06658.
4. *A beta-law for macroscopic energy in globally reset harmonic Brownian gases*, accessible mathematical research note, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-beta-law-for-macroscopic-energy-in-globally-reset-harmonic-bro--e140ac2fc363.
5. *Sharp resetting fingerprints in collective energy tails of a confined Brownian gas*, accessible mathematical research note, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-resetting-fingerprints-in-collective-energy-tails-of-a-con--e3f475057006.
