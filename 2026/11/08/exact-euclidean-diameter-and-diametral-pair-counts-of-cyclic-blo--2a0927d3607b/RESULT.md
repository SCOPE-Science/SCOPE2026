# Exact Euclidean diameter and diametral-pair counts of cyclic block polytopes

## Finding
For integers \(m\ge4\) and \(a\ge1\), let \(\mathcal C_m^{(a)}\subset\mathbb R^{am}\) be the cyclic block polytope introduced in [1]. Put \(r=\lfloor m/2\rfloor\). Then its squared diameter in the **standard ambient Euclidean metric** is
\[
\boxed{\operatorname{diam}_2(\mathcal C_m^{(a)})^2=2r.}
\]
Every diametral pair consists of two distinct **vertices** obtained from maximum independent sets of the cycle \(C_m\): choose \(r\) pairwise nonadjacent blocks for each endpoint, put one coordinate equal to \(1\) in each selected block, and put \(0\) in every other coordinate. The two resulting vectors must have disjoint coordinate support. This condition is both necessary and sufficient. In particular, for odd \(m\), the half-integral vertices are never diametral endpoints.

The exact number \(N_{m,a}\) of unordered pairs attaining the diameter is
\[
\boxed{N_{2r,a}=a^{2r}+[a(a-1)]^r\quad(r\ge2),}
\]
and
\[
\boxed{N_{2r+1,a}=(2r+1)\sum_{t=0}^{r-1}a^{2r-t}(a-1)^t
+\frac{2r+1}{2}[a(a-1)]^r\quad(r\ge2).}
\]
The odd formula can equivalently be expressed, without a sum, as
\[
N_{2r+1,a}=(2r+1)a^{r+1}\bigl(a^r-(a-1)^r\bigr)
+\frac{2r+1}{2}[a(a-1)]^r.
\]
The formulas are integers for all permitted \(a\), since \(a(a-1)\) is even. In particular, the unblocked counts are \(N_{2r,1}=1\) and \(N_{2r+1,1}=2r+1\), whereas colored blocks yield additional same-block-support pairs.

## Assumptions and scope
The coordinates are \(x_{ij}\) with \(i\in\mathbb Z/m\mathbb Z\) and \(1\le j\le a\). Define the nonnegative block sums \(R_i(x)=\sum_{j=1}^a x_{ij}\), and set
\[
\mathcal C_m^{(a)}=\{x\in\mathbb R_{\ge0}^{am}:R_i(x)+R_{i+1}(x)\le1
\text{ for all }i\in\mathbb Z/m\mathbb Z\}.
\]
The Euclidean distance is calculated in the displayed coordinate system, with no projection, normalization, or change of inner product. The polytope is full-dimensional and compact for \(m\ge4\). A diametral pair means an **unordered set of two distinct points of the whole polytope** separated by its maximum Euclidean distance; the theorem proves that these endpoints are necessarily vertices, so the count is finite. The original public source is dated 2026-07-24 [1].

## Proof
**Step 1: classify vertices.** Define the fractional stable-set polytope
\[
Q_m=\{R\in\mathbb R_{\ge0}^{m}:R_i+R_{i+1}\le1\text{ cyclically}\}.
\]
Every vertex \(x\) of \(\mathcal C_m^{(a)}\) has at most one positive coordinate in each block: two such coordinates could be varied in opposite directions while retaining the block sum. Its block-sum vector \(R(x)\) must be a vertex of \(Q_m\): if \(R(x)\) were the midpoint of two distinct feasible block-sum vectors, then their zero entries at the zero blocks agree, and small signed perturbations of the sole positive coordinate in each nonzero block would decompose \(x\) nontrivially.

Conversely, fixing a vertex of \(Q_m\) and assigning each of its nonzero block sums to exactly one coordinate of that block gives a vertex of \(\mathcal C_m^{(a)}\). Indeed, any convex decomposition would project to a convex decomposition of the vertex of \(Q_m\), forcing the same block sums; within each block a nonnegative point supported on a single coordinate is extreme in its fixed-sum simplex.

For completeness, the vertices of \(Q_m\) can be determined directly. If any coordinate vanishes, the remaining active cycle edges induce disjoint paths. Their vertex constraints form a bipartite incidence matrix and hence are totally unimodular; such a vertex has only \(0\) and \(1\) coordinates, corresponding precisely to an independent set of \(C_m\). If all coordinates are positive, vertexhood requires every cyclic edge inequality to be tight. When \(m\) is odd the unique solution of \(R_i+R_{i+1}=1\) is \(R_i=1/2\) for all \(i\); when \(m\) is even these equations leave a one-dimensional family and so produce no vertex with all coordinates positive. Thus the complete vertex list is: colored independent-set incidence vectors, and, only for odd \(m\), one-half in a chosen coordinate of every block. This classification is compatible with [1, Lemma 3.4]; it is not claimed as new.

**Step 2: diameter and equality.** Every independent set of \(C_m\) has size at most \(r\). Therefore an integral vertex \(v\) satisfies \(\|v\|_2^2\le r\), with equality exactly when it encodes a *maximum* independent set. A half-integral vertex, present only when \(m=2r+1\), has squared norm \(m/4<r\) because \(r\ge2\). Hence \(\|v\|_2^2\le r\) at all vertices; by convexity of squared norm, the same inequality holds throughout the polytope.

For every two points \(x,y\) in the polytope, nonnegativity gives \(x\cdot y\ge0\). Consequently
\[
\|x-y\|_2^2=\|x\|_2^2+\|y\|_2^2-2x\cdot y\le2r.
\]
Two disjoint maximum independent sets exist on every cycle: for an even cycle take the two alternating color classes, and for an odd cycle take the sets of alternating positions that omit one of two different adjacent pairs. Put a \(1\) in an arbitrary coordinate of each selected block. Their supports are disjoint, so their squared distance is \(2r\), proving sharpness.

