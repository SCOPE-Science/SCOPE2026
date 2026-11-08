# Sharp rank–corank convexification of hypersimplex vertex sets

## Finding
For every pair of integers \(n\ge3\) and \(1\le k\le n-1\), let
\[
P_{n,k}=\left\{y\in[0,1]^n:\sum_{i=1}^ny_i=k\right\},\qquad
V_{n,k}=\{\mathbf 1_I:I\subseteq\{1,\ldots,n\},\ |I|=k\}.
\]
The Schneider nonconvexity index of the vertex set of this uniform-matroid base polytope is exactly
\[
\boxed{c(V_{n,k})=\max\{k,n-k\}},\qquad
c(A):=\inf\{\lambda>0:A+\lambda\operatorname{conv}(A)\text{ is convex}\}.
\]
Accordingly its sharp vertex-generation parameter, in the normalization of Artstein-Avidan–Falah–Slomka, is
\[
\boxed{\eta(P_{n,k})=\frac{1}{1+\max\{k,n-k\}}}.
\]
The result holds in the affine hull \(\sum_i y_i=k\), and thus under arbitrary invertible affine changes of coordinates in that hull.

More precisely, for \(\lambda\ge1\), write \(y_{(1)}\ge\cdots\ge y_{(n)}\) for the ordered coordinates of \(y\in P_{n,k}\). Then the **full pointwise coverage criterion** is
\[
\boxed{(1+\lambda)y\in V_{n,k}+\lambda P_{n,k}
\iff y_{(k)}\ge\frac{1}{1+\lambda}
\ \text{and}\ y_{(k+1)}\le\frac{\lambda}{1+\lambda}.}
\]
For \(\lambda\ge1\), the uncovered region in \(P_{n,k}\), after normalizing by \(1+\lambda\), is therefore precisely the disjoint union of the two strict-failure regions
\[
\left\{y:y_{(k)}<\frac{1}{1+\lambda}\right\}
\quad\text{and}\quad
\left\{y:y_{(k+1)}>\frac{\lambda}{1+\lambda}\right\}.
\]
The first region is nonempty exactly when \(\lambda<n-k\); the second is nonempty exactly when \(\lambda<k\). Hence the two rank–corank thresholds give the entire coverage phase diagram, not just the endpoint.

## Assumptions and scope
All vector coordinates are real, \(n\ge3\), \(1\le k\le n-1\). The convex set \(P_{n,k}\) has relative dimension \(n-1\), and \(V_{n,k}\) is exactly its finite vertex set. Scalar multiplication and Minkowski addition use the embedding in \(\mathbb R^n\). The word “convex” for the sumset is ordinary Euclidean convexity (equivalently relative convexity in its affine hull). The pointwise order-statistic characterization is asserted only for \(\lambda\ge1\); the global convexification index is proved for **all** \(\lambda>0\). There is no generic-position assumption or unproved rank restriction.

## Proof
**1. Normalization.** Since \(\operatorname{conv}(V_{n,k})=P_{n,k}\), the convex hull of \(V_{n,k}+\lambda P_{n,k}\) is \((1+\lambda)P_{n,k}\). It follows that the sumset is convex exactly if it equals this dilate. Dividing by \(1+\lambda\) converts convexification into covering \(P_{n,k}\) by its homothetic vertex copies.

**2. Exact membership in a fixed vertex copy.** Fix \(y\in P_{n,k}\), \(\lambda>0\), and a subset \(I\subset[n]\) of cardinality \(k\). The equation
\[
(1+\lambda)y=\mathbf1_I+\lambda z,\qquad z\in P_{n,k},
\]
forces \(z_i=((1+\lambda)y_i-\mathbf1_I(i))/\lambda\). Its coordinate sum automatically equals \(k\). The conditions \(0\le z_i\le1\) are equivalent to
\[
y_i\ge\frac1{1+\lambda}\quad(i\in I),
\qquad y_i\le\frac\lambda{1+\lambda}\quad(i\notin I).
\]
When \(\lambda\ge1\), the former threshold is no larger than the latter. Thus a suitable \(I\) exists exactly when there are at least \(k\) coordinates at least \(1/(1+\lambda)\) and at most \(k\) coordinates strictly greater than \(\lambda/(1+\lambda)\). These conditions are, respectively, the inequalities for \(y_{(k)}\) and \(y_{(k+1)}\) in the stated formula. This proves both directions, including all threshold ties.

**3. The sharp universal coordinate bounds.** For any \(y\in P_{n,k}\), its \(k-1\) largest coordinates sum to at most \(k-1\). Therefore the remaining \(n-k+1\) coordinates have sum at least \(1\), and each is at most \(y_{(k)}\), proving
\[
y_{(k)}\ge\frac1{n-k+1}.
\]
The first \(k+1\) coordinates have sum at most \(k\), and each is at least \(y_{(k+1)}\), proving
\[
y_{(k+1)}\le\frac{k}{k+1}.
\]
Both bounds are attained. The lower bound is attained by
\[
y^{\mathrm{corank}}=(\underbrace{1,\ldots,1}_{k-1},
\underbrace{1/(n-k+1),\ldots,1/(n-k+1)}_{n-k+1}),
\]
and the upper by
\[
y^{\mathrm{rank}}=(\underbrace{k/(k+1),\ldots,k/(k+1)}_{k+1},
\underbrace{0,\ldots,0}_{n-k-1}).
\]
Every vector in these two displays belongs to \(P_{n,k}\), including the cases \(k=1\) or \(k=n-1\) where a block is empty.

