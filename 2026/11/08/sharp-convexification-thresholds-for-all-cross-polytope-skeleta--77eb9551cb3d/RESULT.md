# Exact convexification thresholds for the intermediate skeleta of a cross-polytope

## Finding

Let \(d\ge3\) and \(2\le s\le d-1\). Let \(C_d=\{x\in\mathbb R^d:\|x\|_1\le1\}\). Its closed \((s-1)\)-skeleton is
\[
A_{d,s}=\{y:\|y\|_1=1,\ |\operatorname{supp}y|\le s\}.
\]
If \(a_1\ge\cdots\ge a_d\) are the ordered coordinate magnitudes of \(x\), then
\[
\operatorname{dist}_{\ell_1}(x,A_{d,s})=\|x\|_1+1-2\min\left\{1,\sum_{i=1}^s a_i\right\}.
\]
For every real \(\lambda\ge0\),
\[
A_{d,s}+\lambda C_d \text{ is convex}
\quad\Longleftrightarrow\quad A_{d,s}+\lambda C_d=(1+\lambda)C_d
\quad\Longleftrightarrow\quad \lambda\ge\max\{1,d/s-1\}.
\]
Thus the exact convexification radius decreases with skeleton rank until it reaches the floor of one at \(s\ge\lceil d/2\rceil\). The set equality and the threshold hold for every invertible affine image of the pair \((A_{d,s},C_d)\).

## Assumptions and scope

The skeleton includes all faces of dimension at most \(s-1\) and their boundaries. Each face is spanned by a set of signed coordinate vertices with no antipodal pair; this gives the support description above. The summand is the entire scaled unit ball, not another skeleton. The endpoint \(s=1\) is known from the cross-polytope vertex result cited below; at \(s=d\) the elementary distance to the whole boundary is \(|\|x\|_1-1|\). Neither endpoint is claimed as a contribution here.

## Proof

Fix \(x\), set \(q=\|x\|_1\), and choose a nonempty allowed support \(I\) with \(|I|\le s\). The signs of a nearest vector on this support can be matched to those of \(x\), with either sign allowed at zero. Write \(t_I=\sum_{i\in I}|x_i|\). The error outside \(I\) is \(q-t_I\). Inside, the triangle inequality bounds the error below by \(|1-t_I|\), and this is attained by only increasing magnitudes if \(t_I<1\), or only decreasing them if \(t_I>1\), to bring the sum to one. Hence the optimal error on \(I\) is \(q+1-2\min(1,t_I)\). This is nonincreasing in \(t_I\), so taking the \(s\) largest magnitudes proves the distance formula.

The set \(A_{d,s}\) contains all vertices of \(C_d\). Thus the sum is contained in \((1+\lambda)C_d\), and its convex hull is exactly that body. Membership in the sum is equivalent to distance at most \(\lambda\), because the skeleton is compact. The origin is at distance one, so \(\lambda<1\) cannot give equality. If \(\lambda<d/s-1\), the point \(x=(1+\lambda)(1,\ldots,1)/d\) on the enlarged boundary has top-\(s\) magnitude sum \(s(1+\lambda)/d<1\) and therefore distance \((1+\lambda)+1-2s(1+\lambda)/d>\lambda\). This proves necessity.

Suppose \(\lambda\ge\max(1,d/s-1)\) and take \(q\le1+\lambda\). The sum of the largest \(s\) magnitudes is at least \(sq/d\), so the distance is bounded above by \(q+1-2\min(1,sq/d)\). For \(q\in[0,d/s]\) this is affine and bounded by the maximum of its endpoint values, \(1\) and \(d/s-1\). For \(q\ge d/s\) it equals \(q-1\le\lambda\). Every point of the enlarged body is thus covered, including at the threshold. If \(F(x)=Tx+b\) with \(T\) invertible, then \(F(A)+\lambda F(C)=T(A+\lambda C)+(1+\lambda)b\); this proves the affine assertion.

## Verification

The proof treats all admissible real parameters and dimensions. The accompanying `verify_cross_skeleton.py` is a supplementary exact-rational checker. It compares the sorted formula with a support enumeration using the fixed-support distance calculation, and samples obstructions and coverage for \(2\le d\le7\) (including endpoint controls outside the scope of the new claim). Its finite tests do not establish either the support-wise lemma or universal coverage.

## Relationship to prior work and limitations

The cross-polytope vertex case \(s=1\), including the exact distance formula with the maximum coordinate and the threshold \(d-1\), is already stated in [Complete volumetric convexification spline for cross-polytope vertices](https://github.com/Resultary/2026/tree/main/2026/11/1/SCOPE-complete-volumetric-convexification-spline-for-cross-polytope-ve--7c478cf9bf62). The intermediate-face calculation allows mass to be allocated over several coordinates; a test involving only the maximum coordinate does not characterize that distance. Computing the support optimum shows when the balanced boundary obstruction gives way to the origin. The formula concerns whole skeleta, not arbitrary selections of faces.

Meyer, [*Finite convexification by Minkowski summation*](https://arxiv.org/abs/2610.26744), gives general exposed-set criteria for finiteness of the relative index. Artstein-Avidan, Falah and Slomka, [*Vertex generated polytopes*](https://arxiv.org/abs/2407.20604), study the index for vertex sets. The analogous [result for products of simplices](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-central-witness-convexification-thresholds-for-every-skeleton-of--f2144e0cf323) concerns a different family: a cross-polytope in dimension at least three is not an affine product of simplices. These comparisons do not establish historical priority over all results on sparse \(\ell_1\) approximation or covering. No assertion is made for a different convexifying body, for sums of copies of the skeleton, or for non-affine equivalents.
