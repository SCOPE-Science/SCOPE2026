# Sharp two-mode \(L^p\) circle sampling distortion and zero-on-grid extremizers

## Finding
Fix \(1<p<2\), set \(s=p/2\), and let \(m\geq1\) be an integer. For any fixed \(\tau\in\mathbb R\), consider the equal-weight samples \(z_j=e^{i(\tau+2\pi j/m)}\), \(0\leq j<m\), of the complex two-dimensional function space \(\operatorname{span}_{\mathbb C}\{1,z\}\) on the unit circle. For nonzero \((a,b)\in\mathbb C^2\), define
\[
I_p(a,b)=\frac1{2\pi}\int_0^{2\pi}|a+be^{i\theta}|^p\,d\theta,\qquad Q_{m,p,\tau}(a,b)=\frac1m\sum_{j=0}^{m-1}|a+bz_j|^p.
\]
The sharp *relative \(p\)-moment* error is
\[
\boxed{\sup_{(a,b)\ne(0,0)}\left|\frac{Q_{m,p,\tau}(a,b)}{I_p(a,b)}-1\right|=E_{m,p}
=\frac{2\Gamma(1+s)^2\sin(\pi s)}{\pi}\sum_{\ell=1}^{\infty}\frac{\Gamma(\ell m-s)}{\Gamma(\ell m+s+1)}.}
\]
Every and only extremizing nonzero pair satisfies \(|a|=|b|>0\) and \(a+bz_j=0\) at one sample. At every extremizer, the sampled moment *underestimates* the exact moment by \(E_{m,p}\); no pair overestimates by the full absolute-error constant. In particular \(E_{1,p}=1\), and, with \(m\to\infty\),
\[
\boxed{E_{m,p}\sim\frac{2\Gamma(1+s)^2\sin(\pi s)}{\pi}\zeta(p+1)m^{-(p+1)}.}
\]
The result is an exact all-\(m\) norm-discretization theorem for the canonical complex two-dimensional subspace, not a statement about arbitrary higher-dimensional subspaces or arbitrary sampling locations.

## Assumptions and scope
Lebesgue measure on the circle is normalized to probability measure. Coefficients \(a,b\) may be arbitrary complex numbers, including zero individually, but not both zero. The exponent is strictly between one and two, the samples form a complete regular \(m\)-gon with equal weights, and the error concerns moments rather than their \(p\)-th roots. At \(m=1\) the sampling map is not injective, but its exact relative-error constant is still meaningful. The rotation \(\tau\) does not affect the constant or the zero-on-grid characterization.

## Proof
**Reduction to one real parameter.** Let \(M=|a|^2+|b|^2>0\), \(r=2|ab|/M\in[0,1]\), and choose a phase \(\varphi\) so that
\[
|a+be^{i\theta}|^p=M^s(1+r\cos(\theta+\varphi))^s.
\]
If one coefficient vanishes, take \(r=0\) and any \(\varphi\). Write \(F_r(\theta)=(1+r\cos\theta)^s\) and let \(c_k(r)=(2\pi)^{-1}\int_0^{2\pi}F_r(\theta)e^{-ik\theta}\,d\theta\). These coefficients are real and even in \(k\); \(c_0(r)>0\).

**Strict coefficient dominance.** For \(k\ge1\) and \(0<r<1\), the Chebyshev Rodrigues identity
\[
\frac{T_k(u)}{\sqrt{1-u^2}}=\frac{(-1)^k}{(2k-1)!!}\frac{d^k}{du^k}(1-u^2)^{k-1/2}
\]
and \(k\) integrations by parts give
\[
c_k(r)=\frac{(s)_{\underline{k}}}{\pi(2k-1)!!}
\int_{-1}^1r^k(1-u^2)^{k-1/2}(1+ru)^{s-k}\,du,
\]
where \((s)_{\underline{k}}=s(s-1)\cdots(s-k+1)\). The boundary terms vanish because the first \(k-1\) derivatives of \((1-u^2)^{k-1/2}\) vanish at both endpoints. Since \(0<s<1\), \(\operatorname{sgn}c_k(r)=(-1)^{k-1}\). The integrand is pointwise strictly increasing in \(r\), because
\[
\frac\partial{\partial r}\left[r^k(1+ru)^{s-k}\right]
=r^{k-1}(1+ru)^{s-k-1}(k+sru)>0
\]
for \(-1\le u\le1\), \(0<r<1\), and \(k\ge1\). Meanwhile \(c_0(r)\) is strictly decreasing on \((0,1)\): pairing \(u\) and \(-u\) in its derivative gives the strictly negative factor
\[
su\left[(1+ru)^{s-1}-(1-ru)^{s-1}\right],\qquad u\in(0,1).
\]
Thus \(|c_k(r)|/c_0(r)\) is strictly increasing as \(r\) increases from zero to one, for every fixed \(k\ge1\). Continuity at \(r=1\) follows by dominated convergence in the original integral and in the positive Rodrigues integral: near \(u=-1\) the latter behaves like \((1+u)^{s-1/2}\), which is integrable.

