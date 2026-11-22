# An off-antipodal optimal design for a sparse three-frequency Fourier band

## Finding
Let \(V=\operatorname{span}_{\mathbb C}\{1,e^{it},e^{3it}\}\) on the circle with normalized Haar measure. Observe the squared modulus continuously on two equal arcs of half-width \(a\), centered at \(\pm\theta/2\), where \(2a\le\theta\le\pi\) and \(0<a<\pi/2\). Let \(\lambda_{\min}(a,\theta)\) be the least concentration eigenvalue on \(V\), normalized by full-circle energy. Then
\[
\lim_{a\downarrow0}a^{-3}\max_{2a\le\theta\le\pi}\lambda_{\min}(a,\theta)
=\frac{2+4\sqrt{154}/7}{3\pi}.
\]
Every maximizing separation converges to the **non-antipodal** angle
\[
\theta_*=2\arccos\sqrt{\frac{\sqrt{154}-8}{20}}
=2.16401496685156\ldots\text{ radians}.
\]
For all sufficiently small positive \(a\), the maximizing separation is unique and satisfies \(\theta(a)=\theta_*+O(a^2)\). In contrast, antipodal placement has the exact least eigenvalue
\[
\lambda_{\min}(a,\pi)=\frac{2a-\sin(2a)}{\pi},
\]
so the optimal small-arc stability gain over antipodality is precisely
\[
\frac12+\frac{\sqrt{154}}7=2.27281052085584\ldots.
\]
This is an E-optimal concentration design for this sparse fixed Fourier support, not a claim about arbitrary supports or arc numbers.

## Assumptions and scope
The ambient circle is \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\), with \(dt/(2\pi)\). The Fourier basis \(1,e^{it},e^{3it}\) is orthonormal. Put
\[
 E_{a,\theta}=\{t:|t-\theta/2|_{\mathbb T}\le a\}\cup\{t:|t+\theta/2|_{\mathbb T}\le a\},
\]
where arcs have disjoint interiors. Set
\[
\lambda_{\min}(a,\theta)=\min_{c\in\mathbb C^3,\;\|c\|_2=1}\frac1{2\pi}\int_{E_{a,\theta}}\left|c_0+c_1e^{it}+c_3e^{3it}\right|^2dt.
\]
A common rotation and exchange of arcs do not affect the eigenvalues, so \(2a\le\theta\le\pi\) covers all equal-width two-arc geometries up to those symmetries. The frequency support is exactly \(\{0,1,3\}\), not the consecutive triple; it is the smallest primitive non-arithmetic three-frequency pattern by total span. The optimum and error statements are for \(a\to0\) with fixed frequencies; finite-width global optimality is asserted only for sufficiently small \(a\), with no numerical value claimed for the threshold of sufficiency.

## Proof
**1. Exact matrix and the point-null direction.** For Fourier frequencies \(k,h\in\{0,1,3\}\), integration gives the Hermitian real Gram entries
\[
G_{kh}(a,\theta)=\begin{cases}
2a/\pi,&k=h,\\
\displaystyle\frac{2\sin((k-h)a)\cos((k-h)\theta/2)}{\pi(k-h)},&k\ne h.
\end{cases}
\]
Write \(c=\cos(\theta/2)\) and \(u=c^2\). The polynomial
\[
 P_\theta(z)=(z^2-2cz+1)(z+2c)
=z^3+(1-4u)z+2c
\]
vanishes at both arc centers \(z=e^{\pm i\theta/2}\). Its coefficient vector \(v_\theta=(2c,1-4u,1)\) has squared norm
\[
 D(u)=16u^2-4u+2>0.
\]
For each center, the squared angular derivative \(|\partial_tP_\theta(e^{it})|^2\) equals \(4+28u-32u^2\). The sum over the two centers is \(8(1+7u-8u^2)\). Thus the normalized trial vector has captured energy
\[
\frac{a^3}{3\pi}F(u)+O(a^5),\qquad
F(u)=\frac{8(1+7u-8u^2)}{16u^2-4u+2}.
\]
The error is uniform for \(0\le u\le1\), since the polynomial and all derivatives through any fixed order are uniformly bounded and the centered arcs are symmetric.

