# Sharp one-erasure gradient frames for quadratic spherical harmonics on regular simplices

## Finding

Fix an integer \(d\ge3\), and choose the \(d+1\) vertices \(u_1,\ldots,u_{d+1}\in S^{d-1}\) of a regular simplex, normalized by \(u_i\cdot u_j=-1/d\) for \(i\ne j\). Let \(\mathcal H_2\) be the complex exact-degree-two spherical-harmonic space, and let \(S\) be a nonempty subset of the vertices. Define the derivative-only observation form
\[
\langle T_Sf,f\rangle_{\mathcal D}=\frac{1}{|S|}\sum_{u\in S}\|\nabla_{S^{d-1}}f(u)\|^2,
\qquad\|f\|_{\mathcal D}^2=\int_{S^{d-1}}\|\nabla_{S^{d-1}}f(x)\|^2\,d\sigma(x),
\]
where \(d\sigma\) is probability-normalized sphere area, and the operator \(T_S\) is defined through the corresponding Hilbert-space inner product. Thus its eigenvalues are squared singular values for gradient measurements with mean-squared sample norm and Dirichlet source norm.

**All erasure counts.** For \(1\le k=|S|\le d\), every subset has nullity exactly
\[
\dim\ker T_S=\frac{(d-k)(d-k+1)}2.
\]
For \(k=d+1\) the kernel is zero. Consequently, any one vertex may be erased without loss of injectivity, whereas deletion of two or more vertices always destroys injectivity.

**Sharp one-erasure spectrum.** If \(|S|=d\), set
\[
L_d=\frac{(d+1)(d+2)}{d^3},\quad H_d=\frac{(d+1)(d+2)}{d^2},\quad
\lambda_{\pm,d}=\frac{d+2}{4d^3}\left(d^2+4d+2\pm\sqrt{d^4+12d^2+16d+4}\right).
\]
The complete spectrum, with algebraic multiplicities, is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
\lambda_{-,d}&d-1\\
L_d&1\\
\lambda_{+,d}&d-1\\
H_d&d(d-3)/2
\end{array}
\]
(the final branch has multiplicity zero for \(d=3\)). The four displayed values are strictly ordered as written for every \(d\ge3\). They are positive, and \(\lambda_{-,d}\) is always the sharp lower squared singular value. The sharp squared condition number is \(\lambda_{+,3}/\lambda_{-,3}\) at \(d=3\), and \(H_d/\lambda_{-,d}\) at \(d\ge4\); in particular, its ratio to \(d\) tends to one as \(d\to\infty\).

For comparison only, the full \(d+1\)-vertex frame has eigenvalues \((d+2)/d^2\) with multiplicity \(d\), and \((d+2)/d\) with multiplicity \((d+1)(d-2)/2\). The original contribution is the exact erasure classification and the explicit one-deletion spectrum, not this full-vertex two-level calculation.

## Assumptions and scope

The field is complex; the arguments apply to the real subspace and then complexify. The dimension \(d\ge3\) is arbitrary. Every surviving vertex is assigned equal weight \(1/|S|\), independent of which original vertex was removed. The sampled quantity is the full intrinsic tangent gradient, not the scalar value, its normal derivative, or a subset of gradient coordinates. The domain is precisely \(\mathcal H_2\), not all polynomials of degree at most two. Condition numbers refer to ratios of positive squared singular values, except that zero eigenvalues are explicitly identified when there are at least two erasures.

## Proof

**(1) Quadratic representation and normalization.** Each \(f\in\mathcal H_2\) is uniquely \(f_A(x)=x^{\mathsf T}Ax\) with a complex symmetric trace-zero \(d\times d\) matrix \(A\). Equip this matrix space \(\mathcal M\) with Frobenius Hermitian norm. Standard fourth moments on the sphere and the degree-two Laplacian eigenvalue \(2d\) give
\[
\int|f_A|^2\,d\sigma=\frac{2\|A\|_F^2}{d(d+2)},\qquad
\|f_A\|_{\mathcal D}^2=\frac{4\|A\|_F^2}{d+2},\qquad
\nabla_Sf_A(u)=2(I-uu^{\mathsf T})Au.
\]
Hence \(T_S\) corresponds on \(\mathcal M\) to
\[
\langle T_SA,A\rangle_F=\frac{d+2}{|S|}\sum_{u\in S}\left(\|Au\|^2-|u^{\mathsf T}Au|^2\right).
\]
All formulas hold for complex matrices because the absolute squares use Hermitian norms.

