# An all-time entropy-process invariance despite switching-controlled transport in an active dimer

## Finding
In the fluctuation-driven, maximally nonreciprocal two-particle harmonic model of Cocconi, Alston and Bertrand [1], the **entire stochastic process** of center-of-mass medium entropy production is independent in law of the orientation-switching rate, even though center-of-mass diffusion depends strictly on it. The result is an exact dynamical identifiability obstruction, stronger than the previously established independence of the *mean* entropy-production rate.

Let \(k,\kappa,D,\lambda>0\), let \(W^x,W^y\) be independent standard Brownian motions, and let \(S\) be an independent stationary symmetric \(\{\pm1\}\)-valued telegraph process that flips at rate \(\lambda\). Consider
\[
\begin{aligned}
 dX_t&=-\kappa S_tY_t\,dt+\sqrt D\,dW^x_t,\\
 dY_t&=-2kY_t\,dt+\sqrt{4D}\,dW^y_t,
\end{aligned}
\]
where \(Y_0\sim N(0,D/k)\) is independent of the drivers. Define the (dimensionless) **center-of-mass medium-entropy functional** by
\[
\Sigma_t=\frac2D\int_0^t (-\kappa S_sY_s)\circ dX_s.
\]
Then for every collection of times \(0\le t_1<\cdots<t_m\), the joint law of \((\Sigma_{t_1},\ldots,\Sigma_{t_m})\) does not depend on \(\lambda\); in fact the law on continuous entropy trajectories is independent of \(\lambda\).

For every \(T\ge0\) and \(q\in[0,1]\), put \(\delta_q=2\sqrt{k^2+4\kappa^2q(1-q)}\). The **exact finite-time Laplace transform** is
\[
\boxed{\displaystyle
 \mathbb E e^{-q\Sigma_T}=\left[
 \frac{e^{2kT}}{\cosh(\delta_qT)+\frac{4k^2+\delta_q^2}{4k\delta_q}\sinh(\delta_qT)}
 \right]^{1/2}.}
\]
Consequently \(\mathbb E e^{-\Sigma_T}=1\), \(\Sigma_T\) has the exact detailed fluctuation symmetry \(\mathbb P(\Sigma_T\in ds)=e^s\mathbb P(\Sigma_T\in-ds)\), and
\[
\begin{split}
 \mathbb E\Sigma_T&=\frac{2\kappa^2}{k}T,\\
 \operatorname{Var}(\Sigma_T)&=\left(\frac{4\kappa^2}{k}+\frac{4\kappa^4}{k^3}\right)T-\frac{\kappa^4}{k^4}(1-e^{-4kT}).
\end{split}
\]
The long-time scaled cumulant-generating function is
\[
\boxed{\displaystyle \lim_{T\to\infty}\frac1T\log\mathbb E e^{-q\Sigma_T}=k-\sqrt{k^2+4\kappa^2q(1-q)}}
\]
for every real \(q\) in the open interval \(\big(\frac{1-\sqrt{1+k^2/\kappa^2}}2,\frac{1+\sqrt{1+k^2/\kappa^2}}2\big)\), where the square root is real (including \([0,1]\)). The center-of-mass effective diffusivity, on the contrary, is
\[
 \boxed{D_{\mathrm{eff}}(\lambda)=\frac D2\left(1+\frac{\kappa^2}{k(k+\lambda)}\right)},
\]
strictly decreasing in \(\lambda>0\).

## Assumptions and scope
This is the unconfined, steric-repulsion-free, maximally antisymmetric **discrete synchronous-switching** branch of [1, Eqs. (2), (17)–(19)]: their notations are \(k=\bar k\), \(\kappa=\kappa_0\), and \(D=D_x\). The two particles have equal bare diffusivities; the antisymmetric stiffness is \(\psi=2\kappa S\), the symmetric stiffness fluctuation is zero. The relative coordinate \(Y\) begins in its unique equilibrium Gaussian law. The center of mass need not have a stationary position distribution because it is unconfined.

The entropy observable is the center-of-mass **medium contribution**, with thermal diffusion coefficient \(D/2\). Neither the entropy of a prescribed nonstationary initial center-of-mass density nor a finite-volume system-boundary entropy term is included. Since the relative-coordinate OU and symmetric telegraph dynamics are autonomous, independent, and reversible in the stated stationary initialization, they contribute no steady housekeeping term. This does *not* assert an exact finite-time total-entropy theorem for an arbitrary nonstationary system preparation.

