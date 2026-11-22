# Parity-rigid inversion and the exact joint law of circular Voronoi cell lengths

## Finding
Let \(n\geq3\) points be sampled independently and uniformly on a circle of circumference one. Choose one of the sampled sites uniformly at random as an origin for clockwise indexing and let \(L_0,\ldots,L_{n-1}\) denote the resulting ordered geodesic Voronoi cell lengths. The complete finite-sample law and inverse reconstruction have the following parity dichotomy.

**Odd number of sites.** For odd \(n\), define
\[
Q_i(l)=\sum_{j=0}^{n-1}(-1)^j l_{(i-j)\bmod n}.
\]
On the hyperplane \(\sum_i l_i=1\), the joint density with respect to \(dl_0\cdots dl_{n-2}\), with \(l_{n-1}=1-\sum_{i=0}^{n-2}l_i\), is
\[
f_n(l)=(n-1)!\,2^{n-1}\,\mathbf 1\{Q_i(l)>0\text{ for all }i\}.
\]
The spacings between successive sites are uniquely reconstructed by \(S_i=Q_i(L)\); hence, the ordered cell lengths determine the site configuration up to rigid rotation.

**Even number of sites.** For even \(n\), the lengths satisfy the deterministic constraint
\[
\sum_{i\text{ even}}L_i=\sum_{i\text{ odd}}L_i=\frac12.
\]
For an admissible vector \(l\), write \(b_0=0\) and recursively \(b_i=2l_i-b_{i-1}\) for \(1\leq i\leq n-1\). Put
\[
a(l)=\max_{i\text{ even}}(-b_i),\quad c(l)=\min_{i\text{ odd}}b_i,\quad\Delta(l)=c(l)-a(l).
\]
Use \(l_1,\ldots,l_{n-2}\) as free coordinates, with \(l_0=\frac12-\sum_{2\leq i\leq n-2,\ i\text{ even}}l_i\) and \(l_{n-1}=\frac12-\sum_{1\leq i\leq n-3,\ i\text{ odd}}l_i\). The joint density with respect to \(dl_1\cdots dl_{n-2}\) is
\[
f_n(l)=(n-1)!\,2^{n-2}[\Delta(l)]_+.
\]
Here \([u]_+=\max(u,0)\); values outside the stated alternating-balance hyperplane have zero probability. At almost every attainable \(l\), the inverse sites constitute a genuine one-dimensional family, not a single configuration. Their spacings are
\[
S_i=(-1)^i T+b_i,\quad T\mid (L=l)\sim\operatorname{Uniform}(a(l),c(l)).
\]
The density vanishes linearly with the length of the feasible inverse fiber. Thus the full finite-sample joint cell law is constant on a polytope in odd order and fiber-length weighted on a lower-dimensional polytope in even order.

## Assumptions and scope
Geodesic (intrinsic arc-distance) Voronoi cells are used, with no co-located sites (an almost-sure event). A randomly marked site fixes the cyclic index; retaining clockwise order is essential. The circle circumference is one, so all lengths are dimensionless; multiply site gaps and cell lengths by the circumference for other scales. Formulas hold for every integer \(n\ge3\). Density coordinates are explicitly specified, since the even-order law is singular in the ambient \((n-1)\)-simplex. All inverse statements are modulo a common rotation; reflection is not silently identified.

## Proof
**1. Spacings and Voronoi map.** Marking a uniformly selected sampled site removes the bias inherent in anchoring the shortest observed angle. The clockwise gaps \(S_0,\ldots,S_{n-1}\) have the uniform \(\operatorname{Dirichlet}(1,\ldots,1)\) law on \(\{s_i>0,\ \sum s_i=1\}\), with density \((n-1)!\) in coordinates \(s_0,\ldots,s_{n-2}\). The two geodesic boundary midpoints of site \(i\) are half the preceding and following gaps from that site, so
\[
2L_i=S_{i-1}+S_i\quad(i\bmod n).
\]

**2. Odd inversion and density.** Iterating the recursion \(S_i=2L_i-S_{i-1}\) once around the odd cycle yields \(S_i=Q_i(L)\). This is the unique real solution. Positivity of all reconstructed gaps is both necessary and sufficient for realizability. In free sum-one coordinates the linear map \(s\mapsto l\) has absolute Jacobian \(2^{-(n-1)}\): the full circulant \((I+P)/2\) has determinant \(2^{1-n}\) for odd \(n\), and its eigenvalue on the all-ones direction is one, so restriction to the sum-zero hyperplane has the same determinant. Applying the invertible change-of-variables formula to the uniform spacing simplex proves the displayed constant density and its normalization.

