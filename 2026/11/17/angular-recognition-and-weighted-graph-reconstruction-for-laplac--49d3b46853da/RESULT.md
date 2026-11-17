# Angular recognition and weighted-graph reconstruction for Laplacian-column simplices

## Finding

Let \(n\ge3\). Suppose \(\Theta=(\theta_{ij})\) specifies all pairwise *interior dihedral angles* between the facets opposite the respective vertices of a nondegenerate Euclidean \((n-1)\)-simplex; only simultaneous relabeling of facets is immaterial. Define the exterior-normal cosine matrix \(C\) by \(C_{ii}=1\), \(C_{ij}=-\cos\theta_{ij}\) for \(i\ne j\). Its one-dimensional kernel contains a vector \(a\) with every coordinate strictly positive. Set
\[
K=\operatorname{diag}(a)\,C\,\operatorname{diag}(a),\qquad
R=(K^{\dagger})^{1/2},
\]
where \(\dagger\) is the Moore--Penrose pseudoinverse and the square root is the unique positive-semidefinite square root.

**Angular recognition and reconstruction theorem.** The specified simplex is similar, in its inherited Euclidean metric, to \(T_L=\operatorname{conv}\{Le_1,\ldots,Le_n\}\subset\mathbf1^{\perp}\), the canonical Laplacian-column simplex of a connected, undirected, positively edge-weighted loopless graph, **if and only if** \(R_{ij}\le0\) for every \(i\ne j\). When this holds, \(R\) itself is a connected weighted graph Laplacian and its weights are explicitly \(w_{ij}=-R_{ij}\) for \(i\ne j\). The weight matrix is uniquely determined by the angle matrix up to one common positive scalar; a simultaneous permutation of the angle rows and columns induces the same permutation of graph vertices. In particular, the graph is unweighted with a common positive edge weight precisely when all strictly negative off-diagonal entries of \(R\) are equal.

The same statement works directly from a symmetric candidate matrix \(C\), without assuming a simplex exists, provided \(C\succeq0\), \(\operatorname{rank}C=n-1\), \(C_{ii}=1\), and \(\ker C\) is spanned by a strictly positive vector. The sign test above is then necessary and sufficient for the candidate to be realized by a connected weighted graph Laplacian-column simplex. Choosing \(a\) with \(\sum_i a_i=n\) fixes a canonical representative of the recovered weight ratios.

This image includes simplices with obtuse dihedral angles; it is **not** the usual correspondence between nonobtuse simplices and graph Laplacians as their inverse Gram matrices. For example, the path graph on four vertices yields \(((L^{\dagger})^2)_{12}=7/16>0\); its corresponding interior dihedral angle is obtuse and has cosine \(-7/\sqrt{105}\).

## Assumptions and scope

All graphs are finite, connected, undirected, loopless, and have strictly positive weights on their edges; a nonedge is represented by weight zero. The Laplacian has \(L_{ij}=-w_{ij}\) for \(i\ne j\) and \(L_{ii}=\sum_{j\ne i}w_{ij}\). Its rank is \(n-1\), it is symmetric positive semidefinite, and \(L\mathbf1=0\). The simplex is given by the *columns of \(L\)* in the standard Euclidean metric on \(\mathbf1^\perp\), not by a vertex configuration with Gram matrix \(L\). The distinction matters.

The input is the **complete pair-indexed angle matrix**, modulo simultaneous facet permutation; the unordered multiset of angle values is not asserted to determine the graph. Angles alone are invariant under similarity, so no absolute conductance scale can be recovered. All matrix operations and sign conditions in the theorem are mathematically exact; ordinary floating-point eigenvalue routines provide approximate checks, not exact tests of zero weights.

## Proof

**1. Facet normals in the column realization.** Let \(L\) be any connected weighted graph Laplacian. Write \(Q=L^{\dagger}\). Since \(QL=LQ=P=I-\mathbf1\mathbf1^{\mathsf T}/n\), for each \(i,j\),
\[
 (Qe_i)^{\mathsf T}Le_j=\delta_{ij}-1/n.
\]
Consequently \(Qe_i\) is perpendicular to the facet opposite vertex \(Le_i\) and points inward, towards that vertex. The normal is nonzero because \(Q\) is positive definite on \(\mathbf1^\perp\) and \(Pe_i\ne0\). With \(b_i=\|Qe_i\|>0\), the normal-cosine matrix is
\[
 C=\operatorname{diag}(b)^{-1}\,Q^2\,\operatorname{diag}(b)^{-1}.
\]
The use of inward rather than outward normals does not alter pairwise cosine products. The interior dihedral cosine is the negative of this normal cosine. Since \(Q^2\mathbf1=0\) and \(\operatorname{rank}Q=n-1\), \(C\succeq0\), \(\operatorname{rank}C=n-1\), and \(\ker C=\operatorname{span}\{b\}\), with \(b>0\).

**2. Necessity and the inverse operation.** For any positive kernel vector \(a\) of \(C\), there is a scalar \(t>0\) such that \(a=tb\). Thus
\[
 K=\operatorname{diag}(a)C\operatorname{diag}(a)
 =t^2Q^2.
\]
The spectral decomposition of \(L\) on \(\mathbf1^\perp\) shows
\[
 (K^{\dagger})^{1/2}=(t^{-2}L^2)^{1/2}=t^{-1}L.
\]
This proves the off-diagonal sign condition and explicitly recovers every edge weight up to common scale. The positive nullspace is one-dimensional, so \(a\) is unique up to scale, and no other connected weighted graph can yield the same labeled \(C\) except by scaling all weights. Matrix functions commute with simultaneous permutation, proving the unlabeled isomorphism assertion.

