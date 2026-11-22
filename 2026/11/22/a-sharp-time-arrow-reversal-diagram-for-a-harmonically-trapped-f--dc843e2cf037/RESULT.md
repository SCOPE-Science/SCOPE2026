# A sharp time-arrow reversal diagram for a harmonically trapped finite-tumble particle

## Finding

The position of a stationary one-dimensional run-and-tumble particle in a harmonic trap has an exactly computable **fourth-order temporal arrow** even when the particle spends positive random durations at rest. Unlike its two-time covariance, the position-only statistic
\[
\mathcal A(t)=\mathbb E[X_0^3X_t]-\mathbb E[X_0X_t^3]
\]
can reverse sign **at exactly one positive observation lag**. The complete parameter classification below also allows a strictly positive arrow at every lag or a strictly negative arrow at every lag. Every sign statement is unchanged by independent thermal Brownian diffusion, at any nonnegative strength.

Let \(a>0\) be the rate of ending a run, \(c>0\) the rate of leaving the tumble/rest state, \(b>0\) the harmonic relaxation rate and \(v>0\) the propulsion speed. Define
\[
B_0=a-b-2c,\qquad
B_\infty=B_0+\frac{(a+3b)(a-c)}{\max(a,b)+c}.
\]
Then for every \(t>0\), the **exhaustive phase diagram** is:

1. If \(a\le c\), then \(\mathcal A(t)<0\) at every positive lag.
2. If \(a>c\) and \(B_0\ge0\), then \(\mathcal A(t)>0\) at every positive lag.
3. If \(a>c\) and \(B_\infty\le0\), then \(\mathcal A(t)<0\) at every positive lag.
4. If \(a>c\) and \(B_0<0<B_\infty\), there is **exactly one** \(t_*>0\), with \(\mathcal A(t)<0\) for \(0<t<t_*\), \(\mathcal A(t_*)=0\), and \(\mathcal A(t)>0\) for \(t>t_*\).

The cases are disjoint: when \(a>c\), one always has \(B_\infty>B_0\). Equality at \(B_0=0\) belongs to the strictly positive class, and equality at \(B_\infty=0\) belongs to the strictly negative class. At \((a,b,c,v)=(2,1,1,1)\), the unique crossing is \(t_*\approx1.132906609052\), with arbitrary independent thermal diffusivity \(D\ge0\).

More precisely, put \(e_\lambda(t)=e^{-\lambda t}\mathbf1_{t\ge0}\), with causal convolution \(*\), and define
\[
H=e_a*e_b*e_{3b}*e_{a+2b},\qquad J=H*e_{a+b+c},
\quad K=\frac{6acv^4}{(a+b)(a+3b)(a+c)(a+2b+c)}.
\]
There is an exact, resonance-safe representation
\[
\boxed{\mathcal A(t)=K\big[(a-b-2c)H(t)+(a+3b)(a-c)J(t)\big].}
\]
The ratio \(J(t)/H(t)\) is strictly increasing on \((0,\infty)\), with limits \(0\) and \(1/[\max(a,b)+c]\). The uniqueness assertion is thus analytic, not an inference from a plot or numerical sampling.

## Assumptions and scope

The internal continuous-time Markov velocity \(S_t\in\{-1,0,+1\}\) jumps from each running state \(\pm1\) to rest state \(0\) at rate \(a\), and from rest to each run direction at rate \(c/2\). The choice of direction after each rest is independent and symmetric. Let \(B_t\) be independent standard Brownian motion and let the position satisfy
\[
dX_t=(-bX_t+vS_t)\,dt+\sqrt{2D}\,dB_t,\quad a,b,c,v>0,\quad D\ge0.
\]
The stationary solution is defined by its causal convolution with the two-sided stationary \(S\) and \(B\); it has all finite polynomial moments. The sign convention in this manuscript is **earlier cubed, later linear, minus earlier linear, later cubed**. All conclusions are for stationary processes and positive forward time lags. The Gaussian thermal forcing may be arbitrarily strong, but it must be independent of the motor process.

The hidden motor has invariant probabilities \(\pi(0)=a/(a+c)\), \(\pi(+)=\pi(-)=c/[2(a+c)]\), so \(\mathbb E[S]=0\) and \(\mathbb E[S^2]=c/(a+c)\). The two-time covariance of any real stationary process obeys \(\mathbb E[X_0X_t]=\mathbb E[X_0X_{-t}]\) and cannot by itself distinguish the temporal order; this is why the fourth-order asymmetry is of interest.

## Proof

