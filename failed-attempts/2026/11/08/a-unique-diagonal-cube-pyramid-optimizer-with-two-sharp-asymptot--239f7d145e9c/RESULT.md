# A unique diagonal cube-pyramid optimizer with two sharp asymptotic corrections

## Finding

Let \(Q_n=[0,1]^n\), where \(n\geq3\). For a section perpendicular to the body diagonal,
\[
H_s=\left\{z\in\mathbb R^n:\sum_{j=1}^n z_j=s\right\},\qquad \frac n2\leq s<n,
\]
consider the largest-volume pyramid whose base is \(Q_n\cap H_s\) and whose apex lies in \(Q_n\). Its volume is \(V_n(s)\). There is **exactly one** maximizing parameter \(s_n\) on \([n/2,n]\), and \(s_n>n/2\).

Writing \(c_n=V_n(n/2)\) and \(D_n=V_n(s_n)\), the following expansions hold as \(n\to\infty\):
\[
\boxed{s_n=\frac n2+\frac16+\frac{2}{45n}+O(n^{-2}),}
\]
\[
\boxed{\frac{D_n}{c_n}=1+\frac1{6n}+\frac7{120n^2}+O(n^{-3}),}
\]
\[
\boxed{D_n=\sqrt{\frac3{2\pi n}}\left(1+\frac1{60n}+\frac{73}{3360n^2}+O(n^{-3})\right).}
\]
In particular, the optimum diagonal section is displaced by a nonzero, asymptotically constant coordinate-sum offset from the cube center, and the optimal relative volume gain over the centered diagonal section is asymptotically \(1/(6n)\).

## Assumptions and scope

A pyramid is the convex hull of an apex and a compact, full-dimensional-in-its-hyperplane base. The cube and Euclidean volume have their standard normalization. The assertion optimizes **only over sections orthogonal to a main diagonal**, with the apex anywhere in the cube; it does **not** assert that these pyramids are globally maximal among sections of all orientations. The dimension satisfies \(n\geq3\), and the big-O constants are absolute for sufficiently large \(n\).

