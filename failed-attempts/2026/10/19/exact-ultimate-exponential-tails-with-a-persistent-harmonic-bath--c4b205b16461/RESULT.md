# Exact ultimate exponential tails with a persistent harmonic bath

## Finding

Consider two coupled Brownian coordinates with the first coordinate instantaneously reset to zero by an independent Poisson clock while the second coordinate is never reset. For **every fixed strictly positive choice** of the five dynamical parameters, the stationary tracer is exponentially distributed on the **logarithmic far-tail scale**. Its exact decay exponent is

\[
\kappa=\sqrt{\frac{r(a+b)^2}{b^2D_x+a^2D_y}}.
\]

More precisely, the stationary law satisfies

\[
\mathbb E[e^{\theta X}]<\infty\quad\Longleftrightarrow\quad |\theta|<\kappa,
\qquad
\lim_{z\to\infty}\frac{1}{z}\log\mathbb P(X>z)
=\lim_{z\to\infty}\frac{1}{z}\log\mathbb P(X<-z)=-\kappa.
\]

In the dimensionless viscoelastic model of Santra and Das, this gives the finite-bath-memory exponent \(\kappa=\sqrt{r(1+\gamma)}\) for every fixed \(0<\gamma<\infty\). The result concerns the limit of large position **at fixed finite memory**, not the large-memory approximation taken first in that paper.

## Assumptions and scope

Fix \(a,b,D_x,D_y,r>0\). Between resets let

\[
\begin{aligned}
dX_t&=-a(X_t-Y_t)\,dt+\sqrt{2D_x}\,dW_t,\\
dY_t&=b(X_t-Y_t)\,dt+\sqrt{2D_y}\,dB_t,
\end{aligned}
\]

where the two Brownian motions and an independent homogeneous Poisson process of intensity \(r\) are mutually independent. At each Poisson event apply \((X,Y)\mapsto(0,Y)\), with no direct reset of the bath. Both coordinates range over the real line and the process is understood at its unique invariant probability law. Write

\[
\lambda=a+b,\qquad D_{\mathrm c}=\frac{b^2D_x+a^2D_y}{\lambda^2}>0.
\]

The theorem is about the one-time stationary marginal of \(X\) and its moment-generating function and tail *logarithmic exponents*. It does not claim an exact density, an exponential-prefactor limit, or uniformity as parameters approach zero or infinity.

## Proof

**1. Free excursion at a specified bath position.** The drift matrix and long-time projection are

\[
A=\begin{pmatrix}-a&a\\b&-b\end{pmatrix},\qquad
P=\lambda^{-1}\begin{pmatrix}b&a\\b&a\end{pmatrix},\qquad
e^{At}=P+e^{-\lambda t}(I-P).
\]

For an excursion of duration \(t\geq0\) begun at \((X_0,Y_0)=(0,y)\), put \(q=e^{-\lambda t}\). Linearity and independence of fresh Brownian increments give

\[
X_t=\alpha(t)y+Z_x(t),\qquad
Y_t=\beta(t)y+Z_y(t),\qquad
\alpha(t)=\frac{a}{\lambda}(1-q),\quad
\beta(t)=\frac{a+bq}{\lambda}.
\]

The centered jointly Gaussian noises \((Z_x,Z_y)\) are independent of \(y\). Direct integration of \(2e^{As}\operatorname{diag}(D_x,D_y)e^{A^\mathsf{T}s}\) yields

\[
\begin{aligned}
V_x(t):=\operatorname{Var}Z_x(t)
&=2D_{\mathrm c}t
+\frac{4a(bD_x-aD_y)}{\lambda^3}(1-q)
+\frac{a^2(D_x+D_y)}{\lambda^3}(1-q^2),\\
V_y(t):=\operatorname{Var}Z_y(t)
&=2D_{\mathrm c}t
+\frac{4b(aD_y-bD_x)}{\lambda^3}(1-q)
+\frac{b^2(D_x+D_y)}{\lambda^3}(1-q^2).
\end{aligned}
\]

In particular there is a parameter-dependent constant \(C<\infty\) such that \(|V_x(t)-2D_{\mathrm c}t|\leq C\) and \(|V_y(t)-2D_{\mathrm c}t|\leq C\) for every \(t\geq0\). For \(t>0\), \(0<\beta(t)<1\), and \(0\leq\alpha(t)<a/\lambda<1\).

