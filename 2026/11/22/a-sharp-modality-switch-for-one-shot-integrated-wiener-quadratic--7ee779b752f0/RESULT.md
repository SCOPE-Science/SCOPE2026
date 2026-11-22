# A sharp modality switch for one-shot integrated-Wiener quadratic-energy sensing

## Finding

Let \(B\) be standard Brownian motion on \([0,1]\), and let \(X(t)=\int_0^t B(u)\,du\). We seek the random path energy

\[
Q=\int_0^1X(t)^2\,dt
\]

from **exactly one** scalar reading, either \(Y_X(x)=X(x)+\varepsilon\) or \(Y_B(x)=B(x)+\varepsilon\), with a freely selected \(x\in[0,1]\). The independent Gaussian instrument error has the same calibrated variance \(\eta\ge0\) for the two modalities. The estimator is always the exact conditional mean \(\mathbb E[Q\mid Y]\); the design criterion is its unconditional mean-square error.

There is exactly one positive noise level

\[
\eta_*=0.112491318055058160574\ldots
\]

where the two modalities tie. Below \(\eta_*\), value sensing is strictly better and has exactly one globally optimal site. Above \(\eta_*\), derivative sensing is strictly better and has exactly one globally optimal site. At equality, the optimal designs are exactly value sensing at \(x=1\) and derivative sensing at \(x=z_*\), where

\[
z_*=0.57779219282177255636\ldots,
\quad 168z_*^5-1015z_*^4+1680z_*^3-1050z_*^2+280z_*-33=0,
\]

\[
\eta_*={z_*(8z_*^3-45z_*^2+60z_*-20)\over 10(1-z_*)^2(4-z_*)}.
\]

The root condition is meant on the interval \((z_0,1)\), where \(z_0\) is the unique root of \(8z^3-45z^2+60z-20=0\) on \([0,1]\). In particular \(z_0=0.5121355061523095\ldots\).

More precisely, define

\[
\begin{aligned}
 A_B(z)&={z^2(20-30z+15z^2-2z^3)\over60},\\
 A_X(z)&={z^4(105-105z+35z^2-2z^3)\over1260},\\
 R_B(z,\eta)&={A_B(z)\over z+\eta},\\
 R_X(z,\eta)&={A_X(z)\over z^3/3+\eta}.
\end{aligned}
\]

At the degenerate zero-noise site \(z=0\) the information score is defined as zero. All other denominators above are positive. Define

\[
\begin{aligned}
 M_B(z)&=10(1-z)^2(4-z),\\
 N_B(z)&=z(8z^3-45z^2+60z-20),\\
 M_X(z)&=1260-1575z+630z^2-42z^3,\\
 N_X(z)&=z^3\big(8z^3-105(1-z)^2\big).
\end{aligned}
\]

For each \(\eta\ge0\), the unique derivative-observation optimizer is \(z_B(\eta)\in[z_0,1)\), characterized by \(N_B(z_B)=\eta M_B(z_B)\). The unique value-observation optimizer is the solution \(z_X(\eta)\in[r,1)\) of \(N_X(z_X)=\eta M_X(z_X)\) if \(0\le\eta<8/273\), and is \(z_X(\eta)=1\) if \(\eta\ge8/273\). Here \(r=0.8018180534911620\ldots\) is the unique root of \(8r^3=105(1-r)^2\) in \((0,1)\).

## Assumptions and scope

The process starts at \(B(0)=X(0)=0\). The covariance normalization is \(\mathbb E B(s)B(t)=\min(s,t)\), and physical time is the unit interval. Measurement noise is independent of the path and Gaussian with **identically calibrated numerical variance** for measuring a value or a derivative. Changing the relative calibration changes the threshold. Only one nonadaptive scalar measurement is permitted. Bayes error refers to the unconditional risk \(\mathbb E[(Q-\mathbb E[Q\mid Y])^2]\), not the variance conditional on a particular observed value.

## Proof

**1. The nonlinear information criterion.** For a centered jointly Gaussian pair \((X(t),Y)\), where \(v=\operatorname{Var}Y>0\) and \(c(t)=\operatorname{Cov}(X(t),Y)\), Gaussian conditioning and Isserlis' identity give

\[
\mathbb E[Q\mid Y]={1\over12}+{K\over v^2}(Y^2-v),
\quad K=\int_0^1c(t)^2\,dt.
\]

Consequently, \(\operatorname{Var}(\mathbb E[Q\mid Y])=2K^2/v^2\). A direct covariance integral gives \(\operatorname{Var}(Q)=11/840\). The exact Bayes risk is therefore

\[
\mathcal E(Y)={11\over840}-2(K/v)^2.
\]

It is sufficient, and strictly equivalent, to maximize the nonnegative score \(K/v\). This uses a genuinely quadratic, second-Gaussian-chaos target: linear posterior integration variance is not the present criterion.

**2. Exact scalar scores.** For \(0\le t\le z\),

\[
\operatorname{Cov}(X(t),B(z))={t^2\over2},\qquad
\operatorname{Cov}(X(t),X(z))={zt^2\over2}-{t^3\over6}.
\]

For \(z\le t\le1\), these are \(tz-z^2/2\) and \(tz^2/2-z^3/6\), respectively. Squaring and integrating both pieces gives \(A_B,A_X\) as displayed above; the measurement variances are \(v_B=z+\eta\) and \(v_X=z^3/3+\eta\). The derivatives factor exactly as

\[
\partial_zR_B={z(\eta M_B-N_B)\over60(z+\eta)^2},\quad
\partial_zR_X={z^3(\eta M_X-N_X)\over420(3\eta+z^3)^2}.
\]

