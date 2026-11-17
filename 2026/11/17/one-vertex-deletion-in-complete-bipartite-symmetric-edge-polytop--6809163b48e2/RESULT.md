# One-vertex deletion in complete-bipartite symmetric-edge polytopes: a metric contact transition and exact volume loss

## Finding
For integers \(p,q\ge2\), let \(n=p+q\), let \(L=[p]\), \(R=\{p+1,\ldots,p+q\}\), and consider the intrinsic Euclidean polytope
\[
P_{p,q}=\operatorname{conv}\{\pm(e_i-e_j):i\in L,\ j\in R\}\subset\{x\in\mathbb R^n:\sum_i x_i=0\}.
\]
Remove the single signed vertex \(v=e_1-e_{p+1}\), retaining its negative and every other signed root, and call the resulting polytope \(P'_{p,q}\). Then the squared directed Hausdorff distance and squared distance of \(v\) to \(P'_{p,q}\) coincide and equal
\[
\operatorname{dist}(v,P'_{p,q})^2=
\begin{cases}
\dfrac{4(p+q)}{pq+4(p+q)},&pq\le2(p+q),\\[4pt]
\dfrac{pq}{2pq-p-q},&pq\ge2(p+q).
\end{cases}
\]
The two expressions agree at equality. The metric projection is unique. When \(pq<2(p+q)\), it belongs to the relative interior of a facet of the deleted polytope containing \((p-1)+(q-1)+(p-1)(q-1)\) vertices. At equality, the projection lies in a proper subface of that facet, although the full facet is the exposed contact set. When \(pq>2(p+q)\), it lies in the relative interior of an \((n-3)\)-simplex, which is exactly its exposed contact face. Thus the exposed-contact dimension drops from \(n-2\) to \(n-3\) strictly after the threshold. The integer threshold cases satisfy \((p-2)(q-2)=4\).

For the root lattice \(\Lambda=\mathbb Z^n\cap\{\sum x_i=0\}\), normalized \((n-1)\)-volume means \((n-1)!\operatorname{vol}_{n-1}(K)/\sqrt n\). Put \(m=p-1\), \(k=q-1\), and define
\[
\begin{aligned}
T_{p,q}&=\frac{2}{m!k!}\sum_{i=0}^{m}\sum_{j=0}^{k}
\binom mi^2\binom kj^2(i+j)!(m+k-i-j)!,\\
E_{p,q}&=\frac{2}{(m-1)!(k-1)!}\sum_{i=0}^{m-1}\sum_{j=0}^{k-1}
\binom{m-1}i^2\binom{k-1}j^2i!j!(m+k-2-i-j)!.
\end{aligned}
\]
Then the original normalized volume is \(T_{p,q}\), and the **exact normalized volume lost after deletion** is \(E_{p,q}\). Consequently the relative loss is \(E_{p,q}/T_{p,q}\). Both are positive integers. In particular, for \(p=2\) and \(q\ge2\),
\[
T_{2,q}=(q+1)2^q,\qquad E_{2,q}=2^{q-1},\qquad E_{2,q}/T_{2,q}=\frac1{2(q+1)}.
\]
The case \(p=2\) is symmetric to \(q=2\).

## Assumptions and scope
All measures and distances use the canonical Euclidean embedding in the zero-sum hyperplane; the normalized-volume convention above is not a polar volume. A **single oriented** root is removed: this is different from deleting an undirected graph edge, which removes both orientations. The assertions hold for every pair of integers \(p,q\ge2\), without an asymptotic or genericity assumption. The normalized-volume formula counts the volume of the removed cap, not lattice points or the polar volume.

## Proof
**1. Exact cap description.** Write \(Q=\operatorname{conv}\{e_i-e_j:i\in L,j\in R\}\), the affine product of a \((p-1)\)-simplex and a \((q-1)\)-simplex. Then \(P=\operatorname{conv}(Q,-Q)\). Every point of \(P\) has a representation
\[
x=s(a,-c)+(1-s)(-b,d),\quad a,b\in\Delta_{p-1},\ c,d\in\Delta_{q-1},\quad 0\le s\le1,
\]
where coordinates are ordered as \(L,R\), and \(s=(1+\sum_{i\in L}x_i)/2\) is uniquely determined by \(x\). In \(Q\), deleting \(v\) truncates exactly the product-simplex corner \((a_1,c_1)=(1,1)\); its remaining-vertex hull is \(a_1+c_1\le1\). Put \(z=-x|_R\). For fixed \(x\) in the original slice, the smallest attainable top weights are \(a_1=(x_1)_+/s\) and \(c_1=(z_1)_+/s\) when \(s>0\): the other coordinates can absorb all unused top weight because both color classes have at least two vertices. Each of \(x_1,z_1\) is at most \(s\). Thus the removed-vertex hull is exactly
\[
P'=P\cap\{x:x_1-x_{p+1}\le s(x)\}.
\]
The cutting hyperplane \(H\) is \(x_1-x_{p+1}=s(x)\). The cap is the pyramid with apex \(v\) and base \(F=P\cap H\). Its base is
\[
F=\operatorname{conv}(\{A_j=e_1-e_{p+j}:2\le j\le q\}\cup
\{B_i=e_i-e_{p+1}:2\le i\le p\}\cup
\{C_{ij}=e_{p+j}-e_i:2\le i\le p,2\le j\le q\}).
\]
The top and bottom slices have different values of \(s\), and the top vertices span an \((n-3)\)-simplex. Hence \(F\) has dimension \(n-2\) and is a facet of \(P'\).

**2. Projection and contact transition.** Let \(\bar A,\bar B,\bar C\) denote the respective averages of the three displayed root classes. Set
\[
g=\operatorname{proj}_{\sum x_i=0}\!\left(e_1-e_{p+1}-\tfrac12\sum_{i\in L}e_i\right),\qquad
\|g\|^2=1+\frac{pq}{4n}.
\]
The orthogonal projection of \(v\) onto \(H\) is \(z_H=v-g/\|g\|^2\), with decomposition
\[
z_H=\alpha\bar A+\beta\bar B+\gamma\bar C,\quad
(\alpha,\beta,\gamma)=\frac{(q(p+2),\ p(q+2),\ 2n-pq)}{pq+4n}.
\]
When \(pq\le2n\), these weights are nonnegative, so \(z_H\in F\); because all of \(P'\) lies on the opposite side of \(H\) from \(v\), this is its metric projection. The squared distance is \(1/\|g\|^2=4n/(pq+4n)\). Positive coefficients give relative interior membership and all vertices of \(F\) as contacts when \(pq<2n\); at equality \(\gamma=0\) but the normal is still perpendicular to the whole facet.

When \(pq>2n\), define
\[
\alpha_0=\frac{p(q-1)}{2pq-n},\quad\beta_0=\frac{q(p-1)}{2pq-n},\quad
z_0=\alpha_0\bar A+\beta_0\bar B.
\]
Then \(\alpha_0+\beta_0=1\), \(\|v-z_0\|^2=pq/(2pq-n)\), and the residual \(r=v-z_0\) satisfies \(r\cdot A_j=r\cdot B_i=(pq-n)/(2pq-n)\). For every \(C_{ij}\),
\[
r\cdot C_{ij}-r\cdot A_j=\frac{2n-pq}{2pq-n}<0.
\]
Every other surviving signed root has no larger residual scalar product: their values are respectively the negatives of these class values or \(-1\) for \(-v\); positive \(e_i-e_{p+j}\) with \(i,j\ne1\) also has the negative of the \(C\)-class value. Hence \(r\cdot(w-z_0)\le0\) for each vertex \(w\in P'\), the exact convex-projection criterion. Only the \(A\) and \(B\) classes attain equality. The \(n-2\) contact points are affinely independent, giving the stated simplex. Strict convexity of squared distance gives uniqueness in every regime.

For any \(x\in P=\operatorname{conv}(v,P')\), convexity of distance to \(P'\) bounds it above by \(\operatorname{dist}(v,P')\). Thus the directed Hausdorff distance from \(P\) to \(P'\) equals the distance at \(v\).

**3. Volume computation.** Let \(d=n-1=m+k+1\). In lattice coordinates obtained by omitting one ambient coordinate, the slice at \(s\) of \(P\) is the product of two simplex-difference bodies \(s\Delta_{m}-(1-s)\Delta_m\) and \(s\Delta_k-(1-s)\Delta_k\), where \(\Delta_m\) has \(m+1\) vertices. The classical simplex mixed-volume identity is
\[
\operatorname{vol}_{\rm coord}(a\Delta_r-b\Delta_r)=\frac1{r!}\sum_{i=0}^{r}\binom ri^2 a^i b^{r-i}.
\]
The coordinate Jacobian from the variable \(s\) is \(2\). Integrating the product over \(0\le s\le1\), expanding, and using the beta integral yields \(d!\operatorname{vol}_{\rm coord}(P)=T_{p,q}\).

For the base \(F\), write \(t=1-s\) and assign weight \(\lambda\) to its top \(B\)-class, weight \(1-\lambda\) to the top \(A\)-class, and weight \(t\) to its bottom \(C\)-class. Holding \(s,\lambda\) fixed, its remaining coordinates form the product
\[
(s\lambda\Delta_{m-1}-t\Delta_{m-1})\times
(s(1-\lambda)\Delta_{k-1}-t\Delta_{k-1}).
\]
The free-sum coordinate on \(F\) changes by \(s\,d\lambda\), and the full root-lattice-coordinate Jacobian contributes \(2\,ds\). Since the cap is a pyramid of unit lattice height over \(F\), its coordinate volume is \(1/d\) times the base coordinate volume. Therefore
\[
\operatorname{vol}_{\rm coord}(P\setminus P')=
\frac2{d(m-1)!(k-1)!}
\int_0^1\!\int_0^1 s\!
\sum_{i=0}^{m-1}\binom{m-1}{i}^2(s\lambda)^i t^{m-1-i}
\sum_{j=0}^{k-1}\binom{k-1}{j}^2(s(1-\lambda))^j t^{k-1-j}\,d\lambda\,ds.
\]
Apply \(\int_0^1\lambda^i(1-\lambda)^j d\lambda=i!j!/(i+j+1)!\) and \(\int_0^1s^{i+j+1}(1-s)^{m+k-2-i-j}ds=(i+j+1)!(m+k-2-i-j)!/(m+k)!\). Multiplying by \(d!\) yields \(E_{p,q}\). For \(p=2\), elementary binomial summation gives the special formulas above.

## Verification
The standalone `deletion_checker.py` contains exact rational projections and checks the first-order inequality against every remaining signed root for \(2\le p,q\le17\) (256 pairs). It evaluates the two exact integer-volume sums and their positivity, checks the explicit \(p=2\) identities, and independently computes convex hull volumes for 11 small parameter pairs using SciPy. Expected success output: `BICLIQUE_SIGNED_ROOT_DELETION_PASS exact_profiles=256 independent_hulls=11 threshold=pq-2(p+q)`. The proof covers all parameters; finite checks are corroboration, not an exhaustive proof.

## Relationship to prior work
Higashitani, Jochemko and Michałek derived facets, unimodular triangulations, the Ehrhart numerator, and volumes of the **original** complete-bipartite symmetric-edge polytopes, including their facets. D'Alì, Delucchi and Michałek studied the same class and its relation to metric fundamental polytopes; Chen, Davis and Korchevskaia classified face subgraphs. Awasthi, Kalantari and Zhang used vertex-to-remaining-hull distance as a robustness quantity. These results motivate the object and the invariant and are not claimed here as new. The assertions here instead concern the truncated body obtained by removing only one orientation, its sharp metric-projection transition, and the exact lost cap volume. No independent literature-priority certification is asserted.

## Limitations
The analysis removes one oriented root, not an undirected graph edge or an arbitrary set of roots. It does not classify the entire face lattice or Ehrhart polynomial of the truncated polytope. Historical equivalence in literature on deleted lattice-polytope vertices or on metric root polytopes remains a risk. Independent mathematical review has not been performed.

## References
- P. Awasthi, B. Kalantari, and Y. Zhang, *Robust Vertex Enumeration for Convex Hulls in High Dimensions*, arXiv:1802.01515 (first public 2018-02-05).
- A. Higashitani, K. Jochemko, and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678 (first public 2018-07-20), especially Theorem 3.1, Proposition 3.4, and Section 4.
- A. D'Alì, E. Delucchi, and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193 (2019-10-11), especially Sections 2–4.
- T. Chen, R. Davis, and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315 (2021-07-26).
