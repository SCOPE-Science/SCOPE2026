# Finite-size rounding of a fluctuating-rate first-passage transition

## Finding

A nearest-neighbor walker with independently refreshed heavy-tailed jump rates has an exact finite-volume physical-time mean first-passage law. Place an absorbing site at \(0\), suppress jumps beyond the reflecting site \(N\), and start at any fixed integer \(j\geq1\). The jump rate is resampled every \(\tau>0\) units of physical time from the distribution with Laplace transform \(\mathbb E[e^{-s\lambda}]=(1+s^\alpha)^{-1}\), where \(0<\alpha\leq1\). Let \(T_N\) be the time of absorption. For all integers \(N\geq j\), its mean is the explicit finite sum

\[
\mathbb E_j T_N=\frac{2}{2N+1}\sum_{m=0}^{N-1}
\sin(j\theta_m)\cot(\theta_m/2)\,
F_{\alpha,\tau}(1-\cos\theta_m),
\qquad\theta_m=\frac{(2m+1)\pi}{2N+1},
\]

where

\[
F_{\alpha,\tau}(s)=\tau^{1-\alpha}s^{-\alpha}
+\tau\int_0^1\frac{1-u^\alpha}{1+(\tau s)^\alpha u^\alpha}\,du.
\]

At fixed \(j\) and \(\tau\), this mean has three *sharp* volume regimes:

\[
\begin{array}{ll}
0<\alpha<1/2:& \mathbb E_j T_N\longrightarrow M_\infty(j,\alpha,\tau)<\infty,\\[2pt]
\alpha=1/2:&\displaystyle \mathbb E_j T_N=
\frac{2j\sqrt{2\tau}}{\pi}\log N+O(1),\\[4pt]
1/2<\alpha\leq1:&\displaystyle
\mathbb E_j T_N\sim \frac{2^{3\alpha+1}j\,\tau^{1-\alpha}}{\pi^{2\alpha}}
(1-2^{-2\alpha})\zeta(2\alpha)\,N^{2\alpha-1}.
\end{array}
\]

Here \(\zeta\) is the Riemann zeta function and the finite limiting mean in the first regime is given by the absolutely convergent integral

\[
M_\infty(j,\alpha,\tau)=\frac1\pi\int_0^\pi
\sin(j\theta)\cot(\theta/2)F_{\alpha,\tau}(1-\cos\theta)\,d\theta.
\]

The transition has an explicit *finite-size scaling function*. For every fixed \(u\in\mathbb R\), choose \(\alpha_N=\tfrac12+u/\log N\), with \(N\) large enough that \(0<\alpha_N\leq1\). Then

\[
\boxed{\lim_{N\to\infty}
\frac{\mathbb E_j T_N}{\sqrt\tau\log N}
=\frac{2\sqrt2\,j}{\pi}\,\Phi(u),\qquad
\Phi(u)=\begin{cases}\dfrac{e^{2u}-1}{2u},&u\ne0,\\1,&u=0.\end{cases}}
\]

Thus the half-line divergence at the critical tail exponent is rounded by a reflecting boundary through a universal logarithmic crossover, including its exact amplitude. The physical-time renewal correction is nonnegative and bounded independently of the interval size:

\[
0\leq \mathbb E_j T_N-\tau^{1-\alpha}(A_N^{-\alpha}\mathbf1)_j
\leq\frac{\tau\alpha}{1+\alpha}.
\]

## Assumptions and scope

The state space prior to absorption is \(\{1,\ldots,N\}\). Conditional on the current rate \(\lambda\), a particle at an interior site \(i\) attempts each of the two nearest-neighbor jumps at rate \(\lambda/2\). A jump from \(1\) to \(0\) absorbs the particle. At \(N\), the attempted jump to \(N+1\) is suppressed rather than redirected; hence its only physical jump is to \(N-1\), at rate \(\lambda/2\). At \(N=1\), only the attempted jump to \(0\) remains. This boundary convention is essential to the numerical constants.

Rates \(\lambda_0,\lambda_1,\ldots\) are independent, drawn afresh at deterministic physical times \(0,\tau,2\tau,\ldots\), independently of the jump attempts. The clock starts with a fresh draw at time zero. The distribution is determined by its completely monotone Laplace transform \((1+s^\alpha)^{-1}\), which is a probability law on nonnegative rates for \(0<\alpha\leq1\). For \(\alpha=1\) it is the unit-mean exponential law. Absorption may happen *within* a refresh interval; it is not postponed until a refresh boundary.

Let \(A_N\) be the positive killed generator with diagonal \(1\) for indices \(1,\ldots,N-1\), diagonal \(1/2\) at \(N\), and nearest-neighbor off-diagonal entries \(-1/2\). For \(N=1\), \(A_1=[1/2]\). Matrix fractional powers are defined by the ordinary real symmetric spectral calculus. The volume limits hold with the starting site \(j\) and the refresh duration \(\tau\) fixed. They are not joint limits with a growing starting position or a varying refresh interval.