**3. Derivative-sensor uniqueness.** The cubic \(8z^3-45z^2+60z-20\) is strictly concave on \([0,1]\), negative at zero, positive at one, and has precisely one zero \(z_0\in(1/2,3/5)\). For \(z\ge z_0\), differentiation yields

\[
(N_B'M_B-N_BM_B')=-20(z-1)(2z^2-7z+2)(2z^3-15z^2+30z-20)>0.
\]

Indeed each of the three nonconstant factors has negative sign on \((z_0,1)\). Hence \(N_B/M_B\) grows strictly from zero to infinity on \([z_0,1)\). The derivative sign from Step 2 implies the stated unique global optimizer \(z_B(\eta)\) for every finite \(\eta\ge0\).

**4. Value-sensor uniqueness.** Put \(r\) for the root of \(8r^3=105(1-r)^2\); uniqueness follows because \(8z^3/[105(1-z)^2]\) strictly increases on \((0,1)\). On \([0,1]\), \(M_X\) decreases but is always at least \(273>0\). On \([r,1]\),

\[
N_X'M_X-N_XM_X'=-126z^2(2z^3-35z^2+105z-105)(4z^3-45z^2+75z-30)>0.
\]

The first parenthesis is negative throughout \([0,1]\); the second is positive on \([r,1]\), since \(r>4/5\), the second polynomial is concave, and its values at \(4/5\) and \(1\) are respectively \(406/125\) and \(4\). Thus \(N_X/M_X\) rises strictly from zero to \(8/273\), proving the interior-to-endpoint classification from Step 2.

**5. No derivative optimum at small noise.** For \(z\in[0,1]\), let \(q(z)=6z^4-45z^3+90z^2-60z+13\). With \(y=z-1/2\), \(|y|\le1/2\),

\[
q(z)=6y^4+15y^2-{3y\over4}+{1\over4}
          +{33\over2}y^2(1-2y)>0.
\]

The displayed sum is strictly positive because its first four terms equal \(6y^4+15(y-1/40)^2+77/320\). Therefore

\[
 {A_B(z)\over z}={13\over180}-{q(z)\over180}<{13\over180}
\]

for every \(z>0\). Hence the best derivative score for any nonnegative noise is strictly below \(13/180\). But \(R_X(1,8/273)=13/180\) and \(R_X(1,\eta)\) decreases in noise. Value sensing dominates for all \(0\le\eta\le8/273\).

**6. A unique modality switch beyond the value-site boundary.** For \(\eta\ge8/273\), the best value score is \(R_X(1,\eta)=(11/420)/(\eta+1/3)\). Define

\[
T(\eta)={\eta+1/3\over11/420}
\max_{z\in[0,1]}{A_B(z)\over z+\eta}.
\]

Every derivative optimizer satisfies \(z\ge z_0>1/3\), so the factor \((\eta+1/3)/(\eta+z)\) strictly increases in \(\eta\) at any potentially maximizing \(z\). Taking the optimizer at a smaller noise level proves that \(T\) itself is strictly increasing. Step 5 gives \(T(8/273)<1\). Also \(\lim_{\eta\to\infty}T(\eta)=(1/20)/(11/420)=21/11>1\), because \(A_B(z)\) is increasing and reaches \(1/20\) at \(z=1\). Continuity and strict monotonicity prove exactly one transition. Substituting the stationary identity \(\eta=N_B/M_B\) into \(T=1\) and canceling factors nonzero on \((z_0,1)\) yields the stated quintic. Its root in that interval is unique by the already-proved crossing, and exact rational endpoint substitutions isolate it in \((57779/100000,57780/100000)\).

## Verification

Run \(\texttt{python verify_energy_sensor.py}\) with Python 3, SymPy and mpmath. The script independently rebuilds both squared-covariance integrals and their derivatives, checks rational identities including the bounding polynomial, integrates the prior quadratic-energy covariance, verifies the defining quintic's sign bracket, and compares fixed-site formulas against independent numerical quadrature. Its supplementary finite-grid checks are **not** used as proofs of any global statement.

## Relationship to prior work

Xi–Briol–Girolami (2018) formulate Gaussian-process multi-output integration, posterior variance formulas for *linear* integrals and convergence results. Their Proposition 1 and theoretical-results section do not assert an optimal single-instrument design for the second-chaos energy functional here. Chai–Garnett (2018) analyze constrained nonnegative integrands and polynomial Gaussian-process transformations; their square-transform moment table is compatible with the Gaussian conditioning used above but does not optimize a choice between value and derivative sensors for integrated Brownian energy.

Separate results on linear integrated-Wiener functionals with competing value/derivative observations do not imply the present second-chaos risk formula or the threshold \(0.112491\ldots\). The related two-point Brownian quadratic-energy observation problem uses a different process and a fixed measurement modality. The broad mathematical possibility of an earlier equivalent result is not ruled out by the limited literature comparison.

## Limitations

The model assumes a known unit-time once-integrated Wiener prior, an exact conditional-mean estimator, a single observation, independent Gaussian measurement noise, and comparable numerical noise variances for a value and its derivative. The result does not establish worst-case deterministic quadrature accuracy, multiple-observation optimality, robustness to prior misspecification, equal physical instrument cost, or improved trajectory integration. The polynomial root is specified exactly but not by radicals. No independent mathematical or publication-priority audit has been performed.

## References

1. Xi, X., Briol, F.-X., and Girolami, M. (2018). *Bayesian Quadrature for Multiple Related Integrals*. First publicly posted 12 January 2018. https://arxiv.org/abs/1801.04153
2. Chai, H., and Garnett, R. (2018). *Improving Quadrature for Constrained Integrands*. First publicly posted 13 February 2018. https://arxiv.org/abs/1802.04782
