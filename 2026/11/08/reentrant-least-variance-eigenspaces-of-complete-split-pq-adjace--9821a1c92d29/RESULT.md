# Reentrant least-variance eigenspaces of complete-split PQ adjacency polytopes

## Finding

For integers \(p,q\ge 2\), let \(G_{p,q}=K_p\vee\overline{K_q}\), the join of a clique on \(p\) vertices with an independent set on \(q\) vertices. Its PQ-type adjacency polytope is
\[
P_{p,q}=\operatorname{conv}\{(e_i,e_j)\in\mathbb R^{2(p+q)}:i=j\text{ or }\{i,j\}\in E(G_{p,q})\}.
\]
Here both orientations of every undirected edge are included. Choose \(X\) uniformly from the distinct vertices of \(P_{p,q}\), and let \(C=\operatorname{Cov}(X)\) in the ambient Euclidean coordinates. Put
\[
n=p+q,\qquad N=p^2+2pq+q,\qquad A=p(p-2),\qquad H_p(q)=-q^2+Aq-2p^2.
\]
There are exactly \(N\) vertices and \(\dim P_{p,q}=2n-2\). The **complete covariance spectrum**, with mode multiplicities (to be added when numerical eigenvalues coincide), is

| Eigenvalue | Mode multiplicity |
| --- | ---: |
| \(0\) | \(2\) |
| \(n/N\) | \(2p-1\) |
| \(p/N\) | \(q-1\) |
| \((p+2)/N\) | \(q-1\) |
| \(n(p^2+2p+q)/N^2\) | \(1\) |

The greatest positive eigenvalue is always \(n/N\); the least positive eigenvalue is
\[
\lambda_{\min}^{+}(C)=\min\left\{\frac pN,\frac{n(p^2+2p+q)}{N^2}\right\}.
\]
A **reentrant transition** occurs: the least-variance eigenspace is the antisymmetric independent-vertex contrast space when \(H_p(q)<0\) (dimension \(q-1\)), but switches to the one-dimensional symmetric clique-versus-independent contrast space when \(H_p(q)>0\). At \(H_p(q)=0\) the least eigenspace is their direct sum of dimension \(q\). The complete integer phase classification is:

* \(2\le p\le4\): \(H_p(q)<0\) for all integers \(q\ge2\).
* \(p=5\): \(H_p(q)>0\) exactly for \(6\le q\le9\), and equality occurs precisely at \(q=5,10\).
* \(p=6,7\): \(H_p(q)>0\) exactly for \(4\le q\le p(p-2)-4\), with no integer equality.
* \(p\ge8\): \(H_p(q)>0\) exactly for \(3\le q\le p(p-2)-3\), with no integer equality.

In particular, as \(q\) grows for each fixed \(p\ge5\), the least-variance mode changes from antisymmetric to symmetric and back to antisymmetric. The intrinsic covariance condition number is exactly
\[
\kappa(C\vert_{\operatorname{aff}(P_{p,q})})=
\begin{cases}
\dfrac{N}{p^2+2p+q},&H_p(q)>0,\\[4pt]
\dfrac{p+q}{p},&H_p(q)\le0.
\end{cases}
\]
The two formulas agree at equality. The large root of the transition polynomial is \(p^2-2p-2+O(p^{-1})\) as \(p\to\infty\), giving a quadratic scale for the second transition.

## Assumptions and scope

All graphs are finite, simple, undirected, and have the indicated labeled clique and independent-set partition. Uniformity means that each **polytope vertex** receives weight \(1/N\), including the loop-derived diagonal points; it does not mean a uniform point by polytope volume. The Euclidean structure is the standard metric of \(\mathbb R^{2n}\). Covariance eigenvalues are considered on the affine tangent space; the two unavoidable coordinate-sum directions give the stated zero eigenvalues. The input parameters are arbitrary integers \(p,q\ge2\), without an ordering assumption.

## Proof

**1. Exact vertex set and second moments.** Each allowed \((e_i,e_j)\) is a vertex: the linear functional extracting coordinate \(i\) from the first block and coordinate \(j\) from the second block attains its unique maximum \(2\) there. Let \(B\) be the symmetric matrix with \(B_{ij}=1\) exactly when \(i=j\) or \(\{i,j\}\) is an edge. In clique/independent order,
\[
B=\begin{pmatrix}J_p&J_{p\times q}\\J_{q\times p}&I_q\end{pmatrix},\quad
w=B\mathbf1=(n\mathbf1_p,(p+1)\mathbf1_q),\quad \mathbf1^Tw=N.
\]
For \(X=(e_I,e_J)\), the joint distribution is \(\Pr(I=i,J=j)=B_{ij}/N\), so \(\mathbb E e_I=\mathbb E e_J=w/N\), \(\mathbb E[e_Ie_I^T]=\operatorname{diag}(w)/N\), and \(\mathbb E[e_Ie_J^T]=B/N\). Hence, with \(D=\operatorname{diag}(w)\),
\[
C=\begin{pmatrix}
D/N-ww^T/N^2&B/N-ww^T/N^2\\
B/N-ww^T/N^2&D/N-ww^T/N^2
\end{pmatrix}.
\]

**2. Exact orthogonal splitting.** The orthogonal map \((u,v)\mapsto((u+v)/\sqrt2,(u-v)/\sqrt2)\) block-diagonalizes \(C\) into
\[
C_+=\frac{D+B}{N}-\frac{2ww^T}{N^2},\qquad
C_- =\frac{D-B}{N}=\frac{L(G_{p,q})}{N}.
\]
The antisymmetric block therefore has eigenvalues \(0\) once, \(p/N\) on contrasts within the independent set (multiplicity \(q-1\)), and \(n/N\) on contrasts within the clique and between the two classes (total multiplicity \(p\)). Indeed,
\[
L(G_{p,q})=
\begin{pmatrix}nI_p-J_p&-J_{p\times q}\\-J_{q\times p}&pI_q\end{pmatrix}.
\]

