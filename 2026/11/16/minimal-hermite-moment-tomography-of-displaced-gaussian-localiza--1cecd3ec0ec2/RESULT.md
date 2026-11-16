# Minimal Hermite moment tomography of displaced Gaussian localization balls

## Finding

For every integer \(d\ge1\), let \(\mathcal F_d\) be the Bargmann–Fock space on \(\mathbb C^d\) with Gaussian probability measure \(d\mu(z)=\pi^{-d}e^{-|z|^2}\,dV(z)\), and let \(T_B\) be the Toeplitz (Gaussian Gabor localization) operator with the indicator symbol of an **unknown Euclidean ball** \(B=B(c,r)\subset\mathbb C^d\), where \(c\in\mathbb C^d\) and \(0<r<\infty\). Write \(e_0=1\), \(e_j=z_j\) for \(1\le j\le d\). The \(d+1\) selected matrix coefficients
\[
\langle T_B e_0,e_0\rangle,\qquad \langle T_B e_j,e_0\rangle\quad(1\le j\le d)
\]
(with the inner product linear in its first variable) **uniquely determine the center and radius** among all nonempty balls. These are exactly \(2d+1\) real observations, and no family of fewer continuous real-valued observations can distinguish all such balls.

The inverse is globally the **unique unconstrained minimizer of an explicit convex functional**. Set \(n=2d\), identify \(\mathbb C^d\cong\mathbb R^n\), and write the observations as \(m=\int_Bd\mu\) and \(b=\int_B z\,d\mu\in\mathbb R^n\). Define, for \((t,u)\in\mathbb R\times\mathbb R^n\),
\[
\Psi(t,u)=\int_{\mathbb R^n}\big(t+u\cdot z-|z|^2\big)_+\,d\mu(z).
\]
The unique minimizer of \(\Psi(t,u)-tm-u\cdot b\) is \((t_*,u_*)\), and the original geometry is \(c=u_*/2\), \(r=\sqrt{t_*+|u_*|^2/4}\).

The observation map is a real-analytic local diffeomorphism. With \(\lambda=\int_{\partial B} \pi^{-d}e^{-|z|^2}\,dS(z)\) and \(\nu\) the corresponding probability measure on the boundary, its Jacobian determinant, with inputs \((r,c_1,\ldots,c_n)\) and outputs \((m,b_1,\ldots,b_n)\), is
\[
\boxed{\det D(m,b)=r^n\lambda^{n+1}\det\operatorname{Cov}_{\nu}(\omega)>0,\qquad \omega=(z-c)/r.}
\]
In one complex dimension, put \(a=|c|\), \(q=2ar\), and \(R_j=I_j(q)/I_0(q)\), where \(I_j\) is the modified Bessel function. Then \(\lambda=2r e^{-a^2-r^2}I_0(q)\) and the determinant equals
\[
\boxed{r^2\lambda^3\left(\frac{1+R_2}{2}-R_1^2\right)\frac{1-R_2}{2}.}
\]

## Assumptions and scope

The symbol is exactly the indicator of one nonempty bounded Euclidean ball in normalized time-frequency coordinates; the dimension is arbitrary but finite. The Gaussian density is strictly positive everywhere. The inner product convention is linear in the first argument, so \(\langle T_Be_j,e_0\rangle=\int_Bz_j\,d\mu\); for the opposite convention one reads its complex conjugate. The data are indexed operator matrix coefficients, **not** eigenvalues or an unordered spectrum. No unknown intensity scale multiplies the indicator symbol.

## Proof

**1. Moment identification.** Orthogonal projection in \(\mathcal F_d\) gives \(\langle T_Bf,g\rangle=\int_Bf\overline g\,d\mu\). Substituting \(f=e_0\) and \(f=e_j\), \(g=e_0\), gives exactly the observed mass and complex first moments. Thus the observations contain \(n+1=2d+1\) real numbers.

**2. Global injectivity.** Write a ball as the positivity set of \(q_{t,u}(z)=t+u\cdot z-|z|^2\), with \(u=2c\) and \(t=r^2-|c|^2\). For distinct nonempty balls \(B_1,B_2\), the affine function \(L=q_1-q_2\) is strictly positive on \(B_1\setminus B_2\) and strictly negative on \(B_2\setminus B_1\), outside boundaries of measure zero. The symmetric difference has positive measure; the fixed Gaussian density is positive. Therefore
\[
\int_{\mathbb R^n}L(z)(\mathbf1_{B_1}(z)-\mathbf1_{B_2}(z))\,d\mu(z)>0.
\]
If the mass and vector first moments agreed, the left side would be zero because \(L\) is affine, a contradiction. This argument holds for **any** strictly positive locally integrable density for which the displayed moments exist.

**3. Constructive convex inverse.** The positive-part function is convex; hence \(\Psi\) is finite and convex on all \(\mathbb R^{n+1}\). Differentiation under the integral (the quadratic zero set has measure zero, including the radius-zero case) yields \(\nabla\Psi(t,u)=(\int_{\{q>0\}}d\mu,\int_{\{q>0\}}z\,d\mu)\). For the true parameter, the gradient is \((m,b)\), so it minimizes the asserted convex functional. Any other minimizer would have the same gradient. Empty balls have gradient zero while \(m>0\); nonempty balls with matching gradient coincide by step 2, and the fixed coefficient of \(-|z|^2\) makes their \((t,u)\) parameters equal. Thus the minimizer is unique globally; **no initialization or geometric constraint** is required in the mathematical minimization statement.