**3. Even inverse fiber and density.** The alternating sum of \(2L_i=S_{i-1}+S_i\) vanishes when \(n\) is even, proving the two alternating sums equal \(1/2\). Let \(T=S_0\). Successive substitutions give \(S_i=(-1)^iT+b_i\). Every spacing is positive exactly for
\[
\max_{i\text{ even}}(-b_i)<T<\min_{i\text{ odd}}b_i.
\]
The alternating length identity ensures that the closing equation for \(L_0\) is also satisfied. This proves sufficiency, describes every solution, and excludes all putative solutions when \(\Delta\le0\).

Parameterize the spacing simplex by \((s_0,\ldots,s_{n-2})\), and the output together with its hidden fiber coordinate by \((T,l_1,\ldots,l_{n-2})\). The latter map has triangular absolute Jacobian \(2^{-(n-2)}\), since its successive diagonal factors are \(1,1/2,\ldots,1/2\). Consequently, the joint density of \((T,L_1,\ldots,L_{n-2})\) is the constant \((n-1)!2^{n-2}\) on the region \(a(l)<T<c(l)\). Integrating over \(T\) gives the asserted linear-fiber density; dividing the joint density by the marginal density gives the conditional uniform law. These arguments show normalization without an unproved polytope-volume calculation.

**4. Covariance singularity cross-check.** The Dirichlet spacing covariance restricted to the sum-zero hyperplane is \(1/[n(n+1)]\) times the identity. The cycle-averaging map has complex Fourier multiplier \((1+e^{2\pi i k/n})/2\), so the covariance eigenvalues of \(L\) at Fourier frequencies \(1\le k<n\) are
\[
\lambda_k=\frac{\cos^2(\pi k/n)}{n(n+1)}.
\]
There is an additional zero eigenvalue at \(k=n/2\) exactly in even order, independently confirming the dimension loss. This covariance calculation is a consistency check, not the novelty claim.

## Verification
Run `python3 tools/verify.py` using the Python standard library. It performs 4,812 deterministic exact-rational assertions across \(n=3,\ldots,14\): reconstruction from samples, both parity constraints, two interior selections of even inverse fibers, and exact rational Jacobian determinants on each finite size. The infinite-order proof is the algebraic change-of-variables argument above, not an extrapolation from these tests.

## Relationship to prior work
Járai-Szabó and Néda, *On the size-distribution of Poisson Voronoi cells* (arXiv:cond-mat/0406116, first posted 2004-06-04), Section 2, derive the one-dimensional **typical-cell marginal** from two independent exponential spacings in an infinite Poisson model. Their article does not state the finite circular jointly ordered cell vector, its parity-dependent singular support, or the inverse-fiber law. Devroye, Györfi, Lugosi and Walk, *On the measure of Voronoi cells* (arXiv:1512.04267, first posted 2015-12-14), Theorems 1–2 and the dimension-one discussion, establish asymptotic typical-cell measure laws; those theorems concern a **single cell**, not exact joint distribution or deterministic inverse recovery. Their paper's primary MSC classification is 60D05.

The related published published-finding corpus record *Exact neighbor threshold-dependence phase diagram for circular Voronoi cells* concerns covariances of two threshold indicators for nearby cells, a weaker pairwise observable. Its accessible abstract does not imply the full vector density or conditional inverse-fiber theorem; the complete underlying article was not accessible for line-by-line comparison. General Poisson–Voronoi literature remains a historical-priority risk. The result is not a claim that the cyclic averaging identity, Dirichlet spacings, or linear change of variables are themselves new.

## Limitations
The order and cyclic orientation of the cell lengths must be retained; an unordered multiset of lengths has additional permutation ambiguities. In even order, individual site gaps are intrinsically unidentifiable from cell lengths, and the conditional law describes the remaining uncertainty rather than providing unique reconstruction. The law assumes independent uniform sites; it does not cover arbitrary sampling densities, random numbers of sites, or Euclidean planar Voronoi polygons. Earlier treatments of moving averages of Dirichlet vectors, possibly under other terminology, may imply the same formulas, so complete historical priority remains unresolved. No independent mathematical review is asserted.

## References
1. F. Járai-Szabó and Z. Néda, *On the size-distribution of Poisson Voronoi cells*, arXiv:cond-mat/0406116 (first public posting 2004-06-04), https://arxiv.org/abs/cond-mat/0406116.
2. L. Devroye, L. Györfi, G. Lugosi and H. Walk, *On the measure of Voronoi cells*, arXiv:1512.04267v1 (first public posting 2015-12-14), https://arxiv.org/html/1512.04267v1; journal version, *Journal of Applied Probability* 54 (2017), 394–408, DOI 10.1017/jpr.2017.7.
3. published-finding corpus, *Exact neighbor threshold-dependence phase diagram for circular Voronoi cells*, public research record 2026/10/18/SCOPE-exact-neighbor-threshold-dependence-phase-diagram-for-circular-v--2133366397a2, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-neighbor-threshold-dependence-phase-diagram-for-circular-v--2133366397a2.
