# Every central hyperplane section of a box that is a zonoid

## Finding

**Complete criterion.** For any integer \(d\ge2\), positive numbers \(s_1,\ldots,s_d\), and nonzero \(u\in\mathbb R^d\), define the rectangular box and central section by
\[
Q=\prod_{i=1}^d[-s_i,s_i],\qquad H=\{x:\langle u,x\rangle=0\},\qquad K=Q\cap H.
\]
Let \(I=\{i:u_i\ne0\}\), \(m=|I|\), and \(a_i=s_i|u_i|\) for \(i\in I\). Then the following are equivalent:

1. \(K\) is a zonoid (allowing a translate of a centrally symmetric zonoid).
2. \(K\) is a finite Minkowski sum of segments, i.e., a zonotope.
3. Either \(m\le3\), or there is an active coordinate \(j\in I\) such that
\[
a_j\ge\sum_{i\in I\setminus\{j\}}a_i.
\]

If the dominance inequality holds, the section is an affine \((d-1)\)-cube. If \(m\le3\), it is a Cartesian product of a centrally symmetric polygon or segment and inactive coordinate intervals. If \(m\ge4\) and every active coefficient is strictly smaller than the sum of the others, **each active-coordinate facet of \(K\) fails central symmetry**, so \(K\) is not a zonoid. These assertions include equality, degenerate support, and all dimensions.

## Assumptions and scope

All half-lengths \(s_i\) are strictly positive; \(u\ne0\). The section lies in \(H\) with the induced affine dimension \(d-1\), since the origin is interior to \(Q\). A zonoid is a Hausdorff limit of Minkowski sums of line segments, possibly translated. It has centrally symmetric exposed faces. A zonotope is a *finite* Minkowski sum of line segments. An affine cube is an affine image of \([-1,1]^{d-1}\). No genericity or exclusion of coefficient equalities is assumed.

Independent reflections and diagonal rescalings reduce the problem to \([-1,1]^m\cap\{\sum_{i=1}^m a_ix_i=0\}\), times the cube from the \(d-m\) inactive coordinates. Such invertible affine transformations preserve zonoids, zonotopes and central symmetry.

## Proof

**Lemma (rigidity of noncentral box sections).** Let \(r\ge3\), \(b_1,\ldots,b_r>0\), \(S=\sum_{i=1}^rb_i\), and \(0<|t|<S\). The \((r-1)\)-dimensional polytope
\[
C_t=\{x\in[-1,1]^r:\textstyle\sum_i b_ix_i=t\}
\]
is centrally symmetric if and only if some \(j\) satisfies
\[
b_j\ge |t|+\sum_{i\ne j}b_i.
\]
In that case \(C_t\) is an affine \((r-1)\)-cube.

*Proof of lemma.* Reflection reduces to \(t>0\). Put \(\delta=(S-t)/2\), so \(0<\delta<S/2\), and make the invertible affine substitution \(y_i=b_i(1-x_i)/2\). It sends \(C_t\) onto
\[
T=\{y:\ 0\le y_i\le b_i,\quad\textstyle\sum_i y_i=\delta\}.
\]
If there is a dominant \(j\), then \(b_j\ge t+\sum_{i\ne j}b_i\). Arbitrarily assigning all remaining \(x_i\in[-1,1]\) and solving for \(x_j\) gives \(|x_j|\le1\). Thus \(C_t\) is an affine cube and is centrally symmetric.

Conversely, assume no such \(j\) exists, equivalently \(b_i<S-\delta\) for every \(i\). Then \(\sum_{k\ne i}b_k>\delta\); hence the minimum and maximum of coordinate \(y_i\) on \(T\) are respectively \(0\) and \(\min(b_i,\delta)\). If \(T\) were centrally symmetric about \(c\), the reflection of these extrema would require
\[
c_i=\frac12\min(b_i,\delta),\qquad \sum_i\min(b_i,\delta)=2\delta.\tag{*}
\]
But the final equality is impossible. If every \(b_i\le\delta\), the left side equals \(S>2\delta\). Otherwise choose \(j\) with \(b_j>\delta\). As \(b_j<S-\delta\), the other positive coefficients sum to more than \(\delta\). Because \(r\ge3\), there are at least two other positive coefficients, and
\[
\sum_{i\ne j}\min(b_i,\delta)>\delta.
\]
Indeed, if one of them exceeds \(\delta\), it contributes \(\delta\) plus a strictly positive contribution from another; if none does, truncation does not change their sum. Adding \(\min(b_j,\delta)=\delta\) contradicts (*). This proves the lemma for \(t>0\), and \(C_{-t}=-C_t\) handles \(t<0\). \(\square\)

*Proof of the criterion.* Normalize active coordinates as stated above. If \(m\le3\), the central active section is either a point, a line segment or a centrally symmetric polygon. Every centrally symmetric planar polygon is a sum of line segments. Taking its Cartesian product with the unused intervals remains a zonotope.

