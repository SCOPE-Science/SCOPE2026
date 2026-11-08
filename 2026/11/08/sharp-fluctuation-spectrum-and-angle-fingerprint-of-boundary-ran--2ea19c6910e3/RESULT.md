# Sharp fluctuation spectrum and angle fingerprint of boundary-random polygon area loss

## Finding

Let \(Q\subset\mathbb R^2\) be a fixed nondegenerate convex polygon with \(m\ge3\) vertices and perimeter \(P>0\). Its exterior turning angles, indexed cyclically, are \(\theta_i\in(0,\pi)\), so that \(\sum_{i=1}^m\theta_i=2\pi\). Choose \(N\) independent points uniformly by arclength on the *entire* boundary, let \(Q_N\) be their convex hull, and set \(\Delta_N=\operatorname{area}(Q)-\operatorname{area}(Q_N)\). For mutually independent standard exponential variables \(E_i,F_i\), \(1\le i\le m\), define \(Z_i=E_iF_i\). Then

\[
N^2\Delta_N\ \xrightarrow{\ \mathrm d\ }\ S_Q=\frac{P^2}{2}\sum_{i=1}^m\sin\theta_i\,Z_i.
\]

**Every fixed positive integer moment converges**. In particular,

\[
\lim_{N\to\infty}N^2\mathbb E\Delta_N=\frac{P^2}{2}\sum_i\sin\theta_i,\qquad
\lim_{N\to\infty}N^4\operatorname{Var}(\Delta_N)=\frac{3P^4}{4}\sum_i\sin^2\theta_i.
\]

The limiting law is non-Gaussian. For every integer \(k\ge1\) its \(k\)-th cumulant is

\[
\operatorname{cum}_k(S_Q)=c_k\left(\frac{P^2}{2}\right)^k\sum_i(\sin\theta_i)^k,
\]

where \(c_k>0\) is the number of *transitive ordered pairs of permutations* of a \(k\)-element labeled set. In particular \(c_1=1\), \(c_2=3\), \(c_3=26\), \(c_4=426\). Consequently **if the perimeter \(P\) and number \(m\) of sides are known, the first \(m\) limiting cumulants determine exactly the multiset** \(\{\sin\theta_1,\ldots,\sin\theta_m\}\), with multiplicities. This does not imply recovery of side lengths or the ordered polygon.

**Sharp complete fluctuation range.** Define the scale-free limiting squared coefficient of variation by

\[
R(Q)=\lim_{N\to\infty}\frac{\operatorname{Var}(\Delta_N)}{(\mathbb E\Delta_N)^2}
=3\,\frac{\sum_i\sin^2\theta_i}{(\sum_i\sin\theta_i)^2}.
\]

For every fixed number of vertices \(m\ge3\), its **complete attainable range over convex polygons** is

\[
\boxed{\frac3m\le R(Q)<\frac32.}
\]

The lower equality cases have an exact classification by their exterior-angle multisets: for \(m=3\), only three angles \(2\pi/3\); for \(m=4\), exactly \(\{x,x,\pi-x,\pi-x\}\), \(0<x\le\pi/2\); and for \(m\ge5\), either all angles are \(2\pi/m\), or precisely \(m-1\) are \(\pi/(m-2)\) and the remaining angle is \(\pi-\pi/(m-2)\). **Non-equiangular minimizers therefore exist for every \(m\ge4\)**. The strict upper bound is sharp and approached by degenerating families but is never attained by a nondegenerate convex polygon.

The limiting expected area deficit has the sharp upper bound

\[
\lim_{N\to\infty}N^2\mathbb E\Delta_N\le\frac{P^2m}{2}\sin\frac{2\pi}{m},
\]

with equality **if and only if** \(Q\) is equiangular (not necessarily equilateral for \(m\ge4\)).

## Assumptions and scope

The polygon is fixed while \(N\to\infty\), has exactly \(m\) noncollinear successive edges of positive length, no reflex turns, and interior angles in \((0,\pi)\). Each of the \(N\) samples is independent and arclength-uniform. Area is ordinary Euclidean area; all random variables \(E_i,F_i\) above are independent with density \(e^{-x}\mathbf1_{x>0}\). The ambient classification is random convex sets and integral geometry (MSC2020 52A22).

## Proof

**Exact finite-sample corner decomposition.** For the vertex \(v_i\), let \(a_{i,N}\) and \(b_{i,N}\) be the distances along its two incident edges to the nearest sample on each edge. Work on event \(G_N\) that every edge carries at least one sampled point. Every sampled point in the interior of an edge between its first and last sample is redundant for its convex hull. Thus the portion of \(Q\) absent from \(Q_N\) is the union, with disjoint interiors, of the \(m\) corner triangles whose vertices are \(v_i\) and the nearest sample on the two incident edges. Their areas are \(\tfrac12a_{i,N}b_{i,N}\sin\theta_i\). Hence on \(G_N\),

\[
\Delta_N=\frac12\sum_{i=1}^m a_{i,N}b_{i,N}\sin\theta_i.\tag{1}
\]

