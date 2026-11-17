# An arithmetic deep-face resonance in balanced partition-matroid polytopes

## Finding

Fix integers \(r\ge3\), \(q\ge2\), and \(1\le c<q\). Partition \([rq]\) into \(r\) labelled classes \(B_1,\ldots,B_r\) of cardinality \(q\), and equip \(\mathbb R^{rq}\) with its standard Euclidean metric. Put
\[
H=\Delta(rc,rq)=\{x\in[0,1]^{rq}:\sum_i x_i=rc\},\qquad
P=\{x\in H:\sum_{i\in B_j}x_i=c\text{ for every }j\}
=\prod_{j=1}^r\Delta(c,B_j).
\]
The smaller set \(P\) is the base polytope of the direct sum of \(r\) uniform rank-\(c\) matroids, whereas \(H\) is the base polytope of a uniform rank-\(rc\) matroid. Write \(rc=aq+s\), where \(a=\lfloor rc/q\rfloor\) and \(0\le s<q\), and define
\[
F(k)=\begin{cases}
(c-k)^2/(q-k),&0\le k\le c,\\
(k-c)^2/k,&c\le k\le q.
\end{cases}
\]
The overlap at \(k=c\) is consistent. Then the exact Euclidean Hausdorff distance is
\[
\boxed{d_H(H,P)^2=\begin{cases}
aF(q)+(r-a)F(0),&s=0,\\
aF(q)+(r-a-1)F(0)+F(s),&1\le s<q.
\end{cases}}
\]

The entire farthest-point locus \(\{x\in H:d(x,P)=d_H(H,P)\}\) is as follows.

* If \(s=0\), it consists of exactly \(\binom r a\) vertices: their blocks have \(a\) complete-one blocks and \(r-a\) all-zero blocks.
* If \(0<s<q\) and \(s\ne c\), it consists of exactly \(r\binom{r-1}{a}\binom q s\) vertices: their blocks have \(a\) complete-one blocks, one block with \(s\) ones, and all remaining blocks zero.
* If \(s=c\), it is exactly a disjoint union of \(r\binom{r-1}{a}\) coordinate faces of \(H\), each congruent to \(\Delta(c,q)\) and of dimension \(q-1\). In every such face \(a\) blocks are all ones, \(r-a-1\) blocks are all zeros, and the remaining block is arbitrary in \(\Delta(c,q)\). All these points, including nonvertices, are equally far from \(P\).

Thus the deepest locus contains nonvertices **if and only if** \(q\mid(r-1)c\), equivalently \(rc\bmod q=c\). This is an arithmetic resonance of the block sizes and quotas. For example, \((r,q,c)=(3,4,2)\) has squared Hausdorff distance \(2\), and its farthest set is six disjoint three-dimensional octahedral faces rather than isolated vertices.

## Assumptions and scope

The metric is the ambient coordinate Euclidean distance, not a rescaled intrinsic metric on the smaller affine hull. The three integer parameters satisfy exactly the conditions above. Distances are from \(H\) to \(P\), which equals the symmetric Hausdorff distance because \(P\subset H\). All class labels are distinct; the formulas and extremal classifications are valid without any generic-position assumption. The result classifies *all points* maximizing the distance, not only the vertex-supported ones.

## Proof

**1. Euclidean projection of a binary block.** Let \(u\in\{0,1\}^q\) have exactly \(k\) ones. Its unique Euclidean projection \(\pi(u)\) onto \(\Delta(c,q)\) is
\[
\pi(u)_i=\begin{cases}
1,&k\le c\text{ and }u_i=1,\\
(c-k)/(q-k),&k\le c\text{ and }u_i=0,\\
c/k,&k\ge c\text{ and }u_i=1,\\
0,&k\ge c\text{ and }u_i=0.
\end{cases}
\]
This is feasible in all boundary cases. By permutation symmetry among the one-coordinates and zero-coordinates, uniqueness of Euclidean projection makes the projected point constant on each group. The closest feasible pair of values must first preserve every possible one-coordinate when \(k\le c\), and preserve every possible zero-coordinate when \(k\ge c\), since otherwise moving mass from a zero-coordinate toward a one-coordinate strictly reduces squared error. The remaining single affine constraint gives the displayed values. Therefore \(\|u-\pi(u)\|_2^2=F(k)\).

**2. Distance from an ambient vertex.** The vertices of \(H\) are binary incidence vectors of subsets of cardinality \(rc\). If one such vertex has \(k_j\) ones in block \(B_j\), then \(0\le k_j\le q\), \(\sum_j k_j=rc\), and the Cartesian-product projection just proved gives
\[
d(u,P)^2=\sum_{j=1}^r F(k_j).
\]
Conversely every integral occupancy profile obeying those conditions is attained by some vertex of \(H\).

**3. Strict-convex occupancy extremum.** Extend \(F\) to real \(0\le t\le q\) by the same piecewise formulas. It is continuously differentiable at \(t=c\), where both one-sided derivatives vanish. Direct differentiation shows
\[
F''(t)=\begin{cases}
2(q-c)^2/(q-t)^3,&0<t<c,\\
2c^2/t^3,&c<t<q.
\end{cases}
\]
Both are strictly positive. Hence \(F\) is strictly convex on \([0,q]\). If two coordinates of an occupancy vector lie strictly between \(0\) and \(q\), shift mass between those coordinates, preserving their sum. Their two-term \(F\)-sum is strictly convex along the feasible shift interval; its value at the original interior point is strictly less than at one endpoint. Both endpoints are integral whenever the original occupancies are integral. Iterating ends with at most one non-endpoint occupancy, and strictly increases the sum at every nontrivial step. Given total \(rc\), the unique such multiset is \(a\) copies of \(q\), one copy of \(s\) if \(s>0\), and zeros otherwise. It follows that this multiset and only it maximizes \(\sum_jF(k_j)\). The displayed squared-distance formula and the extremal-vertex counts follow by choosing full blocks, a possible partial block, and its \(s\) selected positions.

