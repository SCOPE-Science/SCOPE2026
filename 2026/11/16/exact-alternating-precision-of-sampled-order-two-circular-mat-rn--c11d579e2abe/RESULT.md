# Exact alternating precision of sampled order-two circular Matérn fields

## Finding

Let the period-one circular Matérn kernel of Fourier order two be
\[
K_\kappa(x)=\sum_{m\in\mathbb Z}\frac{e^{2\pi i m x}}{(\kappa^2+4\pi^2m^2)^2},\qquad \kappa>0.
\]
For every integer \(n\ge3\), sample it at \(x_j=j/n\), \(0\le j<n\), and form the real positive-definite circulant covariance \(\Sigma_{ij}=K_\kappa((i-j)/n)\). Write \(Q=\Sigma^{-1}\), and let \(d=\min(|i-j|,n-|i-j|)\) be cyclic distance. The central assertion, with **no exceptional parameter, sample size, or pair**, is
\[
Q_{ij}\ne0,\qquad \operatorname{sign}(Q_{ij})=(-1)^d\quad(i\ne j).
\]
Thus the exact Gaussian conditional-dependence graph on every sampled cycle is complete, with alternating precision signs. In contrast, the same sampling of the order-one circular Matérn kernel has nearest-neighbor precision, so every non-neighbor precision entry vanishes whenever \(n\ge4\).

The inverse entries themselves have a closed form. Put
\[
\begin{gathered}
a=\kappa/n,\quad r=e^{-a},\\
A=1-r^4-4ar^2,\quad B=2r\big[a(1+r^2)-(1-r^2)\big],\\
s=\sqrt{A^2-B^2},\quad t=\frac{B}{A+s},\quad \eta=-t,\\
V=\frac{4r^2}{B},\qquad W=\frac{-4r(1+r^2)-VA}{B},\qquad
R=\left(1+r^2+\frac{2rA}{B}\right)^2.
\end{gathered}
\]
These satisfy \(A>B>0\), \(s>0\), \(0<t<1\), and \(R>0\). For \(d=0,1,\ldots,n-1\), using \(Q_{0d}=Q_{d0}\), the exact formula is
\[
\boxed{Q_{0d}=4\kappa^3\left[
 W\mathbf1_{d=0}+\frac V2\big(\mathbf1_{d=1}+\mathbf1_{d=n-1}\big)
 +\frac R{s}\frac{\eta^d+\eta^{n-d}}{1-\eta^n}\right].}
\]
For non-neighbor indices, only the last, geometrically decreasing term remains. At fixed \(\kappa\), as \(n\to\infty\), its geometric base satisfies \(t\to 2-\sqrt3\). In particular, the entries are never literally sparse, even though off-neighbor effects decay exponentially in lattice distance.

For an integer cyclic bandwidth \(L\ge1\), let \(Q^{(L)}\) retain the entries of \(Q\) at cyclic distances at most \(L\) and set the others to zero. Then the maximum absolute row-sum error obeys
\[
\boxed{\|Q-Q^{(L)}\|_\infty\le
\frac{16\kappa^3R}{s}\,
\frac{t^{L+1}}{(1-t)(1-t^n)}.}
\]
This is an explicit, finite-sample control on approximate locality; it does not assert exact conditional independence after truncation.

## Assumptions and scope

There is no restriction on the positive real parameter \(\kappa\), beyond positivity. The sample size is every integer \(n\ge3\), and all sample sites are precisely equispaced on the period-one circle. Order two here means Fourier denominator power two, corresponding to Matérn smoothness \(\nu=3/2\) in one dimension; the order-one control corresponds to \(\nu=1/2\). The normalization of \(K_\kappa\) is fixed by the displayed Fourier series; an arbitrary positive variance multiplier rescales the precision entries without changing any sign or zero pattern. No claim concerns nonuniform grids, other smoothness orders, or a spatial discretization of a stochastic differential equation.

## Proof

