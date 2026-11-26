# Smooth but nowhere Gevrey at the reset point: the stationary density of proportional Brownian resetting

## Finding

For free one-dimensional Brownian motion subjected at independent exponential times to multiplication of its position by a fixed nonzero contraction, the stationary density is infinitely differentiable, real analytic at every nonzero position, yet **not real analytic, nor of any finite Gevrey order, at the resetting point**. All derivatives at that point are explicit, giving a sharp superfactorial growth law. The distinction holds for both positive contractions and negative contractions combined with reflection.

Precisely, fix \(D,r>0\), \(-1<a<1\) with \(a\ne0\), set \(\rho=|a|\in(0,1)\) and \(\lambda=\sqrt{r/D}\). Let \(p\) be the unique stationary probability density of the process defined below. For all integers \(n\ge0\),

\[
p^{(2n+1)}(0)=0,\qquad
p^{(2n)}(0)=(-1)^n p(0)\lambda^{2n}\rho^{-n^2}
\prod_{j=0}^{n-1}(1-\rho^{2j+1}).
\]

Writing \(Q_\rho=\prod_{j=0}^{\infty}(1-\rho^{2j+1})>0\), the normalized even derivatives converge sharply:

\[
\frac{(-1)^n p^{(2n)}(0)}{p(0)\lambda^{2n}\rho^{-n^2}}
\longrightarrow Q_\rho.
\]

The empty product for \(n=0\) is one. In particular the Taylor series at zero has radius zero. The pointwise density is smooth across zero although no convergent Taylor expansion at zero represents it on a nontrivial interval.

## Assumptions and scope

Let \(W_t\) be standard Brownian motion, independent of a rate-\(r\) Poisson process \(N_t\). Between its jump times the position evolves as \(dX_t=\sqrt{2D}\,dW_t\); at each jump time \(T\), \(X_T=a X_{T-}\). The above conclusions concern its unique stationary distribution, with no spatial drift, for every fixed \(D,r>0\) and \(0<|a|<1\).

For clarity, a function is Gevrey of finite order \(s\ge0\) near zero when there are a neighborhood and constants \(C,A>0\) such that \(|f^{(k)}(x)|\le CA^k(k!)^s\) throughout that neighborhood for all integers \(k\ge0\). The result excludes every finite \(s\) (including real analyticity, the order-one case).

Let the \(q\)-product notation mean \((z;q)_m=\prod_{j=0}^{m-1}(1-zq^j)\) and \((z;q)_\infty=\lim_{m\to\infty}(z;q)_m\) for \(|q|<1\). The central height is the strictly positive finite number

\[
p(0)=\frac{\lambda}{2}\,
\frac{(\rho;\rho^2)_\infty}{(\rho^2;\rho^2)_\infty}.
\]

## Proof

**1. Stationary distribution and Fourier decay.** Under a synchronous coupling using the same Brownian path and the same Poisson jump times, two initial states have difference \(a^{N_t}(X_0-Y_0)\), which converges to zero almost surely. A stationary law exists: in Fourier variables the positive-definite function

\[
\phi(k)=\prod_{j=0}^{\infty}
\left(1+\frac{D}{r}\rho^{2j}k^2\right)^{-1}
\]

is a characteristic function because each factor is that of a centered Laplace variable with scale \(\sqrt{D/r}\,\rho^j\), and the associated independent sum converges in \(L^2\). It satisfies \((r+Dk^2)\phi(k)=r\phi(ak)\). The coupling establishes uniqueness. Its law is symmetric because \(\phi\) is real and even, including when \(a<0\).

For every integer \(M>0\), retaining only the first \(M\) denominator factors shows \(|\phi(k)|\le C_M |k|^{-2M}\) for \(|k|\ge1\). Consequently \(k^m\phi(k)\in L^1(\mathbb R)\) for every integer \(m\ge0\), so Fourier inversion yields \(p\in C^\infty(\mathbb R)\), with all derivatives obtained by differentiating the integral. In particular, odd derivatives vanish at the origin by evenness, and \(p(0)=(2\pi)^{-1}\int\phi(k)\,dk>0\).

**2. Exact jet from the stationary equation.** In the sense of distributions, the steady forward equation is

\[
D p''(x)-rp(x)+\frac{r}{\rho}p(x/a)=0.
\]

Both sides are continuous, and in fact smooth by step 1, so the equation holds pointwise together with every differentiated version. Evenness implies \(p(x/a)=p(x/\rho)\) for either sign of \(a\). Differentiation \(2n\) times at zero gives

\[
p^{(2n+2)}(0)=\lambda^2\bigl(1-\rho^{-(2n+1)}\bigr)p^{(2n)}(0).
\]

