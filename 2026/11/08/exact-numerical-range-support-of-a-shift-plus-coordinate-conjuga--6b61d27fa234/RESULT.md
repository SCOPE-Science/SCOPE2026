# Exact numerical-range support of a shift plus coordinate conjugation

## Finding
For every real \(a>0\), define the real-linear map \(\Phi_a=S+aC\) on complex \(\ell^2(\mathbb N_0)\), where \(S e_j=e_{j+1}\) and \(C(x_j)_j=(\overline{x_j})_j\). Its essential numerical range equals the closure of its ordinary numerical range, and its ordinary numerical range contains precisely the **interior** of that closure. Let \(K_a=W_{\rm e}(\Phi_a)\). For every angle \(\theta\in\mathbb R\), the support function of \(K_a\) is
\[
h_a(\theta)=\begin{cases}
a+|\cos\theta|,&a|\cos\theta|\ge\sin^2\theta,\\[2pt]
\dfrac{\sqrt{a^2+\sin^2\theta}}{|\sin\theta|},&a|\cos\theta|<\sin^2\theta.
\end{cases}
\]
There is a genuine switch at \(|\cos\theta|=(\sqrt{a^2+4}-a)/2\). The boundary has positive-length circular arcs centered at \(1\) and \(-1\), each of radius \(a\), separated by noncircular arcs. The horizontal and vertical half-widths are \(1+a\) and \(\sqrt{1+a^2}\), respectively, so the boundary is never an ellipse. The ordinary numerical radius and the essential operator norm are both \(1+a\).

## Assumptions and scope
The Hilbert space is complex \(H=\ell^2(\mathbb N_0)\) with inner product linear in the **first** argument, \(\langle x,y\rangle=\sum_j x_j\overline{y_j}\). The ordinary numerical range is \(W(\Phi_a)=\{\langle\Phi_a x,x\rangle:\|x\|=1\}\). The essential numerical range is the set of limits of these scalars along weakly null unit-vector sequences. The parameter \(a\) is real and strictly positive; no assertion is made about arbitrary real-linear perturbations or other shifts. The support function determines a unique closed convex subset of the plane.

## Proof
**1. Fourier-pair bound.** Identify \(x=(x_j)\in H\) with the Hardy boundary function \(f(t)=\sum_{j\ge0}x_j e^{ijt}\in L^2(-\pi,\pi)\). Parseval gives
\[
\langle Sx,x\rangle=\frac1{2\pi}\int_{-\pi}^{\pi}e^{it}|f(t)|^2\,dt,\qquad
\langle Cx,x\rangle=\overline{\frac1{2\pi}\int_{-\pi}^{\pi}f(t)f(-t)\,dt}.
\]
(The second identity follows from orthogonality of distinct Fourier modes and density of polynomials.) Pairing \(t\) and \(-t\) for \(0<t<\pi\), the directional quadratic form
\(\operatorname{Re}(e^{-i\theta}\langle\Phi_a x,x\rangle)\) has diagonal contributions \(\cos(t-\theta)|f(t)|^2\) and \(\cos(t+\theta)|f(-t)|^2\), and cross contribution \(2a\operatorname{Re}(e^{i\theta}f(t)f(-t))\). It is bounded above by the largest eigenvalue of
\[
M_{\theta}(t)=\begin{pmatrix}
\cos(t-\theta)&a\\a&\cos(t+\theta)
\end{pmatrix}
\]
times \(|f(t)|^2+|f(-t)|^2\). That largest eigenvalue is
\[
L_{\theta}(t)=\cos t\cos\theta+\sqrt{a^2+\sin^2t\sin^2\theta}.
\]
Consequently the support is at most \(\max_{0\le t\le\pi}L_{\theta}(t)\).

**2. Exactness of the Fourier-pair bound.** For any \(0<t<\pi\) and complex \(u,v\) with \(|u|^2+|v|^2=1\), put, for \(0\le j<N\),
\[
x_j^{(N)}=N^{-1/2}(u e^{ijt}+v e^{-ijt}),\qquad x_j^{(N)}=0\ \text{for}\ j\ge N.
\]
As \(N\to\infty\), the squared norm tends to one, while
\[
\langle Sx^{(N)},x^{(N)}\rangle\to |u|^2e^{-it}+|v|^2e^{it},\qquad
\langle Cx^{(N)},x^{(N)}\rangle\to2\overline{uv}.
\]
Choose the phases so the cross term is positive in the chosen direction; then optimize \((|u|,|v|)\) to obtain \(L_{\theta}(t)\). At \(t=0,\pi\), constant and alternating blocks with a suitable global phase yield \(a+\cos\theta\) and \(a-\cos\theta\). Thus the upper bound is attained **as a supremum**, not necessarily by any single unit vector, and
\[
h_a(\theta)=\max_{-1\le u\le1}\left[u\cos\theta+\sqrt{a^2+(1-u^2)\sin^2\theta}\right].
\]

