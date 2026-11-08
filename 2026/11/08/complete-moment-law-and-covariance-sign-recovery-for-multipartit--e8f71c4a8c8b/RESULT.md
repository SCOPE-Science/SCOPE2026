# Complete moment law and covariance-sign recovery for multipartite stable-set polytopes

## Finding

Let \(r\ge1\) and let \(m_1,\ldots,m_r\) be positive integers with \(N=\sum_i m_i\). Let \(G=K_{m_1,\ldots,m_r}\) be the complete multipartite graph with labeled parts, and let \(P_G\subset\mathbb R^N\) be its canonical stable-set polytope. If \(X=(X_{ij})\) is uniformly distributed on \(P_G\) with respect to \(N\)-dimensional Lebesgue volume, then for **every** family of nonnegative integer exponents \(\alpha_{ij}\), with \(A_i=\sum_{j=1}^{m_i}\alpha_{ij}\) and \(A=\sum_i A_i\),
\[
\boxed{\mathbb E\prod_{i=1}^r\prod_{j=1}^{m_i}X_{ij}^{\alpha_{ij}}
=\frac{\prod_{i=1}^r(m_i+1)_{A_i}}
{(N+1)_A\prod_{i=1}^r\prod_{j=1}^{m_i}(\alpha_{ij}+1)}.}
\tag{1}
\]
Here \((q)_s=q(q+1)\cdots(q+s-1)\) for positive integers \(s\), and \((q)_0=1\). The exact volume is
\[
\operatorname{Vol}_N(P_G)=\frac{\prod_i m_i!}{N!}.
\tag{2}
\]

For distinct vertices \((i,j)\ne(h,k)\), the off-diagonal covariance is
\[
\boxed{\operatorname{Cov}(X_{ij},X_{hk})=
\begin{cases}
\displaystyle\frac{(m_i+1)(N-m_i)}{4(N+1)^2(N+2)},&i=h,\\[5pt]
\displaystyle-\frac{(m_i+1)(m_h+1)}{4(N+1)^2(N+2)},&i\ne h.
\end{cases}}
\tag{3}
\]
If \(r\ge2\), every off-diagonal covariance is nonzero, and it is **negative exactly for pairs joined by an edge** of \(G\). Thus the signs of the \(N\times N\) covariance matrix alone recover the entire labeled graph.

The centroid has coordinates \(\mathbb E X_{ij}=(m_i+1)/(2(N+1))\). Its Euclidean inertia \(J(P_G)=\mathbb E\|X-\mathbb EX\|^2\) is
\[
\boxed{J(P_G)=\frac{(N-2)\sum_i m_i^3+6N\sum_i m_i^2+(5N+2)N}{12(N+1)^2(N+2)}.}
\tag{4}
\]
For fixed \(N\ge2\) and fixed number \(r\) of nonempty parts, this is strictly Schur-convex in their sizes: its minimum occurs exactly at part sizes differing by at most one, and its maximum occurs exactly at \((N-r+1,1,\ldots,1)\), up to permutation. Across all complete multipartite graphs on \(N\) labeled vertices,
\[
\boxed{\frac{N^2}{(N+1)^2(N+2)}\le J(P_G)\le\frac N{12},}
\tag{5}
\]
with equality on the left only for the complete graph and on the right only for the edgeless graph (for \(N\ge2\)). Splitting a part into two nonempty parts strictly decreases inertia.

## Assumptions and scope

The graph is simple, unweighted, and complete multipartite; a single part is allowed as the edgeless boundary case. Coordinates are the standard indicator coordinates of all stable sets, including the empty set, without affine deformation. The uniform distribution is volume-uniform **inside** the full-dimensional convex polytope, not uniform on its finite vertex set. Formula (1) covers arbitrary nonnegative integral monomial degrees, including total degree zero. No claim concerns general graph stable-set polytopes or alternate Euclidean embeddings.

## Proof

