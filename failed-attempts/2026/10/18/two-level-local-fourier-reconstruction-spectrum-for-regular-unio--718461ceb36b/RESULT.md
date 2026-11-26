# Two-level local Fourier reconstruction spectrum for regular unions of arcs

## Finding

**Theorem.** Fix an integer \(m\ge2\) and a duty fraction \(0<\alpha<1\). On the angular circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), define
\[
E_{m,\alpha}=\bigcup_{j=0}^{m-1}\left[\frac{2\pi j}{m},\frac{2\pi(j+\alpha)}{m}\right].
\]
The normalized Fourier coefficients of an arc union \(E\) are
\[
 c_k(E)=\frac{1}{2\pi}\int_E e^{-ik\theta}\,d\theta
 \qquad(k=1,\ldots,m-1).
\]
For sufficiently small *real* perturbations of the labeled starting and ending angles, of fixed total arc length, select the unique local common-rotation gauge by requiring both sums of perturbations to be zero. This slice has real dimension \(2m-2\). Viewed as a real linear map from Euclidean endpoint coordinates to \(\mathbb C^{m-1}\) with its standard real Euclidean norm, the Fourier moment Jacobian has exactly two squared singular values,
\[
 \boxed{\lambda_{\pm}(m,\alpha)=\frac{m}{4\pi^2}\bigl(1\pm|\cos(\pi\alpha)|\bigr),}
\]
each with multiplicity \(m-1\) (the two values coalesce at half duty). In particular it is an isomorphism at every interior duty fraction, and its exact linear condition number is
\[
 \boxed{\kappa(m,\alpha)=\sqrt{\frac{1+|\cos(\pi\alpha)|}{1-|\cos(\pi\alpha)|}}.}
\]
It is independent of the number of arcs and is minimized, with value \(1\), **only** at \(\alpha=1/2\).

Write \(h\) for a small gauge-fixed real endpoint perturbation and \(E(h)\) for the corresponding union of arcs. Then \(c_k(E_{m,\alpha})=0\) for every indicated frequency and, uniformly over all small nonzero \(h\),
\[
 \lambda_-\|h\|_2^2+O(\|h\|_2^3)
 \ \le\ \sum_{k=1}^{m-1}|c_k(E(h))|^2
 \ \le\ \lambda_+\|h\|_2^2+O(\|h\|_2^3).
\]
Both quadratic coefficients are optimal, witnessed infinitesimally by corresponding singular vectors. Thus the endpoint inverse problem has a locally sharp quadratic Fourier-energy stability constant, and the inverse function theorem gives local analytic recovery from precisely these \(m-1\) complex moments in the fixed-length, fixed-rotation slice. The statement is local, and makes no assertion about a global inverse or about perturbations with changing length.

## Assumptions and scope

All arcs are nonempty, disjoint, and labeled in cyclic order near the reference configuration. Their starts and ends are, respectively,
\[
 s_j=\frac{2\pi j}{m}+u_j,\qquad
 t_j=\frac{2\pi(j+\alpha)}m+v_j,
 \qquad 0\le j<m.
\]
Fixed normalized total measure means \(\sum_j(v_j-u_j)=0\), exactly, and selecting the closest common rotation means \(\sum_j(u_j+v_j)=0\), hence
\[
 T=\bigl\{(u,v)\in\mathbb R^{2m}:\sum_j u_j=\sum_j v_j=0\bigr\}.
\]
The domain norm is \(\|(u,v)\|_2^2=\sum_j(u_j^2+v_j^2)\). The codomain norm is \(\|z\|_2^2=\sum_{k=1}^{m-1}|z_k|^2\), without doubling conjugate frequencies. Every stated singular value refers to these choices; different Fourier or endpoint normalizations require corresponding factors.

## Proof

**1. Linearization.** An endpoint integration gives, for every nonzero integer \(k\),
\[
 c_k(E)=\frac{1}{2\pi ik}\sum_{j=0}^{m-1}
 \left(e^{-iks_j}-e^{-ikt_j}\right).
\]
Consequently the derivative at zero is
\[
 (Dc_k)_0(u,v)=\frac1{2\pi}\sum_{j=0}^{m-1}
 e^{-2\pi ikj/m}\left(e^{-2\pi ik\alpha/m}v_j-u_j\right).
\]
As each geometric series with frequency \(1\le k\le m-1\) vanishes, all reference low moments vanish.

**2. Exact Fourier decomposition of the real tangent.** Put \(\zeta=e^{2\pi i/m}\), \(\delta=2\pi\alpha/m\), and use *unnormalized* discrete Fourier coordinates
\[
 U_k=\sum_{j=0}^{m-1}\zeta^{-kj}u_j,
 \qquad V_k=\sum_{j=0}^{m-1}\zeta^{-kj}v_j.
\]
Since \(u,v\) are real and have zero mean, \(U_0=V_0=0\), \(U_{m-k}=\overline{U_k}\), \(V_{m-k}=\overline{V_k}\), and Parseval reads
\[
 \|(u,v)\|_2^2=\frac1m\sum_{k=1}^{m-1}
 \bigl(|U_k|^2+|V_k|^2\bigr).
\]
For every index \(1\le k<m/2\), combine the output at \(k\) with the complex conjugate output at \(m-k\). Exactly,
\[
 2\pi\begin{pmatrix}Dc_k\\overline{Dc_{m-k}}\end{pmatrix}
 =B_k\begin{pmatrix}U_k\\V_k\end{pmatrix},
 \qquad B_k=\begin{pmatrix}-1&e^{-ik\delta}\\-1&e^{i(m-k)\delta}\end{pmatrix}.
\]
The Hermitian Gram matrix \(B_k^*B_k\) has diagonal \(2,2\), and its off-diagonal entry has modulus
\[
 |e^{-ik\delta}+e^{i(m-k)\delta}|=2|\cos(m\delta/2)|
 =2|\cos(\pi\alpha)|.
\]
Its eigenvalues are therefore \(2(1\pm|\cos(\pi\alpha)|)\). Each of the pair's real Euclidean squared input norms is \(\frac2m(|U_k|^2+|V_k|^2)\), whereas the real output squared norm is \(\frac1{4\pi^2}\|B_k(U_k,V_k)^T\|^2\). Their quotient gives precisely \(\lambda_\pm\), each with *real* multiplicity two for that paired block.

