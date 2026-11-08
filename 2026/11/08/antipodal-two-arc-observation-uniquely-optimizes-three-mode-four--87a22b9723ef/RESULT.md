# Antipodal two-arc observation uniquely optimizes three-mode Fourier stability

## Finding

On the circle \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), consider the three-frequency subspace \(H=\operatorname{span}\{e^{-it},1,e^{it}\}\). An observer measures its energy on two equal angular arcs of prescribed total length. Among **every admissible separation** of these arcs, opposite placement uniquely maximizes the worst-case observable fraction.

For each \(0<\beta<\pi/2\), the sharp value is
\[
\sup_{\beta\le\alpha\le\pi/2}\ \inf_{0\ne f\in H}
\frac{\int_{E_{\alpha,\beta}}|f(t)|^2\,dt}
{\int_{\mathbb T}|f(t)|^2\,dt}
=\frac{2\beta-\sin(2\beta)}{\pi},
\]
with equality in the outer optimization **only** at \(\alpha=\pi/2\). Interchange of the arcs and a common rotation do not change the design. The result includes an exact penalty for non-antipodal placement and the sharp comparison with one contiguous observation arc.

## Assumptions and scope

Identify angles modulo \(2\pi\). For \(0<\beta<\pi/2\) and \(\beta\le\alpha\le\pi/2\), let
\[
E_{\alpha,\beta}=[-\alpha-\beta,-\alpha+\beta]\cup[\alpha-\beta,\alpha+\beta]\quad(\bmod\ 2\pi).
\]
The interiors are disjoint, and each arc has length \(2\beta\). The endpoint \(\alpha=\beta\), where the arcs meet at one point, is included because endpoints do not affect integration. Any pair of equal-length arcs with disjoint interiors is congruent to one of these configurations after rotation and possible interchange. The full-circle orthonormal Fourier basis is \(e^{-it},1,e^{it}\) in \(L^2(\mathbb T,dt/(2\pi))\).

The lower frame bound is
\[
A_\beta(\alpha)=\inf_{0\ne f\in H}
\frac{(2\pi)^{-1}\int_{E_{\alpha,\beta}}|f(t)|^2\,dt}
{(2\pi)^{-1}\int_{\mathbb T}|f(t)|^2\,dt}.
\]
This is a continuous *energy observation* (not point sampling, weighted quadrature, or the full time-frequency concentration spectrum).

## Proof

**1. Exact Gram spectrum.** In the ordered basis \((e^{-it},1,e^{it})\), the observation Gram matrix is the real Toeplitz matrix
\[
G_{\alpha,\beta}=\begin{pmatrix} a&u&v\\u&a&u\\v&u&a\end{pmatrix},\qquad
a=\frac{2\beta}\pi,\quad
u=\frac{2\sin\beta\cos\alpha}\pi,\quad
v=\frac{\sin(2\beta)\cos(2\alpha)}\pi.
\]
This follows directly from integrating \(e^{ikt}\) for Fourier differences \(k=0,1,2\) over the two arcs. The antisymmetric vector \((1,0,-1)\) has eigenvalue \(a-v\). The symmetric subspace spanned by \((1,0,1)/\sqrt2\) and \((0,1,0)\) has the matrix \(\bigl(\begin{smallmatrix}a+v&\sqrt2u\\\sqrt2u&a\end{smallmatrix}\bigr)\). Its eigenvalues are
\[
\lambda_\pm=a+\frac v2\pm\frac12\sqrt{v^2+8u^2}.
\]
The smaller one is always the minimum eigenvalue: for \(v\le0\), \(\lambda_-<a-v\) directly; when \(v>0\), write \(t=\cos\alpha\), so \(2t^2-1>0\) and
\(u=\frac{2\sin\beta}\pi t>\frac{\sin(2\beta)}\pi(2t^2-1)=v\). Hence \(\sqrt{v^2+8u^2}>3v\) and again \(\lambda_-<a-v\). Thus
\[
A_\beta(\alpha)=a+\frac v2-\frac12\sqrt{v^2+8u^2}.
\]

**2. Unique global maximin.** Let \(B=\sin(2\beta)/\pi>0\), \(C=2\sin\beta/\pi>B\), and \(t=\cos\alpha\). Then \(u=Ct\) and \(v=B(2t^2-1)\). At antipodal separation \(t=0\) we obtain \(A_\beta(\pi/2)=a-B\). For any \(t>0\), subtracting this candidate value from the symmetric two-by-two Gram block gives
\[
\begin{pmatrix} 2Bt^2&\sqrt2Ct\\\sqrt2Ct&B\end{pmatrix},
\]
whose determinant is \(2t^2(B^2-C^2)<0\). Therefore this block has a negative eigenvalue, which means the original Gram matrix has an eigenvalue strictly below \(a-B\). This proves the unique optimum for every admissible \(\alpha\), including the endpoint where the arcs meet.