**1. Exact polytope description.** The stable sets of a complete multipartite graph lie in a single part. Therefore its stable-set polytope is the convex hull of the coordinate cubes \([0,1]^{m_i}\), each embedded in its own coordinate block. Write \(s_i(x)=\max_{1\le j\le m_i}x_{ij}\). By taking convex combinations of these cubes, with coefficients at least \(s_i(x)\), one obtains the exact description
\[
P_G=\{x\ge0:\sum_{i=1}^r s_i(x)\le1\}.
\tag{6}
\]
Conversely, for a point satisfying the right-hand constraints, choose coefficients \(\lambda_i\ge s_i(x)\) summing to one (possible because the sum of maxima is at most one). Each block divided by its positive coefficient belongs to the corresponding cube, proving inclusion. If some coefficient is zero, its block is zero. The simplex near the origin shows full dimensionality.

**2. Block maxima of a volume-uniform point.** Put \(S_i=\max_j X_{ij}\), and let \(S_0=1-\sum_iS_i\). The Lebesgue volume in a single nonnegative block whose maximum is at most \(s\) is \(s^{m_i}\). Consequently the joint unnormalized density of \((S_1,\ldots,S_r)\) on \(S_i\ge0\), \(\sum_iS_i\le1\) is \(\prod_i m_i S_i^{m_i-1}\). The Dirichlet integral gives (2), and after normalization
\[
(S_0,S_1,\ldots,S_r)\sim\operatorname{Dirichlet}(1,m_1,\ldots,m_r).
\tag{7}
\]
Conditionally on \(S_i=s_i>0\), exactly one of the \(m_i\) coordinates attains the maximum, uniformly among its indices; the remaining coordinates are independent uniform variables on \([0,s_i]\). Distinct blocks are conditionally independent. Ties and zero maxima have probability zero and do not affect the formulas.

**3. All monomial moments.** Fix arbitrary nonnegative integral exponents. Given the maxima, the conditional monomial expectation for block \(i\) is
\[
\mathbb E\left[\prod_j X_{ij}^{\alpha_{ij}}\mid S_i=s_i\right]
=s_i^{A_i}\frac1{m_i}\sum_{j=1}^{m_i}\prod_{\ell\ne j}\frac1{\alpha_{i\ell}+1}
=s_i^{A_i}\frac{m_i+A_i}{m_i\prod_j(\alpha_{ij}+1)}.
\tag{8}
\]
The Dirichlet moment identity gives
\[
\mathbb E\prod_i S_i^{A_i}=\frac{\prod_i(m_i)_{A_i}}{(N+1)_A}.
\tag{9}
\]
Multiplying (8) over all blocks, using (9), and canceling \((m_i+A_i)(m_i)_{A_i}/m_i=(m_i+1)_{A_i}\), proves (1) for every degree and every part size.

**4. Covariance and graph recovery.** Formula (1) gives
\[
\mathbb EX_{ij}=\frac{m_i+1}{2(N+1)},\qquad
\mathbb E X_{ij}^2=\frac{(m_i+1)(m_i+2)}{3(N+1)(N+2)}.
\tag{10}
\]
For two distinct coordinates in one part, their raw product moment is \((m_i+1)(m_i+2)/(4(N+1)(N+2))\); across parts \(i\ne h\) it is \((m_i+1)(m_h+1)/(4(N+1)(N+2))\). Subtracting the products of the means and simplifying yields (3). When \(r\ge2\), each \(m_i<N\), so within-part covariances are strictly positive and cross-part covariances strictly negative. The latter pairs are exactly graph edges. With one part, all off-diagonal covariances vanish as for a cube.

**5. Euclidean inertia and extremizers.** Summing the coordinate variances from (10) gives
\[
J(P_G)=\sum_i\left[
\frac{m_i(m_i+1)(m_i+2)}{3(N+1)(N+2)}
-\frac{m_i(m_i+1)^2}{4(N+1)^2}\right].
\tag{11}
\]
Expansion yields (4). For fixed \(N\ge2\), put
\[
g_N(t)=\frac{(N-2)t^3+6Nt^2+(5N+2)t}{12(N+1)^2(N+2)}.
\]
Then \(J=\sum_i g_N(m_i)\), and \(g_N''(t)>0\) for \(t>0\). Every transfer of one unit from a larger part to a smaller part, when their difference is at least two, strictly decreases \(J\). Repeated balancing yields the unique minimum composition up to permutation. The reverse inequality shows that moving units to an already larger part strictly raises \(J\) until all but one part have size one, proving the maximum.

