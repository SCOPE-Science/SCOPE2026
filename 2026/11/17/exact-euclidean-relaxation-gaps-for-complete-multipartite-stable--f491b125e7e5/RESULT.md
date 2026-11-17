# Exact Euclidean relaxation gaps for complete multipartite stable-set polytopes

## Finding
Let \(G=K_{a_1,\ldots,a_r}\) be a complete multipartite graph with \(r\ge3\) nonempty classes \(V_i\), with integer sizes \(a_i\ge1\), and total order \(n=\sum_i a_i\). In \(\mathbb R^n\) with its standard orthonormal coordinates, set
\[
P=\operatorname{conv}\{\mathbf1_I:I\text{ is a stable set of }G\},
\qquad
F=\{x\ge0:x_u+x_v\le1\text{ for every }uv\in E(G)\}.
\]
This is the ordinary edge-inequality fractional stable-set relaxation (not the stronger all-clique relaxation). Define \(h=\frac12\mathbf1_n\) and \(S=(r-2)/2\). There is a unique \(\lambda>0\) solving
\[
\sum_{i=1}^r\min\left\{\frac12,\frac{\lambda}{a_i}\right\}=S.
\]
Then the exact (symmetric, since \(P\subset F\)) Euclidean Hausdorff distance is
\[
\boxed{d_H(F,P)^2=\sum_{i=1}^r a_i
\min\left\{\frac12,\frac{\lambda}{a_i}\right\}^{\!2}.}
\]
The **unique farthest point in the entire continuous polytope** \(F\) is \(h\). Its **unique nearest point** in \(P\) has constant coordinate \(\frac12-\min\{\frac12,\lambda/a_i\}\) on class \(V_i\). Thus every contact/screening transition is captured by the inequalities \(a_i\le2\lambda\), at which the projection has zero coordinates on class \(V_i\).

For three classes, no class is screened and the expression simplifies to
\[
\boxed{d_H(F,P)^2=\frac{1}{4\left(a_1^{-1}+a_2^{-1}+a_3^{-1}\right)}.}
\]
For every fixed \(r\) and total order \(n\), the squared gap is uniquely maximized, up to class permutation, by the most balanced positive-integer size profile; it is uniquely minimized by \((n-r+1,1,\ldots,1)\). The latter has the exact squared gap
\[
\boxed{D_{\min}^2=\frac{(r-2)^2}{4\left(r-1+(n-r+1)^{-1}\right)}.}
\]
If \(r\) divides \(n\), the balanced squared gap is \(D_{\max}^2=n(r-2)^2/(4r^2)\). For fixed \(r\) with \(n\to\infty\), balanced profiles have \(D_{\max}^2=n(r-2)^2/(4r^2)+O(n^{-1})\), while \(D_{\min}^2\to (r-2)^2/[4(r-1)]\).

An explicit **facet-contact transition** occurs for four classes of sizes \((a,b,b,b)\), where \(1\le a\le b\):
\[
\boxed{
 d_H(F,P)^2=\begin{cases}
 a/4+b/12,&3a\le b,\\
 ab/(b+3a),&3a\ge b.
\end{cases}}
\]
For \(3a\le b\), the nearest point to \(h\) vanishes identically on the size-\(a\) class and equals \(1/3\) on the other three classes; for \(3a>b\) it is strictly positive on all four classes.

## Assumptions and scope
All classes have positive integer size, \(r\ge3\), and all distances are ambient Euclidean distances in the original vertex-coordinate realization. The edge relaxation is \(F\), not the clique-relaxed polytope. Its compactness follows because every vertex has a neighbor and its coordinate is at most one. The borderline case \(r=2\) is excluded from the theorem: there the edge relaxation equals the integral stable-set polytope and its Hausdorff gap is zero.

## Proof
**1. An exact description of the integral polytope.** Put \(B_i=\{x\in[0,1]^n:\operatorname{supp}(x)\subseteq V_i\}\). Every stable set lies in one class, so \(P=\operatorname{conv}(\bigcup_i B_i)\). Equivalently,
\[
\boxed{P=\left\{x\ge0:\sum_{i=1}^r\|x_{V_i}\|_\infty\le1\right\}.}
\]
Indeed, convexity of each block maximum proves necessity. Conversely, for any such \(x\), write \(m_i=\|x_{V_i}\|_\infty\) and \(\sum_i m_i\le1\); the vectors \(x_{V_i}/m_i\), when \(m_i>0\), belong to \(B_i\) and reconstruct \(x\) by a convex combination, using the origin for any leftover mass. This description shows that \(P\) is coordinatewise down-closed.

