# Sharp affine projection norms across all simplex face skeletons

## Finding
Let \(m\ge2\) and \(1\le r\le m\) be integers. On a nondegenerate real simplex \(T\) with \(m\) vertices, choose an \((r-1)\)-dimensional face uniformly among its \(\binom mr\) faces, then choose a point uniformly by normalized \((r-1)\)-dimensional volume on that face. Denote the resulting probability by \(\mu_{m,r}\) and its support by \(\Sigma_{m,r}\). Thus \(r=1\) is the vertex measure, \(r=m-1\) is an equal-facet mixture, and \(r=m\) is uniform volume on \(T\). For regular simplices this is normalized Hausdorff measure on the chosen skeleton.

Let \(P_{m,r}:L^2(\mu_{m,r})\to \mathcal A(T)|_{\Sigma_{m,r}}\) be orthogonal projection onto real affine functions. Its exact, attained \(L^\infty\)-operator norm is
\[
\boxed{\Lambda_{m,r}=\|P_{m,r}\|_{\infty\to\infty}=\frac{2(m-1)(r+1)}{2m-r-1}\left(1-\frac{r-1}{(m-1)(r+1)}\right)^r-1.}
\]
For \(r\ge2\), exactly the \(m\) vertices maximize the evaluation-kernel absolute integral; for \(r=1\), the projection is vertex interpolation, has norm \(1\), and every point of the full simplex has evaluation norm \(1\). For \(r\ge2\), a norm-attaining input is \(f(y)=\operatorname{sgn}K(v_i,y)\) at any vertex \(v_i\), and the opposite sign also works.

The sharp minimum of a projected nonnegative input is
\[
\boxed{\inf_{0\le f\le1}\ \min_{x\in\Sigma_{m,r}}(P_{m,r}f)(x)=\frac{1-\Lambda_{m,r}}2.}
\]
For \(r\ge2\), it is attained by the indicator of \(\{y:K(v_i,y)<0\}\). For each fixed \(r\ge2\), \(\Lambda_{m,r}\) increases strictly with the ambient number of vertices \(m\ge r\) and satisfies the **sharp dimension-free ceiling**
\[
\boxed{\Lambda_{m,r}<r,\qquad \lim_{m\to\infty}\Lambda_{m,r}=r.}
\]
For \(r=1\), \(\Lambda_{m,1}=1\). In the simultaneous high-dimensional regime \(r/m\to\theta\in(0,1]\),
\[
\boxed{\lim_{m\to\infty}\frac{\Lambda_{m,r}}m=\frac{2\theta e^{-\theta}}{2-\theta}.}
\]
The full-volume case \(r=m\) specializes to the previously established simplex formula; the intermediate face-skeleton hierarchy, its sharp face-rank ceiling, and the two-parameter limit are the claims here.

## Assumptions and scope
Every face is selected with **equal probability**, regardless of its Euclidean volume; conditional uniformity applies within that face. This distinction matters on irregular simplices: the measure is not generally normalized global Hausdorff measure of the skeleton. The projector is onto the entire real affine space, with evaluation on the support skeleton. The formula is shape-independent because normalized face volume and barycentric coordinates are preserved by affine bijections. No continuity or coupling between different simplices is imposed.

## Proof
Write \(\lambda_i\), \(1\le i\le m\), for barycentric coordinates. The random barycentric vector \(B\) under \(\mu_{m,r}\) is produced by uniformly choosing an \(r\)-subset of coordinates, assigning a uniform Dirichlet vector with all parameters \(1\) to those coordinates, and setting all others to zero. Therefore
\[
\mathbb EB_i=\frac1m,\quad \mathbb EB_i^2=\frac{2}{m(r+1)},\quad \mathbb EB_iB_j=\frac{r-1}{m(m-1)(r+1)}\quad(i\ne j).
\]
The barycentric Gram matrix equals \(G=\delta I+bJ\), with
\[
\delta=\frac{2m-r-1}{m(m-1)(r+1)}>0,\qquad b=\frac{r-1}{m(m-1)(r+1)},
\]
where \(J\) is the all-ones matrix. Since \(G\mathbf1=\mathbf1/m\),
\[
G^{-1}=\delta^{-1}(I-J/m)+J.
\]
Thus the reproducing kernel, normalized against the probability \(\mu_{m,r}\), is
\[
K(x,y)=1+\delta^{-1}\left(\sum_i\lambda_i(x)\lambda_i(y)-\frac1m\right),\qquad \int K(x,y)\,d\mu_{m,r}(y)=1.
\]
For every \(x\in T\), \(K(x,y)=\sum_i\lambda_i(x)K(v_i,y)\). Convexity of absolute value and permutation symmetry give
\[
\int|K(x,y)|\,d\mu_{m,r}(y)\le\sum_i\lambda_i(x)\int|K(v_i,y)|\,d\mu_{m,r}(y)=\int|K(v_1,y)|\,d\mu_{m,r}(y).
\]
For \(r\ge2\) this inequality is strict at every nonvertex: if two coefficients \(\lambda_i(x),\lambda_j(x)\) are positive, then on a relatively open set of an observed face near \(v_i\), \(K(v_i,y)>0\) and \(K(v_j,y)<0\), forcing strict triangle inequality on a set of positive measure. The required signs hold because \(K(v_i,v_i)>0\) and \(K(v_j,v_i)=1-\delta^{-1}/m<0\) when \(r>1\). When \(r=1\), direct vertex interpolation gives evaluation norm \(1\) everywhere.

