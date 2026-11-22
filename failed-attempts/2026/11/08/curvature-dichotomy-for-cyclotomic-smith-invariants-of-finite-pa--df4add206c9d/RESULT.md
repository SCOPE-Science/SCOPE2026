# Curvature dichotomy for cyclotomic Smith invariants of finite-parabola Fourier sampling

## Finding

Let \(p\ge3\) be an odd prime, let \(a,b\in\mathbb F_p\), and set
\[
P_a=\{(t,at^2):t\in\mathbb F_p\}\subset\mathbb F_p^2.
\]
The unnormalized Fourier restriction from functions supported on \(P_b\) to Fourier samples indexed by \(P_a\), using the standard dot product, has the square matrix
\[
M_{a,b}(s,t)=\zeta_p^{st+ab\,s^2t^2},\qquad
s,t\in\mathbb F_p,\quad \zeta_p=\exp(2\pi i/p).
\]
Write \(\mathcal O=\mathbb Z_p[\zeta_p]\), \(\pi=\zeta_p-1\), and \(m=(p-1)/2\). All elementary divisors below are local Smith divisors over the discrete valuation ring \(\mathcal O\), considered up to multiplication by units.

**Curved pairs.** If \(ab\ne0\), the complete list of Smith exponents is
\[
\boxed{0,1,1,2,2,\ldots,m,m.}
\]
It is independent of the two nonzero curvatures, including their product.

**Flat boundary.** If \(ab=0\), the complete list is instead
\[
\boxed{0,1,2,\ldots,p-1.}
\]
Both matrices are nonsingular over \(\mathbb C\), and their determinant valuations are respectively
\[
\boxed{
 v_\pi(\det M_{a,b})=
 \begin{cases}
 (p^2-1)/4,&ab\ne0,\\
 p(p-1)/2,&ab=0.
 \end{cases}}
\]
Thus the exact largest local reconstruction denominator exponent drops from \(p-1\) to \((p-1)/2\) upon introducing nonzero quadratic curvature on both sampling and support curves.

## Assumptions and scope

The Fourier kernel uses the *positive* additive character \(\zeta_p^{x\cdot\xi}\); conjugating all entries has the same Smith exponents. The curves have the indicated parametrization and both contain the origin. The matrix has \(p\) rows and \(p\) columns, with each parameter represented exactly once. The coefficient ring is the completed cyclotomic integer ring \(\mathbb Z_p[\zeta_p]\); these are not claimed as global integral Smith divisors. We use the valuation \(v_\pi(\pi)=1\), for which \(v_\pi(p)=p-1\).

## Proof

**1. Multiplicative reduction in the curved case.** Put \(c=ab\in\mathbb F_p^\times\) and \(H_c(u)=u+cu^2\). The matrix entry depends only on \(u=st\):
\[
 M_{a,b}(s,t)=\zeta_p^{H_c(st)}.
\]
Let \(\omega:\mathbb F_p^\times\to\mathbb Z_p^\times\) denote the Teichmüller character, so \(\omega(u)\equiv u\pmod p\) and its values are the \((p-1)\)-st roots of unity. Consider the integral output/input bases consisting of the point mass at zero, the indicator of \(\mathbb F_p^\times\), and the nontrivial multiplicative characters \(u\mapsto\omega(u)^r\), \(1\le r\le p-2\), extended by zero at zero. The changes of basis are invertible over \(\mathcal O\): the multiplicative character table has determinant a unit since its inverse divides only by \(p-1\).

Under these bases, \(M_{a,b}\) splits into a two-dimensional block and a monomial block on nontrivial characters. The first block is
\[
\begin{pmatrix}1&p-1\\1&S_c\end{pmatrix},\qquad
S_c=\sum_{u\ne0}\zeta_p^{H_c(u)},
\]
whose elementary divisors are \(1\) and
\[
\Delta_c=S_c-(p-1)=\sum_{u\ne0}(\zeta_p^{H_c(u)}-1).
\]
For \(1\le r\le p-2\), multiplication sends \(\omega^r\) to \(L_r\omega^{-r}\), where
\[
L_r=\sum_{u\ne0}\omega(u)^r\zeta_p^{H_c(u)}.
\]
The nontrivial block is a permutation times \(\operatorname{diag}(L_1,\ldots,L_{p-2})\); it suffices to compute the \(\pi\)-valuations of \(\Delta_c\) and these \(L_r\).

