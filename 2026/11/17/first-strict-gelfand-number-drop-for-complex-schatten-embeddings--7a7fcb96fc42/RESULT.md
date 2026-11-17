# First strict Gelfand-number drop for complex Schatten embeddings and a real–complex two-by-two gap

## Finding
Let \(n\ge2\) and \(0<p<q\le\infty\), with \(1/\infty:=0\). For the complex-linear Schatten embedding \(I:\mathcal S_p^n(\mathbb C)\to\mathcal S_q^n(\mathbb C)\), the exact initial plateau is
\[
c_k(I)=1\quad(1\le k\le2n-1),\qquad c_{2n}(I)<1.
\]
For order two, all Gelfand numbers can be given explicitly. In the order \(k=1,2,3,4\),
\[
(c_k^{\mathbb C})=(1,1,1,2^{1/q-1/p}),\qquad
(c_k^{\mathbb R})=(1,1,2^{1/q-1/p},2^{1/q-1/p}),
\]
where the real version uses real matrices and real-linear test spaces. Thus the first strict loss of rank-one saturation occurs at different indices over the two fields.

## Assumptions and scope
The Schatten \(p\)-quasi-norm of a matrix \(A\) with singular values \(s_1,\ldots,s_n\) is \(\|A\|_p=(\sum_j s_j^p)^{1/p}\) for finite \(p>0\), and \(\|A\|_\infty=\max_j s_j\). The \(k\)-th Gelfand number of an identity embedding \(I\) is
\[
c_k(I)=\inf_{F\le\mathbb F^{n\times n},\ \operatorname{codim}_{\mathbb F}F<k}\ \sup_{A\in F\setminus\{0\}}\frac{\|A\|_q}{\|A\|_p},
\]
where \(\mathbb F=\mathbb C\) or \(\mathbb R\) and the codimension uses the specified field. The result covers every real exponent \(0<p<q\le\infty\) and does not assume convexity of the source unit ball.

## Proof
**1. Rank one is exactly the equality case.** By monotonicity of finite sequence \(\ell^r\) quasi-norms, \(\|A\|_q\le\|A\|_p\), and the ratio is one for any rank-one \(A\). Conversely, when \(p<q\), equality for nonzero \(A\) forces at most one positive singular value. This follows directly by normalizing \(\sum_j s_j^p=1\) and applying strict inequality \(\sum_j (s_j^p)^{q/p}<1\) if at least two terms are positive (the case \(q=\infty\) uses \(\max_j s_j^p<1\)). Hence a matrix subspace has restriction norm one exactly when it contains a rank-one matrix; if it has no rank-one matrix, compactness of its \(p\)-unit sphere makes that norm strictly below one.

**2. The complex first-drop index.** The projectivized nonzero rank-one matrices form the Segre variety \(\mathbb P^{n-1}\times\mathbb P^{n-1}\subset\mathbb P^{n^2-1}\), of dimension \(2n-2\). By the projective dimension theorem, every projective linear subspace \(\mathbb P^{d-1}\) of dimension at least \((n-1)^2\) intersects this variety: indeed, \((d-1)+(2n-2)\ge n^2-1\) when \(d\ge(n-1)^2+1\). Conversely, there exists a projective linear subspace of dimension \((n-1)^2-1\) disjoint from it. To see existence, let \(N=n^2\) and \(d=(n-1)^2\); in the Grassmannian of \(d\)-dimensional vector subspaces of \(\mathbb C^N\), the condition of containing a fixed projective point has codimension \(N-d=2n-1\). The incidence family over the Segre variety has dimension at most the Grassmannian dimension minus \((2n-1)-(2n-2)=1\); thus its dimension is at most \(\dim\mathrm{Gr}(d,N)-1\). Therefore the incidence projection is a proper closed subset and a disjoint \(d\)-space exists. 

