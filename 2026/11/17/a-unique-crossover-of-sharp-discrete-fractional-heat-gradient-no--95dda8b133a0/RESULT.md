# A unique crossover of sharp discrete fractional-heat gradient norms

## Finding

Let \(L\) be the nearest-neighbor Laplacian on the integer lattice, and let \(D\) be the forward difference. For every fractional order \(0<s\leq1\) and every time \(t>0\), the **exact norm for smoothing arbitrary bounded initial data** is

\[
\mathcal N_s(t):=\|D e^{-tL^s}\|_{\ell^\infty(\mathbb Z)\to\ell^\infty(\mathbb Z)}
=\frac{2}{\pi}\int_0^\pi
\exp\!\bigl[-t(4\sin^2(\theta/2))^s\bigr] \,d\theta.
\]

The same unit-norm step function attains this bound for all orders and all positive times. **For every pair \(0<a<b\leq1\), there is exactly one positive time \(\tau_{a,b}\)** for which \(\mathcal N_a(\tau_{a,b})=\mathcal N_b(\tau_{a,b})\); the crossing is simple, and

\[
\mathcal N_a(t)>\mathcal N_b(t)\quad(0<t<\tau_{a,b}),
\qquad
\mathcal N_a(t)<\mathcal N_b(t)\quad(t>\tau_{a,b}).
\]

Hence no fractional order gives a uniformly stronger rough-input gradient smoothing bound than another at every positive time. The exact endpoint and time asymptotics are

\[
\mathcal N_1(t)=2e^{-2t}I_0(2t),\qquad
\mathcal N_s(t)=2-2m(s)t+O_s(t^2)\ (t\downarrow0),
\]
\[
m(s)=\frac{4^s\Gamma(s+1/2)}{\sqrt\pi\,\Gamma(s+1)},\qquad
\mathcal N_s(t)\sim\frac{\Gamma(1/(2s))}{\pi s}\,t^{-1/(2s)}\ (t\to\infty).
\]

The moment \(m(s)\) is strictly increasing on \((0,1]\).

## Assumptions and scope

Sequences are real and bounded on \(\mathbb Z\). For \(f\in\ell^\infty(\mathbb Z)\), define
\[
(Lf)(j)=2f(j)-f(j-1)-f(j+1),\qquad (Df)(j)=f(j+1)-f(j).
\]
The semigroup \(S_s(t)=e^{-tL^s}\) is the bounded convolution extension of the spectral multiplier \(\exp[-t(4\sin^2(\theta/2))^s]\). Its kernel is
\[
p_s(t,k)=\frac1\pi\int_0^\pi
\exp[-t(4\sin^2(\theta/2))^s]\cos(k\theta)\,d\theta,
\qquad k\in\mathbb Z.
\]
The operator norm is the supremum of \(\|DS_s(t)f\|_\infty\) over \(\|f\|_\infty\leq1\). The proof also works for complex bounded sequences. No finite lattice, boundary, normalization of the graph Laplacian by vertex degree, or simultaneous scaling of time with the order is implicit.

## Proof

**1. Strict unimodality.** For the ordinary lattice heat kernel \(p_1(u,k)\), symmetry and the discrete heat equation give, with \(d_j(u)=p_1(u,j)-p_1(u,j+1)\) for \(j\geq0\),
\[
d'_0=-3d_0+d_1,\qquad
 d'_j=d_{j-1}-2d_j+d_{j+1}\quad(j\geq1),
\]
with initial conditions \(d_0(0)=1\) and \(d_j(0)=0\) for \(j\geq1\). Adding three times the identity to this bounded tridiagonal generator leaves a matrix with nonnegative entries and positive paths from zero to every \(j\). The exponential power series therefore shows \(d_j(u)>0\) for all \(u>0\) and all \(j\geq0\). This also gives the classical formula \(p_1(u,k)=e^{-2u}I_{|k|}(2u)\).

