# A sharp sign transition in successive-cycle work correlations of an active information engine

## Finding

A periodically measured harmonic information engine with a **Gaussian active Ornstein–Uhlenbeck bath**, independent thermal noise, independent Gaussian measurement errors and *full-shift* feedback has an exact work-autocovariance hierarchy. The correlation of work extracted in two immediately successive cycles can be strictly negative, whereas correlations at every separation of at least two cycles are strictly positive. A sharp active-force-amplitude criterion determines whether the nearest-cycle covariance switches sign exactly once as the cycle period increases.

Write \(a=\kappa/\gamma>0\) for the trap relaxation rate, \(b>0\) for the active-bath correlation decay rate, \(\tau>0\) for the cycle period, \(\sigma^2>0\) for the independent measurement-error variance, and \(A^2>0\) for the active-force variance. Let \(W_n\) denote the extracted work in cycle \(n\), and set \(h=e^{-a\tau}\). Define the strictly positive adjacent-cycle active-force integral covariance

\[
K(\tau)=\frac{A^2}{\gamma^2}\begin{cases}
\displaystyle\frac{(1-e^{-(a+b)\tau})(e^{-b\tau}-e^{-a\tau})}{a^2-b^2},&a\ne b,\\[5pt]
\displaystyle\frac{\tau e^{-a\tau}(1-e^{-2a\tau})}{2a},&a=b.
\end{cases}
\]

Then for every integer \(\ell\ge1\) and every cycle index in the stationary regime,

\[
\operatorname{Cov}(W_n,W_{n+\ell})=\frac{\kappa^2}{2}\begin{cases}
K(\tau)^2-e^{-2a\tau}\sigma^4,&\ell=1,\\
K(\tau)^2e^{-2b(\ell-1)\tau},&\ell\ge2.
\end{cases}
\]

Define the increasing function \(G_{a,b}(\tau)=e^{a\tau}\gamma^2K(\tau)/A^2\):

\[
G_{a,b}(\tau)=\begin{cases}
\displaystyle\frac{(1-e^{-(a+b)\tau})(e^{(a-b)\tau}-1)}{a^2-b^2},&a\ne b,\\[5pt]
\displaystyle\frac{\tau(1-e^{-2a\tau})}{2a},&a=b.
\end{cases}
\]

The adjacent-cycle covariance changes from strictly negative to strictly positive **exactly once** as \(\tau\) ranges over positive values if and only if either \(b\le a\), or \(b>a\) and

\[
A^2>\gamma^2\sigma^2(b^2-a^2).
\]

If \(b>a\) and \(A^2\le\gamma^2\sigma^2(b^2-a^2)\), the adjacent-cycle covariance remains strictly negative at *every finite* positive cycle period. Whenever a switch exists, its unique period is the solution of \(G_{a,b}(\tau_*)=\gamma^2\sigma^2/A^2\); equality produces a single zero, not a sign reversal at multiple periods. For every finite \(\tau>0\), all lags \(\ell\ge2\) have strictly positive covariance.

## Assumptions and scope

The overdamped position satisfies \(\gamma\dot x_t=-\kappa(x_t-\lambda_t)+\xi_t+\eta_t\) between interventions. The thermal noise is centered Gaussian white noise with \(\mathbb E[\xi_t\xi_s]=2\gamma k_{\mathrm B}T\delta(t-s)\), with \(T\ge0\). The independent, stationary, centered *Gaussian* active force satisfies \(\mathbb E[\eta_t\eta_s]=A^2e^{-b|t-s|}\). The measurement error \(\epsilon_n\sim N(0,\sigma^2)\) is independent across cycles and independent of both noises. Feedback is instantaneous and uses the full measured displacement (gain one), moving the trap center by the pre-feedback relative position plus measurement error. The active force is *not* reset. The cycle index ranges over a two-sided stationary realization, which removes initial transients.

Let \(Y_n=x_{n\tau-}-\lambda_{n\tau-}\) be the pre-feedback relative displacement, so the post-feedback displacement equals \(-\epsilon_n\). The extracted feedback work is exactly \(W_n=(\kappa/2)(Y_n^2-\epsilon_n^2)\). This is a work-fluctuation result, not a claim about heat, total entropy production or any feedback protocol with gain other than one.

## Proof

**1. Cycle decomposition.** Solving the linear Langevin equation on one cycle gives

\[
Y_n=-h\epsilon_{n-1}+B_n,\qquad
B_n=\gamma^{-1}\!\int_{(n-1)\tau}^{n\tau}e^{-a(n\tau-u)}[\xi_u+\eta_u] \,du.
\]

Here the jointly Gaussian sequence \((B_n)\) is independent of all \(\epsilon_j\). White-noise cycle integrals are independent at distinct cycle indices. For \(\ell\ge1\), the colored-noise covariance factorizes over disjoint intervals and yields

