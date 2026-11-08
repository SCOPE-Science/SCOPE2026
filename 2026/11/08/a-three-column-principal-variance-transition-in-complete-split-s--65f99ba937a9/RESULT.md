# A three-column principal-variance transition in complete-split spanning-tree polytopes

## Finding

For every pair of integers \(p,q\ge 2\), consider the complete-split graph \(G_{p,q}=K_p\vee\overline{K_q}\). Let \(X\in\{0,1\}^{E(G_{p,q})}\) be the edge-incidence vector of a uniformly selected spanning tree, and let \(C_{p,q}=\operatorname{Cov}(X)\), using the **standard Euclidean metric** of its edge coordinates. Put \(n=p+q\). This is also the covariance of the uniform distribution on vertices of the spanning-tree polytope.

For \(p=2\), the complete covariance spectrum, counting multiplicities, is
\[
0\ (1),\qquad \frac{2q+1}{(q+2)^2}\ (1),\qquad
\frac1{2(q+2)}\ (q-1),\qquad \frac{q+1}{2(q+2)}\ (q).
\]
The condition number on the affine tangent space is exactly \(q+1\).

For \(p\ge3\), define
\[
 Q=\frac{p-1}{pn},\quad T=\frac{2p+q-3}{pn},\quad
 V=\frac{p+2q-1}{n^2},\quad Y=\frac{2(n-1)}{n^2}
\]
and the symmetric matrix
\[
 B=\begin{pmatrix}
 \dfrac{p+2q}{n^2}&-\dfrac{\sqrt{q(p-2)}}{n^2}\\
 -\dfrac{\sqrt{q(p-2)}}{n^2}&\dfrac{2p^2+2pq-3p+q^2-q}{pn^2}
 \end{pmatrix}.
\]
Write \(B_-<B_+\) for its two eigenvalues. The **complete spectrum** is \(0\) (multiplicity 1), \(V\) (multiplicity 1), \(Q\) (multiplicity \(q-1\)), \(T\) (multiplicity \((p-1)(q-1)\)), \(Y\) (multiplicity \(p(p-3)/2\), absent for \(p=3\)), and \(B_-\), \(B_+\), each of multiplicity \(p-1\). At coinciding eigenvalues, multiplicities add. Every listed nonzero eigenvalue is positive.

**Sharp principal-variance transition.** For every \(p\ge3\), the smallest positive eigenvalue is always \(Q\). The largest is \(B_+\) when \(q=2\), is the tied value \(B_+=T\) when \(q=3\), and is \(T\) when \(q\ge4\). In particular, the largest-eigenvalue multiplicity is respectively \(p-1\), \(3(p-1)\), and \((p-1)(q-1)\). The transition occurs at **exactly three independent-set vertices**, independently of clique size.

Equivalently, the covariance condition number on \(\{x:\sum_e x_e=0\}\) is
\[
 \kappa(C_{p,q})=
 \begin{cases}
 q+1,&p=2,\\[3pt]
 \dfrac{(p+1)(3p+2)+\sqrt{(p-2)(p^3+4p^2+5p-2)}}{2(p-1)(p+2)},&p\ge3,\ q=2,\\[7pt]
 \dfrac{2p+q-3}{p-1},&p\ge3,\ q\ge3.
 \end{cases}
\]

## Assumptions and scope

The graph is simple and unweighted, with a clique of \(p\) vertices and an independent set of \(q\) vertices, all cross edges present. The probability distribution assigns equal mass to every spanning tree, equivalently to every distinct vertex of the graphic-matroid base polytope. Covariance is taken in the ambient edge-coordinate Euclidean structure; the constant vector is the sole null direction, because the spanning-tree polytope of a connected graph with no bridges has affine codimension one. No claims are made for \(p=1\), \(q=1\), nonuniform tree laws, or volume-uniform sampling on the polytope.

## Proof