**Fourier aliasing and exact extremizers.** The coefficients are absolutely summable: for \(r<1\), \(F_r\) is real analytic; at \(r=1\), the explicit Gamma formula below gives \(|c_k(1)|=O(k^{-p-1})\). The regular-polygon identity therefore yields
\[
\frac{Q_{m,p,\tau}(a,b)}{I_p(a,b)}-1
=\frac{2}{c_0(r)}\sum_{\ell=1}^{\infty}c_{\ell m}(r)\cos(\ell m(\tau+\varphi)).
\]
By the triangle inequality and strict coefficient dominance,
\[
\left|\frac{Q}{I}-1\right|\le\frac2{c_0(r)}\sum_{\ell\ge1}|c_{\ell m}(r)|
\le\frac2{c_0(1)}\sum_{\ell\ge1}|c_{\ell m}(1)|,
\]
with strict second inequality unless \(r=1\). At \(r=1\), the sign of \(c_{\ell m}(1)\) is \((-1)^{\ell m-1}\); setting \(m(\tau+\varphi)\equiv m\pi\pmod{2\pi}\) makes each cosine equal \((-1)^{\ell m}\), so all summands are negative and the upper bound is attained. This condition is exactly that some sample is a zero of \(a+bz\). Conversely, equality in the absolute-value triangle inequality forces each nonzero summand to have the same maximal phase. Its negative case forces \(\cos(m(\tau+\varphi))=(-1)^m\) and hence a sampled zero. Its positive case is impossible: the first harmonic would force \(\cos(m(\tau+\varphi))=(-1)^{m-1}\), and then the second harmonic has cosine one while \(c_{2m}(1)<0\). This proves the complete equality classification, including \(m=1\).

**Exact coefficients.** A beta integral (equivalently the Rodrigues formula at \(r=1\)) evaluates
\[
c_k(1)=2^{-s}\frac{\Gamma(2s+1)}{\Gamma(s-k+1)\Gamma(s+k+1)},\quad k\ge0.
\]
Using the reflection identity for Gamma yields
\[
\frac{|c_k(1)|}{c_0(1)}=\frac{\Gamma(1+s)^2\sin(\pi s)}{\pi}\frac{\Gamma(k-s)}{\Gamma(k+s+1)},\qquad k\ge1.
\]
Substitution establishes the claimed exact series. The standard Gamma-ratio limit \(\Gamma(x-s)/\Gamma(x+s+1)\sim x^{-(2s+1)}\), together with uniform summable power bounds for \(x\ge1\), allows dominated convergence over \(\ell\ge1\), giving the sharp \(\zeta(p+1)\) coefficient. At \(m=1\), the extremizer has a sampled zero, so \(Q=0\) and the exact error is one.

## Verification
A standalone standard-library checker in `CHECKER.py` calculates the integral for balanced coefficients from the beta integral, verifies the exact zero-on-grid finite-grid errors and Fourier-sign formulas, and tests the sharp envelope against many nonbalanced complex-coefficient examples using numerical integration. Its finite checks are supplementary and do not replace the infinite-series or global-maximality arguments above. The proof establishes all integers \(m\ge1\) and the complete complex-coefficient domain.

## Relationship to prior work
Feng Dai and Egor Kosov, *Empirical approximation of \(L^p\) norms for \(p\in(1,2)\)*, arXiv:2611.05930v1 (public 4 November 2026), prove random-sampling discretization for arbitrary finite-dimensional subspaces, including complex ones, under a boundedness hypothesis. Their stated results control sample size by general dimension and error, and do not give this deterministic regular-polygon equality classification or its exact constant. The standard trapezoidal Fourier-aliasing identity is used as a known ingredient, not asserted as original. The new assertion is the global optimization over all complex linear binomials and the strict rigidity of extremizers together with the Gamma-series constant.

## Limitations
The result is restricted to two complex Fourier modes and equal-weight regular circular grids, with \(1<p<2\). It does not determine the optimal choice among arbitrary discrete sampling designs, does not generalize its equality geometry to higher degrees, and does not establish a corresponding universal minimax rate. A pre-existing equivalent reformulation in classical periodic quadrature or polynomial-norm literature remains possible; the available bibliographic and research-record comparisons do not constitute a mathematical proof of novelty. No independent mathematical audit has been performed.

## References
1. F. Dai and E. Kosov, *Empirical approximation of \(L^p\) norms for \(p\in(1,2)\)*, arXiv:2611.05930v1, 4 November 2026, https://arxiv.org/html/2611.05930v1.
2. L. N. Trefethen and J. A. C. Weideman, *The Exponentially Convergent Trapezoidal Rule*, SIAM Review 56 (2014), 385–458; https://ora.ox.ac.uk/objects/uuid:b82a6442-da54-4595-a3e9-688b4048facc. Background on trapezoidal Fourier aliasing; its exponentially analytic regime differs from the present endpoint cusp.
3. R. F. Bass and K. Gröchenig, *Random Sampling of Multivariate Trigonometric Polynomials*, SIAM Journal on Mathematical Analysis 36 (2004/05), https://doi.org/10.1137/S0036141003432316. Context for polynomial sampling, not the present equality classification.
