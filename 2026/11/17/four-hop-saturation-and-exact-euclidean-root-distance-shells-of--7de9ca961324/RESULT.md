# Four-hop saturation and exact Euclidean root-distance shells of cycle symmetric edge polytopes

## Finding
For each integer \(n\ge4\), write \(e_0,\ldots,e_{n-1}\) for the standard basis in \(\mathbb R^n\), with subscripts interpreted modulo \(n\). Set
\[
P_n=\operatorname{conv}\{e_i-e_{i+1},e_{i+1}-e_i:0\le i<n\},\qquad
Q_n=\operatorname{conv}\{e_i-e_j:i\ne j\}.
\]
Thus \(P_n\) is the symmetric edge polytope of the cycle, and \(Q_n\) is the complete type-\(A\) root polytope. Both are embedded in the same zero-sum Euclidean hyperplane with its inherited, unrescaled inner product.

**Theorem (one exact distance-shell law).** For every ordered pair of distinct indices \(i,j\), let \(d=\min\{(j-i)\bmod n,(i-j)\bmod n\}\). Then
\[
\operatorname{dist}_2(e_i-e_j,P_n)^2=\begin{cases}
0&d=1,\\
\tfrac12&d=2,\\
\tfrac8{11}&d=3,\\
\tfrac34&d\ge4.
\end{cases}
\]
Each projection is unique, and an explicit convex combination of at most five signed cycle-edge roots realizing it is given below. For each \(d<n/2\), the corresponding shell has \(2n\) ordered roots; the antipodal-distance shell for even \(n\), \(d=n/2\), contains \(n\) ordered roots. In particular,
\[
d_H(Q_n,P_n)^2=\begin{cases}\tfrac12&4\le n\le5,\\ \tfrac8{11}&6\le n\le7,\\ \tfrac34&n\ge8.\end{cases}
\]
The farthest-point locus of the **whole** polytope \(Q_n\) consists exactly of the roots with \(d=\lfloor n/2\rfloor\) for \(n\le7\), and with \(d\ge4\) for \(n\ge8\); no nonvertex points are farthest. The numbers of such farthest points are respectively \(n(n-3)\), \(n(n-5)\), and \(n(n-7)\) in these three ranges.

The squared distance ceases to distinguish cyclic separations once four edges intervene, while the path analogue has a different sharp threshold and farthest-point behavior.

## Assumptions and scope
Only standard Euclidean distance is used, not graph shortest-path distance, a transport norm, or a normalized Hausdorff distance. The indexing convention is \(0,\ldots,n-1\) cyclically. The chosen arc orientation below can be arbitrary at the even antipodal tie; either choice yields a valid projection certificate. Results apply to the entire continuous containing polytope, not only its root vertices. They do not imply analogous formulas for weighted cycles or other norms.

## Proof
Let \(x=e_i-e_j\). For any vector \(r\) define the support function of the cycle polytope by
\[
h_{P_n}(r)=\max_{k\in\mathbb Z/n\mathbb Z}|r_k-r_{k+1}|.
\]
The elementary Euclidean projection criterion is that a point \(y\in P_n\) is the (necessarily unique) metric projection of \(x\) precisely when
\[
\langle x-y,y\rangle=h_{P_n}(x-y).
\]
Indeed, with \(r=x-y\), this equality is equivalent to \(\langle r,z-y\rangle\le0\) for every \(z\in P_n\), which is the first-order optimality condition for squared Euclidean distance. In all cases below \(y\) is explicitly a convex combination of signed cycle-edge roots, and the stated equality is verified coordinatewise.

**Distance one.** If \(d=1\), then \(x\) itself is a cycle-edge root. Put \(y=x\), so \(r=0\).

**Distance two.** Choose a two-edge arc \(i\to a\to j\). Put
\[
y=\tfrac12(e_i-e_a)+\tfrac12(e_a-e_j)=\tfrac12(e_i-e_j).
\]
Then \(r=\tfrac12(e_i-e_j)\), \(\|r\|^2=1/2\), and both \(h_{P_n}(r)\) and \(\langle r,y\rangle\) equal \(1/2\). This includes the two-path tie when \(n=4\).

**Distance three.** Choose a shorter cyclic direction \(s\in\{-1,1\}\) such that \(j=i+3s\) modulo \(n\). Define five signed edge roots
\[
A=e_i-e_{i+s},\quad B=e_{i+s}-e_{i+2s},\quad C=e_{i+2s}-e_j,\quad D=e_i-e_{i-s},\quad E=e_{j+s}-e_j.
\]
Set
\[
y=\tfrac1{11}(3A+B+3C+2D+2E).
\]
The weights are nonnegative and sum to one. Because \(n\ge6\), the residual \(r=x-y\) has values \(6/11\) at \(i\), \(-6/11\) at \(j\), \(2/11\) at \(i+s,i-s\), \(-2/11\) at \(j-s,j+s\), and zero elsewhere; the six displayed positions are distinct even when \(n=6\). Consequently
\[
\|r\|^2=2(6/11)^2+4(2/11)^2=\tfrac8{11},\quad
h_{P_n}(r)=\tfrac4{11}=\langle r,y\rangle.
\]
Every adjacent residual difference has absolute value at most \(4/11\), including at the possible antipodal tie.