**1. Transfer-current formula.** Choose an orientation for every edge and write \(b_e\) for the signed vertex-incidence vector. If \(L\) is the graph Laplacian, the matrix-tree polynomial \(\tau(\mathbf w)=\sum_{S\text{ spanning tree}}\prod_{e\in S}w_e\) has first and second logarithmic derivatives
\[
 \operatorname{Cov}(X_e,X_f)=\delta_{ef}K_{ee}-K_{ef}^{\,2},\qquad K_{ef}=b_e^{\top}L^+b_f,
\]
at all edge weights 1. This follows by differentiating the reduced determinant of the weighted Laplacian and Jacobi's identity. The right-hand side does not depend on the chosen edge orientations.

**2. Exact transfer currents.** Set \(n=p+q\). The Laplacian acts by \(n\) on clique-vertex contrasts, by \(p\) on independent-set contrasts, and by \(n\) on the one-dimensional contrast between the two vertex classes. Hence
\[
 L^+=\frac1n\left(I-\frac1nJ_n\right)+\left(\frac1p-\frac1n\right)\Pi_I,
\]
where \(\Pi_I\) is orthogonal projection onto the independent-set contrast subspace. Orient clique edges arbitrarily and all cross edges from clique to independent set. For cross edges \((i,j)\) and \((k,l)\), with \(i,k\) clique vertices and \(j,l\) independent vertices,
\[
 K_{(i,j),(k,l)}=\frac{\delta_{ik}}n+\frac{\delta_{jl}}p-\frac1{pn}.
\]
Two clique edges have transfer current \(\pm 1/n\) if incident and zero if disjoint, with diagonal \(2/n\). A clique edge and a cross edge have transfer current \(\pm 1/n\) exactly when their clique endpoints overlap.

**3. Covariance blocks.** Let \(c=\binom p2\). Let \(M\) be the \(p\times c\) *unsigned* clique-edge incidence matrix, and let \(R\) be the \(p\times pq\) row-incidence matrix of cross edges. In clique-edge versus cross-edge coordinates, the transfer-current formula gives
\[
 C_{CC}=\frac{2(n-1)I_c-M^{\top}M}{n^2},\qquad
 C_{CX}=-\frac{M^{\top}R}{n^2},
\]
\[
 C_{XX}=T I_{pq}-\frac{p-2}{pn^2}(I_p\otimes J_q)
 -\frac{n-2}{p^2n}(J_p\otimes I_q)-\frac1{p^2n^2}J_{pq}.
\]
Here \(J_d\) is the \(d\times d\) all-ones matrix. These identities include every entry, not only diagonal moments.

**4. Orthogonal diagonalization.** The identities \(MM^{\top}=(p-2)I_p+J_p\) and \(RR^{\top}=qI_p\) yield mutually orthogonal invariant spaces. Independent-set contrasts constant along clique rows give eigenvalue \(Q\), with dimension \(q-1\). Tensor products of clique and independent-set contrasts give \(T\), with dimension \((p-1)(q-1)\). The kernel of \(M\) in clique-edge coordinates gives \(Y\), with dimension \(p(p-3)/2\) for \(p\ge3\). The two simultaneous class-constant directions give eigenvalues \(0\) and \(V\). For \(p\ge3\), a fixed normalized clique contrast \(u\) couples the normalized clique-edge vector \(M^{\top}u/\sqrt{p-2}\) to the normalized cross-row vector \(R^{\top}u/\sqrt q\); the exact restricted matrix is \(B\). It occurs independently \(p-1\) times. These dimensions sum to \(\binom p2+pq\), so no eigenvalue is missing. When \(p=2\), the clique-edge contrast component vanishes; the unmatched cross-row contrast contributes a further copy of \(T\), giving the separately stated spectrum.

