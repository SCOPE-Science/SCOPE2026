# The sharp nonnormal Ky Fan-two projection constant in dimension three

## Finding

On the real or complex vector space of all \(3\times3\) matrices, let
\[\|A\|_{(2)}=s_1(A)+s_2(A),\qquad s_1(A)\ge s_2(A)\ge s_3(A)\ge0,\]
where \(s_j(A)\) are singular values. The trace-centering projection
\[\mathcal C(A)=A-\frac{\operatorname{tr}A}{3}I_3\]
has exact induced norm
\[\boxed{\|\mathcal C\|_{(2)\to(2)}=\frac12+\frac{\sqrt6}{4}.}\]
Moreover, this is the minimum norm among **all real-linear projections** onto the real subspace of trace-zero matrices, both when the ambient matrices are real and when they are complex (and hence also among complex-linear projections in the complex case).

The maximum is attained by the real, nonnormal rank-one matrix
\[A_*=\begin{pmatrix}\sqrt{3/8}&\sqrt{5/8}&0\\0&0&0\\0&0&0\end{pmatrix},\]
for which \(\|A_*\|_{(2)}=1\). In contrast, the same trace-centering map restricted to real symmetric matrices or complex Hermitian matrices has norm exactly \(1\) in the Ky Fan-two norm. Thus the nonnormal amplification is strict already in the first genuinely intermediate Ky Fan setting.

## Assumptions and scope

All matrices have size \(3\times3\), with entries in either \(\mathbb R\) or \(\mathbb C\). The Ky Fan norm is the unnormalized sum of the largest two singular values. A projection onto the trace-zero space is an idempotent real-linear map that fixes every trace-zero matrix and has exactly that range. The statement is not about matrices of other sizes or other Ky Fan ranks.

## Proof

**1. Three partial-isometry tests suffice.** Let \(\|A\|_{(2)}\le1\), and choose a singular-value decomposition \(A=U\operatorname{diag}(s_1,s_2,s_3)V^*\). Put \(E_j=\operatorname{diag}(\mathbf1_{i\le j})\) and \(R_1=UE_1V^*\), \(R_2=UE_2V^*/2\), \(R_3=UE_3V^*/2\). Then
\[A=(s_1-s_2)R_1+2(s_2-s_3)R_2+2s_3R_3,\]
with nonnegative coefficients whose sum is \(s_1+s_2\le1\). Each \(R_j\) has Ky Fan-two norm \(1\). By linearity and the triangle inequality, it suffices to bound \(\|\mathcal C(R_j)\|_{(2)}\) separately for ranks \(j=1,2,3\). This convex decomposition covers *every* real or complex matrix, not just normal matrices.

**2. Rank two cannot amplify.** For \(R_2\), \(\|R_2\|_F=1/\sqrt2\). Trace-centering is an orthogonal projection for the Frobenius inner product, so \(\|\mathcal C(R_2)\|_F\le1/\sqrt2\). Because \(\|X\|_{(2)}\le\sqrt2\|X\|_F\), we obtain \(\|\mathcal C(R_2)\|_{(2)}\le1\).

**3. Full-rank partial isometries are strictly below the proposed maximum.** Write \(R_3=U/2\) for unitary (orthogonal in the real case) \(U\). Since \(U\) is normal, its eigenvalues \(z_1,z_2,z_3\) lie on the unit circle. Write \(m=(z_1+z_2+z_3)/3\). For any two indices \(1,2\), put \(a=z_1-z_2\), \(b=(z_1+z_2)/2-z_3\). Then
\[z_1-m=a/2+b/3,\qquad z_2-m=-a/2+b/3.\]
The parallelogram identity and Cauchy–Schwarz imply
\[\frac{|z_1-m|+|z_2-m|}{2}\le \frac13\sqrt{\frac94|a|^2+|b|^2}.\]
After rotating the three points, we may write \(z_1=e^{i\theta}\), \(z_2=e^{-i\theta}\) and \(c=|\cos\theta|\in[0,1]\). Hence \(|a|^2=4(1-c^2)\) and \(|b|\le1+c\), giving
\[\frac{|z_1-m|+|z_2-m|}{2}\le\frac13\sqrt{10+2c-8c^2}\le\frac{3}{2\sqrt2}.\]
The last quadratic has its maximum at \(c=1/8\). The chosen indices can be the ones with the two largest values of \(|z_i-m|\), so
\[\|\mathcal C(R_3)\|_{(2)}\le\frac{3}{2\sqrt2}<\frac12+\frac{\sqrt6}{4}.\]
This calculation covers all complex unitary matrices and therefore all real orthogonal ones.

