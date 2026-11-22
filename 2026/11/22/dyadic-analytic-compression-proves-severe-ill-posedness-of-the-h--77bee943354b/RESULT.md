# Dyadic analytic compression proves severe ill-posedness of the Hausdorff–Cesàro composite

## Finding

For the Hausdorff moment operator \(H:L^2(0,1)\to\ell^2(\mathbb N)\), and the diagonal compact operator \(D\), defined by
\[
(Hf)_n=\int_0^1 x^{n-1}f(x)\,dx,\qquad (Dy)_n=\frac{y_n}{n},\quad n\ge1,
\]
consider the compact composition \(T=DH\), equivalently the Hausdorff–Cesàro adjoint composition \(HC^*\). For every integer \(J\ge1\) there exists an explicit rank-at-most-\(J^2\) operator \(R_J\) satisfying
\[
\boxed{\|T-R_J\|_{L^2\to\ell^2}<8\,2^{-J}.}
\]
Consequently, its ordered singular values satisfy
\[
\boxed{s_{J^2+1}(T)\le8\,2^{-J},\qquad
s_n(T)\le16\exp\bigl(-\log2\,\sqrt{n-1}\bigr)\quad(n\ge1).}
\]
In particular, \(\lim_{n\to\infty}n^p s_n(T)=0\) for every real \(p>0\). Therefore the compact inverse problem governed by \(T\) is severely ill-posed, in the standard singular-value classification.

## Assumptions and scope

The source space is complex or real \(L^2((0,1),dx)\), with Lebesgue measure, and the target is standard \(\ell^2(\mathbb N)\). Rows are numbered from \(n=1\). The operator \(C^*\) is the continuous Cesàro adjoint for which the established identity \(HC^*=DH\) holds. The claim concerns infinite-dimensional singular values, not eigenvalues of a fixed finite section. No asymptotic equivalence or lower stretched-exponential bound is asserted.

## Proof

**1. Analytic row family.** For \(\operatorname{Re}z>1/2\), define the \(L^2(0,1)\)-vector
\[
g_z(x)=\frac{x^{z-1}}{z}.
\]
This map is holomorphic with
\[
\|g_z\|_2=\frac1{|z|\sqrt{2\operatorname{Re}z-1}}.
\]
The \(n\)-th row of \(T\) is the functional induced by \(g_n\).

**2. A fixed ellipse works at every dyadic scale.** Let \(a=2^j\), for \(j\ge0\), and let \(z=\tfrac a2(3+t)\), with real \(-1\le t\le1\). The image of the Bernstein ellipse \(E_2\), of parameter \(\rho=2\), obeys \(\operatorname{Re}z\ge7a/8\). Because \(a\ge1\), one also has \(2\operatorname{Re}z-1\ge3a/4\). Thus throughout this ellipse
\[
\left\|g_{a(3+t)/2}\right\|_2\le M a^{-3/2},\qquad M=\frac{16}{7\sqrt3}.
\]
The Banach-valued analytic Chebyshev series has coefficients bounded by \(2M a^{-3/2}2^{-k}\) at degree \(k\ge1\). Its truncation \(p_{j,L}(t)\) through degree \(L-1\) therefore satisfies the uniform norm bound
\[
\sup_{t\in[-1,1]}\left\|g_{a(3+t)/2}-p_{j,L}(t)\right\|_2
\le4M a^{-3/2}2^{-L}.
\]
This statement follows by Cauchy's contour formula for Chebyshev coefficients and a geometric-series sum. It holds also for \(a=1\), where holomorphy is as an \(L^2\)-valued function rather than a pointwise-bounded family at \(x=0\).

