# Sharp Euclidean completion gap for transitive-tournament root polytopes

## Finding
For each integer \(n\ge 2\), let \(e_1,\ldots,e_n\) be the orthonormal coordinate basis in \(\mathbb R^n\) and define
\[
P_n=\operatorname{conv}\{e_i-e_j:1\le i<j\le n\},\qquad
S_n=\operatorname{conv}\{e_i-e_j:1\le i\ne j\le n\}.
\]
Thus \(P_n\) is the directed-edge polytope of the transitive tournament and \(S_n\) is the symmetric type-\(A\) root polytope. Distances are ambient Euclidean distances, equivalent to intrinsic distances in the common zero-sum hyperplane. Because \(P_n\subseteq S_n\), their Hausdorff distance is directed from \(S_n\) to \(P_n\).

The **exact squared Hausdorff distance** is
\[
\boxed{d_H(S_n,P_n)^2=\begin{cases}
8,&n=2,\\
\frac92,&n=3,\\
\frac{16}{5},&n=4,\\
2+\frac{12}{(n-3)(n-2)(n-1)},&n\ge5.
\end{cases}}
\]
For every \(n\ge2\), there is **exactly one farthest point**, namely the negative highest root \(x_n=e_n-e_1\). Its nearest point is also unique. For \(n\ge5\), writing \(m=n-2\) and \(c=6/[m(m^2-1)]\), that point is
\[
\boxed{q_n=\sum_{h=1}^{m-1}c\,h(m-h)(e_{h+1}-e_{h+2}).}
\]
All \(n-3\) displayed coefficients are strictly positive and sum to one. Hence the projection lies in the relative interior of the simplex spanned by the strictly internal simple roots, rather than on a vertex. For \(n=4\) it instead has the three-simple-root barycentric formula
\[
q_4=\tfrac15(e_1-e_2)+\tfrac35(e_2-e_3)+\tfrac15(e_3-e_4),
\]
while \(q_3=\tfrac12(e_1-e_3)\) and \(q_2=e_1-e_2\).

In particular, the gap decreases to \(\sqrt2\), and for \(n\ge5\) its squared excess above two is exactly \(12/[(n-3)(n-2)(n-1)]\). The change from support involving the exterior simple roots at \(n=4\) to exclusively internal simple roots at \(n=5\) is sharp.

## Assumptions and scope
The Euclidean realization is fixed: all coordinates are the usual orthonormal ones, with no additional normalization of roots. The displayed \(P_n\) **does not contain the origin** for \(n\ge2\). It is not the often-studied origin-adjoined positive-root polytope \(\operatorname{conv}(P_n\cup\{0\})\). Every statement concerns the whole continuous convex bodies, not just the two finite root sets or their graph distances. When \(n=2\), \(P_2\) is a singleton and the same distance definition applies. The expression involving \(m\) is used only for \(n\ge5\).

## Proof
**1. A minimal-norm point of any ordered positive-root family.** Let \(m\ge2\) and let \(a_1<\cdots<a_m\) be distinct coordinate indices. Write \(R=\operatorname{conv}\{e_{a_h}-e_{a_k}:1\le h<k\le m\}\), set
\[
c_m=\frac6{m(m^2-1)},\quad s_m=\frac{12}{m(m^2-1)},\quad
u=\sum_{h=1}^{m}c_m(m+1-2h)e_{a_h}.
\]
The telescoping identity
\[
\nu=\sum_{h=1}^{m-1}c_mh(m-h)(e_{a_h}-e_{a_{h+1}})
\]
expresses \(\nu\) as a convex combination because \(\sum_{h=1}^{m-1}h(m-h)=m(m^2-1)/6\). Directly,
\[
\|\nu\|^2=s_m,\qquad
\langle\nu,e_{a_h}-e_{a_k}\rangle=(k-h)s_m\ge s_m=\langle\nu,\nu\rangle.
\]
Therefore \(\langle\nu,z-\nu\rangle\ge0\) for each vertex \(z\) of \(R\), hence for all \(z\in R\). Expanding \(\|z\|^2=\|\nu\|^2+2\langle\nu,z-\nu\rangle+\|z-\nu\|^2\) proves that \(\nu\) is the unique point of \(R\) closest to the origin. This algebraic point is also identifiable from the previously known minimum-sphere center of the positive-root polytope; the novelty asserted below is its different use in the full-versus-directed Hausdorff problem.

