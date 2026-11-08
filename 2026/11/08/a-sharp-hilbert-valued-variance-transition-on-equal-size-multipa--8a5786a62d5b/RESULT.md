# A sharp Hilbert-valued variance transition on equal-size multipartite metrics

## Finding

Fix integers \(r\ge3\) and \(m\ge2\). Divide \(N=rm\) points into \(r\) classes of \(m\) points each; put distance \(t\in(0,2]\) between distinct points in a common class and distance \(1\) between points in different classes. Equip the points with uniform probability. For maps \(F\) into any real Hilbert space, write
\[
\mathcal S_H(r,m,t)=\sup_{\operatorname{Lip}(F)\le1}\frac1{rm}\sum_x\|F(x)-\overline F\|^2,\qquad \overline F=\frac1{rm}\sum_x F(x).
\]
Then the sharp Hilbert-valued Lipschitz variance is
\[
\boxed{\mathcal S_H(r,m,t)=\min\left\{\frac12,\frac{r-1}{2r}+\frac{(m-1)t^2}{2mr}\right\}.}
\]
The two branches meet exactly at \(t_*=\sqrt{m/(m-1)}\), independently of \(r\). For \(0<t\le t_*\), **all** maximizers are isometric embeddings of this finite metric, up to Hilbert-space isometry and translation. Their minimal affine dimensions are \(rm-1\) if \(t<t_*\), and \(r(m-1)\) if \(t=t_*\).

For \(t>t_*\), every maximizer, after subtracting its common class centroid, has classwise mean zero, every point has squared norm \(1/2\), vectors from different classes are orthogonal, and intraclass distances are at most \(t\). These conditions are also sufficient. In particular, at the complete-multipartite graph metric \(t=2\), the least Euclidean dimension in which a maximizer exists is \(r\) when \(m\) is even and \(2r\) when \(m\) is odd.

## Assumptions and scope

The scalar field of each target Hilbert space is real. The domain is a finite metric space with positive within-class distance \(t\le2\) and cross-class distance \(1\); the bound \(t\le2\) ensures the triangle inequality. Each of the \(rm\) distinct points has probability \(1/(rm)\). The supremum is over all Hilbert target spaces and all nonexpansive maps \(F\), with no a priori bound on target dimension. Only the **Hilbert-valued** variance is asserted; scalar-valued spread is a different functional and need not equal the formula above.

Index the points by \((i,a)\), with \(1\le i\le r\) and \(1\le a\le m\). Let the class centroids be \(c_i=m^{-1}\sum_a F(i,a)\), the grand centroid be \(c=r^{-1}\sum_i c_i\), the within-class variances be \(A_i=m^{-1}\sum_a\|F(i,a)-c_i\|^2\), and define \(A=r^{-1}\sum_i A_i\), \(B=r^{-1}\sum_i\|c_i-c\|^2\). The total variance is \(A+B\).

## Proof

**Two exact upper bounds.** For any two distinct classes \(i,j\), averaging squared cross-distances gives
\[
\frac1{m^2}\sum_{a,b}\|F(i,a)-F(j,b)\|^2=A_i+A_j+\|c_i-c_j\|^2\le1.
\]
Summing this over all unordered class pairs, and using \(\sum_{i<j}\|c_i-c_j\|^2=r^2 B\), yields
\[
(r-1)A+rB\le\frac{r-1}{2}.
\]
It follows that
\[
A+B\le\frac12-\frac B{r-1}\le\frac12,
\qquad
A+B\le\frac{r-1}{2r}+\frac Ar.
\]
Within each class, the pairwise-variance identity and the Lipschitz constraint give
\[
A_i=\frac1{m^2}\sum_{a<b}\|F(i,a)-F(i,b)\|^2
\le\frac{m-1}{2m}t^2=:C.
\]
Thus \(A\le C\), proving both branches of the proposed upper bound. Both inequalities are sharp, as the constructions below show.

An exact nonnegative deficit identity, valid for every admissible map, is
\[
\frac12-(A+B)=\frac B{r-1}+\frac1{r(r-1)m^2}
\sum_{i<j}\sum_{a,b}\bigl(1-\|F(i,a)-F(j,b)\|^2\bigr).
\]
In particular, equality in the universal one-half bound forces a common class centroid and forces **every** cross-distance to equal one. Equality in the second bound forces \(A=C\), so **every** intraclass distance equals \(t\), as well as saturation of every cross-distance. The latter equality condition is therefore exactly metric isometry.

**An isometric configuration up to the transition.** For \(0<t\le t_*\), set \(C=(m-1)t^2/(2m)\le1/2\). In mutually orthogonal subspaces, choose centered regular \(m\)-simplices \(u_{ia}\) of within-class squared distances \(t^2\) and squared vertex norms \(C\). In another orthogonal subspace, choose a centered regular \(r\)-simplex of class centroids \(v_i\), with squared between-centroid distances \(1-2C\), which is nonnegative. Define \(F(i,a)=v_i+u_{ia}\). Then every intraclass distance is \(t\) and every cross-distance is exactly \(1\). Hence the map is an isometric embedding attaining the second upper bound. At \(t=t_*\), the centroid simplex collapses to zero and both branches meet.

**The plateau and its equality geometry.** For \(t\ge t_*\), choose centered regular \(m\)-simplices, each of squared vertex norm \(1/2\), embedded in mutually orthogonal subspaces. Their within-class pairwise distances equal \(t_*\le t\), and their cross-class distances equal one. The resulting variance is exactly \(1/2\), establishing the plateau.

