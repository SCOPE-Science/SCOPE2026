# Quartic Ritz-gap repulsion and eigenvector-conditioning tails for equilateral unitary compressions

## Finding

Let \(\omega=e^{2\pi i/3}\) and \(A=\operatorname{diag}(1,\omega,\omega^2)\). For a Haar-random two-plane \(\mathcal U\) in either \(\mathbb C^3\) or \(\mathbb R^3\), choose any orthonormal matrix \(Q\) spanning it and set \(B=Q^*AQ\). The spectrum of \(B\) is independent of the chosen basis. Write \(D=|\lambda_1(B)-\lambda_2(B)|\). If \(D>0\), define \(\kappa_{\mathrm{eig}}\) to be the spectral condition number of a matrix of **unit Euclidean norm** right eigenvectors of \(B\) (independent of their phases and ordering).

For complex Haar planes,
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-4}\Pr\{D\le\varepsilon\}=\frac{\pi}{12\sqrt3},\qquad
\lim_{R\to\infty}R^4\Pr\{\kappa_{\mathrm{eig}}>R\}=\frac{4\pi}{3\sqrt3}.
\]
For real Haar planes (with the same *complex* normal matrix \(A\)), the respective constants are
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-4}\Pr\{D\le\varepsilon\}=\frac1{16},\qquad
\lim_{R\to\infty}R^4\Pr\{\kappa_{\mathrm{eig}}>R\}=1.
\]
In both ensembles the eigenvalues are distinct almost surely, yet the unique defective compression belongs to the closure of the sampling support. Consequently, for each real \(p>0\),
\[
\mathbb E\kappa_{\mathrm{eig}}^p<\infty\quad\Longleftrightarrow\quad p<4.
\]
The theorem concerns one Haar-random orthogonal compression of a fixed three-dimensional **normal** matrix, rather than a matrix with independent random entries.

## Assumptions and scope

Take \(\mathbb F=\mathbb C\) or \(\mathbb F=\mathbb R\). For \(\mathbb F=\mathbb C\), \(Q\in\mathbb C^{3\times2}\) is Haar on the complex Stiefel manifold. For \(\mathbb F=\mathbb R\), \(Q\in\mathbb R^{3\times2}\) is Haar on the real Stiefel manifold, and \(Q^*\) means the conjugate transpose (equal here to \(Q^T\)). The matrix \(A\) stays complex in both cases. Let \(v\in\mathbb F^3\) be a random unit normal, so \(QQ^*=I-vv^*\), and put \(w_j=|v_j|^2\), \(u=w_1+\omega w_2+\omega^2w_3\). The weights are nonnegative and sum to one, and \(u\) lies in the closed equilateral triangle \(T=\operatorname{conv}\{1,\omega,\omega^2\}\). In either Haar ensemble, \(w_j>0\) almost surely. The condition number is defined only on the almost-sure event of distinct eigenvalues; assigning \(+\infty\) at the single defective plane does not alter any probability statement.

## Proof

**1. Exact characteristic polynomial.** The determinant of a codimension-one orthogonal compression is the weighted principal-cofactor polynomial:
\[
\det(zI_2-B)=\sum_{j=1}^3w_j\prod_{k\ne j}(z-\lambda_k),\qquad
(\lambda_1,\lambda_2,\lambda_3)=(1,\omega,\omega^2).
\]
Since \(1+\omega+\omega^2=0\), expansion gives the **exact** identity
\[
\det(zI_2-B)=z^2+uz+\bar u.
\]
Thus, writing \(F(u)=u^2-4\bar u\),
\[
D^2=|F(u)|.
\]
If \(F(u)=0\), then \(|u|^2=4|u|\), so \(u=0\) or \(|u|=4\). But \(|u|\le1\) throughout \(T\), hence \(F(u)=0\) **only at** \(u=0\), equivalently \(w_1=w_2=w_3=1/3\).

**2. Nonnormality and unit-column eigenvector conditioning.** From \(QQ^*=I-vv^*\) and unitarity of \(A\),
\[
\|B\|_F^2=\operatorname{tr}(A^*(I-vv^*)A(I-vv^*))=1+|u|^2.
\]
A unitary Schur triangularization of \(B\) has diagonal entries its eigenvalues and an upper entry of modulus \(\nu\), where
\[
\nu^2=1+\frac{|u|^2-D^2}{2}.
\]
Directly computing the overlap of unit right eigenvectors of this triangular matrix shows
\[
\kappa_{\mathrm{eig}}(u)=\frac{\sqrt{\nu^2+D^2}+\nu}{D},\qquad u\ne0.
\]
This expression is basis-independent, including when \(\nu=0\). At \(u=0\), the characteristic polynomial is \(z^2\) and \(\|B\|_F=1\), so \(B\) is a nonzero nilpotent Jordan block. As \(u\to0\), \(\nu\to1\) and
\[
D=2|u|^{1/2}(1+O(|u|)),\qquad
\kappa_{\mathrm{eig}}=|u|^{-1/2}(1+o(1)).
\]
(The first expansion follows by factoring \(F(u)=-4\bar u\,[1-u^2/(4\bar u)]\).)

