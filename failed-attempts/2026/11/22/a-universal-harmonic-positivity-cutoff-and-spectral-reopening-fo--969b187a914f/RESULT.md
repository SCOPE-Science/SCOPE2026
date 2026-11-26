# A universal harmonic-positivity cutoff and spectral reopening for mixtures of circle Poisson kernels

## Finding

Let \(k\ge1\) be an integer, and let \(\mu\) be any Borel probability measure supported in \((0,1)\) and satisfying \(\int(1-r)^{-1}\,d\mu(r)<\infty\). Define the standard circle Poisson kernel and its positive mixture by
\[
P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2},\qquad F_\mu(\theta)=\int P_r(\theta)\,d\mu(r),
\]
and set \(K_b(x,y)=F_\mu(x-y)(1+b\cos(k(x-y)))\), where \(b\in\mathbb R\). Write \(a_j=\int r^j\,d\mu(r)\), for all integers \(j\ge0\).

**Sharp positivity and support theorem.** For every finite set of circle points and every choice of complex coefficients, \(K_b\) is positive semidefinite if and only if
\[
\boxed{\quad b\ge b_*:=-\frac{2a_k}{a_0+a_{2k}}.\quad}
\]
For \(b>b_*\), every Fourier coefficient of \(K_b\) is strictly positive. At \(b=b_*\), the Fourier coefficients at exactly \(n=\pm k\) vanish if \(\mu\) is not a point mass; all remaining coefficients are strictly positive, so the critical kernel is strictly positive definite on every finite set of distinct points. If \(\mu=\delta_r\) is a point mass instead, the critical Fourier support is precisely \(\{-(k-1),\ldots,k-1\}\), of rank \(2k-1\), so finite-set strictness fails for sufficiently many points.

The two-rate case has an exact spectral-reopening identity. For \(0<r<s<1\), \(u,v>0\), \(u+v=1\), and \(\mu=u\delta_r+v\delta_s\), the critical coefficients obey, at every \(n>k\),
\[
\boxed{\quad \widehat K_{b_*}(n)=\frac{uv(s^k-r^k)(1-(rs)^k)(s^{n-k}-r^{n-k})}{u(1+r^{2k})+v(1+s^{2k})}>0.\quad}
\]
Thus even an arbitrarily small positive admixture of a second Poisson scale restores every high Fourier mode suppressed by the pure critical kernel.

## Assumptions and scope

The circle is \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\); Fourier coefficients use \(\widehat F(n)=(2\pi)^{-1}\int_0^{2\pi}F(\theta)e^{-in\theta}\,d\theta\). The summability assumption \(\int(1-r)^{-1}\,d\mu(r)<\infty\) implies \(\sum_{j\ge0}a_j<\infty\), so all Fourier series converge absolutely and uniformly. No positive lower bound or upper bound away from \(1\) on the mixing support is required. The probability normalization gives \(a_0=1\), while every \(a_j>0\). Positive semidefiniteness means the Hermitian Gram form is nonnegative for any finite sample; strict positive definiteness requires positivity on nonzero vectors for pairwise distinct sites. The result is about stationary circle kernels, not nonstationary sum-coordinate modulations or kernels on higher-dimensional spheres.

## Proof

**1. Fourier reduction.** The absolutely convergent Poisson expansion \(P_r(\theta)=\sum_{n\in\mathbb Z}r^{|n|}e^{in\theta}\) gives
\[
\widehat K_b(n)=a_{|n|}+\frac b2\bigl(a_{|n-k|}+a_{|n+k|}\bigr).
\]
The circle Bochner criterion characterizes positive semidefiniteness by nonnegativity of every coefficient. For \(n\ge0\), set
\[
R_n=\frac{a_{|n-k|}+a_{n+k}}{a_n},\qquad R_k=\frac{a_0+a_{2k}}{a_k}.
\]
We prove \(R_n\le R_k\) for all \(n\ge0\). This identifies the most restrictive coefficient for negative \(b\).

**2. Frequencies below \(k\).** Moment coefficients are strictly decreasing, and their sequence is log-convex by the Cauchy–Schwarz inequality \(a_{j+1}^2\le a_ja_{j+2}\). Thus, for \(0\le n<k\),
\[
\frac{a_{k-n}}{a_n}<\frac{a_0}{a_k},\qquad
\frac{a_{n+k}}{a_n}\le\frac{a_{2k}}{a_k}.
\]
The first inequality follows from \(a_{k-n}<a_0\) and \(a_n\ge a_k\). The second follows because \(a_{n+k}/a_n\) is nondecreasing in \(n\) for any log-convex positive sequence. Hence \(R_n<R_k\).

**3. Frequencies above \(k\).** Define \(h(r)=r^{-k}+r^k\), which is strictly decreasing for \(0<r<1\). Although \(h\) may diverge as \(r\downarrow0\), its weighted integrals below are finite for all \(n\ge k\). For every \(n\ge k\),
\[
R_n=\frac{\int r^nh(r)\,d\mu(r)}{\int r^n\,d\mu(r)}.
\]
Increasing \(n\) tilts the measure toward larger \(r\), hence decreases the expectation of \(h\). Formally, for any integer \(m>n\), the covariance of the strictly decreasing \(h(r)\) and strictly increasing \(r^{m-n}\), under the probability measure proportional to \(r^n\,d\mu(r)\), is nonpositive. It is strictly negative unless \(\mu\) is supported at one point. Therefore \(R_n\le R_k\), with strict inequality for \(n>k\) for all non-point-mass mixtures; a point mass gives equality for every \(n\ge k\).

