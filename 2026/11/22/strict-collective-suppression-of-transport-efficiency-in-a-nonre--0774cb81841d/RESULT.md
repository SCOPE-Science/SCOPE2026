# Strict collective suppression of transport efficiency in a nonreciprocal Brownian ring

## Finding

A periodic chase-and-run system with one tagged particle and any finite number of independently noisy followers has an exact transport–dissipation inequality. Its two-particle member saturates the inequality at every nonzero coupling; adding even one follower makes the inequality strict at **every** nonzero coupling. The first many-follower defect can be calculated exactly at fourth order.

Let \(N\ge1\) be an integer, \(D_1,D_2,L>0\), \(k=2\pi/L\), and \(a\in\mathbb R\). For the stochastic dynamics defined below, denote by \(D_{\mathrm{eff}}\) the tagged particle's long-time *unwrapped* diffusivity and by \(\sigma\) the full stationary entropy-production rate. Then

\[
\sigma=\frac{Na^2k^2(D_1+D_2)}{2D_1D_2},\qquad
0\le D_{\mathrm{eff}}-D_1\le \frac{Na^2}{2(D_1+D_2)}
=\frac{D_1D_2}{k^2(D_1+D_2)^2}\,\sigma.
\]

If \(a\ne0\), the first inequality is strict. The *second* inequality is equality if and only if \(N=1\). For every fixed \(N,D_1,D_2,L\), as \(a\to0\),

\[
D_{\mathrm{eff}}=D_1+\frac{Na^2}{2(D_1+D_2)}
-\frac{N(N-1)a^4}{8(D_1+D_2)^2(2D_1+D_2)}+O(a^6).
\]

Thus the transport efficiency \((D_{\mathrm{eff}}-D_1)/\sigma\) of each nonzero-coupling, many-follower system lies **strictly below** the sharp single-follower transport–dissipation frontier. The positive fourth-order defect is the first quantitative collective suppression term. No monotonicity in the follower count at fixed coupling is asserted.

## Assumptions and scope

On the real line, let \(X_t,Y_{1,t},\ldots,Y_{N,t}\) be independent-noise Brownian particle lifts whose periodic positions are understood modulo \(L\). Let \(W_0,W_1,\ldots,W_N\) be independent standard Brownian motions. Consider

\[
\begin{aligned}
 dX_t&=ak\sum_{j=1}^N\sin(k(X_t-Y_{j,t}))\,dt+\sqrt{2D_1}\,dW_{0,t},\\
 dY_{j,t}&=ak\sin(k(X_t-Y_{j,t}))\,dt+\sqrt{2D_2}\,dW_{j,t},\qquad 1\le j\le N.
\end{aligned}
\]

Equivalently, the pair potentials in Zhang–Garcia-Millan's chase-and-run convention are \(V_1(z)=a\cos(kz)\) and \(V_2(z)=-a\cos(kz)\); both pair forces point in the same signed direction. Initially all periodic coordinates are jointly uniform on the \((N+1)\)-torus, independent of future Brownian increments. The coefficient \(D_{\mathrm{eff}}\) is \(\lim_{t\to\infty}\operatorname{Var}(X_t-X_0)/(2t)\), which exists by the corrector construction below. Entropy production uses unit mobility and Boltzmann constant and includes *every* coordinate, not only the observed particle. The theorem is for positive \(D_2\), fixed finite \(N\), the indicated single harmonic, and no external forcing.

## Proof

**1. Uniform stationary environment.** Define \(\theta_j=k(X-Y_j)\pmod{2\pi}\). Write \(d=D_1+D_2\), and let angular derivatives be \(\partial_j\). The relative process has generator \(\mathcal L_a=-S+aB\), where

\[
S=-k^2\left[D_1\left(\sum_j\partial_j\right)^2+D_2\sum_j\partial_j^2\right],\qquad
B=k^2\sum_{j=1}^N\left(\sum_{i\ne j}\sin\theta_i\right)\partial_j.
\]

Every coefficient in the \(j\)-th drift is independent of \(\theta_j\), so \(B\) is divergence-free and skew-adjoint in the normalized Haar \(L^2\) space. Since \(D_2>0\), \(S\) is strictly positive on mean-zero functions; uniform measure is the unique invariant probability measure of the relative process. Full torus uniformity likewise follows by summing derivatives of the original drift, and the tagged mean drift is zero.

**2. Effective diffusion and exact deficit identity.** With \(f_a(\theta)=ak\sum_j\sin\theta_j\), the mean-zero periodic Poisson equation

\[
(S-aB)\chi_a=f_a
\]

has a unique smooth solution. The corrected coordinate \(X_t+\chi_a(\theta_t)\) is a martingale. Under the Haar stationary law its quadratic variation has mean rate

\[
2D_1+2\int\left[D_1\left(\sum_j\partial_j\chi_a\right)^2+D_2\sum_j(\partial_j\chi_a)^2\right]d\mu,
\]

because the integral of each periodic derivative vanishes. Since the corrector is bounded, the same asymptotic variance holds for \(X_t\). With the energy \(\mathcal E(u)=\langle u,Su\rangle\), skew-adjointness gives

\[
D_{\mathrm{eff}}-D_1=\mathcal E(\chi_a)=\langle f_a,\chi_a\rangle.
\]

Set \(\chi_a^{(0)}=S^{-1}f_a=\frac{a}{kd}\sum_j\sin\theta_j\). Expanding the energy of their difference gives the **exact identity**

\[
\boxed{\quad\frac{Na^2}{2d}-(D_{\mathrm{eff}}-D_1)=\mathcal E(\chi_a-\chi_a^{(0)})\ge0.\quad}
\]

