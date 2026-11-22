# Sharp two-coset Riesz bounds and exponentially small collision stiffness of geometric Laplace kernels

## Finding

Let \(h>0\), \(0<s<h\), and let \(\mathcal H=L^2(0,\infty;\mathbb C)\). For \(j\ge0\) and \(a\in\{0,1\}\), put \(s_0=0\), \(s_1=s\), and define
\[
u_{j,a}(t)=\sqrt{2e^{-jh-s_a}}\exp(-e^{-jh-s_a}t),\qquad t>0.
\]
Define, for \(\theta\in[-\pi,\pi]\),
\[
w_{h,\ell}(\theta)=\operatorname{sech}\!\left(\frac{\pi(\theta+2\pi\ell)}h\right),\quad
F_h(\theta)=\frac{2\pi}{h}\sum_{\ell\in\mathbb Z}w_{h,\ell}(\theta),\quad
G_{h,s}(\theta)=\frac{2\pi}{h}\sum_{\ell\in\mathbb Z} w_{h,\ell}(\theta)e^{i(\theta+2\pi\ell)s/h}.
\]
These uniformly convergent series give **the two exact optimal squared Riesz bounds** of the family \((u_{j,a})\):
\[
\boxed{A_h(s)=\min_{\theta\in[-\pi,\pi]}\{F_h(\theta)-|G_{h,s}(\theta)|\}>0,}
\]
\[
\boxed{B_h(s)=\sum_{k\in\mathbb Z}\left[\operatorname{sech}(kh/2)+\operatorname{sech}((kh+s)/2)\right].}
\]
Here optimal means that for every finitely supported complex coefficient array \((c_{j,a})\),
\[
A_h(s)\sum_{j,a}|c_{j,a}|^2\le\Big\|\sum_{j,a}c_{j,a}u_{j,a}\Big\|_{\mathcal H}^2\le B_h(s)\sum_{j,a}|c_{j,a}|^2,
\]
and neither squared constant can be improved.

As the two logarithmic scales coalesce, the optimal lower bound has a **sharp quadratic collision law**
\[
\boxed{A_h(s)=\mathcal C(h)s^2+O_h(s^4)\quad(s\downarrow0),}
\]
where, writing \(W_h(\theta)=\sum_\ell w_{h,\ell}(\theta)\) and \(p_{h,\theta}(\ell)=w_{h,\ell}(\theta)/W_h(\theta)\),
\[
\boxed{\mathcal C(h)=\frac{4\pi^3}{h^3}\min_{\theta\in[-\pi,\pi]}W_h(\theta)\operatorname{Var}_{p_{h,\theta}}(\ell)>0.}
\]
The coefficient has two **contrasting sharp density limits**:
\[
\boxed{\mathcal C(h)\sim\frac{16\pi^3}{h^3}e^{-2\pi^2/h}\quad(h\downarrow0),\qquad
\mathcal C(h)=\frac18+O(e^{-h/2})\quad(h\to\infty).}
\]
Thus two nearly coincident geometric Laplace sampling streams have quadratic loss of stability, but the quadratic coefficient is itself exponentially small at dense logarithmic sampling.

## Assumptions and scope

The sampling parameter \(h\) is any fixed positive real, and the offset is strictly between zero and one logarithmic period, \(0<s<h\). No completeness in all of \(L^2(0,\infty)\) is asserted: a Riesz sequence is a Riesz basis for its closed span, not necessarily a basis of the ambient space. All frame bounds here are **squared** bounds and use the exact normalization \(\|u_{j,a}\|_2=1\). The colliding-scale limit first fixes \(h\) and lets \(s\downarrow0\); only afterward are asymptotics for \(\mathcal C(h)\) taken. The dense and sparse logarithmic regimes are not claimed to be uniform in simultaneously varying \(h\) and \(s\).

## Proof

**Step 1: exact Gram kernel and Toeplitz reduction.** For all \(j,k\ge0\) and \(a,b\in\{0,1\}\), direct integration gives
\[
\langle u_{j,a},u_{k,b}\rangle
=\frac{2\sqrt{e^{-jh-s_a}e^{-kh-s_b}}}{e^{-jh-s_a}+e^{-kh-s_b}}
=\operatorname{sech}\!\left(\frac{(j-k)h+s_a-s_b}{2}\right).
\]
Hence the coefficient Gram is a positive, Hermitian block Toeplitz operator on \(\ell^2(\mathbb N_0;\mathbb C^2)\), with summable matrix coefficients. Put \(K(x)=\operatorname{sech}(x/2)\). The diagonal Fourier series is \(f_h(\theta)=\sum_{k\in\mathbb Z}K(kh)e^{ik\theta}\), and one off-diagonal series is \(g_{h,s}(\theta)=\sum_{k\in\mathbb Z}K(kh+s)e^{ik\theta}\). Its matrix symbol is Hermitian with diagonal entries \(f_h\) and off-diagonal entries \(g_{h,s},\overline{g_{h,s}}\); its eigenvalues are \(f_h\pm|g_{h,s}|\). The Fourier transform identity
\[
\int_{\mathbb R}\operatorname{sech}(x/2)e^{-i\xi x}\,dx=2\pi\operatorname{sech}(\pi\xi)
\]
and Poisson summation give \(f_h=F_h\) and \(g_{h,s}=\overline{G_{h,s}}\). Absolute and locally uniform convergence follows from the exponential decay of \(K\) and its transform.

