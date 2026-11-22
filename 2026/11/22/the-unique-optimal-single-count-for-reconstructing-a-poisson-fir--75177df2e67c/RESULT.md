# The unique optimal single count for reconstructing a Poisson first arrival

## Finding

Let \(N\) be a homogeneous Poisson process of **known** rate \(\lambda>0\) on the unbounded time axis, and let \(T=\inf\{t>0:N_t>0\}\) be its first-arrival time. A numerical observer may obtain **one exact count** \(K=N_x\) at any prespecified deterministic time \(x\ge0\), then estimate \(T\) by any measurable function of \(K\). Under squared loss, the optimal time is uniquely

\[
x_*=\frac{z_*}{\lambda},\qquad z_*=1.7856603836284727622095705222\ldots,
\]

where \(z_*\) is the unique positive zero of

\[
g(z)=e^z-2z+(1-z)\bigl(\operatorname{Ei}(z)-\gamma-\log z\bigr).
\]

Here \(\operatorname{Ei}\) is the real exponential integral and \(\gamma\) is Euler's constant. The exactly optimal mean-square error is

\[
\inf_{x\ge0}\inf_{\widehat T:\mathbb Z_{\ge0}\to\mathbb R}
\mathbb E\bigl[(T-\widehat T(N_x))^2\bigr]
=\frac{0.3217388020117863096997463758\ldots}{\lambda^2}.
\]

The optimal estimator itself is \(\widehat T(0)=x+\lambda^{-1}\) and \(\widehat T(k)=x/(k+1)\) for each integer \(k\ge1\). For comparison, if the observer retains only the binary indicator \(\mathbf 1_{\{N_x>0\}}\), its optimal design has \(\lambda x=1.5936242600400400923\ldots\) and risk \(0.35238976210808514035\ldots/\lambda^2\). Thus retaining the full count reduces even the separately optimized binary risk by approximately \(8.698\%\), and reduces the no-observation risk by about \(67.826\%\).

## Assumptions and scope

The event process is homogeneous Poisson with known strictly positive rate. The single query is a *cumulative exact count* at a deterministic prespecified time on \([0,\infty)\); it does not reveal individual event times. No cutoff horizon or observation-time cost is imposed. The loss is unconditional expected squared error for the **untruncated** first arrival. All statements hold for every \(\lambda>0\). The estimator may be arbitrary measurable, with infinite-risk estimators never improving the infimum.

## Proof

**1. Conditional reconstruction.** Poisson independent increments give \(T\mid\{N_x=0\}\overset d=x+E\), where \(E\sim\mathrm{Exp}(\lambda)\). Given \(N_x=k\ge1\), the \(k\) unordered jump times in \([0,x]\) are independent uniform points; their minimum has mean \(x/(k+1)\) and second moment \(2x^2/[(k+1)(k+2)]\). In particular,

\[
\mathbb E[T\mid N_x=k]=
\begin{cases}x+\lambda^{-1},&k=0,\\x/(k+1),&k\ge1.\end{cases}
\]

Orthogonal projection in \(L^2\) shows this conditional mean minimizes risk among *all* measurable functions of \(N_x\), uniquely up to count-probability-zero sets.

**2. Exact risk.** Put \(z=\lambda x\), and define the entire positive series

\[
F(z)=\sum_{j=1}^{\infty}\frac{z^j}{j\,j!}
=\operatorname{Ei}(z)-\gamma-\log z\quad(z>0),\qquad F(0)=0.
\]

Termwise integration and reindexing yield

\[
\sum_{k=0}^{\infty}\frac{z^k}{k!(k+1)^2}=\frac{F(z)}{z}.
\]

Since \(\mathbb E[T^2]=2/\lambda^2\), conditioning on the Poisson count gives

\[
\begin{aligned}
\lambda^2\mathbb E\bigl[\mathbb E(T\mid N_x)^2\bigr]
&=e^{-z}\left[(z+1)^2+z^2\sum_{k=1}^{\infty}\frac{z^k}{k!(k+1)^2}\right]\\
&=e^{-z}\bigl(1+2z+zF(z)\bigr).
\end{aligned}
\]

Therefore the dimensionless optimal risk at the fixed observation time is exactly

\[
R(z)=\lambda^2\inf_{\widehat T}\mathbb E[(T-\widehat T(N_x))^2]
=2-e^{-z}\bigl(1+2z+zF(z)\bigr).
\]

An independently useful nonnegative expression obtained from conditional variances is

\[
R(z)=e^{-z}\left[1+z^2\sum_{k=1}^{\infty}
\frac{z^k}{k!}\frac{k}{(k+1)^2(k+2)}\right].
\]

