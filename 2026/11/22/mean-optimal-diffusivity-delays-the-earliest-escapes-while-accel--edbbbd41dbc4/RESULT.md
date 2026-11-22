# Mean-optimal diffusivity delays the earliest escapes while accelerating the late tail

## Finding

Let \(L,D_0>0\). In an interval \([0,L]\) with reflection at \(0\) and absorption at \(L\), launch a drift-free Itô diffusion at \(0\), with backward generator \(\mathcal L_D f=D(x)f''\). Under the fixed diffusivity budget \(L^{-1}\int_0^L D(x)\,dx=D_0\), compare homogeneous diffusion \(D_h(x)=D_0\) with the *known* mean-optimal profile
\[
D_*(x)=\frac{3D_0}{2}\sqrt{1-\frac{x}{L}}.
\]
Let \(T_*\) and \(T_h\) be their respective first-absorption times. Write \({}_0F_1\) for the confluent hypergeometric limit function and \(j_{-1/3,n}\) for the increasing positive zeros of \(J_{-1/3}\). The following joint distributional result holds:
\[
\mathbb E e^{-sT_*}=\left[{}_0F_1\!\left(;\frac23;\frac{8sL^2}{27D_0}\right)\right]^{-1}
=\prod_{n\ge1}\left(1+\frac{s}{\lambda_n}\right)^{-1},\qquad
\lambda_n=\frac{27D_0}{32L^2}j_{-1/3,n}^2.
\]
Hence \(T_*\) has the law of the almost surely convergent sum of independent exponential times of rates \(\lambda_n\). The means and variances are
\[
(\mathbb ET_*,\operatorname{Var}T_*)=\left(\frac{4L^2}{9D_0},\frac{16L^4}{135D_0^2}\right),\quad
(\mathbb ET_h,\operatorname{Var}T_h)=\left(\frac{L^2}{2D_0},\frac{L^4}{6D_0^2}\right).
\]
Despite these improvements, the mean-optimal profile has *strictly fewer very early completions*:
\[
\lim_{t\downarrow0}t\log\frac{\mathbb P(T_*\le t)}{\mathbb P(T_h\le t)}
=-\frac{5L^2}{108D_0}<0.
\]
In contrast, it has *strictly fewer very late survivors*:
\[
\lim_{t\to\infty}\frac1t\log\frac{\mathbb P(T_*>t)}{\mathbb P(T_h>t)}
=-\frac{D_0}{L^2}\left(\frac{27}{32}j_{-1/3,1}^2-\frac{\pi^2}{4}\right)<0.
\]
The two first-arrival cumulative distributions therefore cross at least once. Both opposing early/late inequalities persist for all sufficiently small positive \(\delta\) under the **smooth, strictly positive, budget-normalized regularization**
\[
D_\delta(x)=C_\delta\sqrt{1-x/L+\delta},\quad
C_\delta=\frac{3D_0}{2((1+\delta)^{3/2}-\delta^{3/2})}.
\]
No uniqueness of a crossing or optimality for quantiles is asserted.

## Assumptions and scope

The process is a one-dimensional diffusion, started at the reflecting endpoint, absorbed at the far endpoint, with the Itô (zero-drift) stochastic prescription, and positive \(L,D_0\). The coefficient \(D_*\) is positive on \([0,L)\), continuous up to \(L\), and vanishes only at the *absorbing* endpoint. The corresponding killed diffusion is defined by its backward equation with Neumann condition at \(0\) and Dirichlet condition at \(L\). The endpoint is accessible because the speed density \(1/D_*\) is integrable there. The regularized coefficients \(D_\delta\) are smooth and uniformly positive for every \(\delta>0\). The independent exponential-sum representation is an equality in distribution, not a pathwise identity.

## Proof