**3. Low-rank construction.** Fix \(J\ge1\) and put \(L=J\). For the rows \(2^j\le n<2^{j+1}\), \(0\le j<J\), use the Chebyshev polynomial \(p_{j,J}(2n/2^j-3)\) instead of \(g_n\); set all rows with \(n\ge2^J\) to zero. Since each of the \(J\) dyadic row blocks is spanned by at most \(J\) coefficient vectors in \(L^2(0,1)\), the resulting \(R_J\) has rank at most \(J^2\). Rowwise summation yields
\[
\|T_{<2^J}-R_J\|_{\mathcal S_2}^2
\le(4M)^2 4^{-J}\sum_{j=0}^{J-1} 2^{-2j}
\le \frac43(4M)^2 4^{-J}.
\]
For the omitted rows, directly
\[
\|T_{\ge2^J}\|_{\mathcal S_2}^2
=\sum_{n\ge2^J}\frac1{n^2(2n-1)}
\le\sum_{n\ge2^J}n^{-3}
\le\frac32\,4^{-J}.
\]
The final inequality follows by comparing the series to its first term plus an integral. Therefore
\[
\|T-R_J\|\le \|T-R_J\|_{\mathcal S_2}
\le\left(\frac{8M}{\sqrt3}+\sqrt{\frac32}\right)2^{-J}
=\left(\frac{128}{21}+\sqrt{\frac32}\right)2^{-J}<8\,2^{-J}.
\]

**4. Singular values and severity.** The approximation-number characterization on Hilbert spaces gives \(s_{J^2+1}(T)\le\|T-R_J\|\). If \(n\ge2\), choose \(J=\lfloor\sqrt{n-1}\rfloor\) and use monotonicity of singular values to deduce
\[
s_n(T)\le8\,2^{-J}\le16e^{-(\log2)\sqrt{n-1}}.
\]
For \(n=1\), the same generous bound follows from \(\|T\|\le\|T\|_{\mathcal S_2}\), since \(\|T\|_{\mathcal S_2}^2=\sum_{n\ge1}1/[n^2(2n-1)]<2\). For every \(p>0\), \(n^p e^{-c\sqrt n}\to0\). This proves the stated classification, without establishing a sharp decay exponent.

## Verification

The standalone `verify.py` performs finite Cauchy–Hilbert matrix spectral diagnostics, Gauss-quadrature comparisons for the dyadic Chebyshev interpolation model, and direct checks of the explicit constants and row energy. Its finite tests are not substituted for the infinite-dimensional Chebyshev coefficient or approximation-number arguments above. The construction used in the proof is the Chebyshev **series truncation**, whereas the script employs finite interpolation as a supplementary diagnostic only.

## Relationship to prior work

Kindermann and Hofmann (first public preprint 26 January 2024) identify \(T=DH=HC^*\), show compactness, establish \(s_n(T)=O(n^{-3/2})\) and an exponential-type lower bound, and explicitly leave the polynomial-versus-severe decay classification unresolved. The present estimate replaces the polynomial upper bound with a stretched-exponential one, settling that dichotomy in the severe direction. The 2021 Hofmann–Mathé and 2022 Gerth papers investigate the different composition \(HJ\) and do not entail this bound. The older weighted-Hilbert-matrix literature supplies general matrix context, not the stated uniform dyadic analytic rank estimate.

## Limitations

Only an upper singular-value bound is proved; no matching lower bound, sharp rate, spectral asymptotic constant, or stability estimate for numerical recovery is claimed. The exponent \(1/2\) here is a provable rate, not asserted optimal. The proof uses complex analytic approximation, but also applies on the real subspace by taking real Chebyshev coefficients.

## References

- S. Kindermann and B. Hofmann, *Curious ill-posedness phenomena in the composition of non-compact linear operators in Hilbert spaces*, arXiv:2401.14701 (first public 2024-01-26), Sections 4–5. https://arxiv.org/abs/2401.14701
- B. Hofmann and P. Mathé, *The degree of ill-posedness of composite linear ill-posed problems with focus on the impact of the non-compact Hausdorff moment operator*, arXiv:2111.01036 (2021). https://arxiv.org/abs/2111.01036
- D. Gerth, *A note on numerical singular values of compositions with non-compact operators*, arXiv:2201.13185 (2022). https://arxiv.org/abs/2201.13185
- E. Preissmann and O. Lévêque, *On generalized weighted Hilbert matrices*, arXiv:1303.1085 (2013). https://arxiv.org/abs/1303.1085
- F. Werner and B. Hofmann, *A unified concept of the degree of ill-posedness for compact and non-compact linear operator equations in Hilbert spaces under the auspices of the spectral theorem*, 2025. https://doi.org/10.1080/01630563.2025.2451922