Suppose now a map attains variance \(1/2\). The deficit identity forces \(B=0\) and all cross-distances to equal one. Translate the common centroid to zero, so every class individually has zero centroid. Fix \(i\ne j\), and average \(\|F(i,a)-F(j,b)\|^2=1\) over \(b\). This gives \(\|F(i,a)\|^2+A_j=1\) for every \(a\). Hence squared norms are constant inside each class, with value \(A_i\). The cross-distance average gives \(A_i+A_j=1\) for every \(i\ne j\); since \(r\ge3\), these equations force \(A_i=1/2\) for every class. The original cross-distance equality now gives \(\langle F(i,a),F(j,b)\rangle=0\) for all \(i\ne j\) and all \(a,b\). This proves both necessity and sufficiency of the stated plateau characterization. At the boundary \(t=t_*\), the intraclass upper bound is also tight, so all pairwise intraclass distances equal \(t_*\), recovering isometry.

**Sharp affine dimensions.** The centered Gram matrix of any isometric realization is determined by its squared-distance matrix. For \(0<t<t_*\) it is the orthogonal sum of (i) \(r\) centered regular \(m\)-simplex Gram blocks, each of rank \(m-1\), and (ii) a positive centered regular \(r\)-simplex Gram block of rank \(r-1\). Its rank is therefore \(r(m-1)+r-1=rm-1\). At \(t=t_*\), block (ii) vanishes and the rank is \(r(m-1)\). An isometric realization is unique up to Hilbert-space congruence since its full centered Gram matrix is fixed by all pair distances. Thus the ranks are necessary as well as attainable.

At \(t=2\), the plateau characterization decomposes the target as an orthogonal sum of its class spans. Every class contains \(m\) vectors of identical nonzero norm \(1/\sqrt2\) whose sum is zero. A one-dimensional class span is possible precisely when \(m\) is even, by taking equal numbers of the two antipodal vectors. For odd \(m\), one dimension cannot have zero sum, while a regular \(m\)-gon on the circle of radius \(1/\sqrt2\) provides a two-dimensional class span with pairwise distances at most \(\sqrt2<2\). Orthogonality of class spans therefore gives the exact minimum \(r\) for even \(m\) and \(2r\) for odd \(m\), concluding the proof.

## Verification

`check_hilbert_clusters.py` uses only the Python standard library and exact rational arithmetic. It constructs centered Gram matrices for the isometric and plateau regimes, uses their positive-semidefinite orthogonal-projection decomposition in the proof, and checks their entries and pairwise distances, checks the sharp rational formulas in 288 parameter instances, verifies 1,200 independently generated nonexpansive coordinate maps against the bound, and tests the rank transition. The final successful marker is `ALL_CLUSTER_HILBERT_SPREAD_CHECKS_OK`. The computation covers finitely many rational squared parameters and is not presented as proof of the infinite-parametric theorem; the argument above is the proof.

## Relationship to prior work

Addario-Berry, Janson and McDiarmid (2009) studied the **real-scalar** graph spread, namely the largest variance of a real-valued one-Lipschitz function. It does not give the Hilbert-valued formula here, whose maximizers can require target dimension growing linearly with the number of points. Robertson (2023), Theorem 4.3, studied Hilbert distortion and negative type for **two** classes (balanced complete bipartite graph snowflakes). That result contains the threshold corresponding to \(t_*\) for its two-class embedding problem. The occurrence of this threshold for two classes, the regular-simplex construction, and general Euclidean distance-matrix methods are not claimed as new. The present theorem concerns \(r\ge3\) and establishes a different variational invariant together with a complete family of equality conditions, exact rank collapse, and the graph-metric parity law for least maximizing dimension.

Higashitani, Jochemko and Michałek (2018) classify facets for symmetric edge polytopes; the strict-interpolation facet formula has also been established for complete-multipartite Lipschitz-free balls. Those works concern **real-valued Lipschitz polytopes and facet enumeration**, rather than maximizing Hilbert-valued variance. Results on within-cluster projection constants likewise measure linear projection norms, not this variance envelope. Das and Mohanty (2020) calculate spectral properties of squared-distance matrices for complete multipartite **graph metrics**; the existence and inertia of a fixed squared-distance matrix do not establish the extremal variance of all admissible Hilbert embeddings across the entire interval of \(t\), nor the plateau equality classification. Closely related finite-dimensional negative-type and graph-spectral approaches remain a plausible source of equivalent formulations; the bibliographic search cannot rule out unindexed equivalences.

## Limitations

The result assumes equal class sizes and uniform masses, a common within-class distance, and common cross-class unit distance; it does not determine arbitrary asymmetric multipartite metrics or general probability weights. The complete plateau family is classified by geometric conditions, but minimum target dimension is calculated only at the isometric phase and at \(t=2\), not for all intermediate plateau values. The theorem is Hilbert-valued and does not assert the same scalar spread. It supplies a proof and reproducible exact finite tests, but has not received independent mathematical validation. Equivalent results in unindexed Euclidean distance geometry literature remain a bibliographic risk.

## References

1. L. Addario-Berry, S. Janson and C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156v1, first public 6 February 2009, https://arxiv.org/abs/0902.1156.
2. G. Robertson, *Negative type and bi-Lipschitz embeddings into Hilbert space*, arXiv:2309.16070v1, first public 27 September 2023, especially Theorem 4.3, https://arxiv.org/abs/2309.16070.
3. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1, 20 July 2018, especially Proposition 3.5, https://arxiv.org/abs/1807.07678.
4. A. Das and A. Mohanty, *On Squared Distance Matrix of Complete Multipartite Graphs*, arXiv:2012.04341v1, 8 December 2020, https://arxiv.org/abs/2012.04341.