**5. Strict order and phase boundary.** For \(p\ge3\), direct simplification gives
\[
 T-Q=\frac{n-2}{pn}>0,\quad V-Q=\frac{q(p+1)}{pn^2}>0,\quad
 Y-Q=\frac{p^2+pq-p+q}{pn^2}>0,
\]
\[
 T-V=\frac{p(p-2)+q(p+q-3)}{pn^2}>0,\quad
 T-Y=\frac{p(q-1)+q(q-3)}{pn^2}>0.
\]
For the remaining coupled eigenvalues,
\[
 \det(B-QI)=\frac{p^2+pq^2+pq-2p+q^2}{p^2n^3}>0,
\qquad \operatorname{tr}(B- QI)=\frac{p^2+2pq-p+q^2+q}{pn^2}>0.
\]
Thus both eigenvalues of \(B\) exceed \(Q\). Finally,
\[
 \det(B-TI)=\frac{q(p-2)(q-3)}{p^2n^3},\qquad
 B_{22}-T=-\frac{q(p-2)}{pn^2}<0.
\]
At \(q=2\) the determinant is negative, so \(T\) lies strictly between \(B_-\) and \(B_+\). At \(q=3\) it is zero, and the second diagonal inequality shows \(B_+=T\). At \(q\ge4\) the determinant is positive; both diagonal entries are less than \(T\), whence \(B_+<T\). The condition-number formulas follow by dividing the appropriate maximum eigenvalue by \(Q\). For \(p=2\), the displayed three positive eigenvalues obey \(T>V>Q\), yielding \(q+1\). All inequalities hold over the complete stated integer domain, and no finite experimental cutoff enters this argument.

## Verification

The standalone `artifacts/verify.py` uses exact rational arithmetic. It constructs the full covariance matrix from the Laplacian pseudoinverse, independently enumerates all labeled spanning trees in nine small profiles, and compares all covariance entries with combinatorial first and second moments. It also compares complete predicted spectral first and second traces with the exact full covariance matrices on all 64 profiles \(2\le p,q\le9\), including the determinant sign governing the sharp phase. Its successful output is:

`SPLIT_TREE_COVARIANCE_CHECKS_PASSED profiles=64 trees=20219 enumerated_entries=1565`

Finite checks corroborate, but do not replace, the symbolic proof for arbitrary \(p,q\).

## Relationship to prior work

The underlying spanning-tree polytope and its vertex distribution are standard. Aprile, Fiorini, Huynh, Joret, and Wood study extended formulations of spanning-tree polytopes, not this covariance spectrum. General determinant/transfer-current methods, and algorithms for expectations under spanning-tree distributions, yield arbitrary pair probabilities but do not by themselves diagonalize this particular covariance or identify the universal three-column transition. Forest-containment formulas for complete multipartite graphs likewise can imply pair-inclusion probabilities; the present contribution is their **joint Euclidean covariance diagonalization and extremal-eigenspace transition**. Published related work on balanced complete multipartite spanning-tree polytopes concerns different part-size regimes, not the complete-split graph family here.

## Limitations

The result uses the standard unweighted graph and edge-coordinate normalization; it does not describe other metrics or measures. A 2023 paper on complete multipartite spanning-tree containment could be inspected only through publicly visible bibliographic information and abstract, not its full text, leaving a bounded historical-equivalence risk. A February 2026 preprint gives a general forest-containment formula that is stronger at the level of raw pair inclusion and must not be mistaken for evidence that raw moment computation is new. The originality assessment is provisional pending independent literature review. No independent mathematical audit has been performed.

## References

1. Aprile, Fiorini, Huynh, Joret, and Wood, *Smaller extended formulations for spanning tree polytopes in minor-closed classes and beyond*, arXiv:2106.11945 (first public posting 2021-06-22), https://arxiv.org/abs/2106.11945 .
2. Zmigrod, Vieira, and Cotterell, *Efficient Computation of Expectations under Spanning Tree Distributions*, *Transactions of the Association for Computational Linguistics* (2021), https://aclanthology.org/2021.tacl-1.41/ .
3. Li, Chen, and Yan, *Enumeration of spanning trees of complete multipartite graphs containing a fixed spanning forest*, *Journal of Graph Theory* (2023), https://doi.org/10.1002/jgt.22954 .
4. Wang and Ge, *On enumeration of spanning trees of complete multipartite graphs containing a fixed spanning forest*, arXiv:2602.03602 (2026), https://arxiv.org/abs/2602.03602 .
5. The classical matrix-tree theorem and the associated transfer-current determinantal formula, derived from the weighted Laplacian determinant in the proof above.
