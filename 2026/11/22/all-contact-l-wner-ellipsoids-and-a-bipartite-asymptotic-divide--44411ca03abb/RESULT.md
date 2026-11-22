# All-contact Löwner ellipsoids and a bipartite asymptotic divide for balanced multipartite PQ polytopes

## Finding
Let \(r\ge3\) and \(s\ge2\) be integers, \(N=rs\), \(d=2(N-1)\), and let \(G=K_{s,\ldots,s}\) be the complete \(r\)-partite graph with \(s\) vertices per class. In the standard Euclidean realization, its PQ-type adjacency polytope is
\[
P_{r,s}=\operatorname{conv}\{(e_i,e_j):i=j\text{ or }i,j\text{ belong to different classes}\}\subset\mathbb R^N\oplus\mathbb R^N.
\]
Define \(p\in(0,1)\) as the unique positive root
\[
\boxed{r(rs-1)p^2+[rs(r-2)+1]p-(r-1)=0,\qquad
p=\frac{2(r-1)}{rs(r-2)+1+\sqrt{[rs(r-2)+1]^2+4r(rs-1)(r-1)}}.}
\]
The unique minimum-volume enclosing **Löwner ellipsoid** of \(P_{r,s}\) is given explicitly below. Every one of its \(N[1+(r-1)s]\) vertices touches the ellipsoid; no nonvertex polytope point touches it.

Write \(\bar e=N^{-1}\mathbf1\), and define \(U=((x-\bar e)+(y-\bar e))/\sqrt2\), \(V=((x-\bar e)-(y-\bar e))/\sqrt2\). On \(\mathbf1^\perp\), let \(\Pi_B\) be orthogonal projection onto the \((r-1)\)-dimensional space of vectors constant within each class, and let \(\Pi_T\) project onto the \(r(s-1)\)-dimensional space of vectors summing to zero separately within each class. Define four positive quantities
\[
\begin{aligned}
\lambda_{UB}&=\frac{r-2+rp}{N(r-1)},& \lambda_{UT}&=\frac{1+p}{N},\\
\lambda_{VB}&=\frac{r(1-p)}{N(r-1)},& \lambda_{VT}&=\frac{1-p}{N}.
\end{aligned}
\]
Then in the affine hull \(\sum_i x_i=\sum_i y_i=1\),
\[
\boxed{\mathcal E_{r,s}=\left\{(x,y):
\frac{\|\Pi_BU\|^2}{\lambda_{UB}}+\frac{\|\Pi_TU\|^2}{\lambda_{UT}}+
\frac{\|\Pi_BV\|^2}{\lambda_{VB}}+\frac{\|\Pi_TV\|^2}{\lambda_{VT}}\le d\right\}.}
\]
The four squared intrinsic Euclidean semiaxis lengths are \(d\lambda_{UB}\) (multiplicity \(r-1\)), \(d\lambda_{UT}\) (multiplicity \(r(s-1)\)), \(d\lambda_{VB}\) (multiplicity \(r-1\)), and \(d\lambda_{VT}\) (multiplicity \(r(s-1)\)).

The minimum enclosing Euclidean ball \(\mathcal B_{r,s}\) has center \((\bar e,\bar e)\), radius \(\sqrt{2(1-N^{-1})}\), and also touches all the vertices. Nevertheless the ratio of intrinsic volumes is
\[
\boxed{\frac{\operatorname{vol}_d(\mathcal E_{r,s})}{\operatorname{vol}_d(\mathcal B_{r,s})}
=\left[\frac{r(r-2+rp)(1-p)}{(r-1)^2}\right]^{(r-1)/2}
(1-p^2)^{r(s-1)/2}.}
\]
For each **fixed** \(r\ge3\), this ratio tends to the **strictly positive** constant
\[
\boxed{\lim_{s\to\infty}\frac{\operatorname{vol}_d(\mathcal E_{r,s})}{\operatorname{vol}_d(\mathcal B_{r,s})}
=\left[\frac{r(r-2)}{(r-1)^2}\right]^{(r-1)/2}>0.}
\]
In particular the tripartite limit is \(3/4\). This contrasts sharply with the **previously known** balanced bipartite case \(r=2\), whose corresponding volume ratio tends to zero at order \(s^{-1/4}\). The optimal diagonal-contact probability \(p\) equals the uniform-vertex diagonal probability \([1+(r-1)s]^{-1}\) **exactly when \(s=2\)**, and is strictly larger when \(s>2\).

## Assumptions and scope
All graph parts have equal integer size \(s\ge2\), and there are \(r\ge3\) parts. The two coordinate blocks carry the standard ambient Euclidean metric inherited from \(\mathbb R^{2N}\); semiaxis lengths and volume are intrinsic to the \(d\)-dimensional affine hull, not lattice-normalized volumes. Each allowed ordered pair \((e_i,e_j)\) is indeed a polytope vertex because it is a vertex of the ambient product of standard simplices. The covariance below has rank \(d\), proving that the displayed pair of coordinate-sum equations describes the complete affine hull. A minimum-volume ellipsoid is considered among **all** positive-definite ellipsoids in that affine hull, with unrestricted center and no symmetry imposed on competitors.

