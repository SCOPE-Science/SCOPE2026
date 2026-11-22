# Reentrant cross-coordinate energy correlations under periodic orientation renewal

## Finding

Consider a harmonically confined active particle in dimension \(d\ge 2\) whose heading is redrawn **independently and uniformly on the unit sphere at exactly periodic times** rather than at Poisson times. At stationarity the observation phase is uniform over a renewal period. Although its Cartesian positions have zero cross-covariance, their squared positions can have either sign of cross-covariance.

Write \(a>0\) for the common harmonic relaxation rate, \(v>0\) for propulsion speed, \(T>0\) for the deterministic orientation-renewal period, and \(\theta=aT\). For every distinct pair \(i\ne j\), define \(z=e^{-\theta}\),
\[
M_k=\frac{1-z^k}{k\theta},\qquad A=\frac{2}{1+z},\qquad B=\frac{(1-z)^4}{1-z^4},
\]
\[
\begin{aligned}
E_S&=1-2M_1+AM_2=1-\frac{1-z}{\theta},\\
E_{S^2}&=1-4M_1+(4+2A)M_2-4AM_3+A^2M_4,\\
E_P&=1-4M_1+6M_2-4M_3+(1+B)M_4,\\
V_S&=E_{S^2}-E_S^2.
\end{aligned}
\]

**Theorem (exact covariance and reentrant sign).** For every integer \(d\ge2\) and every \(\theta>0\),
\[
\boxed{\operatorname{Cov}(X_i^2,X_j^2)
=\frac{v^4}{a^4d^2}\left(V_S-\frac{2E_P}{d+2}\right).}\tag{1}
\]
For every fixed finite dimension, this covariance is strictly negative for all sufficiently short renewal periods and all sufficiently long renewal periods. At \(\theta=3\), it is strictly positive in **every integer dimension \(d\ge41\)**. Consequently, for each such dimension, as the deterministic renewal period increases from zero to infinity, the covariance changes sign at least twice: negative, then positive, then negative. By continuity there are at least two distinct finite positive zero-crossing periods.

The threshold \(41\) is a *rigorously certified sufficient dimension*, not a claim that the smallest possible dimension has been determined. At \(d=41\) the normalized bracket in (1) has exact-rational certified signs at \(\theta=1,3,10\):
\[
\begin{array}{c|ccc}
\theta&1&3&10\\\hline
V_S-2E_P/43&-0.001921448746\ldots&+0.000180806766\ldots&-0.014647861967\ldots
\end{array}
\]
The signs, rather than the decimal truncations, are established by an exact-rational certificate included with this finding.

## Assumptions and scope

The process is the unique stationary solution of
\[
\dot{\boldsymbol X}(t)=-a\boldsymbol X(t)+v\boldsymbol U(t),
\]
where, at all times belonging to one interval of length \(T\), \(\boldsymbol U(t)\) is constant; at every successive interval it is an independent uniform vector on \(S^{d-1}\). At stationarity the origin of the periodic clock has an independent uniform phase on \([0,T)\). This randomized phase is essential: observing only at prescribed phases defines a different statistic. The heading sequence is independent of that phase. There is no additional thermal noise, no directional persistence across renewals, no spatial interaction, and no anisotropic trap.

The deterministic schedule is a stationary renewal process after randomizing the phase. The stable linear drift and bounded heading produce the unique stationary causal solution
\[
\boldsymbol X(t)=v\int_{-\infty}^{t}e^{-a(t-s)}\boldsymbol U(s)\,ds.
\]
The covariance in (1) is an equal-time stationary covariance of **two distinct squared Cartesian positions**, not the covariance of positions and not a temporal autocorrelation. All dimensions are integers and all model parameters are strictly positive.

## Proof