**2. Matching least-eigenvalue asymptotic at fixed separated centers.** Fix \(0<\theta\le\pi\). Let \(w(t)=(1,e^{it},e^{3it})\) and \(t_\pm=\pm\theta/2\). Taylor integration gives, in operator norm,
\[
 G(a,\theta)=\frac a\pi A(\theta)+\frac{a^3}{3\pi}B(\theta)+O_\theta(a^5),
\]
where \(A=\sum_{\sigma=\pm} w(t_\sigma)^*w(t_\sigma)\) and
\[
 B=\sum_{\sigma=\pm}\left[w'(t_\sigma)^*w'(t_\sigma)
+\frac{w''(t_\sigma)^*w(t_\sigma)+w(t_\sigma)^*w''(t_\sigma)}2\right].
\]
Because the two center evaluations are linearly independent for \(0<\theta\le\pi\), \(A\) has rank two. Its nullspace is exactly the span of \(v_\theta\). For this vector the terms in \(B\) containing the evaluations vanish, so
\[
 \frac{v_\theta^*Bv_\theta}{\|v_\theta\|^2}=F(u).
\]
The simple isolated zero eigenvalue of \(A\) has an analytic perturbation under the parameter \(a^2\). Consequently its emerging eigenvalue in \(G\) is
\[
\lambda_{\min}(a,\theta)=\frac{a^3}{3\pi}F(\cos^2(\theta/2))+O_\theta(a^5).
\]
The same expansion, with its first two derivatives in \(\theta\), is uniform on every compact neighborhood within \((0,\pi]\) where the two evaluation rows remain independent. The other two eigenvalues have order \(a\), so the emerging eigenvalue is indeed the minimum for sufficiently small \(a\).

**3. Unique global limiting design, including moving centers.** Direct differentiation yields
\[
 F'(u)=-\frac{4(40u^2+32u-9)}{(8u^2-2u+1)^2}.
\]
On \([0,1]\), its denominator is positive and its numerator changes sign exactly once, at
\[
 u_*=\frac{\sqrt{154}-8}{20}\in(0,1).
\]
The derivative changes from positive to negative there, and \(F''(u_*)<0\). Substitution gives \(F(u_*)=2+4\sqrt{154}/7\). The trial-polynomial bound in Step 1 is uniform even when \(\theta\) depends on \(a\) and the centers nearly collide. Hence
\[
\limsup_{a\downarrow0} a^{-3}\max_{2a\le\theta\le\pi}\lambda_{\min}(a,\theta)
\le\frac{F(u_*)}{3\pi}.
\]
Evaluating the Step 2 asymptotic at the fixed interior angle \(\theta_*=2\arccos\sqrt{u_*}\) gives the reverse limit. Any maximizing \(\theta(a)\) must converge to \(\theta_*\): otherwise compactness and the uniform trial bound would give an upper coefficient strictly below \(F(u_*)\). In a fixed neighborhood of \(\theta_*\), the simple-eigenvalue analytic expansion from Step 2 holds in \(C^2\) with remainder \(O(a^2)\) after division by \(a^3\). Since the limiting profile has a nondegenerate strict maximum, this local profile is strictly concave for sufficiently small \(a\), so the global maximum is unique. Its critical-point equation and the nonzero second derivative imply \(\theta(a)=\theta_*+O(a^2)\).

**4. Exact antipodal benchmark.** At \(\theta=\pi\), the Gram entries connecting the zero frequency to the odd frequencies vanish. The odd-frequency pair has off-diagonal entry \(-\sin(2a)/\pi\), so the eigenvalues are \(2a/\pi\) and \((2a\pm\sin(2a))/\pi\). Thus the stated least eigenvalue is exact. As \(a\downarrow0\), it is \(4a^3/(3\pi)+O(a^5)\). Dividing the optimal leading coefficient by this constant gives \(F(u_*)/4=1/2+\sqrt{154}/7\).