For \(0<s<1\), the function \(\lambda\mapsto e^{-t\lambda^s}\) is the Laplace transform of a probability measure \(\eta_{s,t}\) concentrated on \((0,\infty)\) (positive-stable Bochner subordination). Thus
\[
p_s(t,k)=\int_0^\infty p_1(u,k)\,\eta_{s,t}(du).
\]
It follows that \(p_s(t,k)=p_s(t,-k)>0\), \(\sum_kp_s(t,k)=1\), and \(p_s(t,j)>p_s(t,j+1)\) for every \(j\geq0\). The same properties hold at \(s=1\).

**2. Exact norm, including attainment.** Convolution and the \(\ell^\infty\) duality of an absolutely summable coefficient row give
\[
\|DS_s(t)\|_{\infty\to\infty}
=\sum_{k\in\mathbb Z}|p_s(t,k+1)-p_s(t,k)|.
\]
Strict symmetry/unimodality and the vanishing of kernel coefficients at infinity telescope this sum to \(2p_s(t,0)\), which is the displayed spectral integral. The step \(f(j)=-1\) for \(j\leq0\), and \(f(j)=1\) for \(j\geq1\), aligns with the signs of the coefficient row at the edge \((0,1)\). It gives \((DS_s(t)f)(0)=2p_s(t,0)\) for every \(s,t\), proving simultaneous sharpness.

**3. A strictly single-crossing Laplace comparison.** Let \(\Theta\) be uniform on \([0,\pi]\), and put \(U=4\sin^2(\Theta/2)\). Its distribution function is
\[
F_U(u)=\begin{cases}
0,&u\leq0,\\
\tfrac2\pi\arcsin(\sqrt u/2),&0<u<4,\\
1,&u\geq4.
\end{cases}
\]
For \(0<a<b\leq1\), write \(F_a(y)=\mathbb P(U^a\leq y)\), \(F_b(y)=\mathbb P(U^b\leq y)\), and \(g(y)=F_a(y)-F_b(y)\). Since raising a positive number below one to the smaller power makes it larger, while the inequality reverses above one, we have the strict sign pattern
\[
g(y)<0\quad(0<y<1),\qquad
g(y)>0\quad(1<y<4^b),
\]
with \(g=0\) outside \((0,4^b)\), and \(g(1)=0\). Integration by parts, justified because the distributions have bounded support and no atom at zero, yields
\[
p_a(t,0)-p_b(t,0)=t\int_0^\infty e^{-ty}g(y)\,dy.
\]
Introduce \(H(t)=e^t[p_a(t,0)-p_b(t,0)]/t\), extended continuously to \(t=0\). Then
\[
H'(t)=-\int_0^\infty(y-1)e^{-t(y-1)}g(y)\,dy<0
\quad\text{for all }t\geq0,
\]
because \((y-1)g(y)>0\) on both nontrivial intervals.