**2. Exact first nonzero cyclotomic jets.** Choose the integer representative \(h(u)\in\{0,1,\ldots,p-1\}\) of \(H_c(u)\). Since \(\zeta_p=1+\pi\), we have the finite identity
\[
\zeta_p^{H_c(u)}=\sum_{j=0}^{p-1}\binom{h(u)}j\pi^j.
\]
For \(j<p\), reduction of the coefficient modulo \(p\) is the degree-\(2j\) polynomial
\[
F_j(u)=\frac{1}{j!}\prod_{h=0}^{j-1}(u+cu^2-h)
\quad\text{in }\mathbb F_p[u].
\]
In particular, for \(j\ge1\) its leading coefficient is \(c^j/j!\); its next-to-leading coefficient is \(c^{j-1}/(j-1)!\), since all terms from powers lower than \((u+cu^2)^j\) have degree at most \(2j-2\).

Use exact character orthogonality:
\[
\sum_{u\ne0}u^d=
\begin{cases}-1,&(p-1)\mid d,\\0,&(p-1)\nmid d,\end{cases}
\quad\text{in }\mathbb F_p.
\]
For \(1\le r\le p-2\), let \(E_r=p-1-r\) and \(k_r=\lceil E_r/2\rceil\). The constant coefficient of \(L_r\) is exactly zero. For every \(j<k_r\), the polynomial \(u^rF_j(u)\) contains no monomial whose positive exponent is a multiple of \(p-1\), since \(r+2j<p-1\). Hence the coefficient of \(\pi^j\) in \(L_r\) is divisible by \(p\). At \(j=k_r\), the sole eligible exponent of \(F_j\) is \(E_r\). If \(E_r=2k_r\), its coefficient is \(c^{k_r}/k_r!\); if \(E_r=2k_r-1\), its coefficient is \(c^{k_r-1}/(k_r-1)!\). Either is nonzero modulo \(p\). It follows that
\[
\boxed{v_\pi(L_r)=\left\lceil\frac{p-1-r}{2}\right\rceil.}
\]
Indeed, every earlier coefficient divisible by \(p\) contributes valuation at least \(p-1\), which exceeds \(k_r\le m\); higher-order terms cannot cancel the unique \(\pi^{k_r}\)-term.

For \(\Delta_c\), subtracting \(p-1\) removes the constant coefficient exactly. For \(j<m\), \(F_j\) has positive degree at most \(2j<p-1\) and zero constant term, so its sum over nonzero \(u\) is zero modulo \(p\). At \(j=m\), the leading term \((c^m/m!)u^{p-1}\) is the only term contributing to the sum, and its coefficient is nonzero. Since \(m<p-1\), the same valuation argument gives
\[
\boxed{v_\pi(\Delta_c)=m.}
\]
The list from the nontrivial characters is \(m,m-1,m-1,\ldots,1,1\); adding the elementary divisors \(0,m\) of the two-dimensional block gives \(0,1,1,2,2,\ldots,m,m\). No appeal to finite enumeration is made.

**3. Flat boundary.** For \(ab=0\), the matrix is the ordinary \(p\)-point Fourier matrix \(\zeta_p^{st}\). Set \(X_s=\zeta_p^s\). Its columns evaluate monomials \(1,X,\ldots,X^{p-1}\) at the distinct \(X_s\). Replace the monomials by the monic Newton polynomials
\[
N_k(X)=\prod_{j=0}^{k-1}(X-X_j),\qquad0\le k<p.
\]
This column change is unitriangular over \(\mathcal O\). The resulting evaluation matrix is lower triangular, with every entry in column \(k\) divisible by \(\pi^k\), and diagonal entry \(N_k(X_k)=\prod_{j<k}(\zeta_p^k-\zeta_p^j)\) of valuation exactly \(k\). Factoring \(\pi^k\) from column \(k\) leaves a lower-triangular matrix whose diagonal consists of units. Thus the Smith exponents are exactly \(0,1,\ldots,p-1\).

