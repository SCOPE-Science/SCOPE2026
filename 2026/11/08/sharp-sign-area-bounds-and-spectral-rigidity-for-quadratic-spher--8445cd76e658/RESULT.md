# Sharp sign-area bounds and spectral rigidity for quadratic spherical harmonics

## Finding
Let \(\sigma\) denote normalized surface area on the unit two-sphere \(\mathbb S^2\). For any nonzero real symmetric trace-zero \(3\times3\) matrix \(A\), put \(h_A(\omega)=\omega^{\mathsf T}A\omega\) and \(p(A)=\sigma\{\omega\in\mathbb S^2:h_A(\omega)>0\}\). The following inequalities are sharp:
\[
1-\frac1{\sqrt3}\le p(A)\le\frac1{\sqrt3}.
\]
Equality at the upper endpoint holds precisely when \(A\) is a positive multiple of an orthogonal conjugate of \(\operatorname{diag}(1,1,-2)\); equality at the lower endpoint holds precisely when \(A\) is a positive multiple of an orthogonal conjugate of \(\operatorname{diag}(2,-1,-1)\). Every intermediate area fraction occurs.

Moreover, \(p(A)=1/2\) holds precisely when \(A\) has rank two, i.e. its eigenvalues are a nonzero scalar multiple of \((1,0,-1)\). In particular the largest possible global sign-area imbalance of a nonzero real quadratic spherical harmonic equals \(2/\sqrt3-1\).

There is an exact, strictly monotone spectral profile. For the two-nonnegative-eigenvalue branch, after orthogonal conjugacy and positive scaling, write \(A=\operatorname{diag}(u,1-u,-1)\), \(1/2\le u\le1\). Define
\[
H(u)=\frac1{2\pi}\int_0^{2\pi}\sqrt{\frac{c_u(\theta)}{1+c_u(\theta)}}\,d\theta,
\qquad c_u(\theta)=u\cos^2\theta+(1-u)\sin^2\theta.
\]
Then \(p(A)=H(u)\), \(H\) is continuous and strictly decreasing on \([1/2,1]\), and \(H(1/2)=1/\sqrt3\), \(H(1)=1/2\). Matrices in the opposite eigenvalue-sign branch satisfy \(p(A)=1-H(u)\) with the same spectral parameter. The following explicit rigidity bounds hold in the corresponding branches:
\[
\frac1{\sqrt3}-H(u)\ge \frac5{64\sqrt2}\left(u-\frac12\right)^2,
\qquad
(1-H(u))-\left(1-\frac1{\sqrt3}\right)\ge\frac5{64\sqrt2}\left(u-\frac12\right)^2.
\]
These are stability estimates rather than claims that the displayed quadratic coefficient is optimal.

## Assumptions and scope
All harmonic functions and matrices are real. The area measure \(\sigma\) has total mass one. Every real homogeneous quadratic harmonic on \(\mathbb R^3\), restricted to \(\mathbb S^2\), has the displayed form with \(A=A^{\mathsf T}\), \(\operatorname{tr}A=0\), because the Euclidean Laplacian of \(h_A\) is \(2\operatorname{tr}A\). The nonzero hypothesis rules out the identically zero polynomial. Multiplication of \(A\) by a positive scalar and orthogonal conjugation leave \(p(A)\) unchanged; negation exchanges its positive and negative regions.

## Proof
**Zero-set and spectral reduction.** A nonzero polynomial has zero surface area on \(\mathbb S^2\) (alternatively, parameterize the sphere and use that a nonzero real analytic function has null zero set). Thus \(p(-A)=1-p(A)\). The trace-zero symmetric matrix \(A\ne0\) has both positive and negative eigenvalues. If it has two nonnegative eigenvalues, denote them by \(a\ge b\ge0\), with the remaining eigenvalue \(-a-b\). Since \(a+b>0\), dividing by \(a+b\) gives the canonical diagonal form \(\operatorname{diag}(u,1-u,-1)\), \(u=a/(a+b)\in[1/2,1]\). If it has only one nonnegative eigenvalue, replace \(A\) by \(-A\) and apply the previous case. The zero eigenvalue case belongs to both descriptions and will be consistent.

**Exact sign-area profile.** Parameterize almost every \(\omega\in\mathbb S^2\) as \((\sqrt{1-z^2}\cos\theta,\sqrt{1-z^2}\sin\theta,z)\). Under normalized area measure, \(z\) and \(\theta\) are independent, uniform respectively on \([-1,1]\) and \([0,2\pi]\). For the canonical diagonal matrix,
\[
h_A(\omega)=c_u(\theta)(1-z^2)-z^2.
\]
Because \(c_u(\theta)\ge0\), this quantity is strictly positive if and only if \(|z|<\sqrt{c_u(\theta)/(1+c_u(\theta))}\), up to a null set. Conditioning on \(\theta\) gives exactly the integral defining \(H(u)\).

