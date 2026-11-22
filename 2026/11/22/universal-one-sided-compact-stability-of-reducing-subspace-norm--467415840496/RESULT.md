# Universal one-sided compact stability of reducing-subspace norm attainment

## Finding
Let \(H\) be an infinite-dimensional separable complex Hilbert space. Write \(\mathcal B_+(H)\) for the bounded positive self-adjoint operators whose restrictions to **every nonzero closed reducing subspace** attain their operator norms. For an operator \(T\), write \(\beta_0(H)\) for the class in which \(|T|\) belongs to \(\mathcal B_+(H)\).

**Theorem (sharp universal compact-perturbation classification).** Fix any compact self-adjoint operator \(K\) on \(H\). Let \(K_-:=(-K)_+\) be its negative part. The following conditions are equivalent:

1. \(K_-\) has finite rank.
2. For **every** \(A\in\mathcal B_+(H)\), the operator \(A+K\) belongs to \(\beta_0(H)\).
3. For every \(A\in\mathcal B_+(H)\) satisfying \(A+K\geq0\), the positive operator \(A+K\) belongs to \(\mathcal B_+(H)\).

In particular, **every** positive compact perturbation preserves reducing-subspace norm attainment of positive operators, even when it has infinite rank, fails to commute with the starting operator, and the starting operator has several distinct points in its essential spectrum. No bound on the perturbation norm is needed. Conversely, if \(K_-\) has infinite rank, **every** scalar starting operator \(A=cI\) with \(c>\|K\|\) violates condition 3. The obstruction can have arbitrarily small trace-class norm.

## Assumptions and scope
All operators are bounded and act on the same infinite-dimensional separable complex Hilbert space. A reducing subspace for a self-adjoint operator is a closed subspace whose orthogonal projection commutes with the operator. Norm attainment of a restriction is ordinary operator-norm attainment, not minimum-modulus attainment. For positive \(A\), membership in \(\mathcal B_+(H)\) is equivalent to an orthonormal eigenbasis together with a **reverse well-ordered** set of eigenvalues: every nonempty subset has a largest member. Equivalently, the eigenvalue set contains no strictly increasing infinite sequence. This structural criterion is due to the cited work of Su--Zhang and Golla--Osaka--Sequeira.

A compact self-adjoint \(K\) has the canonical decomposition \(K=K_+-K_-\), with \(K_+,K_-\geq0\) compact. Finite rank of \(K_-\) counts multiplicity, so it is equivalent to having only finitely many negative eigenvalues counted with multiplicity. The theorem does not assert preservation for non-self-adjoint compact perturbations, nor for arbitrary nonpositive starting operators.

## Proof
**Lemma 1: a positive bounded perturbation cannot move spectrum down across a gap.** Suppose \(S=S^*\), \(\sigma(S)\cap(a,b)=\emptyset\), and \(0\leq E\leq\eta I\) with \(\eta<b-a\). Then
\[
\sigma(S+E)\cap(a+\eta,b)=\emptyset.
\]
Indeed, for any \(\lambda\in(a+\eta,b)\), split \(H=H_-\oplus H_+\) by the spectral projections of \(S\) onto \(( -\infty,a]\) and \([b,\infty)\). The diagonal blocks of \(S+E-\lambda I\) on these subspaces satisfy \(X_-\leq-(\lambda-a-\eta)I<0\) and \(X_+\geq(b-\lambda)I>0\). In the two-by-two operator block matrix, the Schur complement of \(X_-\) is \(X_+-Y^*X_-^{-1}Y\geq X_+>0\). Both blocks are boundedly invertible; hence the full operator is invertible. The argument includes the cases in which one spectral summand is zero.

**Lemma 2: finite-rank perturbations of either sign introduce only finitely many spectral points into a gap.** Suppose \(C=C^*\), \(\sigma(C)\cap(a,b)=\emptyset\), and \(F\geq0\) has finite rank \(r\). Then each of \(C+F\) and \(C-F\) has at most \(r\) **distinct spectral points** in \((a,b)\). On \(\operatorname{ran}F\), the finite-dimensional Hermitian Birman--Schwinger matrix
\[
G(\lambda)=F^{1/2}(C-\lambda I)^{-1}F^{1/2}
\]
is defined for \(\lambda\in(a,b)\). A point \(\lambda\) in the gap belongs to \(\sigma(C+F)\) (respectively, \(\sigma(C-F)\)) exactly when \(-1\) (respectively, \(1\)) is an eigenvalue of \(G(\lambda)\); finite rank makes all such spectral points eigenvalues. Furthermore
\[
G'(\lambda)=F^{1/2}(C-\lambda I)^{-2}F^{1/2}>0
\]
as a quadratic form on the \(r\)-dimensional \(\operatorname{ran}F\). Hence each of the \(r\) ordered eigenvalues of \(G(\lambda)\) is strictly increasing in \(\lambda\) and can cross either fixed level \(1\) or \(-1\) at most once. For \(r=0\) the assertion is immediate.