## Proof
**1. Balanced vertex contact measure.** Every class has \(s\) vertices, and each graph vertex has \(k=(r-1)s\) neighbors. Give each of the \(N\) diagonal vertices \((e_i,e_i)\) mass \(p/N\) and each of the \(Nk\) oriented graph-edge vertices \((e_i,e_j)\) mass \((1-p)/(Nk)\). These masses are positive and total one. Both coordinate marginals are uniform on the \(N\) labels, hence the mean is \(c=(\bar e,\bar e)\).

Put \(H=I-\mathbf1\mathbf1^{\mathsf T}/N\), and let \(A\) be the adjacency matrix of \(G\). The centered covariance \(C\) in the original \((x,y)\) chart has diagonal blocks \(H/N\) and off-diagonal blocks
\[
\frac1N\left[pH+(1-p)\left(\frac Ak-\frac{\mathbf1\mathbf1^{\mathsf T}}N\right)\right].
\]
The graph adjacency operator acts as \(-sI\) on \(B\) and as zero on \(T\). Passing to orthogonal \((U,V)\) coordinates therefore diagonalizes \(C\): its \(U\)- and \(V\)-blocks are
\[
C_U=\frac1N[(1+p)H+(1-p)A/k],\qquad
C_V=\frac{1-p}N[H-A/k],
\]
with the four stated eigenvalues and multiplicities. All are strictly positive for \(r\ge3\) and \(0<p<1\). Thus \(\mathcal E_{r,s}=\{z:(z-c)^{\mathsf T}C^{-1}(z-c)\le d\}\).

**2. Exact contact equality.** The projections of a diagonal vertex, centered at \(c\), onto \(U_B,U_T\) have squared norms \(2(r-1)/N\) and \(2r(s-1)/N\); its \(V\) components vanish. Its squared inverse-covariance norm is therefore
\[
Q_D=\frac{2(r-1)^2}{r-2+rp}+\frac{2r(s-1)}{1+p}.
\]
For a directed graph-edge vertex with labels in different classes, the squared projection norms onto \(U_B,U_T,V_B,V_T\) are, respectively, \((r-2)/N\), \(r(s-1)/N\), \(r/N\), and \(r(s-1)/N\). Its squared inverse-covariance norm is
\[
Q_E=\frac{(r-2)(r-1)}{r-2+rp}+\frac{r(s-1)}{1+p}+\frac{rs-1}{1-p}.
\]
Their difference is
\[
F(p)=Q_D-Q_E=
\frac{r(r-1)}{r-2+rp}+\frac{r(s-1)}{1+p}-\frac{rs-1}{1-p}.
\]
On \((0,1)\), \(F\) is strictly decreasing, with \(F(0)>0\) and \(F(p)\to-\infty\) as \(p\uparrow1\). Clearing positive denominators shows that \(F(p)=0\) is exactly the displayed quadratic equation. Thus the specified \(p\) is unique and \(Q_D=Q_E\). Since the contact-mass average of the two values equals \(\operatorname{tr}(C^{-1}C)=d\), both values equal \(d\). Every generating vertex is on \(\partial\mathcal E_{r,s}\), so the whole convex hull lies inside. Because the quadratic form is strictly convex, every nontrivial convex combination of distinct vertices lies strictly inside the ellipsoid; there are no other contacts.

**3. Unrestricted optimality and uniqueness.** Any other containing ellipsoid in the same affine hull can be written \(\{z:(z-a)^{\mathsf T}S^{-1}(z-a)\le1\}\) for positive-definite \(S\). Average its vertex containment inequalities with the positive contact weights. Since the contact mean is \(c\) and covariance is \(C\),
\[
\operatorname{tr}(S^{-1}C)+(a-c)^{\mathsf T}S^{-1}(a-c)\le1.
\]
Applying the arithmetic-geometric mean inequality to the \(d\) positive eigenvalues of \(C^{1/2}S^{-1}C^{1/2}\) gives
\[
d\left(\frac{\det C}{\det S}\right)^{1/d}\le\operatorname{tr}(S^{-1}C)\le1.
\]
Hence \(\det S\ge d^d\det C\), with equality only if \(a=c\) and \(S=dC\). This proves least intrinsic volume and uniqueness without restricting competitors to symmetric ellipsoids.

**4. Euclidean ball, volume, and dimensional limit.** Each vertex has centered squared Euclidean norm \(2(1-1/N)=d/N\). A containing ball must have squared radius at least the contact-mass average of squared distances from its center, which equals \(d/N\) plus the squared displacement from \(c\). Thus \(\mathcal B_{r,s}\) is the unique minimum containing ball. Its shape is \((d/N)I_d\); the ellipsoid shape is \(dC\), giving volume ratio
\[
\left[N^{d}\det C\right]^{1/2}
=\left[\frac{r(r-2+rp)(1-p)}{(r-1)^2}\right]^{(r-1)/2}
(1-p^2)^{r(s-1)/2}.
\]
For fixed \(r\ge3\), the positive root equation gives \(p\sim(r-1)/[r(r-2)s]\), hence \(s p^2\to0\); the limit follows. The previously established balanced bipartite parameter \(p_{2,s}=2/(1+\sqrt{16s-7})\) instead has \(p_{2,s}\sim1/(2\sqrt s)\). Substituting it into the same determinant expression with \(r=2\) gives the previously implied asymptotic ratio \(\sqrt2e^{-1/4}s^{-1/4}\to0\). This is a comparison, not a new bipartite theorem.

