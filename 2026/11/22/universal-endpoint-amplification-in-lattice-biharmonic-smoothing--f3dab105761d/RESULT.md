# Universal endpoint amplification in lattice biharmonic smoothing and noncommuting cycle limits

## Finding
Let \(L\) be the nearest-neighbor Laplacian on the integer lattice, \((Lf)_j=2f_j-f_{j-1}-f_{j+1}\), and let \(T_\lambda=(I+\lambda L^2)^{-1}\) for \(\lambda>0\), acting on real bounded sequences. Then its exact sharp coordinatewise noise gain is the absolute mass of its convolution kernel, and this gain has the universal large-smoothing limit
\[
\boxed{\lim_{\lambda\to\infty}\|T_\lambda\|_{\ell^\infty(\mathbb Z)\to\ell^\infty(\mathbb Z)}
=1+\frac{\sqrt2\,e^{-3\pi/4}}{1-e^{-\pi}}
=1.140093467050976\ldots.}
\]
For every integer \(n\ge3\), let \(L_n=2I-S_n-S_n^{-1}\) on the cyclic group of order \(n\), where \(S_n\) is the cyclic shift, and put \(T_{n,\lambda}=(I+\lambda L_n^2)^{-1}\). The two limits of the **sharp maximum-norm operator gains** do not commute:
\[
\boxed{\lim_{\lambda\to\infty}\lim_{n\to\infty}\|T_{n,\lambda}\|_{\infty\to\infty}
=1+\frac{\sqrt2\,e^{-3\pi/4}}{1-e^{-\pi}},\qquad
\lim_{n\to\infty}\lim_{\lambda\to\infty}\|T_{n,\lambda}\|_{\infty\to\infty}=1.}
\]
The first limit is strictly greater than one: taking the large-grid limit before strong regularization leaves a nonvanishing worst-case coordinatewise amplification, whereas strong regularization on every fixed cycle converges to ordinary averaging.

## Assumptions and scope
The lattice and cycle Laplacians have symbol \(q(\theta)=2-2\cos\theta\), with no additional normalization. The penalty is \(L^2\) (the square of the Laplacian) and the data-fidelity term is the identity. The infinite operator is defined as the absolutely summable Fourier convolution whose multiplier is \(1/[1+\lambda q(\theta)^2]\). Its norm is the induced norm on **real** \(\ell^\infty\); since the kernel is real, the same numerical norm holds over complex inputs. Finite cycles use the nearest-neighbor periodic closure, not free-end or other boundary rules. The order of the limits in the finding is essential; no uniformity in both \(n\) and \(\lambda\) is claimed.

## Proof
**1. Absolute kernel and sharp norm.** The Fourier multiplier of \(T_\lambda\) is
\[
M_\lambda(\theta)=\frac1{1+\lambda(2-2\cos\theta)^2},\qquad
 g_{\lambda,k}=\frac1{2\pi}\int_{-\pi}^{\pi} e^{ik\theta}M_\lambda(\theta)\,d\theta.
\]
The rational Laurent symbol is analytic in an annulus containing the unit circle because its denominator never vanishes there for positive \(\lambda\). Therefore \((g_{\lambda,k})_{k\in\mathbb Z}\) decays exponentially and belongs to \(\ell^1\). Since convolution by \(g\) has norm at most \(\sum_k|g_k|\), and the bounded test sequence \(f_{-k}=\operatorname{sgn}(g_k)\) attains that value at the origin, its **sharp** norm is
\[
 N(\lambda)=\|T_\lambda\|_{\infty\to\infty}=\sum_{k\in\mathbb Z}|g_{\lambda,k}|.
\]
The row sum is \(\sum_k g_{\lambda,k}=M_\lambda(0)=1\).

