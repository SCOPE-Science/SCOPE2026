# Gaussian radial fluctuations of the expected-volume measures of Brownian convex hulls

## Finding

For an integer \(d\geq1\), let \(W\) be standard Brownian motion in \(\mathbb R^d\) on \([0,1]\), and let \(W_t^{\mathrm{br}}=W_t-tW_1\). Denote by \(K_d^B\) and \(K_d^A\) the convex hulls of the respective paths. For \(\bullet\in\{B,A\}\), define the normalized expected-volume measure
\[
\nu_d^\bullet(E)=\frac{\mathbb E\,\mathrm{vol}_d(K_d^\bullet\cap E)}{\mathbb E\,\mathrm{vol}_d(K_d^\bullet)},\qquad E\subseteq\mathbb R^d\ \text{Borel}.
\]
Let \(X_d^\bullet\) have law \(\nu_d^\bullet\), and set \(R_d^\bullet=\|X_d^\bullet\|^2\). Then, as \(d\to\infty\) through all positive integers,
\[
\frac{R_d^B-d/3}{\sqrt d}\ \Longrightarrow\ N(0,22/45),\qquad
\frac{R_d^A-d/12}{\sqrt d}\ \Longrightarrow\ N(0,11/360).
\]
Both limits share the standardized form
\[
\frac{R_d^\bullet-c_\bullet d}{c_\bullet\sqrt d}\ \Longrightarrow\ N(0,22/5),
\qquad c_B=1/3,\quad c_A=1/12.
\]
The first two moments also satisfy \(\mathbb E R_d^\bullet=c_\bullet d+O(1)\) and \(\mathrm{Var}(R_d^\bullet)=(22/5)c_\bullet^2d+O(1)\). The standardized radial variance is \(11/5\) times the radial variance of the Gaussian time-average of the corresponding generating path, even though their leading squared radii agree.

## Assumptions and scope

The hulls use standard independent-coordinate Brownian motion or Brownian bridge over the full unit interval. The measure \(\nu_d^\bullet\) averages the hull's Lebesgue measure **before** normalization. It is equivalently obtained by selecting a hull under a volume-biased path law, then sampling uniformly inside it; it is generally different from sampling a hull under the original path law and then a point uniformly inside that hull. All asserted limits concern the annealed measures \(\nu_d^\bullet\), not the law conditional on a typical hull. No high-dimensional embedding that simultaneously couples all dimensions is required.

## Proof

**1. Gaussian-probe reduction.** Put \(p_d^\bullet(r)=\mathbb P(re_1\in K_d^\bullet)\) and \(M_d^\bullet(z)=\int_0^\infty r^{z-1}p_d^\bullet(r)\,dr\). Radial integration identifies
\[
L_d^\bullet(t):=\mathbb E\exp(-tR_d^\bullet/2)
=\frac{\int_0^\infty r^{d-1}p_d^\bullet(r)e^{-tr^2/2}\,dr}{M_d^\bullet(d)},\qquad t\geq0.
\]
Let \(Z\sim N(0,I_d)\), independent of the hull, and write \(q_d^\bullet(\sigma)=\mathbb P(\sigma Z\in K_d^\bullet)\). Gaussian radial integration gives, for \(t>0\),
\[
q_d^\bullet(t^{-1/2})=\frac{t^{d/2}}{2^{d/2-1}\Gamma(d/2)}M_d^\bullet(d)L_d^\bullet(t).
\]
Kabluchko's exact Gaussian-probe identities [1, Section 2.1], obtained from [2, Theorem 5.1], supply
\[
q_d^B(t^{-1/2})=\frac2\pi\int_0^1
\frac{\Psi_d(\operatorname{arsinh}(\sqrt t\,y))}{\sqrt{1-y^2}\sqrt{1+ty^2}}\,dy,
\quad q_d^A(t^{-1/2})=\frac{\Psi_{d+1}(2\operatorname{arsinh}(\sqrt t/2))}{\sinh(2\operatorname{arsinh}(\sqrt t/2))},
\]
where \(\Psi_k(z)=\sum_{j\geq0}z^{k+2j}/(k+2j)!\). These are established identities, not contributions claimed here.

