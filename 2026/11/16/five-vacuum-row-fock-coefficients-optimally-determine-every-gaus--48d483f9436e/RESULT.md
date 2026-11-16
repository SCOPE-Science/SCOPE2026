# Five vacuum-row Fock coefficients optimally determine every Gaussian-weighted ellipse

## Finding

Let \(\mathcal F\) be the analytic Bargmann–Fock space on \(\mathbb C\) with measure \(d\gamma(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\) and orthonormal monomials \(e_j(z)=z^j/\sqrt{j!}\). For a bounded measurable set \(E\), its localization Toeplitz operator is \(T_E=P_{\mathcal F}\mathbf 1_E P_{\mathcal F}\). Its calibrated vacuum-row measurements are

\[
M_j(E)=\int_E z^j\,d\gamma(z),\qquad j=0,1,2.
\]

Up to the known factors \(\sqrt{j!}\) and complex-conjugation convention, these are the three entries of \(T_E\) connecting the vacuum to the first two excited Fock modes. The first measurement is real. **The five real numbers**

\[
m(E)=(M_0,\Re M_1,\Im M_1,\Re M_2,\Im M_2)
\]

**determine every nondegenerate filled planar ellipse uniquely**. They are optimal: no continuous assignment of four or fewer real scalars identifies every such ellipse. The map is a smooth diffeomorphism onto its image, and reconstruction is the unique minimizer of a convex positive-part functional given below.

There is also a nonvanishing Jacobian and an explicit (not generally sharp) determinant lower bound. Unlike a circular aperture, the ellipse has an arbitrary center, aspect ratio, orientation, and size; no unknown contrast is permitted.

## Assumptions and scope

Identify \(z=x+iy\). An ellipse means the **open interior**

\[
E=\{X\in\mathbb R^2:(X-c)^TB(X-c)<1\},\quad X=(x,y)^T,
\]

where \(c\in\mathbb R^2\), \(B\) is a real symmetric positive-definite \(2\times2\) matrix, and all five parameters vary freely. Boundaries have Gaussian measure zero, so closed interiors give identical data.

Every ellipse has a unique normalized defining quadratic with quadratic coefficient of trace \(-1\):

\[
Q_\theta(X)=s+b_1x+b_2y-\tfrac12(x^2+y^2)+u(x^2-y^2)+2vxy
=s+b^TX-X^TAX,
\]

\[
A=\begin{pmatrix}\frac12-u&-v\\-v&\frac12+u\end{pmatrix},\qquad \operatorname{tr}A=1.
\]

The admissible parameters have \(u^2+v^2<1/4\) and

\[
R^2=s+c^TAc>0,\qquad c=\tfrac12 A^{-1}b.
\]

Then \(E=\{(X-c)^TA(X-c)<R^2\}\), and its semiaxes are \(R/\sqrt{\lambda_1(A)}\) and \(R/\sqrt{\lambda_2(A)}\). Conversely the original ellipse \((c,B)\) gives \(A=B/\operatorname{tr}B\), \(R^2=1/\operatorname{tr}B\), \(b=2Ac\), and \(s=R^2-c^TAc\).

Define the five real harmonic feature polynomials

\[
\psi(X)=(1,x,y,x^2-y^2,2xy)^T.
\]

Their integrals over \(E\) are exactly \(m(E)\) above. Note that the radial quadratic moment is **not observed**.

## Proof

**1. Injectivity.** Consider distinct ellipses \(E_i=\{Q_i>0\}\) in normalized form, and write \(P=Q_1-Q_0\). The radial quadratic term cancels because both matrices have trace one, so \(P=a\cdot\psi\) for one real vector \(a\). On \(E_1\setminus E_0\), \(P>0\), while on \(E_0\setminus E_1\), \(P<0\). Thus, if the ellipses have different interiors, then strict positivity of the Gaussian density gives

\[
\int_{\mathbb R^2}(\mathbf1_{E_1}-\mathbf1_{E_0})P\,d\gamma>0.
\]

If the five observations were equal, the same integral would instead be \(a\cdot(m(E_1)-m(E_0))=0\), a contradiction. If the ellipse interiors coincide, their two normalized quadratic equations coincide: affine-transferring the common boundary to the unit circle shows two degree-two polynomials vanishing on that circle differ by a scalar multiple of its defining equation; matching the traces fixes the scalar. Hence the map is injective.

**2. Sharp observation count.** The family \(\mathbb R^2\times\mathrm{Sym}^+_2\) is a connected five-dimensional open manifold. If a continuous injective map into \(\mathbb R^4\) existed, composing with the standard inclusion into \(\mathbb R^5\) would violate invariance of domain: its image would have to be open in \(\mathbb R^5\), but lies in a hyperplane. The same excludes fewer measurements. Our five observations attain the lower bound.

**3. Convex global reconstruction.** Let

\[
F(\theta)=\int_{\mathbb R^2}(Q_\theta(X))_+\,d\gamma(X),\qquad (q)_+=\max(q,0).
\]

On the convex domain \(u^2+v^2<1/4\) with \(s,b\) arbitrary, \(F\) is finite and convex; differentiation at nonempty ellipses yields \(\nabla F(\theta)=m(E_\theta)\). For the true data \(m_*=m(E_{\theta_*})\), pointwise convexity gives

\[
F(\theta)-\theta\cdot m_*\ge F(\theta_*)-\theta_*\cdot m_*.
\]

Equality requires that the defining quadratics have the same positivity set up to Gaussian null sets, since crossing a sign boundary makes the positive-part supporting inequality strict. The normalized-ellipse argument in Step 1 then forces \(\theta=\theta_*\). Thus this convex optimization has a **unique global minimizer**, without any other measured moment.

**4. Exact Jacobian and strict local stability.** Differentiating the moving-domain moments (equivalently differentiating the positive-part potential twice) gives

\[
J(\theta)=Dm(\theta)=\int_{\partial E}\frac{\psi(X)\psi(X)^T}{|\nabla Q_\theta(X)|}\,d\gamma_{\partial}(X),
\]

where \(d\gamma_{\partial}=\pi^{-1}e^{-|X|^2}\,d\sigma(X)\) is Gaussian-weighted arc length. Write

\[
X(\varphi)=c+RA^{-1/2}(\cos\varphi,\sin\varphi)^T.
\]

The coarea formula gives the exact boundary Gram representation

\[
J(\theta)=\frac{1}{2\sqrt{\det A}}\int_0^{2\pi}\psi(X(\varphi))\psi(X(\varphi))^T\frac{e^{-|X(\varphi)|^2}}\pi\,d\varphi.
\]

Suppose a linear combination of the features vanished on the ellipse boundary. After the affine change of variables to the unit circle, a quadratic vanishing on the whole circle is a scalar multiple of its defining quadratic. Transferring back, the combination must be a multiple of \(Q_\theta\). The former has zero quadratic trace while \(Q_\theta\) has trace \(-1\); hence the combination is zero. Therefore \(J\) is positive definite for every nondegenerate ellipse. The inverse function theorem and global injectivity prove smooth invertibility onto an open image.

For a fully explicit stability certificate put \(a_{\max}=R/\sqrt{\lambda_{\min}(A)}\). Because the Gaussian boundary weight is at least \(\pi^{-1}e^{-(|c|+a_{\max})^2}\), the Gram comparison and a trigonometric calculation yield

\[
\boxed{\displaystyle\det J(\theta)\ge
\frac{R^{12}}{64(\det A)^{13/2}}
\exp\bigl(-5(|c|+a_{\max})^2\bigr)>0.}
\]

For completeness, without the Gaussian weight the boundary Gram has determinant \(\pi^5R^{12}/[64(\det A)^{13/2}]\). To verify it, translation and rotation of the five-feature vector act by matrices of determinant one. On an axis-aligned ellipse with semiaxes \(a_1,a_2\), its nonconstant angular feature parts are \(a_1\cos\varphi\), \(a_2\sin\varphi\), \((a_1^2+a_2^2)\cos(2\varphi)/2\), \(a_1a_2\sin(2\varphi)\); together with the constant they are orthogonal. Their squared angular norms give \(\det\int\psi\psi^T d\varphi=\pi^5a_1^4a_2^4(a_1^2+a_2^2)^2/2\), and \(a_1^2a_2^2=R^4/\det A\), \(a_1^2+a_2^2=R^2/\det A\). Multiplying by the coarea prefactor five times gives the stated determinant.

## Verification

The standalone file `ellipse_moment_checker.py` implements deterministic Gauss–Legendre radial and trapezoidal angular integration under the standard Gaussian. It evaluates three noncircular, displaced ellipses, compares the **analytic boundary Gram** against centered finite differences of all five moment derivatives, confirms positive eigenvalues and the explicit determinant bound, and solves the convex moment objective numerically using its analytical gradient. Run with `python ellipse_moment_checker.py` after installing `numpy` and `scipy`. Its expected end line is `GAUSSIAN_ELLIPSE_FIVE_MOMENT_TOMOGRAPHY_PASS cases=3`. The all-ellipse theorem uses the analytical proof, not those finite checks.

## Relationship to prior work

The Gaussian STFT/Fock identification and planar concentration setting are standard; see Jaming–Speckbacher (2019). Abreu–Dörfler (2012) recover circular domains from a **Hermite eigenfunction condition**, not arbitrary ellipses from the five indicated matrix coefficients. Di Dio (2019) treats broad semialgebraic and Gaussian-weighted moment reconstruction, with substantially higher moment orders in the cited general boundary-polynomial criterion, rather than a sharp five-real-observation vacuum-row theorem. Classical unweighted shape-from-moments reconstruction is established in Gustafsson–He–Milanfar–Putinar (2000). The new assertion assessed here is restricted to the Gaussian-weighted **finite** moment map, its missing radial-quadratic measurement, global convex inversion, and exact boundary Gram positivity. Classical polynomial-threshold separation is used as a proof method, not itself claimed as a new technique.

## Limitations

The ellipse must be a single full-dimensional unit-contrast filled ellipse. The Gaussian weight and phase-space origin must be known, the complex phases of the moment coefficients calibrated, and boundaries ignored as null sets. No theorem about unions, annuli, arbitrary shape masks, unknown density, or noisy uniform stability is asserted. The determinant bound is positive but not globally uniform and is not claimed sharp. Historical priority remains provisional where older general shape-reconstruction results could contain equivalent specialized formulations. The numerical checker validates examples only.

## References

1. P. Jaming and M. Speckbacher, *Planar sampling sets for the short-time Fourier transform*, arXiv:1906.02964v1 (first public 2019-06-07), https://arxiv.org/html/1906.02964v1.
2. P. J. di Dio, *The multidimensional truncated Moment Problem: Shape and Gaussian Mixture Reconstruction from Derivatives of Moments*, arXiv:1907.00790v1 (first public 2019-06-28), https://arxiv.org/abs/1907.00790.
3. L. D. Abreu and M. Dörfler, *An Inverse Problem for Localization Operators*, arXiv:1202.5841 (2012), https://arxiv.org/abs/1202.5841.
4. B. Gustafsson, C. He, P. Milanfar and M. Putinar, *Reconstructing planar domains from their moments*, Inverse Problems 16 (2000), 1053–1070, https://doi.org/10.1088/0266-5611/16/4/312.
5. F. Palombi, S. Toti and R. Filippini, *Numerical Reconstruction of the Covariance Matrix of a Spherically Truncated Multinormal Distribution*, 2017, https://doi.org/10.1155/2017/6579537.
