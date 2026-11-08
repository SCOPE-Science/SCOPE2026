# Exact correlation-rate reversal and critical cancellation in an OU-squared noisy trap

## Finding

For the stationary Ornstein–Uhlenbeck-squared noisy-trap model defined below, the full positive-lag particle-position autocovariance has the explicit one-dimensional integral

\[
C(t)=\frac{2D}{\mu}\exp\!\left[-(\kappa-q)t-3b-be^{-\mu t}\right]
J_{\lambda}\!\left(2b(1+e^{-\mu t})\right),\quad
J_{\lambda}(c)=\int_0^1 y^{\lambda-1}e^{cy}\,dy.
\]

Define its observable instantaneous logarithmic relaxation rate by \(h(t)=-\frac{d}{dt}\log C(t)\), with asymptotic limit \(h_\infty=\kappa-q\). For \(\lambda\ge1\), \(h(t)>h_\infty\) for every finite \(t\ge0\). For \(0<\lambda<1\), let \(c_\lambda>0\) be the **unique** solution to \(J_\lambda'(c_\lambda)/J_\lambda(c_\lambda)=1/2\). Then the exhaustive classification is:

- If \(b\le c_\lambda/4\), \(h(t)<h_\infty\) for all \(t>0\); when equality holds, \(h(0)=h_\infty\).
- If \(c_\lambda/4<b<c_\lambda/2\), exactly one finite time \(t_*>0\) satisfies \(h(t_*)=h_\infty\); the rate is strictly above its limit before the crossing and strictly below afterward. The crossing occurs at
  \[
  t_*=\frac{1}{\mu}\log\frac{2b}{c_\lambda-2b}.
  \]
- If \(b\ge c_\lambda/2\), \(h(t)>h_\infty\) for all finite \(t\ge0\).

On the nontrivial boundary \(b=c_\lambda/2\), the usual first exponential correction vanishes and a **positive second-harmonic correction** takes over:

\[
 h(t)-(\kappa-q)
 =4qb\,V_\lambda(2b)e^{-2\mu t}+O(e^{-3\mu t}),
 \qquad V_\lambda(c)=\frac{J_\lambda''(c)}{J_\lambda(c)}
 -\left(\frac{J_\lambda'(c)}{J_\lambda(c)}\right)^2>0.
\]

Off that boundary,
\[
 h(t)-(\kappa-q)
 =q\left(2\frac{J_\lambda'(2b)}{J_\lambda(2b)}-1\right)e^{-\mu t}
 +O(e^{-2\mu t}).
\]

In all cases \(h(t)>0\), and \(C(t)\sim A e^{-(\kappa-q)t}\) with \(A=(2D/\mu)e^{-3b}J_\lambda(2b)>0\). This is a statement about the *position* two-time autocovariance, not the stiffness autocovariance or the stationary variance alone.

## Assumptions and scope

Consider two independent standard Brownian motions \(W,B\) on a two-sided time axis and the Itô dynamics
\[
 dX_t=-(\kappa+K_t)X_t\,dt+\sqrt{2D}\,dW_t,
 \qquad dK_t=-\mu K_t\,dt+\sqrt{2D_K}\,dB_t.
\]
Assume \(\mu,D,D_K>0\), and \(\kappa>2D_K/\mu^2\). Choose the unique stationary centered Gaussian stiffness process \(K\), with \(\mathbb E[K_sK_t]=(D_K/\mu)e^{-\mu|t-s|}\), and the causal stationary square-integrable solution \(X\). Let \(t\ge0\) be a physical time lag; by symmetry the covariance at negative lag is \(C(|t|)\). Write
\[
 q=\frac{D_K}{\mu^2},\qquad b=\frac{D_K}{\mu^3},\qquad
 \lambda=\frac{2(\kappa-2q)}{\mu}>0,\qquad C(t)=\mathbb E[X_0X_t].
\]
All statements hold for each fixed admissible parameter quadruple. The instantaneous rate is defined using the right derivative at \(t=0\), and ordinary derivatives at \(t>0\). The finite-variance threshold is taken from the source, not claimed as new.

## Proof

**1. Stationary convolution and its domain.** For any real \(s<t\), let \(A_{s,t}=\int_s^t K_v\,dv\). The causal solution is
\[
 X_t=\sqrt{2D}\int_{-\infty}^{t}
 \exp[-\kappa(t-s)-A_{s,t}]\,dW_s.
\]
Independence of \(B\) and \(W\), and Gaussian exponential moments, give
\[
 \mathbb E[X_t^2]=2D\int_0^\infty
 e^{-2\kappa u}\exp\!\left(2\operatorname{Var}(A_{t-u,t})\right)du,
\]
where \(\operatorname{Var}(A_{t-u,t})=2q[u-(1-e^{-\mu u})/\mu]\). Hence the integrand decays as \(e^{-(2\kappa-4q)u}\) times a bounded positive factor. The strict inequality \(\kappa>2q\) ensures existence of the stationary Itô integral in \(L^2\), finite variance, and legitimate covariance use below.

**2. The new two-interval Gaussian contraction.** At lag \(t\ge0\) the only Brownian-noise increments common to \(X_0\) and \(X_t\) precede zero. Put \(u\ge0\), \(A_u=\int_{-u}^0 K_v\,dv\), and \(B_t=\int_0^tK_v\,dv\). Their Gaussian covariance data are
\[
 \operatorname{Var}(A_u)=2q\left[u-\frac{1-e^{-\mu u}}{\mu}\right],\quad
 \operatorname{Var}(B_t)=2q\left[t-\frac{1-e^{-\mu t}}{\mu}\right],
\]
\[
 \operatorname{Cov}(A_u,B_t)
 =b(1-e^{-\mu u})(1-e^{-\mu t}).
\]
By conditional Itô isometry and the Gaussian moment-generating identity,
\[
 C(t)=2D\int_0^\infty e^{-\kappa(t+2u)}
 \exp\!\left[2\operatorname{Var}(A_u)+\frac12\operatorname{Var}(B_t)
 +2\operatorname{Cov}(A_u,B_t)\right]du.
\]
Writing \(z=e^{-\mu t}\), this is exactly
\[
 C(t)=2De^{-(\kappa-q)t-b(1-z)}
 \int_0^\infty e^{-(2\kappa-4q)u-2b(1+z)(1-e^{-\mu u})}\,du.
\]
The positive change of variables \(y=e^{-\mu u}\) proves the stated \(J_\lambda\) representation, without analytic continuation or formal series manipulations.

**3. The rate and its monotone tilt.** For every \(\lambda>0\) and real \(c\), define the probability density
\[
 f_{\lambda,c}(y)=\frac{y^{\lambda-1}e^{cy}}{J_\lambda(c)},\qquad 0<y<1,
\]
and put \(M_\lambda(c)=\mathbb E_{\lambda,c}[Y]=J_\lambda'(c)/J_\lambda(c)\). Differentiation under the integral yields
\[
 M_\lambda'(c)=\operatorname{Var}_{\lambda,c}(Y)>0,
 \quad M_\lambda(0)=\frac{\lambda}{\lambda+1},
 \quad \lim_{c\to\infty}M_\lambda(c)=1.
\]
Strict positivity follows because this density is never supported on a single point. Laplace concentration near \(y=1\) gives the stated terminal limit. Differentiating the exact expression for \(C\) gives, identically,
\[
 h(t)=\kappa-q+qz\left[2M_\lambda(2b(1+z))-1\right].
\]
Since \(0<M_\lambda(c)<1\), \(h(t)>\kappa-2q>0\). If \(\lambda\ge1\), the tilted mean is strictly above \(1/2\) for every \(c>0\). If \(0<\lambda<1\), strict monotonicity of \(M_\lambda\) proves the unique positive \(c_\lambda\). For \(t\in(0,\infty)\), the argument \(c(t)=2b(1+e^{-\mu t})\) is strictly decreasing from \(4b\) to \(2b\), traversing a given threshold at most once. The exact sign classification and crossing-time expression follow, including the boundary cases.

**4. Sharp large-lag asymptotics.** Set \(z=e^{-\mu t}\). Taylor expansion of the analytic tilted mean at \(2b\) gives
\[
 2M_\lambda(2b+2bz)-1=
 [2M_\lambda(2b)-1]+4bV_\lambda(2b)z+O(z^2).
\]
Multiplication by \(qz\) establishes both the generic leading \(e^{-\mu t}\) correction and the strictly positive \(e^{-2\mu t}\) coefficient at the cancellation surface \(b=c_\lambda/2\). Setting \(z=0\) in the positive exact covariance integral yields its amplitude \(A\).

**5. Short-lag normalization.** The stationary Itô equation for \(X_t^2\) gives \(\mathbb E[(\kappa+K_t)X_t^2]=D\). As \(\frac{d}{dt}C(t)|_{t=0+}=-\mathbb E[(\kappa+K_0)X_0^2]\), we obtain the independent boundary check \(C'(0+)=-D\). This is also reproduced by differentiating the displayed integral.

## Verification

The standalone reproducibility file `checker.py` evaluates the covariance both from the independent two-interval Gaussian integral over \(u\) and from its tilted-beta closed form, without using the latter to evaluate the former. It also compares the analytical rate with a numerical derivative, checks the endpoint normalization \(C'(0+)=-D\), tests signs on both sides of the unique root, verifies strict positivity of the derivative \(M_\lambda'(c)\) against the tilted variance, and tests the critical second-harmonic coefficient. With 48-digit arithmetic, the checker reports `PASS 96 independent quadrature, derivative, sign, root, and critical asymptotic checks`. These finite diagnostics are corroboration, not an infinite proof; all quantified uniqueness and asymptotic claims follow from Steps 1–4.

For an illustrative, dimensionless admissible parameter set \((\mu,D_K,\kappa,D)=(1,0.6,1.45,1)\), one has \((\lambda,b,q)=(0.5,0.6,0.6)\) and \(\kappa-q=0.85\). The unique root is \(c_{0.5}=1.6920310427012196098\ldots\) and the rate crosses its asymptote once at \(t_*=0.89153502635300631235\ldots\). The positive covariance starts at \(C(0)=1.0696162071319520830\ldots\). These decimals are approximate; the exact theorem is the integral and sign classification above.

## Relationship to prior work

Cocconi, Alston, Romano and Bertrand (2024) introduced and studied this continuous-fluctuating-stiffness model. Their Section 4.1, especially Eqs. (30)–(34), establishes the **stationary variance** and its finite-moment threshold. The present covariance reduces to that formula at zero lag, but the crucial covariance between stiffness integrals over adjacent past and future intervals is not part of the single-time variance computation. The exact positive-lag autocovariance, its exponential-tilt rate criterion, unique rate reversal, and critical second harmonic are the assessed additions.

Alston, Cocconi and Bertrand (2022) analyzed entropy production for fluctuating potentials, including continuous stiffness dynamics. Cocconi, Alston and Bertrand (2023), Appendix B, derived an ordinary OU position correlator in a special decoupled constant-stiffness regime (Eqs. (B8)–(B9)), and a fluctuating-stiffness **one-time variance** (Eqs. (B13)–(B20)); neither formula gives the present stationary positive-lag OU-squared covariance or its crossover phase diagram. Gupta and Klapp (2025) analyze single-time moments and thermodynamics in a closely related OU-stiffness model; no stronger two-time phase classification was identified in the inspected material. Standard Gaussian exponential identities are known and not claimed as new. Absence of identified coverage in the inspected sources does not establish worldwide priority.

## Limitations

The finite-variance condition \(\kappa>2D_K/\mu^2\) is essential for this covariance statement. The model assumes an independent additive thermal Brownian noise, independent stationary Gaussian stiffness noise, and time-independent coefficients; it does not cover non-Gaussian stiffness, colored additive forcing, or finite-sample estimation errors. The phase classification concerns crossing of the instantaneous logarithmic *rate* with its long-lag limit, not crossing of the covariance itself with a simple exponential, and does not claim monotonicity of the instantaneous rate. The numerical example is illustrative only. General Gaussian filtering/Feynman–Kac literature may contain a stronger equivalent theorem; publication priority requires independent examination.

## References

1. L. Cocconi, H. Alston, J. Romano, T. Bertrand, *The OU-squared process: Characterising dissipative confinement in noisy traps*, arXiv:2405.09460, first public version 2024-05-15. https://arxiv.org/abs/2405.09460
2. H. Alston, L. Cocconi, T. Bertrand, *Non-equilibrium thermodynamics of diffusion in fluctuating potentials*, arXiv:2202.02630 (2022). https://arxiv.org/abs/2202.02630
3. L. Cocconi, H. Alston, T. Bertrand, *Active bound states arising from transiently nonreciprocal pair interactions*, Physical Review Research **5**, 043032 (2023), doi:10.1103/PhysRevResearch.5.043032. https://thibaultbertrand.com/assets/pdf/2023_prresearch_a.pdf
4. D. Gupta, S. H. L. Klapp, *Nonequilibrium fluctuations in a harmonic trap with annealed stochastic stiffness*, arXiv:2507.20915 (2025). https://arxiv.org/abs/2507.20915
