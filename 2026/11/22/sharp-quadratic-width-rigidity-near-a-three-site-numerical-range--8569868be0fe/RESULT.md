# Sharp quadratic width rigidity near a three-site numerical-range disk

## Finding
Let \(J\) be the \(3\times3\) upper Jordan shift, \(D=\operatorname{diag}(d_0,d_1,d_2)\) with real entries, and \(A_\varepsilon=J+\varepsilon D\) for real \(\varepsilon\). Let \(w_\varepsilon(\theta)\) be the width of \(W(A_\varepsilon)\) in direction \(e^{i\theta}\). Set
\[
Q(D)=\frac{4(d_0-d_2)^2+(d_0+d_2-2d_1)^2}{8\sqrt2},\qquad \bar d=(d_0+d_1+d_2)/3.
\]
The **width oscillation** \(\Omega_\varepsilon=\max_\theta w_\varepsilon(\theta)-\min_\theta w_\varepsilon(\theta)\) is, for every real \(\varepsilon\),
\[
\Omega_\varepsilon=\lambda_{\max}(H+\varepsilon D)+\lambda_{\max}(H-\varepsilon D)-\sqrt2,
\quad H=(J+J^*)/2.
\]
It is strictly positive whenever \(\varepsilon\ne0\) and \(D\) is nonscalar. As \(\varepsilon\to0\),
\[
\Omega_\varepsilon=Q(D)\varepsilon^2+O_D(\varepsilon^4).
\]
The exact **sharp Hessian bounds** are
\[
\frac{3}{4\sqrt2}\|D-\bar d I\|_F^2\le Q(D)\le\frac1{\sqrt2}\|D-\bar d I\|_F^2.
\]
For nonzero traceless real \(D\), lower equality holds precisely on the line \(D\propto\operatorname{diag}(1,-2,1)\); upper equality holds precisely on \(D\propto\operatorname{diag}(1,0,-1)\).

Let \(\delta_\varepsilon\) be the smallest Hausdorff distance between the convex numerical range \(W(A_\varepsilon)\) and any closed Euclidean disk in \(\mathbb C\), allowing a point disk. Then
\[
\delta_\varepsilon=\tfrac14 Q(D)\varepsilon^2+O_D(|\varepsilon|^3).
\]
Thus the sharp quadratic least-detectable transverse disk-deformation coefficient under \(\|D-\bar d I\|_F=1\) is \(3/(16\sqrt2)\). In the least-detectable direction \(D=\operatorname{diag}(1,-2,1)\), both defects are *exact for all real* \(\varepsilon\):
\[
\Omega_\varepsilon=\sqrt{2+9\varepsilon^2}-\sqrt2,
\qquad \delta_\varepsilon=\frac{\sqrt{2+9\varepsilon^2}-\sqrt2}{4}.
\]
The last equality is for the displayed unnormalized \(D\), whose Frobenius norm is \(\sqrt6\).

## Assumptions and scope
All spaces are over \(\mathbb C\), numerical ranges use the standard Hilbert inner product, and matrix norms are Frobenius unless explicitly stated. The perturbation is **real diagonal** and the off-diagonal Jordan entries equal one. No assertion is made about arbitrary complex or off-diagonal perturbations, larger Jordan blocks, or a dimension-independent stability constant. Scalar \(D\) only translates the numerical range and gives zero width and disk defects for every \(\varepsilon\).

## Proof
Write \(f(t)=\lambda_{\max}(H+tD)\). The unitary \(U_\theta=\operatorname{diag}(1,e^{i\theta},e^{2i\theta})\) conjugates \(\operatorname{Re}(e^{-i\theta}J)\) to \(H\) and fixes \(D\). Hence the support function of the numerical range is \(h_\varepsilon(\theta)=f(\varepsilon\cos\theta)\). The bipartite sign matrix \(S=\operatorname{diag}(1,-1,1)\) satisfies \(SHS=-H\) and \(SDS=D\), giving \(\lambda_{\min}(H+tD)=-f(-t)\). Therefore
\[
w_\varepsilon(\theta)=f(\varepsilon\cos\theta)+f(-\varepsilon\cos\theta).
\]
The largest eigenvalue is a convex function of a Hermitian affine pencil, so \(g(t)=f(t)+f(-t)\) is convex and even. It is consequently nondecreasing for \(t\ge0\). The angular maximum occurs at \(\theta=0\), while the minimum occurs at \(\theta=\pi/2\), where \(g(0)=\sqrt2\), proving the exact oscillation identity. Rayleigh's principle gives \(g(t)\ge2f(0)\). If equality held for a nonzero \(t\), the unique top eigenvector \(v_+=(1/2,1/\sqrt2,1/2)\) of \(H\) would maximize both \(H+tD\) and \(H-tD\); subtracting the corresponding eigenvector equations makes \(Dv_+\) proportional to \(v_+\). All three entries of \(v_+\) are nonzero, so \(D\) would be scalar. This proves strictness.