Let \(U_1,\dots,U_n\) be independent uniform random variables on \([0,1]\), and let \(f_n\) denote the density of \(S_n=\sum_jU_j\). Its inclusion-exclusion representation is
\[
f_n(s)=\frac1{(n-1)!}\sum_{k=0}^{\lfloor s\rfloor}(-1)^k{n\choose k}(s-k)^{n-1},\qquad 0<s<n.
\]
For \(s\geq n/2\), the farthest cube vertex from \(H_s\) is the origin. The coarea formula gives \(\operatorname{vol}_{n-1}(Q_n\cap H_s)=\sqrt n\,f_n(s)\). Thus the exact pyramid volume is
\[
V_n(s)=\frac{s}{n}f_n(s),\qquad \frac n2\leq s\leq n.
\]
Reflection in the cube center identifies the opposite, equally optimal sections. For each \(n\geq3\), the unique value \(s_n\) also has the exact characterization \(f_n(s_n)+s_n f_n'(s_n)=0\). In dimension three, the optimizer is \(s_3=1+1/\sqrt2\), and its volume \(D_3=(1+\sqrt2)/6\) is the previously known global cube-pyramid maximum [1].

## Proof

**1. Global uniqueness in the diagonal family.** The density of a uniform interval is log-concave (with the zero extension), and convolution preserves log-concavity; consequently \(f_n\) is positive and log-concave on \((0,n)\). Since \(\log s\) is strictly concave, \(\log(s f_n(s))\) is strictly concave on \((0,n)\). For \(n\geq3\), the central derivative exists; the symmetry \(f_n(n/2+x)=f_n(n/2-x)\) implies \(f_n'(n/2)=0\). Therefore \(V'_n(n/2)=f_n(n/2)/n>0\). Since \(V_n(n)=0\), strict concavity yields one and only one maximizer in \((n/2,n)\).

**2. Differentiable local-limit expansion.** Put \(a_n(x)=f_n(n/2+x)\). Fourier inversion for sums of centered uniforms gives
\[
a_n(x)=\frac1{2\pi}\int_{\mathbb R}e^{-itx}\left(\frac{\sin(t/2)}{t/2}\right)^n\,dt.
\]
With \(t=u/\sqrt n\), the central Taylor expansion is
\[
n\log\left(\frac{\sin(u/(2\sqrt n))}{u/(2\sqrt n)}\right)
=-\frac{u^2}{24}-\frac{u^4}{2880n}-\frac{u^6}{181440n^2}
+O\left(\frac{u^8}{n^3}\right).
\]
Expanding the Fourier phase and integrating termwise against the Gaussian kernel \(e^{-u^2/24}\) gives, uniformly for \(|x|\leq R\) for every fixed \(R\),
\[
\frac{a_n(x)}{\sqrt{6/(\pi n)}}
=1-\frac{6x^2+3/20}{n}
+\frac{18x^4+(9/2)x^2-13/1120}{n^2}
+O_R(n^{-3}). \tag{1}
\]
The expansion and its first \(x\)-derivative have uniform remainders of this order. To justify termwise integration with the claimed derivative remainder, choose the scaled Fourier window \(|u|\leq n^{1/16}\). On this window the logarithmic Taylor remainder is bounded by \(C|u|^8/n^3\); combining it with the phase expansion gives a remainder dominated by \(C_Rn^{-3}(1+|u|^{18})e^{-u^2/48}\), both before and after one \(x\)-derivative. On \(n^{1/16}<|u|<\delta\sqrt n\), the sinc inequality \( |\sin v/v|\leq e^{-c v^2}\) for \(|v|<\delta/2\) makes the integral exponentially small in \(n^{1/8}\). On \(|u|\geq\delta\sqrt n\), separate a fixed compact interval, where the sinc modulus is uniformly less than one, and the remaining tail, where it is bounded by \(2/|t|\) in the unscaled Fourier variable \(t=u/\sqrt n\). Those pieces are exponentially small in \(n\), also with the extra factor \(t\) from differentiation. Thus the remainder and its derivative are uniformly \(O_R(n^{-3})\) after the displayed normalization. The required centered Gaussian moments are \(12,432,25920,2177280\) in degrees two, four, six and eight. This yields (1), including its constant term.

Taking the logarithm of (1) cancels the terms independent of \(x\) and yields
\[
\log\frac{a_n(x)}{a_n(0)}=-\frac{6x^2}{n}+\frac{18x^2}{5n^2}+O_R(n^{-3}), \tag{2}
\]
\[
\frac{a'_n(x)}{a_n(x)}=-\frac{12x}{n}+\frac{36x}{5n^2}+O_R(n^{-3}). \tag{3}
\]

**3. Localization and the optimizing offset.** The logarithmic derivative of \(V_n(n/2+x)\) is \((n/2+x)^{-1}+a'_n(x)/a_n(x)\). At \(x=0\) it is positive; at \(x=1\) it is negative for all sufficiently large \(n\), by (3). Strict log-concavity therefore puts the unique optimum \(x_n=s_n-n/2\) in \((0,1)\), so the fixed-compact expansions apply at \(x_n\). The stationarity equation becomes
\[
0=\frac{2-12x_n}{n}+\frac{16x_n}{5n^2}+O(n^{-3}),
\]
whence first \(x_n=1/6+O(n^{-1})\), and then
\[
x_n=\frac16+\frac{2}{45n}+O(n^{-2}). \tag{4}
\]

**4. Sharp relative and absolute values.** Using (2),
\[
\log\frac{D_n}{c_n}
=\log\left(1+\frac{2x_n}{n}\right)+\log\frac{a_n(x_n)}{a_n(0)}
=\frac{2x_n-6x_n^2}{n}+\frac{(18/5)x_n^2-2x_n^2}{n^2}+O(n^{-3}).
\]
The leading expression is stationary at \(x=1/6\), so the \(n^{-1}\) correction in (4) contributes only at order \(n^{-3}\). Consequently
\[
\log\frac{D_n}{c_n}=\frac1{6n}+\frac2{45n^2}+O(n^{-3}),
\]
and exponentiation gives the claimed relative expansion. Equation (1) at \(x=0\) also reproduces the previously known central Laplace–Pólya expansion [4]:
\[
c_n=\sqrt{\frac3{2\pi n}}\left(1-\frac3{20n}-\frac{13}{1120n^2}+O(n^{-3})\right).
\]
Multiplication yields the absolute expansion for \(D_n\). This completes the proof.

## Verification

Run `python verify.py` with SciPy as specified in `requirements.txt`. The standalone script independently evaluates the Irwin–Hall inclusion-exclusion density using exact rational arithmetic in small dimensions, cross-checks the SciPy density and derivatives, numerically optimizes the diagonal-pyramid volume, tests the exact three-dimensional case, and compares the first two asymptotic corrections at increasing dimensions. It passed 672 finite checks in the reported run. No numerical calculation is used in place of the analytic proof for all dimensions.

## Relationship to prior work

Nikolov [1] derives the same exact volume representation and gives the global maximal pyramid volume in dimension three, the centered extremum and its leading high-dimensional limit, and strict inequalities between the unknown global maxima and centered values. Those results are prior work, not new here. The new claim is the complete unique diagonal-family optimizer together with its two explicit high-dimensional corrections. Pournin [2] studies the **orientations** of hypercube sections at fixed distance from the center, rather than maximizing section area multiplied by available pyramid height over the displacement variable. Marengo–Farnsworth–Stefanic [3] describe the classical Irwin–Hall density itself, not the size-biased optimization and its sharp corrections. Ambrus–Gárgyán [4] record the already-known two correction coefficients for the **central** Laplace–Pólya integral; the new results concern the free-offset optimizer and its shifted maximum, not the central coefficients.

## Limitations

No assertion is made about the maximizing section orientation for the unrestricted cube-pyramid problem when \(n\geq4\). The Irwin–Hall density formula and the dimension-three global value were already known. The correction terms are asymptotic and do not provide a universal finite-dimensional error constant. Related older probability/convex-geometric literature may contain an equivalent off-center size-biased-density calculation; historical priority is therefore provisional. No independent mathematical audit has been performed.

## References

[1] N. Nikolov, *Maximal volumes of pyramids in the unit cube*, arXiv:2610.14047v1 (first posted 2026-10-04), https://arxiv.org/html/2610.14047v1.

[2] L. Pournin, *Local extrema for hypercube sections*, arXiv:2203.15054v2 (2023), https://arxiv.org/html/2203.15054v2.

[3] J. E. Marengo, D. L. Farnsworth, L. Stefanic, *A Geometric Derivation of the Irwin-Hall Distribution*, International Journal of Mathematics and Mathematical Sciences (2017), doi:10.1155/2017/3571419, https://onlinelibrary.wiley.com/doi/10.1155/2017/3571419.

[4] G. Ambrus, B. Gárgyán, *Estimates on the decay of the Laplace–Pólya integral*, Bulletin of the London Mathematical Society 57 (2025), 3360–3379, doi:10.1112/blms.70157, https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.70157.