**1. Mean optimizer (credited input, also checked).** The reflecting–absorbing mean solves \(D(x)m''(x)=-1\), \(m'(0)=m(L)=0\), so \(m(0)=\int_0^L(L-x)/D(x)\,dx\). Cauchy–Schwarz and \(\int_0^L D=L D_0\) give \(m(0)\ge(\int_0^L\sqrt{L-x}\,dx)^2/(LD_0)=4L^2/(9D_0)\), with equality precisely for \(D=D_*\). This optimal profile and minimum were established in Menon (2026); the novel claim is the distributional comparison.

**2. Exact transform.** Rescale \(x\) by \(L\) and time by \(L^2/D_0\). With \(y=1-x/L\) and \(A=3D_0/2\), the Laplace transform \(u_s(y)=\mathbb E_{L(1-y)}e^{-sT_*}\) obeys
\[
A\sqrt y\,L^{-2}u_s''(y)=s u_s(y),\qquad u_s(0)=1,\quad u_s'(1)=0.
\]
Set \(z=(4L/3)\sqrt{s/A}\). A basis consists of \(\sqrt y\,I_{-2/3}(zy^{3/4})\) and \(\sqrt y\,I_{2/3}(zy^{3/4})\). Their derivatives at \(y=1\) are respectively \(3zI_{1/3}(z)/4\) and \(3zI_{-1/3}(z)/4\). Enforcing reflection and \(u_s(0)=1\), and using
\[
I_{-2/3}(z)I_{-1/3}(z)-I_{2/3}(z)I_{1/3}(z)=\frac{\sqrt3}{\pi z},
\]
yields
\[
u_s(1)=\frac{(z/2)^{-1/3}}{\Gamma(2/3)I_{-1/3}(z)}
=\left[{}_0F_1(;2/3;z^2/4)\right]^{-1}.
\]
Since \(z^2/4=8sL^2/(27D_0)\), this is the stated transform.

**3. Product and moments.** The classical Bessel product for order \(-1/3>-1\) gives
\[
{}_0F_1(;2/3;z^2/4)=\prod_{n\ge1}\left(1+\frac{z^2}{j_{-1/3,n}^2}\right).
\]
As \(j_{-1/3,n}\sim\pi n\), the sum of reciprocal rates converges, proving the independent-exponential representation. Expanding \({}_0F_1(;2/3;v)=1+(3/2)v+(9/20)v^2+O(v^3)\) and differentiating the reciprocal transform gives \(\mathbb ET_*=4L^2/(9D_0)\), \(\mathbb ET_*^2=128L^4/(405D_0^2)\), and the announced variance. The homogeneous transform is \(1/\cosh(L\sqrt{s/D_0})\), yielding its displayed moments.

**4. Earliest arrivals.** The large-positive-argument modified-Bessel asymptotic gives
\[
\log\mathbb E e^{-sT_*}=-\frac{4L}{3}\sqrt{\frac{2s}{3D_0}}+O(\log s),\qquad
\log\mathbb E e^{-sT_h}=-L\sqrt{\frac{s}{D_0}}+O(1).
\]
For a nonnegative random time whose log-Laplace transform is \(-a\sqrt s+O(\log s)\), exponential tilting (or the exponential Tauberian theorem) yields \(\lim_{t\downarrow0}t\log\mathbb P(T\le t)=-a^2/4\). To see the lower bound without assuming a density formula, tilt by \(e^{-sT}\); its mean is \(a/(2\sqrt s)+o(s^{-1/2})\) and relative variance tends to zero. Choose its mean just below \(t\), lower-bound the un-tilted mass on a narrow interval below \(t\), then shrink the interval; the Chernoff bound gives the matching upper bound. Here the two constants are \(-8L^2/(27D_0)\) and \(-L^2/(4D_0)\), whose difference is \(-5L^2/(108D_0)\).

**5. Late survivors and a rigorous spectral inequality.** The killed Sturm–Liouville eigenfunction regular at \(y=0\) has the form \(\sqrt y\,J_{2/3}(j y^{3/4})\); reflection at \(y=1\) gives \(J_{-1/3}(j)=0\). Its principal eigenvalue is \(\lambda_1=27D_0j_{-1/3,1}^2/(32L^2)\). To compare rigorously with the homogeneous eigenvalue \(\pi^2D_0/(4L^2)\), write
\[
\Gamma(2/3)(z/2)^{1/3}J_{-1/3}(z)=1-\frac32 w+\frac9{20}w^2-\frac9{160}w^3+\cdots,\quad w=z^2/4.
\]
For \(0\le z\le43/25\), the alternating remainder after the cubic term is nonnegative and the cubic lower bound is decreasing and greater than \(0.113\) on \(0\le w\le(43/50)^2\). Thus \(j_{-1/3,1}>43/25\). Consequently
\[
\frac{27}{32}j_{-1/3,1}^2>\frac{27}{32}\left(\frac{43}{25}\right)^2>\frac{121}{49}>\frac{\pi^2}{4},
\]
using \(\pi<22/7\). The principal eigenfunction is strictly positive and the initial survival function has nonzero projection on it, so its decay is governed by this eigenvalue. This proves the late-survival ratio and hence, by continuity, at least one CDF crossing.

**6. Positive-profile robustness.** The normalized \(D_\delta\) converges pointwise to \(D_*\), and \(D_\delta^{-1}\to D_*^{-1}\) in \(L^1(0,L)\) by dominated convergence. The intrinsic action \(\int_0^L D_\delta(x)^{-1/2}\,dx\) tends to \(\int_0^L D_*(x)^{-1/2}\,dx\), which strictly exceeds the homogeneous action. For smooth positive coefficients, the classical short-time diffusion action gives the same early-arrival sign. The principal eigenvalue admits the Rayleigh characterization
\[
\lambda_1(D)=\inf_{f(L)=0,\,f\ne0}\frac{\int_0^L|f'(x)|^2\,dx}{\int_0^L|f(x)|^2/D(x)\,dx},
\]
with \(f\in H^1(0,L)\) and natural Neumann boundary at \(0\). Since \(\|f\|_\infty\le\sqrt L\|f'\|_2\) for \(f(L)=0\), the \(L^1\) convergence of inverse coefficients makes the quadratic denominators converge uniformly on the derivative-unit sphere. Thus \(\lambda_1(D_\delta)\to\lambda_1(D_*)\), preserving the strict late-survival inequality for all sufficiently small \(\delta>0\). The mean inequality also persists by dominated convergence, but the regularizations need not be exactly mean-optimal.

## Verification

The accompanying `verify.py` uses only the Python standard library. It checks exact rational moment identities, a positive lower bound for the Bessel-root polynomial, numerical Bessel-root bracketing, Laplace values at several arguments, the short-time action constants and a finite-difference shooting calculation for a positive regularization. On replay it returned `PASS` with \(j_{-1/3,1}=1.866350858874\), normalized principal eigenvalues \(2.939005289604\) and \(2.467401100272\), and a positive-regularization example at \(\delta=10^{-4}\). Numerical checks are not used to prove infinite products, all-time comparisons or a unique crossing; those are addressed in the proof, and no unique crossing is claimed. Run `python3 verify.py` from the directory containing that file.

## Relationship to prior work

Menon (2026) establishes the exact mean-optimal square-root Itô profile and its \(1/9\) mean improvement. Menon, dos Santos and Anteneodo (2023) give bounded-interval first-passage machinery for heterogeneous diffusion, including a statement that certain power-law families can be treated by Bessel methods. Dos Santos, Menon and Anteneodo (2022) analyze power-law heterogeneous first-passage laws on a different (unbounded) geometry. These are credited, not recast as discoveries. The present finding adds the explicit optimal-profile law, the competing sharp short/long-time comparisons with the homogeneous law, and robustness under strictly positive smooth profiles. Classical Bessel product and Sturm–Liouville theory are used as tools.

## Limitations

The conclusions concern one-dimensional, zero-drift Itô diffusion, reflecting–absorbing boundaries, an initial point at reflection, and the stated mean-budget constraint. They do not give uniqueness or location of the CDF crossing, optimize any finite-time quantile, or quantify the range of positive regularization values for which the inequalities persist. The singular exact optimum vanishes at the absorbing endpoint; strictly positive regularizations preserve the qualitative reversal but are not themselves asserted to minimize the mean. The underlying Bessel-transform framework is classical, and implicit coverage of aspects of the result by older general spectral theory cannot be ruled out without independent priority assessment.

## References

1. L. Menon, *Optimal heterogeneous diffusivity profiles for mean first-passage minimization* (first posted 12 November 2026), arXiv:2611.17470v1, https://arxiv.org/html/2611.17470v1 .
2. L. Menon Jr., M. A. F. dos Santos and C. Anteneodo, *Random-search efficiency in a bounded interval with spatially heterogeneous diffusion coefficient* (2023), arXiv:2311.00818, https://arxiv.org/abs/2311.00818 .
3. M. A. F. dos Santos, L. Menon Jr. and C. Anteneodo, *Efficiency of random search with space-dependent diffusivity* (2022), arXiv:2206.14229, https://arxiv.org/abs/2206.14229 .
4. E. Martin, U. Behn and G. Germano, *First-passage and first-exit times of a Bessel-like stochastic process*, Phys. Rev. E 83, 051115 (2011), https://doi.org/10.1103/PhysRevE.83.051115 .
