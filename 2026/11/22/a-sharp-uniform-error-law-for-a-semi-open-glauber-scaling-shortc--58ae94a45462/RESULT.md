# A sharp uniform error law for a semi-open Glauber scaling shortcut

## Finding

A proposed error-function shortcut to the finite-size single-time correlation function of the zero-temperature semi-open Glauber–Ising chain has a rigorously controlled, *uniformly sharp* short-time error. In the continuum scaling model specified below, let \(u(t,x)\) be the exact correlation and \(v(t,x)\) the published shortcut. For every length \(N>0\), separation \(0<x<N\), and time \(t>0\),
\[
0<v(t,x)<u(t,x)<1-\frac{x}{N},\qquad
0<u(t,x)-v(t,x)<\frac{\operatorname{erfc}(N/\sqrt{2t})}{\operatorname{erf}(N/\sqrt{2t})}.
\]
The absolute error bound is *asymptotically sharp uniformly in space* as \(t/N^2\to0\):
\[
\sup_{0<x<N}\bigl(u(t,x)-v(t,x)\bigr)
\sim\operatorname{erfc}(N/\sqrt{2t})
\sim\sqrt{\frac{2t}{\pi N^2}}\exp\!\left(-\frac{N^2}{2t}\right).
\]
For example, whenever \(t\le N^2/8\), the absolute error is everywhere smaller than \(\operatorname{erfc}(2)/\operatorname{erf}(2)<0.00470\). This makes the short-time approximation window quantitatively reproducible, independent of the observation separation.

At every fixed interior separation, the sharp late-time discrepancy is instead algebraic,
\[
u(t,x)-v(t,x)=\frac{x(N^2-x^2)}{6Nt}+O_{N,x}(t^{-2}),
\]
although the exact model relaxes exponentially. Accordingly, with \(H(x)=1-x/N\),
\[
\int_0^\infty [H(x)-u(t,x)]\,dt
=\frac{x(N-x)(2N-x)}{3N}<\infty,
\qquad
\int_0^\infty[H(x)-v(t,x)]\,dt=\infty.
\]
The latter divergence concerns extrapolating the shortcut **outside** its short-time approximation regime, not a failure asserted for the regime where the original source recommends using it.

## Assumptions and scope

Take \(N>0\). In the continuum finite-size scaling description of the initially disordered, zero-temperature semi-open chain, let \(u\) be the bounded solution of
\[
\partial_tu=\tfrac12\partial_x^2u\quad(0<x<N),\qquad
u(t,0)=1,\quad u(t,N)=0,\quad u(0,x)=0\ (0<x<N).
\]
Boundary and initial data are incompatible at \((t,x)=(0,0)\), so all pointwise inequalities and limits are explicitly for positive times and interior separations. Set
\[
v(t,x)=1-\frac{\operatorname{erf}(x/\sqrt{2t})}
{\operatorname{erf}(N/\sqrt{2t})}.
\]
Here \(v\) is a short-time scaling approximation rather than a second exact Glauber correlation. The diffusion normalization is \(\partial_t=\frac12\partial_x^2\); formulas require this normalization. No assertion is made about microscopic finite-lattice errors beyond the continuum scaling model.

## Proof

**Exact reference solution.** Subtract the steady harmonic profile \(H(x)=1-x/N\). Standard Dirichlet sine expansion gives the absolutely convergent positive-time representation
\[
u(t,x)=H(x)-\frac2\pi\sum_{k=1}^{\infty}
\frac{\sin(k\pi x/N)}{k}
\exp\left(-\frac{k^2\pi^2t}{2N^2}\right).
\]
Equivalently, if \(B\) is standard Brownian motion started at \(x\), and \(\tau_0,\tau_N\) are its first hitting times of the endpoints, \(u(t,x)=\Pr_x(\tau_0\le t,\tau_0<\tau_N)\). Hence \(0<u(t,x)<H(x)\), and the half-line hitting probability \(\varepsilon_x(t)=\operatorname{erfc}(x/\sqrt{2t})\) bounds \(u\) above.

**Strict comparison and uniform bound.** Write \(s=x/\sqrt{2t}\), \(a=N/\sqrt{2t}\) and \(E=\operatorname{erf}\). Direct differentiation, using that \(E(s)\) alone solves the heat equation on the half-line, yields
\[
\left(\partial_t-\tfrac12\partial_x^2\right)v(t,x)
=-\frac{aE(s)e^{-a^2}}{\sqrt\pi\,tE(a)^2}<0.
\]
Since \(u\) and \(v\) have the same Dirichlet boundary and initial values, the parabolic strong comparison principle gives \(u>v\) in the interior for positive times. The monotone decrease of \(E(z)/z\) for positive \(z\) gives \(0<v<H\). Writing \(\varepsilon_N=\operatorname{erfc}(a)\) and \(\varepsilon_x=\operatorname{erfc}(s)\),
\[
v=\frac{\varepsilon_x-\varepsilon_N}{1-\varepsilon_N},\qquad
0<u-v\le\varepsilon_x-v
=\frac{\varepsilon_N(1-\varepsilon_x)}{1-\varepsilon_N}
<\frac{\varepsilon_N}{1-\varepsilon_N},
\]
which is the stated uniform bound.