**1. Stationary polynomial balances.** Let \(m_{ij}=\mathbb E[X^iS^j]\) in the stationary law and \(p=c/(a+c)\). The motor generator satisfies \(QS=-aS\), \(QS^2=c-(a+c)S^2\), and \(S^3=S\). The joint generator is
\[
Lf=(-bx+vs)\partial_x f+D\partial_x^2 f+Qf.
\]
Applying \(\mathbb E[Lf]=0\) successively to \(XS,X^2,X^2S^2,X^3S,X^4\) gives the exact triangular identities
\[
\begin{aligned}
m_{11}&=\frac{vp}{a+b},&m_{20}&=\frac{vm_{11}+D}{b},\\
m_{22}&=\frac{cm_{20}+2vm_{11}+2Dp}{a+c+2b},&
m_{31}&=\frac{3vm_{22}+6Dm_{11}}{a+3b},\\
m_{40}&=\frac{vm_{31}+3Dm_{20}}{b}.
\end{aligned}
\]
They determine every initial fourth-order mixed moment needed below with no moment-closure approximation.

**2. Exact two-time Laplace transform.** The generator preserves the five-dimensional polynomial span \((x^3,x^2s,xs^2,x,s)\). Its column action, listed in that order, is
\[
\begin{aligned}
L(x^3)&=-3bx^3+3vx^2s+6Dx,\\
L(x^2s)&=-(2b+a)x^2s+2vxs^2+2Ds,\\
L(xs^2)&=-(b+a+c)xs^2+cx+vs,\\
Lx&=-bx+vs,\qquad Ls=-as.
\end{aligned}
\]
For \(\operatorname{Re}z>0\), the resolvent \((zI-L)^{-1}\) of this explicitly displayed finite matrix gives both \(\mathcal L\{\mathbb E[X_0^3X_t]\}\) and \(\mathcal L\{\mathbb E[X_0X_t^3]\}\) by contracting coefficients with the preceding stationary moments. Straight rational cancellation yields
\[
\widehat{\mathcal A}(z)=
K\frac{(a-b-2c)z+2a^2+3ab-2ac-b^2-6bc-2c^2}
{(z+a)(z+b)(z+3b)(z+a+2b)(z+a+b+c)}.
\]
This exact formula has no \(D\) dependence; all thermal terms cancel algebraically. More conceptually, \(X=Y+Z\), where \(Y\) is the non-Gaussian active component and \(Z\) an independent centered stationary Gaussian Ornstein–Uhlenbeck process. Wick expansion and symmetry of both two-time covariances cancel all cross terms in \(\mathcal A\), so \(\mathcal A_X=\mathcal A_Y\).

The numerator decomposes identically as
\[
(a-b-2c)(z+a+b+c)+(a+3b)(a-c).
\]
Taking inverse Laplace transforms of the five strictly positive resolvent factors proves the stated \(H,J\) representation at **all** positive rates, including coincident poles. A matrix-resolvent derivation, the exact symbolic cancellation, and independent numerical semigroups are reproduced by the accompanying `verify.py`.

**3. Strictly increasing positive-kernel ratio.** The function \(H(t)\) is the convolution of four exponentials supported on the nonnegative half-line. Each such function is log-concave on its convex support, and convolution preserves log-concavity. Moreover \(H(t)>0\) for every \(t>0\). For fixed \(u>0\), and \(t>u\), log-concavity implies
\[
\frac{d}{dt}\log\frac{H(t-u)}{H(t)}
=(\log H)'(t-u)-(\log H)'(t)\ge0.
\]
Since
\[
\frac{J(t)}{H(t)}=\int_0^t e^{-(a+b+c)u}\frac{H(t-u)}{H(t)}\,du,
\]
its integrand is nondecreasing wherever it is defined, and as the upper limit increases an additional interval of strictly positive integrand is included. Consequently \(R(t):=J(t)/H(t)\) increases **strictly** for all \(t>0\). At the origin, \(H(t)\sim t^3/3!\) and \(J(t)\sim t^4/4!\), so \(R(t)\to0\).

The four decay rates in \(H\) are \(a,b,3b,a+2b\), and their minimum is \(m=\min(a,b)\). Elementary pole analysis of the product of their Laplace transforms shows \(H(t)\sim Ct^{k-1}e^{-mt}\), where \(k=2\) if \(a=b\) and \(k=1\) otherwise, with \(C>0\). Convolution with the additional faster exponential \(e_{a+b+c}\) then yields
\[
\lim_{t\to\infty}R(t)=\frac{1}{a+b+c-m}=\frac{1}{\max(a,b)+c}.
\]
This also follows by partial fractions in the nonresonant case and continuous limits in the resonant case. The multiplicity \(k\) does not change the ratio limit.

