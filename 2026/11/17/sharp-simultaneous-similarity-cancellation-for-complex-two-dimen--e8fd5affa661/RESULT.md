# Sharp simultaneous similarity cancellation for complex two-dimensional matrix families

## Finding
Let \(I\) be any nonempty index set, finite or infinite, and let \(\mathcal A=(A_i)_{i\in I}\) and \(\mathcal B=(B_i)_{i\in I}\) be families of complex \(2\times2\) matrices. For an integer \(q\ge1\) let \(A_i^{(q)}\) denote the orthogonal direct sum of \(q\) copies of \(A_i\). Define the optimal *common* similarity condition number
\[
 s_I(\mathcal A,\mathcal B)=\inf\{\|X\|\|X^{-1}\|:X\in GL_2(\mathbb C),\ A_iX=XB_i\ \text{for all }i\in I\},
\]
with the value \(+\infty\) if no common invertible intertwiner exists. Then
\[
\boxed{s_I(\mathcal A^{(q)},\mathcal B^{(q)})=s_I(\mathcal A,\mathcal B)\quad\text{for all finite }q\ge1.}
\]
In particular, the sharp simultaneous similarity modulus from the fixed-size amplification problem is
\[
\boxed{\Theta^{\mathrm{sim}}_{2,q}(t)=t\qquad(q\ge1,\ t\ge1),}
\]
where \(\Theta^{\mathrm{sim}}_{2,q}(t)\) is the supremum of the unamplified optimal common condition numbers over all (including infinite) simultaneously indexed families whose \(q\)-fold amplifications have a common similarity of condition number at most \(t\).

A structural dichotomy explains the equality. If all source matrices commute and at least one is nonscalar, the entire common-similarity optimization reduces to that single nonscalar source matrix and its target. If two source matrices fail to commute, their common commutant consists only of scalars; in that case every nonzero common intertwiner is a scalar multiple of one invertible intertwiner, and **every** amplified common intertwiner is a Kronecker product \(C\otimes X\) with \(C\in M_q(\mathbb C)\). Its condition number equals \(\kappa(C)\kappa(X)\). Thus even arbitrarily many noncommuting constraints cannot improve the best conditioning after replication.

## Assumptions and scope
All matrices act on \(\mathbb C^2\) with the standard Hilbert norm; all operator norms are spectral norms. The index set has no cardinality constraint. The matrices need not be normal, invertible or pairwise commuting. Amplification always means finite orthogonal direct sums. The result does not concern higher matrix sizes or unrelated similarities for separate members of the families; the same invertible matrix must intertwine every indexed pair.

## Proof
**Step 1: cancellation of existence.** Suppose \(W\in GL_{2q}(\mathbb C)\) satisfies \(A_i^{(q)}W=WB_i^{(q)}\) for every \(i\). If all \(A_i\) are scalar, the equations and invertibility of \(W\) show that \(B_i=A_i\) for every \(i\). The identity is a common similarity. Otherwise fix a nonscalar \(A_0\) from the source family.

If every \(A_i\) commutes with \(A_0\), the centralizer identity
\[
\{Z\in M_2(\mathbb C):ZA_0=A_0Z\}=\operatorname{span}\{I,A_0\}
\]
holds because every nonscalar \(2\times2\) matrix is cyclic, whether it has distinct or repeated eigenvalues. Thus write \(A_i=\alpha_i I+\beta_i A_0\). Since the similarity of the \(q\)-fold copies of \(A_0,B_0\) forces equality of their Jordan block multiplicities, \(A_0\) and \(B_0\) are similar. Furthermore, the amplified intertwining equations imply
\[
W(B_i^{(q)}-\alpha_i I-\beta_iB_0^{(q)})=0,
\]
so \(B_i=\alpha_i I+\beta_iB_0\). Consequently every intertwiner of \(A_0,B_0\) is a common intertwiner for the entire family, at every multiplicity.

If some \(A_1\) fails to commute with \(A_0\), any matrix commuting with all source matrices must have form \(Z=\alpha I+\beta A_0\). The equation \([Z,A_1]=\beta[A_0,A_1]=0\) forces \(\beta=0\). Thus the joint commutant is exactly the scalars. Regard \(W\) and \(W^{-1}\) as \(q\)-by-\(q\) block matrices of size two. Every block of \(W\) intertwines all \(B_i\) with \(A_i\), and every block of \(W^{-1}\) intertwines in the reverse direction. Each product of a block of \(W\) with the matching block of \(W^{-1}\) therefore belongs to the scalar joint commutant. A diagonal block of \(WW^{-1}=I\) is a sum of these scalar products and equals \(I\); at least one summand is nonzero. Hence the two constituent blocks of that summand are invertible. One of them is a common similarity \(X\) of the original families. This proves existence cancellation without invoking infinite-dimensional theory.

**Step 2: norm preservation in the noncommuting case.** Fix the common invertible intertwiner \(X\) just obtained. For any two common intertwiners \(Y\) and \(X\), the matrix \(YX^{-1}\) commutes with every \(A_i\), so \(Y=cX\) for a scalar \(c\). Thus the optimal unamplified condition number is \(\kappa(X)=\|X\|\|X^{-1}\|\), and every nonzero common intertwiner is invertible. At amplification multiplicity \(q\), every block of a common intertwiner is of form \(c_{jk}X\). Reordering direct-sum coordinates yields \(W=C\otimes X\), and this is invertible precisely when \(C\) is. Singular values of Kronecker products multiply, so \(\kappa(W)=\kappa(C)\kappa(X)\ge\kappa(X)\). Choosing \(C=I_q\) gives equality.