If some \(a_j\ge\sum_{i\ne j}a_i\), every choice of the other \(d-1\) normalized coordinates in \([-1,1]\) determines an admissible unique \(j\)-th coordinate. Consequently \(K\) is an affine \((d-1)\)-cube, hence a zonotope.

Finally suppose \(m\ge4\) and \(a_j<\sum_{k\ne j}a_k\) for all active \(j\). Fix any active coordinate \(x_i=1\) in the normalized model. The resulting proper exposed facet is
\[
F_i=\Bigl\{x_{\!I\setminus\{i\}}\in[-1,1]^{m-1}:\sum_{j\ne i}a_jx_j=-a_i\Bigr\}\times[-1,1]^{d-m}.
\]
It has relative dimension \(d-2\) because \(a_i<\sum_{j\ne i}a_j\). Apply the lemma with \(r=m-1\ge3\), \(t=-a_i\), and remaining coefficients \(b_j=a_j\). Its dominance condition would be \(a_j\ge a_i+\sum_{k\notin\{i,j\}}a_k\), contradicting the assumption. Thus its active factor is not centrally symmetric. Neither is \(F_i\), since projection of a centrally symmetric body must be centrally symmetric.

Every exposed face of a zonoid is centrally symmetric (indeed, up to translation it is another zonoid). Therefore \(K\) cannot be a zonoid. This completes all implications and the stronger assertion about facets. \(\square\)

## Verification

The standalone standard-library Python checker `check_box_sections.py` constructs vertices by solving one coordinate from the offset hyperplane and setting every other coordinate to a sign. All arithmetic uses exact rational numbers. It independently determines central symmetry by reflecting the complete vertex set about its vertex barycenter; it does **not** use the displayed truncated-sum proof to decide symmetry.

For \(r=3,4,5\), it exhausts coefficient tuples from \(\{1,2,3\}^r\) and each feasible nonzero integer offset with either sign. It additionally checks the decisive nondominant active facets for all central configurations of \(m=4,5,6\) and coefficient tuples from \(\{1,2,3\}^m\). In total there are 6,827 cases; all agree, including equality and genuinely nonsymmetric high-dimensional faces. The output is `ALL_DIMENSION_BOX_ZONOID_CHECKS_PASSED`.

The analytic proof is valid for all positive real coefficients and all dimensions. Finite checks are consistency tests, not infinite proofs.

## Relationship to prior work

Anantharaman (2019; open-access arXiv version 2023) asked when central cube sections are zonoids, proved selected four-dimensional zonoid/nonzonoid cases and explicitly reported no complete classification. The present criterion solves that question uniformly in all dimensions and for every rectangular box. The dimension-four specialization coincides with the previously obtained four-box criterion and is not claimed as new. What is established here beyond the dimension-four statement is the all-dimensional off-center section rigidity lemma and its use on every active-coordinate facet in every ambient dimension. The result does not follow simply from the classification of four-dimensional slices: the exposing facet in higher dimensions itself has larger dimension.

Shephard (1967) recorded the classical fact that zonotopes are characterized by central symmetry of their two-dimensional faces. Anantharaman recalls the necessary central symmetry of every zonoid face. The present proof uses this classical obstruction, not a new characterization of zonoids in general.

Ambrus (2021) studies extremal and stationary volume of central cube sections; Mathis and Meroni (2022) prove that *fiber bodies* of zonoids are zonoids. Critical volumes and fiber bodies are different from exact zonotopality of fixed central hyperplane slices; neither result implies the stated criterion.

## Limitations

This classification is restricted to **central hyperplane** sections of **rectangular boxes**, and their invertible affine equivalents. It does not classify general codimension-two sections, translated noncentral hyperplane sections, or sections of general zonotopes. Historical priority remains provisional: an equivalent statement in unindexed classical literature cannot be ruled out by searches. No independent audit has been performed.

## References

- R. Anantharaman, *Example of cube slices that are not zonoids*, Scientiae Mathematicae Japonicae 81 (2019), 315–326, DOI: 10.32219/isms.81.3_315 (available online 2019-05-10); full open-access version *A cube Slice that is not a Zonoid*, arXiv:2305.18351v2 (2023), sections 1–4.
- G. C. Shephard, *Polytopes with Centrally Symmetric Faces*, Canadian Journal of Mathematics 19 (1967), 1206–1213, DOI: 10.4153/CJM-1967-109-3.
- G. Ambrus, *Critical central sections of the cube*, arXiv:2107.14778 (2021).
- L. Mathis and C. Meroni, *Fiber Convex Bodies*, Discrete & Computational Geometry 70 (2023), 1451–1475, first publicly available 2022, DOI: 10.1007/s00454-022-00451-3.
