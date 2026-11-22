# A two-bond spectral threshold and critical doublet law for weighted shifts

## Finding
Let \(m\ge2\) be an integer and \(a>1\). On \(\ell^2(\mathbb Z)\), let \(J_{m,a}\) be the bounded self-adjoint Jacobi operator with zero diagonal and off-diagonal weights \(a/2\) at the bonds \((0,1)\), \((m,m+1)\), and \(1/2\) on every other bond. Put \(\beta=a^2-1\). Define \(z_+\in(0,1)\) as the unique solution of
\[
a^2z_+^2+\beta z_+^{m+1}=1,
\]
and, when it exists, \(z_-\in(0,1)\) as the nontrivial solution of
\[
a^2z_-^2-\beta z_-^{m+1}=1.
\]
Then the complete spectrum is \([-1,1]\) together with exactly the simple pair \(\pm\lambda_+\), and, if and only if \(\beta>2/(m-1)\), the additional simple pair \(\pm\lambda_-\), where
\[
\lambda_\pm=\frac{z_\pm+z_\pm^{-1}}2>1,\qquad\lambda_+>\lambda_-.
\]
At equality \(\beta=2/(m-1)\), the second channel has a band-edge resonance but no square-summable eigenvector. There are no other eigenvalues, including at the band edges or inside the band.

The two modes satisfy two quantitatively distinct separation laws.

**Fixed-enhancement tunneling.** For each fixed \(a>1\), as \(m\to\infty\), the two positive outliers exist and obey
\[
\lambda_\pm\longrightarrow\frac{a+a^{-1}}2,\qquad
\lambda_+-\lambda_-\sim\frac{(a^2-1)^2}{2a^{m+2}}.
\]

**Critical weak-enhancement window.** Fix \(\gamma>0\) and put \(a_m=\sqrt{1+\gamma/m}\). There is always a positive outlier \(\lambda_+(m,a_m)\), with
\[
\lim_{m\to\infty}m^2(\lambda_+(m,a_m)-1)=\frac{\kappa_+(\gamma)^2}{2},
\qquad 2\kappa_+=\gamma(1+e^{-\kappa_+}),\ \kappa_+>0.
\]
A second positive outlier exists eventually if and only if \(\gamma>2\). In that case,
\[
\lim_{m\to\infty}m^2(\lambda_-(m,a_m)-1)=\frac{\kappa_-(\gamma)^2}{2},
\qquad 2\kappa_-=\gamma(1-e^{-\kappa_-}),\ \kappa_->0.
\]
Each of the two scalar equations has exactly one strictly positive solution on the stated parameter domain. For \(0<\gamma\le2\), there is no second positive outlier for any \(m\ge2\). In addition, as \(\gamma\downarrow2\) from above, \(\kappa_-(\gamma)/(\gamma-2)\to1\), so the second scaled gap vanishes quadratically at the critical value.

Let \(W_{L,m,a}\) be the unilateral weighted forward shift on \(\ell^2(\mathbb N_0)\) whose weights equal \(a\) at positions \(L\) and \(L+m\) and equal \(1\) elsewhere. The bulk limiting numerical radius is exactly
\[
\lim_{L\to\infty}w(W_{L,m,a})=\lambda_+(m,a).
\]
Thus the spectral threshold describes a second localized mode in the bulk limit of a natural two-defect shift, not a threshold for the numerical radius alone (which is set by the upper mode).

## Assumptions and scope
The sequence index convention is \(\mathbb Z\) for the bilateral Jacobi operator and \(\mathbb N_0\) for the unilateral weighted shift. The bond \((j,j+1)\) has Jacobi coefficient \(w_j/2\). All weights are strictly positive; both exceptional weights have the same value \(a>1\). The distance \(m\) counts the displacement of the bond indices, not the number of untouched bonds (which is \(m-1\)). The finite-distance assertions hold for every integer \(m\ge2\), including at strict and equality thresholds. The two asymptotics use different quantifiers: fixed \(a\) as \(m\to\infty\), or fixed \(\gamma\) and \(a_m^2=1+\gamma/m\) as \(m\to\infty\). The numerical-radius limit holds for each fixed pair \((m,a)\) as \(L\to\infty\).

## Proof
**1. Reduction to one real dispersion parameter.** The free bilateral Jacobi operator has spectrum \([-1,1]\). Changing two off-diagonal coefficients is finite rank, so the essential spectrum of \(J_{m,a}\) is unchanged. The nonzero diagonal-alternation unitary \((Ux)_j=(-1)^jx_j\) conjugates \(J_{m,a}\) to \(-J_{m,a}\), giving spectral symmetry. A solution with \(|\lambda|<1\) is oscillatory on either free half-line, and at \(\lambda=\pm1\) it is affine (with alternating signs at the lower endpoint); square summability forces it to vanish on both tails and then everywhere. Thus point spectrum can occur only outside the band. For \(\lambda>1\), there is a unique \(z\in(0,1)\) such that \(2\lambda=z+z^{-1}\). On each free exterior half-line a square-summable solution is a scalar multiple of the corresponding decaying geometric tail.