**Step 3: norm preservation in the commuting case.** By Step 1 the family optimization reduces to a single similar pair \(A_0,B_0\). For completeness, we show that optimal similarity of any two complex \(2\times2\) matrices is invariant under finite amplification. If they have a repeated eigenvalue \(\lambda\) and are nonscalar, the nilpotents \(N_A=A_0-\lambda I\), \(N_B=B_0-\lambda I\) are unitarily equivalent to \(\left(\begin{smallmatrix}0&r_A\\0&0\end{smallmatrix}\right)\) and \(\left(\begin{smallmatrix}0&r_B\\0&0\end{smallmatrix}\right)\), respectively, with \(r_A=\|N_A\|>0\), \(r_B=\|N_B\|>0\). The diagonal intertwiner \(\operatorname{diag}(r_A/r_B,1)\) attains condition number \(\max\{r_A/r_B,r_B/r_A\}\).

If the two common eigenvalues are distinct, set
\[
J_A=\frac{2A_0-(\lambda_++\lambda_-)I}{\lambda_+-\lambda_-},\qquad J_B=\frac{2B_0-(\lambda_++\lambda_-)I}{\lambda_+-\lambda_-}.
\]
Both are involutions with eigenvalues \(\pm1\). An involution in dimension two is unitarily equivalent to \(K_j=\left(\begin{smallmatrix}0&j\\j^{-1}&0\end{smallmatrix}\right)\), with \(j=\|J\|\ge1\): take unit eigenvectors \(u_+,u_-\), align their phases so \(\langle u_+,u_-\rangle=\beta\in[0,1)\), and use the orthonormal sum/difference basis; then \(j=\sqrt{(1+\beta)/(1-\beta)}\). With \(j_A=\|J_A\|\) and \(j_B=\|J_B\|\), \(\operatorname{diag}(j_A/j_B,1)\) intertwines the two canonical involutions and attains condition number \(\max\{j_A/j_B,j_B/j_A\}\). Scalar pairs have optimum one.

In each nonscalar case a common polynomial of \(A_0,B_0\)—the shifted nilpotent or normalized spectral involution—has nonzero norms \(r_A,r_B\) or \(j_A,j_B\). Every amplified invertible intertwiner preserves these polynomials, so the inequalities
\[
\kappa(W)\ge\max\{\|F_A\|/\|F_B\|,\|F_B\|/\|F_A\|\}
\]
apply to every amplification, since \(\|F^{(q)}\|=\|F\|\). The displayed canonical intertwiners meet these lower bounds and can be directly summed to achieve the same bound at multiplicity \(q\). Thus norm preservation holds for commuting families too. All cases are exhausted.

**Step 4: sharp modulus.** The established identity implies \(\Theta^{\mathrm{sim}}_{2,q}(t)\le t\). For the reverse inequality choose the one-element family with \(A=\left(\begin{smallmatrix}0&t\\t^{-1}&0\end{smallmatrix}\right)\) and \(B=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\). Both its original and amplified optimum equal \(t\), by Step 3. Hence the modulus equals \(t\).

## Verification
The proof is self-contained for arbitrary index sets and finite replication counts. The standalone `verify.py` checks exact intertwining identities and commutant dimensions for representative commuting and noncommuting families over rational matrices, plus amplified condition numbers. These finite checks illustrate, but are not substitutes for, the cyclic-centralizer classification, block-inverse argument, and two-sided norm inequalities in the proof.

## Relationship to prior work
Aouichaoui (2026, arXiv:2611.01298, especially Theorem 2.1) establishes a uniform but unspecified conditioning bound \(C(n,q,t)\) for *arbitrary simultaneously indexed families*, and the bound tends to one when the amplified conditioning does. Jiang, Ma, Shi, and Zhang (2026, arXiv:2607.20593) study the earlier single-pair doubling similarity function. The exact single-pair dimension-two cancellation identity is not claimed as a new contribution here: it is an elementary special case and is explicitly reconstructed in Step 3. The distinct claim is that **arbitrary simultaneous constraints, including noncommuting and infinite indexed families**, also admit exact constant one for every finite multiplicity, through the scalar-versus-cyclic commutant dichotomy. Florentino (2008) studies classification and simultaneous triangularization for complex two-dimensional matrix families; these are similarity-class questions, not sharp condition-number preservation under amplification.

## Limitations
The theorem is specific to two-dimensional complex matrices and orthogonal finite amplifications; no claim is made about higher dimension or infinite amplification. The proof does not classify optimal intertwiners for commuting families individually, only reduces their optimization to a single matrix. Earlier unindexed equivalents through matrix-representation or operator-space similarity theory remain a bibliographic risk; the literature comparison is not an independent validation. No infinite claim is justified merely by finite computation.

## References
1. M. A. Aouichaoui, *Similarity cancellation and primitive operator roots*, arXiv:2611.01298 (first public 2026-10-31), https://arxiv.org/html/2611.01298v1 .
2. C. Jiang, M. Ma, R. Shi, Y. Zhang, *The Ulam--Kaplansky problem in operator algebras*, arXiv:2607.20593 (first public 2026-07-22), https://arxiv.org/html/2607.20593v2 .
3. C. A. A. Florentino, *Simultaneous similarity and triangularization of sets of 2 by 2 matrices*, arXiv:0809.3032 (2008), https://arxiv.org/abs/0809.3032 .
4. J. W. Demmel, *The Condition Number of Similarities that Diagonalize Matrices*, UCB/CSD-83-127 (1983), https://www2.eecs.berkeley.edu/Pubs/TechRpts/1983/CSD-83-127.html .
