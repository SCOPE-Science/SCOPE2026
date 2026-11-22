# Exact metric inballs and parity of incenter freedom in path matchable-subgraph polytopes

## Finding
Let \(n\ge3\), and let \(\mathcal M_n\subset\mathbb R^n\) be the canonical **perfectly matchable subgraph polytope** of the path on \(n\) vertices, including the empty induced subgraph. All distances are the ambient Euclidean distances restricted to its affine hull, which has dimension \(n-1\). Put
\[
w_{n,i}=\sqrt{\frac{i(n-i)}{n}}\quad(1\le i<n),\qquad u_n=\sqrt{\frac{n-1}{n}}.
\]
The exact radius of a largest intrinsic Euclidean ball contained in \(\mathcal M_n\) is
\[
\boxed{r_n=\left(u_n+\max_{1\le i\le n-2}(w_{n,i}+w_{n,i+1})\right)^{-1}.}
\]
In closed form, writing \(k\ge1\) for odd order and \(k\ge2\) for even order,
\[
\boxed{\begin{aligned}
r_{2k+1}^{-1}&=2\sqrt{\frac{k(k+1)}{2k+1}}+\sqrt{\frac{2k}{2k+1}},\\
r_{2k}^{-1}&=\sqrt{\frac{k^2-1}{2k}}+\sqrt{\frac{k}{2}}+\sqrt{\frac{2k-1}{2k}}.
\end{aligned}}
\]
**All** optimal centers have an exact elementary parametrization below. Their affine dimensions are
\[
\boxed{\dim\operatorname{aff}\operatorname{Incenters}(\mathcal M_n)=
\begin{cases}n-3,&n\text{ odd},\\n-4,&n\text{ even}.\end{cases}}
\]
In particular, the incenter is unique exactly for \(n=3,4\). For large \(n\), \(\sqrt n\,r_n\to1\).

This metric law differs sharply from the same abstract polytope in its **matching-edge coordinates**, whose standard-coordinate inradius is the constant \(1/(2+\sqrt2)\) and whose incenter is unique for every \(n\ge3\). The distinction is intrinsic to the natural vertex-incidence Euclidean realization, not a change in the face lattice.

## Assumptions and scope
The vertices of the path are \(1,\ldots,n\). An induced subset \(S\subseteq[n]\), including \(S=\varnothing\), is perfectly matchable when the induced path components have even cardinality. The polytope \(\mathcal M_n\) is the convex hull of the incidence vectors \(\mathbf1_S\) of these sets in \(\mathbb R^n\). No linear rescaling or lattice-normalized metric is used. The affine hull equals the linear image of the unsigned path-incidence matrix \(B\) with columns \(e_i+e_{i+1}\), \(1\le i<n\).

Define the lower-dimensional parameter polytope
\[
Q_{n-1}=\{x\in\mathbb R^{n-1}:x_i\ge0\ (1\le i<n),\quad x_i+x_{i+1}\le1\ (1\le i<n-1)\}.
\]
It is the stable-set polytope of a path with \(n-1\) nodes; these are its complete irredundant facets for \(n\ge3\). Then \(\mathcal M_n=BQ_{n-1}\). For any radius \(r\ge0\), the full set of centers of radius-\(r\) balls in \(\mathcal M_n\) is
\[
\left\{Bx:x_i\ge r w_{n,i},\quad x_i+x_{i+1}\le1-r u_n\text{ for all eligible }i\right\}.
\]
The above expression at \(r=r_n\) gives the **entire** incenter set without omitted facets.

## Proof
**1. Identification of the polytope and its metric.** Any perfect matching of an induced subgraph of a path must match the first selected vertex to its only selected right neighbor, then proceed successively. Thus it is unique whenever it exists. A collection of disjoint edges in the original path is equivalently an independent set of the edge-adjacency path. Consequently the vertex indicators are exactly \(Bx\) for the binary independent-set indicators \(x\). The independent-set polytope of a path is described by the listed nonnegativity and consecutive-pair inequalities: the path incidence constraint matrix is totally unimodular, or one may use the standard perfect-graph stable-set description. Since \(B\) has full column rank, the image has dimension \(n-1\) and its facets correspond bijectively to the facets of \(Q_{n-1}\).

