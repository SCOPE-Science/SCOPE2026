# Strict collective suppression of transport efficiency in a nonreciprocal Brownian ring

## Finding

Let \(N\ge1\), \(D_1,D_2,L>0\), \(k=2\pi/L\), and \(a\in\mathbb R\). Put \(d=D_1+D_2\). For the sinusoidal chase-and-run diffusion below, the full stationary entropy-production rate \(\sigma\) and the unwrapped tagged diffusivity \(D_{\rm eff}\) satisfy
\[
\sigma=\frac{Na^2k^2d}{2D_1D_2},\qquad
0\le D_{\rm eff}-D_1\le \frac{Na^2}{2d}
=\frac{D_1D_2}{k^2d^2}\sigma.
\]
At \(a=0\) both inequalities are equalities. At \(a\ne0\) the lower inequality is strict, and equality in the upper inequality holds exactly when \(N=1\). For each fixed \(N,D_1,D_2,L\), as \(a\to0\),
\[
D_{\rm eff}=D_1+\frac{Na^2}{2d}
-\frac{N(N-1)a^4}{8d^2(2D_1+D_2)}+O(a^6).
\]
Thus for every nonzero coupling the many-follower efficiency \((D_{\rm eff}-D_1)/\sigma\) is strictly below the single-follower frontier. No comparison of diffusivities or monotonicity in \(N\) at fixed coupling is asserted.

## Assumptions and scope

The real lifts have dynamics
\[
\begin{aligned}
dX_t&=ak\sum_{j=1}^N\sin(k(X_t-Y_{j,t}))\,dt+\sqrt{2D_1}\,dW_{0,t},\\
dY_{j,t}&=ak\sin(k(X_t-Y_{j,t}))\,dt+\sqrt{2D_2}\,dW_{j,t},\qquad 1\le j\le N,
\end{aligned}
\]
where the Brownian motions are independent and the initial positions modulo \(L\) are jointly uniform, independent of future Brownian increments. Define \(D_{\rm eff}=\lim_{t\to\infty}\operatorname{Var}(X_t-X_0)/(2t)\). Entropy production uses unit mobility and Boltzmann constant and includes all coordinates. The theorem is specific to finite \(N\), strictly positive diffusivities, a single harmonic, and no external forcing.

## Proof

Write \(\theta_j=k(X-Y_j)\bmod 2\pi\) and \(\partial_j=\partial/\partial\theta_j\). The relative generator is \(-S+aB\), where
\[
S=-k^2\left[D_1\left(\sum_j\partial_j\right)^2+D_2\sum_j\partial_j^2\right],\qquad
B=k^2\sum_j\left(\sum_{i\ne j}\sin\theta_i\right)\partial_j.
\]
Each drift coefficient is independent of the angle it differentiates, so \(B\) is skew-adjoint on smooth periodic functions in normalized Haar measure \(\mu\). Haar is invariant. The drift in the full torus also has zero divergence: for each pair its \(X\)- and \(Y_j\)-derivatives cancel. Its uniform density is invariant, and the map to relative angles pushes that density to \(\mu\). The tagged drift \(f_a=ag\), with \(g=k\sum_j\sin\theta_j\), has zero Haar mean.

On mean-zero functions set \(\mathcal E(u)=\langle u,Su\rangle\). This energy controls the \(H^1\)-norm by the positive \(D_2\) term and the periodic Poincaré inequality. Thus the bilinear form of \(S-aB\) is coercive and bounded on mean-zero \(H^1\). The equation \((S-aB)\chi_a=f_a\) has a unique mean-zero weak solution, smooth by elliptic regularity. Itô's formula makes \(X_t+\chi_a(\theta_t)\) a martingale up to its initial value. Its noise coefficients in the angular coordinates are
\[
\sqrt{2D_1}\left(1+k\sum_j\partial_j\chi_a\right)
\quad\text{and}\quad -\sqrt{2D_2}\,k\partial_j\chi_a\quad(1\le j\le N).
\]
The linear terms have zero Haar expectation, so the expected quadratic variation per unit time is
\[
2D_1+2k^2\int\left[D_1\left(\sum_j\partial_j\chi_a\right)^2+D_2\sum_j(\partial_j\chi_a)^2\right]d\mu
=2D_1+2\mathcal E(\chi_a).
\]
The bounded corrector difference has bounded variance and changes the martingale variance by at most \(O(\sqrt{t}+1)\). Consequently \(D_{\rm eff}-D_1=\mathcal E(\chi_a)=\langle f_a,\chi_a\rangle\), using skew-adjointness.

Put \(u_0=S^{-1}g=(kd)^{-1}\sum_j\sin\theta_j\). The energy of \(au_0\) is \(Na^2/(2d)\). Expanding the squared energy of the difference and using \(S(au_0)=f_a\) proves the exact deficit identity
\[
\frac{Na^2}{2d}-(D_{\rm eff}-D_1)=\mathcal E(\chi_a-au_0).
\]
For \(a\ne0\) the lower bound cannot be an equality because \(f_a\ne0\). Equality in the upper bound is equivalent to \(\chi_a=au_0\), hence to \(Bu_0=0\). Directly,
\[
Bu_0=\frac{k}{d}\sum_{i<j}\sin(\theta_i+\theta_j).
\]
The sum is empty at \(N=1\) and otherwise contains nonzero mutually orthogonal Fourier modes. This proves strictness for every nonzero \(a\) at \(N\ge2\).

The full stationary current equals the drift times the uniform density. Averaging the sum of the squared drift components divided by their diffusion coefficients yields \(\sigma=(Na^2k^2/2)(D_1^{-1}+D_2^{-1})\): the sines are orthogonal and each has squared Haar norm \(1/2\).

Finally, \(S^{-1}B\) is bounded on mean-zero \(H^1\) by ellipticity and bounded smooth drift coefficients. A Neumann series gives analytic dependence of the corrector near zero, with \(\chi_a-au_0=a^2 S^{-1}Bu_0+O(a^3)\) in the energy norm. The deficit is even in \(a\) by translating every relative angle by \(\pi\), which conjugates the equations at \(a\) and \(-a\). The coefficient of \(a^4\) in the deficit is therefore \(\langle Bu_0,S^{-1}Bu_0\rangle\), and the remainder is \(O(a^6)\). The pair-sum modes have eigenvalue \(k^2(4D_1+2D_2)\) under \(S\), so the coefficient is \(\binom N2/[2d^2(4D_1+2D_2)]\), as stated. The remainder need not be uniform in the parameters.

## Verification and relationship to prior work

The finite Fourier checks in `verify.py` are numerical consistency tests; the proof above establishes the all-coupling result and the analytic remainder. Zhang and Garcia-Millan, *Entropy production of non-reciprocal interactions* ([arXiv:2209.09721](https://arxiv.org/abs/2209.09721)), introduced the chase-and-run model and studied its uniform stationary law and entropy production. The single-follower efficiency frontier is also described in [*Exact spectral tomography and a sharp transport–dissipation frontier for a nonreciprocal Brownian pair*](https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-exact-spectral-tomography-and-a-sharp-transport-dissipation-fron--2c35e3026ea0). Benois et al., *Enhanced diffusion of tracer particles in nonreciprocal mixtures* ([arXiv:2307.05408](https://arxiv.org/abs/2307.05408)), study transport in a nonreciprocal binary suspension. Here the model-specific result is the strict deficit from the frontier at all nonzero couplings for \(N\ge2\) and its first, explicitly collective coefficient, not a new general corrector method or a priority guarantee.