**2. Strong-smoothing kernel scaling.** Put \(h=\lambda^{-1/4}\), and extend
\[
F_h(\xi)=\begin{cases}
[1+h^{-4}(2-2\cos(h\xi))^2]^{-1},&|\xi|\le\pi/h,\\0,&\text{otherwise}.
\end{cases}
\]
For each real \(\xi\), \(F_h(\xi)\to(1+\xi^4)^{-1}\). On its support, \(2-2\cos(h\xi)\ge4h^2\xi^2/\pi^2\); hence
\[
0\le F_h(\xi)\le\left(1+\frac{16}{\pi^4}\xi^4\right)^{-1}.
\]
Dominated convergence establishes \(F_h\to(1+\xi^4)^{-1}\) in \(L^1(\mathbb R)\). Its inverse Fourier transform is the classical fourth-order resolvent kernel
\[
K(x)=\frac{e^{-|x|/\sqrt2}}{2\sqrt2}
\left[\cos\!\left(\frac{|x|}{\sqrt2}\right)+\sin\!\left(\frac{|x|}{\sqrt2}\right)\right].
\]
Changing variables \(\theta=h\xi\) in the coefficient formula, the Fourier \(L^1\) estimate proves the uniform-in-integer-index convergence
\[
\sup_{k\in\mathbb Z}\left|h^{-1}g_{\lambda,k}-K(hk)\right|\longrightarrow0.
\]
For a fixed \(R>0\), it follows by the Riemann-sum theorem that
\[
\sum_{|hk|\le R}|g_{\lambda,k}|\longrightarrow\int_{-R}^{R}|K(x)|\,dx.
\]