Because \(g_N(0)=0\) and \(g_N\) is strictly convex on the nonnegative axis, \(g_N(a+b)>g_N(a)+g_N(b)\) for positive \(a,b\). Splitting a part therefore strictly reduces \(J\). Iterating gives the global extrema: for one part the polytope is the cube and \(J=N/12\); for all singleton parts it is the standard simplex and \(J=N^2/((N+1)^2(N+2))\). This proves (5) and all equality cases.

## Verification

The attached script `geometry_stable_set_moment_checker.py`, run with the listed dependencies, independently triangulates the convex hull of all stable-set incidence vectors in dimensions two through five and integrates its first and second moments exactly using rational simplex identities. It checked 17 distinct part-size profiles and 653 nonzero simplices. A separate exact barycentric expansion checked 368 cubic and quartic monomials in dimensions two through four. All matched (1)--(4), including covariance signs. These finite checks are diagnostic; the universal statement is proved by the Dirichlet and convexity arguments above.

Run `python geometry_stable_set_moment_checker.py` in a Python environment with the versions in `requirements.txt`. The two success markers are `MULTIPARTITE_STAB_EXACT_SIMPLEX_MOMENTS_PASSED 17 653` and `MULTIPARTITE_STAB_ALL_MOMENTS_CUBIC_QUARTIC_CHECKS_PASSED 368`.

## Relationship to prior work

Aliniaeifard, Benedetti, Bergeron, Li and Saliola (arXiv:1804.00360, first posted 2018-04-02) study the stable-set-polytope framework and its edges, not its Lebesgue-volume moments. Kohn, Shapiro and Sturmfels (arXiv:1807.10258, first posted 2018-07-26) develop general generating functions for moments of polytopes and simplex integrations; general algorithms do not state the uniform all-degree formula (1) for this graph family or its covariance-sign recovery and Schur extremal conclusions.

A published result, *The John ellipsoid and full contact structure of balanced complete-multipartite stable-set polytopes*, explicitly uses the same sum-of-block-maxima description but determines a maximum-volume inscribed ellipsoid for balanced parts. Its shape invariant is different from the interior uniform-volume distribution; the previously described polytope geometry is credited here. A published result, *Sharp isotropic-constant range of all Hanner polytopes*, derives moment recursions for centrally symmetric free sums. The present anchored cubes are not generally centrally symmetric (the two singleton-part example is a triangle), and the Hanner covariance recursion does not supply the nonzero inter-block means and covariance signs here. An earlier closed formula under free sums, joins, or Dirichlet-distribution terminology remains a residual historical-priority possibility.

## Limitations

This establishes uniform-volume polynomial moments and their stated consequences for complete multipartite graphs in standard coordinates only. It does not establish the covariance-sign recovery law for all perfect graphs or arbitrary stable-set polytopes. Novelty is based on the published records and papers inspected, not an exhaustive literature certification. The small-dimensional exact checks do not constitute a proof for all dimensions and all monomial orders; the analytical proof does. No independent mathematical audit has been performed.

## References

1. F. Aliniaeifard, C. Benedetti, N. Bergeron, S. X. Li, F. Saliola, *Stable set polytopes and their 1-skeleta*, arXiv:1804.00360 (first public 2018-04-02), https://arxiv.org/abs/1804.00360.
2. K. Kohn, B. Shapiro, B. Sturmfels, *Moment Varieties of Measures on Polytopes*, arXiv:1807.10258 (first public 2018-07-26), https://arxiv.org/abs/1807.10258.
3. *The John ellipsoid and full contact structure of balanced complete-multipartite stable-set polytopes*, published record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-john-ellipsoid-and-full-contact-structure-of-balanced-comple--fc5ba86494aa.
4. *Sharp isotropic-constant range of all Hanner polytopes*, published record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-isotropic-constant-range-of-all-hanner-polytopes--7976b0937cd2.