The Euclidean quadratic form induced on matching-edge parameters is
\[
\|Bx\|_2^2=x^{\mathsf T}Gx,\qquad G=B^{\mathsf T}B,
\]
where \(G\) is tridiagonal with diagonal entries \(2\) and immediate off-diagonal entries \(1\). Its inverse has the explicit entries
\[
\boxed{(G^{-1})_{ij}=(-1)^{i+j}\frac{\min(i,j)\,[n-\max(i,j)]}{n}}
\quad(1\le i,j<n).
\]
To verify the inverse, multiply its \(i\)-th row by the three neighboring columns of \(G\): the second discrete difference is zero away from the diagonal, while the diagonal jump is one; boundary terms vanish because the numerator becomes zero at indices \(0\) and \(n\). This also follows by conjugating the Dirichlet path Laplacian by an alternating-sign diagonal matrix.

**2. Exact intrinsic facet distances.** For \(a\in\mathbb R^{n-1}\), the Euclidean norm of the gradient of the functional \(a^{\mathsf T}x\) in the intrinsic metric is \(\sqrt{a^{\mathsf T}G^{-1}a}\). The coordinate facet normal \(a=e_i\) therefore has squared norm \(i(n-i)/n\). For each consecutive-sum facet \(a=e_i+e_{i+1}\), substitution of the displayed inverse yields
\[
a^{\mathsf T}G^{-1}a=\frac{n-1}{n},
\]
independently of \(i\). Hence the perpendicular clearances from \(Bx\) to the supporting planes are exactly \(x_i/w_{n,i}\) and \((1-x_i-x_{i+1})/u_n\). These are genuine facet distances in the affine hull, not distances measured in the full ambient space to an incorrectly extended hyperplane.

**3. Global upper bound and attainment.** Let an intrinsic ball of radius \(r\) centered at \(Bx\) be contained in \(\mathcal M_n\). The entire irredundant facet system forces
\[
x_i\ge r w_{n,i},\qquad x_i+x_{i+1}\le1-r u_n.
\]
For every \(1\le i\le n-2\), adding two lower bounds to the adjacent upper bound gives
\[
r(w_{n,i}+w_{n,i+1}+u_n)\le1.
\]
Thus no ball can have radius larger than the stated \(r_n\). Set \(x_i=r_n w_{n,i}\) simultaneously for every \(i\). All lower bounds hold with equality, and all upper bounds hold precisely because \(r_n\) is the inverse of the maximum; this is a feasible center of a radius-\(r_n\) ball. Thus the bound is globally sharp.

**4. Parity and the full affine incenter locus.** The strictly concave and symmetric function \(t\mapsto\sqrt{t(n-t)/n}\), sampled at \(t=1,\dots,n-1\), increases strictly toward the middle and decreases strictly beyond it. Its neighboring-pair sums are therefore maximal at a unique central pair when \(n=2k+1\), namely \((w_{n,k},w_{n,k+1})\), and at exactly two adjacent central pairs when \(n=2k\), namely \((w_{n,k-1},w_{n,k})\) and \((w_{n,k},w_{n,k+1})\). These give the displayed closed forms.

For every maximal adjacent pair, the radius inequality is an equality. Because its constituent lower and upper facet inequalities have nonnegative slack, equality forces both corresponding coordinates to satisfy \(x_i=r_n w_{n,i}\). In odd order precisely the two middle parameters \(x_k,x_{k+1}\) are fixed; in even order precisely the three middle parameters \(x_{k-1},x_k,x_{k+1}\) are fixed. Conversely the complete incenter locus is the clearance polytope above, so these equations and the remaining weak facet inequalities describe **every** optimizer.

To prove its *affine dimension*, start at \(x_i=r_n w_{n,i}\). Every noncentral consecutive-sum facet has positive slack, because its adjacent weight sum is strictly below the maximum. Raise every parameter not forced by the central equalities by the same sufficiently small \(\varepsilon>0\). The central equalities remain unchanged, all other upper constraints remain satisfied strictly, and all nonforced lower constraints become strict. Hence the optimizer set has relative interior in the affine subspace cut out by exactly two or exactly three independent parameter equalities. Since \(B\) is injective, its affine dimension is \(n-3\) for odd order and \(n-4\) for even order.