Let \(\ell_{\min}\) denote the shortest side. Since arclength is uniform, a union bound gives \(\Pr(G_N^c)\le m(1-\ell_{\min}/P)^N\).

**Endpoint Poisson limit.** Fix any nonnegative numbers \(u_1,\ldots,u_{2m}\). For all large \(N\), the \(2m\) arcs of length \(Pu_j/N\) starting at the two sides of each polygon vertex are pairwise disjoint. The probability that none of the \(N\) uniform samples lies in their union is exactly \(\bigl(1-\sum_j u_j/N\bigr)^N\), which tends to \(e^{-\sum_j u_j}\). This joint survival convergence proves

\[
\left\{\frac N P a_{i,N},\frac N P b_{i,N}:1\le i\le m\right\}
\xrightarrow{\mathrm d}\{E_i,F_i:1\le i\le m\},
\]

with all \(2m\) limits independent. Formula (1) and the continuous mapping theorem prove the asserted distributional limit on \(G_N\); the exponentially rare complement does not affect weak convergence.

**Convergence of every moment.** For any endpoint distance \(g_N\) along a particular side, and for \(0\le t<N\ell/P\),

\[
\Pr(Ng_N/P>t)=(1-t/N)^N\le e^{-t}.
\]

For larger \(t\) the event is empty (take the nearest distance as the full side length when no point lies on the edge). Thus the family of normalized endpoint distances is bounded in every positive moment uniformly in \(N\). By Hölder's inequality, the products and their finite sums in (1), multiplied by \(N^2\), are uniformly bounded in every moment on \(G_N\). On \(G_N^c\), use \(0\le\Delta_N\le\operatorname{area}(Q)\) and its exponentially small probability; its contribution to any fixed moment of \(N^2\Delta_N\) tends to zero. This yields uniform integrability of all powers and hence convergence of all positive integer moments. The expectation and variance follow from \(\mathbb E Z=1\), \(\mathbb E Z^2=4\), and \(\operatorname{Var}(Z)=3\).

**Full law and positive cumulants.** Since \(Z=EF\) with independent standard exponentials,

\[
\mathbb E[Z^k]=(k!)^2,\qquad
\mathbb E[e^{-uZ}]=\int_0^\infty\frac{e^{-x}}{1+ux}\,dx\quad(u\ge0).
\]

The Laplace transform of \(S_Q\) is the product of the latter integrals with \(u\) replaced by \(uP^2\sin\theta_i/2\). To prove \(c_k=\operatorname{cum}_k(Z)>0\) for all \(k\), count ordered pairs \((\sigma,\tau)\) of permutations of \(\{1,\ldots,k\}\). There are \((k!)^2\) pairs. Partition the labeled set into the orbits of the subgroup generated by \(\sigma,\tau\); on each block the restrictions form a *transitive* pair. Conversely, a set partition decorated with transitive pairs on each block uniquely defines a pair of permutations. The resulting partition decomposition is exactly the classical moment–cumulant formula, so \(c_k\) counts transitive pairs. It is strictly positive because taking \(\sigma\) to be any full \(k\)-cycle and \(\tau\) the identity gives such a pair. Additivity and homogeneity of cumulants for independent variables yield the displayed cumulant formula. The strictly positive third cumulant excludes a Gaussian law.

**Angle-spectrum reconstruction.** Given \(P\) and \(m\), divide \(\operatorname{cum}_k(S_Q)\) by \(c_k(P^2/2)^k\), for \(1\le k\le m\). This gives the first \(m\) power sums of the positive numbers \(\sin\theta_i\). Newton's identities recover their elementary symmetric functions, hence the monic polynomial with these numbers as roots and the complete unordered multiset. No choice between the supplementary exterior angles is claimed.

**Complete normalized fluctuation range and equality cases.** Write \(s_i=\sin\theta_i>0\) and \(w_i=s_i/\sum_j s_j\), so \(R(Q)=3\sum_i w_i^2\). Cauchy–Schwarz gives \(R(Q)\ge3/m\), with equality exactly when every \(s_i\) is equal.

For the strict upper bound, fix any \(i\). The other \(m-1\) turning angles lie in \((0,\pi)\) and sum to \(2\pi-\theta_i\in(\pi,2\pi)\). Minimizing the concave function \(\sum_{j\ne i}\sin\theta_j\) on the closed polytope of angles in \([0,\pi]\) with that fixed sum reduces to its extreme points. Each such vertex has one angle \(\pi\), one \(\pi-\theta_i\), and all other angles zero; therefore its sine sum is \(\sin\theta_i\). Strict concavity and positivity of every actual angle give \(\sum_{j\ne i}\sin\theta_j>\sin\theta_i\). Thus every \(w_i<1/2\), and

\[
3\sum_i w_i^2<3\Bigl(\max_i w_i\Bigr)\sum_iw_i<\frac32.
\]