**3. Sufficiency and candidate-angle realization.** Assume \(C\succeq0\), rank \(n-1\), diagonal \(1\), and a strictly positive null vector \(a\). Then \(K=\operatorname{diag}(a)C\operatorname{diag}(a)\) is positive semidefinite of rank \(n-1\) with kernel exactly \(\operatorname{span}\{\mathbf1\}\). The matrix \(R=(K^\dagger)^{1/2}\) is symmetric positive semidefinite with that same kernel, and thus its row sums vanish. When every off-diagonal entry is nonpositive, define \(w_{ij}=-R_{ij}\ge0\), placing an edge where \(w_{ij}>0\). The zero row sums make \(R\) the weighted graph Laplacian of this graph. The rank \(n-1\) forces the graph to be connected (the number of zero eigenvalues of a weighted graph Laplacian equals its number of components).

Moreover \(R^{\dagger}=K^{1/2}\), because both have eigenvalue \(\sqrt\mu\) on an eigenspace of \(K\) with eigenvalue \(\mu>0\), and zero on the common kernel. Equivalently,
\[
 (R^{\dagger})^2=K.
\]
The \(i\)-th facet inward normal of \(T_R\) is \(R^{\dagger}e_i\), by step 1, and has squared norm \(K_{ii}=a_i^2\). Its unit-normal matrix therefore has Gram entries
\[
 \frac{K_{ij}}{a_i a_j}=C_{ij},
\]
so all specified dihedral angles are realized. This also proves that every candidate satisfying the hypotheses and sign test actually defines the desired simplex angle data. Conversely, step 1 proves those candidate conditions for every Laplacian-column simplex.

**4. Strict separation from the nonobtuse graph-simplex correspondence.** For the unweighted path on four vertices, a direct inverse on \(\mathbf1^\perp\) gives
\[
L^{\dagger}=\frac18\begin{pmatrix}7&1&-3&-5\\1&3&-1&-3\\-3&-1&3&1\\-5&-3&1&7\end{pmatrix},\qquad
(L^{\dagger})^2=\frac1{16}\begin{pmatrix}21&7&-9&-19\\7&5&-3&-9\\-9&-3&5&7\\-19&-9&7&21\end{pmatrix}.
\]
The first two inward normals have positive inner product \(7/16\). Thus their facet interior angle has cosine \(-7/\sqrt{105}<0\), although \(L\) is a valid positive-weight Laplacian. A criterion requiring all dihedral angles to be nonobtuse would incorrectly exclude this graph's canonical Laplacian-column simplex.

## Verification

The standalone `checker.py` tests the construction using independently computed symmetric eigendecompositions and pseudoinverses. It exhaustively ranges over all **770 connected labeled simple graphs** on three, four, or five vertices, and on each graph checks both unit weights and a deterministic positive rational weighting. The tests compare the reconstructed \(R\) with the original \(L\) up to a global scalar and verify reconstituted unit normal-cosine matrices. A separate centered positive-semidefinite matrix with a positive off-diagonal entry supplies a rejecting non-graph input. All such computations are finite **numerical stress tests**, not an all-dimensional proof; the proof above supplies the infinite statement. Small eigenvalues and nonedge entries are tested with numerical tolerances. Execute `python checker.py` with Python 3 and NumPy.

## Relationship to prior work

Braun and Meyer introduced Laplacian-column simplices in 2017 and studied lattice and Ehrhart properties, not a complete inverse from their Euclidean dihedral angles [1]. Devriendt and Van Mieghem discuss the Fiedler graph--simplex correspondence in which the graph Laplacian is the **vertex Gram matrix** of a representative simplex [2]. Devriendt gives the general relation between simplex dihedral angles and the **pseudoinverse vertex Gram matrix**, as well as a characterization of hyperacute simplices by graph Laplacians [3]. These are important ingredients, not new claims here. In the column realization the vertex Gram matrix is instead \(L^2\), and the angle inverse requires a **positive semidefinite square root of a pseudoinverse** followed by an off-diagonal sign test. As the four-vertex path shows, the image is not confined to the hyperacute simplices in [2,3]. The new assertion here is the explicit all-dimensional image criterion and recovery of *the original weighted graph* from pair-indexed angles, including graph sparsity and conductance ratios. Whether an equivalent theorem occurs in unindexed sources requires further independent historical review.

## Limitations

Only the full angle matrix, not its unlabeled entry multiset, is used. Weights are determined only up to common scale. The image theorem is exact but does not provide perturbation robustness or a polynomial bit-complexity bound for exact algebraic-number arithmetic. Floating-point checker tolerances do not decide exact graph sparsity. The argument excludes disconnected graphs and dimension below two. Historical originality remains provisional without independent comprehensive literature audit.

## References

[1] B. Braun and M. Meyer, *Laplacian Simplices*, arXiv:1706.07085v1 (public 2017-06-21), https://arxiv.org/abs/1706.07085, especially §3 for the definition of the column simplex.

[2] K. Devriendt and P. Van Mieghem, *The Simplex Geometry of Graphs*, arXiv:1807.06475v1 (public 2018-07-17), https://arxiv.org/abs/1807.06475, especially §3 for the Fiedler correspondence using a vertex Gram matrix.

[3] K. Devriendt, *Effective resistance is more than distance: Laplacians, Simplices and the Schur complement*, arXiv:2010.04521v1 (public 2020-10-09), https://arxiv.org/abs/2010.04521, especially §2.2--2.3 for the normal-angle/pseudoinverse Gram identity and nonobtuse characterization.
