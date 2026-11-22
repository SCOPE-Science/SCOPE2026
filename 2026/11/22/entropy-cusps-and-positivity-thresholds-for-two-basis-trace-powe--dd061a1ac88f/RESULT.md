# Entropy cusps and positivity thresholds for two-basis trace-power kernels

## Finding

Let two ordered orthonormal bases of a complex Hilbert space of dimension \(d\geq2\) determine their \(2d\) rank-one projections. For exponent \(r>0\), form the trace-power kernel \(\mathcal K_r(P,Q)=\operatorname{Tr}[(PQP)^r]\). Write \(U\) for the unitary overlap matrix and \(B_{ij}=|U_{ij}|^2\). For the kernel matrix \(G_r\), the entire spectral list is

\[
\sigma(G_r)=\{1+s_j(B^{\circ r}),\,1-s_j(B^{\circ r}):1\le j\le d\},
\]

with multiplicities, where \(s_j\) are singular values and \(B^{\circ r}\) denotes entrywise powers with \(0^r=0\). Consequently, for \(0<r<1\), \(G_r\) is positive semidefinite exactly when the bases agree up to reordering and phases; for \(r\ge1\), it is always positive semidefinite, and for \(r>1\) it is positive definite exactly when the bases have no common ray. The negative spectral edge for \(0<r<1\) is bounded sharply by \(1-d^{1-r}\), attained exactly when the bases are mutually unbiased.

More precisely, let the bipartite support graph of \(B\) have connected components \(C_1,\ldots,C_m\). The row and column indices of each component have the same cardinality \(d_j\), and the corresponding submatrix \(B_j\) is doubly stochastic. Define the mean transition entropy of that component by

\[
h_j=-\frac1{d_j}\sum_{a,b\in C_j} (B_j)_{ab}\log (B_j)_{ab},\qquad 0\log0=0.
\]

Let \(h_{\min}=\min_j h_j\) and \(h_{\max}=\max_j h_j\). Then **the exact one-sided critical slopes** of the smallest kernel eigenvalue are

\[
\begin{aligned}
\lambda_{\min}(G_{1-\varepsilon})&=-\varepsilon h_{\max}+O(\varepsilon^2),\\
\lambda_{\min}(G_{1+\varepsilon})&=\varepsilon h_{\min}+O(\varepsilon^2)
\end{aligned}
\quad(\varepsilon\downarrow0).
\]

At \(r=1\), the kernel has exactly \(m\) zero eigenvalues. Immediately below \(1\), it has exactly one negative eigenvalue per support component with \(d_j>1\); singleton components retain one zero eigenvalue. Immediately above \(1\), it is positive definite on every nontrivial component and retains one zero eigenvalue per singleton component. These near-critical inertia statements hold in some positive, basis-dependent neighborhood of \(1\); they are not asserted uniformly in \(d\).

## Assumptions and scope

The dimension \(d\) is any finite integer at least two. Both bases are complete orthonormal systems in the *same complex* Hilbert space; phases, ordering, and any vanishing overlaps are allowed. The \(2d\) projections are included with multiplicity (a common ray appears once in each basis). The trace is the ordinary non-normalized matrix trace. Equivalently, the kernel equals \(d\) times the kernel formed using the normalized trace \(\operatorname{Tr}/d\). The Gram matrix is real symmetric despite the potentially complex entries of \(U\).

The support graph has a left vertex for each row and a right vertex for each column, and an edge precisely where \(B_{ij}>0\). A singleton component means one row and one column connected by a unit-modulus entry. The words “immediately below” and “immediately above” mean sufficiently close to \(1\) for the fixed bases. No statement about arbitrary sets of positive operators or arbitrary numbers of unrelated bases is made.

## Proof

**1. Rank-one reduction and spectrum.** If \(P=|e\rangle\langle e|\) and \(Q=|f\rangle\langle f|\), then \(PQP=|\langle e,f\rangle|^2P\), so \(\operatorname{Tr}[(PQP)^r]=|\langle e,f\rangle|^{2r}\). Orthogonality within each basis gives the exact block identity