**2. The all-dimensional upper bound.** Assume \(n\ge5\), put \(m=n-2\), and take a negative root \(x=e_j-e_i\), where \(1\le i<j\le n\). Apply step 1 to the \(m\) coordinate indices other than \(i,j\), obtaining \(\nu_{ij}\in P_n\), whose support is disjoint from that of \(x\). Thus
\[
\operatorname{dist}(x,P_n)^2\le\|x-\nu_{ij}\|^2
=2+s_m=2+\frac{12}{(n-3)(n-2)(n-1)}.
\]
Every positive root belongs to \(P_n\), and every point of \(S_n\) is a convex combination of positive and negative roots. Convexity of distance to a closed convex set therefore gives the same upper bound for \(d_H(S_n,P_n)^2\).

**3. Sharp projection at the negative highest root.** Take \(x=e_n-e_1\) and the point \(q=q_n\) from the finding. Its only nonzero coordinates are
\[
q_{h+1}=c_m(m+1-2h),\qquad1\le h\le m;
\quad q_1=q_n=0,
\]
and \(\langle x,q\rangle=0\), \(\|q\|^2=s_m=2c_m\). The Euclidean projection criterion for a convex hull is
\[
\langle x-q,z-q\rangle\le0\quad\text{for every root }z=e_a-e_b\text{ with }a<b.
\]
Equivalently, \(\langle q-x,z\rangle\ge s_m\). If \(2\le a<b\le n-1\), then \(\langle q-x,z\rangle=(b-a)s_m\ge s_m\). If \(a=1<b<n\) or \(1<a<b=n\), its minimum over the relevant roots is \(1-c_m(m-1)\). This is at least \(s_m=2c_m\) precisely when
\[
1\ge c_m(m+1)=\frac6{m(m-1)},
\]
which holds for every \(m\ge3\). For the remaining root \(e_1-e_n\), the inner product is \(2\ge s_m\). Hence the projection criterion holds for **all** vertices of \(P_n\), proving that \(q\) is the unique metric projection of \(x\). Its squared distance equals \(2+s_m\) and attains the upper bound in step 2.

**4. Uniqueness of the farthest point.** Let \(x=e_j-e_i\ne e_n-e_1\) be any other negative root. Its complementary-coordinate witness \(\nu_{ij}\) in step 2 has coordinates bounded in magnitude by
\[
c_m(m-1)=\frac6{m(m+1)}\le\frac12.
\]
If \(j<n\), take the positive root \(z=e_j-e_{j+1}\); otherwise \(i>1\) and take \(z=e_{i-1}-e_i\). In both cases \(\langle x,z\rangle=1\), \(\langle x,\nu_{ij}\rangle=0\), and \(\langle\nu_{ij},z\rangle\le1/2\). Therefore
\[
\langle x-\nu_{ij},z-\nu_{ij}\rangle
=1-\langle\nu_{ij},z\rangle+s_m>0.
\]
Moving a sufficiently small positive distance from \(\nu_{ij}\) toward \(z\) strictly **reduces** the squared distance to \(x\). Thus every such root has distance strictly smaller than \(\sqrt{2+s_m}\). The positive roots have distance zero, so \(e_n-e_1\) is the sole farthest vertex of \(S_n\). Finally, a convex combination involving any other vertex has strictly smaller distance by convexity, proving uniqueness among **all points** of \(S_n\).

**5. Exceptional dimensions.** For \(n=2\), \(S_2\) is the segment with endpoints \(\pm(e_1-e_2)\) and \(P_2\) is its positive endpoint, giving squared distance \(8\). For \(n=3\), the root \(e_3-e_1\) projects to \(\tfrac12[(e_1-e_2)+(e_2-e_3)]\), with squared distance \(9/2\). The projection criterion is immediate from its two supporting roots; each other negative root is within squared distance two of a positive root. For \(n=4\), at \(x=e_4-e_1\), the proposed \(q_4\) gives residual
\[
x-q_4=(-6,-2,2,6)/5.
\]
Its scalar product with each of the three consecutive simple roots equals \(-4/5\), while the other three positive roots have scalar products \(-8/5,-8/5,-12/5\). Hence the projection criterion is satisfied, since \(\langle x-q_4,q_4\rangle=-4/5\), and \(\|x-q_4\|^2=16/5\). For the five remaining negative roots \(e_j-e_i\), in index order \((i,j)=(1,2),(1,3),(2,3),(2,4),(3,4)\), explicit positive-root convex combinations give squared-distance **upper bounds** \(4/3,11/6,1,11/6,4/3\), all strictly less than \(16/5\). These combinations, displayed and checked in the standalone exact verifier, complete the exceptional case. Convexity again proves uniqueness on the entire \(S_4\).