**Step 2: strict lower positivity.** For each \(\theta\), the normalized weights \(p_{h,\theta}(\ell)\) are strictly positive for every integer \(\ell\). Consequently,
\[
\frac{|G_{h,s}(\theta)|}{F_h(\theta)}
=\left|\sum_{\ell\in\mathbb Z}p_{h,\theta}(\ell)e^{2\pi i\ell s/h}\right|<1,
\]
because equality in the triangle inequality would require all phases to agree, which fails for neighboring integers when \(0<s/h<1\). The continuous function \(F_h-|G_{h,s}|\) has a strictly positive minimum on the compact frequency circle, proving \(A_h(s)>0\).

**Step 3: optimal bounds.** The full-line Laurent operator with the symbol just described is unitarily equivalent to multiplication by that \(2\times2\) Hermitian symbol. The half-line Gram operator is its compression, so the pointwise spectral extrema give valid Riesz bounds. Conversely, take an eigenvector of the symbol at a frequency of extremum, multiply it by a long finite exponential wave \(e^{ij\theta}\) over indices \(j=N,\ldots,N+L-1\), and normalize it. As \(L\to\infty\), the Rayleigh quotient converges to the selected symbol eigenvalue, because the matrix coefficients are absolutely summable. Thus the extrema are the sharp half-line bounds, with no endpoint outliers. Moreover,
\[
f_h(\theta)\le f_h(0),\qquad |g_{h,s}(\theta)|\le g_{h,s}(0)
\]
by the triangle inequality applied to the nonnegative Fourier coefficients \(K(kh)\) and \(K(kh+s)\). Both inequalities are equalities at zero, so the optimal upper bound is \(B_h(s)=f_h(0)+g_{h,s}(0)\), the claimed convergent scalar series.

**Step 4: quadratic collision coefficient.** Let \(\omega_\ell=(\theta+2\pi\ell)/h\). The ratio \(G_{h,s}/F_h\) is the characteristic function of the discrete probability distribution \(p_{h,\theta}\) at argument \(s\). Its modulus has, uniformly in \(\theta\in[-\pi,\pi]\), the Taylor expansion
\[
\left|\sum_\ell p_{h,\theta}(\ell)e^{is\omega_\ell}\right|
=1-\tfrac{s^2}{2}\operatorname{Var}_{p_{h,\theta}}(\omega_\ell)+O_h(s^4).
\]
For rigor, the aliases have uniformly bounded exponential moments on the compact frequency circle, and the squared modulus is a real analytic even function of \(s\), uniformly bounded away from zero for sufficiently small \(s\). Since
\[
\operatorname{Var}(\omega_\ell)=(2\pi/h)^2\operatorname{Var}(\ell),
\]
we obtain, uniformly in \(\theta\),
\[
F_h(\theta)-|G_{h,s}(\theta)|
=s^2\frac{4\pi^3}{h^3}W_h(\theta)\operatorname{Var}_{p_{h,\theta}}(\ell)+O_h(s^4).
\]
Taking a minimum preserves the uniform remainder and proves the formula for \(\mathcal C(h)\). Every variance is strictly positive (all integer weights are positive), so the minimum is strictly positive.

**Step 5: dense-log-grid asymptotic.** Set \(a=2\pi^2/h\) and \(y=\theta/(2\pi)\). By symmetry it suffices to consider \(0\le y\le1/2\). Write \(v_k(y)=\operatorname{sech}(a(k+y))\) and
\[
E_a(y)=\frac{\sum_{k<l}(k-l)^2v_k(y)v_l(y)}{\sum_k v_k(y)}.
\]
This identity is exactly \(W_h\operatorname{Var}_p(\ell)\). At \(y=0\), \(v_0=1\), \(v_{\pm1}=2e^{-a}(1+o(1))\), and all further terms have exponentially smaller effect; hence
\[
E_a(0)=4e^{-a}(1+o(1)).
\]
For \(0\le y\le1/4\), the alias \(k=0\) dominates uniformly, \(\sum_k v_k=v_0(1+o(1))\). The pair terms involving \(0\) and \(\pm1\) therefore imply
\[
E_a(y)\ge (1-o(1))(v_{-1}(y)+v_1(y))
\ge(4-o(1))e^{-a}\cosh(ay)\ge(4-o(1))e^{-a}.
\]
For \(1/4\le y\le1/2\), the two closest aliases \(0,-1\) give \(E_a(y)\ge v_0v_{-1}/\sum_kv_k\). Uniformly in this range \(\sum_k v_k\le(2+o(1))v_0\), whereas \(v_{-1}\ge c e^{-3a/4}\) for an absolute \(c>0\). Thus \(E_a(y)\gg e^{-3a/4}\gg e^{-a}\). Combining both ranges yields \(\min_yE_a(y)=4e^{-a}(1+o(1))\), proving
\[
\mathcal C(h)\sim (4\pi^3/h^3)4e^{-2\pi^2/h}.
\]

