# A sharp metric–volume separation under biclique deletion from a product of simplices

## Finding

Let \(a,b\ge2\) and \(1\le s<a\), \(1\le t<b\) be integers. Choose subsets \(S\subseteq[a]\), \(T\subseteq[b]\) of cardinalities \(s,t\). Write \(u=a-s\), \(v=b-t\), \(Q=\Delta_{a-1}\times\Delta_{b-1}\), and
\[
P=\operatorname{conv}\{(e_i,f_j):i\notin S\text{ or }j\notin T\}\subset\mathbb R^{a+b}.
\]
This is the standard bipartite edge-root polytope of the two-step Ferrers graph obtained by deleting the full biclique \(S\times T\) from \(K_{a,b}\), using an orthogonal sign choice on the second vertex class. All distances and volumes below are the intrinsic Euclidean quantities in \(\mathbb R^{a+b}\).

**Metric classification.** All \(st\) deleted vertices have one and the same squared distance,
\[
\boxed{d_H(Q,P)^2=\frac{(u+1)(v+1)}{2uv+u+v}.}
\]
The only farthest points of the *continuous* polytope \(Q\) are precisely those \(st\) deleted vertices; all surviving grid vertices have distance zero. For each deleted \((e_i,f_j)\), its unique nearest point is explicitly given below. It lies in the relative interior of an exposed simplex face with \(u+v\) vertices and Euclidean \((u+v-1)\)-volume
\[
\boxed{\frac{\sqrt{2uv+u+v}}{(u+v-1)!}.}
\]

**Exact volume deficit.** Put \(N=a+b-2\) and \(K=s+v-1\). The fraction of the original intrinsic volume removed by the deletion is exactly
\[
\boxed{\frac{\operatorname{vol}(Q\setminus P)}{\operatorname{vol}(Q)}
=\frac{\displaystyle\sum_{j=0}^{s-1}\binom Kj\binom{N-K}{a-1-j}}
{\binom N{a-1}},}
\]
with binomial coefficients outside their natural ranges interpreted as zero. Equivalently, this is the probability that a hypergeometric sample of size \(K\), taken from a population with \(a-1\) elements of one color and \(b-1\) of another, contains at most \(s-1\) elements of the first color.

**Gaussian metric–volume separation.** Along any integer sequence with \(a,b\to\infty\), \(s/a\) and \(t/b\) bounded away from both zero and one, let
\[
\mu=\frac sa+\frac tb-1,\qquad
\sigma^2=\frac{su}{a^2(a+1)}+\frac{tv}{b^2(b+1)}.
\]
If \(\mu/\sigma\to\lambda\in\mathbb R\), then the removed-volume fraction tends to \(\Phi(\lambda)\), where \(\Phi\) is the standard normal distribution function. If \(\mu/\sigma\to\pm\infty\), the fraction tends to one or zero, respectively. Under these same hypotheses the Hausdorff distance always tends to \(1/\sqrt2\), irrespective of that volume fraction. Thus the relative volume undergoes a sharp Gaussian crossover at \(s/a+t/b=1\) while worst-case geometric loss retains a nonzero limit.

## Assumptions and scope

For \(m\ge2\), \(\Delta_{m-1}=\{x\in\mathbb R^m:x_i\ge0,\ \sum_ix_i=1\}\), with standard coordinate unit vectors. The two vertex classes have sizes \(a,b\); \(S,T\) are proper nonempty subsets. The affine dimension of \(Q\) and \(P\) is \(a+b-2\), since both complements are nonempty and the surviving graph is connected. The displayed face volume is measured in its affine hull. The distance from \(Q\) to its subset \(P\) is the ordinary Euclidean Hausdorff distance. No affine rescaling, edge weighting, or degenerate empty block is included.

## Proof

**1. One exact separating inequality.** Every grid vertex \((e_i,f_j)\) of \(Q\) has \(x(S)+y(T)\in\{0,1,2\}\). It has value two exactly when \((i,j)\in S\times T\), and is retained otherwise. Every edge of \(Q\), as a product of simplices, changes either the first coordinate or the second coordinate but not both, so the functional \(x(S)+y(T)\) changes by at most one along any edge. Therefore the hyperplane at value one intersects no grid edge in its relative interior. Cutting by that halfspace creates no new vertices and hence
\[
P=\{(x,y)\in Q:x(S)+y(T)\le1\}.\tag{1}
\]
In particular, \(P\) is full-dimensional in the affine hull of \(Q\), because a grid vertex with \(i\notin S,j\notin T\) lies strictly below the cut.

