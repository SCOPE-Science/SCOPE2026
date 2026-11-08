# Sharp convexification thresholds for all cross-polytope skeleta

## Finding

Let \(d\ge2\) and \(1\le s\le d\) be integers. Write
\[
C_d=\{x\in\mathbb R^d:\|x\|_1\le1\},\qquad
A_{d,s}=\{x\in\mathbb R^d:\|x\|_1=1,\ |\operatorname{supp}(x)|\le s\}.
\]
The set \(A_{d,s}\) is the closed \((s-1)\)-skeleton of the regular cross-polytope \(C_d\). Define its relative finite-convexification index by
\[
c(A_{d,s};C_d)=\inf\{\lambda\ge0:A_{d,s}+\lambda C_d\text{ is convex}\}.
\]

**Theorem (sharp complete skeleton phase diagram).** For every such \(d,s\) and \(\lambda\ge0\),
\[
\boxed{\quad A_{d,s}+\lambda C_d=(1+\lambda)C_d
\ \Longleftrightarrow\ 
\lambda\ge \max\left\{1,\frac ds-1\right\}.\quad}
\]
Consequently,
\[
\boxed{c(A_{d,s};C_d)=\max\left\{1,\frac ds-1\right\}.}
\]
The Minkowski sum is nonconvex below the displayed threshold. The threshold is \(d-1\) for vertices alone and is identically \(1\) from skeleton rank \(s\ge\lceil d/2\rceil\) onward. These identities extend to all invertible affine images of \(C_d\) and its corresponding skeleta.

A more precise statement, also proved below, gives the exact distance from an arbitrary \(x\in\mathbb R^d\) to the skeleton in the \(\ell_1\) norm. If \(t_1\ge\cdots\ge t_d\) is the descending rearrangement of \((|x_1|,\ldots,|x_d|)\), then
\[
\boxed{\operatorname{dist}_{\ell_1}(x,A_{d,s})
=\|x\|_1+1-2\min\left\{1,\sum_{j=1}^{s}t_j\right\}.}
\]

## Assumptions and scope

Every face of the cross-polytope uses a subset of the signed coordinate vertices without an antipodal pair. Thus the union of all faces of dimension at most \(s-1\), including their boundaries, consists exactly of the vectors with \(\ell_1\) norm one and at most \(s\) nonzero coordinates. This convention includes \(s=1\) (vertices only) and \(s=d\) (the full boundary). For the Minkowski sum, \(\lambda C_d\) is the full scaled convex body, not the scaled skeleton and not another copy of the nonconvex set.

For any compact \(A\) with \(\operatorname{conv}(A)=C_d\), the Minkowski sum \(A+\lambda C_d\) is convex if and only if it is exactly \((1+\lambda)C_d\): the inclusion \(A+\lambda C_d\subseteq(1+\lambda)C_d\) holds, and the convex hull of the left side is \((1+\lambda)C_d\). This observation makes the displayed set equality equivalent to the stated convexification index.

## Proof

**1. Exact nearest-skeleton formula.** Fix an arbitrary \(x\in\mathbb R^d\), and put \(q=\|x\|_1\). For a nonempty support \(I\subseteq\{1,\ldots,d\}\) with \(|I|\le s\), consider those \(y\in A_{d,s}\) supported in \(I\). A closest such vector can be chosen with each nonzero coordinate having the sign of the corresponding coordinate of \(x\) (an arbitrary sign is allowed when \(x_i=0\)). Let \(a_i=|x_i|\), \(b_i=|y_i|\), \(t_I=\sum_{i\in I}a_i\), and \(\sum_{i\in I}b_i=1\). The sum of absolute errors off \(I\) is \(q-t_I\). Within \(I\), the minimum possible error is exactly \(|t_I-1|\): the triangle inequality gives this lower bound, and it is attained by decreasing some \(a_i\) when \(t_I\ge1\) or increasing some \(a_i\) when \(t_I<1\), maintaining nonnegativity and total mass one. Therefore the minimum over this face is
\[
q-t_I+|t_I-1|=q+1-2\min\{1,t_I\}.
\]
Minimizing over all supports chooses the \(s\) largest coordinate magnitudes and gives the claimed exact formula with \(T_s=\sum_{j\le s}t_j\).

**2. The two necessary obstructions.** Since \(\operatorname{dist}_{\ell_1}(0,A_{d,s})=1\), the origin is absent from \(A_{d,s}+\lambda C_d\) whenever \(\lambda<1\), despite lying in \((1+\lambda)C_d\).

If instead \(\lambda<d/s-1\), choose the balanced boundary point
\[
x_\lambda=\frac{1+\lambda}{d}(1,\ldots,1).
\]
It belongs to \((1+\lambda)C_d\), and its top-\(s\) coordinate sum is \(s(1+\lambda)/d<1\). The distance formula yields
\[
\operatorname{dist}_{\ell_1}(x_\lambda,A_{d,s})
=(1+\lambda)+1-\frac{2s(1+\lambda)}d
> (1+\lambda)-1=\lambda.
\]
Thus \(x_\lambda\notin A_{d,s}+\lambda C_d\). Neither of the obstructions depends on a limiting or genericity assumption, so they cover every subcritical real parameter.

