# The four-sector quadratic-harmonic spectrum of coordinate-dominant spherical cells

## Finding
For every integer \(d\ge4\), let \(S^{d-1}\subset\mathbb R^d\) carry surface measure and let the single cubical Voronoi cell be
\[
C_d=\{x\in S^{d-1}:x_1\ge |x_j|\ (2\le j\le d)\}.
\]
Its area fraction is \(1/(2d)\). Let \(\mathcal H_2(\mathbb C^d)\) be the complex homogeneous harmonic quadratics, equipped with its full-sphere \(L^2\) norm. Its concentration operator \(T_d\) is specified by \(\langle T_df,g\rangle=\int_{C_d}f\bar g\,d\sigma\) with the full-sphere inner product on the left.

Let \(Y_1,\ldots,Y_d\) be independent chi-square variables with one degree of freedom, \(M=\max_jY_j\), and for \(y>0\) set
\[
a(y)=\mathbb E[Y_1\mid Y_1\le y],\qquad v(y)=\operatorname{Var}(Y_1\mid Y_1\le y).
\]
Then the **complete spectrum, in strictly decreasing order**, is
\[
\begin{aligned}
\lambda_{z,d}&=\frac{(d-1)\mathbb E[(M-a(M))^2]+\mathbb E[v(M)]}{4d^2},&&\text{multiplicity }1,\\
\lambda_{m,d}&=\frac{\mathbb E[M a(M)]}{2d},&&\text{multiplicity }d-1,\\
\lambda_{c,d}&=\frac{\mathbb E[a(M)^2]}{2d},&&\text{multiplicity }\binom{d-1}{2},\\
\lambda_{t,d}&=\frac{\mathbb E[v(M)]}{4d},&&\text{multiplicity }d-2.
\end{aligned}
\]
In particular, the displayed entries are exact one-dimensional quadratures in standard special functions: if \(F(y)=\operatorname{erf}(\sqrt{y/2})\) and \(f(y)=e^{-y/2}/\sqrt{2\pi y}\), then \(M\) has density \(d f(y)F(y)^{d-1}\), and
\[
a(y)=1-\frac{2yf(y)}{F(y)},\qquad
v(y)=3-\frac{(6y+2y^2)f(y)}{F(y)}-a(y)^2.
\]
The invariant eigenspaces, respectively, are
\[
\begin{split}
&\operatorname{span}\{(d-1)x_1^2-\sum_{j=2}^dx_j^2\},\\
&\operatorname{span}\{x_1x_j:2\le j\le d\},\\
&\operatorname{span}\{x_jx_k:2\le j<k\le d\},\\
&\bigl\{\sum_{j=2}^d b_jx_j^2:\sum_{j=2}^db_j=0\bigr\}.
\end{split}
\]
Consequently the exact sharp energy bounds for every nonzero \(h\in\mathcal H_2(\mathbb C^d)\) are
\[
\lambda_{t,d}\le\frac{\int_{C_d}|h|^2\,d\sigma}{\int_{S^{d-1}}|h|^2\,d\sigma}\le\lambda_{z,d}.
\]
The upper equality space is a single complex line; the lower equality space has complex dimension \(d-2\). The exact condition number is \(\kappa_d=\lambda_{z,d}/\lambda_{t,d}\), and
\[
\lambda_{z,d}\sim\frac{(\log d)^2}{d},\quad
\lambda_{m,d}\sim\frac{\log d}{d},\quad
\lambda_{c,d}\sim\frac1{2d},\quad
\lambda_{t,d}\sim\frac1{2d},\quad
\boxed{\kappa_d\sim2(\log d)^2}\qquad(d\to\infty).
\]

## Assumptions and scope
The cell is the **single positive** face, not the union of two antipodal faces. The harmonics are homogeneous of **exact degree two**, not all degrees up to two and not discretely sampled data. The statements hold for every integer dimension \(d\ge4\), for complex or real coefficients. The asymptotic is an ordinary limit over integer dimensions. Integrals and moments are with respect to unweighted spherical area; normalization of the area cancels from the Rayleigh quotient.