**4. Complete sign classification.** Both \(K\) and \(H(t)\) are strictly positive, so the sign of \(\mathcal A(t)\) is exactly that of
\[
B(t)=B_0+(a+3b)(a-c)R(t).
\]
For \(a\le c\), both \(B_0=a-b-2c\) and the second term are negative or nonpositive, so the sign is negative. For \(a>c\), the coefficient of \(R\) is positive and Step 3 makes \(B(t)\) strictly increasing from \(B_0\) to \(B_\infty\). The endpoint limits are **not attained** at finite positive lags. Thus \(B_0\ge0\) implies strictly positive sign, \(B_\infty\le0\) implies strictly negative sign, and \(B_0<0<B_\infty\) implies one and only one positive zero, by continuity and strict monotonicity. This proves every case and boundary, including coincident rates, without a numerical root-count assumption.

## Verification

Run `python3 verify.py` with SymPy, NumPy and SciPy installed. The checker derives the stationary moments from the stated generator, performs an exact symbolic resolvent factorization, verifies independence from thermal diffusivity, and compares the two-time polynomial-generator semigroup with an **independently built five-stage positive convolution semigroup** at multiple positive lags and both resonant/nonresonant rates. It passes **123 assertions** (as run for this package), and independently brackets the crossing at \(1.132906609052\) for \((a,b,c,v)=(2,1,1,1)\), including positive thermal noise. The finite numerical experiments support, but do not replace, the all-rate mathematical proof in Steps 3–4.

## Relationship to prior work

Sun, Ye and Chen (arXiv:2610.24961v1, first public 2026-10-18) develop exactly the three-state finite-tumble harmonic model and calculate conditional single-time position distributions and moments. Their conditional motor-state correlators are important input; the present **two-observation-time, position-only asymmetry and exact sign diagram** are not identified among their results. Sun, Ye and Podgornik (arXiv:2409.00578) previously obtained the same model's stationary moment machinery and distribution. Basu et al. (arXiv:1910.10083) give stationary one-time distributions in a three-state harmonic trap.

The published *A sharp dimension-seven threshold for the quartic time arrow of trapped run-and-tumble motion* concerns **instantaneous complete orientation redraw without a finite tumble state** and establishes a different high-dimensional temporal sign boundary. Its explicitly stated scope excludes finite-duration tumbles. A previously established **mixed motor-state/position** time arrow for the same finite-tumble dynamics is strictly positive at every lag, but it measures motor activity alongside position rather than the position-only quartic observable, and does not imply the present sign reversal. The published *An exact two-moment inverse fold in a trapped run-and-tumble particle* concerns this motor's stationary, **one-time** moment identifiability. The published *A golden-ratio kurtosis boundary for intermittent run-and-rest motion* concerns **unconfined displacement fourth cumulants**, not the stationary harmonically filtered two-time temporal arrow. Their semigroup and moment methods are acknowledged; none directly implies the current positivity-ratio theorem or sharp parameter classification without the new filtering calculation.

The claim is limited to this specific fully derived result, not the novelty of stochastic-process methods, Markov resolvents, thermal Gaussian cancellation in general, or quartic irreversibility as a diagnostic. Literature and accessible research records have been compared by objects, parameter domains, and logical implication. Undiscovered equivalent formulations or unpublished analyses remain a priority risk; independent audit has not been performed.

## Limitations

The model assumes independent exponentially distributed run and rest times, symmetric run-direction relaunch, linear harmonic confinement, stationarity, and optional **independent** Gaussian thermal noise. It does not cover directionally biased rest exits, nonexponential waits, nonlinear traps, underdamped motion, spatially coupled particles, or motor–bath feedback. A vanishing fourth-order statistic does not establish microscopic reversibility, and its sign is not an entropy-production rate. The theorem is exact for the mathematical model, not a claim of experimental identifiability under finite samples. Its historical priority requires wider independent literature verification.

## References

1. A. Sun, F. Ye and J. Z. Y. Chen, *Run-and-tumble particles in a harmonic external field: constructing the solution of the Fokker-Planck equation from the equations of motion*, arXiv:2610.24961v1 (first public 2026-10-18). https://arxiv.org/abs/2610.24961
2. A. Sun, F. Ye and R. Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578v1 (2024-09-01). https://arxiv.org/abs/2409.00578
3. U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit and G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083 (2019). https://arxiv.org/abs/1910.10083
4. *A sharp dimension-seven threshold for the quartic time arrow of trapped run-and-tumble motion*, available public mathematical finding, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-sharp-dimension-seven-threshold-for-the-quartic-time-arrow-of--0d6063747558
5. *An exact two-moment inverse fold in a trapped run-and-tumble particle*, available public mathematical finding, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-an-exact-two-moment-inverse-fold-in-a-trapped-run-and-tumble-par--432388eb4847
6. *A golden-ratio kurtosis boundary for intermittent run-and-rest motion*, available public mathematical finding, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-golden-ratio-kurtosis-boundary-for-intermittent-run-and-rest-m--1c58232cf9d7
7. A. Prékopa (1973), *On logarithmic concave measures and functions*, Acta Sci. Math. **34**, 335–343 (convolution closure of log-concavity).
