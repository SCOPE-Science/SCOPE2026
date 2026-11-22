# Exact joint ternary valuation law for Catalan and central binomial numbers

## Finding

Let \(B_n=\binom{2n}{n}\), \(C_n=B_n/(n+1)\), and let \(\nu_3\) be the exponent of three dividing a nonzero integer. For all integers \(L\ge0\), define
\[
P_L(x,y)=\sum_{0\le n<3^L}x^{\nu_3(B_n)}y^{\nu_3(C_n)}.
\]
Then the **complete joint valuation distribution, at every ternary index depth**, is the following rational formal series:
\[
\boxed{\sum_{L\ge0}P_L(x,y)u^L
=\frac{1-2uxy+u^2(x^2y+xy-x)}{(1-ux)\bigl(1-2(1+xy)u+3xyu^2\bigr)}.}
\tag{1}
\]
For every \(L\ge1\), the attainable pairs of valuations are **exactly**
\[
\boxed{\{(a,b):0\le b\le a\le L\}\setminus\{(L,L)\},}
\tag{2}
\]
so there are \(L(L+3)/2\) such pairs. The top boundary has the particularly simple exact frequencies
\[
\boxed{[x^L y^b]P_L(x,y)=\begin{cases}1,&b=0,\\2^{b-1},&1\le b<L.\end{cases}}
\tag{3}
\]
If \(N_L\) is uniform on \(\{0,\ldots,3^L-1\}\), write \(A_L=\nu_3(B_{N_L})\), \(H_L=\nu_3(C_{N_L})\), and \(q=3^{-L}\). Their exact covariance is
\[
\boxed{\operatorname{Cov}(A_L,H_L)=\frac L2-\frac{17}{16}+\left(\frac L2+\frac54\right)q-\frac{3q^2}{16}.}
\tag{4}
\]
In particular the covariance grows linearly, not merely by a bounded correction. Both centered valuations have the **same** normal fluctuation:
\[
\boxed{\left(\frac{A_L-L/2}{\sqrt{L/2}},\frac{H_L-L/2}{\sqrt{L/2}}\right)\Longrightarrow (Z,Z),\quad Z\sim\mathcal N(0,1).}
\tag{5}
\]
Thus this pair has asymptotically perfect, rather than asymptotically independent, Gaussian fluctuations.

## Assumptions and scope

All binomial and Catalan numbers are positive integers, with \(B_0=C_0=1\). All three exponents in (1) are formal indeterminates; \(u\) marks digit length, while \(x\) and \(y\) mark two exact, nonnegative valuations. A zero-length ternary string represents \(n=0\) and contributes \(P_0=1\). Equations (1)--(4) hold for every specified finite \(L\). Equation (5) is a limit theorem only as \(L\to\infty\).

## Proof

**1. Carry and trailing-digit decomposition.** Kummer's theorem gives \(A(n)=\nu_3(B_n)\) as the number of carries, including the final outgoing carry, when adding the base-three digits of \(n+n\). From \(C_n=B_n/(n+1)\),
\[
H(n)=\nu_3(C_n)=A(n)-t(n),\qquad t(n)=\nu_3(n+1).
\tag{6}
\]
Write an index \(0\le n<3^L\) with exactly \(L\) ternary digits read from least to most significant. The integer \(t(n)\) is the number of initial digits equal to \(2\); for the all-\(2\) string this is \(L\). Each such digit creates a carry, so the subtraction in (6) cancels exactly these first \(t(n)\) carries. If all digits are \(2\), the pair is \((A,H)=(L,0)\).

Let \(z=xy\). Once the first non-\(2\) digit is processed, each later carry contributes the joint factor \(z\). The weighted carry matrix, with incoming carry \(0,1\) in rows and outgoing carry \(0,1\) in columns, is
\[
M(z)=\begin{pmatrix}2&z\\1&2z\end{pmatrix}.
\tag{7}
\]
Indeed, a digit \(d\in\{0,1,2\}\) in incoming carry state \(c\) produces outgoing carry \(\lfloor(2d+c)/3\rfloor\). Set \(F_j^{(c)}(z)=e_c M(z)^j\mathbf1\), where \(e_c\) is the indicated unit row vector and \(\mathbf1=(1,1)^T\).