## Verification
The included standard-library script `verify.py` checks all rational convex coefficients, the exact minimum-norm identity, all necessary projection inequalities, and the strict-witness inequalities for every negative root in dimensions \(5\) through \(16\). It checks the low-dimensional certificates for dimensions \(2,3,4\) and verifies the highest-root projection inequalities again at dimensions \(30,61,103\). The result was `POSITIVE_ROOT_HAUSDORFF_PASS small=2,3,4 all_negative_certificates=5..16 large_highest_KKT=30,61,103`.

A separate optional SciPy-based test `verify_qp.py` independently solved 220 constrained quadratic programs for all negative roots in dimensions \(2\) through \(11\), recovering the claimed unique Hausdorff extremizer and squared distances to numerical precision. Its result was `INDEPENDENT_QP_PASS negative_roots=220 dimensions=2..11`. The exact all-dimensional argument is in the proof above; neither finite test is used to assert an infinite statement.

## Relationship to prior work
Numata, Takahashi and Tamaki (2022, arXiv:2203.14521) define directed-edge polytopes in the present realization and classify facets and faces, but not their Hausdorff distances to bidirected completions. Setiabrata (2020, arXiv:2001.05191) studies the faces of the **origin-adjoined** positive-root polytope; adding the origin changes the nearest-point question and cannot be silently substituted. Ehrenborg, Hetyei and Readdy (2019, arXiv:1901.07113) classify triangulations of the full root polytope, not its Euclidean distance from a directed subpolytope. Gutekunst, Mészáros and Petersen (2019, arXiv:1903.06595) investigate root cones, resonance chambers and triangulations.

Earlier public same-object mathematical results give the minimum enclosing Euclidean sphere, its parabolic center, and the complete one-skeleton of the transitive-tournament positive-root polytope. The parabolic coefficients used in step 1 are therefore **not claimed as novel in isolation**. Neither a minimum enclosing sphere nor a skeleton determines the projection of the opposite highest root or the full Hausdorff extremum. A separate previous result gives a Poisson law for **random directional width loss** of this pair; that stochastic average-direction invariant does not imply the present worst-case point-to-set distance. The exact distance, the uniqueness across the continuous full polytope, and the exceptional transition at \(n=5\) are the asserted claim.

## Limitations
This is an exact metric result for one canonical orientation and the standard Euclidean coordinates, not an arbitrary tournament, a weighted root system, or an arbitrary affine image. The asymptotic constant applies only to this embedding. The origin-adjoined model is a different polytope. The classification of all nearest projections of **every** negative root is not claimed; only the unique global maximizer and its projection are classified. Earlier equivalent work under another geometric formulation remains a possible historical-priority risk; no independent audit is claimed.

## References
1. R. Ehrenborg, G. Hetyei and M. Readdy, *Classification of Uniform Flag Triangulations of the Boundary of the Full Root Polytope of Type A*, arXiv:1901.07113v1 (2019-01-21), https://arxiv.org/abs/1901.07113.
2. S. C. Gutekunst, K. Mészáros and T. K. Petersen, *Root Cones and the Resonance Arrangement*, arXiv:1903.06595v1 (2019-03-15), https://arxiv.org/abs/1903.06595.
3. L. Setiabrata, *Faces of Root Polytopes*, arXiv:2001.05191v1 (2020-01-15), https://arxiv.org/abs/2001.05191.
4. Y. Numata, Y. Takahashi and D. Tamaki, *Faces of Directed Edge Polytopes*, arXiv:2203.14521v1 (2022-03-28), https://arxiv.org/abs/2203.14521.
5. *Simple roots control the minimum sphere of transitive-tournament directed edge polytopes* (2026), publicly available mathematical finding.
6. *Exact 1-skeleton and simple-vertex exhaustion of transitive-tournament root polytopes* (2026), publicly available mathematical finding.
7. *Poisson width loss and macroscopic exposed roots of transitive-tournament polytopes* (2026), publicly available mathematical finding.
