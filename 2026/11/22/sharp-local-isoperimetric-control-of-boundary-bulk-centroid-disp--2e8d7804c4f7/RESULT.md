# Sharp local isoperimetric control of boundary–bulk centroid displacement

## Finding
Let \(f\) be a nonzero real \(C^3\), \(2\pi\)-periodic function whose Fourier coefficients of orders \(0,1,-1\) vanish. For all sufficiently small positive \(\varepsilon\), let \(K_\varepsilon\subset\mathbb R^2\) be the strictly convex body with radial function \(\rho_\varepsilon(\theta)=1+\varepsilon f(\theta)\). Denote area by \(A_\varepsilon\), perimeter by \(L_\varepsilon\), the uniform-area centroid by \(c(K_\varepsilon)\), and the uniform-arclength boundary centroid by \(c(\partial K_\varepsilon)\). Then

\[
\lim_{\varepsilon\downarrow0}
\frac{L_\varepsilon\,\|c(\partial K_\varepsilon)-c(K_\varepsilon)\|}
{L_\varepsilon^2-4\pi A_\varepsilon}
<\frac{1}{4\pi}.
\]

The constant is nevertheless the **exact supremum** of these limits over all admissible nonzero \(f\):

\[
\boxed{\sup_{f\ne0}\lim_{\varepsilon\downarrow0}
\frac{L_\varepsilon\,\|c(\partial K_\varepsilon)-c(K_\varepsilon)\|}
{L_\varepsilon^2-4\pi A_\varepsilon}=\frac{1}{4\pi}.}
\]

No individual nonzero perturbation realizes this supremum. In particular, the optimal sequence requires increasingly high, increasingly numerous adjacent angular Fourier modes. A single nonzero harmonic gives a zero quadratic centroid-displacement term.

## Assumptions and scope
Write \(u(\theta)=(\cos\theta,\sin\theta)\), and identify \(\mathbb R^2\) with \(\mathbb C\). Define

\[
a_k=\frac{1}{2\pi}\int_0^{2\pi}f(\theta)e^{-ik\theta}\,d\theta,
\qquad a_{-k}=\overline{a_k},\qquad a_0=a_1=a_{-1}=0.
\]

Set
\[
E(f)=\sum_{k=2}^{\infty}(k^2-1)|a_k|^2>0,
\qquad Q(f)=\sum_{k=2}^{\infty}(k-1)(k+2)a_k\overline{a_{k+1}}.
\]

Both series converge absolutely for \(f\in C^3\). The omission of orders \(0\) and \(\pm1\) removes the infinitesimal uniform scaling and translation gauges of the disk; it is not a restriction on the higher shape frequencies. The result concerns fixed perturbation functions as \(\varepsilon\) tends to zero, not arbitrary large deformations or a globally uniform estimate for all convex bodies. Each \(f\) admits a small-enough interval of \(\varepsilon>0\) on which strict convexity holds.

More precisely, the complex centroid displacement and the isoperimetric deficit have the expansions

\[
c(\partial K_\varepsilon)-c(K_\varepsilon)
=\varepsilon^2 Q(f)+O_f(\varepsilon^3),
\quad
L_\varepsilon^2-4\pi A_\varepsilon
=8\pi^2\varepsilon^2 E(f)+O_f(\varepsilon^3).
\]

Thus the limit in the finding is exactly \(|Q(f)|/(4\pi E(f))\).

