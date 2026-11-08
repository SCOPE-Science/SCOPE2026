# Special-unitary fourth-moment resonance and traceless spectral rigidity

## Finding
For the first real matrix-coefficient space on \(\mathrm{SU}(n)\), the sharp fourth-moment embedding is Gaussian-bounded in every dimension \(n\ge3\) except \(n=4\), where a determinant invariant raises its sharp fourth-power constant from \(3\) to \(7/2\). For traceless Hermitian coefficients on \(\mathrm{SU}(4)\), the ratio is exactly affine in the normalized determinant, and its sharp minimum and maximum occur at the distinct eigenvalue-multiplicity patterns \(3+1\) and \(2+2\).

## Assumptions and scope
Equip \(\mathrm{SU}(n)\) with probability Haar measure. For every complex \(n\times n\) matrix \(A\ne0\), \(n\ge3\), define \(f_A(U)=\operatorname{Re}\operatorname{tr}(A^*U)\), \(S=\operatorname{tr}(AA^*)>0\), \(Q=\operatorname{tr}((AA^*)^2)\), \(r=Q/S^2\), and \(d=\operatorname{Re}\det A/S^2\). We study the attained ratio \(K_n(A)=\mathbb E f_A^4/(\mathbb E f_A^2)^2\), the fourth power of the \(L^2\)-to-\(L^4\) norm along \(f_A\). No restriction to diagonal or normal matrices is imposed in the first theorem.

The exact formulas are
\[
\mathbb E f_A^2=\frac{S}{2n},\qquad
K_n(A)=\begin{cases}
\dfrac{3n^2}{n^2-1}\left(1-\dfrac{r}{n}\right),&n=3\text{ or }n\ge5,\\[3pt]
\dfrac{16}{5}-\dfrac45 r+8d,&n=4.
\end{cases}
\]
Their complete sharp intervals are \([3n/(n+1),3]\) for \(n=3\) or \(n\ge5\), and \([12/5,7/2]\) for \(n=4\). In every dimension the lower extremizers are exactly rank-one matrices. Outside dimension four, the upper extremizers are exactly matrices with all singular values equal. In dimension four the upper extremizers are exactly \(A=cV\), where \(c>0\) and \(V\in\mathrm{SU}(4)\). Thus \(n=4\) is the unique dimension at least three with fourth-moment amplification greater than the Gaussian ratio \(3\).

For traceless Hermitian \(A\ne0\) in dimension four, \(d=\det A/S^2\) is real and
\[
K_4(A)=\frac{14}{5}+\frac{56}{5}d,
\qquad -\frac1{48}\le d\le\frac1{16},
\qquad \frac{77}{30}\le K_4(A)\le\frac72.
\]
Lower equality holds exactly for unitary conjugates and nonzero real multiples of \(\operatorname{diag}(1,1,1,-3)\); upper equality holds exactly for conjugates and nonzero real multiples of \(\operatorname{diag}(1,1,-1,-1)\). All intermediate ratios in both unrestricted and Hermitian ranges are attained.

## Proof
**Moment selection and normalization.** Write \(Z=\operatorname{tr}(A^*U)\). Multiplication of \(U\in\mathrm{SU}(n)\) by any central \(n\)-th root of unity shows \(\mathbb E Z^p\overline Z^{\,q}=0\) unless \(n\) divides \(p-q\). For \(n\ge3\), the second moment therefore equals \(\mathbb E f_A^2=\tfrac12\mathbb E|Z|^2=S/(2n)\). At fourth order the only allowed unbalanced monomial in any dimension \(n\ge3\) is \(Z^4\) or \(\overline Z^4\), and that occurs only when \(n=4\). Balanced moments agree with \(\mathrm U(n)\), since scalar rotation preserves their integrands and the unitary Haar law decomposes into scalar times special-unitary Haar law. The order-two unitary Weingarten formula gives
\[
\mathbb E|Z|^4=\frac2{n^2-1}\left(S^2-\frac Qn\right).
\]
When \(n=4\), the invariant subspace of \((\mathbb C^4)^{\otimes4}\) under \(\mathrm{SU}(4)\) is the alternating determinant line. Orthogonal projection onto its normalized Levi-Civita tensor gives \(\mathbb E Z^4=\overline{\det A}\), including the factor \(1/4!\) that cancels the \(4!\) determinant contractions. Expanding \(f_A^4=(Z+\bar Z)^4/16\) yields the displayed formulas: the balanced contribution is \(6\mathbb E|Z|^4/16\), and in dimension four the extra term is \(\operatorname{Re}\det A/8\).