## Proof
**1. Sign-gauge invariance for the entire entropy path.** Because the velocity \(v_t=-\kappa S_tY_t\) has zero quadratic covariation with \(X_t\)'s Brownian part, the stochastic integral in the definition of \(\Sigma\) has the same Itô and Stratonovich value. Expanding \(dX_t\) gives
\[
 \Sigma_t=\frac{2\kappa^2}{D}\int_0^tY_s^2\,ds-\frac{2\kappa}{\sqrt D}\int_0^tY_sS_s\,dW^x_s.
\]
Put \(\widetilde W_t=\int_0^tS_s\,dW^x_s\). Conditional on the entire \((S,Y)\) path, \(\widetilde W\) is a standard Brownian motion: its increments are centered jointly Gaussian with conditional covariance \(\int S_s^2ds\), exactly the Brownian covariance. Since that conditional law does not depend on \((S,Y)\), \(\widetilde W\) is independent of \((S,Y)\), so in particular of \(Y\). Thus
\[
 \Sigma_t\ \stackrel{\mathrm{process}}{=}\ \frac{2\kappa^2}{D}\int_0^tY_s^2ds-\frac{2\kappa}{\sqrt D}\int_0^tY_s\,dB_s,
\]
with \(B\) an independent standard Brownian motion. Every finite-dimensional distribution and the full continuous-path law are independent of the switching rate \(\lambda\). This argument actually works for any independent predictable sign process with \(|S_s|=1\) almost everywhere, not only for a Markov telegraph clock; only the stated telegraph family is used for the transport comparison.

**2. Conditional Gaussian law and fluctuation symmetry.** Let \(A_T=\int_0^T Y_s^2ds\) and \(c=2\kappa^2/D\). Conditional on the *full* \(Y\) path, stochastic integration with independent \(B\) gives
\[
 \Sigma_T\mid Y\ \sim\ N(c A_T,2c A_T).
\]
Since \(A_T>0\) almost surely for \(T>0\), the conditional density has the ratio \(p(s\mid A_T)/p(-s\mid A_T)=e^s\). Averaging over \(A_T\) proves the exact detailed fluctuation symmetry, without asserting anything about additional system-boundary entropy. Also
\[
 \mathbb E(e^{-q\Sigma_T}\mid Y)=e^{-c q(1-q)A_T}.
\]
At \(q=0,1\) the transform equals one.

**3. Integrated OU-square transform.** With \(u=-c q(1-q)\), consider \(F(t,y)=\mathbb E_y\exp(u\int_0^tY_s^2ds)\). Its Feynman–Kac equation is \(\partial_tF=(-2ky\partial_y+2D\partial_y^2+uy^2)F\), with initial value one. The Gaussian ansatz \(F=e^{A(t)y^2+B(t)}\) gives
\[
 A'=8DA^2-4kA+u,\qquad B'=4DA,\qquad A(0)=B(0)=0.
\]
Writing \(a=2k\) and \(\delta=\sqrt{a^2-8Du}\), the solution is
\[
 A(t)=\frac{u\sinh(\delta t)}{\delta\cosh(\delta t)+a\sinh(\delta t)},\qquad
 B(t)=\frac{at-\log(\cosh(\delta t)+(a/\delta)\sinh(\delta t))}{2}.
\]
The stationary Gaussian initial variance is \(D/k\). Therefore \(\mathbb E e^{uA_T}=e^{B(T)}(1-2(D/k)A(T))^{-1/2}\), whose simplification gives the boxed finite-time formula. For \(q\in[0,1]\), \(u\le0\), the Feynman–Kac solution is finite and the square-root expression is positive. The same calculation works for the stated open real interval where \(\delta>0\) and the stationary integral is finite.

**4. Cumulants and asymptotic growth.** Since \(\operatorname{Cov}(Y_0,Y_s)=(D/k)e^{-2k|s|}\), Wick's formula yields \(\operatorname{Cov}(Y_0^2,Y_s^2)=2(D/k)^2e^{-4k|s|}\). Hence
\[
 \mathbb E A_T=(D/k)T,\quad
 \operatorname{Var}(A_T)=(D/k)^2\left[\frac Tk-\frac{1-e^{-4kT}}{4k^2}\right].
\]
Conditional variance gives \(\operatorname{Var}(\Sigma_T)=2c\mathbb E A_T+c^2\operatorname{Var}(A_T)\) and the displayed cumulant identities. The leading exponential of the positive hyperbolic denominator in the finite-time Laplace formula is \(e^{\delta_qT}\) times a positive prefactor, proving \(\ell(q)=k-\delta_q/2\) on the stated interval, with symmetry under \(q\mapsto1-q\).