**Lemma 3: arbitrary positive compact perturbations preserve the positive class.** Let \(A\in\mathcal B_+(H)\) and \(K\geq0\) compact. Put \(B=A+K\). By the published reverse-well-order criterion, \(A\) has pure point spectrum with reverse well-ordered eigenvalues \(\Lambda\). The closure \(\overline\Lambda=\sigma(A)\) is also reverse well-ordered and countable (the elementary closed-order lemma; see Golla--Osaka--Sequeira, Lemma 2.14). Weyl's theorem gives \(\sigma_{\rm ess}(B)=\sigma_{\rm ess}(A)\), a countable set. All spectral points outside this essential spectrum are isolated eigenvalues of finite multiplicity, and there are at most countably many of them. Therefore \(\sigma(B)\) is countable. Every scalar spectral measure of the self-adjoint \(B\) is supported on this countable set and hence is purely atomic; thus \(B\) has pure point spectrum.

Suppose its eigenvalue set is not reverse well-ordered. Then there exist strictly increasing distinct eigenvalues \(\lambda_n\uparrow\mu\). Unit eigenvectors for different eigenvalues are orthogonal, so \((\lambda_n)\) is a singular Weyl sequence and \(\mu\in\sigma_{\rm ess}(B)=\sigma_{\rm ess}(A)\subseteq\sigma(A)\). Since \(\sigma(A)\) is closed and reverse well-ordered, there is \(\delta>0\) such that
\[
\sigma(A)\cap(\mu-\delta,\mu)=\emptyset.
\]
By the spectral theorem for the positive compact \(K\), choose a finite-rank positive spectral truncation \(F\) such that \(E:=K-F\geq0\) and \(\eta:=\|E\|<\delta/3\). Lemma 1 applied to \(C:=A+E\) shows that \(\sigma(C)\) has no points in \((\mu-\delta+\eta,\mu)\). Lemma 2 shows that \(B=C+F\) has at most \(\operatorname{rank}F\) distinct spectral points in this interval. But all sufficiently large \(\lambda_n\) belong to that interval, a contradiction. Thus the eigenvalues of \(B\) are reverse well-ordered, and the published spectral criterion yields \(B\in\mathcal B_+(H)\). Notice that nowhere is \([A,K]=0\) assumed.

**Classification.** If \(\operatorname{rank}K_-<\infty\), apply Lemma 3 to \(A\) and \(K_+\) to obtain \(C=A+K_+\in\mathcal B_+(H)\subset\beta_0(H)\). The finite-rank perturbation theorem for \(\beta_0(H)\) (Su--Zhang, Theorem 4.3) gives \(A+K=C-K_-\in\beta_0(H)\), regardless of the sign of \(C-K_-\). Here is also a direct verification of the **needed self-adjoint special case**, independent of that general theorem. Put \(F=K_-\) and \(B=C-F\). As in Lemma 3, compactness of \(F\) and countability of \(\sigma(C)\) imply that \(B\) has countable spectrum and hence pure point spectrum. Since \(C\geq0\), the negative spectral subspace of \(B\) has dimension at most \(\operatorname{rank}F\): otherwise it contains a nonzero vector annihilated by \(F\), contradicting nonnegativity of \(C\). Therefore only finitely many distinct negative eigenvalues can contribute to the spectrum of \(|B|\). If \(|B|\) had a strictly increasing infinite sequence of eigenvalues, after omitting these finitely many negative eigenvalues it would give a strictly increasing sequence of **positive** eigenvalues of \(B\) converging to a positive point \(\mu\in\sigma_{\rm ess}(C)\). Since the closed spectrum of \(C\) is reverse well-ordered, \(C\) has a gap immediately below \(\mu\); the negative-sign version of Lemma 2 allows at most \(\operatorname{rank}F\) eigenvalues of \(C-F\) in that gap, a contradiction. Thus \(|B|\) is pure point with reverse well-ordered eigenvalues and \(B\in\beta_0(H)\). This proves condition 1 implies condition 2, and condition 2 implies condition 3 by positivity of the result in condition 3.

Conversely, suppose \(K_-\) has infinite rank. The compact spectral theorem supplies orthonormal eigenvectors \(e_n\) with \(Ke_n=-t_ne_n\), where \(t_n>0\) strictly decreases to zero. Choose **any** \(c>\|K\|\) and set \(A=cI\). This \(A\) is positive and belongs to \(\mathcal B_+(H)\), while \(B=A+K>0\). On the reducing subspace \(M=\overline{\operatorname{span}}\{e_n:n\geq1\}\), the restriction \(B|_M\) has distinct eigenvalues \(c-t_n\) strictly increasing to \(c\), so \(\|B|_M\|=c\) is not attained. Hence condition 3 fails. The three statements are equivalent.

