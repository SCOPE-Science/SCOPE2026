# Sharp thermal-noise frontier for lagged active-work correlations in a harmonic active particle

## Finding

In a stationary, one-dimensional, overdamped active Ornstein–Uhlenbeck particle in a harmonic trap, the *regular covariance density of the active-work increments at two distinct times* admits a complete, all-parameter sign classification. Writing \(A>0\) for the stationary variance of the active propulsion, \(D\ge 0\) for translational diffusivity, \(\kappa>0\) for the trap relaxation rate, and \(d=D/A\), put

\[
 d_c(\kappa)=\frac{\kappa+2}{\kappa(\kappa+1)^2}.
\]

For \(0\le d<d_c(\kappa)\), the positive-lag covariance density \(K(t)\) is strictly positive up to exactly one time \(t_*>0\), vanishes there, and is strictly negative afterwards. For \(d\ge d_c(\kappa)\), it is strictly negative at **every** positive lag. The crossing, when it exists, is

\[
 t_* = \begin{cases}
 \displaystyle \frac{1}{\kappa-1}\log\!\left(\frac{\kappa(\kappa+3)}{2(\kappa+1)}-\frac{d\kappa(\kappa-1)(\kappa+1)}{2}\right),&\kappa\ne1,\\
 \displaystyle \frac34-d,&\kappa=1.
 \end{cases}
\]

The logarithm is invoked only inside the stated crossing regime, where its argument is positive. At fixed \(\kappa\), the crossing time strictly decreases with \(d\) until it reaches zero at \(d_c(\kappa)\). For any fixed \(d>0\), \(d_c(\kappa)\) decreases strictly from infinity to zero as \(\kappa\) increases, so there is exactly one trap-relaxation threshold separating the two regimes.

This is a statement about separated work *increments*, not a claim that the full work-current covariance is negative definite. A nonnegative white-noise contact contribution remains at zero lag and is strictly positive when \(D>0\).

## Assumptions and scope

Let \(B,C\) be independent standard Brownian motions. Choose \(\kappa>0\), \(A>0\), and \(D\ge0\); time is nondimensionalized so that propulsion persistence decays at rate one. Let \((X_t,V_t)_{t\in\mathbb R}\) be the unique strictly stationary solution of

\[
 dX_t=(-\kappa X_t+V_t)dt+\sqrt{2D}\,dB_t,\qquad
 dV_t=-V_tdt+\sqrt{2A}\,dC_t.
\]

Define the active work over any finite interval by

\[
 W_b-W_a=\int_a^b V_s\circ dX_s=\int_a^b V_s\,dX_s,
\]

where the two stochastic integrals agree because \([V,X]_t=0\). For each \(t>0\), the *positive-lag, regular covariance density* is the limit

\[
 K(t)=\lim_{\varepsilon,\delta\downarrow0}
 \frac{\operatorname{Cov}(W_\varepsilon-W_0,\,W_{t+\delta}-W_t)}{\varepsilon\delta},
\]

with the increments disjoint (eventually \(\varepsilon<t\)). This limit exists. Neither the density at \(t=0\) nor the covariance of a heuristic product involving the distributional velocity is used to define \(K\).

For \(\kappa\ne1\), its exact expression is

\[
\boxed{K(t)=\frac{A^2}{(\kappa-1)(\kappa+1)^2}
\left[\kappa(\kappa+3)e^{-(\kappa+1)t}-2(\kappa+1)e^{-2t}\right]
-D\kappa A e^{-(\kappa+1)t}.}
\]

At resonance \(\kappa=1\), the continuous limit is

\[
\boxed{K(t)=A^2e^{-2t}\left(\frac34-t-\frac DA\right).}
\]

The stationary mean active-work rate is \(\mathbb E[W_T]/T=A/(\kappa+1)\). The singular, full stationary work-current covariance has the additional nonnegative contact term \(2DA\,\delta_0\), in the sense of test functions. Consequently, for every \(T\ge0\),

\[
 \operatorname{Var}(W_T)=2DA T+2\int_0^T(T-s)K(s)\,ds.
\]

This identity implies the strictly positive long-time variance rate

\[
 \lim_{T\to\infty}\frac{\operatorname{Var}(W_T)}{T}
 =\frac{2DA}{\kappa+1}+\frac{2A^2}{(\kappa+1)^3}.
\]

The latter mean and integrated-variance formulas are consistency checks rather than asserted new results about long-time work fluctuations.

## Proof

**Stationary Gaussian input.** Let \(Z_t=(X_t,V_t)^\top\). Its drift matrix and stationary covariance are