**4. Determinants and uniqueness.** Summing all Smith exponents gives \(2(1+\cdots+m)=m(m+1)=(p^2-1)/4\) in the curved case and \(0+\cdots+(p-1)=p(p-1)/2\) in the flat case. Since no elementary divisor vanishes, every matrix is nonsingular over \(\mathbb Q_p(\zeta_p)\), hence its exact cyclotomic determinant is a nonzero algebraic number and the complex matrix is invertible. The maximum exponent in each list is the exact loss of local integral precision under inversion.

## Verification

The standalone Python 3 script `verify.py` tests the curved Smith lists directly over the exact truncated ring \(\mathbb F_p[\pi]/(\pi^{m+1})\) for primes \(p=3,5,7,11,13,17,19\) and for the distinct coefficients \(c\in\{1,2,-1\}\). There are 20 field-coefficient cases. Each matrix is formed from the actual binomial coefficients of its Fourier entries; a valuation-minimal pivot algorithm performs elementary row and column operations over the truncated ring, without relying on floating point calculations or on the predicted character decomposition. All computed exponents equal the stated sequence.

Reproduce using `python3 verify.py` from the directory containing this file. The checker prints `PARABOLIC_LOCAL_SMITH_PASS`. The flat boundary is proved by the exact Newton evaluation reduction above, not by applying a characteristic-\(p\) truncation beyond its valid precision. The finite calculations corroborate but do not prove the all-prime theorem.

## Relationship to prior work

Mockenhaupt and Tao initiated finite-field Fourier restriction and studied paraboloids, and Iosevich and Koh established extension estimates for quadratic surfaces. These results concern analytic estimates rather than the local arithmetic elementary divisors of a square restriction between two parabolic curves. Published classifications of orthonormal exponential bases on finite parabolas address exact pairwise orthogonality; they do not characterize this generally nonorthogonal invertible self-sampling matrix. Recent parabolic zero-set theorems address zeros of sparse Fourier sums over the entire frequency plane and do not state the full-support, specified-frequency local Smith classification here.

The distinction from earlier norm-one-conic Fourier sampling is also structural: the parabolic graph contains its origin and is not a multiplicative norm-one conic; its restricted Fourier kernel has a separate origin/uniform block and quadratic multiplicative phase, yielding a different sequence length and a flat-to-curved valuation transition. The character-table reduction and root-of-unity binomial expansions are classical techniques and are not claimed as inventions.

## Limitations

The theorem covers odd prime fields and precisely the two parabolic families \(P_a\), \(P_b\). It does not claim a numerical \(\ell^2\) condition number, global integer Smith normal form, all-minor nonvanishing, or any extension-field analog. Completeness is proved for these local Smith exponents, not for arbitrary frequency sets on a parabola. A general older theorem on twisted quadratic Gauss-sum valuations might implicitly imply this specialization; historical priority remains an explicit risk.

## References

1. Gerd Mockenhaupt and Terence Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234v1, first public 2002-04-18. https://arxiv.org/abs/math/0204234
2. Alex Iosevich and Doowon Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1, first public 2008-04-28. https://arxiv.org/abs/0804.4505
3. Dongwei Li, *Parity-Sensitive Fourier Uncertainty and Zero-Set Rigidity on the Finite Parabola*, arXiv:2609.16030v1, first public 2026-09-11. https://arxiv.org/abs/2609.16030
4. *Complete exponential spectra of the parabola over odd prime-power rings* (published mathematical research record, 2026), inspected in its complete theorem and proof for comparison with orthogonality-based results.
