# Sharp mean-square Fejér error of periodic bounded-variation data: an asymptotic two-jump separation law

## Finding
Let \(\mathbb T=\mathbb R/\mathbb Z\) carry normalized Lebesgue measure. For each integer \(N\ge1\), let \(\sigma_N\) be the ordinary Fejér mean defined by the Fourier multiplier \(\widehat{\sigma_N f}(k)=(1-|k|/N)_+\widehat f(k)\). For real \(f\in BV(\mathbb T)\), let \(V(f)=|Df|(\mathbb T)\). Define the sharp squared approximation norm
\[
 C_N^2=\sup_{V(f)>0}\frac{\|f-\sigma_N f\|_{L^2(\mathbb T)}^2}{V(f)^2}.
\]
Every nonconstant extremizer is an indicator of one circular arc, up to addition of a constant, multiplication by a nonzero real scalar, and rotation. For every finite \(N\), its squared sharp constant is exactly
\[
 C_N^2=\max_{0\le d\le1/2}\!\left\{\frac{d(1-d)}4+\frac1{4\pi^2}\sum_{k=1}^{N-1}\left(\frac1{N^2}-\frac1{k^2}\right)(1-\cos(2\pi k d))\right\}.
\]
The sum is empty at \(N=1\); hence \(C_1=1/4\) and the optimal arc is a semicircle. Define \(\operatorname{Si}(q)=\int_0^q(\sin u)/u\,du\). There is exactly one \(q_*\in(0,2\pi)\) satisfying
\[
 \frac\pi2-\operatorname{Si}(q_*)+\frac{\sin q_*-q_*\cos q_*}{q_*^2}=0.
\]
It is the unique global maximizer over \(q>0\) of
\[
 \Phi(q)=\frac{2-\cos q-\sin(q)/q+q(\pi/2-\operatorname{Si}(q))}{4\pi^2}.
\]
The sharp asymptotic law and the localization of *every* optimal arc are
\[
 \lim_{N\to\infty}N C_N^2=\Phi(q_*)=0.053710534226645\ldots,\qquad
 \lim_{N\to\infty}N d_N=\frac{q_*}{2\pi}=0.532264718605\ldots,
\]
where \(d_N\in[0,1/2]\) is the shorter circular length of any optimal arc. Equivalently \(\sqrt N\,C_N\to0.231755332682\ldots\). In particular, for all sufficiently large \(N\), a semicircle is strictly suboptimal: worst Fejér mean-square error requires two approaching jumps.

## Assumptions and scope
All functions are real-valued periodic distributional \(BV\) classes on the unit-length circle; constants are factored out by the variation seminorm. The norm is the square root of normalized Lebesgue \(L^2\) energy. An arc indicator has two jump discontinuities and variation \(2\), unless the arc is empty or full. The parameter \(d\) is always the shorter of the two complementary arc lengths. No monotonicity or continuity of \(f\) is assumed. The Fejér indexing is fixed above, including \(N=1\) as projection onto constants.

## Proof
**1. Exact reduction to one arc.** For any nonconstant periodic real \(BV\) function, \(\mu=Df\) is a real signed measure of total mass zero. Its Jordan masses are both \(V(f)/2\). The product coupling of the normalized positive and negative variations expresses \(\mu\) as a convex average of \((V(f)/2)(\delta_a-\delta_b)\). Each such signed atomic derivative is the derivative of a signed circular arc indicator. The linear map \(I-\sigma_N\) annihilates constants, and the Hilbert-space triangle inequality bounds its norm on \(f\) by the maximum attained on one such indicator. Conversely, any optimal arc attains the bound. Strict convexity of the real Hilbert norm forces equality in this convex averaging only when all nonzero residual vectors are identical. The multiplier of \(I-\sigma_N\) is strictly positive at every nonzero integer frequency, so its nullspace consists precisely of constants. Thus any extremizing \(f\) itself has the single-arc form specified above.

**2. Exact formula.** Normalize an arc indicator to \(f=\tfrac12\mathbf1_{[0,d)}\), so \(V(f)=1\). Its Fourier coefficients satisfy \(|\widehat f(k)|^2=\sin^2(\pi k d)/(4\pi^2 k^2)\) at \(k\ne0\). Parseval gives
\[
 \|(I-\sigma_N)f\|_2^2=\frac1{4\pi^2}\sum_{k=1}^{\infty}\frac{\min(k/N,1)^2}{k^2}(1-\cos(2\pi k d)).
\]
Using \(\sum_{k\ge1}(1-\cos(2\pi k d))/k^2=\pi^2d(1-d)\) for \(0\le d\le1\) yields the finite formula in the finding. Complementary arcs have the same nonconstant Fourier coefficients up to sign, so \(0\le d\le1/2\) is sufficient.

**3. Scaling limit.** Write \(w(t)=1\) for \(0<t\le1\) and \(w(t)=t^{-2}\) for \(t>1\). With \(q=2\pi Nd\),
\[
 N\|(I-\sigma_N)(\tfrac12\mathbf1_{[0,d)})\|_2^2
 =\frac1{4\pi^2N}\sum_{k\ge1}w(k/N)(1-\cos(qk/N)).
\]
The Riemann sums converge locally uniformly in \(q\ge0\) to \(\Phi(q)=(4\pi^2)^{-1}\int_0^\infty w(t)(1-\cos qt)\,dt\). Splitting the integral at \(1\) and integrating by parts gives the stated sine-integral expression. Its value at infinity is \(\Phi_\infty=(2\pi^2)^{-1}\).

