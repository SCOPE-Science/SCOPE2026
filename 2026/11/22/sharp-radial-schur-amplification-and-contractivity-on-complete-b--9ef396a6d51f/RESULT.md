# Sharp radial Schur amplification and contractivity on complete bipartite graphs

## Finding
For all integers \(a,b\ge 2\) and real \(t\), consider the symmetric Schur symbol
\[
M_{a,b}(t)=\begin{pmatrix}I_a&tJ_{a,b}\\tJ_{b,a}&I_b\end{pmatrix}.
\]
Its entrywise multiplier on complex matrices satisfies the **sharp** equality
\[
\boxed{\|S_{M_{a,b}(t)}\|_{B\to B}=\|S_{M_{a,b}(t)}\|_{\mathrm{cb}}=\begin{cases}
1,& |t|\le (ab)^{-1/2},\\
1+\dfrac{2(abt^2-1)}{2ab|t|+a+b},& |t|>(ab)^{-1/2}.
\end{cases}}
\]
Thus contractivity is equivalent to complete positivity and occurs exactly at \(|t|\le (ab)^{-1/2}\). On a countably infinite complete bipartite graph, with both parts infinite and the same radial symbol, the operator and completely bounded norms are exactly \(1+|t|\).

## Assumptions and scope
All matrices and operators act on complex Hilbert spaces. The blocks \(I_a,I_b\) are identity matrices and \(J_{a,b}\) consists of ones. The symbol retains diagonal entries, annihilates off-diagonal entries within each bipartition class and multiplies cross-part entries by the real parameter \(t\). For finite \(a,b\), the operator norm is induced by the usual spectral norm on \(B(\mathbb C^{a+b})\); the completely bounded norm takes the supremum over all matrix amplifications. The countable case acts on \(B(\ell^2(\mathbb N\sqcup\mathbb N))\). No normalization by the number of vertices is used. Negative \(t\) is equivalent to positive \(|t|\) under diagonal unitary conjugation of the symbol.

## Proof
**1. Contractive range.** Write \(T=|t|\). Conjugation of the symbol by the diagonal unitary that is \(+1\) on the first part and \(-1\) on the second changes the sign of \(t\) and preserves Schur norms. On vectors orthogonal to constants within either part, \(M_{a,b}(T)\) acts as the identity. On the two normalized part-constant vectors its compression is
\[
\begin{pmatrix}1&T\sqrt{ab}\\T\sqrt{ab}&1\end{pmatrix}.
\]
Consequently the symbol is positive semidefinite precisely when \(abT^2\le 1\). In that regime its Schur map is unital completely positive, and its norm and completely bounded norm are both one. Conversely, any contractive unital Schur map is completely positive when its Hermitian symbol is positive; here necessity in the supercritical region also follows directly from the sharp strict lower bound below.

**2. Explicit upper certificate for the supercritical range.** Assume \(abT^2>1\), and set
\[
D=2abT+a+b,\qquad z=\frac{2(abT^2-1)}{D},\qquad w=(\mathbf1_a,-\mathbf1_b)^\mathsf T,
\qquad P=M_{a,b}(T)+zww^*.
\]
Then \(P-M_{a,b}(T)=zww^*\succeq0\), and every diagonal entry of \(P\) is \(1+z\). On each partwise zero-sum subspace \(P+M_{a,b}(T)\) acts as multiplication by two. On the normalized constant vectors its compression is
\[
\begin{pmatrix}2+az&\sqrt{ab}(2T-z)\\\sqrt{ab}(2T-z)&2+bz\end{pmatrix}.
\]
This matrix is positive semidefinite: the diagonal entries are positive and its determinant equals
\[
(2+az)(2+bz)-ab(2T-z)^2
=4-4abT^2+2(a+b+2abT)z=0.
\]
Thus both \(P+M\) and \(P-M\) are positive. Writing \(Q_{\pm}=(P\pm M)/2\), we have \(M=Q_+-Q_-\) with positive kernels whose diagonal entries are respectively \((2+z)/2\) and \(z/2\). The elementary completely positive Schur-map norm identity therefore proves
\[
\|S_M\|_{\rm cb}\le\|S_{Q_+}\|_{\rm cb}+\|S_{Q_-}\|_{\rm cb}=1+z.
\]