**2. Exact missing-vertex projection.** Fix a deleted pair \((i,j)\in S\times T\). Set
\[
L=2uv+u+v,\qquad
\theta=\frac{v(u+1)}L,\qquad
\bar e=\frac1u\sum_{h\notin S}e_h,\quad
\bar f=\frac1v\sum_{\ell\notin T}f_\ell.
\]
Define
\[
z=\bigl(\theta e_i+(1-\theta)\bar e,\;(1-\theta)f_j+\theta\bar f\bigr).\tag{2}
\]
The point \(z\) is a positive convex combination of the \(v\) surviving vertices \((e_i,f_\ell)\), \(\ell\notin T\), and the \(u\) surviving vertices \((e_h,f_j)\), \(h\notin S\). To verify that it is the Euclidean projection of \(w=(e_i,f_j)\), put \(r=w-z\). The first component of \(r\) is \((1-\theta)(e_i-\bar e)\), and the second is \(\theta(f_j-\bar f)\). An allowed grid vertex maximizes \(r\cdot(e_h,f_\ell)\) only when either \(h=i,\ell\notin T\) or \(h\notin S,\ell=j\): all other allowed types have strictly smaller inner product. The two maximal values are equal exactly when
\[
(1-\theta)\left(1+\frac1u\right)=\theta\left(1+\frac1v\right),
\]
which holds by the displayed choice of \(\theta\). Thus the convex combination \(z\) is supported entirely on the exposed maximizing face, and \(r\cdot(p-z)\le0\) for every \(p\in P\). The Euclidean projection criterion yields \(z=\Pi_P(w)\). Strict convexity of squared Euclidean distance gives uniqueness. Directly,
\[
\|w-z\|^2=(1-\theta)^2\frac{u+1}{u}
+\theta^2\frac{v+1}{v}
=\frac{(u+1)(v+1)}L.\tag{3}
\]
All deleted vertices are equivalent under permutations within \(S,T\), so the distance in (3) is their common distance.

**3. Contact-face simplex and volume.** The maximizing face in step 2 has exactly the \(u+v\) vertices just identified. Pick one \((e_i,f_{\ell_0})\) with \(\ell_0\notin T\) as base point. A spanning list of edge vectors consists of \(v-1\) vectors \((0,f_\ell-f_{\ell_0})\) and \(u\) vectors \((e_h-e_i,f_j-f_{\ell_0})\), with \(\ell\in T^c\setminus\{\ell_0\}\) and \(h\in S^c\). Its Gram matrix has diagonal blocks \(I_{v-1}+J_{v-1}\) and \(I_u+3J_u\), with all-one off-diagonal blocks; its determinant is \(2uv+u+v=L\). The edge vectors are independent, so this exposed face is a \((u+v-1)\)-simplex. Its intrinsic Euclidean volume is \(\sqrt L/(u+v-1)!\). Formula (2) has strictly positive coefficients on all its vertices, hence lies in the relative interior.

**4. Complete Hausdorff classification.** Let \(w_h\) range over the grid vertices of \(Q\), and let \(z_h=\Pi_P(w_h)\). Write \(r_h=w_h-z_h\), which is zero on surviving vertices. Every \(x\in Q\) is a convex combination \(x=\sum_h\lambda_hw_h\). Since \(\sum_h\lambda_hz_h\in P\),
\[
\operatorname{dist}(x,P)^2\le\Big\|\sum_h\lambda_hr_h\Big\|^2
=\sum_h\lambda_h\|r_h\|^2
-\frac12\sum_{h,k}\lambda_h\lambda_k\|r_h-r_k\|^2.\tag{4}
\]
The right side is at most (3). Equality requires all positively weighted vertices to be deleted and their residuals identical. Distinct deleted vertices have distinct residuals, as the first and second components record the chosen indices \(i,j\) with nonzero coefficients. Equality therefore holds exactly at one deleted grid vertex. This proves both the distance and full farthest-point classification.

**5. Exact intrinsic volume loss.** A uniformly volume-distributed point of \(Q\) is a pair of independent uniform-simplex points \((X,Y)\). The coordinate sums \(U=X(S)\) and \(V=Y(T)\) are independent beta random variables, with parameters \((s,u)\) and \((t,v)\), respectively. By (1) the removed-volume fraction is \(\Pr(U+V>1)\). Setting \(W=1-V\), the second variable has beta parameters \((v,t)\). The beta variable \(U\) is distributed as the \(s\)-th order statistic from \(a-1\) independent uniform samples; \(W\) is the \(v\)-th order statistic from a separate independent sample of \(b-1\) uniforms. Pooling the two samples, their order-label sequence is a uniformly random shuffle of \(a-1\) first-color labels and \(b-1\) second-color labels. The event \(U>W\) says that among the first \(K=s+v-1\) pooled order positions there are at most \(s-1\) first-color labels. Counting these shuffles proves the stated hypergeometric finite sum. Boundary equalities have probability zero.

