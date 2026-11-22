# Sharp two-scale subtraction and critical rigidity of circle Poisson covariances

## Finding
On \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) define the Poisson kernel
\[
P_t(\theta)=\frac{1-t^2}{1-2t\cos\theta+t^2}
=\sum_{n\in\mathbb Z}t^{|n|}e^{in\theta},\qquad 0\le t<1,
\]
with \(0^0=1\). For \(0<r<1\), \(0\le s\le r\) and real \(\gamma\), consider the nonstationary symmetric kernel
\[
K_{r,s,\gamma}(x,y)=P_r(x-y)-\gamma\cos x\cos y\,P_s(x-y).
\]
**Theorem.** This kernel is positive semidefinite on every finite subset of the circle if and only if \(\gamma\le\Gamma(r,s)\). For \(s<r\), define the positive, compact, two-step selfadjoint matrix \(W_{r,s}\) on \(\ell^2(\mathbb Z)\) by its nonzero entries
\[
(W_{r,s})_{n,n}=\frac{s^{|n-1|}+s^{|n+1|}}{4r^{|n|}},\qquad
(W_{r,s})_{n,n+2}=(W_{r,s})_{n+2,n}
=\frac{s^{|n+1|}}{4r^{(|n|+|n+2|)/2}}.
\]
Writing \(\Lambda(r,s)\) for its largest eigenvalue, the sharp threshold is \(\boxed{\Gamma(r,s)=1/\Lambda(r,s)}\). It is *computably exact*: if \(\Lambda_N\) is the greatest eigenvalue of the principal section indexed by \(-N,\ldots,N\), with \(N\ge3\), then, for \(q=s/r\),
\[
\boxed{0\le\Lambda(r,s)-\Lambda_N(r,s)
\le\left(\frac{1+s^2}{4r}+\frac12\right)q^N.}
\]
In particular the entire threshold curve is strictly decreasing in \(s\), with sharp endpoint laws
\[
\boxed{\Gamma(r,0)=2r,\qquad\Gamma(r,r)=\frac{2r}{1+r^2},}
\]
\[
\boxed{\Gamma(r,s)=2r-rs^2+O_r(s^4)\quad(s\downarrow0),}
\]
\[
\boxed{\Gamma(r,s)=\frac{2r}{1+r^2}
+\frac{8r^2}{(1-r^2)(1+r^2)^2}(r-s)
+O_r((r-s)^2)\quad(s\uparrow r).}
\]
At the boundary \(\gamma=\Gamma(r,s)\), **all finite Gram matrices at distinct sites are positive definite when \(s<r\)**. By contrast, at \(s=r\), a finite Gram matrix on pairwise distinct sites is singular **exactly when it contains both \(0\) and \(\pi\)**; its nullspace is then one-dimensional, with opposite coefficients on those two sites and zero elsewhere.

## Assumptions and scope
Every angle is modulo \(2\pi\), and the axial cosine is measured against the fixed diameter through \(0\) and \(\pi\). Positive semidefiniteness means nonnegativity of every finite Hermitian Gram form, for arbitrary sites and complex coefficients. Strict finite-site positive definiteness requires strictness for every nonzero vector at pairwise distinct sites. There is no lower restriction on real \(\gamma\). At \(s=0\), the convention \(0^0=1\) means \(P_0\equiv1\).

## Proof
**Fourier reduction and sharp necessity.** For a finite complex measure \(\mu=\sum_j c_j\delta_{x_j}\), put \(F_n=\sum_j c_je^{-inx_j}\) and \(u_n=r^{|n|/2}F_n\). Then \(u\in\ell^2\). The Poisson expansion gives the exact identity
\[
\sum_{j,k}c_j\overline{c_k}K_{r,s,\gamma}(x_j,x_k)
=\sum_n r^{|n|}|F_n|^2
-\gamma\sum_n s^{|n|}\left|\frac{F_{n-1}+F_{n+1}}2\right|^2
=\langle u,(I-\gamma W_{r,s})u\rangle.
\]
Indeed \(W_{r,s}=A_r^{-1/2}CA_sCA_r^{-1/2}\) on the finitely supported core, where \(A_t\) is diagonal with entries \(t^{|n|}\) and \((Cv)_n=(v_{n-1}+v_{n+1})/2\). The matrix displayed in the theorem is its bounded positive extension. The weighted Fourier sequences of all finite point masses have dense linear span in \(\ell^2\): an orthogonal vector would yield an absolutely uniformly convergent Fourier series, zero at every angle, hence identically zero. Consequently all finite Gram forms are nonnegative exactly when \(I-\gamma W_{r,s}\ge0\); a failure of this operator inequality gives a finite negative Gram form by density. For \(s<r\), the nonzero band entries tend geometrically to zero, so \(W\) is compact and has a positive largest eigenvalue. Since \(W\ge0\), its operator inequality is exactly \(\gamma\le\Lambda^{-1}\).