**Sharp endpoints and uniqueness.** Put \(g(c)=\sqrt{c/(1+c)}\), \(0\le c\le1\). On \((0,1]\),
\[
g'(c)=\frac1{2\sqrt c(1+c)^{3/2}}>0,
\quad g''(c)=-\frac{1+4c}{4c^{3/2}(1+c)^{5/2}}<0.
\]
As \(\theta\) varies uniformly, \(c_u(\theta)=1/2+(u-1/2)\cos(2\theta)\) has mean \(1/2\). Strict concavity and Jensen's inequality imply \(H(u)\le g(1/2)=1/\sqrt3\), with equality exactly for \(u=1/2\). Furthermore, for \(1/2<u<1\), pairing values of \(\cos2\theta\) with their negatives gives
\[
H'(u)=\frac12\,\mathbb E\big[T\{g'(1/2+(u-1/2)T)-g'(1/2-(u-1/2)T)\}\big]<0,
\]
where \(T=\cos2\theta\) has a symmetric nondegenerate distribution. Indeed, \(g'\) is strictly decreasing, so each paired integrand is negative except when \(T=0\). Dominated convergence yields continuity at both endpoints. Finally,
\[
H(1)=\frac2\pi\int_0^{\pi/2}\frac{\cos\theta}{\sqrt{1+\cos^2\theta}}\,d\theta
=\frac2\pi\arcsin(1/\sqrt2)=\frac12.
\]
This proves the strict profile, all two-nonnegative-branch equality cases, and the corresponding results for the negated branch. The two branches have overlapping midpoint exactly when a zero eigenvalue occurs. The intermediate value theorem proves that every area fraction in the sharp interval is realized.

**Quantitative stability.** The positive function \(-g''(c)\) is decreasing on \((0,1]\). Indeed its logarithmic derivative is \(4/(1+4c)-3/(2c)-5/(2(1+c))<0\), using \(4/(1+4c)<1/c\). Therefore \(-g''(c)\ge-g''(1)=5/(16\sqrt2)\). The elementary strong-concavity form of Jensen's inequality gives
\[
 g(\mathbb EC)-\mathbb Eg(C)\ge\frac5{32\sqrt2}\operatorname{Var}(C)
\]
for each random \(C\in[0,1]\); endpoints follow by continuity. Taking \(C=c_u(\theta)\) and using \(\operatorname{Var}(\cos2\theta)=1/2\) yields \(\operatorname{Var}(C)=(u-1/2)^2/2\), proving the displayed stability bounds. No finite grid or numerical integration is used in these universal arguments.

## Verification
Run `python3 positive_area_degree2_checker.py` from this directory. The script verifies both endpoint reductions and the curvature formula, compares angular-profile values across seven spectral parameters with the predicted strict ordering and stability bounds, and independently estimates four sign-area fractions by direct quasi-uniform sampling on the sphere. These finite numerical checks confirm formula consistency but do not replace the analytic proof of the universal inequalities, equality classifications, or quantified stability. The executable is self-contained, uses only Python's standard library, and has no external data dependencies.

## Relationship to prior work
Nazarov, Polterovich and Sodin study the sign-area asymmetry of eigenfunctions in disks centered on nodal lines, in a high-eigenvalue regime; their result is local and asymptotic rather than this global degree-two exact classification. Eremenko, Jakobson and Nadirashvili examine possible nodal-set topology on the sphere rather than sharp positive-domain area. The published analysis of spherical quadratic-form distributions by Saldanha and Tomei and the general density formulas of Hillier treat each **fixed** spectrum; their distributional setting includes the random variable here, but the inspected statements do not supply a sharp optimization over all trace-zero three-dimensional spectra or the rigidity estimate. The latter comparison is qualified by limited access to the full Saldanha--Tomei article. Existing sharp \(L^4\) estimates for degree-two harmonics concern norm moments rather than the sign-area functional, which cannot be recovered from a fixed even moment.

## Limitations
The theorem covers only the two-sphere, real degree-two spherical harmonics, the global zero-threshold sign partition and normalized area. It does not assert analogous sharp fractions for higher degrees, other spheres, displaced thresholds, or complex eigenfunctions. The coefficient in the explicit stability estimate is not asserted to be best possible. An equivalent historical formulation under quadratic-form sign probabilities or nodal areas may exist; the inaccessible full text of the Saldanha--Tomei paper remains a specific originality risk.

## References
1. F. Nazarov, L. Polterovich, M. Sodin, *Sign and area in nodal geometry of Laplace eigenfunctions*, arXiv:math/0402412 (first posted 2004-02-25), https://arxiv.org/abs/math/0402412.
2. A. Eremenko, D. Jakobson, N. Nadirashvili, *On nodal sets and nodal domains on the sphere and plane*, arXiv:math/0611627 (2006), https://arxiv.org/abs/math/0611627.
3. G. Hillier, *The Density of a Quadratic Form in a Vector Uniformly Distributed on the n-Sphere*, University of Southampton Discussion Paper No. 9902 (revised July 1999), https://eprints.soton.ac.uk/33137/1/9902.pdf; *Econometric Theory* 17 (2001), 1–28.
4. N. C. Saldanha, C. Tomei, *The accumulated distribution of quadratic forms on the sphere*, *Linear Algebra and its Applications* 245 (1996), 335–351.
