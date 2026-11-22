# Sharp quartic Fourier-extension profile for constant–quadrupole data on the two-sphere

## Finding
Let \(\mu\) be probability surface measure on \(\mathbb S^2\), let \(\mathcal H_2\) be the complex degree-two spherical harmonics, and define
\[
(Tf)(x)=\int_{\mathbb S^2}e^{-ix\cdot\omega}f(\omega)\,d\mu(\omega).
\]
For every nonzero \(f=a+Q\), with \(a\in\mathbb C\), \(Q\in\mathcal H_2\), put \(\beta=\|Q\|_{L^2(\mu)}^2/\|f\|_{L^2(\mu)}^2\). Then
\[
\frac{\|Tf\|_{L^4(\mathbb R^3)}^4}{\pi^2\|f\|_{L^2(\mu)}^4}
\leq (1-\beta)^2+\frac65\beta(1-\beta)
+\frac{8\sqrt5}{49}\sqrt{1-\beta}\,\beta^{3/2}
+\frac{33}{49}\beta^2.\tag{1}
\]
This bound is sharp **at each** \(\beta\in[0,1]\). For \(0<\beta<1\), equality holds exactly for scalar multiples of
\[
\sqrt{1-\beta}+\sqrt\beta\,Y_u(\omega),\qquad
Y_u(\omega)=\frac{\sqrt5}{2}(3(u\cdot\omega)^2-1),\quad u\in\mathbb S^2.
\]
For \(\beta=0\), equality holds for all nonzero constants. For \(\beta=1\), equality holds exactly for complex scalar multiples of nonzero **real** degree-two spherical harmonics, not only zonal ones.

## Assumptions and scope
All norms on the sphere use the probability measure \(d\mu=d\sigma/(4\pi)\), while the target \(\mathbb R^3\) uses unnormalized Lebesgue measure. The Fourier transform uses the phase \(e^{-ix\cdot\omega}\), with no additional factors. The space \(\mathcal H_2\) consists of restrictions of trace-free complex homogeneous quadratic harmonic polynomials, so its elements have zero spherical mean. The claim treats all complex coefficients, every prescribed real \(\beta\in[0,1]\), and no higher spherical-harmonic modes.

## Proof
**Radial reduction and four exact integrals.** Let \(j_0\) and \(j_2\) be the standard real spherical Bessel functions. For \(x=r\theta\), Funk–Hecke gives
\[
(Tf)(r\theta)=a j_0(r)-Q(\theta)j_2(r),\qquad
j_0(r)=\frac{\sin r}{r}.
\]
The four radial integrals needed below are
\[
\begin{aligned}
\int_0^\infty r^2j_0(r)^4dr&=\frac\pi4, &
\int_0^\infty r^2j_0(r)^2j_2(r)^2dr&=\frac\pi{20},\\
\int_0^\infty r^2j_0(r)j_2(r)^3dr&=-\frac\pi{28}, &
\int_0^\infty r^2j_2(r)^4dr&=\frac{11\pi}{140}.
\end{aligned}\tag{2}
\]
Here is an exact independent derivation, avoiding numerical integration. Define even, compactly supported one-dimensional functions \(q_0(t)=\tfrac12\mathbf1_{[-1,1]}(t)\) and \(q_2(t)=\tfrac14(1-3t^2)\mathbf1_{[-1,1]}(t)\), whose Fourier transforms with phase \(e^{irt}\) are \(j_0(r)\) and \(j_2(r)\). For \(0\le s\le2\), their pairwise convolutions are
\[
\begin{aligned}
H_{00}(s)&=(2-s)/4,\\
H_{02}(s)&=s(s-2)(s-1)/8,\\
H_{22}(s)&=-(s-2)(3s^4+6s^3-8s^2-16s+8)/160.
\end{aligned}\tag{3}
\]
The convolutions are even and vanish off \([-2,2]\). One-dimensional Plancherel and differentiation give
\[
\int_0^\infty r^2j_aj_bj_cj_d\,dr
=2\pi\int_0^2 H_{ab}'(s)H_{cd}'(s)\,ds,
\]
for pairs \((a,b),(c,d)\) from \((0,0),(0,2),(2,2)\). Integrating the explicit polynomials verifies every value in (2). The derivative identities also justify the improper integrals by Plancherel.

**Exact quartic formula.** Multiply \(f\) by one complex unit scalar so \(a\ge0\) is real and write \(Q=U+iV\) with real \(U,V\in\mathcal H_2\). Set \(u=\|U\|_2\), \(v=\|V\|_2\), \(s=(u^2+v^2)^{1/2}\), and write \(\mathbb E\) for spherical averaging. Expanding \(|a j_0-j_2(U+iV)|^4\), then applying (2), yields the **identity**
\[
\frac{\|Tf\|_4^4}{\pi^2}
=a^4+\frac{a^2}{5}(6u^2+2v^2)
+\frac{4a}{7}\mathbb E[U(U^2+V^2)]
+\frac{11}{35}\mathbb E[(U^2+V^2)^2].\tag{4}
\]

