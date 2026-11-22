# Sharp quadratic-character phase conditioning over prime fields

## Finding
For every prime \(p\ge5\), let \(\eta:\mathbb F_p\to\{0,\pm1\}\) be the quadratic character, with \(\eta(0)=0\), and put \(\omega=\exp(2\pi i/p)\). For any \(c\in\mathbb F_p^\times\), form the complex \(p\)-by-\(p\) matrix indexed by \(s,t\in\mathbb F_p\),
\[
 A_{p,c}(s,t)=\omega^{\eta(st+c)}.
\]
Thus every entry belongs to the three-phase alphabet \(\{1,\omega,\omega^{-1}\}\). The **least singular value** is, exactly,
\[
 \boxed{\sigma_{\min}(A_{p,c})=2\sin(\pi/p).}
\]
It is simple: the unique least right singular line is spanned by the vector \(v(0)=0\), \(v(t)=\eta(t)\) for \(t\ne0\). All matrices with \(c\ne0\) have the same singular-value multiset. To specify the **largest singular value**, write \(C=\cos(2\pi/p)\), \(S=\sin(2\pi/p)\), and
\[
 T_p=2p-1+\left|1+(p-1)C-e^{2\pi i/p}\right|^2,
 \qquad D_p=(1-C)^2+p^2 S^2.
\]
Then
\[
 \boxed{\sigma_{\max}(A_{p,c})=\left(\frac{T_p+\sqrt{T_p^2-4D_p}}2\right)^{1/2}.}
\]
Consequently the exact Euclidean spectral condition number is the ratio of these displayed quantities, and
\[
 \boxed{\kappa_2(A_{p,c})=\frac{p^2}{2\pi}+O(1)}
 \quad\text{as }p\to\infty\text{ through primes.}
\]
This quadratic degradation occurs despite every matrix entry having modulus one. There is exactly one weakest right-singular direction.

## Assumptions and scope
All results concern complex singular values of the **unnormalized** square matrix \(A_{p,c}\). The field must be a prime field of odd prime order at least five, the shift \(c\) is nonzero, and \(\omega\) is the primitive complex \(p\)-th root specified above. In particular, the quadratic character is evaluated in \(\mathbb F_p\) before mapping its values \(-1,0,1\) to integer exponents. Arbitrary simultaneous or independent relabelings of the rows and columns preserve the singular values. The singular vectors are specified for the original column labels.

The family is a natural three-phase analogue of multiplicative Hankel matrices: restriction to nonzero row and column indices gives an operator whose kernel depends only on \(st\), and multiplicative Fourier characters diagonalize its singular-value problem. The exact least singular value is the optimal worst-case \(\ell^2\)-noise amplification denominator in linear reconstruction from this matrix.

## Proof
**1. Reduction of all shifts to one shift.** If \(c\ne0\), write \(s=cr\). By multiplicativity of the Legendre character,
\[
 \eta(st+c)=\eta(c)\,\eta(rt+1).
\]
Hence \(A_{p,c}\) is a row permutation of \(A_{p,1}\) when \(\eta(c)=1\) and of its entrywise complex conjugate when \(\eta(c)=-1\). Both operations preserve every singular value. They also preserve the displayed real quadratic-character right singular line. It suffices to treat \(c=1\).

**2. Orthogonal decomposition.** Let \(n=p-1\), \(\vartheta=2\pi/p\), \(C=\cos\vartheta\), \(S=\sin\vartheta\), \(\delta=1-C\), and \(w=e^{i\vartheta}\). The kernel function on \(\mathbb F_p\) has the exact expansion
\[
 F(u)=e^{i\vartheta\eta(1+u)}
 = C+iS\eta(1+u)+\delta\,\mathbf1_{\{u=-1\}}.
\]
Use the orthonormal basis consisting of \(e_0\), the normalized constant vector \(n^{-1/2}\mathbf1_{\mathbb F_p^\times}\), and all normalized nontrivial multiplicative characters of \(\mathbb F_p^\times\), extended by zero at \(0\). The first two basis vectors span an invariant two-dimensional block, with representing matrix
\[
 B=\begin{pmatrix}
 w&\sqrt n\,w\\
 \sqrt n\,w&1+nC-w
 \end{pmatrix}.
\]
The lower-right entry follows from \(\sum_{u\in\mathbb F_p}F(u)=1+nC\). Every nontrivial multiplicative character \(\chi\) belongs to a different orthogonal Fourier sector: the full matrix sends \(\chi\) to \(L_\chi\chi^{-1}\), where
\[
 L_\chi=iS\sum_{u\ne0}\chi(u)\eta(1+u)+\delta\chi(-1).
\]
The singular value on that sector is therefore \(|L_\chi|\). The two-dimensional block singular values are the singular values of \(B\); no mixing between it and the other character sectors occurs.

**3. Exact weakest character.** The classical quadratic-character identity
\(\sum_{u\ne0}\eta(u)\eta(1+u)=-1\)
gives
\[
 L_\eta=-iS+\delta\eta(-1),\qquad
 |L_\eta|=\sqrt{S^2+\delta^2}=\sqrt{2\delta}=2\sin(\pi/p)=:m_p.
\]
For every nontrivial character \(\chi\ne\eta\), the sum in \(L_\chi\) is, up to a unit-modulus factor, a Jacobi sum for the three nontrivial characters \(\chi,\eta,\chi\eta\). The Gauss/Jacobi identity thus gives its modulus as \(\sqrt p\); consequently
\[
 |L_\chi|\ge S\sqrt p-\delta>m_p.
\]
Indeed, with \(\alpha=\pi/p\), the strict inequality is equivalent after \(S=2\sin\alpha\cos\alpha\), \(\delta=2\sin^2\alpha\), and \(m_p=2\sin\alpha\) to
\[
 \sqrt p\cos\alpha>1+\sin\alpha.
\]
For \(p\ge5\), the left side is at least \(\sqrt5\cos(\pi/5)\), and the right side is at most \(1+\sin(\pi/5)\); the former is strictly greater than the latter.