**2. Exact normalized transforms.** Define the analytic germ
\[
h(z)=\frac{\operatorname{arsinh}\sqrt z}{\sqrt z},\qquad h(0)=1.
\]
Let \(U_d\) have the beta law with parameters \(((d+1)/2,1/2)\). Substituting the series for \(\Psi_d\) in the type-\(B\) integral, applying \(\operatorname{arsinh}(\sqrt t\,y)=\sqrt t\,y h(ty^2)\), and normalizing by \(L_d^B(0)=1\) yields the **exact identity**
\[
L_d^B(t)=\mathbb E\left[h(tU_d)^d G_d(tU_d)\right],
\quad G_d(z)=(1+z)^{-1/2}\sum_{j=0}^{\infty}
\frac{d!}{(d+2j)!}\bigl(zh(z)^2\bigr)^j.
\tag{1}
\]
The beta law is obtained by setting \(U_d=y^2\) in the normalized weight \(y^d(1-y^2)^{-1/2}\,dy\). Similarly, the type-\(A\) identity becomes
\[
L_d^A(t)=h(t/4)^dH_d(t),
\quad H_d(t)=\frac{h(t/4)}{\sqrt{1+t/4}}
\sum_{j=0}^{\infty}\frac{(d+1)!}{(d+1+2j)!}
\bigl(th(t/4)^2\bigr)^j.
\tag{2}
\]
Both expressions extend analytically to a fixed disk around zero: for each finite \(d\), the Gaussian maximal tail of \(\sup_{0\leq s\leq1}\|W_s\|\) (and of the bridge) gives an exponential moment of \(R_d^\bullet\) for all sufficiently small positive exponents, and the two expressions are analytic there. The identities for positive \(t\) extend by the identity theorem.

**3. Uniform transform estimates.** Since \(h(0)=1\), choose \(\delta>0\) so that \(\log h\) is analytic and Lipschitz on \(|z|\leq\delta\). Factorial denominators in (1) and (2) give a constant \(C\) independent of \(d\) with
\[
|G_d(z)-1|\leq C|z|,\qquad |H_d(z)-1|\leq C|z|\quad (|z|\leq\delta).
\]
Set \(V_d=1-U_d\). It is beta distributed with parameters \((1/2,(d+1)/2)\), so for each integer \(k\geq0\),
\[
\mathbb E V_d^k=\frac{(1/2)_k}{((d+2)/2)_k}
\leq\frac{(1/2)_k2^k}{d^k}.
\]
Consequently for \(2C|t|<1\),
\[
\mathbb E e^{Cd|t|V_d}\leq(1-2C|t|)^{-1/2}=1+O(|t|).
\]
The Lipschitz bound \(|\log h(tU_d)-\log h(t)|\leq C|t|V_d\) and \(|e^z-1|\leq e^{|z|}-1\) now imply
\[
\mathbb E\left|\frac{h(tU_d)^d}{h(t)^d}-1\right|=O(|t|).
\]
Combining this with the uniform bounds on \(G_d,H_d\) yields, uniformly in \(d\geq1\) and \(t\) in a sufficiently small complex disk,
\[
L_d^B(t)=h(t)^d(1+O(|t|)),\qquad
L_d^A(t)=h(t/4)^d(1+O(|t|)).
\tag{3}
\]
The constants in the \(O(\cdot)\) notation are absolute on a fixed disk. In particular, (3) controls the logarithms with errors \(O(|t|)\), not merely the first two moments.

**4. Gaussian limits.** Taylor expansion at zero gives
\[
h(t)=1-t/6+3t^2/40+O(t^3),\qquad
\log h(t)=-t/6+11t^2/180+O(t^3).
\]
Putting \(t=-2is/\sqrt d\) for fixed real \(s\) into (3),
\[
\log L_d^B(-2is/\sqrt d)=is\sqrt d/3-11s^2/45+o(1),
\]
\[
\log L_d^A(-2is/\sqrt d)=is\sqrt d/12-11s^2/720+o(1).
\]
Multiplying by the characteristic-function centering factors \(e^{-isc_\bullet\sqrt d}\) and applying Lévy's continuity theorem proves the two asserted Gaussian limits. Scaling by \(c_\bullet\) gives the common variance \(22/5\).

