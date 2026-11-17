# A unique reset-clock preference reversal in Gaussian endpoint divergence

## Finding
For every strictly positive Gaussian reset width below the harmonic equilibrium width, the symmetric Kullback–Leibler endpoint-divergence rate under periodic versus Poisson reset clocks of the **same mean frequency** has exactly one preference reversal. At high reset frequency the Poisson clock produces a strictly larger endpoint-divergence rate; at low frequency the periodic clock produces a strictly larger rate. At precisely one finite frequency the two rates agree. The result concerns the information-geometric endpoint contribution, not implementation-dependent total dissipation.

Specifically, for any \(a>0\) set
\[
g_a(x)=\frac{a^2(1-e^{-x})^2}{2[1+a(1-e^{-x})]},\qquad x\geq0.
\]
Let \(Z\) be a unit-mean exponential random variable and let
\[
\Delta_a(x)=\mathbb E[g_a(xZ)]-g_a(x).
\]
There is exactly one \(x_c(a)\in(0,\infty)\) satisfying \(\Delta_a(x_c(a))=0\), with \(\Delta_a(x)>0\) for \(x<x_c(a)\) and \(\Delta_a(x)<0\) for \(x>x_c(a)\). Moreover, the best periodic clock gives a strictly greater endpoint-divergence rate than the best Poisson clock after optimizing their frequencies independently. For the finite-width ratio \(q=1/2\) (equivalently \(a=1\)), \(x_c\approx0.42891636051\), so the crossover occurs at \(r/(2\lambda)\approx2.3314568808\).

## Assumptions and scope
Consider the one-dimensional harmonic Ornstein–Uhlenbeck process \(dX_t=-\lambda X_t\,dt+\sqrt{2D}\,dB_t\), with \(\lambda,D>0\). At every independent reset, replace its position by a fresh sample from \(\mathcal N(0,qD/\lambda)\), with \(0<q<1\). Reset times are either deterministic intervals \(1/r\), or independent exponential intervals of mean \(1/r\), with \(r>0\). Resets are idealized as instantaneous, including at frequencies where a physical implementation could incur extra overhead.

The conditional law \(t\) after each reset is centered Gaussian with variance
\[
v(t)=\frac D\lambda\left[q+(1-q)(1-e^{-2\lambda t})\right].
\]
Define the cycle reward as the symmetric endpoint Gaussian KL divergence, in natural-log units, between this conditional law and the reset law. With \(a=(1-q)/q\) and \(x=2\lambda t\), that reward is exactly \(g_a(x)\). Its long-time mean rate follows the elementary renewal-reward law. Define
\[
\mathcal P_a(r)=r g_a(2\lambda/r),\qquad
\mathcal E_a(r)=r\,\mathbb E\bigl[g_a((2\lambda/r)Z)\bigr].
\]
The theorem compares these **rates at the same mean reset frequency**. Any positive constant multiplying both rewards leaves the comparison unchanged.

