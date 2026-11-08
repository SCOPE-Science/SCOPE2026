# Uniform rigidity of skew-min extremizers in real \(L^p\)

## Finding
Let \((\Omega,\mu)\) be a measure space admitting two disjoint measurable sets of finite positive measure, and let \(X=L^p(\mu;\mathbb R)\). For \(1\le p<\infty\), define
\[
\mathcal K_p(X)=\sup_{\substack{\|f\|_p=\|g\|_p=1\\r,s\ge0,\ r^2+s^2=1}}\min\{\|rf+sg\|_p,\|sf-rg\|_p\}.
\]
For \(p=\infty\), use the same definition with essential-supremum norms. Then
\[
\mathcal K_p(X)=2^{|1/p-1/2|},\qquad 1\le p\le\infty,
\]
where \(1/\infty=0\). This value follows from existing two-coordinate matrix-norm methods; the contribution here is the **complete equality and uniform near-equality geometry**:

* If \(1<p<2\), equality holds exactly when \(r=s=2^{-1/2}\) and \(f g=0\) almost everywhere.
* If \(2<p<\infty\), equality holds exactly when \(r=s=2^{-1/2}\), \(|f|=|g|\) almost everywhere, and
  \[\int_{\{fg\ge0\}}|f|^p\,d\mu=\int_{\{fg<0\}}|f|^p\,d\mu=\tfrac12.\]
* If \(p=2\), the value is one, and equality holds exactly when \(rs\langle f,g\rangle=0\).

More strongly, for any sequence of admissible quadruples \((f_n,g_n,r_n,s_n)\), where the underlying measure spaces may vary, the corresponding minima tend to \(2^{|1/p-1/2|}\) **if and only if** the following conditions hold:
\[
\begin{array}{ll}
1<p<2:& |r_n-s_n|+\|\min(|f_n|,|g_n|)\|_p\longrightarrow0;\\[2pt]
2<p<\infty:& |r_n-s_n|+\||f_n|-|g_n|\|_p+\left|\int\operatorname{sgn}(f_ng_n)|f_n|^p\,d\mu_n\right|\longrightarrow0.
\end{array}
\]
Here the sign at zero is set to zero. In particular the near-equality criterion is uniform over all real \(L^p\) spaces in the stated class, including nonatomic spaces and spaces of varying dimension.

At the quartic exponent there is additionally an **exact nonnegative defect decomposition**. For any real unit vectors \(f,g\in L^4\), set \(r=s=2^{-1/2}\). Then
\[
\boxed{\quad 2-\min\left\{\left\|\frac{f+g}{\sqrt2}\right\|_4^4,\left\|\frac{f-g}{\sqrt2}\right\|_4^4\right\}
=\frac34\int(f^2-g^2)^2\,d\mu+\left|\int fg(f^2+g^2)\,d\mu\right|.\quad}
\]
The two terms separately measure modulus mismatch and sign-balance bias. This identity gives the explicit sharp bound \(\||f|-|g|\|_4^4\le 4\,\mathrm{defect}/3\) at balanced coefficients.

## Assumptions and scope
All spaces and functions are **real**. The measure space must contain two disjoint sets of finite positive measure, to realize both types of exact witness; the proof of the upper bound and the rigidity implications do not require nonatomicity. The norm-one conditions are essential. The exponent used to normalize the scalar coefficients is always two, independent of the ambient exponent \(p\). The critical exponent \(p=2\) is treated separately, and no endpoint equality classification or stability assertion is claimed for \(p=1\) or \(p=\infty\).

## Proof
**1. The scalar sharp inequality.** For \(r,s\ge0\) with \(r^2+s^2=1\), write
\[M_{r,s}=\begin{pmatrix}r&s\\s&-r\end{pmatrix}.\]
This is an orthogonal matrix. On real \(\mathbb R^2\), the standard two-coordinate norm comparisons give
\[
\|M_{r,s}z\|_{\ell_p^2}\le K_p\|z\|_{\ell_p^2},\qquad K_p=2^{|1/p-1/2|},\quad 1\le p\le\infty.
\]
For \(1<p<2\), this follows from \(\|Mz\|_p\le 2^{1/p-1/2}\|Mz\|_2=K_p\|z\|_2\le K_p\|z\|_p\). For \(2<p<\infty\), reverse the positions of the two norm comparisons: \(\|Mz\|_p\le\|Mz\|_2=\|z\|_2\le K_p\|z\|_p\). These inequalities are also valid at the endpoints. Integrating the pointwise \(p\)-th-power estimate yields
\[
\|rf+sg\|_p^p+\|sf-rg\|_p^p\le2K_p^p.
\]
Therefore the minimum of the two output norms is at most \(K_p\). The \(p=\infty\) case follows instead by taking essential suprema of the pointwise bounds.

