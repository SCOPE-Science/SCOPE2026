# Five strictly ordered covariance modes of balanced multipartite spanning-tree polytopes

## Finding
For integers \(k\ge3\) and \(n\ge2\), let \(G=K_{n,\ldots,n}\) have \(k\) parts of size \(n\), and let \(X\in\{0,1\}^{E(G)}\) be the edge-indicator vector of a uniformly sampled spanning tree of \(G\). The spectrum of its covariance \(C=\operatorname{Cov}(X)\), with multiplicities, is exactly

\[
\begin{array}{c|c|c}
\text{mode}&\text{eigenvalue}&\text{multiplicity}\\\hline
0&0&1\\
L&\dfrac{kn-2}{kn^2(k-1)}&k(n-1)\\
A&\dfrac{k^2n-2k+1}{kn^2(k-1)^2}&k-1\\
T&\dfrac{2(k^2n-kn-2k+1)}{kn^2(k-1)^2}&\binom{k}{2}(n-1)^2\\
H&\dfrac{2(kn-2)}{kn^2(k-1)}&k(k-2)(n-1)\\
B&\dfrac{2(k^2n-2k+1)}{k^2n^2(k-1)}&\dfrac{k(k-3)}2
\end{array}
\]

The last class is absent for \(k=3\). Every other displayed multiplicity is positive. With subscripts indicating these modes, the eigenvalues are strictly ordered
\[
0<\lambda_L<\lambda_A<\lambda_T<\lambda_H<\lambda_B\quad(k\ge4),
\qquad 0<\lambda_L<\lambda_A<\lambda_T<\lambda_H\quad(k=3).
\]
Hence the intrinsic covariance condition number, namely the ratio of the largest to the smallest positive eigenvalue, is
\[
\boxed{\kappa(C|_{\mathbf1^\perp})=\begin{cases}2,&k=3,\\ 2+\dfrac{2}{k(kn-2)},&k\ge4.\end{cases}}
\]
Thus the edge-indicator covariance of this growing-dimensional family is uniformly conditioned, with a sharp exceptional identity for three parts.

## Assumptions and scope
The graph is simple, complete and *balanced* multipartite; it has \(kn\) vertices and \(E=\binom{k}{2}n^2\) edges. Every labeled spanning tree is sampled with equal probability; each spanning tree corresponds to a distinct vertex of the graphic-matroid base polytope. The covariance acts on the ambient edge-coordinate Euclidean space. Because every tree contains exactly \(kn-1\) edges, the constant edge direction is in its kernel; the polytope's affine tangent space is \(\mathbf1^\perp\) and is full-dimensional there. The result is asserted for all and only integer \(k\ge3,n\ge2\).

## Proof
Write \(a=((k-1)n)^{-1}\), \(q=(k(k-1)n^2)^{-1}\), and \(r=2(a-q)\). The graph Laplacian has eigenvalue \(0\) on constants, \((k-1)n\) on each within-part zero-sum subspace, and \(kn\) on the between-part zero-sum subspace. Therefore its pseudoinverse is
\[
L^+=a(I-H)+\frac{1}{kn}\left(H-\frac{J}{kn}\right),
\qquad H=\operatorname{diag}(J_n/n,\ldots,J_n/n).
\]
If \(v_e\) is an oriented edge incidence vector and \(z_e\in\mathbb R^k\) records its two part endpoints with their signs, the transfer-current kernel is
\[
K_{ef}=v_e^{\mathsf T}L^+v_f=a(v_e\cdot v_f)-q(z_e\cdot z_f),\qquad K_{ee}=r.
\]
The matrix-tree determinant, with independently weighted edges, gives \(\Pr(e\in T)=K_{ee}\) and \(\Pr(e,f\in T)=K_{ee}K_{ff}-K_{ef}^2\) for distinct edges. Thus \(C_{ee}=r(1-r)\), and \(C_{ef}=-K_{ef}^2\) for \(e\ne f\). This step is the established transfer-current identity; novelty is not claimed for it.

Group edge coordinates into \(\binom k2\) blocks, one \(n\times n\) matrix for each unordered part-pair. In a single block, the covariance entries are \(d=r(1-r)\) on the diagonal, \(w_1=-(a-2q)^2\) for distinct edges sharing a vertex, and \(w_0=-4q^2\) for disjoint edges. Between two blocks whose part-pairs share exactly one part, the entries are \(z_1=-(a-q)^2\) if their endpoints in that common part coincide and \(z_0=-q^2\) otherwise. Blocks with disjoint part-pairs have zero covariance. All these identities follow by inserting the two incidence vectors into the displayed kernel; their signs disappear upon squaring.