**5. Moments and comparison.** Differentiating (1)–(2) twice at zero or using the exact Mellin ratios [1, equations (34), (35), (140), (141)] gives
\[
\mathbb E R_d^B=\frac{d(d^2+6d+11)}{3(d+2)^2},\quad
\mathbb E(R_d^B)^2=\frac{d(5d^4+92d^3+646d^2+2068d+2589)}{45(d+2)(d+4)^2},
\]
\[
\mathbb E R_d^A=\frac{d(d^2+9d+26)}{12(d+2)(d+3)},\quad
\mathbb E(R_d^A)^2=\frac{d(5d^4+122d^3+1171d^2+5278d+9624)}{720(d+3)(d+4)(d+5)}.
\]
Hence \(\operatorname{Var}(R_d^B)=22d/45+O(1)\) and \(\operatorname{Var}(R_d^A)=11d/360+O(1)\). The generating-path time-averages \(\int_0^1W_t\,dt\) and \(\int_0^1W_t^{\rm br}\,dt\) have Gaussian laws \(N(0,c_\bullet I_d)\). Their squared radii have variance \(2c_\bullet^2d\), versus \((22/5)c_\bullet^2d\) above: the ratio is exactly \(11/5\) at leading order.

## Verification

`checker.py` is a standalone Python 3 standard-library exact-rational checker. It independently expands the normalized transforms (1)–(2) through order two for 256 dimensions, comparing 1,024 moments with the published rational Mellin formulas, plus positivity and 26 further exact arithmetic/rate assertions (1,562 assertions total). Execution from the embedded file prints `PASS: 1562 independent exact rational assertions`. The finite calculations validate the transform normalizations and variance constants. The infinite-dimensional convergence is proved by the analytic estimates and Lévy's theorem above, not by these tests.

## Relationship to prior work

Kabluchko [1, Corollary 1.13] proves the two leading \(L^2\) thin-shell concentrations \(R_d^B/d\to1/3\) and \(R_d^A/d\to1/12\), and [1, Proposition 3.8] provides exact fixed-order moments. Those facts by themselves do not give the stated distributional Gaussian fluctuations; the new step is the dimension-uniform control (3) of the full Laplace transform on the \(d^{-1/2}\) scale, and the shared variance \(22/5\). Kabluchko [2] supplies the Gaussian-probe absorption identities used as the starting point. Panzo and Socher [3] study high-dimensional expected hull size, circumradius, diameter, and inverse-time bounds, not the volume-annealed interior-point distribution. Other classical convex-hull fluctuation papers deal with random-walk hull perimeter/diameter or fixed-dimensional sample-size asymptotics, not the dimension-asymptotic interior radius considered here. These are statement-level comparisons, not a claim that database nonmatches prove universal priority.

## Limitations

The result is annealed; it proves nothing about a point sampled uniformly inside a typical unweighted realized Brownian hull. It gives weak Gaussian convergence only, without a Kolmogorov or total-variation rate, multivariate coupling across dimension, or a large-deviation principle. Equations (1)–(2) depend on the primary literature's Gaussian-probe formulas. Historical-priority searches cannot guarantee that an equivalent general convex-hull theorem is absent from literature not inspected in full. No independent audit has been performed.

## References

[1] Z. Kabluchko, *Absorption Probabilities for Brownian Convex Hulls in Arbitrary Dimension*, arXiv:2611.00381v1 (first public 2026-10-30), https://arxiv.org/html/2611.00381v1. Especially Sections 1.8, 2.1, and 3.3.

[2] Z. Kabluchko, *Ornstein--Uhlenbeck Spirals: Absorption Probabilities and Conic Intrinsic Volumes*, arXiv:2610.37911 (first public 2026-10-27), https://arxiv.org/abs/2610.37911. The Gaussian-point formulas are reproduced in [1, equations (64)–(65)].

[3] H. Panzo and E. Socher, *Bounds on Some Geometric Functionals of High Dimensional Brownian Convex Hulls and Their Inverse Processes*, arXiv:2407.08712 (first public 2024-07-11), https://arxiv.org/abs/2407.08712.