**2. Exact two-channel equation.** Let \(u\) be such a solution. The left tail gives \(u_{-1}=zu_0\). The equation at site \(0\) gives \(u_0=az u_1\); analogously, at site \(m+1\) it gives \(u_{m+1}=az u_m\). Hence the free recurrence on interior sites \(1,\ldots,m\) has formal boundary conditions \(u_0^{\mathrm{eff}}=a^2zu_1\) and \(u_{m+1}^{\mathrm{eff}}=a^2zu_m\). A general interior solution is \(u_j=A z^{j-1}+Bz^{-(j-1)}\). The left condition is
\[
A(1-a^2z^2)=B\beta z^2,
\]
and the right condition is
\[
B(1-a^2z^2)=A\beta z^{2m}.
\]
The determinant vanishes precisely when
\[
(1-a^2z^2)^2=\beta^2 z^{2m+2},
\]
that is, \(1-a^2z^2=\pm\beta z^{m+1}\). Conversely each interior root gives a nonzero square-summable solution with geometric exterior tails. The plus sign in \(a^2z^2\pm\beta z^{m+1}=1\) is the symmetric positive eigenmode, the minus sign the antisymmetric one. Their eigenvalues are simple, since a decaying left exterior tail determines the entire recurrence up to one scalar.

**3. Root count and sharp threshold.** The function \(z\mapsto a^2z^2+\beta z^{m+1}\) is strictly increasing from zero to \(2a^2-1>1\), so it has exactly one root \(z_+\in(0,1/a)\). For the second branch, roots lie in \((1/a,1)\). Rearranging gives
\[
\beta=a^2z^{-(m-1)}-z^{-(m+1)}=:F(z).
\]
On \((1/a,1)\), \(F\) starts at zero, finishes at \(\beta\), and its derivative has the sign of \((m+1)-(m-1)a^2z^2\). Therefore \(F\) rises and then falls, creating exactly one interior solution to \(F(z)=\beta\) if and only if \((m-1)\beta>2\); otherwise it never crosses the terminal value before \(z=1\). Equality corresponds to the root \(z=1\), whose exterior tails are constant, not square summable. Because \(z_+<1/a<z_-<1\), and \(z\mapsto(z+z^{-1})/2\) strictly decreases on \((0,1)\), \(\lambda_+>\lambda_-\). The two exterior tails and this full root count exclude any additional eigenvalues.

**4. Fixed-amplitude splitting.** Fix \(a>1\) and set \(z_0=1/a\). Both roots tend to \(z_0\), since the perturbations \(\pm\beta z^{m+1}\) vanish uniformly on any compact subinterval of \((0,1)\). Taylor expansion of the two secular equations at \(z_0\), together with \(m a^{-m}\to0\), gives
\[
z_+=z_0-\frac{\beta}{2a^{m+2}}(1+o(1)),\qquad
z_-=z_0+\frac{\beta}{2a^{m+2}}(1+o(1)).
\]
Since the derivative of \((z+z^{-1})/2\) at \(z_0\) is \(-\beta/2\), the asserted splitting follows. The individual eigenvalue limits follow by continuity.

**5. Coupled weak-defect/separation scaling.** Fix \(\gamma>0\), write \(\beta=\gamma/m\), and parameterize each root as \(z=e^{-\kappa/m}\). The secular equations become
\[
m(1-e^{-2\kappa/m})=\gamma\bigl(e^{-2\kappa/m}\pm e^{-(m+1)\kappa/m}\bigr).
\]
For each fixed \(\kappa>0\), these converge to \(2\kappa=\gamma(1\pm e^{-\kappa})\). The plus equation has one positive solution because its left-minus-right side is strictly increasing from \(-2\gamma\) to infinity. The minus equation has a strictly positive solution exactly for \(\gamma>2\): its left-minus-right side is strictly convex, vanishes at zero, has derivative \(2-\gamma\) there, and tends to infinity. The finite root threshold \(\gamma/m>2/(m-1)\) coincides with the eventual split at \(\gamma=2\). Convergence of the roots to the respective positive limiting roots follows by sign bracketing and uniqueness; the root parameters remain in bounded intervals for fixed \(\gamma\). Since \(\lambda=\cosh(\kappa/m)\), the scaled gap limits follow. Expanding \(1-e^{-\kappa_-}=\kappa_--\kappa_-^2/2+O(\kappa_-^3)\) as \(\gamma\downarrow2\) yields \(\kappa_-/(\gamma-2)\to1\).