**Finite-section certificate.** Extend the principal \([-N,N]\) section by zero to the full space. The diagonal entries omitted outside this section are at most \((1+s^2)q^N/(4r)\). Each omitted two-step offdiagonal edge has absolute weight at most \(q^N/4\), and each row meets at most two. Thus the maximum absolute row and column sums of the difference are bounded by \(((1+s^2)/(4r)+1/2)q^N\). The Schur test bounds its norm by the same quantity, while compression cannot increase the largest eigenvalue. This proves the enclosure, including the exact case \(s=0\).

**Strict monotonicity and the small-scale expansion.** For \(s<t\le r\), the quadratic-form difference \(W_{r,t}-W_{r,s}=A_r^{-1/2}C(A_t-A_s)CA_r^{-1/2}\) is positive on finitely supported sequences, hence on the full space by boundedness. Every entry of each \(W_{r,u}\) is nonnegative, and every diagonal entry is *strictly increasing* in \(u\) on \([0,r]\). A compact nonnegative-entry matrix has a top eigenvector with nonnegative coordinates: replace a top Rayleigh maximizer by its coordinatewise absolute values. For this vector all terms in the quadratic form of \(W_{r,t}-W_{r,s}\) are nonnegative and at least one positive diagonal term occurs. Thus \(\Lambda(r,t)>\Lambda(r,s)\) by the Rayleigh principle (also when \(t=r\)). At \(s=0\), \(W\) is supported at indices \(\pm1\) and equals \((4r)^{-1}\begin{psmallmatrix}1&1\\1&1\end{psmallmatrix}\), so \(\Lambda(r,0)=1/(2r)\). Near zero, its odd-index block is analytic in \(s^2\), has a simple top eigenvalue and a diagonal first correction \(s^2/(4r)\) on indices \(\pm1\). The even block has norm \(O_r(s)\) and stays below it. Standard simple-eigenvalue perturbation therefore gives \(\Lambda(r,s)=1/(2r)+s^2/(4r)+O_r(s^4)\); inversion gives the first threshold expansion.

**Equal scale and the linear approach law.** At \(s=r\) the odd and even index blocks separate. All noncentral odd diagonal entries equal \(d=(r+r^{-1})/4\), ordinary offdiagonal edges have weight \(1/4\), and the special bond \(-1\leftrightarrow1\) has weight \(1/(4r)\). The normalized positive vector
\[
u_{\pm(2j+1)}=\sqrt{\frac{1-r^2}{2}}r^j\ (j\ge0),
\qquad u_{2j}=0,
\]
is a simple eigenvector with eigenvalue \(\Lambda_*=(r+r^{-1})/2\). The rest of the spectrum is at most \(d+1/2\): the even block has diagonal at most \(d\) and ordinary offdiagonal weights \(1/4\), and a two-sided Jacobi chain with only one enlarged bond has at most one eigenvalue above its free upper edge. Explicitly, if an eigenvalue exceeds \(d+1/2\), each half-line has a unique summable mode \(c_\pm z^j\), \(0<z<1\), satisfying \(4(\lambda-d)=z+z^{-1}\). The central matching equations are \(z^{-1}c_+=r^{-1}c_-\) and \(z^{-1}c_-=r^{-1}c_+\), forcing \(z=r\), \(c_+=c_-\) and \(\lambda=\Lambda_*\). This establishes uniqueness rather than inferring it from a finite truncation. Thus the top gap is at least \(g=(1-r)^2/(4r)>0\), giving \(\Gamma(r,r)=1/\Lambda_*\).

For the same normalized vector, the Rayleigh deficit from \(s=r\) is exactly
\[
\langle u,(W_{r,r}-W_{r,s})u\rangle
=\frac{r^2-s^2}{r(1-s^2)}.
\]
This follows because after removing the weight \(r^{|n|/2}\), all odd Fourier coordinates of \(u\) become constant, and their cosine average is constant on even indices; summing the resulting geometric series gives the fraction. Although the operators do not converge in norm at \(s=r\), the *localized vector* satisfies \(\|(W_{r,r}-W_{r,s})u\|=O_r(r-s)\), using \(|r^j-s^j|\le jr^{j-1}(r-s)\) and geometric decay. Also \(W_{r,s}\le W_{r,r}\), so the orthogonal complement remains below \(\Lambda_*-g\). The Schur complement on the eigendirection \(u\) thus yields
\[
\Lambda(r,s)=\Lambda_*-\frac{r^2-s^2}{r(1-s^2)}+O_r((r-s)^2).
\]
Expanding its reciprocal gives the claimed linear coefficient.

