# Alternating long–short spectral steps eliminate the balanced two-mode slowdown

## Finding
For a real symmetric positive-definite operator \(H\) with exactly two distinct eigenvalues \(0<b<a\), alternating delayed long and short Barzilai–Borwein steps, initialized by an undelayed long step, converges doubly exponentially from **every** starting residual with both spectral projections nonzero. Precisely, for the residuals defined below,
\[
\lim_{k\to\infty}\frac{1}{k}\log\log\frac{\|r_0\|_2}{\|r_k\|_2}=\log\sqrt{2}.
\]
If the initial residual lies in one eigenspace, the first step terminates exactly. Hence no mixed initial residual has the balanced geometric orbit that is possible with the unmixed long-step rule.

## Assumptions and scope
Let \(H\) be a real symmetric positive-definite matrix with spectrum exactly \(\{a,b\}\), where \(a>b>0\), with arbitrary positive multiplicities. Write \(P_a,P_b\) for orthogonal spectral projections. Let \(r_0\ne0\). Define \(r_{k+1}=(I-\alpha_k H)r_k\) and
\[
\alpha_0=\frac{\|r_0\|_2^2}{r_0^\top H r_0},\qquad
\alpha_k=\begin{cases}
\frac{\|r_{k-1}\|_2^2}{r_{k-1}^\top H r_{k-1}},&k\ge1\text{ odd},\\
\frac{r_{k-1}^\top H r_{k-1}}{r_{k-1}^\top H^2 r_{k-1}},&k\ge2\text{ even}.
\end{cases}
\]
All denominators are positive before termination. These are the delayed long (BB1) and short (BB2) spectral steps on a quadratic, taken in a fixed alternating order. The statement concerns exact arithmetic; it asserts R-type double-exponential decay, not one-step Q-superlinear convergence.

## Proof
**Step 1: exact two-mode dynamics.** If one spectral projection vanishes, \(\alpha_0\) equals the inverse of that eigenvalue, and \(r_1=0\). Otherwise, both spectral projections remain nonzero for all finite iterations, because the high- and low-mode update factors for a long step are respectively
\[
-\frac{a-b}{ae^\phi+b},\quad \frac{(a-b)e^\phi}{ae^\phi+b},
\]
and for a short step are
\[
-\frac{b(a-b)}{a^2e^\phi+b^2},\quad \frac{a(a-b)e^\phi}{a^2e^\phi+b^2},
\]
where \(\phi=\log(\|P_a r_{k-1}\|_2^2/\|P_b r_{k-1}\|_2^2)\). These factors are nonzero for finite positive spectral weights.

Set \(\phi_k=\log(\|P_a r_k\|_2^2/\|P_b r_k\|_2^2)\) and \(L=\log(a/b)>0\). The first step gives \(\phi_1=-\phi_0\). Thereafter the exact ratio recurrence is
\[
\phi_{k+1}=\phi_k-2\phi_{k-1}+c_k,\qquad
c_k=\begin{cases}0&k\text{ odd},\\-2L&k\text{ even}.\end{cases}
\]

**Step 2: the incompatible exceptional cycle.** The forced recurrence has the unique bounded two-periodic particular solution \(p_{2j}=-L/4\), \(p_{2j+1}=-3L/4\). Put \(\psi_k=\phi_k-p_k\). Then \(\psi_{k+1}=\psi_k-2\psi_{k-1}\). Its characteristic roots are \(\sqrt2 e^{\pm i\theta}\) with \(\cos\theta=1/(2\sqrt2)\). Were \(\psi\) zero, the first step would demand both \(\phi_0=-L/4\) and \(\phi_1=L/4=-3L/4\), impossible for \(L>0\). Therefore the homogeneous oscillation is nonzero for *every* mixed initial residual:
\[
\psi_k=C(\sqrt2)^k\cos(k\theta-\delta),\qquad C>0.
\]

**Step 3: both signs appear at the exponential scale.** The angular points \(0,\theta,2\theta,3\theta\) have maximum circular gap \(\max\{\theta,2\pi-3\theta\}<\pi\), since \(\pi/3<\theta<\pi/2\). Consequently a fixed \(\eta>0\), depending on \(\theta\) alone, exists such that every four successive cosines contain one at least \(\eta\) and another at most \(-\eta\) (for any phase shift). In every four successive indices starting at \(j\), therefore, \(\psi\) has positive and negative values of magnitude at least \(\eta C(\sqrt2)^j\). Since \(p_k\) is bounded, the same lower bound up to a factor of two holds for \(\phi\) for all sufficiently large \(j\).

