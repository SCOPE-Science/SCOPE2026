# Gaussian operator noise forces dimension-dependent risk growth in damped scalar Kaczmarz

## Finding

Consider one scalar Fourier mode of the spectrally damped tensor randomized Kaczmarz (SD-TRK) update. Its operator and right-hand side are observed **once** and reused at each iteration. A positive regularization floor makes every finite-iteration ensemble mean-square error finite, yet the error is unbounded as iteration count increases. The exact leading growth distinguishes real Fourier modes from genuinely complex Fourier modes.

Specifically, write \(A=a_0+\xi\), \(B=a_0x_\star+\eta\), \(\beta=\mathbb E|B|^2>0\), and let the scalar damping be \(\lambda(A)=\lambda_0+\tau|A|^2\). When \(\lambda_0>0\),

\[
\lim_{t\to\infty}\frac{\mathbb E|X_t-x_\star|^2}{\sqrt t}
=2\sqrt\pi(2-\sqrt2)\,\beta\,p_A(0)\sqrt{\frac\omega{\lambda_0}}
\quad\text{for a real Gaussian mode},
\]

and

\[
\lim_{t\to\infty}\frac{\mathbb E|X_t-x_\star|^2}{\log t}
=\pi\beta f_A(0)
\quad\text{for a circular complex Gaussian mode}.
\]

Here \(p_A\) is the one-dimensional probability density and \(f_A\) is the planar probability density. The nonnegative coefficient \(\tau\) does not enter either leading term. When \(\lambda_0=0\), the mean-square error is infinite already for every finite \(t\ge1\), even if \(\tau>0\). In all these regimes the iterates converge almost surely to \(B/A\), which is generally not the noiseless target. These conclusions concern expectation over the fixed noisy input pair, not resampled noise at each step.

## Assumptions and scope

Fix \(a_0\ne0\), \(x_\star\), \(0<\omega<2\), \(\lambda_0,\tau\ge0\), and \(t\in\{0,1,2,\ldots\}\). The observed scalars \(A=a_0+\xi\) and \(B=a_0x_\star+\eta\) are independent. In the real case \(a_0,x_\star,\xi,\eta\in\mathbb R\), with \(\xi\sim N(0,\sigma_A^2)\), \(\sigma_A>0\), and independent \(\eta\) of finite second moment with \(\beta=\mathbb E|B|^2>0\). In the complex case \(a_0,x_\star\in\mathbb C\), \(\xi\sim\operatorname{CN}(0,\sigma_A^2)\) is proper circular complex Gaussian, with \(\mathbb E|\xi|^2=\sigma_A^2>0\), and \(\eta\) is independent with finite second moment and the same positivity condition on \(\beta\). The right-hand noise may itself be Gaussian, as in the motivating double-noise model, but its full distribution is unnecessary.

Start at \(X_0=0\) and apply the **fixed-data** recurrence

\[
X_{t+1}=X_t-\frac{\omega\overline A}{\lambda_0+(1+\tau)|A|^2}\,(AX_t-B),
\]

with the zero-denominator event disregarded (it has probability zero). This is exactly the one-row/one-unknown Fourier-slice update of SD-TRK, with \(\lambda(A)=\lambda_0+\tau|A|^2\). The published implementation's noise-scale coefficient is absorbed in \(\tau\); its prescribed positive floor corresponds to \(\lambda_0>0\). A real-valued tensor's zero-frequency and possible Nyquist modes obey the real case, whereas non-self-conjugate frequencies have proper complex Gaussian noise when the input perturbation is independent identically distributed real Gaussian noise. The theorem is formulated modewise, with no assertion about an arbitrary multidimensional tensor system.

For these Gaussian laws the densities at the origin are strictly positive:

\[
p_A(0)=\frac{\exp[-a_0^2/(2\sigma_A^2)]}{\sqrt{2\pi}\sigma_A},
\qquad
f_A(0)=\frac{\exp[-|a_0|^2/\sigma_A^2]}{\pi\sigma_A^2}.
\]