**5. Comparison with the standard matching-edge realization and asymptotic scale.** In the ordinary Euclidean metric on \(Q_{n-1}\), lower facet normal norms are \(1\) and adjacent upper facet normal norms are \(\sqrt2\). The same bounding argument yields radius \(1/(2+\sqrt2)\), attained at the uniform parameter point \(x_i=1/(2+\sqrt2)\). At equality every pair of adjacent parameters must both equal that number. Because the parameter path is connected, this forces all coordinates, proving uniqueness. In contrast, in the vertex-incidence realization \(w_{n,i}=\sqrt n\sqrt{(i/n)(1-i/n)}\) has central maximum asymptotic to \(\sqrt n/2\), and \(u_n\to1\), so \(r_n^{-1}\sim\sqrt n\) as claimed.

## Verification
The accompanying standalone `verify.py` uses exact rational arithmetic to multiply the purported inverse by the Gram matrix for every \(3\le n\le30\), verifies every facet-normal squared length, and compares the predicted central maximizing pairs and center-space constraints. For \(3\le n\le14\), it independently enumerates all perfectly matchable induced path subsets and the images of all nonadjacent edge selections, checking exact equality and injectivity. When SciPy is installed, an independent numerical linear-program solver computes the maximum inscribed radius from **all** metric facet inequalities for each \(3\le n\le50\). All these tests passed; the script reports `PATH_MATCHABLE_INBALL_PASS n=3..30; enumerations n=3..14` and `Independent LP verified n=3..50`. The proof, not the finite tests, establishes the infinite-family and exact incenter-dimension claims.

## Relationship to prior work
The perfectly matchable subgraph polytope is the standard vertex-subset polytope introduced by Balas and Pulleyblank; Mori studies its toric ring, compressedness, and Gorenstein conditions and gives the vertex/edge incidence relationship, including the tree case. Neither the inspected 2022 primary text nor its stated central results address Euclidean inballs or optimal-center dimensions. The representation as a stable-set polytope of the line graph and its elementary facet system are known, and **not** claimed as discoveries here.

A published geometry result on the *ordinary-coordinate* path stable-set polytope gives its indexed facet areas and their boundary layers. It does not determine the inradius in the distinct induced metric \(G\); the present theorem explicitly shows that these metric realizations have radically different radius scales and optimizer dimensions. The previously published interval-vector connected-block polytope of a path is a different convex hull (all consecutive interval indicators and zero), not the Fibonacci-size family of even-component vertex subsets considered here. The path symmetric-edge root crosspolytope has only \(2(n-1)\) vertices and another Euclidean realization. The published alternating adjacent-sum family has different alternating capacities and concerns enclosing spheres; it also does not imply the present inball theorem. These comparisons concern actual statements and objects, not keyword differences.

## Limitations
The result concerns unweighted paths, their canonical unsigned **vertex-incidence** realization, and intrinsic Euclidean balls. It does not address general tree graphs, edge-weighted incidence maps, John ellipsoids, or higher Steiner coefficients. The incenter locus is given exactly by inequalities, but its own face lattice and vertex enumeration are not claimed. The reduction makes the proof elementary once the correct nonorthogonal metric is recognized. A prior equivalence in optimization or metric-embedding terminology not indexed by the searched terms remains a historical-priority risk. No independent external mathematical audit has been performed.

## References
1. K. Mori, *Toric rings of perfectly matchable subgraph polytopes*, arXiv:2210.17147, first public 2022-10-31, https://arxiv.org/abs/2210.17147 .
2. E. Balas and W. R. Pulleyblank, *The perfectly matchable subgraph polytope of a bipartite graph*, *Networks* 13 (1983), 495–516, https://doi.org/10.1002/net.3230130405 .
3. F. Aliniaeifard, C. Benedetti, N. Bergeron, S. X. Li, F. Saliola, *Stable set polytopes and their 1-skeleta*, arXiv:1804.00360, first public 2018-04-02, https://arxiv.org/abs/1804.00360 .
4. *Euclidean facet-area boundary layers of Fibonacci stable-set polytopes*, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-euclidean-facet-area-boundary-layers-of-fibonacci-stable-set-pol--91f5f40b269c .
5. *Block-path connected-block polytopes have parity-split inradii and large incenter loci*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-block-path-connected-block-polytopes-have-parity-split-inradii-a--c3b8e999d5d4 .
6. *Path symmetric edge polytopes have an exact inradius and a codimension-one incenter family*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-path-symmetric-edge-polytopes-have-an-exact-inradius-and-a-codim--4fbd84888e21 .
7. *Fibonacci contact rigidity and exact diametral pairs of alternating adjacent-sum polytopes*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-fibonacci-contact-rigidity-and-exact-diametral-pairs-of-alternat--3cc79fb90b9e .