**3. Scalar optimization and transition.** Set \(c=|\cos\theta|\), \(s=|\sin\theta|\). By symmetry the last maximum is \(\max_{0\le u\le1}\{cu+\sqrt{a^2+s^2(1-u^2)}\}\). If \(s=0\), the maximum is \(a+c\). If \(s>0\), the strictly concave expression has an interior maximizer precisely when \(s^2>ac\), in which case
\[
u_* = \frac{c\sqrt{a^2+s^2}}s,\qquad h_a(\theta)=\frac{\sqrt{a^2+s^2}}s.
\]
Otherwise the maximizer is \(u=1\) and \(h_a(\theta)=a+c\). The equality threshold \(s^2=ac\) is equivalent to \(c=(\sqrt{a^2+4}-a)/2\), as claimed.

**4. Essential range and boundary nonattainment.** Since \(CS=SC\), every scalar \(\langle\Phi_a x,x\rangle\) persists under the shifts \(S^N x\). These are weakly null unit vectors. Therefore \(W(\Phi_a)\subset W_{\rm e}(\Phi_a)\subset\overline{W(\Phi_a)}\), and the essential numerical range is closed, so all three closures agree. For any fixed \(\theta\), the function \(u\mapsto u\cos\theta+\sqrt{a^2+(1-u^2)\sin^2\theta}\) has a unique maximizer: it is strictly concave if \(\sin\theta\ne0\), and strictly monotone when \(\sin\theta=0\). In the Fourier-pair integral, equality would require the nonzero \(L^2\)-mass of \(f\) to be supported on the at most two angles corresponding to that single maximizer, a measure-zero set. Hence **no** unit vector attains a support value in any direction. The numerical range is convex by the real-linear Toeplitz–Hausdorff theorem [2]. Since it is dense in \(K_a\), has nonempty interior (for instance, all scalars \(a e^{i\varphi}\) occur from phase-rotated first-coordinate vectors, and convexity fills their disk), and has no boundary points, it is exactly \(\operatorname{int}K_a\).

**5. Geometry and norms.** In the open angular region \(a|\cos\theta|>\sin^2\theta\), the support function is \(a+|\cos\theta|\), giving nonempty circular arcs of radius \(a\) centered at the two points \(\pm1\). At \(\theta=0\) and \(\theta=\pi/2\), the supports are \(1+a\) and \(\sqrt{1+a^2}\). In the complementary open angular region the support is \(\sqrt{a^2+\sin^2\theta}/|\sin\theta|\). It cannot coincide with a circular support \(R+b\cos\theta+c\sin\theta\) on a nonempty open subinterval: on \((0,\pi)\) the former is real analytic, and such an identity would analytically continue toward zero, where the former diverges but the latter remains bounded. Therefore the connecting arcs are noncircular. An ellipse containing a nontrivial circular arc must be that circle, but these half-widths differ; thus the boundary is not elliptical. The operator norm is at most \(1+a\) by the triangle inequality, while long real constant blocks make \(\|(S+aC)x\|\to1+a\), so it equals \(1+a\). These same blocks escape weakly to zero, hence prove the essential norm is at least \(1+a\); the reverse inequality is immediate. Finally the numerical radius is at most the norm and is at least the rightmost support \(h_a(0)=1+a\), giving equality.

## Verification
The standalone finite identity checks in the accompanying `check_real_shift_conjugation.py` build exact finite-section real quadratic forms from the defining operator, verify 320 random algebraic realification cases, and compare numerical largest eigenvalues against the analytic support bound in 35 parameter-angle pairs. They establish 390 finite diagnostic assertions. The infinite-dimensional equality and nonattainment are proved analytically above; finite matrices are not certificates of those statements. All limits use normalized finite blocks and ordinary Lebesgue/Parseval identities.

## Relationship to prior work
Majumdar and Müller [1] develop essential numerical ranges for arbitrary real-linear operators and show their general compact convexity, but do not give this mixed shift-plus-coordinate-conjugation support law. Kołaczek and Müller [2] prove convexity of the ordinary real-linear numerical range; that theorem is used in Step 4. Their discussion of arbitrary real-linear operators, including finite-dimensional examples, does not determine the boundary of this unilateral model. Kołaczek and Müller [3] treat purely antilinear numerical ranges, whose disk geometry cannot determine this coupled mixed case. The present calculation resolves a concrete infinite-dimensional real-linear example using a two-frequency Fourier-pair variational formula. It is not a claim that general convexity or Fourier diagonalization is new.

## Limitations
The result is limited to the standard unilateral shift and **coordinatewise** conjugation with real \(a>0\). The derived shape uses only the ordinary and essential numerical ranges; it does not classify generalized \(q\)-numerical ranges, spectra, weighted shifts, or arbitrary compact perturbations. More general mixed Toeplitz-plus-antilinear symbol theorems could imply this special case; publication priority has not been independently established. The diagnostics are finite, while Step 4 relies on a published general convexity theorem.

## References
[1] A. Majumdar and V. Müller, *Some Generalized Numerical Ranges of Real-linear Operators on Hilbert Spaces*, first arXiv version 2026-10-12, https://arxiv.org/abs/2610.16823 (especially Sections 2–5).

[2] D. Kołaczek and V. Müller, *Real linear operators and numerical ranges*, first arXiv version 2025-08-06, https://arxiv.org/abs/2508.04347 (Theorem 6.4 and Section 7).

[3] D. Kołaczek and V. Müller, *Numerical Ranges of Antilinear Operators*, Integral Equations and Operator Theory **96** (2024), Article 17, https://doi.org/10.1007/s00020-024-02768-5 (Section 2).