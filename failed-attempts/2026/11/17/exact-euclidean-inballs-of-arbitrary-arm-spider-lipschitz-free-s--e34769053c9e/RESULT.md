# Exact Euclidean inballs of arbitrary-arm spider Lipschitz-free spaces

## Finding
Let \(q\ge3\), and let \(\ell_1,\ldots,\ell_q\) be arbitrary positive integers. Form the unit-edge spider tree \(T\) by joining one endpoint of \(q\) disjoint paths, with the \(i\)-th path containing \(\ell_i\) edges, at a common hub. Put \(n=\sum_{i=1}^q\ell_i\) and \(N=n+1\). In the Euclidean zero-sum hyperplane \(H=\{z\in\mathbb R^N:\sum_{v\in V(T)}z_v=0\}\), consider the standard real Lipschitz-free unit ball
\[
K_T=\operatorname{conv}\{\pm(e_v-e_w):vw\in E(T)\}\subset H.
\]
All radii, facet distances and affine dimensions use the Euclidean structure induced on \(H\), not the abstract Banach-space norm or an arbitrary linear transformation of this realization.

Set
\[
w_i=\frac{\ell_i(\ell_i+1)}2,\qquad
u_i=\frac{\ell_i(\ell_i+1)(2\ell_i+1)}6,
\qquad
\delta=\min_{\varepsilon\in\{-1,1\}^q}
\left|\sum_{i=1}^q\varepsilon_iw_i\right|.
\]
Let \(\mathcal E\subset\{-1,1\}^q\) consist precisely of the sign vectors attaining this minimum, and let \(d=\operatorname{rank}_{\mathbb R}(\mathcal E)\), meaning the row rank of the matrix with rows the sign vectors in \(\mathcal E\).

**Theorem.** The unrestricted (global) Euclidean inradius, the exact number of facets tangent to its origin-centered maximum-radius ball, and the affine dimension of the set \(\mathcal C\) of **all** maximum-radius ball centers are respectively
\[
\boxed{r_{\mathrm{in}}(K_T)=\left(\sum_{i=1}^q\nu_i-\frac{\delta^2}{N}\right)^{-1/2},\qquad
F_{\mathrm{contact}}=|\mathcal E|,\qquad
\dim\operatorname{aff}(\mathcal C)=n-d.}
\]
The origin is an incenter. More structurally, **every** polar vertex normal attaining maximum Euclidean norm corresponds to a Lipschitz potential whose successive edge increments are constant in sign along each complete arm, and **only** such armwise-monotone potentials with sign vector in \(\mathcal E\) attain it. Thus a potentially exponential optimization over all \(2^n\) dual facets reduces exactly to a signed partition of the \(q\) triangular weights \(w_i\).

The signed-partition minimum and the number of minimizing signs can be found by an integer dynamic program using at most \(2\sum_iw_i+1\) states per step, hence polynomially in the number of tree vertices. The contact rank can be determined from the minimizing signs without constructing any full-dimensional facet normals. In particular, \(d\le q\), so whenever at least one arm has more than one edge, \(\dim\operatorname{aff}(\mathcal C)\ge n-q>0\). If \(\delta=0\), the minimizing sign vectors also lie in the proper hyperplane \(\sum_iw_i\varepsilon_i=0\); consequently \(d\le q-1\) and \(\dim\operatorname{aff}(\mathcal C)\ge n-q+1\).

For example, the heterogeneous arms \((1,2,3,4)\) have weights \((1,3,6,10)\) and \(\sum_i\nu_i=50\). The partition \(10=1+3+6\) gives \(\delta=0\) and exactly two minimizing sign vectors. Hence \(r_{\mathrm{in}}=1/\sqrt{50}\), precisely two centered tangent facets, and a nine-dimensional affine family of optimal centers in the ten-dimensional space \(H\).

## Assumptions and scope
The tree is finite, simple and unweighted. Distances among vertices are graph shortest-path distances. The real finite-metric Lipschitz-free unit ball is the convex hull of normalized molecules \((e_v-e_w)/d_T(v,w)\). Every nonedge molecule is a convex combination of oriented unit-edge molecules along its unique shortest path, hence the unit ball is exactly \(K_T\). Each tree edge vector is linearly independent of the others in \(H\), so \(K_T\) is an \(n\)-dimensional crosspolytope as a combinatorial polytope, but not necessarily Euclidean-regular. The theorem is about its **specific canonical Euclidean shape**, not a coordinate-free crosspolytope radius. The assumption \(q\ge3\) keeps all arms proper subtrees and distinguishes the spider from a path.

## Proof
**1. Polar facet normals are signed edge potentials.** The intrinsic Euclidean polar is
\[
K_T^\circ=\{f\in H: |f_v-f_w|\le1\text{ on each tree edge }vw\}.
\]
The linear map taking a zero-sum potential \(f\) to its \(n\) oriented edge differences is an isomorphism. Thus \(K_T^\circ\) is linearly isomorphic to the cube \([-1,1]^n\), whose vertices have every edge difference equal to \(\pm1\). Distinct such vertices give distinct facets \(\langle f,z\rangle\le1\) of \(K_T\). The facet distance from zero is \(1/\|f\|_2\).