**4. From vertices to every point of the hypersimplex.** For any convex decomposition \(x=\sum_v\lambda_v v\) into vertices of \(H\), let \(p_v=\Pi_P(v)\) and \(z_v=v-p_v\). Since \(\sum_v\lambda_v p_v\in P\), the Euclidean variance identity gives
\[
 d(x,P)^2\le\left\|\sum_v\lambda_v z_v\right\|_2^2
 =\sum_v\lambda_v\|z_v\|_2^2-
 \tfrac12\sum_{v,w}\lambda_v\lambda_w\|z_v-z_w\|_2^2
 \le d_H(H,P)^2.
\]
Equality forces every positive-weight vertex to be an extremal vertex from step 3 and all their residual vectors \(z_v\) to be equal. Conversely, if a collection of extremal vertices has the same residual \(z\), every convex combination of them also has distance \(\|z\|\), because the Euclidean projection normal inequality \(\langle z,p-p_v\rangle\le0\) for all \(p\in P\) survives convex averaging.

To identify residual collisions, note that a full block has constant residual \((q-c)/q>0\), and an empty block has constant residual \(-c/q<0\). In a partially filled block with \(s>c\), the residual is \(1-c/s>0\) on selected coordinates and zero on the others; with \(s<c\), it is zero on selected coordinates and \(-(c-s)/(q-s)<0\) on unselected coordinates. For \(s\ne c\) these patterns distinguish not only full, empty and partial blocks, but also every selected coordinate. No two distinct extremal vertices share a residual. When \(s=c\), the partial-block residual vanishes identically, regardless of the selected coordinates. The only collisions then come from changing the selected \(c\)-set within one fixed partial block, leaving all full/empty block assignments unchanged. Their convex hull is exactly the displayed \(\Delta(c,q)\) coordinate face. This proves the complete equality classification.

## Verification

The standalone standard-library script `check_partition.py` evaluates the exact rational formula and exhaustively optimizes occupancy profiles for \(75\) parameter choices \(3\le r\le7\), \(2\le q\le6\), \(1\le c<q\). It examines \(209445\) feasible block-occupancy profiles (representing a combinatorially counted total of \(660714883218\) vertices), confirms every maximizing profile, tests independent numerical Euclidean water-filling projections, and verifies a nonvertex farthest point of the \((3,4,2)\) example. Its output is

`BALANCED_PARTITION_HAUSDORFF_PASS parameter_cases=75 occupancy_profiles=209445 combinatorially_counted_vertices=660714883218 arithmetic_face_resonances=25 independent_projection=PASS nonvertex_deep_hole=PASS`

The proof of the theorem for all parameters is analytical and does not rely on finite enumeration. The count \(660714883218\) is calculated using binomial multiplicities; those vertices are not individually enumerated.

## Relationship to prior work

Schröter, *Multi-splits and tropical linear spaces from nested matroids* (first posted 2017-07-10), gives the precise product-of-hypersimplices description of partition matroid base polytopes (Example 16) and shows that these arise naturally as common cells of matroidal hypersimplex multi-splits (Proposition 22). The present result uses that same geometrically motivated family, but asks for the **ambient Euclidean separation from the full hypersimplex**, which is not the subject of Schröter's enumeration and subdivision theorems.

Lasoń and Michałek, *On algebraic properties of matroid polytopes* (first posted 2020-05-17), explicitly give the Cartesian-product rule for matroid base polytopes (Lemma 2.4), then classify smoothness and Gorenstein properties. The product rule is a premise, not a metric separation result. Torres, *On Finding the Closest Zonotope to a Polytope in Hausdorff Distance* (first posted 2024-07-18), provides general Hausdorff optimization tools for zonotope approximants; it does not provide the rank/quota/block formula or the farthest-face resonance (the present product-of-hypersimplices generally is not a zonotope).

The new point is the combined exact all-parameter Hausdorff radius and exhaustive equality locus, especially the arithmetic distinction between isolated deep vertices and entire deep coordinate faces. Closely related general projection and matroid-polytope results may still contain a reformulation; no priority claim beyond the inspected literature is made.

## Limitations

This concerns equal-sized classes carrying equal quotas, not arbitrary partition matroids or weighted Euclidean metrics. It does not address signed support-function distances or probabilistic average distance. General polytope distance algorithms do not automatically give a closed formula or equality classification. Historical-priority searches cannot establish absolute novelty, and no independent mathematical audit has been performed.

## References

1. B. Schröter, *Multi-splits and tropical linear spaces from nested matroids*, arXiv:1707.02814 (initial submission 2017-07-10), especially Example 16, Proposition 22, Corollary 29. https://arxiv.org/abs/1707.02814
2. M. Lasoń and M. Michałek, *On algebraic properties of matroid polytopes*, arXiv:2005.08359 (initial submission 2020-05-17), especially Lemma 2.4 and Theorems 1.1–1.2. https://arxiv.org/abs/2005.08359
3. G. D. Torres, *On Finding the Closest Zonotope to a Polytope in Hausdorff Distance*, arXiv:2407.13125 (initial submission 2024-07-18), especially Section 3. https://arxiv.org/abs/2407.13125