**6. Sharp Gaussian crossover.** Under the asymptotic hypotheses, the beta means are \(s/a\) and \(t/b\), and their exact variances are the two summands defining \(\sigma^2\). Each centered beta variable, divided by its own standard deviation, converges to a standard normal, as follows for example by writing it as a ratio of independent integer-shape gamma variables and applying the multivariate central limit theorem plus the delta method. The two variables are independent. Their standardized sum consequently converges to a standard normal even if the relative variance weights change, by the joint normal approximation or by taking convergent subsequences of those weights. Since \(\Pr(U+V>1)=\Pr((U+V-1-\mu)/\sigma>-\mu/\sigma)\), the asserted normal CDF follows whenever the standardized mean offset has a finite limit. At infinite offsets, Chebyshev's inequality gives the corresponding limits. Finally, \(u,v\to\infty\), and (3) tends to \(1/2\) in squared distance. This completes the theorem. \(\square\)

## Verification

Run `python checks/check_ferrers.py` with Python 3, NumPy, SciPy and SymPy. Its exact rational calculations cover 441 parameter quadruples with \(2\le a,b\le7\), and all 3,136 deleted ordered vertices in those cases. It checks the normal-cone projection certificate vertex by vertex, the Gram determinant, and the hypergeometric count against an independently enumerated shuffle count. One hundred separately optimized constrained quadratic programs check the projection numerically. The replay result was:

`FERRERS_DELETION_PASS configurations=441 exact_missing_vertices=3136 independent_QP=100 max_gap=3.85e-14 exact_hypergeom_and_gram=441`

Separately, exact hypergeometric probabilities at symmetric block sizes in dimensions \(100\), \(400\), and \(1600\) agree with the Gaussian critical-window prediction for standardized offsets near \(-1,0,1\). These finite computations check formulas and implementations; the claims for arbitrary dimensions rest on the analytical proof above.

## Relationship to prior work

Ohsugi and Tsuchiya (arXiv:2103.15045v1, first public 2021-03-28) study graph PQ adjacency polytopes and their relation to bipartite edge-root polytopes, emphasizing Ehrhart series and normalized volumes for join graphs. Kálmán and Tóthmérész (arXiv:2105.00960v1, first public 2021-05-03) study root-polytope dissections and volume enumerators. These results motivate the use of bipartite root polytopes but do not state the specific Euclidean deleted-vertex projection, contact-simplex volume, or metric–hypergeometric crossover of the present two-step Ferrers family.

A published analysis titled *Hall-deficit quadratic law for minimum spheres of two-step Ferrers root polytopes* treats exactly the same graph family, but determines its minimum enclosing sphere and contact vertices; neither its radius formula nor its proof determines distances to the undeleted product, the missing-root projection simplex, or the removed-volume ratio. The previously studied crown-graph root polytope deletes a matching rather than a full biclique, and its distance and width laws have different formulas. The general beta and order-statistic identities are standard; novelty is claimed only for their joint exact application with this family's Euclidean projection geometry and Gaussian threshold. A stronger unlocated earlier Ferrers-volume or metric comparison remains a priority risk.

## Limitations

The theorem covers a single nonempty proper forbidden biclique in an otherwise complete bipartite graph. It does not supply an arbitrary multi-block deletion theorem, nor does it describe the pointwise projection of *every interior point* of \(Q\). Orthogonal sign reversal of one color class preserves the results, but general affine transformations need not. Historical priority is provisional, and independent mathematical audit has not been performed.

## References

1. H. Ohsugi and A. Tsuchiya, *PQ-type adjacency polytopes of join graphs*, arXiv:2103.15045v1 (2021-03-28), https://arxiv.org/abs/2103.15045; Discrete & Computational Geometry 70 (2023), 214–235.
2. T. Kálmán and L. Tóthmérész, *Root polytopes and Jaeger-type dissections for directed graphs*, arXiv:2105.00960v1 (2021-05-03), https://arxiv.org/abs/2105.00960; Mathematika 68 (2022), 1176–1220.
3. *Hall-deficit quadratic law for minimum spheres of two-step Ferrers root polytopes*, publicly accessible mathematical record identifier a696c8661d8e (2026).
4. *Rare exponential directional loss despite constant Hausdorff distance in crown-graph root polytopes*, publicly accessible mathematical record identifier 771379f5fcb8 (2026).