## Proof
**1. Exactly one inflection of the cycle reward.** Write \(f=1-e^{-x}\), so \(f\in(0,1)\) for \(x>0\). Direct differentiation gives
\[
g_a''(x)=\frac{a^2(1-f)}{2(1+af)^3}\left[2-4f-3af^2-a^2f^3\right].
\]
The bracket is strictly decreasing in \(f\in[0,1]\), is \(2\) at zero, and is negative at one. Hence there is one \(t_0>0\) with \(g_a''(t)>0\) for \(0<t<t_0\), and \(g_a''(t)<0\) for \(t>t_0\). Also \(g_a(0)=g_a'(0)=0\), and \(g_a''\) is integrable.

**2. A strictly ordered comparison kernel.** Because \(g_a(x)=\int_0^\infty g_a''(t)(x-t)_+\,dt\), Fubini's theorem yields
\[
\Delta_a(x)=\int_0^\infty g_a''(t)H_x(t)\,dt,
\qquad H_x(t)=x\left[e^{-t/x}-(1-t/x)_+\right]>0\quad(t>0).
\]
Write \(K(z)=e^{-z}-(1-z)_+\) for \(z>0\), and \(h(z)=zK'(z)/K(z)\) wherever the derivative exists. For \(0<z<1\),
\[
h'(z)=\frac{z^2e^{-z}-(1-e^{-z})^2}{K(z)^2}<0,
\]
using \(2\sinh(z/2)>z\). For \(z>1\), \(h(z)=-z\); the one-sided values at \(z=1\) are \(e-1\) and \(-1\), respectively. Thus \(h\) strictly decreases across its single downward jump. If \(0<x_1<x_2\), then, away from the two possible corners,
\[
\frac{d}{dt}\log\frac{H_{x_2}(t)}{H_{x_1}(t)}
=\frac{h(t/x_2)-h(t/x_1)}{t}>0.
\]
Continuity handles the corners. Therefore the kernel ratio \(H_{x_2}(t)/H_{x_1}(t)\) increases strictly with \(t>0\).

**3. Uniqueness of the preference reversal.** Split the signed integral at \(t_0\):
\[
A(x)=\int_0^{t_0}g_a''(t)H_x(t)\,dt>0,\qquad
B(x)=-\int_{t_0}^\infty g_a''(t)H_x(t)\,dt>0.
\]
Thus \(\Delta_a(x)=A(x)-B(x)\). The strict increase of the kernel ratio just proved, applied to every pair \(u<t_0<v\), gives \(B(x_2)A(x_1)>B(x_1)A(x_2)\) whenever \(x_2>x_1\). Consequently \(B(x)/A(x)\) is strictly increasing. Hence \(\Delta_a\) can change sign at most once, necessarily from positive to negative.

For \(x\downarrow0\), \(g_a(x)=a^2x^2/2+O_a(x^3)\). Since \(\mathbb E[Z^2]=2\), and exponential moments control the Taylor remainder,
\[
\Delta_a(x)=\frac{a^2x^2}{2}+O_a(x^3)>0
\]
for sufficiently small positive \(x\). At the other endpoint put \(g_\infty=a^2/[2(1+a)]\) and \(C_a=\int_0^\infty[g_\infty-g_a(t)]\,dt\), which is strictly positive and finite. Exponential integration and dominated convergence imply
\[
\lim_{x\to\infty}x\Delta_a(x)=-C_a<0.
\]
Continuity now gives existence and, from the strict ratio monotonicity, uniqueness of \(x_c(a)\), including the asserted sign pattern. The claimed comparison of reset **rates** follows because both rates are \(r\) times their respective cycle rewards and \(x=2\lambda/r\) decreases strictly with \(r\).

**4. Independently optimized clocks.** Let \(m_a=\sup_{t>0}g_a(t)/t\). This maximum is finite and strictly positive. It is uniquely attained because
\[
\frac{tg_a'(t)}{g_a(t)}
=\frac{t}{e^t-1}\,
\frac{2+a(1-e^{-t})}{1+a(1-e^{-t})}
\]
is a product of strictly decreasing positive functions, decreases from \(2\) to \(0\), and thus equals \(1\) precisely once. For every random reset duration \(T>0\) with finite mean,
\[
\frac{\mathbb E[g_a(T)]}{\mathbb E[T]}
=\mathbb E\left[\frac{T}{\mathbb E[T]}\frac{g_a(T)}{T}\right]\leq m_a,
\]
with strict inequality for a nondegenerate exponential distribution. The exponential-clock rate is continuous and tends to zero as its mean interval tends to either zero or infinity, so its supremum is attained and remains strictly below \(m_a\). Rescaling by \(2\lambda\) gives the stated optimized periodic-over-Poisson strict inequality. This last general renewal-reward comparison is supporting context, not the originality claim.

## Verification
Run `python3 verify.py` from the directory containing this document. The standard-library-only checker reproduces the analytic second derivative by finite differences; checks the curvature sign-change pattern and strict ordered comparison-kernel inequalities over deterministic grids; finds crossover roots for \(a\in\{0.01,0.1,1,10,100\}\) by numerical quadrature and bisection; and checks both rate orderings for \(a=1\). The recorded run passed 2695 deterministic checks. Computation is supplementary: the theorem for all \(a>0\), all reset rates, and unique sign changes is established by the preceding analytical argument.

For \(a=1\), reduced rate \(r/(2\lambda)=10\) yields reduced periodic and Poisson rates approximately \(0.04134508\) and \(0.06205033\); reduced rate \(1\) yields approximately \(0.12241020\) and \(0.09657359\), respectively.

## Relationship to prior work
Farago (2026), arXiv:2605.28445, derives the harmonic Gaussian endpoint KL functional and analyzes periodic and Poisson clocks in a narrow-reset teleportation approximation; those definitions, renewal averaging, and the associated asymptotics are not new. The present theorem instead retains the exact finite reset width and proves a **unique sign reversal of the difference at matched clock means**; this is not supplied by separately plotting or optimizing the two rates. Prior stochastic-reset thermodynamics includes Mori, Olsen and Krishnamurthy (2023) for stochastic entropy under random reset positions, and Olsen, Gupta, Mori and Krishnamurthy (2024) for the physical work under finite-time resetting. Those objectives and reset implementations differ from the symmetric Gaussian endpoint metric considered here. General variations of renewal-reward inequalities and kernel-ordering methods provide possible broader coverage and should be evaluated before asserting publication priority.

## Limitations
This is a one-dimensional, centered, exactly Gaussian, independent-renewal reset model with \(0<q<1\). Its metric is **only the endpoint symmetric KL divergence**; real reset mechanisms may produce extra entropy or work, particularly when rates approach physical localization timescales. The result does not compare finite-time path-wise total stochastic entropy, correlations between successive reset intervals, or non-Gaussian traps. The crossover is unique for the *equal-mean periodic-versus-exponential comparison*, not a universal uniqueness statement for all clock families. Full independent validation and definitive publication-priority review have not been performed.

## References
1. O. Farago, *The Resetting Heat Engine: A Thermodynamic Cycle of Thermal Expansion and Compression*, first posted 27 May 2026, arXiv:2605.28445v1, https://arxiv.org/abs/2605.28445 (especially Eq. 11 and Eqs. 17–19, plus text on finite-width and implementation effects).
2. F. Mori, K. S. Olsen and S. Krishnamurthy, *Entropy production of resetting processes*, arXiv:2211.15372; Physical Review Research 5, 023103 (2023), https://arxiv.org/abs/2211.15372.
3. K. S. Olsen, D. Gupta, F. Mori and S. Krishnamurthy, *Thermodynamic cost of finite-time stochastic resetting*, arXiv:2310.11267; Physical Review Research 6, 033343 (2024), https://arxiv.org/abs/2310.11267.