**4. Exact rank-one maximum and equality.** Multiplying by a unit-modulus scalar and applying simultaneous unitary conjugation leaves the quotient unchanged. Thus every rank-one partial isometry can be reduced to
\[R_1=\begin{pmatrix}r&\sqrt{1-r^2}&0\\0&0&0\\0&0&0\end{pmatrix},\quad 0\le r\le1.\]
Its centered form is
\[\mathcal C(R_1)=\begin{pmatrix}2r/3&\sqrt{1-r^2}&0\\0&-r/3&0\\0&0&-r/3\end{pmatrix}.\]
The upper-left \(2\times2\) block has singular-value sum \(1\), singular-value product \(2r^2/9\), and singular values
\[\alpha,\beta=\frac{1\pm\sqrt{1-8r^2/9}}2.\]
The remaining singular value is \(r/3\). The larger \(\alpha\) is at least \(2r/3\), and hence \(\beta\le r/3\). Therefore
\[\|\mathcal C(R_1)\|_{(2)}=\frac{1+\sqrt{1-8r^2/9}}2+\frac r3.\]
Its derivative is \(1/3-4r/[9\sqrt{1-8r^2/9}]\), which changes sign once, at \(r^2=3/8\), from positive to negative. The maximum is \(1/2+\sqrt6/4\) and is attained by \(A_*\). Together with steps 1–3, this proves the exact induced norm.

**5. It is a minimum projection norm.** Let \(\mathcal P\) be any real-linear projection onto the traceless real or complex matrix space. Since \(\mathcal P\) fixes all trace-zero matrices, \(\mathcal P(A)=\mathcal C(A)+Q(\operatorname{tr}A)\) for a real-linear \(Q\) taking values in trace-zero matrices. Average \(A\mapsto U^*\mathcal P(UAU^*)U\) over the orthogonal group in the real case, or the unitary group in the complex case. Conjugation preserves the Ky Fan norm, so convexity bounds the norm of this averaged projection by \(\|\mathcal P\|\). The conjugation-average of each traceless \(Q(z)\) is zero; thus the averaged operator is exactly \(\mathcal C\). This proves minimality, even over real-linear maps in the complex case.

**6. Self-adjoint comparison.** On the self-adjoint subspace, diagonalization reduces \(\mathcal C\) to scalar mean-centering in \(\mathbb R^3\) with norm \(|x|_{(2)}\), the sum of the two largest absolute entries. The scalar unit ball is the convex hull of signed permutations of \((1,0,0)\), \((1/2,1/2,0)\), and \((1/2,1/2,1/2)\). Direct mean-centering of these finitely many sign patterns has \(|\cdot|_{(2)}\le1\); a vector \((1,0,0)\) gives equality. Hence the self-adjoint norm equals one, proving the strict nonnormal gap.

## Verification

The accompanying `check_constant.py` uses exact rational identities to check the rank-one extremal equation and the rank-three quadratic bound, and independently tests full matrix singular-value ratios numerically for representative real and complex examples. Its finite experiments only corroborate the analytical argument; steps 1–6 establish the claims for all matrices and all real-linear projections. Run `python3 check_constant.py` in a Python 3 environment with NumPy installed. An exact witness is provided above, requiring no numerical optimization or random sampling.

## Relationship to prior work

Foucart's *Computation of Minimal Projections and Extensions* (2016), Theorem 1, establishes the minimality of trace-centering for unitarily invariant matrix norms. Its Theorem 3 gives the sharp spectral- and nuclear-norm endpoint constants, and Corollary 4 bounds **intermediate** Ky Fan projection constants by \(2-2/n\). In dimension three this supplies the upper bound \(4/3\), not the sharp Ky Fan-two value calculated here. The matrix-space distinction is essential: a previously obtained self-adjoint Ky Fan-two formula yields \(1\), while nonnormal rank-one matrices attain the strictly larger exact number in this finding.

## Limitations

The proof gives the exact intermediate Ky Fan-two constant **only in dimension three**. It does not identify general-dimensional intermediate Ky Fan constants, characterize every maximizing matrix, or quantify uniqueness of minimal projections. The historical-priority check is qualified: an unindexed exact formula in older symmetric-gauge or unitarily invariant norm literature could still exist. No independent audit has been performed.

## References

1. S. Foucart, *Computation of Minimal Projections and Extensions*, Numerical Functional Analysis and Optimization **37** (2016), 159–185, DOI: 10.1080/01630563.2015.1091014. Open author manuscript: https://foucart.github.io/publi/CompMinExt.pdf; especially §4, Theorem 1 and Corollary 4.
2. R. Bhatia, *Matrix Analysis*, Springer, 1997, Chapter IV (background on Ky Fan and unitarily invariant norms; cited for context, not used as an external proof certificate).
