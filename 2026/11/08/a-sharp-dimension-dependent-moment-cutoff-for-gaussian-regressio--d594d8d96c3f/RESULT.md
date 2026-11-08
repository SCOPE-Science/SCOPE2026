# A sharp dimension-dependent moment cutoff for Gaussian regression control variates

## Finding

Fix integers \(d\ge2\) and \(n\ge d+1\). Let \(X_1,\ldots,X_n\) be independent \(N(0,I_d)\) vectors. For a nonzero symmetric real \(d\times d\) matrix \(A\), arbitrary \(b\in\mathbb R^d\), and \(c\in\mathbb R\), integrate
\[
f(x)=x^{\mathsf T}Ax+b^{\mathsf T}x+c,
\qquad \mu=\mathbb E f(X)=\operatorname{tr}A+c.
\]
Regress the observed values \(f(X_i)\) on an intercept and all \(d\) coordinates of \(X_i\) using ordinary least squares (OLS). Use its fitted intercept \(\widehat\mu\) as the same-sample regression-control-variate Monte Carlo estimate. Its design is full column rank almost surely. For **every real \(q>0\)**,
\[
\boxed{\mathbb E|\widehat\mu-\mu|^q<\infty\quad\Longleftrightarrow\quad q<n-d.}
\]
Thus, at \(n=d+1\) even the ordinary expectation of \(\widehat\mu\) is undefined; at \(n=d+2\) its expectation exists but its mean squared integration error is infinite. At \(n\ge d+3\), the mean squared error is finite. For \(n\ge d+2\),
\[
\boxed{\mathbb E\widehat\mu-\mu=-\frac{2}{n}\operatorname{tr}A.}
\]
The conclusion is unaffected by any linear term \(b^{\mathsf T}x\). In contrast, the ordinary sample-mean estimator of the quadratic integrand has moments of all orders.

The one-dimensional boundary is qualitatively different: for \(d=1\) and \(n\ge2\), all positive moments of the same OLS-intercept error are finite. If \(f(x)=a x^2+b x+c\), its exact mean squared error is
\[
\boxed{\mathbb E(\widehat\mu-\mu)^2
=a^2\left[\frac2n+\frac4{n^2}
+\frac{6(n-2)(n-1)}{n^2(n+1)(n+3)}\right].}
\]

## Assumptions and scope

All claims concern independent standard Gaussian inputs, a fixed nonzero symmetric quadratic coefficient \(A\), an unregularized full intercept-plus-linear-controls OLS fit using the same observations for fitting and integration, and finite integers \(n\ge d+1\). No noisy responses, sample splitting, pseudoinverse extension to \(n\le d\), regularization, or claim about other input distributions is included. Finite expectations are understood as absolute Lebesgue integrability, not symmetric principal values. An affine integrand with \(A=0\) is integrated exactly, which is why \(A\ne0\) is necessary.

Set \(m=n^{-1}\sum_iX_i\), let \(U\) be the \(n\times d\) centered design with rows \(U_i=X_i-m\), \(S=U^{\mathsf T}U\), and \(z_i=U_i^{\mathsf T}AU_i\). Define the centered quadratic regression slope
\[
\gamma=S^{-1}U^{\mathsf T}z.
\]
The base square-integrable comparator is the ordinary unbiased Monte Carlo estimator \(n^{-1}\sum_i f(X_i)\). The known-coefficient oracle subtracting \(b^{\mathsf T}X_i\) also has all moments and variance \(2\operatorname{tr}(A^2)/n\).

## Proof

**1. Exact decomposition.** Gaussian orthogonal projection shows that \(m\sim N(0,I_d/n)\) is independent of \(U\), and \(S\) has the \(d\)-variate Wishart law with \(n-1\) degrees of freedom; \(S\) is invertible almost surely. The centered response equals
\[
2m^{\mathsf T}AU_i+U_i^{\mathsf T}AU_i
-\frac1n\operatorname{tr}(AS)+b^{\mathsf T}U_i.
\]
Consequently the fitted slope is \(b+2Am+\gamma\). Subtracting its inner product with \(m\) from the response mean gives the exact identity
\[
\boxed{\widehat\mu=c+\frac1n\operatorname{tr}(AS)
-m^{\mathsf T}Am-m^{\mathsf T}\gamma.}\tag{1}
\]
The arbitrary \(b\) cancels. The terms other than \(m^{\mathsf T}\gamma\) are Gaussian polynomials and hence have moments of all orders.