## Proof

**1. Physical-time renewal and the exact scalar function.** Conditional on one rate draw, the killed transition matrix at elapsed physical time \(t\) is \(e^{-\lambda t A_N}\). Averaging rates gives \(G(t)=(I+(tA_N)^\alpha)^{-1}\). The survival transition matrix after one complete refresh interval is \(K=G(\tau)\), and the expected amount of time spent alive during that interval, as a linear operator on starting states, is \(B=\int_0^\tau G(t)\,dt\). The Markov renewal equation is \(h=B\mathbf1+Kh\). Every eigenvalue of \(K\) is strictly less than one, because \(A_N\) is positive definite, so this equation uniquely yields \(h=(I-K)^{-1}B\mathbf1=F_{\alpha,\tau}(A_N)\mathbf1\).

For a positive eigenvalue \(s\), the eigenvalue of \((I-K)^{-1}B\) is

\[
\frac{1+(\tau s)^\alpha}{(\tau s)^\alpha}
\int_0^\tau\frac{dt}{1+(ts)^\alpha}.
\]

Changing variables \(t=\tau u\), and subtracting \(\tau(\tau s)^{-\alpha}\), gives precisely the displayed formula for \(F_{\alpha,\tau}\). Because \(A_N\) is the negative of a substochastic Markov generator, \(A_N^\alpha\) also generates a substochastic semigroup by subordination. Hence \((I+cA_N^\alpha)^{-1}\) is a nonnegative contraction on vectors bounded between zero and \(\mathbf1\), for every \(c\geq0\). Applying this to the remainder integral and using \(\int_0^1(1-u^\alpha)du=\alpha/(1+\alpha)\) proves the stated two-sided correction bound, without any numerical approximation.

**2. The exact mixed-boundary spectrum.** The normalized eigenvectors of \(A_N\) are multiples of \(\sin(i\theta_m)\), with \(\theta_m=(2m+1)\pi/(2N+1)\) and eigenvalues \(s_m=1-\cos\theta_m\). The boundary equation \(\sin((N+1)\theta_m)=\sin(N\theta_m)\) enforces the reflecting endpoint. Direct finite trigonometric summation gives

\[
\sum_{i=1}^N\sin^2(i\theta_m)=\frac{2N+1}{4},\qquad
\sum_{i=1}^N\sin(i\theta_m)=\frac12\cot(\theta_m/2).
\]

Expanding \(F(A_N)\mathbf1\) in this basis proves the finite spectral-sum expression for every allowed parameter and starting site.

**3. The bounded and divergent regimes.** Write \(H_{\alpha,N}=(A_N^{-\alpha}\mathbf1)_j\), so the correction bound gives \(\mathbb E_jT_N=\tau^{1-\alpha}H_{\alpha,N}+O(1)\), with an error bounded between zero and \(\tau\alpha/(1+\alpha)\). For small positive \(\theta\), uniformly when \(\alpha\) is in a compact subset of \((0,1]\),

\[
\sin(j\theta)\cot(\theta/2)(1-\cos\theta)^{-\alpha}
=2^{\alpha+1}j\,\theta^{-2\alpha}(1+O(\theta^2)).
\]

The same expression is bounded in absolute value by a constant times \(\theta^{-2\alpha}\) throughout the spectral interval. At \(\alpha<1/2\), midpoint Riemann-sum convergence therefore yields the absolutely convergent integral for \(M_\infty\), including the bounded correction function \(F\).

For \(\alpha>1/2\), scale \(H_{\alpha,N}\) by \(N^{1-2\alpha}\) and take each fixed mode. The limiting contribution of mode \(m\) is

\[
\frac{2^{3\alpha+1}j}{\pi^{2\alpha}(2m+1)^{2\alpha}}.
\]

The global \(\theta^{-2\alpha}\) bound provides a summable upper bound in \(m\), so dominated convergence applies to all modes, not merely a finite truncation. The odd-integer sum is \(\sum_{m\geq0}(2m+1)^{-2\alpha}=(1-2^{-2\alpha})\zeta(2\alpha)\), proving the power law and its exact coefficient. At \(\alpha=1\), the coefficient reduces to \(2j\), consistent with the usual killed-walk mean \((A_N^{-1}\mathbf1)_j=j(2N+1-j)\).

At \(\alpha=1/2\), the singular midpoint sum is harmonic. Comparing it with the integral of \(\theta^{-1}\) from a lower cutoff of order \(N^{-1}\) gives \(H_{1/2,N}=(2\sqrt2\,j/\pi)\log N+O(1)\), and the physical-time correction remains bounded.