**3. Exact loss and local stability.** Rationalizing the explicit eigenvalue difference gives
\[
(a-B)-A_\beta(\alpha)
=\frac{4B\tan^2\beta\,t^2}
{\sqrt{(2t^2-1)^2+8t^2\sec^2\beta}+1+2t^2},\qquad t=\cos\alpha.
\]
The denominator is positive; expansion at \(t=0\) yields
\[
(a-B)-A_\beta(\alpha)=2B\tan^2\beta\,\cos^2\alpha+O_\beta(\cos^4\alpha).
\]
The positive quadratic coefficient is sharp, and no other separations have zero loss.

**4. Why splitting improves stability.** The optimal antipodal bound satisfies
\[
a-B=\frac{4\beta^3}{3\pi}+O(\beta^5)\quad(\beta\downarrow0).
\]
For comparison, a *single contiguous arc* \([-2\beta,2\beta]\) with the same total observation length has \(a=2\beta/\pi\), first off-diagonal \(u_c=\sin(2\beta)/\pi\) and second off-diagonal \(v_c=\sin(4\beta)/(2\pi)\). Its smallest Gram eigenvalue is \(a+v_c/2-\sqrt{v_c^2+8u_c^2}/2\), and the Taylor expansion is
\[
A_{\mathrm{contiguous}}(\beta)=\frac{64\beta^5}{135\pi}+O(\beta^7).
\]
Consequently \(A_\beta(\pi/2)/A_{\mathrm{contiguous}}(\beta)\sim45/(16\beta^2)\), a strong small-observation gain, with the two windows having exactly the same measure.

## Verification

The standalone `CHECK.py` directly integrates Fourier exponentials from the four arc endpoints, reconstructs the Gram matrices independently, verifies the closed eigenvalue formula, checks positive gaps and extremality across a deterministic parameter grid, and compares quadratic-form energies to numerical integration. Symbolic checks confirm the determinant certificate and the two small-arc leading coefficients. Run `python CHECK.py` in an environment satisfying `requirements.txt`. The successful run in this package reported `TWO_ARC_FOURIER_CHECKS_PASSED 3591`. Finite checks are corroboration, not the proof of the parameter-uniform theorem.

## Relationship to prior work

General time-frequency localization and prolate spectral theory provide the concentration-operator framework. Azimifard's 2026 multi-component localization analysis studies spectral transition counts, hard windows, and partition-sensitive bounds, rather than an explicitly optimized, finite three-character, two-equal-arc *lower* frame bound. Kunis's 2026 trigonometric quadrature work optimizes a different observation scheme: exact positive quadratures on curves, covering radii, and lengths. Slepian's classical discrete prolate treatment focuses concentration against a single frequency band and finite index sets; no same-parameter antipodal two-arc optimizer was located in accessible material. These comparisons do not constitute a claim of exhaustive publication priority.

## Limitations

The design family consists of **exactly two equal-width arcs**, nonnegative unweighted observation, and precisely the Fourier frequencies \(\{-1,0,1\}\). The theorem neither optimizes arbitrary observation subsets nor treats larger Fourier bands or noisy point-sample designs. The most directly relevant 2026 localization preprint was available by abstract but not accessible as full text through the consulted open interfaces; possible specialized prior coverage remains a publication-priority risk. No independent mathematical audit has been performed.

## References

1. A. Azimifard, *Componentwise and Measure-Sensitive Bounds for One-Dimensional Time-Frequency Localization*, arXiv:2609.14946, first posted 2026-09-14, https://arxiv.org/abs/2609.14946.
2. S. Kunis, *Positive quadrature and mobile sampling of multivariate trigonometric polynomials*, arXiv:2608.11915, first posted 2026-08-12, https://arxiv.org/abs/2608.11915. See Theorems 3.3 and 4.1 for its actual scope.
3. D. Slepian, *Prolate Spheroidal Wave Functions, Fourier Analysis, and Uncertainty—V: The Discrete Case*, Bell System Technical Journal 57 (1978), 1371–1430, doi:10.1002/j.1538-7305.1978.tb02104.x.
4. R. F. Bass and K. Gröchenig, *Random Sampling of Multivariate Trigonometric Polynomials*, SIAM J. Math. Anal. 36 (2004), 773–795, doi:10.1137/S0036141003432316.
