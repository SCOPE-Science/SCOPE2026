# A support trichotomy for norm attainment on scalar \(\ell_p\)-extensions of \(c_0\)

## Finding
Let \(a=(a_n)_{n\ge0}\) be any nonnegative real sequence with \(\sum_{n=0}^\infty a_n=1\). For \(1\le p<\infty\) put
\[
X_p=c_0(\mathbb N_0;\mathbb R)\oplus_p\mathbb R,\qquad
\|(x,t)\|_p=(\|x\|_\infty^p+|t|^p)^{1/p},
\]
and define
\[
T_{p,a}(x,t)=\big((x_n-x_{n+1})_{n\ge0},\ \sum_{n=0}^\infty a_nx_n\big).
\]
The following exact norm and norm-attainment classification holds:
\[
\|T_{p,a}\|=\|T_{p,a}^{**}\|=(2^p+1)^{1/p}.
\]
The original operator attains its norm exactly when \(\operatorname{supp}a\) is finite, and its second adjoint attains its norm exactly when \(\operatorname{supp}a\ne\mathbb N_0\). Hence the three possibilities are finite support (both attain), infinite proper support (only the second adjoint attains), and full support (neither attains).

For \(p=\infty\) use the maximum norm on the same direct sum. The displayed operator has norm \(2\), attained already on the original space. Furthermore, the published universal second-adjoint attainment theorem for \(c_0\) applies because \(X_\infty\) is isometric to \(c_0\). For every \(\varepsilon>0\) a sufficiently large finite \(p\) gives a norm at most \(1+\varepsilon\) times the usual \(c_0\) norm, but full-support \(a\) still yields a non-norm-attaining second adjoint.

## Assumptions and scope
All spaces and operators are real. The index set is \(\mathbb N_0=\{0,1,2,\ldots\}\). The notation \(c_0\) denotes real null sequences with the supremum norm; \(\ell_\infty\) denotes real bounded sequences. All \(a_n\) are nonnegative, not necessarily strictly positive, and their sum equals one. For finite \(p\), the domain and codomain are each \(X_p\). By standard duality, \(X_p^{**}\) identifies isometrically with \(\ell_\infty\oplus_p\mathbb R\), including \(p=1\), because \(\mathbb R\) is reflexive and this is a finite direct sum. The result distinguishes ordinary norm attainment from second-adjoint norm attainment; it makes no assertion about quasi norm attainment.

## Proof
**1. Boundedness and sharp norm.** Put \((Ax)_n=x_n-x_{n+1}\) and \(L_a(x)=\sum a_nx_n\). Then \(A:c_0\to c_0\), \(\|A\|=2\), and \(\|L_a\|=1\). For \((x,t)\in X_p\),
\[
\|T_{p,a}(x,t)\|_p^p=\|Ax\|_\infty^p+|L_a(x)|^p
\le(2^p+1)\|x\|_\infty^p\le(2^p+1)\|(x,t)\|_p^p.
\]
For each integer \(N\ge0\), choose \(x^{(N)}\in c_0\) equal to \(1\) at indices \(0,\ldots,N\), to \(-1\) at index \(N+1\), and to \(0\) elsewhere. Then \(\|x^{(N)}\|_\infty=1\), \(\|Ax^{(N)}\|_\infty=2\), and
\[
L_a(x^{(N)})=\sum_{j=0}^{N}a_j-a_{N+1}\longrightarrow1.
\]
Thus the upper bound is sharp. The same norm holds for the second adjoint by norm preservation under adjoints; alternatively the displayed witnesses already lie in the bidual ball.

**2. Identifying the second adjoint.** Both \(A\) and \(L_a\) are represented by countably supported \(\ell_1\) coordinate functionals. Their canonical bidual extensions have identical formulas on \(\ell_\infty\). Consequently
\[
T_{p,a}^{**}(x,t)=\big((x_n-x_{n+1})_{n\ge0},\ \sum_{n\ge0}a_nx_n\big),
\qquad (x,t)\in\ell_\infty\oplus_p\mathbb R.
\]

**3. Characterizing equality.** For finite \(p\), any unit vector on which the sharp norm is attained must satisfy simultaneously
\[
\|x\|_\infty=1,\quad t=0,\quad\|Ax\|_\infty=2,\quad |L_a(x)|=1.
\]
Indeed every inequality in Step 1 must then be an equality. Because \(a\) is a nonnegative probability sequence, \(|L_a(x)|=1\) for \(\|x\|_\infty\le1\) holds precisely when all coordinates with \(a_n>0\) equal the same sign \(+1\) or \(-1\). This follows from \(\sum a_n(1\mp x_n)=0\) and nonnegativity of every summand.

