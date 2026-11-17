# Rigidity of Schur-multiplier norming weights for projective-plane incidence masks

## Finding
Let \(\Pi\) be any finite projective plane of order \(q\ge2\), with \(v=q^2+q+1\) points and \(v\) lines, and let \(B\) be its point-by-line incidence matrix. For probability vectors \(r\) on points and \(c\) on lines, define
\[
F_\Pi(r,c)=\|D_{\sqrt r}B D_{\sqrt c}\|_{\mathcal S_1}.
\]
Then
\[
F_\Pi(r,c)\le \frac{q+1+(v-1)\sqrt q}{v},
\]
with equality **if and only if** \(r\) and \(c\) are both uniform. Consequently, the complex operator-norm Schur multiplier associated with \(B\) has norm
\[
\|S_B\|=\frac{q+1+(v-1)\sqrt q}{v},
\]
and a rank-one trace-class operator \(\xi\eta^*\), where \(\|\xi\|_2=\|\eta\|_2=1\), norms the adjoint Schur action on trace class exactly when every point coordinate of \(\xi\) and every line coordinate of \(\eta\) has modulus \(1/\sqrt v\). All coordinate phases are unrestricted. In particular, the optimal **probability weights** are unique, even though the norming rank-one operators admit arbitrary row and column phases.

## Assumptions and scope
A finite projective plane of order \(q\ge2\) has \(v=q^2+q+1\) points and lines, each point belongs to \(q+1\) lines, each line contains \(q+1\) points, and each pair of distinct points lies on exactly one common line. No Desarguesian, prime-power, or group-transitivity assumption is made. \(B_{i\ell}=1\) for incidence and zero otherwise. Diagonal matrices are denoted \(D_r\). The Schatten trace norm is the sum of singular values. The complex Schur multiplier \(S_B\) acts entrywise on \(v\)-square matrices with the operator norm. The probability vectors are nonnegative, including boundary cases, and each sums to one.

## Proof
Write \(k=q+1\), \(a=\sqrt q\), and \(b=(k-a)/v>0\). The projective-plane axioms give
\[
BB^*=B^*B=qI+J,
\]
where \(J\) is the all-ones matrix. Therefore the positive square root of \(BB^*\) is
\[
S=(BB^*)^{1/2}=aI+bJ,
\]
since its eigenvalue is \(k\) on the constants and \(a\) on their orthogonal complement. In particular, \(B\) is invertible, and both \(S\) and \((B^*B)^{1/2}\) have constant diagonal \(a+b\).

Factor \(B=X^*Y\) with \(X=S^{1/2}\) and \(Y=S^{-1/2}B\). For any two probability vectors put \(A=XD_{\sqrt r}\) and \(C=YD_{\sqrt c}\). The trace-norm factorization bound gives
\[
\|D_{\sqrt r}BD_{\sqrt c}\|_{\mathcal S_1}=\|A^*C\|_{\mathcal S_1}
\le\frac{\|A\|_F^2+\|C\|_F^2}{2}
=\frac{\operatorname{Tr}(D_rS)+\operatorname{Tr}(D_cB^*S^{-1}B)}2=a+b.
\]
Here \(B^*S^{-1}B=(B^*B)^{1/2}\), and the last equality uses the constant diagonals and the unit sums. For uniform \(r,c\), the weighted matrix equals \(B/v\), and its singular values are \(k/v\) once and \(a/v\) with multiplicity \(v-1\). Thus the upper bound is attained, since
\[
a+b=\frac{k+(v-1)a}{v}.
\]