**1. Positive spectrum and the discrete Fourier symbol.** The inverse transform of \((\kappa^2+\omega^2)^{-2}\) is
\[
\frac{(1+\kappa |x|)e^{-\kappa|x|}}{4\kappa^3}.
\]
Poisson summation, justified by exponential decay, therefore gives
\[
K_\kappa(x)=\frac1{4\kappa^3}\sum_{\ell\in\mathbb Z}
(1+\kappa|x+\ell|)e^{-\kappa|x+\ell|}.
\]
Let \(c_k=(1+a|k|)r^{|k|}\). The covariance eigenvalue at the frequency \(2\pi j/n\) is \(f(2\pi j/n)/(4\kappa^3)\), where direct summation yields
\[
\begin{aligned}
f(\theta)&=\sum_{k\in\mathbb Z}c_ke^{-ik\theta}\\
&=\frac{1-r^2}{D(\theta)}+
\frac{2ar[(1+r^2)\cos\theta-2r]}{D(\theta)^2}
=\frac{A+B\cos\theta}{D(\theta)^2},\\
D(\theta)&=1+r^2-2r\cos\theta.
\end{aligned}
\]
Alternatively, sampling the strictly positive continuous Fourier transform gives
\[
f(\theta)=4a^3\sum_{\ell\in\mathbb Z}
\big[a^2+(\theta+2\pi\ell)^2\big]^{-2}>0.
\]
Moreover \(B=2r(1+r^2)(a-\tanh a)>0\), because \(a>\tanh a\) for \(a>0\). Evaluating \(f\) at \(0\) and \(\pi\) shows \(A>B>0\). Thus \(0<t<1\), and every covariance eigenvalue is strictly positive.

**2. Rational Fourier inversion.** Divide the quadratic polynomial \(D(\theta)^2\) in \(c=\cos\theta\) by the linear polynomial \(A+Bc\). Polynomial long division gives
\[
\frac{D(\theta)^2}{A+B\cos\theta}=W+V\cos\theta+
\frac{R}{A+B\cos\theta},
\]
with \(W,V,R\) precisely as in the statement. Since \(A>B>0\), the standard geometric Fourier series is absolutely convergent:
\[
\frac1{A+B\cos\theta}=\frac1s
\sum_{k\in\mathbb Z}(-t)^{|k|}e^{ik\theta}.
\]
Sampling at the \(n\)-th roots of unity periodizes its Fourier coefficients. For \(0\le d<n\), the geometric tail sums exactly to
\[
\sum_{\ell\in\mathbb Z}\eta^{|d+n\ell|}=
\frac{\eta^d+\eta^{n-d}}{1-\eta^n}.
\]
The constant and cosine terms contribute only at cyclic distances zero and one. This proves the boxed inverse formula, with no unverified limiting step.

**3. Non-neighbor signs, including the antipodal case.** For \(2\le d\le\lfloor n/2\rfloor\), the local terms in the inverse formula vanish. The denominator \(1-(-t)^n\) is positive. If \(n\) is even, \((-t)^d\) and \((-t)^{n-d}\) have the same sign; if \(n\) is odd, they have opposite signs but \(d<n-d\), so the first has strictly larger magnitude. Hence the sign is always \((-1)^d\), and the entry never vanishes.

**4. The nearest-neighbor sign, including odd sample sizes.** Write \(q_n=Q_{01}/(4\kappa^3)\) and \(H=R/s>0\). For even \(n\),
\[
q_n=\frac V2-H\frac{t+t^{n-1}}{1-t^n}
<\frac V2-Ht.
\]
Since \(A/B=(1+t^2)/(2t)\),
\[
R=\frac{(r+t)^2(1+rt)^2}{t^2},\qquad
Ht=\frac{2(r+t)^2(1+rt)^2}{B(1-t^2)}>
\frac{2r^2}{B}=\frac V2.
\]
Therefore \(q_n<0\) for every even \(n\ge4\). For odd \(n\ge3\),
\[
q_n=\frac V2-H\frac{t-t^{n-1}}{1+t^n}.
\]
At fixed \(a\), the positive fraction strictly increases with odd \(n\), so \(q_n\le q_3\). To see \(q_3<0\), use the positive covariance \(C_3=(c_{(i-j)\bmod3}^\mathrm{per})\), whose diagonal is \(u\) and whose three symmetric off-diagonal entries are \(v>0\). Its eigenvalues are \(u+2v>0\) and \(u-v>0\), and its inverse has off-diagonal
\[
-\frac{v}{(u-v)(u+2v)}<0.
\]
This proves the sign of every nearest-neighbor precision entry. Combined with Step 3 and cyclic symmetry, the asserted sign law follows for every pair.

