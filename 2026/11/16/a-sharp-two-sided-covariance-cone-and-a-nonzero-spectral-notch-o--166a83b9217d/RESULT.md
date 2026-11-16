# A sharp two-sided covariance cone and a nonzero spectral notch on hyperbolic three-space

## Finding
Let \(\mathbb H^3\) have constant sectional curvature \(-1\). For \(a>2\) and \(b\in\mathbb R\), define the real, invariant distance kernel
\[
K_{a,b}(p,q)=e^{-a\rho(p,q)}\bigl(1+b\cos\rho(p,q)\bigr),
\qquad \rho(p,q)=d_{\mathbb H^3}(p,q).
\]
Put \(B=a^2>4\), and for \(x\ge0\) define the following polynomials and their rational quotient:
\[
\begin{aligned}
D_0(x)&=(x+B+1)^2-4B,\\
N(x)&=(x+B+2)^2-8(B+1),\\
D_1(x)&=\bigl((x+B)^2+8B+4\bigr)^2-16B(x+B+2)^2,\\
R_B(x)&=\frac{D_0(x)N(x)}{D_1(x)}.
\end{aligned}
\]
All displayed denominators are strictly positive on the stated domain. There is a **unique positive** point \(x_B\) maximizing \(R_B(x)\) for \(x\ge0\), and \(R_B(x_B)>1\). Its value can be determined from a single positive root of the explicitly stated polynomial in the proof. The complete positive-semidefinite parameter region is
\[
\boxed{
-\frac1{R_B(x_B)}\le b\le
\begin{cases}
\displaystyle\frac{(B^2+4)^2}{(B-1)^2(4B+4-B^2)},&4<B<2+2\sqrt2,\\[4pt]
+\infty,& B\ge2+2\sqrt2.
\end{cases}}
\]
Here the infinite upper bound means there is **no upper constraint** on finite \(b\). At the negative endpoint, the spherical transform vanishes at exactly one *nonzero* positive frequency \(\lambda=\sqrt{x_B}\). When the finite positive upper endpoint exists, the transform vanishes exactly at frequency \(\lambda=0\). Each endpoint is included. Every admissible kernel is strictly positive definite on every finite set of distinct points and is \(C_0\)-universal on \(\mathbb H^3\). The universality conclusion follows from the previously established integrable-kernel theorem of Said, Da Costa, Steinert, and Mostajeran, rather than constituting a new general universality theorem.

## Assumptions and scope
The curvature is normalized to \(-1\), \(a>2\) and \(b\) is any real number. Positive semidefinite means that for every finite sequence of points and complex weights, the corresponding Hermitian distance-kernel Gram quadratic form is nonnegative. Repeated points are allowed. Strict positive definiteness means positivity for nonzero weights on pairwise distinct points. \(C_0\)-universality means that the real reproducing-kernel Hilbert space is uniformly dense in the real-valued continuous functions vanishing at infinity. No statement is made for \(a\le2\), other dimensions, or frequency modulations other than \(\cos\rho\).

