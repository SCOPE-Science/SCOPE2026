# Exact VC-shattering polynomial of fixed-norm circles over odd finite fields

## Finding

Let \(q\ge3\) be any odd prime power, let \(t\in\mathbb F_q^\times\), and let \(X=\mathbb F_q^2\). Define \(Q(x_1,x_2)=x_1^2+x_2^2\), and consider the concept family of **all** fixed-norm circles
\[
\mathcal C_{q,t}=\{\{x\in X:Q(x-c)=t\}:c\in X\}.
\]
For \(k\ge0\), let \(s_k(q,t)\) be the number of unordered \(k\)-element supports shattered by this family, with \(s_0=1\). Write \(\chi\) for the quadratic character on \(\mathbb F_q\), with \(\chi(0)=0\), and put \(S=q-\chi(-1)\). Then the **entire** shattered-support polynomial is
\[
\boxed{\Phi_{q,t}(z)=1+q^2z+\frac{q^2S^2}{4}z^2+\frac{q^2S(S-2)(S-4)}6z^3.}
\]
Every higher coefficient is zero. The polynomial is independent of which nonzero field element \(t\) is chosen, even when \(t\) ranges between square and nonsquare classes.

Moreover, an unordered triple \(\{a,b,c\}\subset X\) is shattered **if and only if** the three points lie on a common circle of norm \(t\) and no pair is antipodal about that circle's center. The center, if it exists, is unique. In particular,
\[
\operatorname{VCdim}(\mathcal C_{q,t})=\begin{cases}2,&q\in\{3,5\},\\3,&q\ge7.\end{cases}
\]
The corresponding uniformly random-support probabilities are
\[
\Pr(\text{pair shattered})=\frac{S^2}{2(q^2-1)},\qquad
\Pr(\text{triple shattered})=\frac{S(S-2)(S-4)}{(q^2-1)(q^2-2)}.
\]
These tend respectively to \(1/2\) and \(0\), the latter with asymptotic order \(1/q\).

## Assumptions and scope

The base field has **odd characteristic** and order \(q\ge3\); it need not be a prime field. The norm parameter satisfies \(t\ne0\). Concepts are indicators of radius-\(t\) *equalities* in the quadratic form \(Q\), not Euclidean closed balls or variable-radius spheres. Every possible center is allowed. Counting concerns unordered distinct supports in the full ambient \(X\), not an arbitrary restricted subset \(E\subset X\). No additional empty or full concepts are adjoined.

## Proof

**1. Size and rigidity of a circle.** For any nonzero \(t\), the circle \(C_t=\{x:Q(x)=t\}\) has size \(S=q-\chi(-1)\). Indeed the number of solutions to \(z^2=x^2-t\) is \(q-1\), because \((x-z)(x+z)=t\) and each nonzero choice of \(x-z\) uniquely determines \(x+z\). Hence \(\sum_x\chi(x^2-t)=-1\) and
\[
|C_t|=q+\sum_x\chi(t-x^2)=q-\chi(-1).
\]
The involution \(x\mapsto-x\) partitions \(C_t\) into exactly \(S/2\) antipodal pairs (none has a fixed point).

Two different circles of the same nonzero norm have at most two common points. Subtracting their equations puts any intersection on a nontrivial affine line. A line is not contained in \(Q(x)=t\): if \(Q(u+\lambda v)\) were the constant \(t\) for nonzero \(v\), its quadratic and linear coefficients would force \(Q(v)=0\), \(u\cdot v=0\); in dimension two the orthogonal complement of an isotropic nonzero \(v\) equals its span, so \(Q(u)=0\ne t\). Thus the line meets the conic in at most two points. In particular, three distinct points on one circle are noncollinear and determine their center uniquely.

**2. All centers through a given pair.** Translate a common center to the origin. For two different points \(a,b\in C_t\), both \(0\) and \(a+b\) are centers of norm-\(t\) circles passing through \(a,b\). If \(a+b\ne0\), these are distinct, and the two-circle intersection bound in the *center variable* shows that there are exactly two. If \(b=-a\), any center \(y\) through both satisfies \(y\cdot a=0\) and \(Q(y)=0\). As \(Q(a)=t\ne0\), the one-dimensional orthogonal complement of \(a\) is anisotropic, so \(y=0\); there is exactly one center. Hence a pair is covered by either one circle (antipodal about its unique center), two circles, or none.

**3. Singletons and pairs.** Every point lies on exactly \(S\ge4\) circles, fewer than the \(q^2\) available circles, so every singleton is shattered. A pair sharing a circle is also shattered: each endpoint lies on \(S\) circles, at most two of which also contain the other endpoint, giving both singleton traces. The empty trace exists because \(q^2>2S\) for every odd prime power \(q\ge3\). Conversely a shattered pair must have a common circle. There are \(q^2\binom S2\) incidences of a center and a pair lying on its circle. Exactly \(q^2S/2\) distinct covered pairs have a unique center (one antipodal pair for each center), and all other covered pairs have two centers. Therefore
\[
s_2=\frac{q^2S}{2}+\frac{q^2\binom S2-q^2S/2}{2}=\frac{q^2S^2}{4}.
\]
Also \(s_1=q^2\).