**3. Matching trace-norm witness.** Define two strictly positive rational functions of \(T\):
\[
\alpha=\frac{bT+1}{D},\qquad \beta=\frac{aT+1}{D},\qquad a\alpha+b\beta=1.
\]
Let \(v\in\mathbb R^{a+b}\) have \(a\) entries equal to \(\sqrt\alpha\) and \(b\) entries equal to \(\sqrt\beta\), so \(\|v\|_2=1\). Consider the Hermitian matrix \(B=\operatorname{diag}(v)M\operatorname{diag}(v)\). Its spectrum includes \(\alpha\) with multiplicity \(a-1\) and \(\beta\) with multiplicity \(b-1\). The remaining two eigenvalues are those of
\[
\begin{pmatrix}\alpha&T\sqrt{ab\alpha\beta}\\T\sqrt{ab\alpha\beta}&\beta\end{pmatrix}.
\]
The determinant \(\alpha\beta(1-abT^2)\) is strictly negative. An exact simplification gives
\[
(\alpha-\beta)^2+4abT^2\alpha\beta=T^2.
\]
The sum of the absolute values of these two eigenvalues is therefore \(T\), and the trace norm of the full witness is
\[
\|B\|_1=(a-1)\alpha+(b-1)\beta+T=1+z.
\]
Take \(X=\operatorname{sgn}(B)\), the Hermitian contraction obtained by applying the sign function to the spectrum of \(B\). Since the symbol is real symmetric,
\[
\langle S_M(X)v,v\rangle=\operatorname{Tr}(BX)=\|B\|_1=1+z.
\]
Hence \(\|S_M\|_{B\to B}\ge1+z\), matching the completely bounded upper bound. All finite assertions follow.

**4. Two countably infinite parts.** Let \(W\) be the diagonal unitary taking value \(+1\) on the first infinite part and \(-1\) on the second. If \(E_{\rm diag}\) denotes the diagonal conditional expectation, then entrywise the infinite multiplier satisfies
\[
S_M(X)=E_{\rm diag}(X)+\frac{t}{2}(X-WXW).
\]
The first map has completely bounded norm one, as do the identity and unitary conjugation. Thus \(\|S_M\|_{\rm cb}\le1+|t|\). Conversely, restricting to finite \(a\)-by-\(b\) corners and letting both sizes tend to infinity in the sharp finite formula gives \(\|S_M\|\ge1+|t|\). Both norms are equal to \(1+|t|\), including \(t=0\).

## Verification
The standalone Python 3 standard-library program `VERIFY.py` checks the exact determinant identity, positive-definiteness branch, spectral discriminant, trace-norm witness, the known idempotent boundary, and additional parameter identities by rational arithmetic. Its recorded output is `BICLIQUE_EXACT_IDENTITIES_OK 909454`. The all-parameter and infinite-dimensional conclusions follow from the proof, not the finite checker. In particular, no numerical approximation or finite enumeration is used to infer positivity in untested dimensions.

## Relationship to prior work
Christensen's 2025–2026 positive-order characterization supplies a general variational description of Hermitian Schur norms; the present closed-form positive-kernel and trace-norm certificates solve a specific parameterized graph family. Davidson and Donsig give general factorization and transitive symmetry results, which do not, in the inspected material, state this unbalanced weighted three-parameter law. The known exact complete-bipartite looped projection formula is recovered at \(T=1\), while the previously considered weighted star formula corresponds to a singleton part. Neither boundary slice implies the interpolation-free sharp norm or the nontrivial positivity threshold for both part sizes at least two. González-Pérez and collaborators establish radial transference results on trees for intermediate Schatten classes; the complete bipartite graphs considered here have four-cycles and the present result is at the operator-norm endpoint.

## Limitations
This theorem treats a real-valued radial parameter, not arbitrary complex edge phases or more general three-distance profiles. It concerns operator and completely bounded norms on \(B(\ell^2)\), not sharp intermediate Schatten norms. The formula for the unweighted projection \(T=1\) and the one-part-singleton restriction are already known and are not presented as new. Older symmetric Schur-norm factorization results might contain an equivalent form of the parameter law; no independent priority determination or external mathematical audit has been performed.

## References
1. A. González-Pérez, J. Parcet, J. Pérez García, S. Wang, *Radial Schur multipliers on trees and the failure of Fourier–Schur transference*, arXiv:2610.15881v1 (first public version 2026-10-11), https://arxiv.org/abs/2610.15881.
2. E. Christensen, *The Schur multiplier norm and its dual norm*, arXiv:2505.24670v1 (2025-05-30), Theorem 2.2, https://arxiv.org/abs/2505.24670.
3. K. R. Davidson and A. P. Donsig, *Norms of Schur Multipliers*, arXiv:math/0506073 (2005), https://arxiv.org/abs/math/0506073.
4. R. H. Levene, *Norms of idempotent Schur multipliers*, New York J. Math. 20 (2014), 325–352; arXiv:1302.4849, https://arxiv.org/abs/1302.4849.
5. *Sharp Schur-projection constants for looped complete bipartite graphs* (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-sharp-schur-projection-constants-for-looped-complete-bipartite-g--3c44b45bcba2/RESULT.md.
6. *Exact endpoint Schur norms of radius-one balls on stars of arbitrary degree* (2026), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-endpoint-schur-norms-of-radius-one-balls-on-stars-of-arbit--708bab8a17cc/RESULT.md.
