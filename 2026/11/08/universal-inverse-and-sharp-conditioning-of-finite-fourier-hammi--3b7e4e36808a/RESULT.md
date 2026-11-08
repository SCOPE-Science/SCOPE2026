# Universal inverse and sharp conditioning of finite Fourier Hamming-ball minors

## Finding
Let \(A\) be any finite abelian group of order \(q\ge2\), equipped with a **symmetric perfect bicharacter** \(b:A\times A\to\mathbb C\), and let \(B_{n,r}=\{x\in A^n:|\operatorname{supp}(x)|\le r\}\). Define the unnormalized square Fourier sampling matrix
\[
H_{n,r}(x,y)=b_n(x,y):=\prod_{i=1}^n b(x_i,y_i),\qquad x,y\in B_{n,r}.
\]
For every \(0\le r\le n\), this matrix is invertible. For \(x,y\in B_{n,r}\), put \(u=|\operatorname{supp}(x)\cup\operatorname{supp}(y)|\). Then its **entire inverse kernel** is
\[
(H_{n,r}^{-1})(x,y)=
\begin{cases}
q^{-u}\overline{b_n(x,y)}\displaystyle\sum_{j=0}^{r-u}\binom{n-u}{j}\left(-\frac{q-1}{q}\right)^j,&u\le r,\\[3pt]
0,&u>r.
\end{cases}
\tag{1}
\]
In particular the inverse has an exact support-union sparsity rule, and its entries depend on \(A\) only through \(q\) and the Fourier phase.

For every **fixed** group order \(q\ge2\) and fixed integer radius \(r\ge1\), as \(n\to\infty\), the spectral condition number satisfies the **sharp** law
\[
\boxed{\ \lim_{n\to\infty}\frac{\kappa_2(H_{n,r})}{n^{2r}}=
\frac{(q-1)^{2r}}{q^r(r!)^2}.\ }
\tag{2}
\]
The largest singular vectors become asymptotically constant on the ball, while the left and right smallest-singular-value vectors become asymptotically supported at its origin. These statements are in Euclidean norm, up to arbitrary unit phases, and hold for every fixed \(q,r\) as \(n\to\infty\).

The exact Frobenius norm of the inverse is also determined. With \(S_{m,s}=\sum_{j=0}^{s}\binom mj[-(q-1)/q]^j\),
\[
\|H_{n,r}^{-1}\|_F^2=\sum_{u=0}^r\binom nu(q^2-1)^u q^{-2u}|S_{n-u,r-u}|^2.
\tag{3}
\]

## Assumptions and scope
A symmetric perfect bicharacter obeys \(b(x,y)=b(y,x)\), is multiplicative in both variables, and satisfies \(\sum_{y\in A}b(x,y)=q\mathbf1_{\{x=0\}}\). Every finite abelian group admits such a pairing by decomposition into cyclic factors. The matrix uses the **unnormalized** characters, and condition numbers use singular values in the standard counting-measure Euclidean norm. The exact inverse holds for every finite \(n\ge1\), every \(0\le r\le n\), and every such group and pairing. The asymptotic and singular-vector limits require \(q,r\) fixed and \(n\to\infty\); no uniformity in growing radius or group order is claimed.

## Proof
**1. A one-coordinate Schur complement.** Write \(A^*=A\setminus\{0\}\), and let \(W=(b(a,c))_{a,c\in A}\) be the full, unnormalized Fourier matrix. In block order \(\{0\}\sqcup A^*\),
\[
W=\begin{pmatrix}1&\mathbf1^{\mathsf T}\\\mathbf1&W_*\end{pmatrix},\qquad K:=W_*-\mathbf1\mathbf1^{\mathsf T}.
\]
By character orthogonality and symmetry, \(W^{-1}(a,c)=q^{-1}\overline{b(a,c)}\). The lower-right block of \(W^{-1}\) is the inverse of the Schur complement \(K\), so
\[
K^{-1}(a,c)=q^{-1}\overline{b(a,c)},\qquad a,c\ne0.\tag{4}
\]
In particular, \(K\) is invertible for every finite abelian group, with no field hypothesis.