**1. Exact stationary renewal weights.** Set \(u\) to be the elapsed phase in units of the harmonic relaxation time, so \(u\) is uniform on \([0,\theta)\). Put \(y=e^{-u}\) and \(z=e^{-\theta}\). Integration of the stationary causal solution over the current and previous renewal intervals gives, in distribution,
\[
\frac{a}{v}\boldsymbol X=\sum_{n\ge0}w_n(u)\boldsymbol U_n,
\qquad
w_0=1-y,\quad w_n=y(1-z)z^{n-1}\ \ (n\ge1),
\]
where the \(\boldsymbol U_n\) are independent uniform sphere vectors, independent of \(u\). The nonnegative weights sum to \(1\), and the series converges absolutely. Their square and fourth-power sums are
\[
S(u)=\sum_{n\ge0}w_n(u)^2=1-2y+\frac{2y^2}{1+z},
\]
\[
P(u)=\sum_{n\ge0}w_n(u)^4=(1-y)^4+y^4\frac{(1-z)^4}{1-z^4}.
\tag{2}
\]

**2. Angular contractions and total covariance.** For distinct axes \(i\ne j\), independent uniform vectors on \(S^{d-1}\) satisfy
\[
\mathbb EU_{n,i}=0,\qquad\mathbb EU_{n,i}^2=\frac1d,
\qquad \mathbb E(U_{n,i}^2U_{n,j}^2)=\frac1{d(d+2)},
\qquad\mathbb E(U_{n,i}U_{n,j})=0.
\]
Expanding the fourth moment and grouping equal and unequal renewal-interval indices gives, conditional on \(u\),
\[
\begin{aligned}
\mathbb E[X_i^2\mid u]&=\frac{v^2}{a^2d}S(u),\\
\mathbb E[X_i^2X_j^2\mid u]&=\frac{v^4}{a^4d^2}\left[S(u)^2-\frac{2P(u)}{d+2}\right].
\end{aligned}
\]
The cross terms involving distinct intervals vanish by angular symmetry. Averaging over the stationary phase and subtracting the product of means yields (1). The positive term \(\operatorname{Var}_u S\) describes shared renewal-phase disorder; the negative term \(-2\mathbb E_uP/(d+2)\) records the unit-sphere constraint on orthogonal headings.

**3. Closed phase integration.** Since the phase is uniform and \(y=e^{-u}\),
\[
\mathbb E_u[y^k]=\frac1\theta\int_0^\theta e^{-ku}\,du=M_k.
\]
Expanding (2) and their squares produces exactly the displayed formulas for \(E_S,E_{S^2},E_P\). All denominators are positive for \(\theta>0\). In particular, \(E_P>0\) because the fourth-power sum of the nonnegative weights is positive at every phase. Therefore the covariance bracket is strictly increasing in dimension \(d\) for every fixed \(\theta>0\).

**4. Negative fast-renewal regime.** Put \(u=\theta q\) with \(q\) uniform on \([0,1]\). Taylor expansion of (2), uniformly in \(q\), yields
\[
S(\theta q)=\frac\theta2+\theta^2(q^2-q)+O(\theta^3).
\]
Since \(\operatorname{Var}(q^2-q)=1/180\),
\[
\operatorname{Var}_uS=\frac{\theta^4}{180}+O(\theta^5).
\]
The completed prior intervals contribute a geometric fourth-power sum with leading behavior \(\theta^4/(1-e^{-4\theta})=\theta^3/4+O(\theta^4)\), while the current interval contributes only \(O(\theta^4)\). Thus
\[
E_P=\frac{\theta^3}{4}+O(\theta^4),\qquad
V_S-\frac{2E_P}{d+2}=-\frac{\theta^3}{2(d+2)}+O_d(\theta^4)<0
\]
for all sufficiently small positive \(\theta\), at each fixed finite \(d\).

**5. Negative slow-renewal regime.** In the limit \(\theta\to\infty\), \(z=e^{-\theta}\to0\), and the finite expressions in (1) give
\[
V_S=\frac{1}{3\theta}-\frac1{\theta^2}+O(e^{-\theta}/\theta),
\quad
E_P=1-\frac{11}{6\theta}+O(e^{-\theta}/\theta).
\]
Hence \(V_S-2E_P/(d+2)\to-2/(d+2)<0\). In particular, the covariance is strictly negative at sufficiently long periods for every fixed finite \(d\).