**5. Transport is not blind to the sign clock.** The active drift covariance factors by independence:
\[
 \mathbb E(v_0v_s)=\frac{\kappa^2D}{k}e^{-2(k+\lambda)|s|}.
\]
The standard integrated-velocity Green–Kubo formula yields \(D_{\mathrm{eff}}=D/2+\int_0^\infty\mathbb E(v_0v_s)ds\), giving the stated strictly decreasing formula. Therefore two different flip rates have identical *entire entropy process laws* but different long-time position variance growth rates.

## Verification
Run `python3 CHECK.py` using the Python standard library. The included self-contained checker conducts 95 assertions: direct finite-time-transform evaluation versus an independently integrated Riccati/Feynman–Kac ODE for four parameter sets and nine tilts each, Gallavotti–Cohen transform reflection, integral-fluctuation endpoints, derivatives against exact cumulants, a separate numerical quadrature of the OU-square covariance, strict transport sensitivity, and a seeded 18,000-path OU simulation of the conditional Gaussian mixture. At packaging, all 95 assertions passed. The analytic proof above covers arbitrary positive parameters, all finite \(T\), and the full entropy path; finite numerical checks alone do not establish those universal conclusions.

## Relationship to prior work
Cocconi–Alston–Bertrand [1], available in full as the 2023 preprint and open-access published article, derive this exact stochastic model, its full center-of-mass mean-square displacement, the enhanced effective diffusion constant and the mean entropy-production rate \(2\kappa^2/k\) independent of \(\lambda\) [their Eqs. (17)–(19)]. They do not derive the full process law of entropy, its finite-time transform, the Fano-type variance, or the path-level invariance. Those previously published mean/transport statements are credited, **not** claimed as new.

The integrated-square Ornstein–Uhlenbeck Laplace method is classical, including work of Dankel [4]. The novelty assessed here is **not** the standalone OU quadratic-functional integral, nor the generic fluctuation theorem, but its exact embedding and sign-gauge process law in this specific switching nonreciprocal active dimer, paired with flip-rate-dependent transport. Zhang–Garcia-Millan [2] study entropy *rates* for a different interacting model, and Padmanabha and colleagues [3] study entropy cumulants in a different discrete run-and-tumble framework; neither yields this specific joint claim. Equivalent, differently named sign-noise invariances remain a bibliographic risk.

## Limitations
The claim concerns the stated Gaussian relative coordinate, independent fixed-amplitude sign switching, and the medium entropy of the unconfined center-of-mass coordinate. It does not cover variable-amplitude stiffness fluctuations, state-dependent switching correlated with \(Y\), steric interaction affecting the sign-independent Gaussian relative dynamics, or arbitrary initial \(Y\) laws for the displayed stationary transform. Although the sign-gauge lemma extends to independent non-Markov sign clocks, the comparison of \(D_{\mathrm{eff}}\) specifically uses a symmetric telegraph clock. The detailed fluctuation relation is for the defined medium observable, not for an unspecified total entropy including transient boundary terms. No claim is made of independent validation or bibliographic exhaustiveness.

## References
[1] L. Cocconi, H. Alston and T. Bertrand, *Active Bound States Arise From Transiently Nonreciprocal Pair Interactions*, arXiv:2304.07738v1 (first public 2023-04-16), https://arxiv.org/html/2304.07738v1; *Physical Review Research* **5**, 043032 (2023), https://doi.org/10.1103/PhysRevResearch.5.043032.

[2] Z. Zhang and R. Garcia-Millan, *Entropy production of non-reciprocal interactions*, arXiv:2209.09721v2, https://arxiv.org/html/2209.09721v2.

[3] P. Padmanabha, D. M. Busiello, A. Maritan and D. Gupta, *Fluctuations of entropy production of a run-and-tumble particle*, arXiv:2207.12091v2, https://arxiv.org/abs/2207.12091; *Physical Review E* **107**, 014129 (2023).

[4] T. Dankel, *On the Distribution of the Integrated Square of the Ornstein–Uhlenbeck Process*, *SIAM Journal on Applied Mathematics* **51**, 568–574 (1991), https://doi.org/10.1137/0151029 (abstract accessible; full text not verified in this review).