Here \(\langle f_a,S^{-1}f_a\rangle=Na^2/(2d)\) follows from the independent Fourier first harmonics. If \(a\ne0\), \(\mathcal E(\chi_a)>0\), since otherwise the corrector would be constant and \(f_a=0\). Equality in the upper bound means \(\chi_a=\chi_a^{(0)}\), hence \(B\chi_a^{(0)}=0\). But

\[
B\chi_a^{(0)}=\frac{ak}{d}\sum_{1\le i<j\le N}\sin(\theta_i+\theta_j).
\]

This vanishes identically if \(N=1\); for \(N\ge2\), it is not the zero trigonometric polynomial. Therefore equality holds exactly for one follower (or trivially at zero coupling).

**3. Exact entropy production.** The full uniform density has zero gradient, and its stationary currents equal the original drifts times this density. On averaging their squared currents with inverse diffusion coefficients, the independent sine modes give

\[
\sigma=\frac1{D_1}\left\langle\left(ak\sum_j\sin\theta_j\right)^2\right\rangle
+\frac1{D_2}\sum_j\langle(ak\sin\theta_j)^2\rangle
=\frac{Na^2k^2}{2}\left(\frac1{D_1}+\frac1{D_2}\right).
\]

Combining this with Step 2 proves the stated sharp frontier.

**4. The exact first collective correction.** On the mean-zero Haar space, \(S^{-1}B\) is bounded and the Poisson solution is analytic in \(a\) near zero. The map \((a,\theta)\mapsto(-a,\theta+\pi\mathbf1)\) preserves the dynamics, so the effective diffusion is even in \(a\). Writing \(f_a=af_0\) and \(u_0=S^{-1}f_0\), the first nonzero perturbation beyond \(a^2\) is

\[
-a^4\langle Bu_0,S^{-1}Bu_0\rangle,
\qquad Bu_0=\frac{k}{d}\sum_{i<j}\sin(\theta_i+\theta_j).
\]

The pair-sum Fourier harmonics are mutually orthogonal, each with squared Haar norm \(1/2\) and eigenvalue \(k^2(4D_1+2D_2)\) under \(S\). Hence

\[
\langle Bu_0,S^{-1}Bu_0\rangle
=\frac{\binom N2}{2d^2(4D_1+2D_2)}
=\frac{N(N-1)}{8d^2(2D_1+D_2)}.
\]

This proves the fourth-order coefficient and, by even analyticity, the \(O(a^6)\) remainder for each fixed set of positive parameters. The remainder is not claimed uniform in \(N\), \(k\), or any singular diffusion limit.

## Verification

`verify.py` separately builds finite Fourier–Galerkin representations of the mean-zero Poisson problem, checks the sharp bound and its equality distinction for \(N=1,2,3\), and compares small-amplitude solutions to the displayed fourth-order coefficient for three unequal/equal diffusivity pairs. It also verifies the pair-frequency trigonometric identity symbolically. Run `python verify.py` with NumPy, SciPy and SymPy installed. The finite truncations test the analytic calculation but do **not** replace the infinite-dimensional proof in Steps 1–4.

## Relationship to prior work

Zhang and Garcia-Millan (2022, arXiv:2209.09721) introduced this chase-and-run particle model, proved uniform stationary densities and obtained the full entropy-production expression for arbitrary follower count. These are *inputs* and are not claimed as discoveries here. Benois and collaborators (2023, arXiv:2307.05408) study nonreciprocal tracer diffusion via simulations, a weak-interaction field approximation and low-density two-body theory in a different binary suspension. The directly relevant published published-finding corpus result *Exact spectral tomography and a sharp transport–dissipation frontier for a nonreciprocal Brownian pair* already proves the sharp \(N=1\) efficiency frontier. The present specific claim concerns the exact **strict** failure of saturation for **every** \(N\ge2\) and **every** nonzero coupling, plus its many-body fourth-order defect. It does not claim novelty for the single-follower bound or for the abstract variational energy inequality, which is a standard homogenization tool.

## Limitations

The conclusion is a mathematical classification in this sinusoidal, periodic chase-and-run model, not a universal bound for all nonequilibrium mixtures. The stationary ensemble is essential; noise coefficients are positive; the result does not establish monotonic decrease of diffusivity or efficiency with \(N\) at fixed coupling. The fourth-order expansion is a local asymptotic for fixed \(N\), not an estimate at arbitrary coupling. Broader published work on periodic incompressible advection and other nonreciprocal mixtures could imply parts of the general energy argument; novelty concerns the exact sharp and strict **model-specific** many-follower classification and coefficient. Priority assessment remains limited to the sources inspected and is not independently certified.

## References

1. Z. Zhang and R. Garcia-Millan, *Entropy production of non-reciprocal interactions*, arXiv:2209.09721, first posted 20 September 2022, especially the stochastic dynamics, chase-and-run stationary law, and Eq. (9). https://arxiv.org/abs/2209.09721
2. A. Benois, M. Jardat, V. Dahirel, V. Démery, J. Agudo-Canalejo, R. Golestanian and P. Illien, *Enhanced diffusion of tracer particles in nonreciprocal mixtures*, arXiv:2307.05408, first posted 11 July 2023. https://arxiv.org/abs/2307.05408
3. *Exact spectral tomography and a sharp transport–dissipation frontier for a nonreciprocal Brownian pair*, published-finding corpus mathematical record, 25 October 2026, full RESULT.md inspected. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-spectral-tomography-and-a-sharp-transport-dissipation-fron--2c35e3026ea0
4. D. S. Dean, I. T. Drummond and R. R. Horgan, *Effect of helicity on the effective diffusivity for incompressible random flows*, Phys. Rev. E 63, 061205 (2001), general dispersion background; abstract only inspected. https://doi.org/10.1103/PhysRevE.63.061205