**Step 6: sparse-log-grid asymptotic.** The direct Fourier series is more efficient here. Uniformly in \(\theta\), exponential decay of \(K\) and its first two derivatives gives
\[
f_h(\theta)=1+O(e^{-h/2}),\quad
\partial_s g_{h,s}(\theta)|_{s=0}=O(e^{-h/2}),\quad
\partial_s^2g_{h,s}(\theta)|_{s=0}=-\tfrac14+O(e^{-h/2}).
\]
(The leading second derivative is \(K''(0)=-1/4\), while \(K'(0)=0\).) Expanding the modulus, the coefficient of \(s^2\) in \(f_h-|g_{h,s}|\) is
\[
-\frac12\left(\partial_s^2g_{h,s}(\theta)|_{s=0}+\frac{|\partial_sg_{h,s}(\theta)|_{s=0}|^2}{f_h(\theta)}\right)
=\frac18+O(e^{-h/2})
\]
uniformly in \(\theta\). Its minimum has the same estimate, completing the proof.

## Verification

`check_two_coset.py` is a standalone diagnostic script using NumPy, SciPy, and mpmath. Run `python check_two_coset.py`. It tests direct Gram integrals against the hyperbolic-secant formula, compares the direct Fourier symbol with the Poisson alias sum (including the complex-conjugation convention), checks finite Gram principal sections and sharp upper extrema across three mesh widths and three relative offsets, and tests high-precision quadratic collision and both asymptotic regimes. The local check passed **208 finite assertions**. The infinite-dimensional Riesz property, sharpness, strict positivity, and double asymptotics are proved analytically above; numerical sampling is not treated as exhaustive.

## Relationship to prior work

Bailey, Gallardo-Gutiérrez and Partington (2026) study frames associated with continuous operator semigroups and establish structural frame criteria; their inspected manuscript does not give quantitative sharp Riesz bounds or small-offset asymptotics for interlaced geometric Laplace exponentials. A published theorem on a **single** geometric Szegő-kernel chain establishes exact theta-function spectral bounds independent of its starting depth. The balanced specialization \(s=h/2\) here is an equally spaced **single** geometric chain after reindexing, and its corresponding bounds are already established by the hyperbolic-secant Toeplitz analysis in that result, so no priority is claimed for that specialization. For generic \(s/h\), however, the union of two logarithmic cosets is not one equally spaced chain, and its block symbol, exact two-stream lower bound and quadratic collision stiffness are not consequences of the one-chain spectral statement alone. Standard Poisson summation and the Fourier transform of the hyperbolic secant are classical ingredients and are not claimed as new. Literature on two-coset Fourier exponential bases on unions of bounded intervals addresses oscillatory Fourier characters rather than positive-decay Laplace kernels, and its constants do not imply these formulas.

## Limitations

The sharp lower bound is given by an explicit rapidly convergent one-variable variational formula, not a closed-form minimizer for every \(h,s\). No assertion is made for irregular perturbations of either logarithmic lattice, general multi-coset unions, full spectral type, or a joint limit with \(s\) and \(h\) varying on a prescribed coupled scale. An older equivalent two-stream Poisson-symbol calculation may exist outside the inspected and searchable literature.

## References

1. V. Bailey, E. A. Gallardo-Gutiérrez and J. R. Partington, *Frames Associated with \(C_0\)-Semigroups*, arXiv:2611.13867v1, first public version November 10, 2026, especially Introduction and §§2–5. https://arxiv.org/html/2611.13867v1
2. *Exact theta-spectrum and no spectral outliers for geometric Hardy kernel chains*, public mathematical finding, November 2, 2026, full theorem and proof. https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-theta-spectrum-and-no-spectral-outliers-for-geometric-hard--f971bbe6cbe3/RESULT.md
3. Yu. Lyubarskii and I. Spitkovsky, *Sampling and interpolation for a lacunary spectrum*, Proceedings of the Royal Society of Edinburgh Section A (online 2011), abstract and scope. https://www.cambridge.org/core/journals/proceedings-of-the-royal-society-of-edinburgh-section-a-mathematics/article/abs/sampling-and-interpolation-for-a-lacunary-spectrum/6133A3EB1A4A9399C78E14B8FC5B993A
