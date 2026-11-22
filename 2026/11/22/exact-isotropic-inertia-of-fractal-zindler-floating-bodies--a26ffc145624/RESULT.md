# Exact isotropic inertia of fractal Zindler floating bodies

## Finding
For the nonrectifiable Zindler Jordan body \(K=K_{\alpha,\beta,r}\) defined below, the complete planar inertia tensor is \((J/2)I_2\), where \(J=\int_K\|x\|^2\,dA\) is the following **exact rational expression** in the construction parameters:
\[
J=\frac{\pi}{2}\left[r^4+r^2(A+B)+\frac34A^2-\frac38C-\frac12AB+\frac14E-\frac14B^2+\frac18D\right].
\]
Here
\[
A=\frac1{\alpha^2-1},\quad B=\frac{\beta^2}{\alpha^2-\beta^2},\quad C=\frac1{\alpha^4-1},\quad D=\frac{\beta^4}{\alpha^4-\beta^4},\quad E=\frac{\beta^2}{\alpha^4-\beta^2}.
\]
For the known area \(S=\pi[r^2+(A-B)/2]\), the disk of equal area has polar second moment \(J_{\rm disk}=S^2/(2\pi)\). Consequently
\[
J-J_{\rm disk}=\pi B r^2+\frac\pi2\left[\frac12 A^2-\frac38C+\frac14E-\frac12B^2+\frac18D\right].
\]
Thus the area correction is independent of \(r\), but the moment excess grows with the **sharp positive quadratic coefficient** \(\pi\beta^2/(\alpha^2-\beta^2)\).

## Assumptions and scope
Take any odd integer \(\beta\ge7\) and real \(\alpha>\beta\) satisfying \(\beta^2>\alpha(1+3\pi/2)\), and \(r>(\alpha-1)^{-1}+2\beta/(\alpha-\beta)\). Let \(u(t)=(\cos t,\sin t)\), \(u'(t)=(-\sin t,\cos t)\), and \(h(t)=\sum_{k\ge1}\alpha^{-k}\sin(\beta^k t)\). Define \(z(t)=h(t)u(t)+(r+h'(t))u'(t)\) and let \(K\) be its bounded Jordan region with boundary included. The cited original construction establishes that this is a simple nonrectifiable fractal curve of Hausdorff dimension smaller than two, and proves convergence of the regions bounded by the smooth truncations. The integral uses ordinary two-dimensional Lebesgue area, with origin at the common rotational center (not an arbitrary translated origin).

## Proof
**1. Smooth reduction.** Define \(h_N(t)=\sum_{k=1}^N a_k\sin(\omega_k t)\), where \(a_k=\alpha^{-k}\) and \(\omega_k=\beta^k\). Write \(q=h_N\) and \(p=h_N'\). The smooth boundary \(z_N=q u+(r+p)u'\) has \(z_N'=-r u+(q+q'')u'\). Therefore
\[
\|z_N\|^2=q^2+(r+p)^2,\qquad \det(z_N,z_N')=q(q+q'')+r(r+p).
\]
Green's theorem gives \(J_N=\tfrac14\int_0^{2\pi}\|z_N\|^2\det(z_N,z_N')\,dt\). Each \(\omega_k\) is odd, so \(q(t+\pi)=-q(t)\) and likewise for \(p,q''\). The odd-degree products vanish upon integration. Integration by parts, using \(\int q^3q''=-3\int q^2p^2\) and \(\int qp^2q''=-\frac13\int p^4\), yields
\[
J_N=\frac{\pi r^4}{2}+\frac{r^2}{2}\int_0^{2\pi}(q^2+p^2)\,dt
+\frac14\int_0^{2\pi}\left(q^4-2q^2p^2-\frac13p^4\right)\,dt.
\]
**2. Lacunary fourth-order orthogonality.** In any zero-frequency signed sum of at most four frequencies from \(\{\beta^k:k\ge1\}\) with \(\beta\ge7\), the largest frequency can be canceled only by another copy of the same frequency of opposite sign. Repeating gives pairwise cancellation only. (Without such pairing, the largest uncanceled \(\beta^k\) exceeds the combined absolute value of at most three smaller powers.) Consequently, with
\[
A_N=\sum a_k^2,\quad B_N=\sum \omega_k^2a_k^2,\quad C_N=\sum a_k^4,\quad D_N=\sum\omega_k^4a_k^4,\quad E_N=\sum\omega_k^2a_k^4,
\]
one has the exact averages
\[
\langle q^4\rangle=\tfrac34 A_N^2-\tfrac38 C_N,\quad
\langle p^4\rangle=\tfrac34 B_N^2-\tfrac38 D_N,\quad
\langle q^2p^2\rangle=\tfrac14 A_NB_N-\tfrac18 E_N,
\]
where \(\langle f\rangle=(2\pi)^{-1}\int_0^{2\pi}f(t)\,dt\). The quadratic averages are \(\langle q^2\rangle=A_N/2\) and \(\langle p^2\rangle=B_N/2\). Substitution produces the displayed formula for \(J_N\), with each of \(A,B,C,D,E\) replaced by the corresponding finite sum.