Put \(\alpha=\delta^{-1}\) and \(h=(r-1)/[(m-1)(r+1)]\). At vertex \(v_i\), \(K(v_i,y)=\alpha(\lambda_i(y)-h)\). If \(r\ge2\), the probability that the selected face contains \(i\) equals \(r/m\); conditionally, \(\lambda_i(y)\) has the \(\operatorname{Beta}(1,r-1)\) law, whose survival probability is \((1-t)^{r-1}\). Consequently, the positive kernel mass equals
\[
I_{m,r}:=\int(K(v_i,y))_+\,d\mu_{m,r}(y)=\frac{r}{m}\alpha\int_h^1(1-t)^{r-1}\,dt=\frac{\alpha}{m}(1-h)^r
=\frac{(m-1)(r+1)}{2m-r-1}(1-h)^r.
\]
The same last expression equals \(1\) at \(r=1\), by direct inspection of the discrete kernel. Since the signed kernel mass is \(1\), its absolute integral is \(2I_{m,r}-1\), proving the norm formula. Choosing the sign of the kernel gives norm attainment. Choosing \(f=\mathbf1_{\{K(v_i,\cdot)<0\}}\) gives the sharp negative excursion \(1-I_{m,r}=(1-\Lambda_{m,r})/2\).

For fixed \(r\ge2\), set \(u=(r-1)/[(m-1)(r+1)]\), so \(0<u\le1/(r+1)\). The positive kernel mass becomes
\[
I_{m,r}=\frac{(r+1)(1-u)^r}{2-(r+1)u},\qquad
\frac{d}{du}\log I_{m,r}=\frac{(r-1)((r+1)u-1)}{(1-u)(2-(r+1)u)}.
\]
This derivative is negative except possibly at the endpoint \(u=1/(r+1)\). As \(m\) increases, \(u\) decreases, so \(I_{m,r}\) and \(\Lambda_{m,r}\) increase strictly. Their limit is \((r+1)/2\) and \(r\), respectively, proving the strict finite bound and its optimality. For \(r/m\to\theta\in(0,1]\), \(r\log(1-h)\to-\theta\), while \(\alpha/m^2\to\theta/(2-\theta)\), giving the stated scaled limit.

## Verification
The standalone `verify.py` independently expands the beta density and integrates the positive kernel by rational polynomial integration. For every pair \(2\le m\le16\), \(1\le r\le m\), it checks the barycentric Gram inverse, the exact positive integral, and the closed formula using fractions. Additional exact finite checks test strict increase at fixed face rank, the volume specialization, and fixed-rank limiting diagnostics. Execute with `python3 verify.py`; the expected final line is `ALL_SIMPLEX_SKELETON_CHECKS_PASSED`. The analytic proof, rather than these finite tests, handles all quantifiers and the limit.

## Relationship to prior work
The standard volume-simplex affine projection formula is known, with \(\Lambda_{m,m}=2m(m/(m+1))^{m-1}-1\); it is a **covered endpoint** here, not claimed as new. Hangelbroek--Narcowich--Sun--Ward (2010) study stability of kernel-based least-squares projectors on manifolds, not the exact mixed-dimensional face-uniform simplex operators. Crouzeix--Thomée (1987) establish \(L^p\) stability for global finite-element projectors under mesh conditions, with a different domain and operator. Białas-Cież--Kenne--Sommariva--Vianello (2023) provide numerical bounds for polynomial-projector Lebesgue constants on standard bodies, not the exact face-rank hierarchy. The contribution isolates a family of measures interpolating between vertex observations and full volume and proves an exact all-face-rank law and sharp ceiling determined by the observed face dimension, not ambient dimension.

## Limitations
The result does not assert the same constant for unequal face sampling weights, global Hausdorff measure on irregular simplices, higher polynomial degrees, complex-valued data, or globally coupled finite-element projections. The asymptotic law with \(r/m\to\theta>0\) is distinct from fixed \(r\); no uniform error rate over all growth regimes is asserted. Priority risk persists for terminology absent from the searched literature, including simplicial skeletal cubature and specialized mass-lumping results.

## References
1. T. Hangelbroek, F. J. Narcowich, X. Sun, J. D. Ward, *Kernel Approximation on Manifolds II: The L-infinity Norm of the L2 Projector*, arXiv:1005.2424, first publicly submitted May 13, 2010; DOI:10.1137/100795334.
2. M. Crouzeix, V. Thomée, *The Stability in Lp and W1p of the L2-Projection onto Finite Element Function Spaces*, Mathematics of Computation 48 (1987), 521–532, DOI:10.1090/S0025-5718-1987-0878688-2.
3. L. Białas-Cież, D. J. Kenne, A. Sommariva, M. Vianello, *Evaluating Lebesgue Constants by Chebyshev Polynomial Meshes on Cube, Simplex and Ball*, arXiv:2311.18656 (2023).
4. *Exact positivity defect and max norm of the affine least-squares projector on a simplex*, publicly recorded volume-only result, identifier `99c2b9dd9b34` (2026).