\[
 M=\begin{pmatrix}-\kappa&1\\0&-1\end{pmatrix},\qquad
 \Sigma=\begin{pmatrix}
 D/\kappa+A/[\kappa(\kappa+1)]&A/(\kappa+1)\\
 A/(\kappa+1)&A
 \end{pmatrix}.
\]

The Lyapunov equation \(M\Sigma+\Sigma M^\top+\operatorname{diag}(2D,2A)=0\) follows directly. For every \(t\ge0\), conditional means evolve by \(E_t=e^{Mt}\), where

\[
 E_t=\begin{pmatrix}
 e^{-\kappa t}&\displaystyle\frac{e^{-t}-e^{-\kappa t}}{\kappa-1}\\
 0&e^{-t}
 \end{pmatrix}
\]

when \(\kappa\ne1\), and its upper-right entry is \(te^{-t}\) when \(\kappa=1\).

**Quadratic drift part and Brownian cross term.** By Itô's formula for the work integral,

\[
 dW_t=f(Z_t)dt+\sqrt{2D}\,V_t\,dB_t,\quad
 f(x,v)=v^2-\kappa xv=\begin{pmatrix}x&v\end{pmatrix}Q\begin{pmatrix}x\\v\end{pmatrix},
 \quad Q=\begin{pmatrix}0&-\kappa/2\\-\kappa/2&1\end{pmatrix}.
\]

For \(t>0\), stationarity and Wick's fourth-moment formula give

\[
 \operatorname{Cov}(f(Z_0),f(Z_t))
 =2\operatorname{tr}(Q\Sigma E_t^\top Q E_t\Sigma).
\]

Crucially, this expression **is not yet** \(K(t)\). The noise in the first infinitesimal work increment affects the future position and hence correlates with the future drift. With \(P_t\) the transition semigroup for \(Z\), Gaussian integration by parts/Itô isometry yields

\[
 K(t)=\operatorname{Cov}(f(Z_0),f(Z_t))
 +2D\,\mathbb E\!\left[V_0\partial_x(P_tf)(Z_0)\right].
\]

The derivative is \(\partial_x(P_tf)(x,v)=-\kappa e^{-\kappa t}\mathbb E[V_t\mid Z_0=(x,v)]\), because only the future position has a nonzero derivative in the initial position. Since \(\mathbb E[V_0V_t]=Ae^{-t}\), this cross term equals

\[
 -2D\kappa A e^{-(\kappa+1)t}.
\]

Straight matrix multiplication, or the independent exact-rational implementation in `check.py`, reduces the last two displayed expressions to the boxed formulas. In particular, omitting the cross term would yield a different and incorrect thermal threshold.

**Sharp sign classification.** The short-lag regular limit is

\[
 K(0+)=A^2\frac{\kappa+2}{(\kappa+1)^2}-D\kappa A
 =A^2\kappa\,[d_c(\kappa)-d].
\]

For \(\kappa\ne1\), introduce

\[
 h=\frac{\kappa(\kappa+3)}{2(\kappa+1)}
 -\frac{d\kappa(\kappa-1)(\kappa+1)}2.
\]

Then

\[
 K(t)=\frac{2A^2e^{-2t}}{(\kappa-1)(\kappa+1)}
 \bigl[h e^{-(\kappa-1)t}-1\bigr].
\]

If \(\kappa>1\), the bracket is strictly decreasing whenever it can be positive, and a positive initial regular covariance occurs exactly when \(h>1\); otherwise the bracket is negative for all positive lags. If \(0<\kappa<1\), then \(h>0\), the bracket is strictly increasing, and the external prefactor is negative: thus initial positivity occurs exactly when \(h<1\), with one crossing to negativity, and otherwise the covariance is negative. Direct substitution of \(K(0+)\) shows that both conditions are precisely \(d<d_c(\kappa)\). The unique root is the displayed logarithmic formula. At \(\kappa=1\), the resonant expression has the sign of \(3/4-d-t\), giving the same dichotomy and the root \(3/4-d\). At equality \(d=d_c\) the only zero of the continuous regular extension lies at \(t=0\), excluded from the positive-lag domain.

Differentiation of the root formula within its admissible region gives

\[
 \frac{\partial t_*}{\partial d}
 =-\frac{\kappa(\kappa+1)}{2h}<0\quad(\kappa\ne1),
 \qquad\frac{\partial t_*}{\partial d}=-1\quad(\kappa=1).
\]

Also \(d_c\) is strictly decreasing because the logarithmic derivative of \((\kappa+2)/(\kappa(\kappa+1)^2)\) is
\[
 \frac{1}{\kappa+2}-\frac1\kappa-\frac2{\kappa+1}<0.
\]

