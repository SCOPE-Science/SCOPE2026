# Hermite-node reversal in survival-conditioned Ornstein–Uhlenbeck residence

## Finding

For a one-dimensional Ornstein–Uhlenbeck particle started at its prospective resetting point, absorbed on reaching the trap center, the probability of being above its initial point at time \(t\), **conditional on surviving without a reset**, has a sharp late-time relaxation transition. With
\[
 w=\frac{\kappa a^2}{D}>0,\qquad q=e^{-\kappa t},\qquad u=\sqrt{\frac{w}{1-q^2}},\qquad v=qu,
\]
this conditional probability is, for every \(t>0\),
\[
 F_w(t)=\frac{\Phi(u+v)-\Phi(u-v)}{2\Phi(v)-1},
\]
where \(\Phi\) is the standard normal distribution function. Its quasi-stationary limit is \(e^{-w/2}\), and the following expansion holds for every fixed \(w>0\):
\[
 \frac{F_w(t)}{e^{-w/2}}=1+\frac{w(w-3)}{6}e^{-2\kappa t}
 +\frac{w(3w^3-38w^2+165w-180)}{360}e^{-4\kappa t}
 +O_w(e^{-6\kappa t}).
\]
Consequently, for \(0<w<3\) the probability approaches its quasi-stationary limit strictly **from below** and is eventually strictly increasing. For \(w>3\) it approaches strictly **from above** and is eventually strictly decreasing. Precisely at \(w=3\), the ordinarily leading correction vanishes, while
\[
 F_3(t)=e^{-3/2}\left(1+\frac9{20}e^{-4\kappa t}+O(e^{-6\kappa t})\right),
\]
so the eventual decrease is accelerated from rate \(2\kappa\) to rate \(4\kappa\). Additionally,
\[
 F_w(t)=\frac12-\frac{\kappa a}{2\sqrt{\pi D}}\sqrt t+O(t)
 \quad(t\downarrow0).
\]
Thus at least one genuine strict interior local minimum exists for every \(0<w<3\). Uniqueness of the minimum is not asserted.

## Assumptions and scope

Fix \(\kappa>0\), \(D>0\), \(a>0\), and any independent Poisson reset rate \(r>0\). A single excursion starts at \(X_0=a\) and evolves according to the Itô equation
\[
 dX_t=-\kappa X_t\,dt+\sqrt{2D}\,dW_t.
\]
Let \(T_0=\inf\{t\ge0:X_t=0\}\) be its absorption time. Let \(R\) be the time of the next independent Poisson reset. The observable is
\[
 F_w(t)=\mathbb P_a(X_t>a\mid T_0>t,\ R>t).
\]
The event of not resetting contributes the same factor \(e^{-rt}\) to numerator and denominator. Thus \(F_w\) is independent of \(r\), but it is a physically meaningful observable of reset-free ages selected among nonabsorbed resetting excursions. It is **not** the occupation probability of the full repeatedly reset process without this conditioning and is **not** the integrated residence time before ultimate absorption.

The primary classification is MSC2020 82C31 (stochastic Langevin methods in time-dependent statistical mechanics). The publication motivating the observable is Dubey and Pal (2023), first publicly available 2023-04-11.

## Proof

**1. Killed transition kernel.** Write
\[
 m_t=ae^{-\kappa t},\qquad \sigma_t^2=\frac{D}{\kappa}(1-e^{-2\kappa t}),\qquad
 g_t(y;m)=\frac{\exp[-(y-m)^2/(2\sigma_t^2)]}{\sqrt{2\pi\sigma_t^2}}.
\]
Because both the drift \(-\kappa x\) and constant diffusivity are invariant under simultaneous reflection of initial and final positions, the absorbing half-line transition density at \(y>0\) is given exactly by the method of images:
\[
 p^+(t,a,y)=g_t(y;m_t)-g_t(y;-m_t).
\]
It satisfies the forward Fokker–Planck equation in \(y>0\), the zero boundary value at \(y=0\), the point-mass initial condition at \(a\), and subprobability normalization. Therefore it is the killed OU kernel. Its total mass is
\[
 S(t)=\int_0^\infty p^+(t,a,y)\,dy=2\Phi(m_t/\sigma_t)-1=2\Phi(v)-1>0.
\]
Integrating over \(y>a\) gives \(\Phi((a+m_t)/\sigma_t)-\Phi((a-m_t)/\sigma_t)\), proving the exact closed form. Independent resetting cancels in the conditional ratio.