**4. Sufficiency and sharpness.** For \(\lambda\ge\max\{k,n-k\}\), necessarily \(\lambda\ge1\). The bounds in Step 3 give
\[
y_{(k)}\ge\frac1{n-k+1}\ge\frac1{1+\lambda},
\qquad y_{(k+1)}\le\frac{k}{k+1}\le\frac\lambda{1+\lambda}.
\]
By Step 2 every \(y\in P_{n,k}\) is covered, proving convexity.

Conversely, if \(0<\lambda<k\), the rank witness \(y^{\mathrm{rank}}\) cannot be covered: every \(k\)-subset \(I\) leaves at least one of the \(k+1\) equal positive coordinates unselected, where \((1+\lambda)y_i>\lambda\), contradicting the required bound \(z_i\le1\). If \(0<\lambda<n-k\), the corank witness \(y^{\mathrm{corank}}\) cannot be covered: every \(k\)-subset selects at least one of its \(n-k+1\) small coordinates, where \((1+\lambda)y_i<1\), contradicting \(z_i\ge0\). At least one of these obstructions applies whenever \(\lambda<\max\{k,n-k\}\). The endpoint itself is covered, so the infimum in the definition of \(c\) is attained and equals \(\max\{k,n-k\}\).

Finally, for \(\lambda\ge1\), the two strict-failure regions are disjoint because \(y_{(k)}\ge y_{(k+1)}\) and \(1/(1+\lambda)\le\lambda/(1+\lambda)\). Step 3 proves that their emptiness thresholds are exactly \(n-k\) and \(k\) respectively. The normalization \(\eta(P)=1/(1+c(V(P)))\) yields the displayed vertex-generation parameter.

## Verification
A standalone exact-rational Python program, `verification/check.py`, independently compares brute-force vertex-copy membership with the order-statistic criterion over hypersimplex rational grids for \(3\le n\le7\), several denominators, and seven values of \(\lambda\). It also tests the two sharp witnesses and the asserted threshold for \(3\le n<25\) and deterministic rational convex combinations for \(3\le n\le11\). The program completed **239,672** assertions. These finite computations support implementation and normalization; the proof above establishes every real parameter and all dimensions analytically. To reproduce, run `python verification/check.py` in the extracted package directory (standard Python library only).

## Relationship to prior work
Mark Meyer's *Finite convexification by Minkowski summation* (arXiv:2610.26744v1, first posted 19 October 2026) supplies general exposed-face criteria for whether a compact set becomes convex after addition of a large convex body. It does not determine the sharp numerical value or pointwise coverage phase diagram for the vertices of uniform-matroid base polytopes. Artstein-Avidan, Falah, and Slomka's *Vertex generated polytopes* (arXiv:2407.20604v1, first posted 30 July 2024) introduces the equivalent vertex-generation normalization and proves general bounds, a simplex equality statement, and necessary face restrictions. Those facts are used as context; the new claim is an exact all-rank hypersimplex computation, including both sharp obstruction mechanisms. Meyer's 2025 Schneider-index article studies fractional subadditivity and general sumsets, not this exact family. Jevtić, Timotijević, and Živaljević (arXiv:2504.21345v1) study Minkowski indecomposability of median hypersimplices, which is a different property of their convex bodies. Older unindexed equivalent computations remain a possible historical-priority risk.

## Limitations
The theorem is about the vertex sets of *uniform* matroid base polytopes, not arbitrary matroid base polytopes, rank-selected Boolean polytopes, or arbitrary compact subsets of hypersimplices. The two-phase description is only stated for \(\lambda\ge1\), although the exact global index is for all positive \(\lambda\). The work does not establish a Hausdorff-deficit, uncovered-volume formula, or general coverage stability estimate. Finite tests are not universal proof, and novelty is not independently certified.

## References
1. M. Meyer, *Finite convexification by Minkowski summation*, arXiv:2610.26744v1, first posted 2026-10-19. https://arxiv.org/abs/2610.26744
2. S. Artstein-Avidan, T. Falah, B. A. Slomka, *Vertex generated polytopes*, arXiv:2407.20604v1, first posted 2024-07-30. https://arxiv.org/abs/2407.20604
3. M. Meyer, *Measuring the convexity of compact sumsets with the Schneider non-convexity index*, Journal of Inequalities and Applications 2025, article 103. DOI:10.1186/s13660-025-03356-w. Earliest preprint arXiv:2405.00221, posted 2024-04-30.
4. F. D. Jevtić, M. Ž. Timotijević, R. T. Živaljević, *Indecomposability of the median hypersimplex and polytopality of the hemi-icosahedral Bier sphere*, arXiv:2504.21345v1, posted 2025-04-30.