**Quadrupolar angular bounds.** For each real \(W\in\mathcal H_2\), the spherical pairing formula for trace-free symmetric \(3\times3\) matrices and the trace identity \(\operatorname{tr}(A^4)=\tfrac12(\operatorname{tr}A^2)^2\) give
\[
\mathbb E W^4=\frac{15}{7}\|W\|_2^4,
\quad\|P_2(W^2)\|_2=\frac{2\sqrt5}{7}\|W\|_2^2.
\]
Thus \(|\mathbb E U^3|\le(2\sqrt5/7)u^3\) and \(|\mathbb E UV^2|\le (2\sqrt5/7)uv^2\), so
\[
\mathbb E[U(U^2+V^2)]
\le \frac{2\sqrt5}{7}u(u^2+v^2)
\le\frac{2\sqrt5}{7}s^3.\tag{5}
\]
Cauchy–Schwarz applied to \(U^2,V^2\) additionally gives
\[
\mathbb E[(U^2+V^2)^2]\le\frac{15}{7}(u^2+v^2)^2=\frac{15}{7}s^4.\tag{6}
\]
The equality condition for the sharp positive cubic moment of a nonzero real quadratic harmonic is uniaxial: diagonalizing its representing matrix, with fixed quadratic trace and zero trace, the cubic trace is largest exactly when two eigenvalues coincide. The positive normalized form is \(Y_u\). For (6), equality holds exactly when \(U\) and \(V\) are linearly dependent over \(\mathbb R\), since equality in Cauchy–Schwarz forces \(U^2\) and \(V^2\) proportional as polynomial functions on the sphere.

Substituting (5)–(6) and \(6u^2+2v^2\le6s^2\) in (4) gives
\[
\|Tf\|_4^4/\pi^2\le a^4+\tfrac65a^2s^2
+\tfrac{8\sqrt5}{49}as^3+\tfrac{33}{49}s^4.
\]
Because \(a^2+s^2=\|f\|_2^2\), division by \(\|f\|_2^4\) is (1). For \(a,s>0\), equality in the quadratic step requires \(V=0\), and in the cubic step requires \(U/s=Y_u\); conversely these data saturate every step. If \(a=0\), (6) shows exactly that \(Q\) is a complex scalar multiple of a real quadratic harmonic; if \(s=0\), the datum is constant. This completes the sharpness and equality classification.

## Verification
The standalone `CHECK.py` checks the polynomial convolutions (3), all four rational multiples of \(\pi\) in (2), sphere-moment and trace identities, the sharp cubic zonal value, and the exact quartic coefficient assembly in (1). Run `python CHECK.py` with Python 3 and SymPy. These exact computations support the displayed analytical argument; a finite checker does not prove the Cauchy–Schwarz bounds or exhaustive equality cases, which are proved above.

## Relationship to prior work
Tang and Xu's November 16, 2026 study establishes unrestricted sharp Fourier-extension inequalities for exponents strictly greater than four. Its Appendix B computes the degree-two weighted quadratic and cubic couplings and the angular fourth moment, but does not state the fixed-energy **ordinary fourth-power** profile (1), its additional pure-degree-two radial fourth integral, or the full complex equality classification of the constant–quadrupole band. The classical sharp quartic extension bound has the less informative constant \(\pi^2\) independent of \(\beta\). Related exact mixed radial–angular fourth-power profiles and pure-input harmonic fourth moments involve different norms and do not imply (1) without separate analysis.

## Limitations
The theorem is strictly about the finite band \(\mathcal H_0\oplus\mathcal H_2\). It does not give the optimal fixed-energy profile for unrestricted spherical data or other target exponents. Its originality assessment is limited to accessible indexed and primary material, so previously unindexed equivalent calculations remain possible. No independent validation of this finding is claimed.

## References
- H. Tang and Z. Xu, *Sharp Fourier Extension Inequalities on \(\mathbb S^2\) for All \(q>4\)*, arXiv:2611.20898v1 (first public version November 16, 2026), especially Sections 4.5 and Appendix B, https://arxiv.org/abs/2611.20898.
- D. Foschi, *Global maximizers for the sphere adjoint Fourier restriction inequality*, Journal of Functional Analysis 268 (2015), 690–702; preprint first circulated earlier. (Classical sharp quartic background.)
- *Sharp conditional fourth-power profile for spherical mixed Fourier extension*, published scientific note, November 2, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-conditional-fourth-power-profile-for-spherical-mixed-fouri--c3df597d1e06. (Different mixed norm.)
- *Sharp \(L^4/L^2\) norm and extremizers for degree-two spherical harmonics*, published scientific note, September 20, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-sharp-l4-degree-two-spherical-harmonics--d4106097159f. (Input sphere norm rather than extension norm.)