**5. When uniform vertex weights are optimal.** Uniform weighting over all displayed vertices would put total mass \(q=[1+(r-1)s]^{-1}\) on the diagonal orbit. Direct substitution into the strictly decreasing contact equation yields
\[
F(q)=\frac{2(s-2)(s-1)(rs-s+1)}{s(r-1)(rs-2s+2)(rs-s+2)}.
\]
The denominator is positive; therefore \(F(q)=0\) precisely at \(s=2\), and \(F(q)>0\) otherwise. Since \(F(p)=0\) and \(F\) decreases strictly, this proves \(p=q\) exactly when \(s=2\), and \(p>q\) for \(s>2\).

## Verification
The standalone `checks/check_pq_lowner.py` reconstructs the allowed ordered-pair vertices in all 25 parameter cases \(3\le r\le7\), \(2\le s\le6\). It checks all vertex probabilities, means, covariance entries, the four spectrum blocks, every boundary contact, the Euclidean-ball radius and the ellipsoid-to-ball ratio numerically with displayed tight tolerances. SymPy separately checks the exact rational identities used to clear the contact equation and the uniform-weight threshold formula. The checker passed with the final line `BALANCED_MULTIPARTITE_PQ_LOEWNER_PASS cases= 25`. Run `OPENBLAS_NUM_THREADS=1 python checks/check_pq_lowner.py` with Python 3, NumPy and SymPy. These computations are corroborative; the all-parameter proof is Steps 1–5.

## Relationship to prior work
Ohsugi and Tsuchiya [1] introduced the PQ-type realization above and proved normalized-volume and \(h^*\)-polynomial formulas for complete multipartite graphs. Those lattice invariants do not determine the intrinsic Euclidean enclosing ellipsoid, contact design or limiting volume ratio. An earlier exact Löwner theorem [2] fully covers **balanced bipartite** instances \(K_{s,s}\), and its all-contact covariance method is foundational to this calculation. The present result explicitly excludes that case and proves a distinct \(r\ge3\) theorem, including a positive limiting ellipsoid-to-ball ratio versus the bipartite zero limit. The published metric-projection theorem [3] for arbitrary multipartite PQ polytopes classifies nearest points of missing product vertices; it does not assert or imply a minimum-volume enclosing ellipsoid. The split-graph uniform-vertex covariance study [4] computes a different graph's inertia under **fixed uniform weights**, rather than optimal design weights. The star-graph enclosing-ellipsoid result [5] has unequal multipartition sizes and a four-leaf contact-screening threshold, absent here. All relevant statements have been compared by domain, metric and logical implication; the general covariance optimality method itself is classical and not claimed new.

## Limitations
The result requires equal class sizes and at least three classes, and does not classify arbitrary unbalanced multipartite graphs or general PQ polytopes. The Euclidean volume ratios depend on the chosen standard-coordinate realization, though the optimal-ellipsoid statement is affine equivariant. The asymptotic is for **fixed** \(r\ge3\) with \(s\to\infty\), not simultaneous arbitrary growth of both parameters. Historical priority is provisional: a yet-unindexed general optimal-design formula could subsume this specialization. Finite numeric checks do not constitute infinite-dimensional certification. Independent mathematical audit has not been performed.

## References
[1] H. Ohsugi and A. Tsuchiya, *PQ-type adjacency polytopes of join graphs*, arXiv:2103.15045v1 (first posted 2021-03-28), *Discrete & Computational Geometry* 70 (2023), 214–235, doi:10.1007/s00454-022-00447-z. https://arxiv.org/abs/2103.15045

[2] *The exact Löwner ellipsoid of balanced complete-bipartite PQ-type adjacency polytopes* (2026-10-11), complete proof: https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-the-exact-l-wner-ellipsoid-of-balanced-complete-bipartite-pq-typ--eed12b121d5b/RESULT.md

[3] *Barycentric projection simplices and exact deep-hole shells of multipartite PQ adjacency polytopes* (2026-11-17), complete proof: https://github.com/published-finding corpus/2026/blob/main/2026/11/17/SCOPE-barycentric-projection-simplices-and-exact-deep-hole-shells-of-m--189d12c21cc0/RESULT.md

[4] *Reentrant least-variance eigenspaces of complete-split PQ adjacency polytopes* (2026-11-08), complete proof: https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-reentrant-least-variance-eigenspaces-of-complete-split-pq-adjace--9821a1c92d29/RESULT.md

[5] *A four-leaf contact transition in Löwner ellipsoids of star PQ-adjacency polytopes* (2026-11-08), complete proof: https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-four-leaf-contact-transition-in-l-wner-ellipsoids-of-star-pq-a--625d9f71dd97/RESULT.md