The squared distance is **strictly convex in either endpoint** when the other is fixed. A nonvertex point of a finite polytope is a nontrivial convex combination of distinct feasible points and cannot maximize a strictly convex squared-distance function. Thus every diametral endpoint is a vertex. Equality in the displayed bound then requires \(\|x\|_2^2=\|y\|_2^2=r\) and \(x\cdot y=0\). By the vertex classification these are precisely the stated colored maximum-independent-set vertices with disjoint coordinate support.

**Step 3: enumerate all equality pairs.** If \(m=2r\), the only maximum independent sets are the two alternating block sets. Pairs with different block sets yield \(a^{2r}\) choices. When both endpoints use the same alternating block set, they must choose distinct coordinate labels in each of the \(r\) blocks. This gives \([a(a-1)]^r\) *ordered* label pairs for each of two block sets, and hence \([a(a-1)]^r\) unordered pairs altogether. This proves the even formula.

If \(m=2r+1\), there are precisely \(m\) maximum independent sets, each a rotation of \(S=\{0,2,\ldots,2r-2\}\). For \(1\le k\le r\), the rotated set \(S+2k\) intersects \(S\) in \(r-k\) blocks; for \(0\le k\le r-1\), \(S+(2k+1)\) intersects \(S\) in \(k\) blocks (indices modulo \(m\)). Thus, for each \(t\in\{0,\ldots,r-1\}\), each maximum independent set has precisely two *other* maximum independent sets with overlap size \(t\). There are therefore precisely \(m\) unordered **distinct-block-set pairs** at each overlap size \(t\).

When the block sets overlap in \(t\) positions, their union has \(2r-t\) positions. At each of the \(t\) common blocks the ordered endpoint labels must differ, allowing \(a(a-1)\) choices; every other selected block allows \(a\) choices. Hence an unordered pair of distinct block sets yields \(a^{2r-t}(a-1)^t\) diametral pairs. Summing gives the first term of the odd formula. For equal block sets, the same label argument as in the even case gives \(m[a(a-1)]^r/2\) additional unordered pairs. Finally, the geometric sum gives the equivalent closed form by the factorization \(a^r-(a-1)^r\). No overlap or double counting occurs, since the unordered pair of block supports is determined by the two endpoints.

## Verification
The attached `verify.py` constructs every colored integral vertex, and every half-integral vertex when applicable, in 16 explicit small-parameter cases with \(4\le m\le9\) and \(1\le a\le3\). It checks the defining inequalities, evaluates **973,988 unordered vertex-pair squared distances using exact integer arithmetic** after doubling all coordinates, and independently confirms both the asserted maxima and the closed pair counts. A second independent-support overlap enumeration checks 111 model assertions over \(4\le m\le22\) and \(1\le a\le5\). The analytic proof, not the finite checks, establishes the theorem for all \(m\ge4\) and \(a\ge1\).

To reproduce: run `python3 verify.py` with Python 3.10 or later. The verifier uses only the standard library. The asserted exact distances are integer multiples of \(1/4\), so no numerical tolerance enters.

## Relationship to prior work
Jiang, Yang, and Zhong [1] introduce this exact cyclic block family, prove the relevant cyclic half-integral vertex facts, and develop transfer-matrix, Ehrhart, and Gorenstein results. Their inspected full manuscript (including Lemma 3.4 and its concluding discussion) does not state the Euclidean diameter, classify every diametral pair, or count its colored equality cases. The vertex characterization is acknowledged as part of the earlier theory; the new assertion is the **complete metric extremizer classification and exact two-parameter enumeration**.

A published same-object result for the unblocked cycle fractional stable-set polytope [2] determines the *minimum enclosing ball* and its contact vertices. It does not determine the **maximum pairwise Euclidean separation** or its exact multiplicity, and gives no colored-block count for \(a>1\). The other nearby work on circuit diameter [3] concerns paths through circuit directions of optimization polytopes, not ambient Euclidean vertex-to-vertex diameter. Generic bounds from the independence number supply the easy upper inequality but do not imply the complete equality-pair enumeration. The closed counts and equality rigidity are consequently distinguished from known prior ingredients.

## Limitations
The classification is for equal block sizes and unit cyclic adjacent-sum bounds in the displayed Euclidean coordinates. It does not address arbitrary unequal block sizes, weighted diagonal metrics, modified edge capacities, or general graphs. The lower-bound geometry and vertex types draw on well-known stable-set theory, so independent discovery of the exact colored equality count under a different name remains possible. A textual research search is not a proof of global publication priority, and no independent audit has yet been performed.

## References
1. Xinru Jiang, Shuai Yang, and Yueming Zhong, *Transfer Matrices and Ehrhart Theory for Path and Cyclic Block Polytopes*, arXiv:2607.22008v1, first public 2026-07-24, especially equation (2), Lemma 3.4, and Section 4. https://arxiv.org/abs/2607.22008
2. *Cycle fractional stable-set polytopes have a parity-split minimum sphere*, public mathematical research record, 2026-10-11, full RESULT.md inspected at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-cycle-fractional-stable-set-polytopes-have-a-parity-split-minimu--0b914e4f06d2
3. Sean Kafer, Kanstantsin Pashkovich, and Laura Sanità, *On the Circuit Diameter of Some Combinatorial Polytopes*, arXiv:1709.09642 (2017), *SIAM Journal on Discrete Mathematics* 33 (2019), 1–25. https://arxiv.org/abs/1709.09642