Iterate starting from \(p(0)\), and rewrite each factor as \(1-\rho^{-(2j+1)}=-\rho^{-(2j+1)}(1-\rho^{2j+1})\). Since \(\sum_{j=0}^{n-1}(2j+1)=n^2\), the stated exact formula follows.

**3. Sharp growth, failure of every finite Gevrey order.** Because \(0<\rho<1\), the product \(Q_\rho\) converges to a strictly positive number: the sum of \(\rho^{2j+1}\) is finite and each term is strictly less than one. The truncated products converge to it, proving the displayed derivative asymptotic. Quantitatively,

\[
\log |p^{(2n)}(0)|
=n^2\log(1/\rho)+2n\log\lambda+\log(p(0)Q_\rho)+o(1).
\]

For any fixed constants \(s,A,C\), the growth \(n^2\log(1/\rho)\) exceeds \(\log(CA^{2n}((2n)!)^s)=O(n\log n)\). Thus no finite Gevrey bound holds even at the single point zero; in particular the Taylor coefficients \(p^{(2n)}(0)/(2n)!\) have unbounded \(n\)-th roots and the Taylor series has radius zero.

**4. Analyticity off the reset point and exact height.** The known exact Laplace-mode representation for \(x\in\mathbb R\), with \(q=\rho^2\), is

\[
p(x)=\frac{\lambda}{2(q;q)_\infty}
\sum_{m=0}^{\infty}
\frac{(-1)^m\rho^{m^2}}{(q;q)_m}
\exp\bigl(-\lambda\rho^{-m}|x|\bigr).
\]

This is the partial-fraction inversion of the characteristic product (already established in the cited primary sources). On compact subsets of the open complex right half-plane, the positive-side series converges absolutely and locally uniformly, because \((q;q)_m\) stays bounded away from zero and the exponential decays with \(\Re x>0\). It therefore extends holomorphically near every positive real \(x\). Reflection gives the same on the negative half-line. At \(x=0\), Euler's finite \(q\)-binomial identity, after sending its number of factors to infinity, gives

\[
\sum_{m=0}^{\infty}\frac{(-1)^m\rho^{m^2}}{(\rho^2;\rho^2)_m}
=(\rho;\rho^2)_\infty,
\]

which yields the displayed exact value for \(p(0)\). All claims follow.

## Verification

The standalone script `verification/verify_density.py` uses Python and `mpmath` to compare numerical Fourier-integral derivatives with the exact derivative jet for two nontrivial contractions, check the independently normalized Laplace series at zero, and test algebraic recurrences and finite \(q\)-products. It reports 56 passing diagnostic assertions. The proof above establishes the infinite-order and global conclusions; finite quadrature is not treated as a proof of them.

## Relationship to prior work

Pierce (2022) derived the proportional-reset forward pantograph equation and stationary transform. Tal-Friedman, Roichman and Reuveni (2022) identified the independent-Laplace summation mechanism. Di Bello et al. (2023), in their Brownian specialization, give the exact characteristic product and position-space series. Biroli et al. (2024) extend the stationary formula to negative rescaling and analyze the Gaussian-like center; in their Section II, equation (20), they explicitly report only numerical support for even the linear cusp cancellation. The present result does not claim those known distributions or their Gaussian/exponential regimes as new. It proves the stronger exact all-order differentiability, sharp \(\rho^{-n^2}\) derivative law, and the analytic-off-zero/non-Gevrey-at-zero distinction. Classical \(q\)-binomial identities are standard supporting mathematics.

## Limitations

The theorem concerns strictly nonzero contractive reset factors. At \(a=0\), complete resetting gives a Laplace cusp, while \(|a|=1\) admits no stationary probability law for free diffusion; neither endpoint is included. The conclusion is about the stationary probability density, not finite-time densities, higher-dimensional processes, Lévy flights, added drift, or convergence rates of optimal approximations. No claim of publication priority beyond the inspected sources is made. Earlier pantograph smoothness theorems or unindexed equivalent derivations remain a possible literature-coverage risk. A separate independent audit has not been performed.

## References

1. J. K. Pierce, *An advection-diffusion process with proportional resetting*, arXiv:2204.07215, first posted 2022-04-14. https://arxiv.org/abs/2204.07215
2. O. Tal-Friedman, Y. Roichman and S. Reuveni, *Diffusion with Partial Resetting*, arXiv:2205.03363, first posted 2022-05-06. https://arxiv.org/abs/2205.03363
3. C. Di Bello, A. V. Chechkin, A. K. Hartmann, Z. Palmowski and R. Metzler, *Time-dependent probability density function for partial resetting dynamics*, arXiv:2305.13722, first posted 2023-05-23. https://arxiv.org/abs/2305.13722
4. M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar and G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387, first posted 2024-06-12. https://arxiv.org/abs/2406.08387