\[
G_r=\begin{pmatrix}I_d&A_r\\A_r^{\mathsf T}&I_d\end{pmatrix},\qquad A_r=(B_{ij}^{r})_{ij}.
\]

The real singular-value decomposition of \(A_r\) diagonalizes the off-diagonal symmetric block, yielding eigenvalues \(1\pm s_j(A_r)\). Thus \(\lambda_{\min}(G_r)=1-\|A_r\|_2\).

**2. Global sign classification.** Since \(U\) is unitary, \(B\) is doubly stochastic. For \(r=1\), \(\|A_1\|_2=1\) (both the row and column sums equal one). For \(r>1\), each row and column sum of \(B^{\circ r}\) is at most one, hence \(\|A_r\|_2\le\sqrt{\|A_r\|_1\|A_r\|_\infty}\le1\). Equality can hold only in a support component containing a row with exactly one nonzero entry: if all rows in that component contain at least two positive entries, every row sum is strictly below one, and likewise for columns. Such a singleton-support row of a unitary matrix forces the corresponding column to be a singleton, i.e. a shared ray. Conversely a shared ray gives a direct summand \((1)\) of \(A_r\) and hence a zero eigenvalue of \(G_r\). This proves the strict positivity criterion for \(r>1\).

For \(0<r<1\), one has \(B_{ij}^r\ge B_{ij}\) with strict inequality whenever \(0<B_{ij}<1\). The constant unit vectors \(u=v=d^{-1/2}\mathbf1\) give

\[
\|A_r\|_2\ge u^{\mathsf T}A_rv=\frac1d\sum_{i,j} B_{ij}^r\ge1,
\]

with strict inequality unless every entry of \(B\) lies in \(\{0,1\}\). A doubly stochastic zero-one matrix is a permutation matrix, equivalently \(U\) is monomial. For a monomial \(U\), \(A_r\) is a permutation matrix for every \(r>0\); therefore \(G_r\) is positive semidefinite. This proves the complete positivity boundary.

The concavity of \(t\mapsto t^r\) on nonnegative numbers yields \(\sum_j B_{ij}^r\le d^{1-r}\) in every row and likewise in every column. Thus \(\|A_r\|_2\le d^{1-r}\), giving the sharp universal edge bound. Fourier unitary bases have \(B_{ij}=1/d\) and attain equality. To see equality forces uniform overlaps, consider the nonnegative symmetric bipartite adjacency matrix \(H=\left(\begin{smallmatrix}0&A_r\\A_r^{\mathsf T}&0\end{smallmatrix}\right)\). Its row sums are all at most \(C=d^{1-r}\). If its spectral radius equals \(C\), an irreducible support component attains this maximal degree, and the positive Perron eigenvector and the maximum-coordinate argument force every vertex of that component to have weighted degree \(C\). Equality in the strict Jensen bound then makes each row in that component uniform across all \(d\) columns. This includes *all* right vertices. Equality for each of these columns then makes that column uniform across all \(d\) rows, implying \(B_{ij}=1/d\) globally. Therefore exactly the mutually unbiased bases attain the bound.

**3. Connected-support decomposition and simplicity.** Bistochasticity guarantees that the row and column counts agree in each connected component: the total matrix mass of its rows equals their number, and also equals the number of its columns. After separate permutations, \(B\) is the direct sum of square doubly stochastic blocks \(B_j\). For each connected component, \(B_jB_j^{\mathsf T}\) is an irreducible, symmetric, nonnegative stochastic matrix: any two row vertices can be connected by alternating positive overlap edges. By the Perron–Frobenius theorem, its eigenvalue \(1\) is simple and every other eigenvalue is strictly below \(1\). (It is positive semidefinite, so no negative eigenvalues.) Therefore the leading singular value \(s_1(B_j)=1\) is simple and all remaining singular values satisfy \(s_k(B_j)<1\). In particular, at \(r=1\), each block of \(G_1\) contributes exactly one zero eigenvalue.