## Proof
**1. Gaussian reduction.** Write \(G=(G_1,\ldots,G_d)\) with independent standard Gaussians and \(Y_j=G_j^2\). For a homogeneous quadratic \(h\), polar independence of radius and direction gives
\[
\frac{\int_{C_d}|h(x)|^2\,d\sigma(x)}{\int_{S^{d-1}}|h(x)|^2\,d\sigma(x)}=
\frac{\mathbb E[|h(G)|^2\mathbf1_{C_d}(G)]}{\mathbb E|h(G)|^2}.
\]
Let \(R_d=\{|G_1|\ge\max_{j\ge2}|G_j|\}\). Since every quadratic is even under \(G\mapsto-G\), its numerator on \(C_d\) is exactly half that on \(R_d\). By exchangeability, \(\mathbb P(R_d)=1/d\). Conditional on \(R_d\), \(Y_1\) has the same law as \(M\), and the other \(d-1\) variables, given \(M=y\), are independent copies of \(Y\mid Y\le y\). Their Gaussian signs remain independent symmetric signs.

**2. Four orthogonal sectors.** Signed permutations of coordinates \(2,\ldots,d\) preserve both the full-sphere and regional Gram forms. The four displayed subspaces have pairwise zero Gram cross-terms by signs and permutation exchangeability. They span the trace-free quadratics, as their dimensions add to \(\binom{d+1}{2}-1\); within each, the region form is scalar by direct exchangeability. The relevant whole-Gaussian squared norms of the representative polynomials \((d-1)G_1^2-\sum_{j\ge2}G_j^2\), \(G_1G_2\), \(G_2G_3\), and \(G_2^2-G_3^2\) are \(2d(d-1)\), \(1\), \(1\), and \(4\). Conditioning as in step 1 yields exactly the four formulas above, including the factor \(1/2\) for the single positive cell.

**3. Strict ordering.** The truncated density is proportional on \((0,y)\) to \(t^{-1/2}e^{-t/2}\), so comparison to the \(t^{-1/2}\)-weighted law with decreasing factor \(e^{-t/2}\) gives \(0<a(y)<y/3\). The bounded-support variance inequality gives \(v(y)\le a(y)(y-a(y))<(y-a(y))^2\). This proves \(\lambda_{z,d}>\lambda_{t,d}\). Also \(y>a(y)\) implies \(\lambda_{m,d}>\lambda_{c,d}\).

To compare the two transverse sectors, write \(\mu_j(y)=\int_0^y t^j f(t)\,dt\) and \(F=\mu_0\). Integration by parts yields \(\mu_1=F-2yf\) and \(\mu_2=3\mu_1-2y^2f\); hence
\[
\mu_2F-3\mu_1^2=2yf(3\mu_1-yF)<0.
\]
Thus \(v(y)<2a(y)^2\), proving \(\lambda_{c,d}>\lambda_{t,d}\).