For the \(k\)-th Gelfand number, a minimal-dimensional admissible test space has dimension \(n^2-k+1\). If \(k\le2n-1\) this is at least \((n-1)^2+1\), so every test space contains a rank-one matrix and \(c_k=1\). For \(k=2n\), the disjoint \((n-1)^2\)-dimensional space has codimension \(2n-1<2n\); its restriction norm is strictly below one. This proves both sides of the sharp index threshold for every \(p<q\).

**3. Exact complex order two.** The complex threshold already gives \(c_1=c_2=c_3=1\). On the remaining one-dimensional test space \(\mathbb C I_2\), every nonzero matrix has equal singular values, giving restriction ratio \(2^{1/q-1/p}\). Every nonzero two-by-two matrix has ratio at least \(2^{1/q-1/p}\), by the two-term power-mean inequality. Hence \(c_4=2^{1/q-1/p}\).

**4. Exact real order two.** On the real four-dimensional matrix space, the determinant quadratic form has signature \((2,2)\). Its restriction to any real three-dimensional linear subspace has a nonzero isotropic vector (a three-dimensional subspace cannot be positive or negative definite for this quadratic form; if the restriction is semidefinite it has nonzero kernel, and if indefinite it has a nontrivial zero). Thus every real test space of codimension at most one contains a nonzero rank-one matrix, implying \(c_1=c_2=1\). Let
\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad F=\operatorname{span}_{\mathbb R}\{I_2,J\}.
\]
Every nonzero \(aI_2+bJ\) satisfies \((aI_2+bJ)^T(aI_2+bJ)=(a^2+b^2)I_2\); its singular values are equal. Consequently \(\|I|_F\|=2^{1/q-1/p}\). Since \(\operatorname{codim}_{\mathbb R}F=2\), this shows \(c_3\le2^{1/q-1/p}\), while the universal lower bound established above gives equality. Monotonicity and the exact last Gelfand number then yield \(c_4=2^{1/q-1/p}\).

## Verification
All implications are finite-dimensional analytic statements; no finite numerical experiment is used as proof. The incidence inequality in step 2 can be checked directly: the fixed-point incidence codimension \(2n-1\) exceeds the Segre dimension \(2n-2\). The order-two real construction can be checked by multiplying \(aI_2+bJ\) by its transpose. The singular-value ratio equality cases follow for all real exponents \(0<p<q\le\infty\), including \(p<1\).

## Relationship to prior work
Prochno's 2026 theorem concerns order-of-magnitude estimates for Gelfand numbers of real-matrix Schatten embeddings, including the quasi-Banach range, and explicitly proves a rank-one saturation plateau at least through index \(n\) for order \(n\). Hinrichs, Prochno and Vybíral (2021; publicly available preprint 2020) prove broad asymptotic comparison estimates for real Schatten embeddings. The present exact complex threshold and the contrasting complete real/complex two-by-two sequences refine the field-sensitive beginning of the Gelfand-number spectrum, rather than the existing high-dimensional asymptotic bounds. The Segre dimension and the determinant signature are classical tools; these are not claimed as new results.

## Limitations
The strict inequality at the first-drop index is qualitative for complex orders above two; no sharp size of \(1-c_{2n}\) is established. The general complex plateau is a statement about complex-linear test subspaces, not about real-linear subspaces of complex matrix spaces. Previous works on subspaces avoiding low rank could contain equivalent formulations; the publication-priority comparison is qualified accordingly.

## References
- J. Prochno, *Gelfand numbers of Schatten class embeddings in the quasi-Banach range*, arXiv:2611.08448v1, first public 5 November 2026.
- A. Hinrichs, J. Prochno, J. Vybíral, *Gelfand numbers of embeddings of Schatten classes*, arXiv:2011.06554; *Mathematische Annalen* **380** (2021), 1563–1593.
- Standard projective dimension theorem and the Segre embedding of \(\mathbb P^{n-1}\times\mathbb P^{n-1}\); standard singular-value power-mean comparison.