**2. Support-poset factorization.** Regard an element of \(B_{n,r}\) as a partial assignment with nonzero labels, ordered by extension: \(z\preccurlyeq x\) when each coordinate in the support of \(z\) agrees with the corresponding coordinate of \(x\). Form its zeta matrix \(Z_{x,z}=\mathbf1_{\{z\preccurlyeq x\}}\). For each fixed support \(T\subseteq[n]\), let \(D_T=K^{\otimes |T|}\) on all assignments with that exact support; for \(T=\varnothing\), \(D_T=[1]\). Let \(D=\bigoplus_{|T|\le r}D_T\). The product expansion
\[
b_n(x,y)=\prod_{i=1}^n\bigl(1+\mathbf1_{\{x_i\ne0,y_i\ne0\}}(b(x_i,y_i)-1)\bigr)
\]
gives exactly \(H_{n,r}=ZDZ^{\mathsf T}\). Ordered by support size, \(Z\) is unitriangular. Equation (4) therefore proves invertibility and
\[
H_{n,r}^{-1}=Z^{-\mathsf T}D^{-1}Z^{-1}.
\tag{5}
\]
Each interval in the extension poset is a Boolean lattice, so \((Z^{-1})_{x,z}=(-1)^{|\operatorname{supp}(x)|-|\operatorname{supp}(z)|}\mathbf1_{\{z\preccurlyeq x\}}\).

**3. Entrywise summation.** For a term of (5) to contribute to the entry indexed by \(x,y\), its intermediate common support \(T\) must contain \(\operatorname{supp}(x)\cup\operatorname{supp}(y)\) and have size at most \(r\). Thus there is no contribution when \(u>r\). By (4), a coordinate in both supports contributes \(\overline{b(x_i,y_i)}\), a coordinate in just one contributes \(-1\) after summing a free nonzero label, and a coordinate in neither but included in \(T\) contributes \(-(q-1)\). The signs from these sums cancel the two Möbius signs, because \(|\operatorname{supp}(x)|+|\operatorname{supp}(y)|+|\operatorname{supp}(x)\triangle\operatorname{supp}(y)|\) is even. Each extra coordinate contributes a factor \(-(q-1)/q\); there are \(\binom{n-u}{j}\) choices for \(j\) extras. This proves (1). Counting ordered pairs \((x,y)\) with support union of size \(u\), of which there are \(\binom nu(q^2-1)^u\), proves (3).

**4. Sharp conditioning.** Set \(N_{n,r}=|B_{n,r}|=\sum_{j=0}^r\binom nj(q-1)^j\). Because every entry of \(H_{n,r}\) has modulus one, \(\|H_{n,r}\|_2\le\|H_{n,r}\|_F=N_{n,r}\). If two ball points have disjoint supports their Fourier entry is one; for fixed \(q,r\), the proportion of pairs with intersecting supports is \(O_{q,r}(n^{-1})\). Evaluating the bilinear form against the normalized all-ones vector gives
\[
\|H_{n,r}\|_2=N_{n,r}(1+O_{q,r}(n^{-1}))=\frac{(q-1)^r}{r!}n^r(1+O_{q,r}(n^{-1})).\tag{6}
\]
For fixed \(q,r\), \(S_{n,r}=(-1)^r[(q-1)/q]^rn^r/r!+O_{q,r}(n^{r-1})\). In (3), the \(u=0\) term is \(|S_{n,r}|^2\), while the sum of terms with \(u\ge1\) is \(O_{q,r}(n^{2r-1})\). The absolute value of the inverse's entry at the origin is exactly \(|S_{n,r}|\), and the operator norm is bounded above by the Frobenius norm. Hence
\[
\|H_{n,r}^{-1}\|_2=\frac{(q-1)^r}{q^rr!}n^r(1+O_{q,r}(n^{-1})).\tag{7}
\]
Multiplying (6) and (7) proves (2).