## Proof
**1. Exact spherical transforms.** The principal-series spherical functions on \(\mathbb H^3\) are \(\varphi_\lambda(r)=\sin(\lambda r)/(\lambda\sinh r)\). Radial integration for \(a>2\) gives an absolutely convergent transform
\[
\widehat f(\lambda)=\frac{4\pi}{\lambda}\int_0^\infty f(r)\sinh r\sin(\lambda r)\,dr,
\qquad\lambda\ge0,
\]
with values at zero interpreted by continuity. Elementary Laplace integration yields, writing \(x=\lambda^2\),
\[
\widehat{e^{-ar}}(\lambda)=\frac{8\pi a}{D_0(x)}.
\]
For the modulated term, use \(e^{-ar}\cos r=\operatorname{Re}(e^{-(a-i)r})\) in the same convergent integral. If
\[
F(z,x)=\frac{8\pi z}{\bigl(x+(z-1)^2\bigr)\bigl(x+(z+1)^2\bigr)},
\]
then direct expansion of \(\operatorname{Re}F(a-i,x)\) gives
\[
\widehat{e^{-ar}\cos r}(\lambda)
=\frac{8\pi a}{D_0(x)}\,R_B(x).
\]
In particular,
\[
\widehat K_{a,b}(\lambda)
=\frac{8\pi a}{D_0(\lambda^2)}\bigl(1+b R_B(\lambda^2)\bigr).
\]
The positive factors can be checked without relying on numerical roots:
\[
D_0(x)=\prod_{\sigma\in\{-1,1\}}\bigl(x+(a+\sigma)^2\bigr)>0,
\]
\[
D_1(x)=\prod_{\sigma\in\{-1,1\}}
\left[\bigl(x+(a+\sigma)^2-1\bigr)^2+4(a+\sigma)^2\right]>0.
\]
The transform decays as \(O(\lambda^{-4})\), so spherical inversion is integrable against the \(\lambda^2d\lambda\) Plancherel measure. By the integrable Godement criterion (Da Costa et al.), this kernel is positive semidefinite exactly when \(1+bR_B(x)\ge0\) for all \(x\ge0\).

**2. The unique nonzero spectral maximum.** Differentiate the explicit rational function. Write \(u=B-4>0\) and
\[
R_B'(x)=\frac{2Q_B(x)}{D_1(x)^2},\qquad
Q_B(x)=\sum_{k=0}^{6}q_k(u)x^k.
\]
The complete exact coefficient list is
\[
\begin{aligned}
q_0(u)&=9u^6+235u^5+2362u^4+11784u^3+30528u^2+37488u+14752,\\
q_1(u)&=42u^5+855u^4+7032u^3+29304u^2+62080u+53744,\\
q_2(u)&=75u^4+1134u^3+6348u^2+15640u+14528,\\
q_3(u)&=60u^3+622u^2+1816u+1192,\\
q_4(u)&=15u^2+87u+138,\\
q_5(u)&=-6u-21,\qquad q_6(u)=-3.
\end{aligned}
\]
For every \(u>0\), coefficients \(q_0,\ldots,q_4\) are positive and \(q_5,q_6\) are negative. Descartes' rule of signs shows \(Q_B\) has at most one positive root counted with multiplicity. Since \(Q_B(0)>0\) and \(Q_B(x)\to-\infty\) as \(x\to\infty\), the intermediate value theorem gives exactly one such root, necessarily simple. Denote it \(x_B>0\). Thus \(R_B\) is strictly increasing before \(x_B\) and strictly decreasing thereafter.

Because numerator and denominator have the same leading coefficient, \(\lim_{x\to\infty}R_B(x)=1\). A strictly decreasing function with this limit is greater than one on the interval \((x_B,\infty)\); hence \(R_B(x_B)>1\). At the other endpoint,
\[
R_B(0)=\frac{(B-1)^2(B^2-4B-4)}{(B^2+4)^2},
\qquad
1-R_B(0)=\frac{6B^3+3B^2-4B+20}{(B^2+4)^2}>0.
\]
Therefore the global range of \(R_B\) on the half-line is exactly \([R_B(0),R_B(x_B)]\), with the minimum at zero and the maximum at the unique positive \(x_B\). When \(R_B(0)<0\), the sole negative side of the range is at the origin.

**3. Sharp cone and boundary zeros.** The condition \(1+bR_B(x)\ge0\) for the whole range is equivalent to
\[
b\ge-\frac1{R_B(x_B)},
\]
and, only if \(R_B(0)<0\), also \(b\le-1/R_B(0)\). The sign of \(R_B(0)\) is the sign of \(B^2-4B-4\). Its positive root is \(2+2\sqrt2\), and substituting the displayed expression for \(R_B(0)\) gives the advertised sharp upper bound. At the lower boundary, \(1+bR_B\) vanishes only at \(x_B>0\); when present, the upper boundary vanishes only at \(x=0\). Outside the cone the spherical transform is negative on an open set: either around \(x_B\) or at sufficiently small positive \(x\). Consequently positivity fails, not merely a finite-grid test.