**Unrestricted optimization.** If \(x_1,\dots,x_n\) are the squared singular values divided by \(S\), then \(x_i\ge0\), \(\sum x_i=1\), and \(1/n\le r=\sum x_i^2\le1\), with equality only at uniform singular values and rank one, respectively. This proves the range and equality classes when \(n\ne4\).

For \(n=4\), \(|d|\le\sqrt{x_1x_2x_3x_4}\le1/16\). Thus
\[
\frac72-K_4(A)=\frac45\left(r-\frac14\right)+8\left(\frac1{16}-d\right)\ge0,
\]
with equality exactly at four equal singular values and positive real determinant, equivalently \(A=cV\) with \(c>0\), \(V\in\mathrm{SU}(4)\). For the opposite bound, AM--GM on the six pair products yields
\[
1-r=2\sum_{i<j}x_ix_j\ge12\sqrt{x_1x_2x_3x_4}.
\]
Consequently
\[
K_4(A)-\frac{12}{5}=\frac45(1-r)+8d
\ge\frac45(1-r)-8\sqrt{x_1x_2x_3x_4}
\ge\frac2{15}(1-r)\ge0.
\]
Equality forces \(r=1\), i.e. rank one. This also supplies a quantitative lower stability bound.

**Traceless Hermitian optimization.** Let \(A=A^*\), \(\operatorname{tr}A=0\). Newton's identities for its four real eigenvalues give \(Q=S^2/2-4\det A\), hence \(r=1/2-4d\) and \(K_4=14/5+56d/5\). Scale to \(S=1\) and pair the eigenvalues as \((a+b)/2,(a-b)/2,(-a+c)/2,(-a-c)/2\). Then \(a^2+(b^2+c^2)/2=1\). Put \(s=a^2\in[0,1]\), \(t=b^2\ge0\), \(u=c^2\ge0\). Since \(t+u=2(1-s)\),
\[
16\det A=(s-t)(s-u)=3s^2-2s+tu,
\qquad 0\le tu\le(1-s)^2.
\]
It follows that \(16\det A\ge3(s-1/3)^2-1/3\ge-1/3\), with equality exactly at \(s=1/3\), \(tu=0\), giving the \(3+1\) eigenvalue pattern. Similarly \(16\det A\le(2s-1)^2\le1\), with equality exactly at the \(2+2\) pattern. Both extrema occur. The sharp deficit identities are \(K_4-77/30=(56/5)(d+1/48)\) and \(7/2-K_4=(56/5)(1/16-d)\). The coefficient domain is connected after normalizing \(S=1\), so continuity gives every intermediate attained ratio.

## Verification
The standalone file `su4_fourth_checker.py` independently inverts the order-two unitary Weingarten Gram matrix, checks the normalized alternating-tensor contraction, runs 12,000 exact-rational diagonal spectral checks including the traceless restriction, verifies all sharp endpoint examples, and compares the formulas to an independent QR-generated numerical Haar sample on \(\mathrm{SU}(4)\) (48,000 matrices). It reports `ALL_SU4_FOURTH_MOMENT_CHECKS_PASSED`. Numerical sampling does not establish the general theorem; that rests on the preceding invariant-tensor, Newton-identity, and AM--GM proofs.

## Relationship to prior work
Collins and Śniady (first public preprint 26 February 2004) give the unitary Weingarten integration machinery used for the balanced moments; these integrations are prior work. Borisenko, Voloshyn and Chelnokov (2018) provide general special-unitary polynomial and trace generating integrals, including determinant-charge corrections. Their formulas supply broad moment-computation machinery; the present claim is the sharp real fourth-moment embedding with the complete spectral equality classification, the strict isolated dimension-four Gaussian excess, and the exact constrained traceless-Hermitian determinant interval. Those optimization assertions are not stated in the inspected primary texts. A sufficiently explicit unindexed consequence of general integration formulas remains a novelty risk.

## Limitations
Only fourth moments of real fundamental matrix coefficients for \(n\ge3\) are addressed. The results do not cover higher tensor representations, mixed-degree coefficients, or higher even moments. The trace-zero Hermitian classification is specific to dimension four. No independent mathematical audit or exhaustive claim of bibliographic priority is made.

## References
1. B. Collins and P. Śniady, *Integration with respect to the Haar measure on unitary, orthogonal and symplectic group*, arXiv:math-ph/0402073, first submitted 2004-02-26, especially Section 2.2 and Corollary 2.4. https://arxiv.org/abs/math-ph/0402073
2. O. Borisenko, S. Voloshyn and V. Chelnokov, *SU(N) polynomial integrals and some applications*, arXiv:1812.06069, first submitted 2018-12-14, especially Sections 2, 3.1 and 3.2. https://arxiv.org/html/1812.06069v1