**3. Fractal limit.** Geometric series give \(A_N\to A\), \(B_N\to B\), \(C_N\to C\), \(D_N\to D\), \(E_N\to E\), since \(\beta<\alpha\). The original paper proves uniform boundary convergence and convergence in measure of the corresponding bounded Jordan regions, using their boundary's Hausdorff dimension below two. All regions lie in a common compact disk because \(h_N,h_N'\) are uniformly bounded. Hence bounded-weight convergence in \(L^1\) implies \(\int_{K_N}\|x\|^2\,dx\to\int_K\|x\|^2\,dx\). This establishes the exact formula for the fractal body without differentiating its nowhere-differentiable boundary.

**4. Tensor and disk comparison.** Every \(\omega_k\) is a multiple of \(\beta\), so \(h(t+2\pi/\beta)=h(t)\) and \(z(t+2\pi/\beta)=R_{2\pi/\beta}z(t)\). The body's second-moment matrix commutes with a nontrivial plane rotation, hence is scalar and has trace \(J\). Using the original paper's \(S=\pi[r^2+(A-B)/2]\) and expanding \(S^2/(2\pi)\) gives the exact disk-normalized excess displayed above and its sharp \(r^2\)-coefficient.

## Verification
The standalone `verify_inertia.py` tests finite truncations \(N=1,2,3\) for \((\beta,\alpha)=(7,8)\) and \((9,10.5)\) at \(r=25\). It evaluates both the direct Green-integral trapezoidal quadrature using all Fourier frequencies (\(2^{18}\) grid nodes) and the independently coded rational finite-sum formula. All six differences were smaller than \(2\times10^{-9}\). These finite numerical checks corroborate, rather than prove, the exact and infinite-limit identities.

## Relationship to prior work
Martinez-Maure and Rochera (arXiv:2611.11309v1, public 2026-11-08) construct these fractal floating bodies and calculate their area; they do not evaluate the origin-centered polar second moment or isotropic inertia tensor. Classical projective-hedgehog and Zindler literature describes the curve/chord correspondence. The new result supplies a distinct second-order geometric mass invariant and shows the exact quadratic inertia-versus-area scale separation. Related work on Reuleaux curves computes inertia for a different smooth constant-width family and does not imply the formula for this nonrectifiable lacunary family.

## Limitations
The formula is for the specified lacunary \(\alpha,\beta\) construction and the stated sufficiently-large \(r\). It is not an identity for arbitrary Zindler curves or arbitrary fractal boundaries. The moment is about the rotational center; it equals the centroidal moment because the \(\beta\)-fold symmetry forces centroid zero. The mathematical review is not an independent priority audit; unindexed historical exact formulas remain a residual risk.

## References
- Y. Martinez-Maure and D. Rochera, *Fractal solutions to the two-dimensional floating body problem*, arXiv:2611.11309v1, 2026-11-08, https://arxiv.org/html/2611.11309v1, §§2–4.
- H. Martini, L. Montejano and D. Oliveros, *Bodies of Constant Width: An Introduction to Convex Geometry with Applications*, Springer, 2019, Chapter 5 (classical Zindler–constant-width correspondence), https://doi.org/10.1007/978-3-030-03868-7.