In each \(n\times n\) block decompose \(\mathbb R^n=\langle\mathbf1\rangle\oplus U\), where \(U=\mathbf1^\perp\), and take the four tensor summands. The resulting diagonal block coefficients on \(\mathbf1\otimes\mathbf1\), either of the two single-contrast summands, and \(U\otimes U\), respectively, are
\[
\begin{aligned}
d_0&=d+2(n-1)w_1+(n-1)^2w_0,\\
d_1&=d+(n-2)w_1-(n-1)w_0,\\
d_2&=d-2w_1+w_0.
\end{aligned}
\]
Between adjacent part-pair blocks, the coupling is \(b_0=nz_1+n(n-1)z_0\) on constants and \(b_1=n(z_1-z_0)\) on the shared-part contrast. The constant sector is \(d_0I+b_0A(L(K_k))\), where the line graph of \(K_k\) has adjacency eigenvalues \(2(k-2)\), \(k-4\), and \(-2\), with multiplicities \(1\), \(k-1\), and \(k(k-3)/2\). At \(k=3\) the last eigenspace is absent. Substituting the coefficients gives the zero, \(A\), and \(B\) rows of the table.

For each of the \(k\) parts and each of its \(n-1\) independent contrasts, the incident \(k-1\) part-pair blocks give \(d_1I+b_1(J_{k-1}-I)\). Its one-dimensional constant and \(k-2\) contrast eigenspaces give the \(L\) and \(H\) rows. The tensor contrast sector has eigenvalue \(d_2=\lambda_T\), with the stated multiplicity. These orthogonal sectors exhaust all \(\binom{k}{2}n^2\) edge coordinates, which proves the spectrum and the sole zero direction.

Every inequality is strict by the following exact positive gaps:
\[
\begin{aligned}
\lambda_A-\lambda_L&=\frac{kn-1}{kn^2(k-1)^2},\\
\lambda_T-\lambda_A&=\frac{k(k-2)n-2k+1}{kn^2(k-1)^2},\\
\lambda_H-\lambda_T&=\frac{2}{kn^2(k-1)^2},\\
\lambda_B-\lambda_H&=\frac{2}{k^2n^2(k-1)}\quad(k\ge4).
\end{aligned}
\]
The second numerator is at least \(k(2k-6)+1>0\) for \(k\ge3,n\ge2\). The final gap is relevant only when the \(B\) sector is present. Dividing the greatest by the least positive eigenvalue gives exactly \(2\) for \(k=3\), and \(2+2/[k(kn-2)]\) for \(k\ge4\).

## Verification
The accompanying standalone `artifacts/verify.py` recomputes the edge covariance using exact fractions, compares its entire spectrum with independent numerical diagonalization on five nontrivial graph sizes, verifies the formula, strict gaps and multiplicities for 1,606 parameter pairs, and exhaustively enumerates all 384 spanning trees of \(K_{2,2,2}\), checking all 144 entries of the covariance exactly. It prints `BALANCED_MULTIPARTITE_COVARIANCE_CHECKS_PASSED 1755` on success. These finite checks corroborate but do not replace the preceding infinite-family proof. Run from the file's extracted directory with Python 3 and NumPy: `OPENBLAS_NUM_THREADS=1 python artifacts/verify.py`.

## Relationship to prior work
Chaourar describes facets of general spanning-tree polytopes, not their vertex covariance. The general transfer-current determinantal formula supplies the pairwise inclusion probabilities used here. Li, Chen and Yan (2023) provide spanning-forest containment counts for complete tripartite and quadripartite graphs, while Wang and Ge (2026) extend forest containment enumeration to arbitrary complete multipartite graphs. Those counts can imply individual entries of \(C\); **no originality is claimed for these marginal or pairwise probabilities**. The claim here is the simultaneous full covariance spectral decomposition, exact multiplicities, strict hierarchy and sharp condition number across every balanced multipartite graph with \(k\ge3\). General enumeration results do not, by themselves, present this diagonalization. The closest prior geometry results examined concern inballs or Minkowski centers of other graph base polytopes, rather than this invariant.

## Limitations
The result concerns equal part sizes, uniformly sampled *spanning trees*, and the standard edge-coordinate Euclidean metric; it makes no assertion for unbalanced multipartite graphs or other sampling weights. The formulas are an analytic consequence of classical transfer-current theory, and an equivalent earlier representation-theoretic formulation cannot be categorically excluded. The full text of the 2023 Li–Chen–Yan study was not available for inspection; its published abstract and accessible references were consulted. No independent mathematical audit has been performed.

## References
1. B. Chaourar, *The facets of the spanning trees polytope*, arXiv:1903.07292, first posted 2019-03-18; https://arxiv.org/abs/1903.07292.
2. D. Li, W. Chen, and W. Yan, *Enumeration of spanning trees of complete multipartite graphs containing a fixed spanning forest*, Journal of Graph Theory 104 (2023), 160–170, doi:10.1002/jgt.22954.
3. W. Wang and J. Ge, *On enumeration of spanning trees of complete multipartite graphs containing a fixed spanning forest*, arXiv:2602.03602, 2026-02-03; https://arxiv.org/abs/2602.03602.
4. R. Lyons, *Determinantal probability measures*, Publications Mathématiques de l'IHÉS 98 (2003), 167–212, doi:10.1007/s10240-003-0016-0 (background on transfer-current determinantal measures).