**4. Sharp cutoff and rank.** At \(b=b_*=-2/R_k\),
\[
\widehat K_{b_*}(n)=a_{|n|}\left(1-\frac{R_{|n|}}{R_k}\right).
\]
The inequalities above show that exactly the modes specified in the finding vanish. For \(b>b_*\), all coefficients are positive (including \(b\ge0\), which is immediate from the coefficient formula). For \(b<b_*\), the coefficient at \(n=k\) is negative, proving necessity. If \(\mu=\delta_r\), direct substitution gives
\[
\widehat K_{b_*}(n)=\frac{r^{|n|}(1-r^{2(k-|n|)})}{1+r^{2k}}>0\quad (|n|<k),
\]
and zero for \(|n|\ge k\). For non-point mixtures, the positive Fourier support is all integers except \(\pm k\). Given any \(N\) distinct sample points, a vanishing Gram form forces \(\sum_{j=1}^Nc_je^{inx_j}=0\) for all sufficiently large consecutive integers \(n\). The corresponding \(N\times N\) Vandermonde matrix is invertible, so every \(c_j=0\). This proves strict positive definiteness. The pure case has Fourier feature dimension \(2k-1\) and cannot be strictly positive definite on \(N\ge2k\) distinct sites.

**5. Exact two-rate reopening.** If \(\mu=u\delta_r+v\delta_s\), for \(n>k\) elementary cross multiplication yields
\[
R_k-R_n=\frac{uv r^ks^k\bigl(h(r)-h(s)\bigr)\bigl(s^{n-k}-r^{n-k}\bigr)}{a_ka_n}.
\]
Using \(r^ks^k(h(r)-h(s))=(s^k-r^k)(1-(rs)^k)\), and \(a_kR_k=a_0+a_{2k}\), produces the boxed formula. Each factor in the numerator is positive.

## Verification

A dependency-free Python checker, `proof_check.py`, uses exact rational arithmetic on point-mass, two-rate and three-rate measures for harmonics \(1\le k\le8\). It directly recomputes the Fourier coefficients, critical parameter, ratio inequalities, pure/mixed spectral zeros and the exact two-rate high-frequency factorization. A separate log-convex counterexample is included to test the essential moment restriction. The checker passed 79,922 exact-rational assertions when executed from this package. The infinite universal quantifiers and strictness statements are proved analytically in the preceding section; finite computations are supporting regression tests, not a proof by enumeration.

## Relationship to prior work

Schoenberg–Bochner Fourier positivity and circle spectral support criteria provide the general foundation [1,2]. Work on spectral coefficients of positive definite functions [1], on the strict positive-definite support condition [2], and on Fourier-defined circular densities [3] does not give the moment-mixture cutoff or its exceptional rank transition. A related fractional-power kernel calculation gives the \(e^{-t|n|^\alpha}\) specialization for \(0<\alpha\le1\); these sequences are Poisson mixtures by complete monotonicity. The present result extends this to every summable positive Poisson mixture and supplies the exact two-scale high-frequency reopening law, which cannot be obtained by substituting a fractional exponent. Earlier nonstationary Poisson modulation and mixed-Poisson curvature classifications address different kernels or different observables. The sharp two-rate reopening law, valid for arbitrary harmonic order, is therefore not a restatement of those formulas on the inspected evidence. Priority beyond the inspected sources remains provisional.

## Limitations

A positive mixing law satisfying \(\int(1-r)^{-1}\,d\mu(r)<\infty\) is assumed; complex signed mixing measures, endpoint mass at \(1\), arbitrary log-convex coefficient sequences, multidimensional groups and general polynomial modulations are not covered. The moment assumption matters: \(a_n=(1/3)^n\) for \(n\le4\) and \(a_n=(1/3)^4(2/3)^{n-4}\) for \(n\ge4\) is positive, summable and log-convex, but for \(k=1\) the ratio \(R_1=10/3\) is exceeded by \(R_4=11/3\). The general theorem cannot be extended to all log-convex sequences. No claim of independent validation or comprehensive historical uniqueness is made.

## References

[1] P. G. Bissiri, V. A. Menegatto and E. Porcu, *Relations between Schoenberg Coefficients on Real and Complex Spheres of Different Dimensions*, first public arXiv version 21 July 2018, https://arxiv.org/abs/1807.08184.

[2] J. Emonds and H. Führ, *Strictly positive definite functions on compact abelian groups*, arXiv:1002.3017, https://arxiv.org/abs/1002.3017.

[3] S. Kato, A. Pewsey and M. C. Jones, *Tractable circula densities from Fourier series*, published online 22 November 2021, https://doi.org/10.1007/s11749-021-00790-y.

[4] NIST Digital Library of Mathematical Functions, §1.15(iii), circle Poisson-kernel expansion, https://dlmf.nist.gov/1.15.E12.
