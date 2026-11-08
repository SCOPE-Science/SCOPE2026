# Exact inertia and boundary-rank spectra of the mutual-inverse graphs of finite isotone transformation monoids

## Finding

For integers \(n\geq1\) and \(1\leq r\leq n\), let \(\mathcal O_n\) be the monoid of order-preserving maps \([n]\to[n]\), and \(D_{n,r}\) its Green rank-\(r\) class. Form the **looped mutual-inverse graph** on \(D_{n,r}\): its real symmetric adjacency matrix \(K_{n,r}\) has entry \(1\) at the ordered pair \((f,g)\) precisely when both \(fgf=f\) and \(gfg=g\), including diagonal entries for idempotents. These are *mutual semigroup inverses*, not group inverses.

Put
\[
p=\binom{n-1}{r-1},\qquad q=\binom nr.
\]
The complete inertia, in the order (strictly positive eigenvalues, strictly negative eigenvalues, zero eigenvalues), is
\[
\boxed{\operatorname{In}(K_{n,r})=\left(\binom{p+1}{2},\binom p2,p(q-p)\right).}
\]
In particular the real rank of the mutual-inverse adjacency matrix is exactly \(p^2\) and, except in the top rank \(r=n\), it is singular. This holds for every integer parameter, not merely tested cases.

More precisely, let \(P\) be the set of ordered interval partitions of \([n]\) into \(r\) nonempty blocks, and \(Q\) the set of \(r\)-subsets of \([n]\). Define the \(p\)-by-\(q\) **transversal incidence matrix** \(R\) by \(R_{A,B}=1\) exactly when \(B\) contains one point from each block of \(A\). Let \(\lambda_1,\ldots,\lambda_p>0\) be the eigenvalues of the positive definite matrix \(RR^{\mathsf T}\), counted with multiplicity. Then the full eigenvalue multiset of \(K_{n,r}\) is
\[
\boxed{\{\lambda_i:1\leq i\leq p\}\;\uplus\;\{+\sqrt{\lambda_i\lambda_j},-\sqrt{\lambda_i\lambda_j}:1\leq i<j\leq p\}\;\uplus\;\{0^{\,[p(q-p)]}\}.}
\]
(The multiset union retains repeated numerical eigenvalues.) Equivalently, its monic characteristic polynomial is
\[
\boxed{t^{p(q-p)}\prod_{i=1}^{p}(t-\lambda_i)\prod_{1\leq i<j\leq p}(t^2-\lambda_i\lambda_j).}
\]

For rank \(r=2\), with \(n\geq2\), the Gram eigenvalues are *explicit*:
\[
\boxed{\lambda_k=\frac{n}{2-2\cos(k\pi/n)}=\frac{n}{4\sin^2(k\pi/(2n))},\quad 1\leq k\leq n-1.}
\]
Their product is \(n^{n-2}\), so the spectral radius of \(K_{n,2}\) is \(n/[4\sin^2(\pi/(2n))]\sim n^3/\pi^2\). For rank \(r=n-1\) and \(n\geq2\), the corresponding Gram eigenvalues are
\[
\boxed{\lambda_k=2+2\cos(k\pi/n),\quad1\leq k\leq n-1,}
\]
and their product is \(n\). These explicitly described spectra include the overlapping case \(n=3,r=2\). No assertion is made that the general-rank Gram eigenvalues have a closed trigonometric formula.

## Assumptions and scope

The underlying chain is \([n]=\{1,\ldots,n\}\), and maps compose in either consistent convention; mutual inverse equations are invariant under reversing this convention. The adjacency matrix includes diagonal loops, since \(f\) is its own mutual inverse exactly when \(f^2=f\). Removing those loops changes the spectrum and is **not** covered. The rank parameter is the number of distinct image values, not matrix rank. The theorem concerns the binary mutual-inverse relation, not a specific choice of a permutation matching or an involution matching. All eigenvalues are over \(\mathbb R\).

## Proof