**4. Entropy slopes and inertia.** For fixed \(j\), the entries \((B_j)_{ab}^{r}\) depend real-analytically on \(r\) in a neighborhood of \(1\), with identically zero entries omitted from differentiation. The top singular value \(s_j(r)=\|B_j^{\circ r}\|_2\) is simple there by the previous step and hence analytic. Its left and right unit singular vectors at \(r=1\) are both \(d_j^{-1/2}\mathbf1\). Standard differentiation of a simple singular value gives

\[
s_j'(1)=\frac1{d_j}\sum_{a,b}(B_j)_{ab}\log (B_j)_{ab}=-h_j.
\]

Every \(h_j\ge0\), with \(h_j=0\) precisely for a singleton component: a connected doubly stochastic block of size greater than one contains a fractional positive entry. All non-leading singular values remain strictly below one for \(r\) close enough to one. Hence the largest singular value among all blocks is \(\max_j[1-(r-1)h_j+O((r-1)^2)]\). Taking the maximum of finitely many component expansions proves the two one-sided edge formulas. The sign and multiplicity conclusions follow because a nontrivial component's single leading singular value crosses \(1\) from above to below when \(r\) increases through one, whereas a singleton component remains identically \(1\). This proves all statements.

## Verification

The independent finite-dimensional identities can be reproduced with `python checks/two_basis_trace_kernel_check.py`, requiring Python 3 and NumPy. The checker tests exact block-versus-singular-value formulas numerically for Fourier bases, seeded Haar unitaries, reducible direct sums, and monomial bases, together with the claimed one-sided entropy slopes. A successful run prints `TWO_BASIS_TRACE_KERNEL_CHECK_OK 2262`. The analytical argument above, not the finite calculations, proves the statements for all finite dimensions and exponents.

## Relationship to prior work

Fannes, de Melo, Roga, and Życzkowski (2012, their Proposition 4 and equations (35)–(39)) **already use two mutually unbiased orthonormal bases** as a witness that fractional-power fidelity matrices fail to be universally positive. The Fourier-basis example and its negative quadratic form, including the \(1-d^{1-r}\) edge in the uniform case, are therefore **not claimed as new**. Their work also establishes positivity at exponent one for arbitrary pure-state ensembles. Vuong and Osaka (2026, Theorem 1.1 and Remark 2.4) prove the sharp three-point positive kernel theorem and provide a specific four-point counterexample. Neither inspected source states the entire two-basis positivity and nullity classification for arbitrary overlap supports or the separate mean-entropy slopes governing the critical spectral edge. These are the claimed additions. The argument uses classical Jensen, singular-value and Perron–Frobenius theory, which are not claimed as new.

## Limitations

Originality is a best-knowledge conclusion from the inspected primary sources and focused searches, not a guarantee of bibliographic uniqueness. The support-component entropy derivative can be recognized as a finite-state perturbation of a stochastic matrix, so an older formulation in matrix scaling, transfer-operator pressure, or quantum fidelity may subsume some aspects. The new contribution is the combined complete two-basis kernel classification and explicit component-sensitive critical spectral inertia. No uniform higher-order remainder bound over varying dimensions/bases is claimed. Numerical checks do not constitute proof. Independent mathematical review has not been performed.

## References

1. M. Fannes, F. de Melo, W. Roga, K. Życzkowski, “Matrices of fidelities for ensembles of quantum states and the Holevo quantity”, *Quantum Information and Computation* **12** (2012), 472–489, Proposition 4. https://www.rintonpress.com/xxqic12/qic-12-56/0472-0489.pdf
2. T. D. Vuong and H. Osaka, “Three-Point Trace Positivity: Schatten Norm Compression and Interpolating Metrics”, arXiv:2610.11021v1 (public 2026-10-08), Theorem 1.1 and Remark 2.4; accessible full text version 2. https://arxiv.org/html/2610.11021v2
3. W. Tadej and K. Życzkowski, “A concise guide to complex Hadamard matrices”, *Open Systems & Information Dynamics* **13** (2006), 133–177; reference for mutually unbiased unitary bases and complex Hadamard matrices.