Its endpoint limits are \(+\infty\) and zero, proving the claimed unique stiffness threshold at fixed positive \(d\).

**Contact term and consistency.** The quadratic variation of the work martingale is \(2D\int_0^T V_s^2ds\), whose stationary density is \(2DA\). All remaining cross correlations are represented by the continuous even extension of \(K(t)\) away from zero. Integrating the two exponential expressions gives the finite-duration variance identity and the stated positive asymptotic rate. No inference about a signed covariance density is made from a finite-time variance alone.

## Verification

A standalone, standard-library checker `check.py` reconstructs the two-time Gaussian covariance by all fourth-moment pair contractions, **independently of the final two-exponential closed expression**. Its exact-rational tests substitute independent formal rational values for \(e^{-\kappa t}\) and \(e^{-t}\), thereby checking the entire polynomial identity, not merely sample times. At resonance it substitutes the exact Jordan propagator entry \(te^{-t}\). It also checks the limiting variance rate and representative positive-lag sign regimes, including \(\kappa=1\) and \(D=0\). The packaged checker passes 1,039 assertions.

As a concrete example, for \(\kappa=A=1\), \(D=1/4\), one has \(d_c=3/4\) and

\[
 K(t)=e^{-2t}(1/2-t),\qquad t_*=1/2.
\]

For the same trap and propulsion with \(D=1\), \(K(t)=-e^{-2t}(1/4+t)<0\) for all \(t>0\).

The checker is not a substitute for the semigroup, stochastic cross-term, and monotonicity arguments proving the unrestricted theorem.

## Relationship to prior work

Semeraro, Suma, Petrelli, Cagnetta and Gonnella introduced and numerically investigated active-work large deviations in free and confined active Ornstein–Uhlenbeck particles (public preprint 2021). Semeraro, Gonnella, Suma and Zamparo subsequently analyzed the same harmonic active-work observable, with stationary initial data, and obtained large-deviation rate functions and rare-event singularities (public preprint February 2023). Their full 2023 preprint gives the same Langevin equations, work definition, stationary covariance, and Gaussian quadratic-functional method, but its asserted results concern **integrated work large deviations**, not the exact positive-lag incremental covariance sign boundary derived here.

The full 2023 source was inspected through its lawfully accessible preprint text, including the model, work functional, covariance setup, Toeplitz generating-function treatment, and reported conclusions. The 2021 preprint's title, publicly available abstract, and model description were inspected, but its complete text was not accessible in this review; its stated scope concerns full-work rare-event fluctuations. Generic Gaussian Wick/semigroup identities are standard background and are not asserted to be new. A possible prior derivation buried within other work-fluctuation or general quadratic-OU literature is a residual publication-priority risk.

The equality of the total long-time variance rate with that obtainable from existing scaled cumulant-generating-function methods is expressly treated as a consistency check. The new claim is the **sharp finite-lag covariance sign classification, including the thermal-noise and stiffness frontiers and the resonant case**.

## Limitations

The theorem assumes a stationary, single-coordinate, linear Gaussian active particle; it does not cover nonlinear traps, interacting particles, non-Gaussian propulsion, nonstationary starts, or independently time-varying trap parameters. It classifies only the regular work-current covariance for strictly separated times. At zero lag one must include the positive Dirac contact term; a negative regular covariance is compatible with a positive integrated work variance. The source comparison is evidence of non-coverage in material actually inspected, not a mathematical proof of publication priority. Full text of the 2021 precursor was unavailable, and no independent external scientific audit has been carried out.

## References

1. M. Semeraro, A. Suma, I. Petrelli, F. Cagnetta and G. Gonnella, *Work Fluctuations in the Active Ornstein-Uhlenbeck Particle Model*, arXiv:2103.11369 (first submitted 2021-03-21), https://arxiv.org/abs/2103.11369 , DOI:10.1088/1742-5468/ac3d37.
2. M. Semeraro, G. Gonnella, A. Suma and M. Zamparo, *Work Fluctuations for a Harmonically Confined Active Ornstein-Uhlenbeck Particle*, arXiv:2302.12535 (first submitted 2023-02-24), https://arxiv.org/abs/2302.12535 , *Physical Review Letters* **131**, 158302 (2023), DOI:10.1103/PhysRevLett.131.158302.
3. M. L. Rosinberg, G. Tarjus and T. Munakata, *Comment on "Work Fluctuations for a Harmonically Confined Active Ornstein-Uhlenbeck Particle"*, arXiv:2311.14724 (2023), https://arxiv.org/abs/2311.14724 . This concerns generating-function-domain issues, not an asserted two-time covariance classification.