To characterize equality **including zero weights**, use the elementary inequality for arbitrary square matrices \(A,C\):
\[
\|A^*C\|_{\mathcal S_1}\le\tfrac12(\|A\|_F^2+\|C\|_F^2).
\]
The trace-norm unitary polar formula chooses a unitary \(U\) satisfying \(\operatorname{Re}\operatorname{Tr}(A^*CU)=\|A^*C\|_{\mathcal S_1}\). Therefore equality forces \(\|A-CU\|_F^2=0\), and hence \(AA^*=CC^*\). Substituting the above factorization and conjugating by \(S^{1/2}\) yields the necessary identity
\[
S D_r S=B D_c B^*.
\]
For two distinct points \(i,j\), the \((i,j)\)-entry on the left equals
\[
ab(r_i+r_j)+b^2,
\]
while the right side equals \(c_{\ell(i,j)}\), the weight of their **unique** common line. Fix any line \(\ell\). Because it contains \(q+1\ge3\) points, choose distinct \(i,j,h\) on it. Equality of the values for pairs \((i,j)\), \((i,h)\), and \((j,h)\), together with \(ab>0\), forces \(r_i=r_j=r_h\). Varying the triple shows that every point on \(\ell\) has the same weight. Every two points lie on a line, so all \(r_i\) coincide, and \(r_i=1/v\). The off-diagonal identity then gives \(c_\ell=2ab/v+b^2=1/v\) for every line. Thus uniform weights are the only maximizing pair; boundary weights cannot maximize.

Finally, by trace-class duality and its rank-one extreme-point reduction, the Schur norm is precisely \(\max_{r,c}F_\Pi(r,c)\). For a unit rank-one trace-class operator \(\xi\eta^*\), its Schur image is \(D_\xi B D_{\overline\eta}\), whose trace norm depends only on \(r_i=|\xi_i|^2\) and \(c_\ell=|\eta_\ell|^2\) because diagonal phases are unitary. Hence the uniqueness just proved is exactly the claimed classification of norming rank-one vectors.

## Verification
The argument uses only the finite projective-plane axioms, positive square roots of \(qI+J\), the nuclear–Frobenius factorization inequality with its equality condition, and the rank-one trace-class reduction. Every quantifier and boundary case is included: the equality condition does not require positive weights. The standalone script CHECK.py checks the incidence Gram identities for the projective planes over \(\mathbf F_2\) and \(\mathbf F_3\); these finite diagnostics supplement but do not establish the all-planes theorem.

## Relationship to prior work
Levene's 2026 Lemmas 2.3 and 2.5 give the weighted trace-norm maximization formula and an averaging theorem asserting the **existence** of an invariant optimal weight. For the incidence graph of a projective plane, symmetry (when present) or the displayed factorization already gives the uniform norm value. Neither the averaging lemma nor the displayed general formulas imply uniqueness: the complete-bipartite all-ones matrix has infinitely many optimal weights. The additional equality analysis above exploits uniqueness of the line through two points and the fact that each line contains at least three points. Levene's 2014 small-norm classification concerns a different regime and graph families.

## Limitations
The classification covers **rank-one trace-class normers**, not all possible higher-rank trace-class normers or operator-norm extremizers. The scalar field is complex; analogous real statements require separately checking the real duality convention. The proof assumes a finite projective plane of order at least two and does not establish existence of planes for arbitrary orders. The value of the Schur norm is not claimed as a new independent numerical formula; the contribution is uniqueness of maximizing row/column probability weights and the resulting complete rank-one witness classification. Earlier work on exact norming vectors for structured incidence matrices could contain an equivalent statement and warrants independent priority review.

## References
1. R. H. Levene, *A half-line of Schur idempotent norms*, arXiv:2611.08419v1 (first posted 5 November 2026), especially Lemmas 2.3 and 2.5 and the end of Section 2; https://arxiv.org/html/2611.08419v1 .
2. R. H. Levene, *Norms of idempotent Schur multipliers*, New York Journal of Mathematics 20 (2014), 325–352; https://nyjm.albany.edu/j/2014/20-19.html .
3. C. C. Cowen, P. A. Ferguson, D. K. Jackman, E. A. Sexauer, C. Vogt, and H. J. Woolf, *Finding norms of Hadamard multipliers*, Linear Algebra and Its Applications 247 (1996), 217–235 (cited in reference 1 for rank-one norm reduction).