If \(t=0\), the first digit is \(0\) or \(1\), and both give outgoing carry zero. Their combined contribution is \(2F_{L-1}^{(0)}(z)\). If \(1\le t<L\), the \(t\) trailing digits \(2\) contribute \(x^t\). The first non-\(2\) digit is \(0\) (outgoing carry zero) or \(1\) (outgoing carry one); hence this class contributes
\[
x^t\bigl(F_{L-t-1}^{(0)}(z)+zF_{L-t-1}^{(1)}(z)\bigr).
\]
Adding the all-\(2\) word gives the exhaustive, disjoint identity
\[
P_L(x,y)=x^L+2F_{L-1}^{(0)}(z)+\sum_{t=1}^{L-1}x^t\bigl(F_{L-t-1}^{(0)}(z)+zF_{L-t-1}^{(1)}(z)\bigr)
\quad(L\ge1).
\tag{8}
\]

**2. Rational generating function.** Matrix inversion in the ring of formal series gives
\[
\sum_{j\ge0}u^j\begin{pmatrix}F_j^{(0)}(z)\\F_j^{(1)}(z)\end{pmatrix}
=(I-uM(z))^{-1}\mathbf1
=\frac{1}{\Delta(u,z)}\begin{pmatrix}1-uz\\1-u\end{pmatrix},
\quad \Delta(u,z)=1-2(1+z)u+3zu^2.
\tag{9}
\]
Multiply (8) by \(u^L\) and sum over \(L\ge1\), including \(P_0=1\). The result, prior to simplification, is
\[
1+\frac{ux}{1-ux}+\frac{2u(1-uz)}{\Delta(u,z)}
+\frac{u^2x(1+z-2uz)}{(1-ux)\Delta(u,z)}.
\]
Putting \(z=xy\) and combining denominators proves (1). Specializing \(x=1\) recovers the known one-variable Catalan valuation census
\[
\sum_{L\ge0}P_L(1,y)u^L=\frac{1+(1-2y)u}{1-2(1+y)u+3yu^2};
\]
specializing \(y=1\) gives the corresponding central-binomial carry census \((1-ux)/\Delta(u,x)\). Neither marginal by itself determines (1).

**3. All and only the claimed support.** From (6), \(0\le H\le A\le L\). If \(A=L\) and \(H=L\), then \(t=0\), but the first digit is \(0\) or \(1\), creating no carry, so at most \(L-1\) carries can occur: \((L,L)\) is impossible. To realize \((a,a)\) for \(0\le a\le L-1\), choose a least-significant-first string consisting of digit \(0\), followed by \(a\) digits \(2\), then zeros. To realize \((a,b)\) for \(0\le b<a\le L\), put \(t=a-b\). If \(b=0\) and \(t<L\), use \(t\) digits \(2\), then \(0\), then zeros; for \(t=L\), use the all-\(2\) string. If \(b\ge1\), use \(t\) digits \(2\), then \(b\) digits \(1\), then zeros. These constructions prove (2), including all boundary cases. To have \(A=L\), a string must create a carry at every digit. The all-\(2\) word is the unique \(b=0\) case. For \(1\le b<L\), the first \(t=L-b\) digits must be \(2\), then a digit \(1\), and then any of the \(2\) digits \(1,2\) in each of \(b-1\) remaining positions. This proves (3).

**4. Exact covariance.** Differentiating (1) and setting \(x=y=1\), or using the carry chain, gives for \(q=3^{-L}\)
\[
\mathbb E A_L=\frac L2-\frac14+\frac q4,\qquad
\mathbb E H_L=\frac L2-\frac34+\frac{3q}{4},
\]
and
\[
\mathbb E[A_LH_L]=\frac{(L+1)(L-1)}4-\frac58+\frac{(8L+7)q}{8}.
\]
Subtracting the product of the means yields (4) exactly, also at \(L=0\). The known exact marginal variances (also derivable by differentiation) are
\[
\operatorname{Var}(A_L)=\frac L2-\frac7{16}+\frac q2-\frac{q^2}{16},\quad
\operatorname{Var}(H_L)=\frac L2-\frac{15}{16}+\frac{3q}{2}-\frac{9q^2}{16}.
\]