**2. Complete vertex classification of the fractional relaxation.** A vertex of \(F\) is either a stable-set indicator vector, or a \(0,1/2\)-vector whose positive support meets at least three distinct classes. To prove this, consider a vertex \(x\) and the graph \(H\) of tight edge inequalities \(x_u+x_v=1\), restricted to its strictly positive support. If any coordinate is one, all other classes must be zero, while vertexhood forces each remaining coordinate to be either zero or one. Otherwise all positive coordinates are strictly between zero and one. The tight-edge equations on every connected component of \(H\) must have full column rank: a bipartite component admits a nonzero alternating perturbation in both signs, contradicting vertexhood (all other constraints have positive slack). Every component is therefore nonbipartite. Along an odd tight-edge cycle the equations force value \(1/2\), and connectedness forces the same value throughout the component. Any two such components would have tight edges between them, because each nonbipartite component contains vertices from at least three classes. Therefore there is one component and all positive coordinates equal \(1/2\). The support meets at least three classes; conversely, the zero-coordinate equations together with the cross-class tight equations on any three occupied classes determine the \(1/2\)-vector uniquely, hence it is a vertex. The integral vertices are exactly stable-set indicators.

**3. The unique farthest point.** The all-half vector \(h\) is a fractional vertex because \(r\ge3\). The function \(x\mapsto\operatorname{dist}(x,P)\) is convex; hence its maximum over \(F\) occurs at a vertex. Every integral vertex has zero distance. Consider any other fractional vertex \(u\ne h\), which is obtained from \(h\) by replacing some positive half-coordinates with zeros. Let \(p\) be the unique Euclidean projection of \(h\) onto \(P\). The projection is invariant under within-class permutations and has all coordinates strictly below \(1/2\): the constant-block formula in Step 4 proves this directly. Since \(P\) is down-closed, \(q=\min(p,u)\) coordinatewise belongs to \(P\). Coordinatewise \(|u_j-q_j|\le|h_j-p_j|\), and at every removed coordinate the left side is zero while the right side is strictly positive. Hence \(\operatorname{dist}(u,P)<\operatorname{dist}(h,P)\). Finally any nonvertex point is a nontrivial convex combination of vertices, at least one with strictly smaller distance, so convexity makes the inequality strict there as well. Thus \(h\) alone realizes the Hausdorff gap.

**4. Exact projection and thresholds.** The nearest point of \(P\) to \(h\) exists and is unique by strict convexity of squared Euclidean distance. Permuting coordinates within each class leaves \(P\) and \(h\) invariant, so that point has value \(t_i\) on class \(i\). The constraints reduce to \(t_i\ge0\) and \(\sum_i t_i\le1\). Clearly \(t_i\le1/2\), and since \(r\ge3\), the inequality \(\sum_i t_i\le1\) must be tight. Write \(s_i=1/2-t_i\). We must minimize the strictly convex quadratic
\[
 f(a_1,\ldots,a_r)=\min\left\{\sum_i a_i s_i^2:
0\le s_i\le1/2,\quad\sum_i s_i=(r-2)/2\right\}.
\]
Karush–Kuhn–Tucker conditions give \(s_i=\min\{1/2,\lambda/a_i\}\). The sum of these terms is continuous and strictly increasing up to the required target, giving a unique positive \(\lambda\). In particular every \(s_i>0\), so every coordinate of the projection is strictly below \(1/2\), as used above. For \(r=3\), the total \(\sum_i s_i=1/2\) and each term is positive, so none can saturate; elementary substitution yields the reciprocal-sum formula.