**3. Sufficiency including the endpoint.** Assume \(\lambda\ge L_{d,s}:=\max\{1,d/s-1\}\). Take any \(x\in(1+\lambda)C_d\) and put \(q=\|x\|_1\), so \(0\le q\le1+\lambda\). The sum of the largest \(s\) magnitudes obeys \(T_s\ge(s/d)q\). Hence
\[
\operatorname{dist}_{\ell_1}(x,A_{d,s})
\le q+1-2\min\left\{1,\frac{s}{d}q\right\}.
\]
For \(0\le q\le d/s\), the right-hand expression equals \(1+(1-2s/d)q\); as a linear function it is at most the larger of its endpoint values \(1\) and \(d/s-1\), both no greater than \(\lambda\). For \(q\ge d/s\), it equals \(q-1\le\lambda\). Thus every such \(x\) is within \(\ell_1\) distance \(\lambda\) of \(A_{d,s}\); compactness supplies an actual nearest point. Hence \(x\in A_{d,s}+\lambda C_d\). The reverse inclusion follows from the triangle inequality. This proves equality at and above the sharp threshold.

**4. Affine invariance.** For any invertible linear map \(T\) and translation vector \(b\), put \(F(x)=Tx+b\). Then \(F(A_{d,s})+\lambda F(C_d)=T(A_{d,s}+\lambda C_d)+(1+\lambda)b\). This identity is convex exactly when the original Minkowski sum is convex, and equality with \((1+\lambda)F(C_d)\) is equivalent to equality with \((1+\lambda)C_d\). Thus the same index applies to every affine cross-polytope with the corresponding skeleton.

## Verification

The accompanying standalone `verify_cross_skeleton.py` uses exact rational arithmetic and no external packages. For \(d\) from \(2\) through \(7\) and all allowable \(s\), it independently enumerates every coordinate support to calculate the minimum face-wise distance, checks the rearranged-coordinate distance identity, verifies explicit rational subcritical holes, and tests points throughout the supercritical body at the exact threshold. It performs 11,529 supplementary exact assertions. Running `python verify_cross_skeleton.py` prints `CROSS_SKELETON_EXACT_OK` when they pass. These finite checks do not prove the universally quantified theorem; the proof above supplies that conclusion.

## Relationship to prior work

Mark Meyer's *Finite convexification by Minkowski summation* (arXiv:2610.26744, first posted 2026-10-19) formulates precisely the general problem of when \(A+\lambda K\) becomes convex and proves characterizations through exposed-set covering radii. It supplies the direct conceptual setting, but the theorem above supplies a numerical sharp index and a complete skeleton-rank phase diagram for a particular nonconvex geometric family; the exposed-set characterization alone does not state the displayed constant without a further exact computation.

The 2018 survey by Fradelizi, Madiman, Marsiglietti and Zvavitch concerns convexification under repeated Minkowski averages, a different operation. *Vertex generated polytopes* by Artstein-Avidan, Falah and Slomka concerns sums involving a polytope and its vertex set, but its accessible abstract does not yield the full sharp threshold for every cross-polytope skeleton. A publicly available separate result titled *Sharp finite convexification thresholds for every skeleton of a simplex* proves an integer threshold for **equal-weight sums of copies of simplex skeleta**. Its complete result and proof were inspected; those hypotheses and the claimed conclusion differ from the present continuous addition of the full cross-polytope. There is no reduction supplied by that result from its simplex barycentric splitting to this sharp cross-polytope covering criterion.

## Limitations

The result applies to the entire face skeleton of cross-polytopes and their invertible affine images, not arbitrary centrally symmetric polytopes or arbitrary sparse subcomplexes. It does not characterize sums of several copies of the nonconvex skeleton or Euclidean-ball convexifiers. Although the exact constant and its all-rank classification were not found in the searched relevant records and material examined, independent historical priority remains unverified, particularly for possible equivalent statements in sparse \(\ell_1\) approximation and geometric covering literature. The computational checks supplement rather than independently certify the all-dimensional proof.

## References

1. Mark Meyer, *Finite convexification by Minkowski summation*, arXiv:2610.26744v1, first posted 2026-10-19. https://arxiv.org/abs/2610.26744 .
2. Matthieu Fradelizi, Mokshay Madiman, Arnaud Marsiglietti, Artem Zvavitch, *The convexification effect of Minkowski summation*, arXiv:1704.05486, 2018 survey. https://arxiv.org/abs/1704.05486 .
3. Shiri Artstein-Avidan, Tomer Falah, Boaz Slomka, *Vertex generated polytopes*, arXiv:2407.20604, 2024. https://arxiv.org/abs/2407.20604 .
4. *Sharp finite convexification thresholds for every skeleton of a simplex*, publicly available research record (2026): https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-finite-convexification-thresholds-for-every-skeleton-of-a--92b027220722 .