**Distance at least four.** Define
\[
y=\tfrac14\big[(e_i-e_{i-1})+(e_i-e_{i+1})+(e_{j-1}-e_j)+(e_{j+1}-e_j)\big].
\]
The neighborhoods \(\{i,i\pm1\}\) and \(\{j,j\pm1\}\) are disjoint, and there is no edge directly joining their positive and negative neighbor values, since both cyclic paths from \(i\) to \(j\) have length at least four. The residual \(r=x-y\) equals \(1/2\) at \(i\), \(-1/2\) at \(j\), \(1/4\) at \(i\pm1\), \(-1/4\) at \(j\pm1\), and zero elsewhere. Therefore
\[
\|r\|^2=2(1/2)^2+4(1/4)^2=\tfrac34,\quad
h_{P_n}(r)=\tfrac14=\langle r,y\rangle.
\]
The projection criterion proves the shell formulas and uniqueness in each case.

**Counting and continuous extremizers.** Cyclic symmetry gives \(2n\) ordered roots at each nonantipodal distance and \(n\) at the antipodal distance. Since \(P_n\subseteq Q_n\), the directed Hausdorff distance is \(\max_{x\in Q_n}\operatorname{dist}(x,P_n)\); convexity of distance attains this maximum at a root. To rule out nonvertex ties, suppose \(x=\sum_t\lambda_t x_t\) is a convex combination of roots, and write \(y_t=\Pi_{P_n}(x_t)\), \(r_t=x_t-y_t\). Then
\[
\operatorname{dist}(x,P_n)^2\le\Big\|\sum_t\lambda_t r_t\Big\|^2
=\sum_t\lambda_t\|r_t\|^2-\tfrac12\sum_{s,t}\lambda_s\lambda_t\|r_s-r_t\|^2.
\]
Every positive-distance residual described above has a unique strictly greatest coordinate at its positive root endpoint and a unique strictly least coordinate at its negative endpoint. Thus two distinct ordered roots in any maximum-distance shell have distinct residual vectors. Equality with the global maximum is possible only when one root has weight one. The claimed complete farthest-point classification and counts follow.

## Verification
A standalone standard-library exact-rational checker, `verify_cycle_root_shells.py`, reconstructs every displayed convex combination and tests the support certificate against every signed cycle edge. It exhausts **8,982** ordered roots for \(4\le n\le30\), then tests both directions of every separation for \(31\le n\le200\) (9,775 instances in each direction). It also checks distance-shell maxima, multiplicities, and the strict endpoint residual maxima. The checker reports `CYCLE_ROOT_PROJECTION_PASS`.

A separate numerical convex quadratic-program check independently optimized 302 projections at cycle sizes \(4\) through \(12\), agreeing with the rational formulas with maximum squared-distance discrepancy below \(1.5\cdot10^{-13}\). The infinite-dimensional conclusion rests on the symbolic projection and convexity arguments, not finite computation.

## Relationship to prior work
The standard symmetric edge polytope and its facet/arithmetic theory are given in Higashitani--Jochemko--Michałek (2018). D'Alì--Delucchi--Michałek (2019) develop graph classes, combinatorics, and Kantorovich--Rubinstein interpretations. Jevtić--Timotijević--Živaljević (2018) study weighted-cycle Kantorovich--Rubinstein polytopes and Bier-sphere boundaries. The present Euclidean metric projection onto the **unweighted cycle-edge hull from the complete-root hull** is a different invariant from intrinsic facet counts, cycle transportation distances, and the metric projection of a single deleted cycle vertex. The known path-graph approximation law yields an upper bound under cycle-edge inclusion but not this equality, its three positive shells, or its complete extremizers.

## Limitations
The bibliographic originality assessment is provisional and subject to earlier equivalent formulations. The exact proof is limited to unit cycle-edge root coordinates and the Euclidean norm. A comparison with all possible earlier unpublished or inaccessible works was not established. The computational tests cover finite ranges only; no independent mathematical audit has been performed.

## References
1. A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678 (first posted 2018-07-20), https://arxiv.org/abs/1807.07678.
2. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193 (first posted 2019-10-11), https://arxiv.org/abs/1910.05193.
3. F. D. Jevtić, M. Timotijević, R. T. Živaljević, *Polytopal Bier spheres and Kantorovich–Rubinstein polytopes of weighted cycles*, arXiv:1812.00397 (first posted 2018-12-02), https://arxiv.org/abs/1812.00397.