**5. Extremal singular-vector localization.** The Frobenius distance between \(H_{n,r}\) and the all-ones matrix is \(O_{q,r}(N_{n,r}n^{-1/2})\), since only intersecting-support pairs contribute. Thus the normalized top singular space approaches the constant vector. By (3) and the exact origin entry, \(H_{n,r}^{-1}-S_{n,r}e_0e_0^{\mathsf T}\) has Frobenius norm \(O_{q,r}(n^{r-1/2})\), while \(|S_{n,r}|\asymp n^r\). A rank-one singular-value perturbation bound gives convergence of the top singular vectors of the inverse, equivalently the bottom singular vectors of \(H_{n,r}\), to \(e_0\). The gaps are asymptotically strict, so these extreme singular spaces are one-dimensional for sufficiently large \(n\).

## Verification
A standalone script `hamming_ball_fourier_check.py` constructs the Fourier minor and the closed-form inverse independently. It performs exact two-sided matrix-product verifications on three small binary and order-four groups, including cyclic \(\mathbb Z_4\) and the nonisomorphic group \(\mathbb Z_2^2\). It also checks numerical inversion and the exact Frobenius identity on six further parameter sets, including composite order six. Its terminal marker is `FOURIER_HAMMING_BALL_INVERSE_CHECKS_PASS`. These finite tests are consistency checks, not proofs of the all-parameter statement or its limiting law.

## Relationship to prior work
Delvaux and Van Barel study rank-deficient submatrices of Kronecker Fourier matrices and derive extremal support-size inequalities; their central invariant is **maximal rank deficiency**, not a closed inverse kernel on a principal Hamming ball or a sharp condition-number limit. Gluesing-Luerssen develops Hamming-partition Fourier duality and Krawtchouk/MacWilliams identities, not the inversion of the full principal ball submatrix. Numerical studies of contiguous Fourier submatrices concern a different geometry. A previously obtained complete spectrum for the binary radius-two ball implies the \(q=2,r=2\) conditioning instance of (2), but does not give (1) for general groups or (2) for arbitrary radii. Conversely, (1) does not claim its complete finite-dimensional eigenvalue spectrum. Nearby published records on **shell** sampling and first-band restriction are distinct operators; they do not assert the union-support inverse kernel. A general inverse-of-zeta-compressed-character-table identity, if already in the literature, would limit priority; this remains a residual historical risk.

## Limitations
The leading constant in (2) is a fixed-\(q\), fixed-\(r\) asymptotic, not a uniform bound as \(r\) or \(q\) grows. The theorem does not provide the full singular-value spectrum, finite-size exact condition numbers, or a numerical stability algorithm. Small-parameter checks have limited coverage. Independent mathematical validation and exhaustive historical-priority certification have not been performed.

## References
1. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, Technical Report TW 477 (15 November 2006); Linear Algebra Appl. 426 (2007), 349–367, DOI: 10.1016/j.laa.2007.05.009. Public preprint: https://citeseerx.ist.psu.edu/document?doi=8e34019b75494fa56d9b8791527fcaed304a7ff9&repid=rep1&type=pdf.
2. H. Gluesing-Luerssen, *Fourier-Reflexive Partitions and MacWilliams Identities for Additive Codes*, arXiv:1304.1207 (first version 3 April 2013). https://arxiv.org/abs/1304.1207.
3. A. H. Barnett, *How exponentially ill-conditioned are contiguous submatrices of the Fourier matrix?*, arXiv:2004.09643 (2020), SIAM Rev. 64 (2022), 105–131. https://arxiv.org/abs/2004.09643.
4. S. Dirckx, D. Huybrechs, and R. Ongenae, *On the computation of the SVD of Fourier submatrices*, arXiv:2208.12583 (2022). https://arxiv.org/abs/2208.12583.