**5. Limit law.** The two eigenvalues of \(M(z)\) are \(\lambda_\pm(z)=1+z\pm\sqrt{1-z+z^2}\). At \(z=1\), they equal \(3\) and \(1\); near \(z=1\) the first is simple and dominant. Its logarithmic moment-generating expansion is
\[
\log\frac{\lambda_+(e^s)}3=\frac s2+\frac{s^2}{4}+O(s^3).
\]
Consequently the standard analytic transfer-matrix argument proves \((A_L-L/2)/\sqrt{L/2}\Longrightarrow\mathcal N(0,1)\). Independently, \(t(N_L)\) has distribution
\[
\mathbb P(t=j)=2\cdot3^{-(j+1)}\ (0\le j<L),\qquad \mathbb P(t=L)=3^{-L}.
\]
Thus \(\sup_L\mathbb E t(N_L)\le1/2\), implying \(t(N_L)/\sqrt L\to0\) in probability. Equation (6) and Slutsky's theorem yield the joint limit (5), with no independence assertion about the unscaled difference.

## Verification

The standalone `verify.py` independently uses Legendre's factorial valuation formula to enumerate the exact pair \((\nu_3(B_n),\nu_3(C_n))\) for every \(n<3^9\). In parallel it generates the coefficients of (1) using exact two-variable polynomial arithmetic and its cubic-in-\(u\) denominator recurrence. It compares every coefficient, checks every support point and top-boundary multiplicity, and verifies exact rational means and covariance for \(1\le L\le9\). Separate integer-binomial calculations verify \(800\) initial terms. Recorded output:

`VERIFY_OK levels=0..9, exact_index_pairs=29523, binomial_cases=800, support_and_boundary=PASS, rational_moments=PASS`

These finite tests check the transcription and implementation. The proofs of all-depth identities and weak convergence are the preceding symbolic carry and transfer-matrix arguments.

## Relationship to prior work

Kummer's theorem gives the individual carry valuation, and the Catalan normalization gives (6); these classical facts are not new. Alter and Kubota (1973) analyzed prime and prime-power divisibility of Catalan numbers; the accessible abstract focuses on maximal blocks of prime-divisible terms, and the full paper was not inspected. Chen and Jiang (2013) studied individual Catalan congruences modulo prime powers, rather than a two-sequence valuation census. Snyder (2023) develops valuation trees for polynomial products, not the present binomial/Catalan index coupling. A published *Exact ternary-block distribution and Gaussian law for three-adic Catalan valuations* gives the one-variable specialization \(x=1\), including its Gaussian limit and moments, but does not supply the cross valuation coupling. The published *Joint ternary valuations of central and threefold binomial coefficients* treats a different pair \((\binom{2n}{n},\binom{3n}{n})\), whose covariance stays bounded rather than growing linearly. The joint law (1), sharp support (2)--(3), and covariance (4) are not implied by those statements. Historical priority beyond examined sources is not certified.

## Limitations

The result is confined to prime three and complete index intervals \(0\le n<3^L\). It does not give simultaneous valuations at distinct primes, local limit estimates, or uniform asymptotics for arbitrary real cutoffs. The closed form of the full 1973 Alter--Kubota paper was not available for direct comparison, so an older implicit equivalent remains a specific priority risk. The limiting Gaussian pair is degenerate; it does not imply independence of the unscaled valuations.

## References

1. E. Kummer, classical carry theorem for binomial-coefficient valuations (1852).
2. R. Alter and K. K. Kubota, "Prime and prime power divisibility of Catalan numbers," *J. Combin. Theory Ser. A* **15** (1973), 243--256, DOI:10.1016/0097-3165(73)90072-1; public abstract in *Notices of the AMS*, 1972, https://www.ams.org/journals/notices/197201/197201FullIssue.pdf .
3. Y.-G. Chen and W. Jiang, "Catalan numbers modulo a prime power," *Integers* **13** (2013), A36, https://sunsite3.icm.edu.pl/packages/EMIS/journals/INTEGERS/papers/n36/n36.pdf .
4. D. Snyder, "Products of p-Adic Valuation Trees," arXiv:2308.11718, first posted August 22, 2023, https://arxiv.org/abs/2308.11718 .
5. OEIS A067397, "Maximal power of 3 that divides n-th Catalan number," https://oeis.org/A067397 .
6. "Exact ternary-block distribution and Gaussian law for three-adic Catalan valuations," published October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-ternary-block-distribution-and-gaussian-law-for-three-adic--19d62501d861 .
7. "Joint ternary valuations of central and threefold binomial coefficients," published November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-joint-ternary-valuations-of-central-and-threefold-binomial-coeff--1999135510ae .