**5. Bounds and comparison with order one.** The Taylor expansions \(A=(8/3)a^3+O(a^4)\) and \(B=(4/3)a^3+O(a^4)\) imply \(t\to1/(2+\sqrt3)=2-\sqrt3\) as \(a\downarrow0\). At a non-neighbor cyclic distance \(d\le n/2\), the explicit formula gives
\[
|Q_{0d}|\le\frac{8\kappa^3R}{s(1-t^n)}t^d.
\]
There are at most two vertices at each distance, and summing a geometric tail yields the stated row-sum bound. For Fourier order one, periodization of \(e^{-\kappa|x|}/(2\kappa)\) gives the symbol \((1-r^2)/(2\kappa D(\theta))\); its exact inverse has symbol \(2\kappa D(\theta)/(1-r^2)\), a trigonometric polynomial of degree one. Hence it has only nearest-neighbor off-diagonal entries on any \(n\ge4\) cycle.

## Verification

The companion `verify_precision.py` independently constructs the sampled covariance from a closed periodic-sum formula, inverts the resulting finite matrices at high precision, compares every entry with the Fourier formula, checks the alternating signs and computes the eigenvalue symbol without using the inverse formula. It tests all sample counts from \(3\) through \(16\) and five positive kernel parameters, for 14,980 comparisons. It also directly verifies nearest-neighbor precision for the order-one control at nine sites. The numerical checks are finite corroboration, not the proof of the quantified theorem. Run `python verify_precision.py` with the documented `mpmath` dependency.

## Relationship to prior work

Guinness and Fuentes (2016) introduce circular Matérn Fourier covariances, give half-integer closed forms, and prove their positive-definiteness and smoothness properties. Their Fourier kernels and periodization formulas are ingredients here, not new discoveries. Huang and Li (first publicly posted January 30, 2022) establish the circular Matérn/SPDE correspondence, obtain an exact nearest-neighbor conditional autoregression for order one and compare order two to a *different*, approximate, finite-range conditional autoregressive model; their Section 3 does not give the exact inverse or noncancellation signs for sampled order-two covariance. Lindgren, Rue and Lindström (2011) construct sparse *finite-element approximations* and explicitly observe dense mass-matrix inverses; a finite-element precision is not the exact inverse of the sampled field covariance considered here. General autoregressive-moving-average inversion and cyclic total-positivity theory are possible alternative routes, and may have established an equivalent sign classification elsewhere; priority remains provisional.

## Limitations

The finding is an exact theorem for equispaced samples only, with all positive range parameters and the displayed normalization. It says conditional dependence is nonzero, not that it has a large magnitude, nor that continuous fields lack a generalized Markov property. The truncation bound is a deterministic matrix-norm estimate, not an error bound for all statistical estimators. Historical completeness cannot be established by searches alone; an equivalent prior theorem in the older autoregressive-moving-average or cyclic-total-positivity literature remains the main priority risk. No independent mathematical audit is claimed.

## References

1. J. Guinness and M. Fuentes, *Isotropic covariance functions on spheres: Some properties and modeling considerations*, Journal of Multivariate Analysis **143** (2016), 143–152, DOI: 10.1016/j.jmva.2015.08.018. Author preprint: https://guinness.cals.cornell.edu/papers/spheres_withsupplement.pdf, especially Example 3, Theorem 2 and supplement S2.
2. C. Huang and A. Li, *The Circular Matérn Covariance Function and its Link to Markov Random Fields on the Circle*, arXiv:2201.12856 (first version January 30, 2022), especially Sections 2–3 and Appendices A–B. https://arxiv.org/abs/2201.12856.
3. F. Lindgren, H. Rue and J. Lindström, *An explicit link between Gaussian fields and Gaussian Markov random fields: the stochastic partial differential equation approach*, JRSS B **73** (2011), 423–498, DOI: 10.1111/j.1467-9868.2011.00777.x; especially Section 2 and Result 2. https://rss.onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9868.2011.00777.x.
4. J. N. Haddad, *On the closed form of the covariance matrix and its inverse of the causal ARMA process*, Journal of Time Series Analysis **25** (2004), 443–448, DOI: 10.1111/j.1467-9892.2004.01454.x (general nearby inversion methodology; full text not inspected).