## Proof

**1. Exact recurrence and conditional limit.** For \(A\ne0\) let

\[
q(A)=\frac{\omega|A|^2}{\lambda_0+(1+\tau)|A|^2},\quad
r(A)=1-q(A),\quad
F_t(A)=1-r(A)^t.
\]

Because \(0<\omega<2\), \(0<q(A)<2\), so \(|r(A)|<1\) for every nonzero observed coefficient. A direct geometric-series calculation yields

\[
X_t=\frac BA F_t(A),\qquad X_t\xrightarrow[t\to\infty]{\mathrm{a.s.}}\frac BA.
\]

**2. No regularization floor.** If \(\lambda_0=0\), then \(q(A)=\omega/(1+\tau)\) and \(F_t(A)=1-[1-\omega/(1+\tau)]^t\ne0\) for each \(t\ge1\). Independence gives

\[
\mathbb E|X_t|^2=\beta |F_t|^2\,\mathbb E|A|^{-2}=+\infty.
\]

Indeed \(\mathbb E|A|^{-2}\) diverges near the origin for a positive continuous Gaussian density in both one and two real dimensions. Since \(|z-x_\star|^2\ge|z|^2/2-|x_\star|^2\), the error second moment also diverges.

**3. Each finite regularized iterate has finite risk.** Suppose \(\lambda_0>0\). For every fixed integer \(t\ge1\) the elementary bounds

\[
|F_t(A)|\le\min\left\{2,\frac{t\omega|A|^2}{\lambda_0}\right\}
\]

hold. Consequently \(|F_t(A)/A|^2\le\min\{4/|A|^2,t^2\omega^2|A|^2/\lambda_0^2\}\), which is integrable against either Gaussian density. Let

\[
I_t=\mathbb E\left[\frac{|F_t(A)|^2}{|A|^2}\right],\quad
\mathbb E|X_t|^2=\beta I_t.
\]

**4. Real-mode asymptotic.** Set \(s_t=\sqrt{\lambda_0/(\omega t)}\), write \(A=s_tu\), and observe for every fixed \(u\in\mathbb R\) that \(F_t(s_tu)\to1-e^{-u^2}\). The preceding minimum bound dominates the rescaled integrand by a constant times \(\min\{u^2,u^{-2}\}\). The real Gaussian density is bounded and continuous. Therefore dominated convergence gives

\[
\lim_{t\to\infty}s_t I_t
=p_A(0)\int_{-\infty}^{\infty}\frac{(1-e^{-u^2})^2}{u^2}\,du
=2\sqrt\pi(2-\sqrt2)\,p_A(0).
\]

The integral follows by integrating differences of Gaussian kernels; explicitly, \(\int_{\mathbb R}(1-e^{-a u^2})u^{-2}\,du=2\sqrt{\pi a}\) for \(a>0\), and expanding the square.

**5. Complex-mode asymptotic.** In polar coordinates, with \(d^2a=r\,dr\,d\theta\),

\[
I_t=\int_0^\infty\frac{F_t(r)^2}{r}\left[\int_0^{2\pi} f_A(re^{i\theta})\,d\theta\right]dr.
\]

For a fixed sufficiently small \(\delta>0\), the angular integral equals \(2\pi f_A(0)+O(r)\), while \(q(r)\) is bounded above and below by positive constant multiples of \(r^2\). On \(0<r<t^{-1/2}\), the inequality \(|F_t(r)|\le Ct r^2\) bounds the integral uniformly. On \(t^{-1/2}\le r\le\delta\), \(F_t(r)=1+O(e^{-ct r^2})\), with an error whose integral against \(dr/r\) is uniformly bounded; hence

\[
\int_0^\delta\frac{F_t(r)^2}{r}\,dr=\frac12\log t+O(1).
\]