## Verification
Execute `python3 repro/check.py` with packages listed in `repro/requirements.txt`. The script independently forms the exact Fourier Gram matrix, numerically integrates its entries, checks the symbolic polynomial factorization, derivative-norm identity, exact stationary point and optimum, tests convergence with its predicted quadratic error, checks the exact antipodal spectrum, and compares feasible finite-width designs against the predicted asymptotic optimum. The reproducible execution used 55 decimal digits in `mpmath` and passed 1,345 assertions. These calculations corroborate but do not replace the operator perturbation and global-optimization proof; in particular, finite grids cannot establish uniqueness for all small widths.

## Relationship to prior work
Faou and Le Henaff's generalized spectral concentration framework (arXiv:2410.01465, initial public version October 2, 2024) treats arbitrary masks and numerical eigenvector continuation, but does not optimize this finite sparse Fourier observation over two arc centers. Marceca, Romero and Speckbacher (arXiv:2301.11685) establish eigenvalue-counting bounds for broad Fourier concentration domains, not this exact least-eigenvalue design. Asipchuk and Drezels (arXiv:2211.03821) construct exponential Riesz bases on unions of intervals; their main theorems do not identify the present sparse finite-mode optimizer.

The public result *Sharp two-arc Fourier observability: a Legendre constant and asymptotic antipodal design* solves the **complete consecutive symmetric** Fourier band \(\{-m,\ldots,m\}\). The present support \(\{0,1,3\}\) is not an affine shift/dilation of a three-term arithmetic progression, and no subspace-minimum implication follows from optimization over a larger consecutive band. Its new conclusion is the sharp **off-antipodal** optimum. The public result *Exact spectral staircases for periodic narrow-arc Fourier observation* allows arbitrary sparse frequency sets, but fixes the observation centers to a cyclically equally spaced orbit; it does not optimize the separation. The public consecutive-three-mode antipodal theorem also has a different frequency support. None of the inspected statements entails this counterexample to extending antipodal optimality from consecutive to sparse triples.

## Limitations
The theorem concerns only two equal-width arcs, the three complex Fourier frequencies \(\{0,1,3\}\), and the limiting regime of shrinking arc width. The exact optimizing angle for arbitrary large \(a\) is neither claimed nor computed. The construction does not imply a general design rule for arbitrary sparse supports, multiple arcs, weighted measurements, or phase retrieval. Publication priority may still be affected by unindexed optimal-design literature; the theoretical proof and the best-knowledge literature comparison are not independent certification.

## References
- E. Faou and Y. Le Henaff, *A generalized spectral concentration problem and the varying masks algorithm*, arXiv:2410.01465, initially posted 2024-10-02. https://arxiv.org/abs/2410.01465
- F. Marceca, J. L. Romero and M. Speckbacher, *Eigenvalue estimates for Fourier concentration operators on two domains*, arXiv:2301.11685, initially posted 2023-01-27. https://arxiv.org/abs/2301.11685
- O. Asipchuk and V. Drezels, *Examples of exponential bases on unions of intervals*, arXiv:2211.03821, initially posted 2022-11-07. https://arxiv.org/abs/2211.03821
- *Sharp two-arc Fourier observability: a Legendre constant and asymptotic antipodal design*, public research record. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-two-arc-fourier-observability-a-legendre-constant-and-asym--900ee56c5370
- *Exact spectral staircases for periodic narrow-arc Fourier observation*, public research record. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-spectral-staircases-for-periodic-narrow-arc-fourier-observ--e95b9bae48f1
- *Antipodal two-arc observation uniquely optimizes three-mode Fourier stability*, public research record. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-antipodal-two-arc-observation-uniquely-optimizes-three-mode-four--87a22b9723ef