For lower equality classification, common positive sine implies that, for some \(x\in(0,\pi/2]\), every turning angle equals either \(x\) or \(\pi-x\). If \(q\) of the \(m\) angles are \(\pi-x\), their sum equals \(q\pi+(m-2q)x=2\pi\). Solving this equation with \(0<x<\pi/2\) and integer \(0\le q\le m\) leaves only: \(m=3,q=3,x=\pi/3\); \(m=4,q=2\) with arbitrary \(x\in(0,\pi/2)\); \(m\ge5,q=0,x=2\pi/m\); or \(m\ge5,q=1,x=\pi/(m-2)\). The case \(x=\pi/2\) requires \(m=4\). These are precisely the multisets stated above.

Every admissible turning-angle vector \(\theta\in(0,\pi)^m\) summing to \(2\pi\) occurs in some convex \(m\)-gon: take successive outward unit normals separated by these angles and intersect their tangent supporting half-planes to the unit disk. Adjacent tangent lines meet, and each tangent line contributes a positive-length side since every gap is strictly below \(\pi\); this gives a bounded convex polygon with the prescribed turning angles. In particular the exceptional equality patterns are attained. Choosing turns tending to \((\pi,\pi/2,\pi/2,0,\ldots,0)\) shows \(R(Q)\to3/2\). Finally, the allowed turning-angle region is convex and hence connected; the continuous image of this region under \(R\) is an interval. It contains \(3/m\), has supremum \(3/2\), and never attains its supremum, so its exact range is \([3/m,3/2)\).

**Sharp expected area-loss bound.** Set \(\theta_i=\pi-\alpha_i\), where \(\alpha_i\) is the interior angle. Then \(0<\theta_i<\pi\), and \(\sum_i\theta_i=2\pi\). Since sine is strictly concave on \((0,\pi)\), Jensen's inequality gives \(\sum_i\sin\theta_i\le m\sin(2\pi/m)\) with equality precisely when all turns equal. This is exactly the equiangularity condition, and regular polygons show attainability. This proves the bound and its equality characterization.

## Verification

The standalone program `check_area_loss.py` checks an exact rational-polygon corner decomposition, verifies the first four cumulants both algebraically and by enumerating transitive permutation pairs, numerically checks the product-exponential Laplace integral, and compares direct convex-hull simulations against the sharp asymptotic mean on a nonsymmetric quadrilateral. Its deterministic execution produced:

`CHECK_OK exact_corner_deficit=7/8 cumulants=[1, 3, 26, 426] MonteCarlo_N800_mean=140.390 predicted=135.976 exact_decomposition_maxerr=1.6e-15 fluctuation_shape_checks=1520`

Only the finite checks are experimental; the limit law, all-moment convergence, identifiability and sharp extremizer follow from the analytic argument above. Run with Python 3.9+, NumPy and SciPy.

## Relationship to prior work

The 2011 Groeneboom manuscript concerns convex hulls of *interior-uniform* points in polygons and gives Gaussian fluctuation limits on different scales. Schütt and Werner's earlier boundary-sampling theory imposes two-sided rolling-ball conditions and concerns smooth convex bodies; its main theorem does not apply to polygon corners. Reitzner, Schütt and Werner's 2019 preprint/2023 paper considers boundary-uniform sampling in simple polytopes and proves orders of the *expected* volume deficit; the relevant theorem does not supply the explicit planar non-Gaussian area-loss distribution, its cumulant angle spectrum or sharp equiangular maximum. A related boundary-polygon *perimeter-deficit* law uses the same limiting endpoint gaps but a different local geometric functional; it does not classify the area-deficit fluctuation ratio or its non-equiangular equality cases. The 2024 study by Prochno, Schütt, Sonnleitner and Werner treats the *Hausdorff* distance of boundary-sampled polygons (another error functional). These comparisons establish mathematical distinctions, not a guarantee of historical priority.

## Limitations

The result holds for each fixed, strictly convex-angled polygon as sample size tends to infinity. It gives no uniform rate when the number of sides increases or a side degenerates, and no finite-sample statistical confidence bound. The limiting law determines the multiset of sines of the turning angles, not the ordered angles, side lengths, or congruence class. Asymptotic independence is for the microscopic endpoint gaps, not exact finite-sample independence. Historical novelty remains subject to independent literature assessment.

## References

1. P. Groeneboom, *Convex hulls of uniform samples from a convex polygon*, arXiv:1109.3118, first posted 2011-09-14. https://arxiv.org/abs/1109.3118 (interior-sampling comparison).
2. C. Schütt and E. Werner, *Polytopes with Vertices Chosen Randomly from the Boundary of a Convex Body*, Geometric Aspects of Functional Analysis, LNM 1807, 241–422 (2003). https://case.edu/artsci/math/werner/publications/rpbd.pdf (smooth rolling-ball case).
3. M. Reitzner, C. Schütt and E. Werner, *The Convex Hull of Random Points on the Boundary of a Simple Polytope*, arXiv:1911.05917, first posted 2019-11-14; Discrete Comput. Geom. 69 (2023), 453–504. https://doi.org/10.1007/s00454-022-00460-2 (facet counts and expected-volume asymptotics).
4. J. Prochno, C. Schütt, M. Sonnleitner and E. M. Werner, *Random Approximation of Convex Bodies in Hausdorff Metric*, arXiv:2404.02870, first posted 2024-04-03. https://arxiv.org/abs/2404.02870 (boundary-polygon Hausdorff comparison).