**2. Late-time limit and coefficients.** Put \(q=e^{-\kappa t}\), \(u=a/\sigma_t\), \(v=m_t/\sigma_t=qu\). With \(\phi\) the standard normal density, a change of variables gives
\[
 F_w(t)=e^{-u^2/2}\,
 \frac{\int_{-v}^v e^{-z^2/2}\cosh(uz)\,dz}
 {\int_{-v}^v e^{-z^2/2}\,dz}.
\]
For each fixed \(w>0\), both numerator and denominator after removing their common \(2v\) are analytic in \(q^2\) near zero, since \(u^2=w/(1-q^2)\) and \(v^2=wq^2/(1-q^2)\). The finite Gaussian-window moments satisfy
\[
 \frac{\int_{-v}^v z^2 e^{-z^2/2}\,dz}{\int_{-v}^v e^{-z^2/2}\,dz}
 =\frac{v^2}{3}-\frac{2v^4}{45}+O(v^6),
 \qquad
 \frac{\int_{-v}^v z^4 e^{-z^2/2}\,dz}{\int_{-v}^v e^{-z^2/2}\,dz}
 =\frac{v^4}{5}+O(v^6).
\]
Expanding \(\cosh(uz)\) to fourth order and \(e^{-u^2/2}\) to order \(q^4\) produces exactly
\[
 c_2(w)=\frac{w(w-3)}6,
 \qquad c_4(w)=\frac{w(3w^3-38w^2+165w-180)}{360}.
\]
The constant term is \(e^{-w/2}\), which also follows from the quasi-stationary Rayleigh density \((\kappa/D)y\exp[-\kappa y^2/(2D)]\) on \(y>0\). At the single positive zero \(w=3\) of \(c_2\), direct evaluation yields \(c_4(3)=9/20>0\). Since the expansion is analytic in \(q^2\), it can be differentiated termwise at sufficiently large \(t\); the sign of the first nonzero coefficient gives the asserted eventual approach direction and monotonicity. The threshold concerns fixed \(w\): uniformity across a parameter interval containing \(3\) is not claimed.

**3. Short-time behavior and compulsory turning.** For any fixed \(a>0\), reflection effects are exponentially small as \(t\downarrow0\), because absorption requires traversing distance \(a\). Meanwhile \(m_t=a-\kappa at+O(t^2)\) and \(\sigma_t=\sqrt{2Dt}(1+O(t))\). Hence
\[
 F_w(t)=\mathbb P\bigl(N(m_t,\sigma_t^2)>a\bigr)+O(e^{-c/t})
 =\frac12-\frac{\kappa a}{2\sqrt{\pi D}}\sqrt t+O(t)
\]
for a positive constant \(c\) depending on the fixed parameters. Thus \(F_w\) initially decreases. When \(0<w<3\), the late-time expansion makes it eventually strictly increase and approach its limit from below; continuity and analyticity on \(t>0\) imply that the function must attain an interior strict local minimum. Nonconstant analyticity excludes a flat interval of minima. This does not prove that no other extrema exist.

## Verification

The companion `checker.py` verifies the exact \(q^2\) and \(q^4\) coefficients symbolically by finite-window Gaussian moment expansion and rechecks the critical value \(9/20\). It independently integrates the absorbing method-of-images kernel and compares the result with the closed normal-CDF ratio using high-precision arithmetic. Numerical samples at multiple dimensionless initial distances verify the short- and long-time asymptotics and the asserted eventual signs. A successful local replay produced `PASS 56 independent symbolic/numerical assertions`. Run with `python checker.py`, using installed `sympy` and `mpmath`. These finite checks are supplementary; the infinite parameter range and asymptotic statements follow from the analytic proof above.

## Relationship to prior work

Dubey and Pal, *First-passage functionals for Ornstein Uhlenbeck process with stochastic resetting* (arXiv:2304.05226v1, first posted 2023-04-11), study precisely the absorbing harmonic setting and the **integrated residence time above the reset point**, including its mean and dependence on resetting. Their Sections 2, 4, and 5 were examined; they do not state a classification of the **time-resolved survival-conditioned exceedance probability** or cancellation of its first relaxation mode.

Kishore and Kundu, *Local time of an Ornstein-Uhlenbeck particle* (arXiv:2010.06262, 2020), develop a spectral Hermite framework and examine local-time moments conditioned on survival, including absorbing boundaries. Their spectral theory provides compatible background and could in principle be specialized to one-time conditional occupancy, but its examined survival-conditioned local-time section does not give the \(w=3\) exceedance sign classification or accelerated \(4\kappa\) relaxation. Thus general spectral or killed-kernel formulas are not represented as original here; the precise threshold, time-resolved statement, and forced turning are the assessed contribution.

General quasi-stationary diffusion theory supplies existence and interpretation of the limiting conditioned law, not this location-specific second-mode cancellation by itself. The image kernel is standard and explicitly acknowledged.

## Limitations

The theorem concerns a single reset-free killed excursion **conditioned on both survival and absence of a reset**. It does not classify the unconditional occupation of the repeatedly reset process or optimize the resetting rate. The interior minimum is proved to exist for \(0<w<3\), but its uniqueness and the global monotonicity for \(w\ge3\) are not proved. Remainders are for fixed \(w\), not uniform in unbounded parameter ranges. No publication-priority or independent scientific certification is asserted. Standard method-of-images and Hermite background could make equivalent results derivable from older general formulas; a specific equivalent classification was not identified in the examined primary texts.

## References

1. A. Dubey and A. Pal, *First-passage functionals for Ornstein Uhlenbeck process with stochastic resetting*, arXiv:2304.05226v1, 2023-04-11. https://arxiv.org/html/2304.05226v1
2. G. Kishore and A. Kundu, *Local time of an Ornstein-Uhlenbeck particle*, arXiv:2010.06262, 2020-10-13. https://arxiv.org/abs/2010.06262
3. M. Kolb and D. Steinsaltz, *Quasilimiting behavior for one-dimensional diffusions with killing*, arXiv:1004.5044, 2010. https://arxiv.org/abs/1004.5044 (general quasi-stationary background; no claim of a full-text novelty exclusion)