**4. Strict positive definiteness and universality.** For \(a>2\), the kernel is continuous, invariant and vanishes at infinity. The radial density is absolutely integrable over \(\mathbb H^3\), because the volume growth is \(O(e^{2r})\) and \(|K_{a,b}(r)|\le (1+|b|)e^{-ar}\). Said et al. prove that every continuous integrable real invariant positive-definite kernel on a noncompact Riemannian symmetric space which is \(C_0\) is \(C_0\)-universal. Apply that already-published theorem to each admissible kernel. A nonzero finite sum of distinct point evaluations is a nonzero finite signed or complex measure, and universality implies its Gram quadratic form is positive (for complex weights, apply the real version to real and imaginary parts). Hence strict finite-site positivity holds at both spectral boundaries as well as in the interior.

## Verification
The standalone Python 3 script `check_hyperbolic.py` uses SymPy and mpmath to verify the complex-Laplace transform identity, its exact derivative polynomial, every Descartes coefficient and the zero-frequency ratio, plus 60 supplementary high-precision comparisons of the two transform calculations and sharp spectral bounds. Execute `python check_hyperbolic.py` in the same directory. The exact analytic argument, not any finite test, proves the global parameter classification. The published integrable Godement theorem and the published noncompact universality theorem are used as stated external mathematical premises.

## Relationship to prior work
Da Costa, Mostajeran, Ortega and Said (arXiv:2310.19270) prove the integrable Godement criterion and provide a general harmonic-analytic framework for invariant symmetric-space kernels; their primary emphasis includes the Gaussian and hyperbolic-secant kernels, not the explicit signed exponential–cosine cone classified here. Said, Da Costa, Steinert and Mostajeran (arXiv:2608.00010) prove the universality implication for integrable invariant kernels on noncompact symmetric spaces. The sharp positive-definite parameter interval and its nonzero spectral-notch obstruction are not stated by these general results.

A prior public published-finding corpus mathematical result, *Sharp oscillation threshold for exponentially damped geodesic covariance on hyperbolic three-space* (2026), analyzes the **pure** wave \(e^{-ar}\cos(\omega r)\) and gives a sharp oscillation-frequency threshold. That addresses the limit of pure modulation, not the signed affine mixture \(e^{-ar}(1+b\cos r)\). Indeed, where the pure \(\cos r\) kernel is not positive definite, a bounded positive mixing coefficient can still be admissible; at the other endpoint a negative mixing coefficient can generate an isolated **nonzero-frequency notch**. Neither signed boundary follows from positive-mixture closure alone. The preceding source does supply similar spherical-transform tools, which are reused with explicit credit.

## Limitations
The theorem is restricted to \(a>2\), the curvature-normalized \(\mathbb H^3\), and fixed unit cosine frequency. The polynomial root \(x_B\) is specified exactly and uniquely but has no claimed radicals formula. Earlier equivalent symbolic calculations or a stronger classification in literature not located by the stated searches remain priority risks. No independent audit or external certification has been performed. The published universality implication is not asserted as original.

## References
1. Salem Said, Nathaël Da Costa, Franziskus Steinert, Cyrus Mostajeran, *Universality of kernels on Riemannian symmetric spaces*, arXiv:2608.00010 (public arXiv date 2026-06-19), Sections 4 and 6. https://arxiv.org/abs/2608.00010
2. Nathaël Da Costa, Cyrus Mostajeran, Juan-Pablo Ortega, Salem Said, *Invariant kernels on Riemannian symmetric spaces: a harmonic-analytic approach*, arXiv:2310.19270 (public arXiv date 2023-10-30), Sections 3–4 and Appendix A. https://arxiv.org/abs/2310.19270
3. *Sharp oscillation threshold for exponentially damped geodesic covariance on hyperbolic three-space*, public published-finding corpus mathematics record, 2026-10-26.