**6. Rigorous positive witness and two crossings.** At \(\theta=3\), let \(z=e^{-3}\). The included standalone exact-rational checker bounds \(z\) by reciprocal Taylor partial sums with rigorous geometric remainders. It establishes
\[
\frac{49787068367}{10^{12}}<z<\frac{49787068369}{10^{12}}
\]
and, by interval evaluation of the closed formulas,
\[
\frac{18080676}{10^{11}}<V_S-\frac{2E_P}{43}<\frac{18080678}{10^{11}}.
\]
Every inequality is strict and rationally certified; there are no floating-point sign assumptions. Because \(E_P>0\), the bracket is strictly larger at each integer \(d>41\). The small- and large-period negative limits already proved and continuity of the exact formulas then imply two distinct finite sign crossings for every \(d\ge41\). This completes the theorem.

## Verification

Run `python check.py` with Python 3; it requires only the standard library. The checker uses rational interval arithmetic, an explicit Taylor-tail bound for \(e^\theta\), exact enclosing evaluation of \(V_S\) and \(E_P\), and strict sign checks at \(\theta=1,3,10\) for \(d=41\). It checks the stated rational enclosure at \(\theta=3\), positive \(E_P\), and dimension monotonicity for several additional dimensions. A separate floating-point midpoint integration directly evaluates the original weight sums \(S(u),P(u)\) to check the algebra independently. The latter is supplementary: the infinite-dimensional and all-period conclusions follow analytically from the proof, not from finite numerical grids.

## Relationship to prior work

Guéneau, Majumdar and Schehr (first publicly posted 9 February 2026) establish the stationary distribution and moments for a harmonically confined \(d\)-dimensional run-and-tumble particle with **exponentially distributed** reorientation waiting times. Their exact stick-breaking weights depend on independent exponential waiting intervals; the deterministic-renewal weight sequence and phase mixture used here are different. Two related published mathematical analyses of anisotropic harmonic run-and-tumble energy covariance prove a single sign transition under a **Poisson** orientation clock. Neither statement implies the present twice-reversing deterministic-clock result, and its fast-renewal negative sign explicitly contrasts with the positive high-rate Poisson sign in dimensions at least five.

Farago and Smith (2024) study arbitrary run-time distributions in a confined **one-dimensional** run-and-tumble system. That work motivates non-Poisson tumbling but does not determine the high-dimensional two-axis squared-coordinate covariance or establish this reentrance. Sun, Ye and Podgornik (2024/2025) derive moments for a harmonic particle with finite **tumbling durations**, a distinct duration mechanism; their paper is a residual related-theory comparison risk.

## Limitations

The result proves **at least two** sign crossings for each integer \(d\ge41\), not exactly two, and does not establish that \(41\) is the smallest dimension with this behavior. It does not classify the entire parameter range below that sufficient dimension. The model assumes perfectly periodic heading renewal with stationary uniform phase, isotropic trap and independent uniform full redraws. Nonuniform clock renewal distributions, correlated headings, rotational diffusion, thermal noise, trap anisotropy and interacting particles are not covered. General higher-dimensional renewal-orientation moment results not found in the examined literature might imply this specialization; publication priority remains subject to independent scrutiny.

## References

1. M. Guéneau, S. N. Majumdar and G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436 (first public 2026-02-09), https://arxiv.org/abs/2602.08436.
2. O. Farago and N. R. Smith, *Confined run-and-tumble particles with non-Markovian tumbling statistics*, *Physical Review E* 109, 044121 (2024), arXiv:2401.01576, https://arxiv.org/abs/2401.01576.
3. A. Sun, F. Ye and R. Podgornik, *Exact moments for a run-and-tumble particle with a finite tumble time in a harmonic trap*, arXiv:2409.00578, https://arxiv.org/abs/2409.00578.
4. *A dimension-five sign transition for anisotropic harmonic run-and-tumble energies*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-dimension-five-sign-transition-for-anisotropic-harmonic-run-an--aa1b705578c0.
5. *Anisotropy raises the unique cross-energy correlation threshold for a trapped run-and-tumble particle*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-anisotropy-raises-the-unique-cross-energy-correlation-threshold--c7257b4e8112.