The other eigenpairs of \(H\) are \(v_-=(1/2,-1/\sqrt2,1/2)\) at eigenvalue \(-1/\sqrt2\), and \(v_0=(1/\sqrt2,0,-1/\sqrt2)\) at eigenvalue zero. Nondegenerate Hermitian eigenvalue perturbation gives
\[
f(t)=\frac1{\sqrt2}+a(D)t+B(D)t^2+O_D(t^3),\quad a(D)=\langle v_+,Dv_+\rangle,
\]
with
\[
B(D)=\frac{|\langle v_0,Dv_+\rangle|^2}{1/\sqrt2}+
\frac{|\langle v_-,Dv_+\rangle|^2}{\sqrt2}
=\frac{4(d_0-d_2)^2+(d_0+d_2-2d_1)^2}{16\sqrt2}.
\]
Since \(f\) is real analytic near zero, the even sum cancels odd Taylor powers; \(g(t)=\sqrt2+2B(D)t^2+O_D(t^4)\). Thus \(Q=2B\). Decompose
\[
D-\bar dI=\alpha\operatorname{diag}(1,0,-1)/\sqrt2+
\beta\operatorname{diag}(1,-2,1)/\sqrt6.
\]
These two diagonal matrices are Frobenius orthonormal, and \(Q(D)=\alpha^2/\sqrt2+3\beta^2/(4\sqrt2)\). This proves both optimal constants and their equality directions.

For the disk estimate, the compact convex-set identity \(d_H(K,L)=\|h_K-h_L\|_{L^\infty(S^1)}\) converts the problem into uniform approximation of \(h_\varepsilon\) by \(r+\operatorname{Re}(e^{-i\theta}z)\), with \(r\ge0\). Uniformly in \(\theta\),
\[
h_\varepsilon(\theta)=\frac1{\sqrt2}+a(D)\varepsilon\cos\theta+
\frac{B(D)\varepsilon^2}{2}(1+\cos2\theta)+O_D(|\varepsilon|^3).
\]
Choosing the disk with center \(a(D)\varepsilon\in\mathbb R\) and radius \(1/\sqrt2+B(D)\varepsilon^2/2\) gives the upper bound \(B(D)\varepsilon^2/2+O_D(|\varepsilon|^3)\). For every candidate disk, the alternating sum of the four support errors at \(\theta=0,\pi/2,\pi,3\pi/2\) cancels its constant and first harmonics and equals \(2B(D)\varepsilon^2+O_D(|\varepsilon|^3)\); the absolute value is at most four times the uniform error. Hence the matching lower bound holds. Since \(Q=2B\), the coefficient is \(Q/4\).

Finally, for \(D=\operatorname{diag}(1,-2,1)\), the reflection-even subspace of \(H+tD\) has eigenvalues \(-t/2\pm\sqrt{2+9t^2}/2\); the reflection-odd vector has eigenvalue \(t\). The upper branch strictly exceeds \(t\) for every real \(t\), yielding
\[
h_\varepsilon(\theta)=-\tfrac12\varepsilon\cos\theta+
\tfrac12\sqrt{2+9\varepsilon^2\cos^2\theta}.
\]
After translation by \(-\varepsilon/2\), this is the support function of a centered ellipse, with semiaxes \(\tfrac12\sqrt{2+9\varepsilon^2}\) and \(1/\sqrt2\). The optimal Hausdorff disk for any centered ellipse has radius the arithmetic mean of its two semiaxes and distance half their difference (central symmetry removes any benefit from translating the candidate disk). Consequently the two all-parameter formulas follow.

## Verification
The accompanying standalone standard-library checker evaluates real-symmetric \(3\times3\) eigenvalues using Jacobi rotations. It tests the oscillation expansion, positive sharp quadratic bounds and both exact special-direction formulas over deterministic examples. The checker returns `VERIFY_OK 850 finite assertions`. Its finite tests do not substitute for the real-analytic perturbation proof or establish originality.

## Relationship to prior work
Jiang (2026) proves the global qualitative theorem that a finite matrix numerical range has constant width if and only if it is a disk; that theorem does not give local near-disk stability constants or the least-detectable perturbation direction. Earlier work by Chien, Nakazato and Meng studies width and specific nilpotent Toeplitz matrices. Adams and Gorkin (2026) develop eigenvector perturbation expansions for angular numerical-range curves; those expansions provide relevant methodological antecedents but do not state the sharp diagonal-perturbation width Hessian, its two optimized eigenvalues, or the best-disk asymptotic. The elementary three-eigenvalue perturbation formula is standard prior technology, not itself claimed as original. The asserted contribution is the *combined sharp quantitative local rigidity and exact all-scale benchmark* in the specified natural family.

## Limitations
The asymptotic error constants depend on \(D\), although uniform remainders hold when \(D\) ranges in any fixed bounded set and \(\varepsilon\) is sufficiently small. The best-disk formula is asymptotic for general \(D\), exact for the identified symmetric direction. The theorem gives no sharp global stability bound for arbitrary matrices and makes no claim that traditional eigenvalue perturbation techniques are new. Publication priority for related quantitative near-disk problems requires human bibliographic review; independent validation has not occurred.

## References
1. M. Jiang, *A proof of the constant-width numerical range conjecture*, arXiv:2611.13461v1 (2026), https://arxiv.org/abs/2611.13461.
2. G. Adams and P. Gorkin, *Perturbation Theory for Eigenvalues and Curves Inside the Numerical Range*, Constructive Approximation (published 2026), https://doi.org/10.1007/s00365-026-09765-4.
3. M.-T. Chien, H. Nakazato and J. Meng, *The diameter and width of numerical ranges*, Linear Algebra Appl. **582** (2019), 76–98, https://doi.org/10.1016/j.laa.2019.07.036.