**2. Existence of a stationary bath and its exponential moments.** Let \(T_1,T_2,\ldots\) be independent \(\operatorname{Exp}(r)\) excursion lengths. Bath positions immediately after successive reset events obey the affine random recursion

\[
Q_{j+1}=\beta(T_{j+1})Q_j+\eta_{j+1},
\]

where, conditionally on \(T_{j+1}=t\), the independent new innovation \(\eta_{j+1}\) is \(N(0,V_y(t))\). Because \(\mathbb E\beta(T)^2<1\) and \(\mathbb E V_y(T)<\infty\), iterated contractions establish a unique finite-second-moment invariant bath law, centered and symmetric. Conditional on the excursion lengths, this law is Gaussian with a nonnegative random variance \(H\), given by the almost surely convergent random series whose distribution solves

\[
H\ \stackrel{d}{=}\ V_y(T)+\beta(T)^2H',
\]

with \(H'\) an independent copy and \(T\) independent of it. In particular \(Q\mid H\sim N(0,H)\).

For any \(0<c<r/(2D_{\mathrm c})\), the variance bound in step 1 gives \(\mathbb E e^{cV_y(T)}<\infty\). Define

\[
K_c(w)=\mathbb E\exp\!\left(cV_y(T)+c\beta(T)^2w\right),\quad w\geq0.
\]

Dominated convergence and \(\beta(T)<1\) almost surely imply

\[
e^{-cw}K_c(w)
=\mathbb E\!\left[e^{cV_y(T)-c(1-\beta(T)^2)w}\right]
\longrightarrow0\qquad(w\to\infty).
\]

Since \(K_c\) is increasing and finite at every finite \(w\), there is \(R<\infty\) and \(M<\infty\) with \(K_c(w)\leq\frac12e^{cw}+M\) for all \(w\geq0\). Starting the variance recurrence at zero gives \(\sup_j\mathbb E e^{cH_j}<\infty\); the convergent-series representation and Fatou's lemma imply \(\mathbb E e^{cH}<\infty\). Therefore

\[
\mathbb E e^{sQ}=\mathbb E e^{s^2H/2}<\infty
\quad\text{whenever}\quad |s|<\sqrt{r/D_{\mathrm c}}.
\]

This also constructs the unique invariant joint law by placing an independent exponentially distributed age after an invariant embedded reset state. Uniqueness follows from contraction of the reset-time bath chain and independence of the Poisson clock.

**3. Exact moment-generating-function boundary.** In stationarity the backward time \(T\) since the last Poisson event is \(\operatorname{Exp}(r)\), independent of its bath coordinate \(Q\); the post-reset Brownian increments are fresh. Consequently, for any real \(\theta\) with the expectation interpreted in \([0,\infty]\),

\[
\mathbb E e^{\theta X}
=\int_0^\infty re^{-rt+\theta^2V_x(t)/2}
\mathbb E e^{\theta\alpha(t)Q}\,dt.
\]

If \(|\theta|<\sqrt{r/D_{\mathrm c}}\), then \(|\theta\alpha(t)|<\sqrt{r/D_{\mathrm c}}\) uniformly, and the expectation involving \(Q\) is bounded by a fixed finite constant. The integral is bounded by a constant multiple of

\[
\int_0^\infty e^{-(r-\theta^2D_{\mathrm c})t}\,dt<\infty.
\]

Conversely, since \(Q\) is centered, Jensen's inequality gives \(\mathbb E e^{\theta\alpha(t)Q}\geq1\). The bounded correction to \(V_x(t)\) means that the integral diverges whenever \(\theta^2D_{\mathrm c}\geq r\), **including equality**. Thus the moment-generating function has exactly the claimed open domain.

**4. Matching two-sided logarithmic tail bounds.** For any \(0<\theta<\kappa\), Markov's inequality and step 3 show

\[
\limsup_{z\to\infty}z^{-1}\log\mathbb P(X>z)\leq-\theta.
\]

Letting \(\theta\uparrow\kappa\) gives the upper bound. For a matching lower bound, choose any \(K>0\) with \(\mathbb P(|Q|\leq K)>0\). On the independent event \(T\in[uz,uz+1]\), \(|Q|\leq K\), the Gaussian conditional mean \(\alpha(T)Q\) remains bounded and its variance is \(2D_{\mathrm c}uz+O(1)\), uniformly as \(z\to\infty\). The ordinary Gaussian tail asymptotic gives, for each fixed \(u>0\),

\[
\liminf_{z\to\infty}z^{-1}\log\mathbb P(X>z)
\geq-ru-\frac{1}{4D_{\mathrm c}u}.
\]

Minimizing the right-hand cost over \(u>0\) yields \(u=(2\sqrt{rD_{\mathrm c}})^{-1}\) and cost \(\sqrt{r/D_{\mathrm c}}\). Reflection symmetry of the invariant Gaussian-mixture law gives the identical left-tail limit.

For the source's dimensionless specialization \(a=D_x=1\), \(b=D_y=\gamma^{-1}\), one computes \(D_{\mathrm c}=(1+\gamma)^{-1}\), proving the stated \(\sqrt{r(1+\gamma)}\) exponent for each finite positive \(\gamma\).

## Verification

The standalone `verify.py` checks the free Gaussian variance formulas against independent numerical quadrature of the matrix exponential for six positive parameter sets at four durations each, and checks the stationary second-moment formula independently against the infinitesimal generator. It also verifies the tail saddle constant. Run `python verify.py` with NumPy and SciPy installed. All six test cases passed. These finite tests corroborate the formulas; steps 1–4, not finite enumeration, prove the claimed all-parameter theorem.

As a check against the source model, at \(a=b=D_x=D_y=r=1\) the exact stationary tracer variance equals \(3/2\). The embedded reset-time bath variance is \(9/4\). The model's three stationary second-moment generator equations reproduce the former independently.

## Relationship to prior work

Santra and Das [1] formulate precisely the retained-bath two-coordinate model and prove transient moment relations and a Gaussian-profile **strong-memory limit** for the stationary distribution (their section III, equations (14), (28), and (29)). Those calculations do not give the ultimate \(z\to\infty\) logarithmic tail at an arbitrary fixed finite memory. The present result singles out the noncommutation risk between a memory limit and a spatial far-tail limit; it does **not** contradict the Gaussian-profile approximation in its stated asymptotic regime.

Goswami [2] treats harmonically coupled tracer–bath particles, presents a last-renewal propagator and stationary density integral (equations (5) and (32)), and recovers an exponential profile under a strong-coupling approximation (section III and Appendix A). This is the most pertinent competing framework. Its renewal calculation initializes the bath from a prescribed Gaussian distribution at each last-renewal calculation; for the physically bath-retained process it does not establish the invariant bath-at-reset law. In particular the finite-coupling stationary second moment from the renewal expression differs from the exact retained-bath generator identity (already at the unit-rate example). The present theorem establishes the **exact finite-coupling tail boundary** without assuming a renewed bath. Goswami's strong-coupling exponential profile can have the same collective-diffusion exponent in that limiting regime, so novelty is not claimed for the effective diffusion exponent *as a heuristic or in the strong-coupling limit*.

Tal-Friedman, Roichman, and Reuveni [3] obtain a Laplace-series stationary law for a Brownian **single-coordinate proportional reset** \(X\mapsto cX\). This differs from fully resetting the tracer while leaving a distinct coupled bath coordinate continuous; its factorization does not yield the present random-variance bath perpetuity.

## Limitations

Only independent Gaussian white noises, strictly positive finite couplings and diffusivities, a single retained harmonic bath mode, instantaneous probe-only Poisson resetting, and the one-time stationary marginal are covered. A density asymptotic with a prefactor, moderate-deviation crossover at large \(\gamma\), multiple bath modes, non-Poisson schedules, resetting return-time protocols, and uniformity at singular parameter limits are **not proved**. Residual originality risk remains from implicit consequences of more general Markov-renewal or Gaussian-perpetuity tail theorems and from unindexed publications.

## References

[1] I. Santra and D. Das, *Resetting in a viscoelastic bath: the bath remembers*, arXiv:2603.17027v1 (first public 17 March 2026), https://arxiv.org/html/2603.17027v1 ; *New Journal of Physics* **28** (2026), 074601.

[2] K. Goswami, *Stochastic resetting in a nonequilibrium environment*, arXiv:2412.19564v1 (first public 27 December 2024), https://arxiv.org/html/2412.19564v1 .

[3] O. Tal-Friedman, Y. Roichman, and S. Reuveni, *Diffusion with Partial Resetting*, arXiv:2205.03363v2 (2022), https://arxiv.org/html/2205.03363v2 .