In the symmetric block, clique contrasts have eigenvalue \(n/N\) with multiplicity \(p-1\), and independent-set contrasts have eigenvalue \((p+2)/N\) with multiplicity \(q-1\). Both are orthogonal to \(w\), so the rank-one term vanishes on them. The remaining two-dimensional space is spanned by the normalized class-indicator vectors \(\mathbf1_p/\sqrt p\) and \(\mathbf1_q/\sqrt q\). The all-ones vector is a zero eigenvector of \(C_+\), and its remaining eigenvalue is the trace on this space:
\[
\frac{3p+q+2}{N}-\frac{2[pn^2+q(p+1)^2]}{N^2}
=\frac{n(p^2+2p+q)}{N^2}.
\]
This eigenvalue belongs to the symmetric class contrast \((q\mathbf1_p,-p\mathbf1_q)\). Every listed positive number is strictly positive. Counting multiplicities gives \(2n-2\), so the list is exhaustive and the two zero directions are the only affine-normal directions.

**3. Extremes and phase polynomial.** For \(q\ge2\), we have \((p+2)/N\le n/N\), \(p/N<n/N\), and
\[
\frac nN-\frac{n(p^2+2p+q)}{N^2}
=\frac{2pn(q-1)}{N^2}>0.
\]
Thus the largest eigenvalue is \(n/N\). The two candidates for the least eigenvalue differ by
\[
\frac{n(p^2+2p+q)}{N^2}-\frac pN=-\frac{H_p(q)}{N^2}.
\]
This proves the mode comparison and the condition-number formula, including equality multiplicities.

For \(p\le4\), the quadratic \(H_p(q)\) has negative discriminant \(p^2[(p-2)^2-8]\), so is strictly negative. For \(p=5\) it factors as \(-(q-5)(q-10)\). For \(p=6,7\), \(H_p(3)<0<H_p(4)\); for \(p\ge8\), \(H_p(2)<0<H_p(3)\). Since \(H_p(q)=H_p(A-q)\) and the parabola is concave with at most two roots, these sign comparisons give all stated exact integer intervals and exclude further equality. Finally the two roots, when present, are
\[
\frac{p(p-2)\pm p\sqrt{(p-2)^2-8}}2,
\]
and the upper root expands to \(p^2-2p-2+O(p^{-1})\). This concludes the theorem.

## Verification

Run `python3 artifacts/verify.py` using only the Python standard library. The checker reconstructs all allowed ordered-pair vertices, forms exact integer-scaled covariance matrices \(N^2C\), and tests their action on a spanning set of symmetric/antisymmetric class contrasts and both kernel directions. It checks 85 integer parameter pairs and 209,596 matrix entries across those profiles, with no floating-point tolerances. Expected output: `PQ_SPLIT_COVARIANCE_CHECKS_PASSED 85 parameter_cases 209596 matrix_entries`.

A separate numerical eigensolver spot-check was performed for boundary and nonboundary parameter pairs, including \((5,5)\), \((5,6)\), \((5,10)\), \((8,45)\) and \((8,46)\), agreeing with the predicted extremal eigenvalues and multiplicities. Finite checks are corroboration, not substitutes for the preceding proof for all integers.

## Relationship to prior work

Ohsugi and Tsuchiya's paper studies precisely these PQ-type polytopes for graph joins, including the split family \(K_p\vee\overline{K_q}\), but gives Ehrhart-theoretic \(h^*\) and normalized-volume formulas, not a uniform-vertex covariance theorem. Davis and Chen establish the underlying PQ construction and volume/draconian-sequence connection. Davis, Jakovleski and Pan derive further volume recurrences for other graphs. Classical split-graph Laplacian results describe the spectrum of \(G_{p,q}\), but by themselves do not identify the symmetric centered covariance block or the reentrant comparison. The covariance splitting, full spectrum, exact least-eigenspace phases and condition-number formula above are distinct statements requiring their own calculation.

## Limitations

This theorem concerns the specified standard-coordinate realization and vertex-uniform law; its condition number need not be preserved by a general affine or unimodular change of realization. It makes no statement about volume-uniform covariance, normalized volume, or power-flow solution counts. Searches and comparisons did not establish an earlier equivalent covariance theorem, but cannot certify historical priority exhaustively. No independent mathematical audit has been performed.

## References

1. R. Davis and T. Chen, *Computing Volumes of Adjacency Polytopes via Draconian Sequences*, arXiv:2007.11051, first posted 2020-07-21. https://arxiv.org/abs/2007.11051
2. H. Ohsugi and A. Tsuchiya, *PQ-type adjacency polytopes of join graphs*, arXiv:2103.15045, first posted 2021-03-28; particularly Section 4, Theorem 4.1. https://arxiv.org/abs/2103.15045
3. R. Davis, J. Jakovleski and Q. Pan, *Normalized Volumes of Type-PQ Adjacency Polytopes for Certain Classes of Graphs*, arXiv:2202.09853, first posted 2022-02-20. https://arxiv.org/abs/2202.09853
4. K. C. Das and M. Liu, *Complete split graph determined by its (signless) Laplacian spectrum*, Discrete Applied Mathematics 205 (2016), 45–51. https://doi.org/10.1016/j.dam.2016.01.003