**Exact boundary nullspace.** Suppose \(\gamma=\Gamma(r,s)\) and a finite signed measure at distinct sites has zero Gram energy. Then its weighted Fourier vector lies in the top eigenspace. For \(s<r\), the eigen-equation implies
\[
r^{|n|}F_n=\frac\gamma4\bigl[s^{|n-1|}(F_{n-2}+F_n)+s^{|n+1|}(F_n+F_{n+2})\bigr].
\]
Because \(F_n\) is bounded, \(F_n=O((s/r)^n)\to0\) as \(n\to+\infty\); when \(s=0\), sufficiently high \(F_n\) vanish outright. But for any nonzero finite measure on distinct sites,
\[
\lim_{N\to\infty}\frac1N\sum_{n=0}^{N-1}|F_n|^2=\sum_j|c_j|^2>0,
\]
by averaging off-diagonal geometric series, a contradiction. Hence every distinct-site Gram matrix is strictly positive definite. At \(s=r\), the unique top eigenvector found above unweights to \(F_n\) constant on odd integers and zero on even integers: precisely the Fourier sequence of \(\delta_0-\delta_\pi\). Uniqueness of Fourier coefficients of finite measures proves the exact singular-pair statement and one-dimensional nullspace.

## Verification
Run the included `checker.py` with Python 3, NumPy and SciPy. It passes 116 deterministic supplementary assertions on Jacobi eigenvalues, certified finite-section bounds, small-scale expansions, endpoint values, and finite Gram matrices (including the exact signed antipodal null vector). Finite checks do not prove the infinite assertions; those follow from the analytic argument. In computational use the displayed finite-section inequality is rigorous if the matrix eigenvalue is enclosed with certified numerical arithmetic.

## Relationship to prior work
The Fourier-matrix methods of Buhmann and Jäger (2021, arXiv:2105.02586) motivate the question but do not state a sharp signed **two-scale** Poisson covariance subtraction frontier. Jäger (2020, arXiv:2005.02798) supplies related nonradial harmonic-block context. A prior circle-Poisson kernel theorem for \(P_r(x-y)[1+\varepsilon\cos(k(x+y))]\) establishes a *single-scale* harmonic modulation threshold and a polygonal boundary singularity. Its equal-scale case is relevant and the endpoint \(s=r\) is not claimed as a separate novelty. That theorem does not entail the compact interior-scale Jacobi boundary, both sharp asymptotic laws, or the strictness of all critical finite Gram matrices for \(s<r\). Published two-scale *isotropic two-sphere geodesic exponential* covariance comparisons concern diagonal Legendre coefficients and do not furnish this off-diagonal Fourier frontier. A related 2022 paper on nonstationary spherical covariance families was available only through its abstract in this comparison; an unindexed equivalent remains a stated priority risk.

## Limitations
The parameters are restricted to \(0<r<1\), \(0\le s\le r\) and real \(\gamma\). No closed elementary expression for \(\Gamma\) at interior scales is claimed; instead its exact compact spectral characterization has certified finite-section error bounds. The result does not classify higher axial harmonics, \(s>r\), other dimensions, or arbitrary nonstationary covariance models. Historical priority is provisional; independent mathematical validation has not been performed.

## References
1. M. Buhmann and J. Jäger, *Strict Positive Definiteness of Convolutional and Axially Symmetric Kernels on d-Dimensional Spheres*, arXiv:2105.02586 (first submitted 2021-05-06), https://arxiv.org/abs/2105.02586; open full text https://doi.org/10.1007/s00041-022-09913-x.
2. J. Jäger, *Strictly positive definite kernels on the 2-sphere: beyond radial symmetry*, arXiv:2005.02798 (2020), https://arxiv.org/abs/2005.02798.
3. *Sharp harmonic-modulation cutoff and polygonal singularities for circle Poisson covariances*, publicly recorded mathematical result (2026-10-25), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-sharp-harmonic-modulation-cutoff-and-polygonal-singularities-for--0f4219b7a6a9.
4. *Exact two-scale exponential covariance domination on the two-sphere*, publicly recorded mathematical result (2026-10-26), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-two-scale-exponential-covariance-domination-on-the-two-sph--4e0d440866a1.
5. L. R. Blake, E. Porcu and D. M. Hammerling, *Parametric nonstationary covariance functions on spheres*, Stat 11 (2022), e468, https://doi.org/10.1002/sta4.468; abstract inspected, full text unavailable.