The \(O(r)\) angular-density correction and the region \(r\ge\delta\) contribute \(O(1)\). Thus \(I_t=\pi f_A(0)\log t+O(1)\).

**6. From second moment to target risk.** Finally,

\[
\left|\mathbb E|X_t-x_\star|^2-\beta I_t\right|
\le 2|x_\star|\sqrt{\beta I_t}+|x_\star|^2.
\]

In both regularized cases \(I_t\to\infty\), so the difference is lower order. Substituting the results above proves the stated limits, including the independence from \(\tau\). The almost-sure limit was already established in Step 1. \(\square\)

## Verification

The self-contained companion file `verify.py` evaluates the closed recurrence against 30 direct scalar iterates, verifies the nonzero no-floor multiplier for 14 positive iteration counts, and numerically integrates both Gaussian ensemble formulas at six increasing iteration counts (12 quadratures). The computed ratios tend toward the analytically derived coefficients; exact limiting claims rely on the proof, not on numerical extrapolation. Run `python verify.py` with Python 3, NumPy and SciPy. The script prints `VERIFY_OK` if its checks succeed.

## Relationship to prior work

Lee and Choi (2026), arXiv:2607.13552, introduce SD-TRK, give its Fourier-slice formula in Algorithm 1 and their experimental adaptive damping formula in Eq. (4.9), and prove a conditional error recursion for fixed perturbations in Theorem 4.2. Their paper explicitly distinguishes the fixed-noise analysis from Gaussian simulations. The present theorem instead integrates the risk over a once-sampled Gaussian operator, obtaining exact unbounded iteration-count asymptotics; a conditional bound in terms of the random reciprocal observed singular value does not imply these density-dependent sharp constants.

Bergou et al. (2023), arXiv:2308.16904, analyze noisy matrix Kaczmarz using the observed operator's pseudoinverse. The real scalar limit here resembles that sensitivity mechanism but adds finite-iteration asymptotics with a positive damping floor and a complex-frequency contrast. Elfving (2024) studies stationary iterations under right-hand-side noise with fixed operator. Ma and Molitor (2020) establish tensor randomized Kaczmarz convergence for consistent, noiseless tensor systems. None of the compared primary texts states this joint real/complex Gaussian fixed-data risk asymptotic or its leading constants. Earlier probabilistic spectral-filter work could conceivably contain an equivalent scalar result; that is a historical-priority limitation.

## Limitations

This is an exact-arithmetic, scalar, one-row/one-unknown, fixed-noise model. It neither proves divergence for all tensor systems nor contradicts the conditional fixed-realization robustness result for the proposed damped method. The risk is an ensemble **second moment**, not a typical-run guarantee. A positive damping floor delays catastrophic amplification but is not an asymptotic bias-regularizer at infinite iteration count. The complex case assumes a proper circular Gaussian perturbation and independence between the noisy operator and right-hand side. The finite-iteration leading constants do not apply to freshly resampled operator noise, correlated noise, non-Gaussian densities vanishing at the origin, or an adaptive stopping time.

## References

- N. Lee and J. Choi, *A Spectrally Damped Tensor Randomized Kaczmarz Method for Doubly Noisy Tensor Systems*, arXiv:2607.13552, first public posting 2026-07-15. https://arxiv.org/abs/2607.13552
- E. H. Bergou, S. Boucherouite, A. Dutta, X. Li, and A. Ma, *A Note on Randomized Kaczmarz Algorithm for Solving Doubly-Noisy Linear Systems*, arXiv:2308.16904, first posting 2023-08-31. https://arxiv.org/abs/2308.16904
- T. Elfving, *Noise propagation in linear stationary iterations*, *Numerical Algorithms* 99 (2025), 603–625; published online 2024-07-23. https://doi.org/10.1007/s11075-024-01890-0
- A. Ma and D. Molitor, *Randomized Kaczmarz for Tensor Linear Systems*, arXiv:2006.01246, first posting 2020-06-01. https://arxiv.org/abs/2006.01246
