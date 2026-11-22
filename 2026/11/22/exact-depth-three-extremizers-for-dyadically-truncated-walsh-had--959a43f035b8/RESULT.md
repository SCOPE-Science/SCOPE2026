# Exact depth-three extremizers for dyadically truncated Walsh–Hadamard matrices

## Finding

Let \(W\) be the normalized \(8\times8\) Walsh–Hadamard matrix in Paley column order, with rows and columns numbered \(0,\ldots,7\). Independently choose for each column \(j\) a retained prefix length \(\ell_j\in\{1,2,4,8\}\), and put zeros below that prefix. Denote the resulting real matrix by \(T_\ell\). Then the exact maximum over **all** \(4^8=65{,}536\) length vectors is
\[
\max_{\ell\in\{1,2,4,8\}^{8}}\|T_\ell\|_{2\to2}^2=\zeta,
\quad 32\zeta^3-64\zeta^2+16\zeta-1=0,
\quad \zeta=1.719840461515738\ldots,
\]
where \(\zeta\) is the largest real zero. Thus the largest operator norm is \(1.311426879973008\ldots\). Exactly eight length vectors attain it:
\[
\ell_j=(8,4,2,2,1,1,1,1)_{j\oplus a},\qquad a=0,1,\dots,7,
\]
where \(j\oplus a\) is bitwise exclusive-or on the three-bit labels. For **every other** length vector there is a strict certified gap
\[
\|T_\ell\|_{2\to2}^2 < 17/10 < \zeta.
\]
This gives the complete finite cutoff at three binary levels and all its exact maximizers; no claim is made for higher levels.

## Assumptions and scope

Rows of \(W\) are in the Sylvester recursion order, corresponding to Walsh–Paley characters with binary vector labels: starting with \(W_1=2^{-1/2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}\), set \(W_{n+1}=2^{-1/2}\begin{pmatrix}W_n&W_n\\W_n&-W_n\end{pmatrix}\). At size eight, the matrix \(W_3\) has orthonormal columns. Retain exactly rows \(0\) through \(\ell_j-1\) of column \(j\), zeroing all remaining entries. Both the truncation and the operator norm use these conventions. The quantifiers range over all \(8\)-tuples with entries in \(\{1,2,4,8\}\), with no branch restriction.

## Proof

**1. Exact Gram formula.** Write \(H_\ell=8T_\ell^{\mathsf T}T_\ell\). For \(i,j\in\{0,\ldots,7\}\), put \(m=\min(\ell_i,\ell_j)\). The first \(m\) rows of two Walsh columns are either identical or orthogonal, since \(m\) is a power of two and these rows form a smaller Walsh system repeated over consecutive column blocks. Consequently
\[
(H_\ell)_{ij}=
\begin{cases}
 m,&\left\lfloor i/(8/m)\right\rfloor=\left\lfloor j/(8/m)\right\rfloor,\\
 0,&\text{otherwise}.
\end{cases}
\]
The supplied self-contained checker independently reconstructs the signed Walsh matrix and checks this identity for every column pair and all possible prefix-length pairs before using it.

**2. An exact separation certificate.** Consider the symmetric integer matrix \(K_\ell=68I_8-5H_\ell=40[(17/10)I_8-T_\ell^{\mathsf T}T_\ell]\). Sylvester's criterion gives
\[
K_\ell\succ0\quad\Longleftrightarrow\quad\|T_\ell\|_{2\to2}^2<17/10.
\]
The included `verify.py` enumerates all \(4^8\) vectors in a Cartesian product, forms \(H_\ell\) via the displayed integer formula, and tests every leading principal minor of \(K_\ell\) using exact fraction-free Bareiss elimination and exact integer divisibility assertions. This is an exhaustive finite proof certificate: **precisely** the eight vectors \(\ell_j=(8,4,2,2,1,1,1,1)_{j\oplus a}\) fail strict positive definiteness, and every other vector passes. All operations in this census are on integers and the loop has no early exit.

**3. Exact spectrum of the eight survivors.** For each survivor, exact Faddeev–LeVerrier integer arithmetic in the checker obtains
\[
\det(tI_8-H_\ell)=t^4(t-4)(t^3-16t^2+32t-16).
\]
Let \(q(t)=t^3-16t^2+32t-16\). Exact substitutions give \(q(68/5)=-3088/125<0\) and \(q(14)=40>0\), so \(H_\ell\) has an eigenvalue above \(68/5\), and hence \(\|T_\ell\|_{2\to2}^2>17/10\). Every survivor has the same characteristic polynomial, proving that all eight have equal operator norm, strictly larger than any other length vector. Its largest root divided by eight is precisely \(\zeta\), and dividing the displayed cubic by the normalization yields the equation for \(\zeta\). This proves both sharpness and the exhaustive equality classification.

## Verification

Run `python3 verify.py` with Python 3 standard library only, from the directory containing this document and `verify.py`. The checker reconstructs the size-eight Walsh matrix, independently validates the Gram formula, evaluates all \(65{,}536\) length vectors by exact fraction-free Sylvester tests, asserts the **set equality** of the eight exceptional vectors, and verifies their exact characteristic polynomials. A printed successful result is supported by these explicit all-input assertions, not floating-point experiments. Decimal values above are supplementary approximations; all comparisons and the optimality assertion are proved exactly.

## Relationship to prior work

Lakey, *Towards direct \(L^2\)-bounds for maximal partial sums of Walsh–Fourier series: The case of dyadic partial sums* (arXiv:2602.17627, first publicly posted 19 February 2026), introduces dyadically truncated Walsh–Hadamard operators, identifies the standard single-branch candidate, and states its unrestricted optimality as a conjectural direction, with analytical reductions and numerical evidence. The present claim resolves the exact, **fully quantified eight-column instance** by an integer exhaustive certificate; it does not assert the general conjecture. Hogan and Lakey, *An Eigenvector Problem Arising in the Study of Convergence of Walsh–Fourier Series* (2026), analyze a compressed family associated with the standard truncation and its asymptotic eigenvalue behavior, not the complete depth-three all-truncation equality classification. Searches for alias formulations, matrix norm tables, Sylvester–Hadamard and Walsh partial sums, and exact characteristic polynomials found no demonstrated prior implication of this classification. Absence in searches is not a general uniqueness guarantee.

## Limitations

This is a rigorously exhaustive **finite** classification for the precise \(8\times8\) family, not an infinite-dimensional operator theorem and not a result for arbitrary/non-dyadic prefix lengths. A numerical approximation does not enter the proof. It remains possible that an equivalent enumeration appears in unindexed or subsequent work. No independent mathematical audit has been performed.

## References

1. Joseph D. Lakey, *Towards direct \(L^2\)-bounds for maximal partial sums of Walsh–Fourier series: The case of dyadic partial sums*, arXiv:2602.17627 (2026), https://arxiv.org/html/2602.17627v1 ; first posted 19 February 2026, https://arxiv.org/abs/2602.17627.
2. Jeffrey A. Hogan and Joseph D. Lakey, *An Eigenvector Problem Arising in the Study of Convergence of Walsh–Fourier Series*, Mathematics 14(5), 829 (2026), https://doi.org/10.3390/math14050829.