**Sharpness of the uniform short-time scale.** Fix any \(x\in(0,N)\). The reflection/strong-Markov estimate for a Brownian trajectory that hits \(N\) before \(0\) gives
\[
0\le \varepsilon_x(t)-u(t,x)
\le\operatorname{erfc}\left(\frac{2N-x}{\sqrt{2t}}\right).
\]
Indeed after the Brownian path reaches \(N\), any subsequent visit to \(0\) is at least an additional distance \(N\); the sum of its independent first-passage times is distributed as the first-passage time across distance \(2N-x\). Consequently
\[
u-v=\frac{\varepsilon_N(1-\varepsilon_x)}{1-\varepsilon_N}
-\bigl(\varepsilon_x-u\bigr)
\sim\varepsilon_N\quad(t\downarrow0),
\]
since both \(\varepsilon_x\to0\) and \(\operatorname{erfc}((2N-x)/\sqrt{2t})=o(\varepsilon_N)\). This fixed-point lower bound and the uniform upper bound sandwich the spatial supremum to the same asymptotic. The final exponential equivalence follows from the classical complementary-error-function tail.

**Late time and integrated effect.** Expanding \(\operatorname{erf}(z)=(2/\sqrt\pi)(z-z^3/3+O(z^5))\) yields
\[
H(x)-v(t,x)=\frac{x(N^2-x^2)}{6Nt}+O_{N,x}(t^{-2}).
\]
The first term of the sine series shows
\[
H(x)-u(t,x)=\frac2\pi\sin(\pi x/N)e^{-\pi^2t/(2N^2)}+O_{N,x}(e^{-2\pi^2t/N^2}),
\]
so subtracting gives the late-time bias. For \(F(x)=\int_0^\infty[H(x)-u(t,x)]\,dt\), integrate the Dirichlet heat equation in time to obtain \(-\tfrac12 F''=H\) and \(F(0)=F(N)=0\). The unique solution is \(F=x(N-x)(2N-x)/(3N)\). The leading positive \(1/t\) tail of \(H-v\) has a logarithmically divergent integral. More precisely, \(\int_{t_0}^T[H(x)-v(t,x)]dt=[x(N^2-x^2)/(6N)]\log T+O_{N,x,t_0}(1)\) for every \(t_0>0\).

## Verification

The standalone `checker.py` evaluates the exact sine series independently against a reflected-image Brownian hitting formula, checks the all-time inequalities and uniform bound over multiple lengths, interior separations and dimensionless times, and verifies the PDE residual, short-/long-time asymptotics and integrated deficit. It passes 401 scalar consistency checks using Python's standard library. These finite checks support the reconstruction but are not the proofs of the continuum all-time and all-space statements.

## Relationship to prior work

Malte Henkel's 2026 semi-open-chain paper establishes the exact continuum correlation as a theta-function/sine-series expression and gives the error-function shortcut as an approximation; those ingredients are not claimed here. The present claim is the **joint rigorous quantitative comparison**: strict sign, globally uniform short-time bound with sharp exponential scale, and the precise crossover to algebraic extrapolation error and its integrated effect. The paper's earlier periodic-chain result has a different boundary geometry. Comparison with related published Glauber resetting results concerns different driving/reset protocols; none was identified as implying the specific semi-open approximation bound. The short-time domain intended by the source is respected and explicitly separated from the late-time warning.

## Limitations

The exact \(N\) refers to the **continuum domain length**, not a claim of uniform microscopic finite-lattice accuracy. The sharp small-time pointwise asymptotic requires a fixed interior \(x\); it is not uniform in \(x\) near the endpoints, although the stated *spatial supremum* asymptotic is sharp. Error-function approximation is not proposed for times comparable to or beyond \(N^2\). The claim is checked against relevant accessible literature, but unindexed prior inequalities cannot be ruled out. No independent validation has been performed.

## References

1. M. Henkel, *Exact solution of the Glauber-Ising model on the finite-length semi-open chain* (2026), arXiv:2606.16848v1, first submitted 2026-06-15. https://arxiv.org/abs/2606.16848 .
2. M. Henkel, *Finite-size scaling in the ageing dynamics of the 1D Glauber-Ising model* (2025), arXiv:2501.05912. https://arxiv.org/abs/2501.05912 .