**3. Uniform absolute-mass tails.** Local uniform Fourier convergence alone would *not* justify summing over all indices. To control the tails independently of \(h\), Parseval gives
\[
\sum_{k\in\mathbb Z}k^2|g_{\lambda,k}|^2
=\frac1{2\pi}\int_{-\pi}^{\pi}|M'_\lambda(\theta)|^2\,d\theta.
\]
For \(|\theta|\le\pi\), use \(q(\theta)\le\theta^2\), \(|q'(\theta)|\le2|\theta|\), and \(q(\theta)\ge4\theta^2/\pi^2\). With \(\theta=h\xi\), the derivative bound
\[
|M'_\lambda(h\xi)|\le
\frac{4h^{-1}|\xi|^3}{(1+16\xi^4/\pi^4)^2}
\]
yields \(h\sum_k k^2|g_{\lambda,k}|^2\le C\), for an absolute finite \(C\) and all \(0<h\le1\). Cauchy–Schwarz then gives, uniformly in sufficiently small \(h\),
\[
\sum_{|hk|>R}|g_{\lambda,k}|
\le \left(\sum_k k^2|g_{\lambda,k}|^2\right)^{1/2}
\left(\sum_{|k|>R/h}k^{-2}\right)^{1/2}
\le C'R^{-1/2}
\]
for fixed \(R\ge1\). Combining this tightness with step 2 and then sending \(R\to\infty\) shows
\[
N(\lambda)\longrightarrow\int_{\mathbb R}|K(x)|\,dx.
\]

**4. Exact absolute-mass integral.** The kernel has integral one. Substitute \(r=|x|/\sqrt2\). Its negative intervals on each half-line are precisely
\[
\left(\frac{3\pi}4+2j\pi,\frac{7\pi}4+2j\pi\right),\qquad j=0,1,2,\ldots.
\]
The total absolute negative mass across both half-lines is
\[
\sum_{j\ge0}\left|\int_{3\pi/4+2j\pi}^{7\pi/4+2j\pi}
 e^{-r}(\cos r+\sin r)\,dr\right|
=\frac{e^{-3\pi/4}}{\sqrt2(1-e^{-\pi})},
\]
using the antiderivative \(-e^{-r}\cos r\). The absolute integral equals the signed integral plus twice the negative mass, proving the constant in the finding.

**5. Finite cycles and the order of limits.** Fourier diagonalization (or directly periodizing the absolutely summable lattice kernel) gives the cyclic entries
\[
 g_{n,\lambda}(j)=\sum_{m\in\mathbb Z}g_{\lambda,j+mn},\qquad 0\le j<n.
\]
The triangle inequality shows \(\|T_{n,\lambda}\|_{\infty\to\infty}\le N(\lambda)\). Conversely, fix \(\lambda\) and a large finite symmetric index set containing all but arbitrarily small \(\ell^1\) kernel mass. Once \(n\) is larger than twice that set's radius, the retained indices occur in distinct residue classes. The reverse triangle inequality therefore gives \(\|T_{n,\lambda}\|\ge N(\lambda)-o_n(1)\). Thus \(\lim_{n\to\infty}\|T_{n,\lambda}\|=N(\lambda)\). For fixed \(n\), \(L_n\) has a simple zero eigenvalue (the constant mode) and all other eigenvalues are strictly positive; hence \(T_{n,\lambda}\to\mathbf1\mathbf1^{\mathsf T}/n\) in operator norm as \(\lambda\to\infty\). This averaging matrix has maximum-norm operator gain one. Applying these two fixed-parameter limits in opposite orders gives the asserted inequivalence.

## Verification
Run `python3 verify.py` in the directory containing this document and the supplied standard-library checker. The checker reconstructs lattice coefficients by the **exact contour-residue identity**
\[
 g_{\lambda,k}=2\operatorname{Re}\frac{r^{k+1}}{P'(r)},\qquad k\ge0,
\quad P(z)=z^2+\lambda(z-1)^4,
\]
where \(r\) is the root strictly inside the unit disk satisfying \(r+r^{-1}=2+i/\sqrt\lambda\); reflect these coefficients about zero. It checks convolution mass, finite-cycle Fourier values against cyclic periodization, the sharp periodization norm bound, and approach to the stated large-smoothing limit. The replay performed here returned `CHECK_OK 452 assertions`. These checks are finite and supplementary; the full large-parameter limit is proved by the Fourier scaling and uniform tail argument above. The residue truncation uses a geometric bound and is not a proof by finite enumeration.

## Relationship to prior work
Whittaker–Henderson and Hodrick–Prescott second-difference filtering are standard. McElroy (2006/2008) derived explicit **infinite-filter coefficients**, including oscillatory behavior; the present finding does not claim that formula or basic kernel sign oscillation as new. Cornea-Madeira (2017) and Yamada (2020) examine **finite path** smoothing and related spectral representations; those papers do not state the sharp large-grid/large-regularization maximum-norm coefficient with the stated order-of-limits distinction. Publicly available results on positivity thresholds of periodic biharmonic smoothing give a different regime: a simultaneous \(\lambda\asymp n^4\) positivity threshold, not the two iterated endpoint-gain limits proved here. Results on universal range preservation across Whittaker–Henderson difference orders classify a distinct property, not this exact asymptotic gain. The precise new assertion is the **sharp summed absolute-mass scaling law and its noncommuting finite-cycle counterpart**, not the multiplier, base filter, spectral decomposition, or mere existence of negative coefficients.

## Limitations
The theorem concerns only the unweighted one-dimensional nearest-neighbor lattice and its periodic cycles. It gives the high-\(\lambda\) infinite-grid norm and two iterated limits, not an exact elementary closed form for \(N(\lambda)\) at every finite positive \(\lambda\), not a uniform two-parameter expansion, and not a result about open-ended path boundary conditions or arbitrary graphs. The continuum kernel itself and explicit infinite-filter coefficient formulas are classical/previously studied. Although targeted literature and public mathematical-result comparisons did not reveal this exact endpoint coefficient with the order-of-limits statement, an older derivation under equivalent-kernel or signal-processing terminology could exist. Finite numerical tests do not establish historical priority or the analytic limits.

## References
1. H. Yamada, *A Smoothing Method That Looks Like the Hodrick–Prescott Filter*, Econometric Theory 36 (2020), 961–981; first published online 23 March 2020, DOI: 10.1017/S0266466619000379, https://www.cambridge.org/core/journals/econometric-theory/article/smoothing-method-that-looks-like-the-hodrickprescott-filter/25D72F71BD468396D93D77BBC936A84C .
2. T. McElroy, *Exact Formulas for the Hodrick–Prescott Filter*, U.S. Census Bureau Research Report RRS2006/09 (2006), https://www.census.gov/content/dam/Census/library/working-papers/2006/adrm/rrs2006-09.pdf ; journal version Econometrics Journal 11 (2008), 209–217, DOI: 10.1111/j.1368-423X.2008.00230.x.
3. A. Cornea-Madeira, *The Explicit Formula for the Hodrick–Prescott Filter in Finite Sample*, Review of Economics and Statistics 99 (2017), 314–318, DOI: 10.1162/REST_a_00594, https://eprints.whiterose.ac.uk/id/eprint/97954/ .
4. *Only first-difference Whittaker–Henderson smoothing is universally range-preserving*, public mathematical research result, 4 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-only-first-difference-whittaker-henderson-smoothing-is-universal--b1f399ec57e6 .
5. *Parity-split positivity thresholds for periodic biharmonic smoothing*, public mathematical research result, 18 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-parity-split-positivity-thresholds-for-periodic-biharmonic-smoot--c19471e10093 .