For a signed edge potential, subtract an arbitrary constant so that the hub has value zero. If the uncentered vertex values are \(y_v\), the corresponding zero-sum polar normal is \(f_v=y_v-\bar y\), and
\[
\|f\|_2^2=\sum_v y_v^2-\frac{(\sum_vy_v)^2}{N}.
\tag{1}
\]
The hub contributes zero to both sums.

**2. Strict full-arm screening lemma.** Consider one arm of length \(L\ge1\), with uncentered values \(y_0=0,y_1,\ldots,y_L\) and \(y_j-y_{j-1}\in\{-1,1\}\). Put \(s=\sum_{j=1}^L y_j\), \(v=\sum_{j=1}^L y_j^2\), \(w=L(L+1)/2\), \(u=L(L+1)(2L+1)/6\). The exact variance identity along the \(L+1\) vertices is
\[
(L+1)v-s^2=\sum_{0\le j<k\le L}(y_j-y_k)^2.
\]
Every difference \(|y_j-y_k|\le k-j\). Summing squared bounds and evaluating at a unit-slope ramp gives the sharp inequality
\[
\boxed{(L+1)(u-v)\ge w^2-s^2.}
\tag{2}
\]
If the increments on the arm are not all of the same sign, then \(|s|<w\) (because for each depth \(j\), \(|y_j|\le j\), and equality in the weighted sum would require every increment to have one common sign).

Write \(a\) for the sum of potentials on all **other** arms. Replace the chosen arm by the full-height ramp \(y'_j=\sigma j\), where \(\sigma\) has sign opposite to \(a\) (choose either sign if \(a=0\)). Its new sum is \(s'=\sigma w\) and its new square sum is \(u\). By (1) the change in squared norm is
\[
\Delta=(u-v)+\frac{(a+s)^2-(|a|-w)^2}{N}.
\]
The reverse triangle inequality implies \((a+s)^2\ge(|a|-|s|)^2\), and elementary expansion yields
\[
(|a|-|s|)^2-(|a|-w)^2
=(w-|s|)(2|a|-w-|s|)\ge-(w^2-s^2).
\]
Together with (2), this gives the explicit strict gap
\[
\boxed{\Delta\ge (w^2-s^2)\left(\frac1{L+1}-\frac1N\right)>0}
\tag{3}
\]
for any nonmonotone arm, because \(w^2-s^2>0\) and \(N>L+1\). This **strict** replacement works regardless of the sign choices on the other arms, so every maximizer of the polar Euclidean norm must have constant-signed increments along each complete arm. No argument from finite enumeration is used in this step.

**3. Exact radius and centered contact multiplicity.** For an armwise-monotone potential choose signs \(\varepsilon_i\in\{-1,1\}\). Its uncentered value at depth \(j\) on arm \(i\) is \(\varepsilon_i j\). Consequently \(\sum_v y_v^2=\sum_i\nu_i\) and \(\sum_vy_v=\sum_i\varepsilon_iw_i\). Equation (1) gives
\[
\|f^\varepsilon\|_2^2=\sum_i\nu_i-
\frac{(\sum_i\varepsilon_iw_i)^2}{N}.
\tag{4}
\]
The maximum is therefore \(M^2=\sum_i\nu_i-\delta^2/N\), attained at exactly the signed arm profiles in \(\mathcal E\). The screening lemma shows there are no additional maximizing cube vertices. Distinct sign profiles give distinct polar vertices and facets, hence exactly \(|\mathcal E|\) facets touch the origin-centered ball of radius \(1/M\).

The radius is globally optimal, not just centered-optimal: because \(K_T\) is centrally symmetric, any radius-\(r\) ball contained in \(K_T\) and centered at \(c\) has its reflected ball centered at \(-c\) contained as well. Convexity then contains the ball of radius \(r\) centered at the origin. Equivalently, the opposite pair of maximum-norm facet inequalities forces \(r\le1/M\) at every possible center. This proves the radius formula.

**4. Affine hull of all optimal centers.** Let \(\mathcal F\) be the set of maximizing polar normals \(f^\varepsilon\), \(\varepsilon\in\mathcal E\). For any ball of radius \(1/M\) centered at \(c\), both inequalities with normals \(f^\varepsilon\) and \(-f^\varepsilon\) force \(\langle c,f^\varepsilon\rangle=0\). Conversely, by (3), every other polar vertex normal has strictly smaller norm, hence its facet has strictly positive clearance slack at \(c=0\). Since there are finitely many facets, a relative neighborhood of the origin inside \(\operatorname{span}(\mathcal F)^\perp\cap H\) consists of centers of radius-\(1/M\) balls. Thus
\[
\operatorname{aff}(\mathcal C)=\operatorname{span}(\mathcal F)^\perp\cap H,
\qquad \dim\operatorname{aff}(\mathcal C)=n-\dim\operatorname{span}(\mathcal F).
\tag{5}
\]
For each arm, let \(g_i\in H\) be the centered potential that is depth \(j\) at its vertices, zero at all other vertices including the hub, before subtracting the mean. Then \(f^\varepsilon=\sum_i\varepsilon_i g_i\). The vectors \(g_i\) are linearly independent, because taking the first oriented edge difference along arm \(i\) gives \(1\) for \(g_i\) and \(0\) for every \(g_h\) with \(h\ne i\). Therefore \(\dim\operatorname{span}(\mathcal F)=\operatorname{rank}_{\mathbb R}(\mathcal E)=d\), proving (5) and the stated center dimension.