**4. Unique global maximum of the continuum profile.** Its derivatives are
\[
 4\pi^2\Phi'(q)=\frac\pi2-\operatorname{Si}(q)+\frac{\sin q-q\cos q}{q^2},\qquad
 4\pi^2\Phi''(q)=\frac{2(q\cos q-\sin q)}{q^3}.
\]
On \((0,2\pi)\), \(q\cos q-\sin q\) decreases from zero until \(\pi\), then increases and crosses zero exactly once. Thus \(\Phi'\) first decreases, then increases. It starts positive (limit \(1/(8\pi)\) for \(\Phi'\)), while \(\Phi'(2\pi)<0\): integration by parts yields \(4\pi^2\Phi'(2\pi)=-2\int_{2\pi}^\infty(\sin u)/u^3\,du<0\). The latter alternating half-wave integral is strictly positive. Hence \(\Phi'\) has exactly one zero on \((0,2\pi)\), a strict maximum.

To exclude *all* later local peaks, one integration by parts gives the explicit identity \[
\int_0^\infty w(t)\cos(qt)\,dt=\frac2q\int_1^\infty\frac{\sin(qt)}{t^3}\,dt.
\]
A further integration by parts bounds the last integral by \(2/q\) in absolute value. Hence
\[
 |\Phi(q)-\Phi_\infty|\le\frac1{\pi^2q^2},\qquad q>0.
\]
An exact rational interval calculation using Machin's identity for \(\pi\) and the alternating Taylor series of \(\operatorname{Si}(\pi)\) verifies
\[
 4\pi^2\bigl(\Phi(\pi)-\Phi_\infty\bigr)>\pi^{-2},
\]
so \(\Phi(\pi)>\Phi_\infty+1/(4\pi^4)\), whereas every \(q\ge2\pi\) satisfies \(\Phi(q)\le\Phi_\infty+1/(4\pi^4)\). The corresponding exact rational certificate is implemented in the standalone checker. Consequently the maximum above is the unique global one.

**5. Localization of finite optimizers.** Take any optimizing \(d_N\in[0,1/2]\) and set \(q_N=2\pi N d_N\). For fixed \(q\), Riemann-sum convergence gives \(\liminf N C_N^2\ge\Phi(q_*)>\Phi_\infty\). When \(q_N\to\infty\), discrete summation by parts and the monotonicity of \(w(k/N)\) give
\[
 \left|\frac1N\sum_{k\ge1}w(k/N)\cos(2\pi k d_N)\right|\le\frac{1}{N|\sin(\pi d_N)|}\le\frac1{2N d_N}\to0.
\]
Since \(N^{-1}\sum_{k\ge1}w(k/N)\to2\), this would give \(NC_N^2\to\Phi_\infty\), a contradiction. When \(q_N\to0\), dominated Riemann-sum convergence gives \(NC_N^2\to0\), also impossible. Thus optimal \(q_N\) stay bounded away from zero and infinity. Any subsequential limit maximizes \(\Phi\), so uniqueness forces \(q_N\to q_*\) and \(NC_N^2\to\Phi(q_*)\).

## Verification
The standalone `checker.py` verifies, by exact rational arithmetic, the strict comparison \(\Phi(\pi)>\Phi_\infty+1/(4\pi^4)\), using a certified arctangent interval for \(\pi\) and alternating-series interval bounds for the sine integral. It also compares the finite closed sum with a 150,000-frequency Fourier approximation at several \(N\) and \(d\), and checks the localization numerically at five cutoffs. All 40 finite numerical assertions and the rational certificate passed on extraction. The infinite-dimensional and asymptotic assertions follow from the analytical proof, not from the numerical checks.

## Relationship to prior work
Classical Fejér summation supplies the positive Fourier averaging operator and the general convergence framework. Yun (2012) studies polynomial spectral filters, Fejér as a special case, and pointwise errors near jumps; it does not present the sharp global periodic \(BV\)-to-\(L^2\) error or optimizing arc separation. Adcock and Hansen (2010 preprint) study stable reconstruction to defeat Gibbs oscillation, with nonsharp \(O(N^{-1/2})\) Fourier approximation background, but neither this operator norm nor this two-jump localization. Berdysheva–Dyn–Farkhi–Mokhov (2021) investigate metric Fourier partial sums for set-valued \(BV\) data and pointwise error, not Fejér mean-square extremization. Older direct literature on Fejér approximation, notably Andrienko (1968), must be acknowledged as a residual priority risk because its full text could not be verified here.

## Limitations
The main exact finite formula still requires maximizing one explicit one-variable function for arbitrary \(N\); uniqueness of its finite positive maximizer is not asserted. The theorem determines the continuum limit and all possible asymptotic optimal separations, not a complete finite-cutoff algebraic census. It applies to real periodic distributional variation and normalized \(L^2\), not complex variation, \(L^1\), other Fourier filters, or arbitrary spectral reconstruction algorithms. No independent validation of priority is claimed.

## References
- B. Adcock and A. C. Hansen, *Stable reconstructions in Hilbert spaces and the resolution of the Gibbs phenomenon*, arXiv:1011.6625, publicly posted 2010-11-30, https://arxiv.org/abs/1011.6625 ; accessible author preprint https://www.damtp.cam.ac.uk/research/afha/anders/Adcock_Hansen2.pdf .
- B. I. Yun, *A weighted averaging method for treating discontinuous spectral data*, Applied Mathematics Letters 25 (2012), 1234–1239, https://doi.org/10.1016/j.aml.2012.02.064 .
- E. E. Berdysheva, N. Dyn, E. Farkhi and A. Mokhov, *Metric Fourier Approximation of Set-Valued Functions of Bounded Variation*, Journal of Fourier Analysis and Applications 27 (2021), article 17, https://doi.org/10.1007/s00041-021-09812-7 .
- V. A. Andrienko, *The approximation of functions by Fejér means*, Siberian Mathematical Journal 9 (1968), 1–8, https://doi.org/10.1007/BF02196649 (full text not assessed).
