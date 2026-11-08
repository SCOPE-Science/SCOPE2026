# Sharp endpoint corrections to the thermal mode-transition curve of a harmonically trapped run-and-tumble particle

## Finding
Consider a one-dimensional stationary run-and-tumble particle with a harmonic restoring force and independent thermal Brownian noise. Its dimensionless position law is the convolution of a symmetric beta density of shape \(a>0\) with a centered Gaussian of variance \(s>0\). The Gaussian convolution and the implicit zero-curvature equation for its mode transition were known previously [1–4]; the contributions here are the global strict geometry of the boundary and two sharp, explicit endpoint corrections.

For every \(0<a<1\), there is a unique threshold \(s_c(a)>0\) separating a strictly bimodal density for \(0<s<s_c(a)\) from a strictly unimodal density for \(s\ge s_c(a)\). The critical curve is smooth and strictly decreasing on \((0,1)\). At the threshold the origin is a quartically flat strict maximum, with normalized fourth derivative
\[
\frac{p_{s_c}^{(4)}(0)}{p_{s_c}(0)}=-\frac{2(1-a)}{s_c(a)^2}<0.
\]
Write \(\lambda_a=1/[2s_c(a)]\). The two endpoint expansions are
\[
s_c(a)=1-\sqrt{2\pi}\,e^{1/2}\operatorname{erf}(1/\sqrt{2})\,a+O(a^2),\qquad a\downarrow0,
\]
and, for \(\epsilon=1-a\downarrow0\) and \(L=\log(1/\epsilon)\),
\[
\boxed{\lambda_a=L+\frac32\log L+\log\!\left(\frac2{\sqrt\pi}\right)+O\!\left(\frac{\log L}{L}\right).}
\]
The explicit logarithmic-logarithmic term and constant refine the previously known first-order \(s_c(a)\sim[2\log(1/(1-a))]^{-1}\). For \(a\ge1\) the stationary density is strictly unimodal for every \(s>0\).

## Assumptions and scope
Let \(\kappa,v,D,\rho>0\), and let \(\sigma_t\in\{-1,+1\}\) flip direction at independent exponential times of rate \(\rho\). Let \(W_t\) be independent standard Brownian motion and let
\[
dX_t=(-\kappa X_t+v\sigma_t)\,dt+\sqrt{2D}\,dW_t.
\]
Use the normalized stationary coordinate \(Z=\kappa X/v\), the flip/trap ratio \(a=\rho/\kappa\), and the dimensionless thermal variance \(s=D\kappa/v^2\). In stationarity,
\[
Z\overset{d}=Y_a+\sqrt{s}\,G,\qquad G\sim N(0,1),\quad
f_a(y)=\frac{\Gamma(a+1/2)}{\sqrt\pi\,\Gamma(a)}(1-y^2)^{a-1}\mathbf1_{|y|<1}.
\]
The independent decomposition follows by separating the stationary stochastic convolution into telegraphic and Brownian drives. All claims concern the full real-line stationary marginal, with no finite-particle, finite-observation, or nonharmonic extension.