For even \(m\), the unpaired self-conjugate index \(k=m/2\) has real \(U_k,V_k\). Its complex output is \((-U_k+e^{-i\pi\alpha}V_k)/(2\pi)\), with real quadratic Gram eigenvalues \(1\pm|\cos(\pi\alpha)|\) in the real variables \(U_k,V_k\). Since the corresponding input contribution is \((U_k^2+V_k^2)/m\), its squared singular values again equal \(\lambda_\pm\), each once. Summing paired indices and the optional self-conjugate one yields exactly \(m-1\) eigenvectors of each sign (\(2m-2\) total). In particular \(\lambda_->0\) for \(0<\alpha<1\).

**3. Sharp local inverse stability.** Endpoint integration is real analytic near this fixed disjointness pattern, so for \(h\in T\) we have
\[
 (c_k(E(h)))_{k=1}^{m-1}=Jh+O(\|h\|_2^2).
\]
Squaring the norm gives \(\|Jh\|_2^2+O(\|h\|_2^3)\). The proven spectral bounds for \(J\) imply the displayed sharp inequalities. Taking \(h\) in a unit least- or most-singular eigendirection and replacing it by \(\varepsilon h\), with \(\varepsilon\downarrow0\), proves that neither leading constant can be improved. The square map from the real dimension \(2m-2\) slice to the real dimension \(2m-2\) complex-moment space has invertible derivative \(J\); the analytic inverse function theorem supplies a local inverse.

Finally, the ratio of the positive singular values is the displayed \(\kappa\). It equals one exactly when \(\cos(\pi\alpha)=0\), equivalently \(\alpha=1/2\) in the stipulated interval. Near either endpoint the condition number diverges, reflecting the merging of complementary starts and ends.

## Verification

The independent numerical implementation `verify_jacobian.py` constructs the real Fourier Jacobian directly from endpoint derivatives, computes an orthonormal basis of the two endpoint-sum constraints, and performs its singular-value decomposition. It compares this independently assembled matrix with the closed formula for each of nine arc counts and five duty fractions: **45 configurations passed**, with maximal permitted absolute error \(2\cdot10^{-12}\). It also verifies the vanishing reference low moments and finite-difference differentiation against direct endpoint Fourier integration. These finite tests check the normalization and algebraic derivation, but the proof of the arbitrary-\(m\) theorem is the preceding exact discrete-Fourier calculation. Run `python verify_jacobian.py` with Python 3, NumPy and SciPy installed.

## Relationship to prior work

Courtney (2010) proves global recovery of a union of at most \(m\) arcs from its Fourier partial sum through order \(m\) and gives an endpoint-reconstruction algorithm; that is an earlier qualitative reconstruction result. The present statement instead computes the **complete sharp real differential spectrum**, for **frequencies only through \(m-1\)**, with a fixed-measure and rotation-gauge restriction, at the regular \(m\)-arc configuration. It does not claim Courtney's recovery theorem.

Batenkov, Demanet, Goldman and Yomdin (2018/2019) study lower singular-value bounds for general clustered-node partial Fourier/Vandermonde matrices, including asymptotic superresolution estimates. Their matrix has different sampling and normalization, and their statements do not yield the exact pair of real singular values and the half-duty isometry in this constrained endpoint-reconstruction problem.

Jiang (2026) studies one-dimensional oscillation and low-Fourier-mode uncertainty principles. The alternating regular-arc indicator motivates a complementary *local inversion* question; the oscillation inequalities themselves neither give nor require the singular-value calculation here.

## Limitations

This is an exact **local** inverse and condition-number result, not global recovery, noise robustness beyond the local differential regime, or optimality among arbitrary placement of \(m\) arcs. Endpoints must remain separated and the exact fixed-measure and rotation-gauge constraints must be imposed. No global uniqueness, stronger regularity, or independent external validation is asserted. Literature priority beyond the sources actually inspected remains open to additional checking.

## References

1. F. Jiang, *On a family of one-dimensional oscillation inequalities*, arXiv:2608.04639 (first public version 2026-08-05), https://arxiv.org/abs/2608.04639.
2. D. Courtney, *Unions of arcs from Fourier partial sums*, arXiv:1002.0639 (2010), https://arxiv.org/html/1002.0639v2.
3. D. Batenkov, L. Demanet, G. Goldman, and Y. Yomdin, *Conditioning of partial nonuniform Fourier matrices with clustered nodes*, arXiv:1809.00658 (first version 2018; revised 2019), https://arxiv.org/html/1809.00658v2.