**4. Critical scaling window.** If \(\alpha_N=1/2+u/\log N\), the small-angle expansion and midpoint-integral comparison are uniform for each fixed \(u\). The difference between the singular sum and the corresponding integral is bounded for this sequence, as are the contributions from angles bounded away from zero and the physical-time remainder. The singular integral has leading term

\[
\frac{2^{\alpha_N+1}j}{\pi}
\int_{1/N}^{1}\theta^{-2\alpha_N}d\theta
=\frac{2\sqrt2\,j}{\pi}\log N
\left(\frac{e^{2u}-1}{2u}+o(1)\right),
\]

with its continuous limit at \(u=0\). Multiplication by \(\tau^{1-\alpha_N}\to\sqrt\tau\) proves the stated crossover. The arbitrary fixed multiplicative constant in the lower cutoff affects only the bounded error, not the normalized limit. All four steps are finite-dimensional or controlled by explicit summable bounds, with no extrapolation from a finite numerical experiment.

## Verification

The accompanying `verification/check.py` uses independent numerical diagonalization of the actual killed generator and the explicit analytic sine eigenbasis for all starting sites of chains up to length eleven. It checks the positivity and uniform bound for the renewal correction on additional small chains and compares large finite chains with the limiting power, logarithmic, and critical-window predictions. Execute with `OPENBLAS_NUM_THREADS=1 python verification/check.py` in an environment containing NumPy and SciPy. An execution of the checker passed 951 stated numerical checks. None of these finite computations is used as proof of an infinite-volume or uniform-in-parameter assertion.

## Relationship to prior work

Levit and Reuveni (arXiv:2609.26925, publicly available September 22, 2026) establish the rate-fluctuation model and the sharp half-line first-passage transition at \(\alpha=1/2\). That threshold and the original jump-rate distribution are prior work. Arutkin and Reuveni (arXiv:2302.07041) introduce the more general doubly stochastic continuous-time walk and already compute finite-interval first-exit spectral formulas for exponentially refreshed rates with *two absorbing endpoints*; their general eigenmode method motivates but does not state the heavy-tailed, mixed-boundary finite-size crossover here. Angstmann, Han, Henry, and Huang (arXiv:2511.18256) analyze spectral-fractional first passage in related compounded-jump processes, including a finite interval with two absorbing ends; their finite spectral methodology is relevant but concerns a different physical clock and does not state this exact periodically resampled-rate, reflecting-boundary mean or its critical-width crossover. Angstmann and colleagues (arXiv:2410.10077) study fractional diffusion on finite domains and boundary conventions, again for a different microscopic dynamics.

The present claim is the *exact physical-time finite-chain renewal sum, bounded correction and sharp mixed-boundary finite-size transition and crossover* for the periodically refreshed heavy-tailed rates. It does not assert novelty of spectral fractional powers, the known half-line threshold, or generic first-passage renewal machinery. A broader pre-existing boundary resolvent theorem could make parts of this calculation easier; no claim of an exhaustive world-literature search is made.

## Limitations

The reflecting endpoint suppresses outward attempts; another convention such as redirecting them doubles the right-end jump rate and changes coefficients. The fresh-at-zero sampling protocol is required. The limit fixes \(j\) and \(\tau\); it need not apply to starting points at a fixed fraction of the chain. The result is for the specific heavy-tailed rate law with Laplace transform \((1+s^\alpha)^{-1}\), not all heavy-tailed laws, though the low-frequency mechanism suggests extensions. The asymptotic constants are not asserted to be uniform as \(\tau\) changes. Mathematical proof and computational replication do not constitute an independent external audit or an empirical validation of a physical experiment.

## References

1. B. Levit and S. Reuveni, *First Passage in the Presence of Jump Rate Fluctuations: A Transition from Infinite to Finite Mean*, arXiv:2609.26925 (first public September 22, 2026). https://arxiv.org/abs/2609.26925
2. M. Arutkin and S. Reuveni, *Doubly stochastic continuous time random walk*, arXiv:2302.07041 (2023). https://arxiv.org/abs/2302.07041
3. C. N. Angstmann, D. S. Han, B. I. Henry, and B. Z. Huang, *First-Passage Times for the Space-Fractional Spectral Fokker-Planck Equation*, arXiv:2511.18256 (first public November 23, 2025). https://arxiv.org/abs/2511.18256
4. C. N. Angstmann, D. S. Han, B. I. Henry, B. Z. Huang, and Z. Xu, *A compounded random walk for space-fractional diffusion on finite domains*, arXiv:2410.10077 (first public October 14, 2024). https://arxiv.org/abs/2410.10077
5. G. Uchida, H. Miyoshi, and H. Washizu, *First passage time properties of diffusion with a broad class of stochastic diffusion coefficients*, arXiv:2502.20705 (first public February 28, 2025). https://arxiv.org/abs/2502.20705