**4. Local derivative and determinant.** For a deformation \((\delta r,\delta c)\) of the ball, the normal velocity at \(z=c+r\omega\) is \(\delta r+\delta c\cdot\omega\). Differentiating the moments by boundary transport gives
\[
\delta(m,b)=\int_{\partial B}\pi^{-d}e^{-|z|^2}(1,z)(\delta r+\delta c\cdot\omega)\,dS(z).
\]
Write \(z=c+r\omega\). Subtracting \(c\) times the first output row from the vector-moment rows, then factoring \(r\) from each of the \(n\) vector rows, shows the determinant is \(r^n\) times the determinant of \(\int_{\partial B}w(1,\omega)(1,\omega)^T\,dS\). Taking its Schur complement gives \(r^n\lambda^{n+1}\det\operatorname{Cov}_{\nu}(\omega)\). This covariance is positive definite: every nonzero linear functional of \(\omega\) is nonconstant on the full sphere and the boundary density is strictly positive. The determinant is therefore strictly positive. Analyticity follows from integrating the entire Gaussian over the translated and rescaled unit ball, locally uniformly in \(r>0\), and the real-analytic inverse-function theorem applies.

**5. Explicit planar formula.** Rotate \(c\) to \((a,0)\). On the boundary, \(w(c+r\omega)\) is proportional to \(e^{-2ar\cos\theta}\). The normalized first and second angular moments are \(\mathbb E\cos\theta=-R_1\), \(\mathbb E\cos^2\theta=(1+R_2)/2\), \(\mathbb E\sin^2\theta=(1-R_2)/2\), and the mixed covariance vanishes. Substitution proves the Bessel expression (including \(a=0\) by continuity).

**6. Optimality of the count.** The parameter space \(\mathbb R^n\times(0,\infty)\) is an open \((n+1)\)-manifold. An injective continuous map from it into \(\mathbb R^k\) for \(k\le n\) would, after adjoining zeros, contradict invariance of domain in \(\mathbb R^{n+1}\). Hence fewer than \(2d+1\) continuous real observations cannot identify every ball.

## Verification

The attached `check_gaussian_ball_tomography.py` evaluates independent Bessel-integral moment formulas in the planar case, compares finite-difference Jacobians to the explicit determinant, numerically inverts three off-center cases, and checks positive centered determinants in real dimensions \(2\), \(4\), and \(6\). It uses Python and `mpmath`; execute `python check_gaussian_ball_tomography.py`. These finite checks are supplementary and not proofs of global uniqueness or high-dimensional injectivity.

## Relationship to prior work

Jaming–Speckbacher (2019) study planar STFT sampling bounds and Hermite windows, not finite determination of an unknown ball from low Hermite matrix coefficients. The Gaussian/Fock correspondence underlying the coefficient formula is also developed by Kisil (2021). Knutsen (2022) studies norm bounds for localization on porous sets rather than inverse finite moments. Abreu–Dörfler (2012) recover disk geometry from an eigenfunction condition, which is different information. Gustafsson–He–Milanfar–Putinar (2000) analyze general planar moment reconstruction and uniqueness of polynomial-sublevel indicators using a **larger truncated moment array**, including a mixed quadratic moment; that general-domain result does not supply the three-real-observation ball theorem or its convex inverse and Jacobian. The 2026 inverse-localization preprint by Ramos concerns prescribed eigenfunction data; only its abstract was available for this comparison. This claim does **not** assert novelty of the elementary affine sign-separation argument in isolation.

## Limitations

Uniqueness assumes the symbol is a single ball with known unit contrast. It does not hold for arbitrary measurable regions from only these moments. The inverse is not globally uniformly well conditioned: the Jacobian approaches degeneracy as the radius tends to zero or the Gaussian mass becomes vanishingly small. Only **local** analytic stability is proved at each finite, positive-radius ball, without a universal noise constant or a globally characterized feasible data region. The optimality assertion concerns continuous scalar observations; discontinuous encodings are outside its scope. Historical priority remains provisional, particularly for folklore weighted centroid characterizations and specialist inverse-moment literature. No independent audit has been performed.

## References

- P. Jaming and M. Speckbacher, *Planar sampling sets for the short-time Fourier transform*, arXiv:1906.02964, first public version 2019-06-07, primary MSC 42C40.
- V. V. Kisil, *Cross-Toeplitz Operators on the Fock–Segal–Bargmann Spaces and Two-Sided Convolutions on the Heisenberg Group*, arXiv:2108.13710, first public version 2021-08-31.
- H. Knutsen, *A Fractal Uncertainty Principle for the Short-Time Fourier Transform and Gabor Multipliers*, arXiv:2204.03068, first public version 2022-04-06.
- L. D. Abreu and M. Dörfler, *An inverse problem for localization operators*, arXiv:1202.5841, 2012.
- B. Gustafsson, C. He, P. Milanfar, and M. Putinar, *Reconstructing planar domains from their moments*, Inverse Problems 16 (2000), 1053–1070, DOI 10.1088/0266-5611/16/4/312.
- J. P. G. Ramos, *Eigenfunctions, free boundaries, and time-frequency localization*, arXiv:2607.21590, 2026 (abstract-level comparison only).
