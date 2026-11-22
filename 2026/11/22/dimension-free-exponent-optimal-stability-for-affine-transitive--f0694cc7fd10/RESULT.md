# Dimension-free, exponent-optimal stability for affine-transitive Fourier synthesis

## Finding

Let \(G\) be a finite abelian group of cardinality \(M\), let \(S\subseteq G\) be nonempty, and suppose a group \(\Gamma\) of affine automorphisms of \(G\) preserves \(S\) and acts transitively on it. For any real \(1<r<\infty\), use the unitary Fourier transform and counting \(\ell^r\) norms, and put
\[
\mathcal C_r(S)=\frac{M^{-1/2}|S|}{\|\widehat{\mathbf1_S}\|_r}.
\]
For every nonzero complex \(f\) supported in \(S\), set the (exact) synthesis deficit
\[
\delta=1-\frac{\|\widehat f\|_\infty}{\mathcal C_r(S)\|\widehat f\|_r}\in[0,1).
\]
There are a character \(\chi\in\widehat G\) and a nonzero scalar \(c\) such that
\[
\frac{\|\widehat{f-c\chi\mathbf1_S}\|_r}{\|\widehat f\|_r}
\le
\begin{cases}
2\left(\dfrac{1-(1-\delta)^2}{r-1}\right)^{1/2},&1<r<2,\\[5pt]
\left(1-(1-\delta)^2\right)^{1/2},&r=2,\\[5pt]
2\left(1-(1-\delta)^r\right)^{1/r},&2<r<\infty.
\end{cases}
\]
The implicit small-deficit powers \(1/2\) for \(1<r\le2\) and \(1/r\) for \(r>2\) are optimal among bounds uniform over all finite abelian groups and affine-transitive supports, even allowing the best \(c,\chi\). No power strictly larger can replace either.

## Assumptions and scope

An affine automorphism has the form \(x\mapsto A(x)+b\), where \(A\) is a group automorphism. The Fourier transform is \(\widehat f(\xi)=M^{-1/2}\sum_{x\in G}f(x)\overline{\xi(x)}\). Norms \(\|\cdot\|_r\) are counting norms over the dual group. A character \(\chi\) has modulus one. The sharp constant \(\mathcal C_r(S)\) and the equality cases are the previously established affine-symmetry theorem of Iosevich–Li–Yu; the new assertion is a uniform quantitative near-equality bound with optimal powers. The result is valid for every finite abelian group, all allowed \(r\), and arbitrary nonempty transitive \(S\), including a singleton.

## Proof

**1. The extremizing orbit average.** Choose \(\chi_0\in\widehat G\) where \(|\widehat f|\) is maximal, and let \(g=\overline{\chi_0}f\). Then \(\widehat g(1)=\widehat f(\chi_0)\). Average \(g\) over the affine symmetries:
\[
h(x)=\frac1{|\Gamma|}\sum_{T\in\Gamma}g(Tx)
=\frac1{|S|}\Big(\sum_{x\in S}g(x)\Big)\mathbf1_S(x)
=c\mathbf1_S(x),\qquad
c=\frac{M^{1/2}\widehat f(\chi_0)}{|S|}.
\]
Transitivity gives the second equality; \(c\ne0\). Let \(R=\|\widehat f\|_r>0\). Affine changes of variables send the Fourier transform to a phase times a permutation, so all vectors \(X_T=\widehat{g\circ T}\) have norm \(R\). Their average is \(H=\widehat h\), and by the sharp-constant formula
\[
\|H\|_r/R=\frac{M^{1/2}|\widehat f(\chi_0)|\|\widehat{\mathbf1_S}\|_r}{|S|R}=1-\delta.
\]
For \(r=2\), orbit averaging is an orthogonal projection on the time domain (and therefore after the unitary Fourier transform), so \(\|\widehat{g-h}\|_2^2=R^2-\|H\|_2^2\), giving the asserted identity.

**2. Pairwise convexity.** If \(2<r<\infty\), Clarkson's inequality for complex counting \(\ell^r\) says
\[
\left\|\frac{U+V}{2}\right\|_r^r+
\left\|\frac{U-V}{2}\right\|_r^r
\le\frac{\|U\|_r^r+\|V\|_r^r}{2}.
\]
If \(1<r<2\), the sharp Ball–Carlen–Lieb inequality (also formulated in Ricard–Xu) says
\[
\left\|\frac{U+V}{2}\right\|_r^2+(r-1)
\left\|\frac{U-V}{2}\right\|_r^2
\le\frac{\|U\|_r^2+\|V\|_r^2}{2}.
\]
Both hold for complex vectors and require no Fourier-specific assumption. In either case write \(s=r\) and \(\beta=1\) in the first range, or \(s=2\), \(\beta=r-1\) in the second. Applying the appropriate inequality to \(X_T,X_U\) and averaging independently over uniform \(T,U\in\Gamma\), Jensen's inequality implies
\[
\beta 2^{-s}\mathbb E_{T,U}\|X_T-X_U\|_r^s
\le R^s-\mathbb E_{T,U}\Big\|\frac{X_T+X_U}{2}\Big\|_r^s
\le R^s-\|H\|_r^s.
\]
Because \(X_T\) is the image of \(X_{\mathrm{id}}\) under an isometric group representation, \(\mathbb E_{T,U}\|X_T-X_U\|_r^s=\mathbb E_U\|X_{\mathrm{id}}-X_U\|_r^s\). Also \(X_{\mathrm{id}}-H=\mathbb E_U(X_{\mathrm{id}}-X_U)\), hence Jensen gives
\[
\|\widehat{g-h}\|_r^s\le \mathbb E_U\|X_{\mathrm{id}}-X_U\|_r^s
\le \frac{2^s}{\beta}\big(R^s-\|H\|_r^s\big).
\]
Divide by \(R^s\), substitute \(\|H\|_r/R=1-\delta\), and undo modulation. This proves the claimed bounds.