**2. Witnesses and value.** If \(1\le p<2\), choose disjointly supported unit functions \(f,g\) and \(r=s=1/\sqrt2\). Each output has norm \(2^{1/p-1/2}\). If \(2<p\le\infty\), choose normalized disjoint nonzero functions \(h_1,h_2\), and for finite \(p\) put \(f=2^{-1/p}(h_1+h_2)\), \(g=2^{-1/p}(h_1-h_2)\); for \(p=\infty\) omit the factor. At balanced coefficients both output norms are \(2^{1/2-1/p}\). For \(p=2\), orthogonal functions attain the bound. Thus the scalar constant is sharp.

**3. Pointwise equality and complete norming pairs.** Suppose \(1<p<2\). Equality in \(\|z\|_2\le\|z\|_p\) requires at most one nonzero component, while equality in \(\|Mz\|_p\le K_p\|Mz\|_2\) requires two output components of equal modulus. For nonzero \(z\) these conditions force \(z\) onto a coordinate axis and \(r=s=1/\sqrt2\). Suppose instead \(2<p<\infty\). Equality in \(\|z\|_2\le K_p\|z\|_p\) forces equal component moduli, while equality in \(\|Mz\|_p\le\|Mz\|_2\) forces one output component to vanish. Therefore \(z\) lies on one of the lines \(z_2=\pm z_1\) and again \(r=s=1/\sqrt2\). If the minimum of the two integrated output norms is \(K_p\), their \(p\)-th powers both equal \(K_p^p\), so the pointwise nonnegative scalar deficit vanishes almost everywhere. These conditions give disjoint supports below two and \(g=\pm f\) above two. In the latter case, the two output norm equalities force exactly half the \(p\)-mass onto each sign set. Conversely, the displayed conditions directly give equality. When \(p=2\), the two squared norms equal \(1\pm2rs\langle f,g\rangle\), proving the stated criterion.

**4. Uniform rigidity of maximizing sequences.** Let \(1<p<\infty\), \(p\ne2\), and suppose minima of admissible quadruples tend to \(K_p\). Set
\[
H_{r,s}(a,b)=K_p^p(|a|^p+|b|^p)-|ra+sb|^p-|sa-rb|^p\ge0.
\]
Step 1 gives
\[0\le\int H_{r_n,s_n}(f_n,g_n)\,d\mu_n\le2K_p^p-2\min(\|r_nf_n+s_ng_n\|_p,\|s_nf_n-r_ng_n\|_p)^p\longrightarrow0.\]
On the compact set \(r^2+s^2=1\), \(r,s\ge0\), \(|a|^p+|b|^p=1\), the zero set of \(H\) consists exactly of the balanced coefficients and the axes (\(p<2\)), respectively the two diagonals (\(p>2\)), by Step 3. Compactness implies, uniformly in the varying measure space, \(|r_n-s_n|\to0\). It also implies that the integral of the \(p\)-th power of the pointwise distance from \((f_n,g_n)\) to the corresponding union of lines tends to zero: normalize each nonzero input pair pointwise and integrate against the mass \((|f_n|^p+|g_n|^p)d\mu_n\), whose total mass is two. For \(p<2\), this distance controls \(\min(|f_n|,|g_n|)\), proving the first necessity assertion. For \(p>2\), it controls \(||f_n|-|g_n||\). Choosing the measurable sign \(\sigma_n=\operatorname{sgn}(f_ng_n)\), this yields \(\|g_n-\sigma_nf_n\|_p\to0\). The two nearly maximal output norms, together with \(r_n,s_n\to1/\sqrt2\), now force the positive- and negative-sign \(p\)-masses of \(f_n\) to tend to one half each, giving the signed-integral condition.