**(2) Exact kernel for any erasures.** A gradient vanishes at \(u_i\) exactly when \(Au_i\) is a scalar multiple of \(u_i\). For a complex symmetric \(A\), eigenvectors with distinct eigenvalues are orthogonal for the bilinear form \(v^{\mathsf T}w\). Since any two simplex vertices have nonzero bilinear inner product \(-1/d\), all \(k\) sampled vertices must carry a single common eigenvalue \(\mu\). Any \(k\le d\) simplex vertices are linearly independent; their span \(U\) is a nondegenerate Euclidean subspace, and symmetry forces the decomposition \(A=\mu I_U\oplus B\) on \(U\oplus U^\perp\). With \(r=d-k\), the trace condition determines \(\mu=-\operatorname{tr}(B)/k\), leaving the full \(r(r+1)/2\)-dimensional complex symmetric space for \(B\). This proves the nullity formula. The case \(k=d+1\) follows from any \(d\) sampled vertices.

**(3) Full-frame operator.** Put \(Q(A)=(u_i^{\mathsf T}Au_i)_{i=1}^{d+1}\). Simplex isotropy \((d+1)^{-1}\sum u_iu_i^{\mathsf T}=I/d\) yields
\[
T_{\mathrm{all}}=(d+2)\left(\frac1d I-\frac{1}{d+1}Q^*Q\right).
\]
With \(B_i=u_i u_i^{\mathsf T}-I/d\), the projector Gram matrix is \(\langle B_i,B_j\rangle_F=(u_i\cdot u_j)^2-1/d\). It vanishes on the all-ones vector and equals \(\rho_d=(d^2-1)/d^2\) times the identity on its orthogonal complement. Therefore \(\mathcal M=V\oplus W\), where \(V=\operatorname{span}\{B_i\}\), \(\dim V=d\), \(W=\ker Q\), and \(\dim W=(d+1)(d-2)/2\). The full-frame operator has \(a_d=(d+2)/d^2\) on \(V\) and \(b_d=(d+2)/d\) on \(W\).

**(4) Exact effect of deleting one vertex.** Write \(u=u_{d+1}\), and let
\[
E_u=\{(uv^{\mathsf T}+vu^{\mathsf T})/\sqrt2:v\perp u\}\subset\mathcal M.
\]
For its orthogonal projection \(P_{E_u}\), the equality \(\|(I-uu^{\mathsf T})Au\|^2=\|P_{E_u}A\|_F^2/2\) gives the exact rank-\((d-1)\) downdate
\[
T_{S}=\frac{d+1}{d}T_{\mathrm{all}}-\frac{d+2}{2d}P_{E_u},\qquad S=\{u_1,\ldots,u_d\}.
\]
If \(v\perp u\) has norm one and \(A_v=(uv^{\mathsf T}+vu^{\mathsf T})/\sqrt2\), then \(u^{\mathsf T}A_vu=0\) and, for \(i\le d\), \(u_i^{\mathsf T}A_vu_i=-(\sqrt2/d)(u_i\cdot v)\). It follows from the tight-frame identity for the simplex that
\[
\|Q(A_v)\|^2=\frac{2(d+1)}{d^3},\qquad
\|P_VA_v\|_F^2=\frac{\|Q(A_v)\|^2}{\rho_d}=\alpha_d:=\frac{2}{d(d-1)}.
\]
Polarization gives \(P_{E_u}P_VP_{E_u}=\alpha_dP_{E_u}\). Since \(0<\alpha_d<1\), the \((d-1)\) tangent directions generate mutually orthogonal two-dimensional paired planes containing normalized projections into \(V\) and \(W\). On every such plane the erased frame has matrix
\[
\begin{pmatrix}L_d&0\\0&H_d\end{pmatrix}
-\frac{d+2}{2d}
\begin{pmatrix}
\alpha_d&\sqrt{\alpha_d(1-\alpha_d)}\\
\sqrt{\alpha_d(1-\alpha_d)}&1-\alpha_d
\end{pmatrix}.
\]
Its trace and determinant simplify respectively to
\[
\frac{(d+2)(d^2+4d+2)}{2d^3},\qquad
\frac{(d+1)(d+2)^2}{2d^4}.
\]
Thus its eigenvalues are \(\lambda_{-,d}\) and \(\lambda_{+,d}\). The unused parts of \(V\) and \(W\) have dimensions one and \(d(d-3)/2\) and yield \(L_d,H_d\). Since the downdate has nonzero components along both different baseline levels, rank-one interlacing is strict: \(\lambda_-<L_d<\lambda_+<H_d\). The kernel result from (2) proves positivity; the displayed determinant is also strictly positive. The multiplicities sum to \(\dim\mathcal M=(d-1)(d+2)/2\).