## Verification
The proof is infinite-dimensional and analytic. Lemma 1 checks the full spectral-gap boundary using a Schur complement; Lemma 2 uses strict matrix monotonicity rather than finite enumeration; Lemma 3 establishes pure point spectrum before applying the eigenvalue order criterion. An optional standalone `checker.py` checks explicit noncommuting block witnesses and increasing negative-tail obstructions with floating-point arithmetic, but **does not establish** any infinite-dimensional claim.

For a genuinely noncommuting illustration with multiple essential spectral levels, take \(H=\bigoplus_{n\geq1}\mathbb C^2\), let every block of \(A\) be \(\operatorname{diag}(2,1)\), and every block of \(K\) be \(\epsilon_n\left(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\right)\), with \(\epsilon_n=1/(4n)\). Then \(K\geq0\) is compact of infinite rank and \([A,K]\ne0\). The two eigenvalues of the \(n\)-th block of \(A+K\) are
\[
\lambda_\pm(n)=\frac{3+2\epsilon_n\pm\sqrt{1+4\epsilon_n^2}}2.
\]
Both branches strictly decrease toward \(2\) and \(1\), respectively, from above; this operator has a reverse well-ordered pure point spectrum despite its two distinct essential spectral values. It is outside the narrower absolutely norm-attaining class. For failure when the negative part has infinite rank, take \(K e_n=-\varepsilon2^{-n}e_n\) with arbitrarily small \(\varepsilon>0\), and start from \(A=I\). This obstruction is trace class.

## Relationship to prior work
Su and Zhang, arXiv:2609.37621, establish the pure-point reverse-well-order criterion, the finite-rank stability of \(\beta_0(H)\), a spectral criterion for **individual** compact perturbations through an auxiliary total perturbation, and the identity of the subset invariant under **all** compact perturbations. Those theorems are explicitly credited as inputs. None states the present **fixed-perturbation universal** classification or proves the positive compact lemma without commutativity or a singleton essential spectrum.

Golla, Osaka and Sequeira, arXiv:2610.13490, prove the countable closed-order lemma and present the positive \(\beta(H)\) spectral criterion. Nag and Ramesh, arXiv:2608.19286, prove a dual **minimum-attainment** result for compact subtractions that must **commute with every original eigenspace projection**; the present theorem drops this commutation requirement and gives a sharp full characterization of signed compact perturbations preserving norm attainment for every positive base. Both primary manuscripts were inspected in the relevant sections.

Two other publicly available mathematical records, *Sharp Schatten repair tails for essentially scalar moduli* and *Universal continuous scalar calculi for reducing-subspace norm and minimum attainment*, were inspected in full. The former concerns correcting a **single essentially scalar modulus** with quantitative Schatten costs, not arbitrary positive bases with multiple essential levels. The latter concerns commuting scalar functions of an operator, not a generally noncommuting compact summand. Neither implies the classification above.

## Limitations
The class of starting operators is restricted to **positive self-adjoint** members of \(\beta(H)\); the perturbation is assumed compact and self-adjoint. The theorem makes no assertion that adding positive compact operators to arbitrary nonnormal members preserves the property. It does not provide a quantitative perturbation modulus or a classification for noncompact perturbations. The literature comparison establishes best-knowledge distinctness, not an independent proof of publication priority; unindexed equivalent work remains possible. The finite diagnostic is supplemental rather than a proof.

## References
1. Z. Su and Y. Zhang, *The Stability and Density of Norm Attaining Operators on Reducing Subspaces*, arXiv:2609.37621v1, first public September 29, 2026, Theorems 3.4, 4.3, 5.1 and 6.1. https://arxiv.org/abs/2609.37621
2. R. Golla, H. Osaka and S. S. Sequeira, *Quasinormal and hyponormal operators in the \(\beta(H)\)-class*, arXiv:2610.13490v1, first public October 9, 2026, Theorem 2.2 and Lemma 2.14. https://arxiv.org/abs/2610.13490
3. P. Nag and G. Ramesh, *Minimum attaining operators on reducing subspaces: Spectral structure and density*, arXiv:2608.19286v1, first public August 19, 2026, Proposition 5.2 and Theorem 5.4. https://arxiv.org/abs/2608.19286
4. *Sharp Schatten repair tails for essentially scalar moduli*, published mathematical research record, November 1, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-schatten-repair-tails-for-essentially-scalar-moduli--4e75fd7c38ef
5. *Universal continuous scalar calculi for reducing-subspace norm and minimum attainment*, published mathematical research record, October 18, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-universal-continuous-scalar-calculi-for-reducing-subspace-norm-a--fe8478c3d676