**Step 4: sharp decay.** For either step type the logarithm of the magnitude of the multiplier of the high mode differs from \(-\max\{\phi_{k-1},0\}\) by a uniformly bounded constant (depending only on \(a,b\)); for the low mode it differs from \(-\max\{-\phi_{k-1},0\}\) by a uniformly bounded constant. This follows immediately by factoring \(e^{\max(\phi,0)}\) out of each positive denominator in Step 1. Summing over updates gives, for each mode \(s\in\{a,b\}\), constants \(d_s,D_s>0\) and a finite index after which
\[
-D_s(\sqrt2)^k\le\log\frac{\|P_s r_k\|_2}{\|P_s r_0\|_2}
\le-d_s(\sqrt2)^k.
\]
The lower bound follows from \(|\phi_j|\le C_1(\sqrt2)^j\), and the upper bound follows by applying the four-index positive/negative excursion bound to the final four contributing updates; the additive \(O(k)\) terms are negligible. Combining the two orthogonal components yields \(\exp[-D(\sqrt2)^k]\le\|r_k\|_2/\|r_0\|_2\le\exp[-d(\sqrt2)^k]\) for suitable positive constants and sufficiently large \(k\). Taking two logarithms proves the displayed limit. There is no claim of convergence at finite precision.

## Verification
Run `python3 verify.py` using Python's standard library. It checks the two-mode recurrence against independent exact-rational iterates for different eigenvalues and starting vectors, verifies the nonzero forced particular solution and its incompatibility with the initialization, checks the homogeneous linear recurrence, and checks its two-sided four-step phase excursions. The recorded output is `VERIFY_OK 2256 exact-rational and independent recurrence checks`. The infinite-step bounds in the theorem are analytic; no finite test purports to prove them.

## Relationship to prior work
The long and short Barzilai–Borwein steps, two-dimensional R-superlinear behavior for each fixed choice, and convergence of delayed gradient schemes are classical [1,2]. Recent results give R-linear guarantees for fixed spectral weights [3], exhibit open sets of higher-dimensional nonsuperlinear BB1 behavior [4], and study a different cyclic historical-step mechanism [5]. The claimed contribution is **not** a new individual BB formula or generic superlinearity: it is the exact all-start elimination of the two-mode balanced geometric exception by the *specific alternating* long/short delayed sequence, together with the sharp double-log rate. A more recent delayed-residual treatment [6] analyzes the unmixed step and is not used to set the eligible source date. The comparison does not claim any result about three or more distinct eigenvalues.

## Limitations
The result is exact arithmetic, fixed two-point spectrum with arbitrary multiplicity, and the specified initialization and parity. Floating-point underflow or rounding can change the observed behavior. No general higher-dimensional or stochastic rate is established. Historical-priority risk remains from unindexed analyses of alternating spectral steps; the claim requires independent expert review before external certification.

## References
[1] J. Barzilai and J. M. Borwein, *Two-Point Step Size Gradient Methods*, IMA Journal of Numerical Analysis **8** (1988), 141–148, https://doi.org/10.1093/imanum/8.1.141.

[2] A. Friedlander, J. M. Martínez, B. Molina, M. Raydan, *Gradient Method with Retards and Generalizations*, SIAM J. Numer. Anal. **36** (1999), 275–289, https://doi.org/10.1137/S003614299427315X.

[3] S. Yang and Y.-x. Yuan, *R-Linear Convergence of Barzilai-Borwein Methods on Strictly Convex Quadratics via Closed-Cone Homogeneous Dynamics*, first public September 10, 2026, https://arxiv.org/abs/2609.12100.

[4] D. Li, X. Jiang, M. Hong, *Barzilai–Borwein Fails Superlinear Convergence on an Open Set of Quadratics for Every Dimension \(n\ge4\)*, first public July 23, 2026, https://arxiv.org/abs/2607.21579.

[5] R. Gu, *Superlinear Convergence of Cyclic Gradient Methods with Historical Ritz Step Sizes*, first public October 23, 2026, https://arxiv.org/abs/2610.32705.

[6] X. Xu, *Two-point residual step size gradient methods for linear systems*, first public November 2, 2026, https://arxiv.org/html/2611.02743v1.