**3. Unique global optimizer.** Differentiation using \(F'(z)=(e^z-1)/z\) gives

\[
R'(z)=-e^{-z}g(z),\qquad
g'(z)=\frac{e^z-1}{z}-1-F(z),\qquad
g''(z)=\frac{1+z-e^z}{z^2}<0\quad(z>0).
\]

The limits are \(g(0+)=1\) and \(g'(0+)=0\). Hence \(g'\) is strictly negative everywhere on \((0,\infty)\), by the strict inequality \(e^z>1+z\). Moreover \(g'(1)<0\); strict decrease implies \(g(z)\to-\infty\) as \(z\to\infty\). Consequently \(g\) crosses zero exactly once; \(R'\) changes from negative to positive at that zero. This establishes strict global optimality, including boundary \(z=0\). The other endpoint cannot be a better minimizer: from \(F(z)/e^z\to0\), by l'Hôpital's rule, and \(zF(z)/e^z\to1\), by another application, it follows that \(R(z)\to1\) as \(z\to\infty\). Numerical root evaluation provides the displayed constants; uniqueness is proved analytically.

**4. Binary benchmark.** With only \(I=\mathbf1_{\{N_x>0\}}\), the conditional means are \(x+\lambda^{-1}\) when \(I=0\) and \(\lambda^{-1}-xe^{-z}/(1-e^{-z})\) when \(I=1\). The law of total variance gives exactly

\[
R_{\rm bit}(z)=1-\frac{z^2}{e^z-1}.
\]

Its unique positive interior optimizer is the unique root in \((1,2)\) of \((2-z)e^z=2\). Indeed, after removing the positive prefactors, the derivative of the fraction is controlled by \((2-z)e^z-2\), which first increases and then strictly decreases across the interval \((0,2)\). Direct substitution yields the comparative constants in the finding. The full count is strictly more informative than the binary indicator at each finite positive time because its conditional mean is not constant on the event \(N_x>0\).

## Verification

Run `python verify.py` in an environment with Python, SymPy, and mpmath. The script checks three independent symbolic derivative identities, recomputes the unique-root and risk values at high precision, compares two separately derived series expressions at seven positive arguments, checks dimensional rate scaling and the binary comparison, and tests numerical derivative signs. The accompanying `verification_output.txt` is the direct output of that script. These finite numerical checks do not establish uniqueness or other infinite-range statements; those follow from the proof above.

## Relationship to prior work

Optimal strong approximation of jump-driven processes using discretely observed Poisson paths is studied by Przybyłowicz (2017), including asymptotically optimal nonuniform grids for global jump-diffusion path error. Przybyłowicz, Sobieraj and Stępień (2021) address randomized Euler approximation and complexity for jump SDEs. Neither inspected result asserts the present single-cumulative-count, unbounded-first-arrival squared-risk optimization. Hornberger (2025) studies periodically recorded Poisson arrival data, mixing and rate inference, rather than choosing one count time for the latent first arrival. The present problem concerns a different target and a fixed information budget, and is not obtained by substituting a parameter into these theorems. General conditional order-statistic facts are used as inputs, not claimed as new. Historical priority beyond the located and inspected sources is not independently established.

## Limitations

The result requires a known homogeneous intensity and one noiseless cumulative count; it does not optimize multiple observations, noisy or thresholded counts, adaptive designs, finite observation horizons, nonstationary intensities, or costs for delaying the observation. The full-count and binary risk comparisons concern different optimal observation times. No inference about unknown rate parameters is asserted. The exact universal design constant is a numerical root of a proved unique equation, not a closed elementary constant. Novelty assessment is based on specifically searched and inspected sources and cannot prove exhaustive historical uniqueness.

## References

1. P. Przybyłowicz, *Optimal sampling design for global approximation of jump diffusion SDEs*, arXiv:1701.08311v1, first public version 2017-01-28, https://arxiv.org/abs/1701.08311 . Main result Theorem 4.2 and Sec. 4.1 concern asymptotic global SDE approximation.
2. P. Przybyłowicz, M. Sobieraj, Ł. Stępień, *Efficient approximation of SDEs driven by countably dimensional Wiener process and Poisson random measure*, arXiv:2108.02394v1, first public version 2021-08-05, https://arxiv.org/abs/2108.02394 . See introduction and Secs. 3–4 for finite-sampling numerical complexity.
3. Z. T. Hornberger, *Finite-Horizon Behavior of the Periodically Observed Time-Homogeneous Poisson Process*, *Naval Research Logistics* **72** (2025), 1157–1169, https://doi.org/10.1002/nav.22271 . See model and Theorems 1–3 for periodic arrival-recorded Markov dynamics and mixing.