**2. Sharp moments for \(\gamma\).** Orthogonally diagonalize \(A\), which preserves the Gaussian design and the fitted intercept. Work in the centered sample subspace \(H=\mathbf1_n^\perp\), dimension \(n-1\). Its \(d\) design columns \(u_1,\ldots,u_d\) are independent standard Gaussians on \(H\). Fix one column index \(j\). Condition on the other columns and set \(Y=\operatorname{span}\{u_k:k\ne j\}\); this has dimension \(d-1\) almost surely. Decompose \(u_j=v+w\), where \(v\in Y\), \(w\in W=H\cap Y^\perp\). Conditional on the other columns, \(v\) and \(w\) are independent standard Gaussian projections, and
\[
r:=\dim W=n-d,\qquad \|w\|\stackrel{\mathrm d}=\chi_r.
\]
The Frisch--Waugh--Lovell identity gives
\[
\gamma_j=\frac{w^{\mathsf T}z}{\|w\|^2}.
\]
With \(A\) diagonal, \(z=z_0+2\lambda_j(v\odot w)+\lambda_j(w\odot w)\), where \(z_0=\lambda_j(v\odot v)+\sum_{k\ne j}\lambda_k(u_k\odot u_k)\). Thus
\[
|\gamma_j|\le
\frac{\|z_0\|}{\|w\|}
+2|\lambda_j|\|v\|+|\lambda_j|\|w\|.
\tag{2}
\]
The random \(z_0\) and \(v\) have Gaussian-polynomial moments of every order and are independent of \(\|w\|\). Since \(\chi_r\) has finite negative \(q\)-moment exactly for \(q<r\), (2), for each \(j\), proves \(\mathbb E\|\gamma\|^q<\infty\) whenever \(0<q<r\).

For necessity, relabel a nonzero diagonal eigenvalue as \(\lambda_1\ne0\). Conditional on the remaining columns and \(v\), if \(P_Wz_0\ne0\), the numerator of \(\gamma_1\) has a nonzero first-order term along a cone of directions \(w/\|w\|\) of positive surface measure. For sufficiently small \(\|w\|\) inside that cone, \(|\gamma_1|\ge C/\|w\|\); integration against the \(r\)-dimensional Gaussian radial density diverges for every \(q\ge r\). This nondegeneracy event has positive probability for *every* nonzero \(A\): take \(u_2=(1,0,-1,0,\ldots,0)\), choose \(v=t u_2\), and the centered perpendicular vector \(h=(1,-2,1,0,\ldots,0)\). Choose the remaining \(d-2\) columns linearly independent in \(\{\mathbf1_n,u_2,h\}^\perp\), scaled arbitrarily small. Then
\[
h^{\mathsf T}z_0=2(\lambda_1t^2+\lambda_2)+o(1),
\]
which is nonzero for a suitable \(t\). Because \(n\ge d+1\), this configuration exists, and by continuity it has a positive-probability neighborhood. Therefore
\[
\boxed{\mathbb E\|\gamma\|^q<\infty\iff q<n-d.}\tag{3}
\]

**3. Transfer to the integration error.** Conditional on \(\gamma\), the independent Gaussian vector \(m\) gives
\[
\mathbb E_m|m^{\mathsf T}\gamma|^q
=\frac{\mathbb E|N(0,1)|^q}{n^{q/2}}\|\gamma\|^q.
\]
Combining (1), (3), and the fact that the remaining terms in (1) have all moments (using the triangle inequality for \(q\ge1\), or subadditivity for \(0<q<1\)), proves the if-and-only-if claim. In particular, no finite signed expectation can be assigned at \(n=d+1\) in the usual Lebesgue sense.

**4. Bias, finite risk and the one-dimensional exception.** When \(n-d>1\), the independent centered \(m\) makes \(\mathbb E(m^{\mathsf T}\gamma)=0\). Moreover \(\mathbb ES=(n-1)I_d\) and \(\mathbb E(m^{\mathsf T}Am)=\operatorname{tr}A/n\), giving the displayed bias. When \(n-d>2\), Gaussian odd moments and independence yield the exact positive-term decomposition
\[
\boxed{\mathbb E(\widehat\mu-\mu)^2
=\frac{2\operatorname{tr}(A^2)}n
+\frac{4(\operatorname{tr}A)^2}{n^2}
+\frac1n\mathbb E\|\gamma\|^2.}\tag{4}
\]
The last term is strictly positive for nonzero \(A\), by the nondegenerate residual witness above. It quantifies the extra risk from fitting controls on the integration sample.