## Proof
**Convexity and moment formulas.** For a positive \(C^2\) radial function \(\rho\), the numerator of signed boundary curvature is \(\rho^2+2(\rho')^2-\rho\rho''\). For \(\rho=1+\varepsilon f\) it is \(1+O_f(\varepsilon)>0\); hence the radial body is strictly convex for sufficiently small \(\varepsilon\). The exact area, perimeter and complex moment identities are

\[
A=\tfrac12\int_0^{2\pi}\rho^2\,d\theta,\quad
L=\int_0^{2\pi}\sqrt{\rho^2+(\rho')^2}\,d\theta,
\]

\[
c(K)=\frac{1}{3A}\int_0^{2\pi}e^{i\theta}\rho^3\,d\theta,
\qquad
c(\partial K)=\frac1L\int_0^{2\pi}e^{i\theta}
\rho\sqrt{\rho^2+(\rho')^2}\,d\theta.
\]

**Second variation.** Using \(a_0=a_{\pm1}=0\) to eliminate constant and first-harmonic linear terms, uniform Taylor expansion gives

\[
A_\varepsilon=\pi+\frac{\varepsilon^2}{2}\int_0^{2\pi}f^2\,d\theta,
\qquad
L_\varepsilon=2\pi+\frac{\varepsilon^2}{2}\int_0^{2\pi}(f')^2\,d\theta+O_f(\varepsilon^3),
\]

\[
c(K_\varepsilon)=\frac{\varepsilon^2}{\pi}\int_0^{2\pi}e^{i\theta}f^2\,d\theta+O_f(\varepsilon^3),
\]

\[
c(\partial K_\varepsilon)=\frac{\varepsilon^2}{2\pi}
\int_0^{2\pi}e^{i\theta}\left(f^2+\tfrac12(f')^2\right)d\theta
+O_f(\varepsilon^3).
\]

Subtracting the centroids yields
\[
c(\partial K_\varepsilon)-c(K_\varepsilon)
=\frac{\varepsilon^2}{4\pi}
\int_0^{2\pi}e^{i\theta}((f')^2-2f^2)\,d\theta+O_f(\varepsilon^3).
\]

Fourier orthogonality selects precisely pairs of harmonic orders differing by one. The ordered contributions from the positive and negative frequencies give
\[
\frac1{4\pi}\int e^{i\theta}((f')^2-2f^2)\,d\theta
=\sum_{k\ge2}(k(k+1)-2)a_k\overline{a_{k+1}}=Q(f).
\]

Likewise, Parseval's formula gives
\[
L_\varepsilon^2-4\pi A_\varepsilon
=2\pi\varepsilon^2\int_0^{2\pi}((f')^2-f^2)\,d\theta+O_f(\varepsilon^3)
=8\pi^2\varepsilon^2 E(f)+O_f(\varepsilon^3).
\]

**Sharp upper bound and nonattainment.** Put \(e_k=k^2-1\), \(b_k=\sqrt{e_k}\,a_k\), and
\[
\gamma_k=\frac{(k-1)(k+2)}{\sqrt{(k^2-1)((k+1)^2-1)}}.
\]

For every \(k\ge2\), \(0<\gamma_k<1\), since \(e_ke_{k+1}-((k-1)(k+2))^2=2(k-1)(k+2)>0\). Consequently
\[
|Q(f)|\le\sum_{k\ge2}\gamma_k|b_k||b_{k+1}|
\le\left(\sum_{k\ge2}|b_k|^2\right)^{1/2}
\left(\sum_{k\ge2}|b_{k+1}|^2\right)^{1/2}
\le E(f).
\]

The first inequality is strict for a nonzero adjacent product, because its \(\gamma_k\) is strictly below one; if all adjacent products vanish, then \(Q=0<E\). Hence \(|Q(f)|<E(f)\) for every nonzero \(f\). This proves the strict inequality and nonattainment.

**Sharpness.** For any integers \(N\ge2\) and \(M\ge1\), take the real trigonometric polynomial
\[
f_{N,M}(\theta)=2\sum_{k=N}^{N+M}\frac{\cos(k\theta)}{\sqrt{k^2-1}}.
\]

It satisfies the gauge conditions and \(E(f_{N,M})=M+1\), while
\[
Q(f_{N,M})=\sum_{k=N}^{N+M-1}\gamma_k.
\]

As \(N\to\infty\) with fixed \(M\), \(Q/E\to M/(M+1)\), since \(\gamma_k\to1\). Letting \(M\to\infty\) gives \(\sup |Q|/E=1\). Every finite \((N,M)\) has strictly convex \(K_\varepsilon\) for sufficiently small \(\varepsilon\), so this constructs admissible witnesses and proves sharpness of \(1/(4\pi)\).

## Verification
The included standalone `verify.py` computes exact radial and boundary centroid integrals using periodic quadrature and independently compares them with the two Fourier coefficient formulas. It checks a two-harmonic case with exact leading coefficients, twelve seeded random complex Fourier configurations, and three explicitly constructed high-frequency packets demonstrating approach to the sharp spectral bound. Its completed run reports `PASS`. These finite numerical tests corroborate the formulas; the proof of sharpness and of the all-frequency bound is analytic.

## Relationship to prior work
Myroshnychenko, Ryabogin, Tatarko and Yaskin established a sharp global centroid-separation estimate relative to width in all dimensions. The earlier planar theorem of Nazarov, Ryabogin and Yaskin established the corresponding width and diameter constants in dimension two. Their cited statements concern unrestricted convex bodies and do not imply the present sharp *near-disk* second-order quotient against isoperimetric deficit. In particular, a constant-width or diameter inequality that stays positive at the disk does not supply the vanishing deficit dependence or the high-frequency sharp coefficient established here.

Alvino, Ferone and Nitsch obtained a sharp planar isoperimetric inequality involving Fraenkel asymmetry; that invariant differs from the displacement between boundary and area centroids. The present result evaluates a different, vector-valued geometric shape response and its optimal nonattained Fourier multiplier norm. No universal estimate away from the disk is inferred from this local theorem.

## Limitations
The \(C^3\) regularity, the zero low Fourier gauges, and the fixed-\(f\) limit are part of the theorem. The bound is the supremum over these infinitesimal deformations; there is no claim that the displayed constant bounds the quotient for all finite \(\varepsilon\). There is no exact maximizer among nonzero perturbations. The established literature comparison does not prove independent priority against every unindexed historic source; independent mathematical validation has not been performed.

## References
1. S. Myroshnychenko, D. Ryabogin, K. Tatarko, and V. Yaskin, *The sharp bound on the distance between the centers of mass of a convex body and its boundary*, arXiv:2611.11635v1, first posted 8 November 2026. https://arxiv.org/html/2611.11635v1
2. F. Nazarov, D. Ryabogin, and V. Yaskin, *On the maximal distance between the centers of mass of a planar convex body and its boundary*, arXiv:2305.15646v1, 25 May 2023; Discrete & Computational Geometry 73 (2025), 1016–1036. https://arxiv.org/pdf/2305.15646
3. A. Alvino, V. Ferone, and C. Nitsch, *A sharp isoperimetric inequality in the plane*, Journal of the European Mathematical Society 13 (2011), 185–206; first journal posting 21 October 2010. https://doi.org/10.4171/JEMS/248