**5. Sharp balance law and extremizers.** At fixed \(r,n\), extend the size parameters to real values \(a_i\ge1\) with \(\sum_i a_i=n\). The displayed variational formula is the infimum of affine functions in the parameter vector \(a\), so \(f\) is concave; it is symmetric, hence Schur-concave. The optimizer \(s\) is unique. If the largest and smallest sizes differ, their optimal coordinates satisfy \(s_{\max}<s_{\min}\): the largest class cannot saturate \(s=1/2\), since that would force every class to saturate and violate \(\sum_i s_i=(r-2)/2\). Consequently the optimizers for the profile and its transposition of the largest and smallest classes differ. By strict equality conditions for an infimum of affine functions with unique optimizers, a nontrivial averaging of these two permuted profiles strictly increases \(f\). Iterating integer one-unit transfers proves that the balanced positive-integer profile is the unique maximizer up to permutation. For the minimum, the feasible real size simplex has extreme points consisting of the permutations of \((n-r+1,1,\ldots,1)\). By concavity each has the common minimum value. Their unique optimizers differ when \(n>r\), so mixing distinct extrema strictly increases the value; hence the only minimizing integer profiles are the stated extrema. The case \(n=r\) has just one profile.

For the extreme profile let \(A=n-r+1\). The optimum is interior to the cap \(s_i\le1/2\), because \(\lambda=\frac{(r-2)/2}{r-1+1/A}<1/2\). Thus \(f=S^2/(r-1+1/A)\), yielding the exact minimum. For balanced sizes divisible by \(r\), the optimizer is \(s_i=(r-2)/(2r)\), giving the exact maximum. If the balanced sizes differ by at most one, the unsaturated reciprocal-sum formula applies for all sufficiently large \(n\) with \(r\) fixed, and expansion of \(\sum_i a_i^{-1}\) gives the stated asymptotic.

**6. Four-class transition.** For profile \((a,b,b,b)\), the constraint is \(\sum_i s_i=1\). If no upper cap is active then \(\lambda=(a^{-1}+3b^{-1})^{-1}\), and the smallest-class term \(\lambda/a=b/(b+3a)\) is below \(1/2\) exactly when \(3a\ge b\). If \(3a\le b\), the small-class term saturates at \(1/2\) and each other term equals \(1/6\). Substitution gives the two branches, agreeing at the threshold.

## Verification
`check_fractional_multipartite.py` independently enumerates the fractional relaxation's vertices using numerical halfspace intersection for small graphs; checks their \(0,1/2,1\) types; compares the exact rational threshold formula against a direct numerical constrained projection in the full coordinate space; and exhaustively checks balanced/maximally unequal extremizers on finite positive-integer class-size profiles. Its successful run reports `MULTIPARTITE_HAUSDORFF_PASS numerical_projections=17 independent_halfspace_vertices=230 exact_majorization_profiles=274`. The infinite claims are proved in Steps 1–6; numerical optimizations and finite enumeration are corroborative only.

## Relationship to prior work
De Vries, Friedrich, and Perscheid's work provides the conventional edge-constrained fractional stable-set polytope and studies stronger odd-cycle and wheel relaxations, but not these Euclidean separation metrics. Aliniaeifard and collaborators characterize stable-set polytope edges and combinatorial diameters in the standard coordinate embedding, not the Hausdorff distance to the fractional relaxation. Samer and Haugland discuss the half-integrality of the edge relaxation and fixed-cardinality stable sets, including complete multipartite graphs, but their fixed-cardinality optimization does not supply a Euclidean projection or the present exact relaxation gap. Existing results on minimum enclosing spheres and Gaussian widths of multipartite stable-set polytopes address different extremization problems and do not imply this fractional-to-integral distance. The simple complete-graph case is included here as a specialization, not claimed as an independent contribution.

## Limitations
Historical priority is provisional. The result is specific to the *edge* relaxation and ambient standard Euclidean metric; switching to clique inequalities makes \(F=P\) for a complete multipartite graph, since that graph is perfect. No claim about other norms, arbitrary graphs, or independent third-party certification is made. The finite checker is not a formal proof of the unrestricted theorem.

## References
- S. de Vries, U. Friedrich, B. Perscheid, *An extended formulation for the 1-wheel inequalities of the stable set polytope*, Networks 75 (2020), 86–94, first public 17 October 2019. https://doi.org/10.1002/net.21906
- F. Aliniaeifard, C. Benedetti, N. Bergeron, S. X. Li, F. Saliola, *Stable set polytopes and their 1-skeleta*, arXiv:1804.00360, first public 2 April 2018. https://arxiv.org/abs/1804.00360
- P. Samer, D. Haugland, *Fixed cardinality stable sets*, Discrete Applied Mathematics 303 (2021), 1–17. https://doi.org/10.1016/j.dam.2021.01.019