**5. Constructive partition calculation.** The positive integer weights \(w_i\) allow a dynamic program: initialize \(D_0(0)=1\) and update \(D_i(z)=D_{i-1}(z-w_i)+D_{i-1}(z+w_i)\). At completion, \(\delta=\min\{|z|:D_q(z)>0\}\) and \(|\mathcal E|=\sum_{|z|=\delta}D_q(z)\). There are at most \(2\sum_iw_i+1\) integer states at any step, proving the polynomial bound. For the rank, retain or reconstruct the winning sign vectors, then perform rational row reduction. The theorem does not assert that enumerating every winning vector is polynomial in the input size.

## Verification
The proof applies symbolically to all \(q\ge3\) and all positive integer arm lengths. The independent, standard-library-only `check_spider.py` verifies (2) for every signed unit-step path up to length nine, exhaustively enumerates every signed edge potential for 86 spider parameter profiles (68,904 potentials total), reconstructs exact zero-sum facet norms and contacting-normal ranks, and separately checks signed-partition counts for 1,113 profiles. It reports:

```text
ARM_PATH_VARIANCE_INTEGER_IDENTITY_PASS 1022
SPIDER_ALL_SIGNED_EDGE_POTENTIALS_PASS profiles=86 potentials=68904
TRIANGULAR_PARTITION_COUNTS_PASS profiles=1113
ARBITRARY_ARM_SPIDER_THEOREM_FINITE_CHECKS_PASS
```

Run `python3 check_spider.py` after extracting the embedded script. Its finite checks corroborate, but do **not** replace, the infinite proof. The exact rank step in the checker uses rational row reduction and thus is not subject to floating-point tolerances.

## Relationship to prior work
Aliaga's 2021 work characterizes extreme molecules for proper metric spaces, a foundational property of the primal Lipschitz-free ball, but does not determine Euclidean inballs in a fixed embedding. Alexander, Fradelizi, García-Lirola, and Zvavitch (2019 preprint) connect finite metric spaces and Lipschitz-free unit balls, and study their combinatorial/Banach geometry and volume products. D'Alì, Delucchi, and Michałek (2019 preprint; 2022 publication) relate symmetric-edge and finite-metric fundamental polytopes and provide graph-facet criteria. Delucchi and Hoessly characterize the face structures of tree-metric fundamental polytopes. None of these inspected statements furnishes the signed triangular-partition reduction for the canonical Euclidean spider inball.

Published special-family results determine the inradius and incenter loci for paths, single-edge stars, and two-hub bistars, as well as for uniformly twice-sized arms or mixtures of one- and two-edge arms. These are genuine prior special cases or different graph families; the present theorem specifically treats **arbitrary** arm lengths, including several unequal long arms, and proves the strict path-variance screening lemma needed to avoid all nonmonotone gradient configurations. The distinction is not a change of coordinates: unimodularly equivalent crosspolytopes can have different canonical Euclidean facet distances.

The closest broad equivalence risk is a potentially older formula for maximum centered variance of integer 1-Lipschitz functions on starlike trees or a differently phrased graph-spread theorem. Targeted searches and the indicated full-text inspections did not find one; this does not prove historical uniqueness.

## Limitations
This theorem uses the **unweighted** shortest-path metric and the canonical Euclidean zero-sum embedding. It does not claim that its inradius is invariant under arbitrary Banach-space isometries, unitary changes on unrelated embeddings, or general positive edge weights. It gives the exact affine dimension of all incenters, but does not enumerate the vertices of their center polytope or count facets that become additionally tangent at nonzero centers. The rank calculation may require exponentially many winning sign vectors; only the signed-partition minimum and number of centered contacts have the stated polynomial dynamic program. Priority under unpublished or differently indexed variance formulations is not excluded.

## References
1. Ramón J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219v1 (public 2021-02-01), https://arxiv.org/abs/2102.01219; primary MSC2020 46B20.
2. Matthew Alexander, Matthieu Fradelizi, Luis C. García-Lirola, and Artem Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642v1 (public 2019-11-24), https://arxiv.org/abs/1911.10642.
3. Alessio D'Alì, Emanuele Delucchi, and Mateusz Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1 (public 2019-10-11), https://arxiv.org/abs/1910.05193; *Electronic Journal of Combinatorics* 29 (2022), P3.24.
4. Emanuele Delucchi and Linard Hoessly, *Fundamental polytopes of metric trees via parallel connections of matroids*, arXiv:1612.05534, https://arxiv.org/abs/1612.05534; *European Journal of Combinatorics* 87 (2020), 103098.