The remaining comparison is not a pointwise inequality in \(M\). Set \(m=d-1\), and define the finite, positive integrals
\[
B_0=2\int_0^\infty yf(y)^2F(y)^{m-1}\,dy,\quad
B_1=2\int_0^\infty y^2f(y)^2F(y)^{m-1}\,dy,\quad
C=4\int_0^\infty y^2f(y)^3F(y)^{m-2}\,dy.
\]
Repeated integration by parts, using \((yf)'=(1-y)f/2\) and \((y^2f)'=(3y-y^2)f/2\), gives for the antipodal union \(R_d\)
\[
\lambda_z(R_d)-\lambda_m(R_d)
=\frac{(m^2+4m+1)(B_1-B_0)+(m-1)C}{2d}.
\]
Indeed, the required region moments of the \(Y_j\) reduce to the four values \(\mathbb E[Y_1^2\mathbf1_R]=3/d+3mB_0+mB_1\), \(\mathbb E[Y_1Y_2\mathbf1_R]=1/d+mB_0-B_1\), \(\mathbb E[Y_2^2\mathbf1_R]=3/d-B_1-3B_0\), and \(\mathbb E[Y_2Y_3\mathbf1_R]=1/d-2B_0+C\). Since \(2yf(y)^2=e^{-y}/\pi\),
\[
B_1-B_0=\frac1\pi\int_0^\infty (y-1)e^{-y}F(y)^{m-1}\,dy>0
\]
for \(m\ge2\), by strict positive covariance of the increasing functions \(y\) and \(F(y)^{m-1}\) under an exponential random variable of mean one. Also \(C>0\). Halving the two region eigenvalues therefore proves \(\lambda_{z,d}>\lambda_{m,d}\). Combining the inequalities gives strict descending order in all permitted dimensions.

**4. Dimension asymptotics.** Standard elementary chi-square tail bounds imply \(M/\log d\to2\) in \(L^2\). Since \(a(y)\to1\), \(v(y)\to2\) as \(y\to\infty\), and the truncated first and second moments are uniformly bounded, \(a(M)\to1\) and \(v(M)\to2\) in all needed mean limits. The exact eigenvalue formulas give the four displayed asymptotics. Their strict ordering then gives the condition-number asymptotic, including its constant \(2\).

## Verification
The standalone file `verify_cube_voronoi.py` numerically integrates the exact one-dimensional formulas for several dimensions, verifies the trace \(\operatorname{tr}(T_d)=(\binom{d+1}{2}-1)/(2d)\), and compares the four eigenvalues with a separate Gaussian Sobol-quadrature implementation on the original cone. In dimension three (used only as a check, not as a newly claimed dimension), the values reduce to known exact cubed-sphere-face constants. These finite computations corroborate but do not replace the all-dimensional proof. Running `python verify_cube_voronoi.py` requires Python 3, NumPy and SciPy.

## Relationship to prior work
Hamann, Le Gia, Sloan and Womersley (2023) study reconstructing masked spherical fields through Fourier analysis, including a general masking matrix; their worked numerical masks are smooth and axial on \(S^2\), not coordinate-maximal cells in variable dimension. Cheong and Kang (2015) study discrete Laplace eigensolutions on a cubed-sphere grid, rather than this continuous concentration form. A previously available dimension-three exact single-face quadratic spectrum is a specialization and is **not** claimed as new. Other established results for spherical orthants, quarter-wedges and antipodal caps involve different regions. The contribution here is the all-dimensional coordinate-maximum cell, the strict four-sector ordering and the sharp logarithmic-squared conditioning law.

## Limitations
This is a pure degree-two continuous-observation result. It does not establish reconstruction from finitely many samples or generalize to higher harmonic degrees. The eigenvalues are exact one-dimensional special-function integrals, not asserted to have elementary expressions at general dimension. Historical priority cannot be certified exhaustively; an unindexed equivalent result would supersede the novelty assessment.

## References
1. J. Hamann, Q. T. Le Gia, I. H. Sloan, R. S. Womersley, *Removing the mask -- reconstructing a scalar field on the sphere from a masked field*, arXiv:2309.14815, first posted 2023-09-26, https://arxiv.org/abs/2309.14815 .
2. H.-B. Cheong and H.-G. Kang, *Eigensolutions of the spherical Laplacian for the cubed-sphere and icosahedral-hexagonal grids*, Quarterly Journal of the Royal Meteorological Society 141 (2015), 3383–3398, https://doi.org/10.1002/qj.2620 .
3. C. Gerhards and X. Huang, *Slepian spatiospectral concentration problem on the d-dimensional ball for different notions of bandwidth*, arXiv:2308.03543 (2023), https://arxiv.org/abs/2308.03543 . (Different ambient ball operator.)