If every \(a_n>0\), the last equality forces \(x\) to be a constant sequence of modulus one, hence \(Ax=0\). Thus the bidual fails norm attainment. Conversely, if \(a_k=0\) for some index \(k\), choose \(x_n=1\) at every \(n\ne k\) and \(x_k=-1\). This bounded sequence satisfies \(|L_a(x)|=1\) and \(\|Ax\|_\infty=2\), so \((x,0)\in X_p^{**}\) attains the norm.

In the original space \(c_0\), equality \(|L_a(x)|=1\) is impossible when \(a\) has infinite support, since it would force infinitely many \(x_n\) to equal a common sign of modulus one while \(x_n\to0\). If \(a\) has finite support, choose a finitely supported \(x\) that equals \(1\) on that support and also takes the successive values \(1,-1\) at two consecutive indices beyond it; then \(\|Ax\|_\infty=2\) and \(L_a(x)=1\). This proves both classifications.

**4. Endpoint and quantitative renorming.** For \(p=\infty\), \(\|T_{\infty,a}\|=\max\{2,1\}=2\), attained, for instance, by \(x=(1,-1,0,\ldots)\). The coordinate interleaving \(J(x,t)=(t,x_0,x_1,\ldots)\) identifies \(X_\infty\) isometrically with ordinary \(c_0\). For each finite \(p\),
\[
\|(x,t)\|_\infty\le\|(x,t)\|_p\le 2^{1/p}\|(x,t)\|_\infty.
\]
Taking \(p>\log(2)/\log(1+\varepsilon)\) makes the distortion strictly smaller than \(1+\varepsilon\). Choosing, for instance, \(a_n=2^{-n-1}\), whose support is all of \(\mathbb N_0\), makes the associated second adjoint non-norm-attaining for every such finite \(p\). The published result \(\mathcal L(c_0,c_0)=\mathrm{NA}_2(c_0,c_0)\) identifies the contrasting endpoint. This completes the proof.

## Verification
Every logical dependency is explicit: the finite-support witnesses give the exact norm without numerical optimization; the bidual formula is obtained by \(\ell_1\) duality; equality is characterized by positivity of the probability coefficients. The case \(p=1\) uses equality of two nonnegative real summands, exactly as the other finite exponents. The limit \(p\to\infty\) does not identify the norm-attainment properties at finite \(p\). A supplementary standalone finite-truncation diagnostic is provided in `CHECKER.py`, but no finite test is substituted for the proof over infinite sequences.

## Relationship to prior work
Dantas, Jung and Martín (arXiv:2609.00794, initially public September 1, 2026) establish universal second-adjoint norm attainment on real \(c_0\) (Theorem 3.3) and on vector-valued \(c_0\)-sums of finite-dimensional blocks (Remark 3.4). Their Theorem 5.1 proves that a suitable equivalent renorming of any infinite-dimensional Banach space can destroy this property. These statements do not specify arbitrarily small distortion near the original \(c_0\) norm or the above scalar \(\ell_p\)-extension trichotomy. The new assertion is a quantitative near-isometric stability boundary, not a new proof of their general renorming theorem.

Related studies of full-support versus finite-support norm-attainment phenomena for other positive rank-one or convolution operators concern different operator formulas, target norms and/or quasi norm attainment; these support patterns alone do not imply the present exact second-adjoint classification. They remain relevant prior art for the underlying obstruction mechanism.

## Limitations
Only real \(c_0\) with one scalar \(\ell_p\)-summand and a nonnegative \(\ell_1\) probability functional is covered. No universal classification of all equivalent norms, all finite-dimensional summands, projections, or complex analogues is claimed. The published universal endpoint at \(p=\infty\) is used as prior input. A broader pre-existing theorem about near-isometric renormings may yet subsume the quantitative corollary; independent priority verification has not been performed.

## References
1. S. Dantas, M. Jung, M. Martín, *On operators whose adjoints or second adjoints attain their norms*, arXiv:2609.00794 (first submitted September 1, 2026), especially Theorem 3.3, Remark 3.4 and Theorem 5.1. https://arxiv.org/abs/2609.00794
2. M. I. Ostrovskii, *Extremal problems for operators in Banach spaces arising in the study of linear operator pencils. II*, Integral Equations and Operator Theory 51 (2005), 553–564, cited by Dantas–Jung–Martín as the predecessor of their renorming construction.