**3. The powers cannot improve.** For \(r>2\), choose \(G=\mathbb Z_7\), \(S=G\), a nontrivial character \(\eta\), and \(f_t=\mathbf1_G+t\eta\) for \(0<t<1\). Since \(\mathcal C_r(G)=1\) and \(\widehat f_t\) is supported on two distinct frequencies, the exact deficit is
\[
\delta_t=1-(1+t^r)^{-1/r}\sim t^r/r.
\]
The best relative \(\ell^r\)-distance to any scalar-modulated indicator is exactly \(t(1+t^r)^{-1/r}\), so the exponent \(1/r\) is necessary.

For \(1<r\le2\), let \(G=\mathbb Z_3\), \(S=\{0,1\}\), and \(f_t(0)=1+t\), \(f_t(1)=1-t\), with \(f_t(2)=0\). The reflection \(x\mapsto1-x\) acts transitively on \(S\). For sufficiently small real \(t\), the maximal Fourier coefficient remains at the trivial frequency, while the other two Fourier magnitudes, before the common factor \(3^{-1/2}\), are \((1+3t^2)^{1/2}\). Thus
\[
\delta_t=1-\left(\frac{2^r+2}{2^r+2(1+3t^2)^{r/2}}\right)^{1/r}
=\frac{3}{2^r+2}t^2+O_r(t^4).
\]
The vector \((1+t,1-t,0)\) is at distance bounded below by a positive multiple of \(|t|\) from the union of all character-modulated, scalar indicator lines: the two nontrivial modulations stay separated at \(t=0\), and on the trivial-character line the antisymmetric perturbation is transverse. Fourier transformation is a fixed isomorphism of the three-dimensional space, so the same lower bound holds for the normalized Fourier \(\ell^r\)-distance. Hence no exponent above \(1/2\) works universally. At \(r=2\) the previous orthogonal-projection identity is exact.

## Verification

A standalone Python checker named `checker.py` implements direct normalized cyclic Fourier transforms and verifies the sharp synthesis ratio and the new near-equality bounds for random complex signals on three transitive families: full cycles, two-point reflection orbits, and even-residue subgroups. It includes exact-formula asymptotic tests for both optimal exponents. The proof above is for arbitrary finite abelian groups and does not depend on numerical enumeration. Its only non-elementary input is the established Ball–Carlen–Lieb two-uniform-convexity inequality; the named inequalities are not novel assertions.

## Relationship to prior work

Iosevich, Li and Yu (2026, Theorem 4.1) prove the sharp constant and characterize exact equality by modulated indicators, but their Section 10 explicitly asks for quantitative near-equality control and its dependence on the modulus. The present theorem supplies dimension- and modulus-independent Fourier-norm bounds and demonstrates sharpness of both exponents. Bhowmik, Deodhar and Iosevich (2025, revised 2026) establish general finite spectral-synthesis inequalities, not the near-equality estimate. Clarkson's inequalities, Ball–Carlen–Lieb uniform convexity, and the stronger abstract conditional-expectation inequalities of Ricard–Xu are previously known tools: their statements themselves are not claimed as new. In particular, the new argument is a Fourier-specific orbit-average application, not a new convexity theorem or a new evaluation of the sharp synthesis constant.

## Limitations

The constants displayed in the two non-Hilbert bounds are sufficient and are **not** claimed numerically optimal; only the exponents of the deficit are optimal in the indicated universal sense. The distance is measured in Fourier counting \(\ell^r\), normalized by \(\|\widehat f\|_r\); no uniform time-domain \(\ell^2\) estimate for \(r>2\) is asserted. The theorem requires affine transitivity and \(1<r<\infty\), and it does not treat nonsymmetric supports or \(r=1,\infty\). Bibliographic noncoverage is assessed against identified sources, not proved by search alone; possible older abstract formulations are a residual originality risk.

## References

1. A. Iosevich, Z. Li, K. Yu, *Spectral synthesis, Fourier extension, and arithmetic in* \(\mathbb Z_N^d\), arXiv:2609.25404, first posted 2026-09-21; v2, 2026-11-16, Theorem 4.1 and Section 10. https://arxiv.org/html/2609.25404v2
2. P. Bhowmik, S. Deodhar, A. Iosevich, *On spectral synthesis in* \(\mathbb Z_N^d\), arXiv:2508.12194, first posted 2025-08-17; v2, 2026-08-11. https://arxiv.org/html/2508.12194v2
3. J. A. Clarkson, *Uniformly convex spaces*, Transactions of the American Mathematical Society **40** (1936), 396–414. https://doi.org/10.2307/1989630
4. K. Ball, E. A. Carlen, E. H. Lieb, *Sharp uniform convexity and smoothness inequalities for trace norms*, Inventiones Mathematicae **115** (1994), 463–482. https://doi.org/10.1007/BF01231769
5. É. Ricard, Q. Xu, *A noncommutative martingale convexity inequality*, Annals of Probability **44** (2016), 867–882, Theorem 2. https://arxiv.org/abs/1405.0431