Conversely, if the subquadratic criteria hold, zeroing the smaller of \(|f_n|,|g_n|\) at each point produces disjoint approximants with vanishing \(L^p\) error; the balanced transform of disjoint unit inputs has both norms \(K_p\). If the superquadratic criteria hold, replace \(g_n\) by \(\sigma_nf_n\), again with vanishing \(L^p\) error. The signed-integral hypothesis puts asymptotically one half of the \(p\)-mass in each sign set, giving both balanced output norms \(K_p\). In either case continuity of the transform under \(|r_n-s_n|\to0\) proves convergence of the minima. This completes the *if and only if* sequence classification.

**5. Exact quartic deficit.** For unit real \(L^4\) functions and balanced coefficients, binomial expansion gives
\[
\frac12\left(\left\|\frac{f+g}{\sqrt2}\right\|_4^4+\left\|\frac{f-g}{\sqrt2}\right\|_4^4\right)=\frac12+\frac32\int f^2g^2,
\]
and half their difference equals \(\int fg(f^2+g^2)\). Use \(\min(a,b)=(a+b)/2-|a-b|/2\) and \(\int(f^2-g^2)^2=2-2\int f^2g^2\), obtaining the boxed formula. Pointwise \((|f|-|g|)^4\le(f^2-g^2)^2\) proves the stated quantitative bound. The coefficient \(3/4\) in the exact identity is not an estimated constant.

## Verification
The sharp scalar inequalities have complete analytic equality conditions, and the uniform-stability argument uses compactness only on the fixed two-dimensional scalar sphere; there is no compactness assumption on the function spaces. The standalone `verify.py` independently runs 5,514 finite assertions on the two-coordinate inequality, exact witnesses, and rational quartic expansions, with a fixed seed. The infinite-dimensional claim is proved in Steps 1–5; these finite tests are reproducibility diagnostics only.

## Relationship to prior work
The underlying invariant is the skew minimum-gauge specialization of the family defined by Du, Zhang, Fang and Liu (2026). Existing generalized James and skew-power-mean results already imply, by scalar matrix-norm estimates, the **value** of the skew-min constant on classical real \(L^p\); the numerical value is not put forward as independently novel. The contribution is the *complete classification of every maximizing pair*, the dimension-free *if and only if* characterization of every near-maximizing sequence on varying \(L^p\) spaces, and the exact quartic mismatch/bias identity. The 2026 Schäffer paper contains a different infimum problem and computes a supremal power-mean invariant using a two-coordinate matrix norm, but does not state this rigidity/stability classification. The closest available mathematical-record results likewise give sharp values or matrix reductions rather than these equality and near-equality structures.

## Limitations
The stability theorem is qualitative (a universal, measure-space-independent modulus follows from scalar compactness, but its best explicit rate is not calculated for general \(p\)). The quartic defect identity fixes balanced coefficients. Nothing is asserted about complex \(L^p\), general Banach spaces, or complete endpoint rigidity at \(p=1,\infty\). The general values are not claimed as a separate discovery. A broader prior stability theorem for norm extremizers of two-by-two real orthogonal transforms could overlap with the new rigidity statement; no absolute publication priority is claimed.

## References
1. Q. Du, W. Zhang, Z. Fang and Q. Liu, *Skew-Parameterized Geometric Constants in Banach Spaces*, arXiv:2608.00933v1 (first posted 2026-08-02), https://arxiv.org/html/2608.00933.
2. Y. Xu and Q. Liu, *Skew Schäffer Type Constants*, arXiv:2610.03050v1 (first posted 2026-10-02), https://arxiv.org/abs/2610.03050, especially Theorem 3.2.
3. Z. Rao, Q. Wu, Q. Liu, Q. Ni and Y. Wang, *The skew James type constant in Banach spaces*, arXiv:2504.00827v1 (first posted 2025-03-31), https://arxiv.org/abs/2504.00827.
4. A. Amini-Harandi and M. Rahimi, *On Some Geometric Constants in Banach Spaces*, Mediterr. J. Math. 16 (2019), article 99, https://doi.org/10.1007/s00009-019-1377-z.
5. X. Yang and C. Yang, *An inequality between \(L_{YJ}\) constant and generalized James constant*, Math. Inequal. Appl. 27 (2024), 571–581, https://doi.org/10.7153/mia-2024-27-39.