**(5) Sharp conditioning and asymptotics.** Because every eigenlevel is attained by the decomposition, the lower and upper levels give the sharp constants asserted. From the trace and determinant of the paired block, \(\lambda_{-,d}\sim d^{-1}\), while \(H_d\to1\), so the one-erasure squared condition number is asymptotic to \(d\). This completes the proof.

## Verification

The accompanying standalone `check.py` constructs a regular simplex and an independent explicit orthonormal basis of symmetric trace-zero matrices. It forms the actual tangential gradient measurement matrix and compares its complete numerical Gram spectrum to both the full-frame and one-erasure formulas for \(d=3,\ldots,9\). It separately verifies the exact kernel dimensions for every number \(1\le k<d\) of retained vertices. Run `python check.py` with NumPy and `python symbolic_check.py` with SymPy to confirm exact trace, determinant and discriminant identities. The calculations are finite corroboration only; the all-dimensional conclusions follow from the symbolic proof above.

## Relationship to prior work

- Allasia, Cavoretto and De Rossi (2017) study sphere/manifold Hermite–Birkhoff interpolation using cardinal basis functions and general derivative data. Their full accessible manuscript does not give the harmonic-subspace, gradient-only regular-simplex erasure spectrum.
- Adcock and Sui (2017) study gradient-augmented sparse approximation on tensor-product domains, with measurements of function values as well; their full accessible text does not concern this exact tangent-gradient frame or its erasures.
- Xiao and Zhuang (2023) provide a spherical-harmonic design objective and its gradient/Hessian, primarily specialized to the two-sphere, for design construction and framelets. Their HTML full text does not evaluate this gradient-only erasure spectrum.
- *Exact two-band Hessian and isotropic weighting for minimal spherical two-designs* (2026) explicitly determines a related un-erased regular-simplex two-band Hessian. Its quadratic-sector proof contains the full-node harmonic-gradient decomposition used here, so the full-sample spectrum is **not** a novelty claim. It does not state the arbitrary-erasure nullities, the one-erasure four-level spectrum, or the sharp surviving-frame constants.

## Limitations

The result treats only degree-two harmonics, equal weights on surviving simplex vertices, and observations of the complete intrinsic gradients. It is not a statement of full-gradient data interpolation for arbitrary tangent vector assignments (the data space is generally larger than the harmonic source). For two or more erasures there is a nontrivial nullspace, so no finite inverse norm on the full source space. The separate question of optimizing nonuniform weights after an erasure is not answered. Exact historical priority of the one-erasure spectral evaluation remains uncertain, particularly because frame-theoretic dual interpretations can hide equivalent calculations. No independent mathematical audit has been performed.

## References

1. G. Allasia, R. Cavoretto and A. De Rossi, *Hermite–Birkhoff interpolation on scattered data on the sphere and other manifolds*, arXiv:1705.01032v1, first posted 2017-05-02, https://arxiv.org/abs/1705.01032.
2. B. Adcock and Y. Sui, *Compressive Hermite interpolation: sparse, high-dimensional approximation from gradient-augmented measurements*, arXiv:1712.06645v1, first posted 2017-12-18, https://arxiv.org/abs/1712.06645.
3. Y. Xiao and X. Zhuang, *Spherical framelets from spherical designs*, arXiv:2303.05365v1, first posted 2023-03-09, https://arxiv.org/html/2303.05365v1.
4. *Exact two-band Hessian and isotropic weighting for minimal spherical two-designs*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-two-band-hessian-and-isotropic-weighting-for-minimal-spher--3be0a5399420.