\[
\operatorname{Cov}(B_n,B_{n+\ell})=
\frac{A^2}{\gamma^2}e^{-b(\ell-1)\tau}
\left(\int_0^\tau e^{-a(\tau-u)}e^{-b(\tau-u)}du\right)
\left(\int_0^\tau e^{-a(\tau-v)}e^{-bv}dv\right).
\]

The product of the two displayed positive integrals is \(K(\tau)\gamma^2/A^2\) when \(\ell=1\). Evaluating them gives the piecewise formula above, with the removable equal-rate limit. Consequently \(\operatorname{Cov}(Y_n,Y_{n+\ell})=K(\tau)e^{-b(\ell-1)\tau}\), while \(\operatorname{Cov}(\epsilon_n,Y_{n+\ell})=-h\sigma^2\mathbf1_{\{\ell=1\}}\) and \(\operatorname{Cov}(Y_n,\epsilon_{n+\ell})=0\).

**2. Work covariance.** Every variable involved is jointly centered Gaussian. For centered Gaussian \(U,V\), Isserlis' formula gives \(\operatorname{Cov}(U^2,V^2)=2\operatorname{Cov}(U,V)^2\). Expanding \(W_n=(\kappa/2)(Y_n^2-\epsilon_n^2)\) against \(W_{n+\ell}\) gives exactly the two lag regimes in the Finding. The negative adjacent-lag term comes solely from the measurement error propagated into the next cycle; all other cross-cycle terms are positive squares of the active-bath covariance.

**3. Sharp threshold.** Since \(K>0\), the sign of the lag-one covariance is the sign of \(e^{a\tau}K-\sigma^2\). For \(a>b\), \(G_{a,b}\) is a product of two strictly increasing positive functions divided by a positive constant. For \(b>a\), rewrite it as \((1-e^{-(a+b)\tau})(1-e^{-(b-a)\tau})/(b^2-a^2)\), also strictly increasing. The equal-rate formula is strictly increasing as well. All cases start from zero. As \(\tau\to\infty\), \(G_{a,b}\) tends to infinity if \(b\le a\), and tends from below to \(1/(b^2-a^2)\) if \(b>a\). Comparing its range with \(\gamma^2\sigma^2/A^2\) proves the exhaustive phase classification and uniqueness of the crossing. No finite limit at an infinite period is incorrectly counted as a crossing.

## Verification

The included standalone Python script `verify.py` implements the closed covariance formulas, checks the active-force adjacent and diagonal covariance against direct two-dimensional numerical quadrature for both nonresonant and resonant rates, checks the factorization and monotonicity at 1,200 grid points, and compares the analytical lag-one and lag-two work covariances to independent Gaussian Monte Carlo samples across both sides of the threshold. The script was run successfully in Python 3 with NumPy. The proof above, not these finite numerical tests, establishes the results for all allowed parameter values, cycle indices and lags.

## Relationship to prior work

Bahng, Lee and Ghim (2025) introduced the active-bath harmonic feedback setup and developed one-cycle mean-work, power and pre/post-feedback covariance laws, explicitly recognizing higher work moments as a further direction. Their model's full-shift special case supplies the present starting dynamics, but does not imply a comparison of work at two distinct cycles without additional cross-cycle covariance and Gaussian fourth-moment calculations. Paneru and colleagues (2020) obtained the distribution and variance of *individual-cycle* work for a thermal noisy information engine. That marginal result is not a pair-time covariance, and its bath lacks the exponentially correlated active force that produces positive long-lag correlations here. General Wick and Gaussian-filter formulas are established mathematical tools; the new result is the model-specific exact lag structure and the all-parameter phase boundary, not those tools themselves.

## Limitations

This analysis requires a stationary Gaussian active force and independent Gaussian measurement errors; a non-Gaussian active bath with the same two-time covariance need not have the same work covariance. The protocol fixes gain at one and instantaneous shifts. Thermal-noise intensity does not enter the *cross-cycle* work covariance, although it affects single-cycle work fluctuations and means. The result does not cover optimization over gain, entropy-production bounds, finite-time engine initialization or a finite-sample confidence interval for measuring the covariance. Published-equivalence searches and inspections are not independent audit or a guarantee of publication priority.

## References

1. S. Bahng, J. S. Lee and C.-M. Ghim, *Memory-aware feedback enhances power in active information engines*, arXiv:2508.16866 (first submitted 2025-08-23), https://arxiv.org/abs/2508.16866 .
2. G. Paneru, S. Dutta, T. Sagawa, T. Tlusty and H. K. Pak, *Efficiency fluctuations and noise induced refrigerator-to-heater transition in information engines*, Nature Communications **11**, 1012 (2020), https://doi.org/10.1038/s41467-020-14823-x .
3. G. Paneru, S. Dutta, T. Tlusty and H. K. Pak, *Reaching and violating thermodynamic uncertainty bounds in information engines*, Physical Review E **102**, 032126 (2020), https://arxiv.org/abs/1911.09835 .