Furthermore, \(H(0)=\mathbb E U^b-\mathbb E U^a>0\). To establish this strictly, note that \(\mathbb E\log U=0\) by the classical log-sine integral; for \(m(s)=\mathbb E U^s\), differentiation under the integral gives \(m'(0)=0\) and \(m''(s)=\mathbb E[U^s(\log U)^2]>0\) for \(s\geq0\). Thus \(m\) is strictly increasing for \(s>0\). Finally, choose a closed subinterval of \((0,1)\) on which \(g\) is strictly negative. Its contribution to \(H(t)\) tends to \(-\infty\) exponentially, whereas the positive contribution from \(y>1\) is uniformly bounded. Hence \(H(t)\to-\infty\) as \(t\to\infty\). Strict decrease implies precisely one positive simple zero and the asserted orientation; multiplication by \(te^{-t}>0\) preserves all signs and simplicity.

**4. Endpoint asymptotics.** The beta integral for \(\mathbb E U^s\) gives the displayed gamma ratio. Since \(U^s\) is bounded, Taylor expansion of its Laplace transform yields the small-time formula with a quadratic remainder for every fixed order. For \(s=1\), the ordinary heat-kernel Bessel representation gives \(\mathcal N_1(t)\). At large times, use \(4\sin^2(\theta/2)=\theta^2+O(\theta^4)\) near zero, rescale \(\theta=t^{-1/(2s)}z\), and apply dominated convergence using the positive spectral gap away from zero. Since \(\int_0^\infty e^{-z^{2s}}dz=\Gamma(1/(2s))/(2s)\), the stated sharp coefficient follows.

## Verification

The standalone numerical checker `check_fractional_lattice_crossing.py` can be run with Python 3 and SciPy installed. It evaluates the exact Fourier integral, checks the gamma-beta moment identity, compares the classical kernel to the modified Bessel expression, computes consecutive Fourier coefficients, independently verifies the distribution-function Laplace identity, and locates four sample crossovers using root bracketing. Its output ends with `ALL_FRACTIONAL_LATTICE_CROSSING_CHECKS_PASS`.

For example, the crossing for \((a,b)=(1/2,1)\) is approximately \(1.351743246075\), while for \((a,b)=(1/4,1/2)\) it is approximately \(1.418656660926\). These values and finite kernel calculations corroborate the theorem; none is an exhaustive verification of its universal quantifiers. Positivity, exact sharpness, unique crossing, and asymptotic coefficients are established analytically above.

## Relationship to prior work

The discrete heat kernel and fractional Laplacian are classical: Ciaurri, Gillespie, Roncal, Torrea and Varona (2014 preprint) establish the heat-kernel/Bessel formalism, discrete fractional maximum principle, and related harmonic-analysis operators. Ciaurri, Roncal, Stinga, Torrea and Varona (2016 preprint) analyze fractional discrete diffusion and its nonlocal generator. Abadias and De León-Contreras (2021 preprint) derive discrete semigroup regularity and kernel derivative estimates. Chen and Li (2026 preprint), Proposition 1.2, prove a sharp **rate** \(O_s(t^{-1/(2s)})\) for translated fractional lattice kernels in \(\ell^1\), without an exact one-dimensional norm coefficient or a comparison between any two different fractional orders.

The result here distinguishes the rough-input-to-gradient operator norm from the gradient of a kernel measured in \(\ell^\infty\), from a bounded-input Lipschitz-to-Lipschitz norm, and from norms of the fractional generator itself. Its new content is the simultaneous sharp norm formula with a common extremizer and, centrally, the **unique positive reversal of norm ordering for every two distinct fractional orders**. Existing estimates at a fixed order do not imply this unique-crossing statement. An unnoticed equivalent in older semigroup or Laplace-transform comparison literature cannot be ruled out by database searches alone.

## Limitations

The result is for the one-dimensional infinite nearest-neighbor lattice, graph Laplacian without degree normalization, orders \(0<s\leq1\), the forward one-step gradient, and bounded-input to bounded-gradient norm. It does not establish analogous order crossings in higher dimensions, finite cycles, arbitrary graph generators, other operator norms, or orders above one. The numerical checker does not certify statements over all real orders/times. Originality assessment remains provisional pending independent literature review.

## References

1. Ó. Ciaurri, T. A. Gillespie, L. Roncal, J. L. Torrea and J. L. Varona, *Harmonic Analysis associated with a discrete Laplacian*, original publicly available preprint dated 2014-01-09, arXiv:1401.2091v1; https://arxiv.org/abs/1401.2091 .
2. Ó. Ciaurri, L. Roncal, P. R. Stinga, J. L. Torrea and J. L. Varona, *Nonlocal discrete diffusion equations and the fractional discrete Laplacian, regularity and applications*, original preprint dated 2016-08-31, arXiv:1608.08913v1; https://arxiv.org/abs/1608.08913 .
3. L. Abadias and M. De León-Contreras, *Discrete Hölder spaces, their characterization via semigroups associated to the discrete Laplacian and kernels estimates*, arXiv:2107.06778v1, 2021; https://arxiv.org/abs/2107.06778 .
4. R. Chen and B. Li, *Large-Time Asymptotics for Heat and Fractional Heat Equations on the Lattice and General Finite Subgraphs*, arXiv:2602.16339v1, 2026, particularly Proposition 1.2 and §2.2.1; https://arxiv.org/html/2602.16339v1 .