**4. Characterization and counting of shattered triples.** If a triple is shattered, some circle contains it. After moving that center to the origin, any antipodal pair \(a,-a\) has the origin as its only covering center and cannot realize the trace consisting of that pair but not the third point. Thus a shattered triple cannot contain antipodes.

Conversely let \(a,b,c\in C_t\) be distinct and pairwise nonantipodal. The origin realizes the full trace. The three distinct nonzero centers \(a+b\), \(a+c\), \(b+c\) realize the corresponding exact pair traces: they cover their designated pair, and a circle through all three points would have to be the origin-centered circle by uniqueness. For an exact singleton trace at \(a\), there are \(S\) possible centers through \(a\). Exactly the three centers \(0,a+b,a+c\) also cover either \(b\) or \(c\), leaving \(S-3\ge1\) witnesses; analogously for \(b,c\). Finally the empty trace exists because \(q^2>3S\) for \(q\ge7\). For \(q=3\) or \(q=5\), one has \(S=4\) and no three distinct points of a circle avoid antipodal pairs, so this exceptional empty-trace issue never arises.

Each circle contains \(S/2\) antipodal pairs. A nonantipodal unordered triple is obtained by choosing three different such pairs and one element from each, giving \(8\binom{S/2}3=S(S-2)(S-4)/6\) choices. Each such triple belongs to a unique circle, so
\[
s_3=q^2\,8\binom{S/2}3=\frac{q^2S(S-2)(S-4)}6.
\]

**5. No larger supports.** A shattered support of size at least four would have a three-point subset \(T\) and two distinct centers realizing \(T\) and \(T\) together with a fourth support point. This would put the same three distinct points on two different circles, contradicting step 1. Thus \(s_k=0\) for \(k\ge4\), completing the polynomial and the VC-dimension classification. Dividing \(s_2\) and \(s_3\) by \(\binom{q^2}2\) and \(\binom{q^2}3\) yields the stated probabilities.

## Verification

The accompanying `verify_circle.py` constructs actual finite fields and directly tests all Boolean traces. It verifies all pair-displacement types and every triple contained in a fixed norm circle, as well as the predicted antipodal criterion, for the following fifteen cases: both \(t=1,2\) over each prime field of orders \(3,5,7,11,13,17\), and \(t=1\) over fields of orders \(9,25,27\). Because of translation invariance, these tests cover all pairs and all triples that could possibly be shattered in each selected field. The program prints `ALL_FINITE_FIELD_CIRCLE_TRACES_PASS 15 fields/radii` upon success. Such finite checks corroborate but do not prove the theorem for arbitrary prime powers; the proof above is uniform.

## Relationship to prior work

Fitzpatrick, Iosevich, McDonald and Wyman (2021) study exactly the fixed-nonzero-norm circle classifiers over finite planes and prove existence of shattered triples for sufficiently large restricted sets. Their ten-page preprint gives an explicit witness construction and the general bound of three, not an exact classification of **all** shattered supports or coefficientwise counts on the full plane. The present theorem counts all such supports at every odd prime-power field order and determines the small-field exceptions. Ascoli and collaborators (2022) treat a related multi-distance classifier and thresholds for large subsets, not this complete fixed-radius enumerator. Pham, Senger, Tait and Nguyen (2023) give general pseudorandom-graph VC bounds, not the exact conic support census. These cited results do not imply the coefficient formulas without the additional geometric classification and counting carried out here.

## Limitations

The result is limited to odd characteristic, the nonzero quadratic norm \(Q(x)=x_1^2+x_2^2\), the full finite plane, and a fixed norm parameter. Other quadratic-form ranks, characteristic two, variable radii, and restrictions of center and query domains are not asserted. The literature comparison supports originality within inspected sources, not a comprehensive historical-priority certificate. Independent scientific validation has not been performed.

## References

1. D. Fitzpatrick, A. Iosevich, B. McDonald and E. L. Wyman, *The VC-dimension and point configurations in* \(\mathbb F_q^2\), arXiv:2108.13231 (first public version 2021-08-30). https://arxiv.org/abs/2108.13231
2. R. Ascoli et al., *VC-Dimension and Distance Chains in* \(\mathbb F_q^d\), arXiv:2210.03058 (first public version 2022-10-06). https://arxiv.org/abs/2210.03058
3. T. Pham, S. Senger, M. Tait and N. Thu-Huyen, *VC-dimension and pseudo-random graphs*, arXiv:2303.07878 (first public version 2023-03-14). https://arxiv.org/abs/2303.07878