**6. Unilateral bulk-radius connection.** A bounded unilateral weighted shift has circular numerical range and numerical radius equal to the norm of its Hermitian part. After translation, \((W_{L,m,a}+W_{L,m,a}^*)/2\) is the compression of \(J_{m,a}\) to the subspace spanned by coordinates \(j\ge-L\). These subspaces increase densely as \(L\to\infty\), so the operator norms of the compressions increase to \(\|J_{m,a}\|=\lambda_+\), proving the formula for the bulk limiting numerical radius.

## Verification
The supplementary Python program `verify.py` constructs finite tridiagonal matrices independently of the closed-form equations, compares the predicted isolated eigenvalues with finite-section eigensolvers for 42 parameter pairs, checks the sharp two-mode threshold, tests the exponentially small split in nine parameter pairs, and checks the two critical scaling branches for five coupling values. These computations are consistency tests rather than proofs of spectral completeness, infinite limits, or originality. The mathematical proofs are Steps 1–6 above. Running `python verify.py` with Python 3, NumPy and SciPy prints `CHECKS PASSED` after all assertions.

## Relationship to prior work
Sharif, arXiv:2303.00876 (initial public version March 2, 2023), studies numerical radii of weighted shifts as a norm, periodic examples, and Banach-limit inequalities; it does not give the two-separated-defect mode-count threshold or the joint critical scaling. Chakraborty, Ojha, and Birbonshi (2022) develop determinantal polynomials for arbitrary finite prefixes followed by periodic tails. Their method can in principle characterize eigenvalues of any fixed unilateral finite-prefix defect configuration, but their displayed theorems and examples do not give the explicit two-bond bulk mode-count threshold, tunneling coefficient, or scale \(a_m^2=1+\gamma/m\). Webb and Olver (2021) give a general finite-rank Jacobi connection-coefficient spectral algorithm; the present secular equation is consistent with that framework, while the exact count and coupled-limit classification require additional analysis. A published treatment of adjacent exceptional shift weights gives a boundary location threshold, not the nonadjacent bilateral two-channel transition. The 2023 subwavelength double-defect analysis has a qualitatively analogous one-versus-two-mode transition for a different defect operator. Thus the claimed contribution is the closed analytic nonadjacent *bond*-defect spectral classification and two sharp separation regimes, not the general Jacobi finite-rank method or the qualitative existence of defect hybridization.

## Limitations
The formula assumes two identical enhanced real bond weights and a free one-dimensional background; it is not an arbitrary unequal or signed finite perturbation theorem. No quantitative finite-boundary convergence rate is claimed for the unilateral shift. Finite sections cannot establish absence of hidden eigenvalues, which follows analytically from the secular equations. Broad finite-rank Jacobi algorithms and specialized bond-impurity literature remain a historical-priority risk even after the targeted comparisons.

## References
1. A. Sharif, *On the numerical radius of weighted shifts on \(\ell^2\) as a norm on \(\ell^\infty\) and connections to Banach limits*, arXiv:2303.00876 (initially posted March 2, 2023), https://arxiv.org/abs/2303.00876.
2. B. Chakraborty, S. Ojha, and R. Birbonshi, *Numerical radius of weighted shift operators using determinantal polynomials*, Operators and Matrices 16 (2022), 1155–1174, DOI:10.7153/oam-2022-16-75, https://files.ele-math.com/articles/oam-16-75.pdf.
3. M. Webb and S. Olver, *Spectra of Jacobi Operators via Connection Coefficient Matrices*, Communications in Mathematical Physics 382 (2021), 657–707, DOI:10.1007/s00220-021-03939-w, https://link.springer.com/article/10.1007/s00220-021-03939-w.
4. A. Vandanjav and B. Undrakh, *On the numerical range of some weighted shift matrices and operators*, Linear Algebra and Its Applications 449 (2014), 76–88, DOI:10.1016/j.laa.2014.02.018.
5. *Boundary thresholds and exponential saturation for two-bond weighted shifts*, published mathematical research record (October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-boundary-thresholds-and-exponential-saturation-for-two-bond-weig--89bd59407b31.
6. *Sharp quadratic emergence of localized states from arbitrary multi-impurity thresholds*, published mathematical research record (November 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-quadratic-emergence-of-localized-states-from-arbitrary-mul--6579965f42ff.
7. *Anderson Localization in the Subwavelength Regime*, Communications in Mathematical Physics (2023), Section 4.2, DOI:10.1007/s00220-023-04880-w, https://link.springer.com/article/10.1007/s00220-023-04880-w.