**4. The constant block has no equally weak mode.** A direct calculation gives
\[
 \operatorname{tr}(B^*B)=T_p,\qquad \det(B^*B)=D_p.
\]
Furthermore, since \(m_p^2=2\delta\),
\[
 \det(B^*B-m_p^2 I)
 =(p-1)(p-3)(1-C)^2(1+2C)>0.
\]
Also \(\operatorname{tr}(B^*B-m_p^2I)=T_p-4\delta>0\) for \(p\ge5\), using \(T_p\ge2p-1\), \(\delta<1\). The two real eigenvalues of \(B^*B-m_p^2 I\) are therefore strictly positive. Thus **both** constant-block singular values exceed \(m_p\). Together with Step 3 this proves the exact least singular value and uniqueness of its quadratic-character right-singular line.

**5. Exact largest singular value.** The two singular values of \(B\) are
\[
 \sigma_\pm(B)=\left(\frac{T_p\pm\sqrt{T_p^2-4D_p}}2\right)^{1/2}.
\]
Each nontrivial character sector is bounded by \(|L_\chi|\le S\sqrt p+\delta\) when \(\chi\ne\eta\), while \(|L_\eta|=m_p\). For \(p\ge7\),
\[
 \sigma_+(B)\ge|1+(p-1)C-w|
 \ge(p-1)C>\tfrac35(p-1)>\sqrt p+\tfrac12>S\sqrt p+\delta,
\]
where \(C\ge\cos(2\pi/7)>3/5\), \(\delta<1/2\), and the elementary comparison at \(p=7\) increases with \(p\). For \(p=5\), the second column of \(B\) has squared norm
\[
 4+|1+4C-w|^2=\frac{15+\sqrt5}{2}>\left(S\sqrt5+\delta\right)^2;
\]
for example \(S<24/25\), \(\sqrt5<9/4\), \(\delta<7/10\) make the right-hand square less than \((143/50)^2\), and the left side exceeds \(17/2\). Thus \(\sigma_+(B)\) dominates every character-sector singular value for all admissible primes, giving the claimed formula.

**6. Asymptotic conditioning.** Taylor expansion as \(p\to\infty\) gives \(T_p=p^2+O(1)\), \(D_p=4\pi^2+O(p^{-1})\), and therefore \(\sigma_+(B)=p+O(p^{-1})\). Meanwhile \(m_p=2\pi/p+O(p^{-3})\). Their ratio is \(p^2/(2\pi)+O(1)\).

## Verification
The standalone `CHECK.py` uses Python 3 and NumPy. Running `python CHECK.py` checks numerical least and greatest singular values, the unique quadratic-character weak mode, and the two-dimensional block formulas for ten odd primes from \(5\) through \(37\), with three distinct nonzero shifts for each prime. The checker reports 140 passed assertions. It is a finite numerical cross-check, **not** an exhaustive proof of the theorem. The exact algebraic argument is Steps 1–6 above; the classical Jacobi-sum modulus identity is the only imported nontrivial character-sum ingredient.

## Relationship to prior work
Wei–Li–Wu investigate determinants of generalized Legendre matrices over finite fields, including submatrices indexed by quadratic residues. Their results concern finite-field determinants, not complex singular values of the present \(p\)-dimensional three-phase shifted-product matrix. González-Riquelme–Oliveira e Silva study sharp finite-field extension inequalities on curved Fourier surfaces; those bounds do not specify this sampling matrix's smallest singular value or noise amplification. Existing finite-field Fourier sampling rank results, including the quadratic-phase full-rank theorem for \(e^{2\pi i(a st+b s^2t^2)/p}\), have a different phase function and give injectivity rather than the sharp spectral endpoints here. The computation relies on classical multiplicative characters and Jacobi sums; those classical identities are not claimed as new.

## Limitations
Only odd **prime** fields, nonzero shifts, and the specific phase angle \(2\pi/p\) are covered. No finite-field extension, other phase angle, or arbitrary character is classified. The theorem gives the exact Euclidean condition number but does not determine componentwise stability or rounding effects. A bounded literature comparison found no implication covering the exact sharp endpoint; an unlocated equivalent matrix identity remains a historical priority risk. No independent mathematical audit has been performed.

## References
1. N.-L. Wei, Y.-B. Li, H.-L. Wu, *On generalized Legendre matrices involving roots of unity over finite fields*, arXiv:2305.16064, first public 2023-05-25, https://arxiv.org/abs/2305.16064.
2. C. González-Riquelme, D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647, first public 2024-05-26, https://arxiv.org/abs/2405.16647.
3. Ö. Eğecioğlu, *A Prime Sensitive Hankel Determinant of Jacobi Symbol Enumerators*, Ann. Comb. 14 (2010), 443–456; publicly available online 2011-02-19, https://doi.org/10.1007/s00026-011-0069-6.
4. Classical Jacobi-sum modulus relation, obtained from Gauss sums \(J(\chi,\psi)=G(\chi)G(\psi)/G(\chi\psi)\) when all three characters are nontrivial; see, e.g., the introductory discussion of Jacobi sums at https://en.wikipedia.org/wiki/Jacobi_sum.
5. *Sharp rank trichotomy for quadratic-phase Fourier sampling on a prime-field parabola*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-rank-trichotomy-for-quadratic-phase-fourier-sampling-on-a--5bfb4c77019d.