Define
\[
J_a(\lambda)=\int_0^1 t^{-1/2}(1-t)^{a-1}e^{-\lambda t}\,dt,\qquad
m_a(\lambda)=-\frac{J'_a(\lambda)}{J_a(\lambda)},\qquad
H_a(\lambda)=-2\lambda J'_a(\lambda)-J_a(\lambda).
\]
The critical parameter \(\lambda_a\) is the unique positive solution of \(H_a(\lambda)=0\), equivalently \(2\lambda m_a(\lambda)=1\). It is equivalently the root of the previously published Gaussian-convolution curvature equation. The theorem makes no claim of discovering that equation.

## Proof
**1. Curvature and a positive-crossing identity.** Differentiating the Gaussian convolution at the origin gives
\[
\operatorname{sign}(p_s''(0))=\operatorname{sign}\bigl(2\lambda m_a(\lambda)-1\bigr),\qquad \lambda=\frac1{2s}.
\]
By the integral representation of the confluent hypergeometric function,
\[
J_a(\lambda)=B(1/2,a)\,{}_1F_1(1/2;a+1/2;-\lambda).
\]
Its differential equation is
\[
\lambda J_a''+(a+1/2+\lambda)J'_a+\tfrac12J_a=0.
\]
Set \(g_a(\lambda)=H_a(\lambda)/J_a(\lambda)=2\lambda m_a(\lambda)-1\). Substitution into the differential equation shows that **at every positive zero**,
\[
g_a'(\lambda)=\frac{1-a}{\lambda}.
\]
For \(0<a<1\), \(g_a(0)=-1\), while a Laplace expansion at infinity gives
\[
J_a(\lambda)=\sqrt\pi\lambda^{-1/2}\left(1+\frac{1-a}{2\lambda}+O_a(\lambda^{-2})\right),\quad
g_a(\lambda)=\frac{1-a}{\lambda}+O_a(\lambda^{-2})>0
\]
for all sufficiently large \(\lambda\). A zero exists; every zero crosses strictly upward, so there can be only one. The implicit-function theorem makes \(\lambda_a\), and therefore \(s_c(a)\), smooth.

**2. Strict decrease of thermal threshold.** For fixed \(\lambda>0\), \(m_a(\lambda)\) is the expectation of \(t\) under the normalized density proportional to \(t^{-1/2}(1-t)^{a-1}e^{-\lambda t}\) on \((0,1)\). Raising \(a\) multiplies this density by the strictly decreasing factor \((1-t)^{\Delta a}\), so the monotone-likelihood-ratio ordering implies \(m_a(\lambda)\) strictly decreases as \(a\) increases. The unique upward zero \(\lambda_a\) therefore strictly increases; hence \(s_c(a)=1/(2\lambda_a)\) strictly decreases.

**3. Exactly two or one modes.** For \(0<a<1\), the un-smoothed symmetric beta density decreases on \((-1,0)\), increases on \((0,1)\), and vanishes off \([-1,1]\) (with integrable edge singularities). It is the \(L^1\)-limit of symmetric bounded-variation profiles whose distributional derivatives have sign sequence \(+,-,+,-\). The Gaussian kernel is strictly totally positive, and its variation-diminishing property implies that convolution of such derivatives has at most three sign changes. Smooth convergence of Gaussian convolutions on compact sets transfers the bound to \(p_s'\). By even symmetry and Gaussian tails, the sign of \(p_s''(0)\) therefore selects between exactly one central maximum and exactly two symmetric off-center maxima. At \(s=s_c(a)\), let \(T=Y_a^2\) under the tilted density proportional to \(e^{-T/(2s)}\). The critical equation gives \(\mathbb E_s T=s\). Differentiating the logarithmic derivative of \(J_a\) shows \(\operatorname{Var}_s(T)=2a s^2\), whence
\[
\frac{p_s^{(4)}(0)}{p_s(0)}=\frac{\mathbb E_s T^2-6s\mathbb E_sT+3s^2}{s^4}=-\frac{2(1-a)}{s^2}<0.
\]
The central stationary point is a strict quartic maximum; the sign-variation bound excludes other modes. When \(a\ge1\), the beta density is unimodal (uniform when \(a=1\)); convolution with a Gaussian is strictly unimodal.

**4. Persistent-end expansion.** As \(a\downarrow0\), the tilted \(T\)-law concentrates at \(1\). A beta-integral expansion, uniform for \(\lambda\) in compact subsets of \((0,\infty)\), yields
\[
m_a(\lambda)=1-ae^\lambda\int_0^1t^{-1/2}e^{-\lambda t}\,dt+O(a^2).
\]
The unique root approaches \(\lambda=1/2\). Writing \(\lambda_a=1/2+aC/2+O(a^2)\), the implicit equation gives
\[
C=e^{1/2}\int_0^1t^{-1/2}e^{-t/2}\,dt
=e^{1/2}\sqrt{2\pi}\operatorname{erf}(1/\sqrt2).
\]
Since \(s_c(a)=1/(2\lambda_a)\), the stated first-order expansion follows.

**5. Critical-end expansion.** Put \(\epsilon=1-a\in(0,1/2)\) and write the unnormalized curvature integral as
\[
H_{1-\epsilon}(\lambda)=\int_0^1(2\lambda t-1)t^{-1/2}(1-t)^{-\epsilon}e^{-\lambda t}\,dt.
\]
For \(\epsilon=0\), integration of the exact derivative \(-2(\sqrt t\,e^{-\lambda t})'\) gives \(H_1(\lambda)=-2e^{-\lambda}\). On \(0\le t\le1/2\), the uniform expansion \((1-t)^{-\epsilon}-1=\epsilon t+O(\epsilon t^2)\) gives a Gaussian-Laplace main contribution
\[
\epsilon\int_0^\infty(2\lambda t-1)t^{1/2}e^{-\lambda t}\,dt
=\epsilon\sqrt\pi\,\lambda^{-3/2}.
\]
The remaining bulk integral is \(O(\epsilon\lambda^{-5/2})\). On \(1/2<t<1\), integrability of \((1-t)^{-\epsilon}\) bounds the remainder by \(O(\epsilon(1+\lambda)e^{-\lambda/2})\). Thus uniformly when \(\epsilon\downarrow0\), \(\lambda\to\infty\),
\[
H_{1-\epsilon}(\lambda)=-2e^{-\lambda}
+\epsilon\sqrt\pi\lambda^{-3/2}
\left(1+O(\lambda^{-1})+O(\lambda^{5/2}e^{-\lambda/2})\right).
\]
For any fixed \(\delta\in(0,1)\), compare the two terms at \(\lambda=(1\pm\delta)L\), with \(L=\log(1/\epsilon)\). The signs are opposite, proving \(\lambda_a/L\to1\) by uniqueness of its root. At that root,
\[
2e^{-\lambda_a}=\epsilon\sqrt\pi\lambda_a^{-3/2}(1+O(\lambda_a^{-1})),
\]
so taking logarithms yields
\[
\lambda_a=L+\frac32\log\lambda_a+\log(2/\sqrt\pi)+O(1/\lambda_a).
\]
Substituting \(\lambda_a\sim L\) into the logarithm and refining once proves
\[
\lambda_a=L+\frac32\log L+\log(2/\sqrt\pi)+O((\log L)/L),
\]
as claimed. The gamma-integral coefficient \(\sqrt\pi\) fixes the constant; replacing the curvature equation by only its first-order logarithmic limit would lose both corrections.

## Verification
The standalone `check_phase.py` evaluates independent hypergeometric moment ratios and the implicit root at multiple shape parameters. It tests root sign brackets, monotonic thermal thresholds, the exact critical-tilt variance identity, the fourth-derivative identity, root transversality, the small-\(a\) correction, and the critical-end logarithmic-logarithmic remainder. With `mpmath` at 55 decimal places, **67** diagnostic assertions pass. These finite diagnostics neither prove global uniqueness nor replace the uniform asymptotic and variation-diminishing arguments above.

Reproduce with `python -m pip install mpmath` and `python check_phase.py` from the directory containing both this file and the checker. The numerical checks use deterministic special-function evaluation and bisection, with no random sampling or outside data.

## Relationship to prior work
The Gaussian convolution and stationary symmetric beta density are established in Garcia-Millan and Pruessner [1] and Frydel [2]. Sabhapandit and Majumdar [3], especially equations (93)–(97) and figure 3, derive the *same* Gaussian-smoothed telegraph problem, its implicit hypergeometric curvature boundary and a qualitative two-phase diagram. Guéneau, Majumdar and Schehr [4], equations (90)–(97), repeat the convolution/curvature formulation and explicitly report the **leading** inverse-logarithmic vanishing of the transition temperature. Sevilla and Meléndez Mora [5] give a further convolution treatment and stationary observables. None of these formulas, qualitative plots or first-order limits is claimed as new. The additional established statements here are smooth strict monotonicity with a unique positive crossing, quartic curvature at the boundary, the explicit first linear correction as persistence becomes extreme, and the \((3/2)\log\log\) plus constant correction near the no-transition endpoint.

The global modality bound uses the classical variation-diminishing property of Gaussian convolution, not a novel total-positivity theorem [6]. The claim concerns a natural scalar physical phase boundary; no higher-dimensional or non-Gaussian noise generalization is asserted.

## Limitations
The model requires positive rates, harmonic confinement, an independent Brownian bath, and symmetric two-state orientation switching. The boundary is a statement about an exact infinite-time stationary density, not finite samples. Leading convolution formulas and the implicit critical equation predate this result. Related unindexed modal-bifurcation or special-function asymptotic results could limit priority; absence from the inspected sources and research search does not certify global novelty. The independent scientific audit has not been performed.

## References
[1] R. Garcia-Millan and G. Pruessner, “Run-and-tumble motion: field theory and entropy production,” arXiv:2012.02900, initially posted 2020-12-04. https://arxiv.org/abs/2012.02900

[2] D. Frydel, “Positing the problem of stationary distributions of active particles as third-order differential equation,” arXiv:2207.08695, 2022. https://arxiv.org/abs/2207.08695

[3] S. Sabhapandit and S. N. Majumdar, “Noninteracting particles in a harmonic trap with a stochastically driven center,” arXiv:2404.02480, initially posted 2024-04-03. https://arxiv.org/abs/2404.02480

[4] M. Guéneau, S. N. Majumdar and G. Schehr, “Exact Stationary State of a \(d\)-dimensional Run-and-Tumble Particle in a Harmonic Potential,” arXiv:2602.08436, 2026. https://arxiv.org/abs/2602.08436

[5] F. J. Sevilla and J. A. Meléndez Mora, “Nonequilibrium statistics of harmonically trapped run-and-tumble particles: An exact convolution approach,” arXiv:2608.21781, 2026. https://arxiv.org/abs/2608.21781

[6] Classical Gaussian-kernel total positivity and variation-diminishing theorem; see S. Karlin, *Total Positivity*, Stanford University Press, 1968.