**1. Green-class coordinates and the inverse relation.** Every \(f\in D_{n,r}\) is determined by an interval partition \(A=(A_1,\ldots,A_r)\) (the kernel classes in increasing order) and an image \(B=\{b_1<\cdots<b_r\}\), with \(f(A_i)=b_i\). The cardinalities are \(|P|=\binom{n-1}{r-1}=p\) and \(|Q|=\binom nr=q\), so \(|D_{n,r}|=pq\). For \(f=(A,B)\) and \(g=(C,D)\), the equations \(fgf=f\) and \(gfg=g\) hold if and only if \(D\) is a transversal of \(A\) and \(B\) is a transversal of \(C\). For completeness, the first condition means that \(g\) maps each image value \(b_i\) back into \(A_i\); then each \(b_i\) must lie in the \(i\)-th kernel block of \(g\). The second condition gives the reverse transversality. Equivalently, the \((A,B),(C,D)\) entry of \(K_{n,r}\) is \(R_{A,D}R_{C,B}\). This is precisely the crossed-square relation of Higgins (2026), but the spectrum is not supplied there.

**2. Real diagonalization.** Identify real column vectors on \(P\times Q\) with real \(p\)-by-\(q\) arrays \(X\). Matrix multiplication by \(K_{n,r}\) then has the exact form
\[
\mathcal K(X)=R X^{\mathsf T}R.
\]
First, \(R\) has full row rank. For every cut set \(A\) with right endpoints \(1\leq a_1<\cdots<a_{r-1}<n\), select the image column \(B(A)=\{a_1,\ldots,a_{r-1},n\}\). If this \(B(A)\) is a transversal of another partition \(A'\) with right endpoints \(a'_i\), then \(a'_i\geq a_i\) for all \(i\). Ordering cut sets lexicographically, the square submatrix \((R_{A',B(A)})\) is lower triangular with diagonal entries \(1\), hence has determinant \(1\). The empty cut set for \(r=1\) is included, and the argument covers \(r=n\). Therefore \(\operatorname{rank}R=p\).

Choose a real singular-value decomposition \(R=U\Sigma V^{\mathsf T}\) with singular values \(s_i=\sqrt{\lambda_i}>0\) for \(1\leq i\leq p\). In the orthogonal coordinates \(Y=U^{\mathsf T}XV\), the operator becomes \(Y\mapsto\Sigma Y^{\mathsf T}\Sigma\). On the leading \(p\)-by-\(p\) block, the diagonal matrix units have eigenvalues \(s_i^2=\lambda_i\), and for every \(i<j\) the symmetric and skew-symmetric combinations of two matrix units have eigenvalues \(+s_is_j\) and \(-s_is_j\). The remaining \(p(q-p)\) matrix units lie in the kernel. This constructs an orthogonal eigenbasis, proves the full multiset formula, and yields the displayed inertia and characteristic polynomial. In particular the product of nonzero eigenvalues, with signs, is \((-1)^{\binom p2}\det(RR^{\mathsf T})^p\).

**3. Closed Gram spectra at the two boundary ranks.** For \(r=2\), index the rows of \(R\) by the cut location \(1\leq i\leq n-1\) and columns by the two-point images \(\{a<b\}\). Then \(R_{i,\{a,b\}}=1\) exactly when \(a\leq i<b\). Hence
\[
(RR^{\mathsf T})_{ij}=\min(i,j)\,[n-\max(i,j)].
\]
Let \(L\) be the \((n-1)\)-by-\((n-1)\) discrete Dirichlet Laplacian with diagonal \(2\) and first off-diagonals \(-1\). Direct multiplication, including endpoints, gives \(L(RR^{\mathsf T})=nI\). The vectors with \(i\)-th component \(\sin(ik\pi/n)\) diagonalize \(L\) with eigenvalue \(2-2\cos(k\pi/n)\). Thus the rank-two Gram eigenvalues are as stated. The tridiagonal determinant recursion gives \(\det L=n\), whence \(\det(RR^{\mathsf T})=n^{n-2}\).