For \(d=1\), writing \(u_i=X_i-m\), \(\gamma=a\sum_i u_i^3/\sum_i u_i^2\). The inequality \(|\sum u_i^3|\le \max_i|u_i|\sum u_i^2\) gives all positive moments. Using rotational symmetry on the sphere in \(\mathbf1_n^\perp\) and the sixth spherical moment pairing formula yields
\[
\mathbb E\left(\frac{\sum_i u_i^3}{\sum_i u_i^2}\right)^2
=\frac{6(n-2)(n-1)}{n(n+1)(n+3)}.
\]
Substituting in (4), which is now integrable for every \(n\ge2\), proves the one-dimensional formula.

## Verification

Run `python verify_gaussian_cv.py` with Python 3 and SymPy. It performs 509 exact rational/symbolic checks of (1) on full-rank finite designs with general symmetric \(A\) and arbitrary \(b,c\), the one-dimensional sixth-moment expression, and an explicit near-singular witness: with \(n=3\), \(d=2\), \(A=\operatorname{diag}(1,0)\), and centered columns \((1,0,-1)^{\mathsf T}+\varepsilon(1,-2,1)^{\mathsf T}\) and \((1,0,-1)^{\mathsf T}\), the first quadratic slope equals \(1/(3\varepsilon)-\varepsilon\). The infinite-dimensional family of \(q\)-moment statements is proved analytically through the \(\chi_{n-d}\) radial integral, **not** through those finite checks. Exact program output appears in `verification_output.txt`.

## Relationship to prior work

Portier and Segers (2018 preprint; later revision) explicitly identify the OLS intercept with same-sample Monte Carlo control variates and study asymptotic limits as the number of controls grows. Leluc, Portier and Segers (2019 preprint) develop OLS and other control-variate choices, with nonasymptotic analyses under assumptions including control-variate bounds. Si and coauthors (2020 preprint) study scalable stochastic optimization of control variates. Mourtada (2019 preprint) analyzes more general least-squares prediction risks and inverse sample-covariance moments, but not the exact deterministic Gaussian-quadratic fitted-intercept integration moment law. Their inspected presentations do not supply the precise all-positive-order moment threshold for a fixed Gaussian quadratic and simultaneous Gaussian linear controls; their broad OLS identities alone do not imply the singularity exponent without residual-geometry analysis. Related generic inverse-Wishart moment phenomena are classical and are not claimed original; the specific integration-estimator law, necessity for each nonzero quadratic matrix, all positive moments, and its one-dimensional exception are the subject here. A specialist finite-sample regression-control-variate derivation of the same result may exist outside the inspected sources.

## Limitations

This is an exact result for *unregularized, same-sample* OLS with standard Gaussian coordinates and a nonzero quadratic integrand. It does not establish analogous thresholds for bounded inputs, higher-degree polynomials, independent pilot fitting, ridge stabilization, nonlinear control bases, or arbitrary covariance matrices. The theorem is not a universal claim that regression controls worsen integration: it isolates a natural near-interpolation regime, and the comparison with the known-slope oracle does not resolve all possible alternative estimators. Independent external validation and exhaustive priority verification have not been performed.

## References

1. F. Portier and J. Segers, *Monte Carlo integration with a growing number of control variates*, first public arXiv preprint 2018-01-05, [arXiv:1801.01797](https://arxiv.org/abs/1801.01797); especially Sections 1--3 on the OLS-intercept formulation and asymptotic limits.
2. S. Leluc, F. Portier and J. Segers, *Control variate selection for Monte Carlo integration*, first public arXiv preprint 2019-06-26, [arXiv:1906.10920](https://arxiv.org/abs/1906.10920); especially its OLS definitions and nonasymptotic assumptions.
3. S. Si and coauthors, *Scalable Control Variates for Monte Carlo Methods via Stochastic Optimization*, first public arXiv preprint 2020-06-12, [arXiv:2006.07487](https://arxiv.org/abs/2006.07487).
4. J. Mourtada, *Exact minimax risk for linear least squares, and the lower tail of sample covariance matrices*, first public arXiv preprint 2019-12-23, [arXiv:1912.10754](https://arxiv.org/abs/1912.10754); especially the results on inverse sample-covariance moments and random-design regression risk.