**3. The two local Haar densities.** Under complex Haar measure, \((w_1,w_2,w_3)\) has Dirichlet \((1,1,1)\) law, hence is uniformly distributed on the weight simplex. Under real Haar measure it has Dirichlet \((1/2,1/2,1/2)\) law, whose density in \((w_1,w_2)\) is \((2\pi\sqrt{w_1w_2w_3})^{-1}\). The affine map from \((w_1,w_2)\) to \((\operatorname{Re}u,\operatorname{Im}u)\) has absolute Jacobian \(3\sqrt3/2\), while \(T\) has area \(3\sqrt3/4\). Consequently the planar densities at its center are
\[
f_{\mathbb C}(0)=\frac4{3\sqrt3},\qquad f_{\mathbb R}(0)=\frac1\pi.
\]
In both cases the density is positive and continuous near zero. Therefore, as \(r\downarrow0\),
\[
\Pr\{|u|\le r\}=\pi f_{\mathbb F}(0)r^2+o(r^2).
\]

**4. Sharp tails and moments.** From the local expansions in step 2, for every fixed \(\delta>0\), sufficiently small \(|u|\) makes the gap event \(\{D\le\varepsilon\}\) lie between centered disks of radii \((1-\delta)\varepsilon^2/4\) and \((1+\delta)\varepsilon^2/4\); compactness and the unique zero of \(F\) exclude other contributions. Step 3 then yields
\[
\Pr\{D\le\varepsilon\}\sim\frac{\pi f_{\mathbb F}(0)}{16}\varepsilon^4.
\]
Likewise, the condition-number event \(\{\kappa_{\mathrm{eig}}>R\}\) is sandwiched between centered disks with radii \((1\pm\delta)R^{-2}\) once \(R\) is sufficiently large, and the condition number is bounded away from the central neighborhood. Hence
\[
\Pr\{\kappa_{\mathrm{eig}}>R\}\sim\pi f_{\mathbb F}(0)R^{-4}.
\]
Substitution gives the four constants. Finally the layer-cake formula \(\mathbb E X^p=p\int_0^\infty R^{p-1}\Pr\{X>R\}\,dR\) for \(p>0\), together with the strictly positive leading tail coefficient, proves the exact moment threshold \(p=4\).

## Verification

The accompanying `verify.py` checks exact rational barycentric identities in \(\mathbb Q(\sqrt{-3})\), directly constructs real/complex random-plane compressions and their unit-column eigenvectors, and compares the discriminant, Frobenius and conditioning identities with direct matrix algebra. It also performs *non-certifying* seeded finite-sample checks of the local probability scale and independently checks the four constants. Run it with `python verify.py` in a Python environment with NumPy. An execution of the attached exact script returned 5,436 passing checks. The infinite-limit and moment assertions are proved in Steps 3–4; finite simulation is not their justification.

## Relationship to prior work

The motivating 2026 workshop collection discusses Ritz-value distributions for non-Hermitian matrices and their randomized subspaces, and notes previous deterministic codimension-one results for normal matrices. Shah (2025) proves bounds on expected pseudospectral area of random compressions, with its principal finite-dimensional corollary assuming sketch dimension at most \(n/2-8\), not the present \(n=3\), dimension-two compression. Carden and Hansen (2013) analyze geometric constraints on pairs of Ritz values of three-dimensional normal matrices; Malamud (2003) addresses inverse spectral geometry. Those geometric results are not claimed as new here. The distinct contribution is the field-dependent exact **rare-event and eigenvector-conditioning constants** and the sharp fourth-moment barrier for this equilateral model. The complete text of Carden and Hansen was not accessible for this comparison, and an equivalent probabilistic calculation elsewhere cannot be excluded.

## Limitations

This theorem does not cover arbitrary normal spectra, non-Haar distributions, Krylov subspaces, finite-precision eigensolvers, or a universal bound in the matrix dimension. The matrix is a fixed, deliberately symmetric test case. The real-Haar model uses real trial planes but complex original eigenvalues. The quantity \(\kappa_{\mathrm{eig}}\) requires **unit-normalized columns**; arbitrary rescaling of eigenvectors changes the condition number. No independent audit has been performed.

## References

1. N. Amsel and collaborators, *Linear Systems and Eigenvalue Problems: Open Questions from a Simons Workshop*, arXiv:2602.05394v3 (2026), Section 3.3, https://arxiv.org/html/2602.05394v3 . First public version 2026-02-05.
2. R. Shah, *The Pseudospectrum of Random Compressions of Matrices*, arXiv:2501.01418v1 (2025), https://arxiv.org/html/2501.01418v1 .
3. R. Carden and D. Hansen, *Ritz Values of Normal Matrices and Ceva's Theorem*, Linear Algebra and its Applications 438 (2013), 4114–4129, https://doi.org/10.1016/j.laa.2012.12.030 .
4. S. M. Malamud, *Inverse Spectral Problem for Normal Matrices and a Generalization of the Gauss–Lucas Theorem*, arXiv:math/0304158 (2003), https://arxiv.org/abs/math/0304158 .