For \(r=n-1\), a kernel partition merges exactly one adjacent pair \(j,j+1\), and an image omits a single point \(k\). The image is a transversal precisely when \(k=j\) or \(k=j+1\). Consequently \(RR^{\mathsf T}\) is the \((n-1)\)-by-\((n-1)\) tridiagonal matrix with diagonal \(2\) and first off-diagonals \(+1\). Its sine eigenvectors have eigenvalues \(2+2\cos(k\pi/n)\), and the same determinant recursion gives \(\det(RR^{\mathsf T})=n\).

## Verification

An independently executable Python script `verify_inverse_inertia.py` constructs *all* order-preserving maps for \(1\leq n\leq6\), forms the mutual-inverse adjacency matrix directly by evaluating \(fgf=f\) and \(gfg=g\), and constructs the separate transversal matrix from interval partitions and images. It checks equality of the two adjacencies and their complete real eigenvalue multisets, checks the exact triangular full-rank certificate, and checks the exact rank-two and rank-\((n-1)\) Gram identities and determinants. The recorded replay `verification_output.txt` reports `VERIFY_OK rank_classes=21 elements=637 checked_ordered_pairs=75225 inertia_and_full_spectrum=match`. Numerical eigenvalue comparisons are finite corroboration only; the exact infinite-parameter theorem is established by the proof above.

To reproduce from the two standalone files with Python 3, NumPy, and SymPy installed, run `OPENBLAS_NUM_THREADS=1 python verify_inverse_inertia.py` from the directory containing them. No external data files are needed. The script uses a numerical tolerance in the finite eigenvalue tests, alongside exact integer adjacency, Gram, triangular-minor, and determinant tests.

## Relationship to prior work

Higgins (2026), arXiv:2610.01912v1 (first publicly submitted October 1, 2026), defines the crossed-square inverse relation, identifies the transversal incidence matrix for \(\mathcal O_n\), and proves that every \(\mathcal O_n\) has a permutation matching using balanced weights. Those results establish the *objects and existence property* but not their real mutual-inverse adjacency spectra, full-row-rank incidence certificate, inertia, or the trigonometric boundary-rank spectral formulas. The present work does not claim to prove the prior existence theorem. Higgins (2024) surveys inverse matchings and their bipartite incidence graphs; it does not report this spectral classification. Standard singular-value decomposition and discrete Dirichlet eigenvectors are used as methods, not presented as discoveries. Related earlier results on explicit involutive matchings of selected rank classes are logically different: a matching specifies a permutation inside the inverse relation, not its full adjacency spectrum.

## Limitations

The characteristic-polynomial formula for arbitrary intermediate \(r\) uses the eigenvalues of the explicitly specified Gram matrix \(RR^{\mathsf T}\), not a solved numerical expression for each of them. Closed trigonometric lists are proved only at \(r=2\) and \(r=n-1\). The result does not settle the existence, uniqueness, or enumeration of involution matchings at other ranks, nor does inertia alone imply any Hall condition. A prior equivalent observation phrased using tensor-commutation operators or incidence-graph spectra remains a possible historical-priority risk. No independent mathematical audit has been performed.

## References

1. Peter M. Higgins, *Balanced weightings and permutation matchings applied to the monoid of order-preserving mappings*, arXiv:2610.01912v1, October 1, 2026. https://arxiv.org/html/2610.01912v1
2. Peter M. Higgins, *Finite regular semigroups with permutations that map elements to inverses*, Semigroup Forum **109** (2024), 141–147. https://doi.org/10.1007/s00233-024-10430-0
3. Peter M. Higgins, *Orthodox semigroups and permutation matchings*, arXiv:1812.03743 (2018). https://arxiv.org/abs/1812.03743
4. J. M. Howie, *Fundamentals of Semigroup Theory*, Clarendon Press, Oxford, 1995 (standard Green-class theory).
