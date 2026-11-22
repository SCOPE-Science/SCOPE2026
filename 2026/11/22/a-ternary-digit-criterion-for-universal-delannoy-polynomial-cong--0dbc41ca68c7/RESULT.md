# A ternary-digit criterion for universal Delannoy-polynomial congruences modulo nine

## Finding
For each nonnegative integer \(n\), define the Delannoy polynomial
\[
D_n(X)=\sum_{j=0}^{n}\binom nj\binom{n+j}j X^j\in\mathbb Z[X].
\]
Then the congruence \(D_n(z)\equiv1\pmod9\) holds **for every integer \(z\)** precisely for indices \(n\) with no digit \(1\) in base three and satisfying the following additional digit-coupling condition. Write the ternary digits as \(n=2\sum_{i\ge0}u_i3^i\), where \(u_i\in\{0,1\}\) and all but finitely many are zero. Set
\[
c(u)=u_0+2\sum_{i\ge1}u_i+\sum_{i\ge0}u_i u_{i+1}\pmod3.
\]
Then the **complete pointwise congruence** for every such index is
\[
\boxed{D_n(z)\equiv\begin{cases}
1+3c(u)\pmod9,&z\equiv1\pmod3,\\
1\pmod9,&z\equiv0,2\pmod3.
\end{cases}}
\]
In particular, the universal congruence holds if and only if \(c(u)=0\) in \(\mathbb F_3\).

For every integer \(r\ge0\), the number \(N_r\) of such indices with \(0\le n<3^r\) is given **exactly** by
\[
\boxed{N_r=\frac{2^r+\epsilon_{r\bmod6}}{3},\qquad
(\epsilon_0,\epsilon_1,\epsilon_2,\epsilon_3,\epsilon_4,\epsilon_5)=(2,1,-1,-2,-1,1).}
\]
Thus the prime-square restriction removes asymptotically two thirds of the indices satisfying the corresponding first-power universal congruence, and its finite-block count has an exactly six-periodic bounded defect from \(2^r/3\).

## Assumptions and scope
All \(n\) are ordinary nonnegative integers; the congruence is about **values at every integer argument**, rather than equality of polynomial coefficients modulo nine. The digits \(u_i\) are least-significant first, with infinitely many implicit leading zeros, and their sums are finite. For positive \(n\), the universal congruence is equivalent to \(9\mid\gcd_{z\in\mathbb Z}(D_n(z)-1)\); the formulation by universal congruence also includes \(n=0\) without a convention for a zero fixed divisor. The first-power digit restriction is a known consequence of polynomial Lucas congruences; the additional coupling and exact count are the new assertions.

## Proof
**1. The first-power obstruction.** An integral Vandermonde transformation gives
\[
D_n(X)=\sum_{j=0}^n\binom nj^2X^j(1+X)^{n-j}.
\]
Ordinary Lucas congruences and \((1+X)^3\equiv1+X^3\pmod3\) imply
\[
D_{3a+b}(X)\equiv D_a(X^3)D_b(X)\pmod3
\qquad(0\le b<3).
\]
On \(\mathbb F_3\), this yields \(D_n(z)\equiv\prod_iD_{d_i}(z)\pmod3\) for the ternary digits \(d_i\) of \(n\). Since \(D_0=1\), \(D_1(X)=1+2X\), and \(D_2(X)=1+6X+6X^2\), the value at \(z=1\) is zero whenever a digit equals one. If all digits belong to \(\{0,2\}\), every digit factor is one for every \(z\pmod3\). Therefore those, and only those, indices can satisfy the desired universal congruence. They are even and can uniquely be written \(n=2m\), with ternary digits \(m=\sum_i u_i3^i\), \(u_i\in\{0,1\}\).

**2. Only one argument class matters modulo nine.** From the integer-coefficient formula, \(D_n(X)=1+n(n+1)X+O(X^2)\). For \(n\) with digits zero or two, \(n\equiv0\) or \(2\pmod3\), so \(3\mid n(n+1)\). Hence \(D_n(z)\equiv1\pmod9\) for \(3\mid z\). The identity \(D_n(-1-X)=(-1)^nD_n(X)\), from \(D_n(X)=P_n(1+2X)\) and Legendre parity, proves the same when \(z\equiv-1\pmod3\). For \(z\equiv1\pmod3\), let \(s=1+2z\equiv0\pmod3\). The classical Legendre generating function is
\[
\sum_{n\ge0}P_n(s)t^n=(1-2st+t^2)^{-1/2}.
\]
Its expansion at \(s=0\), up to terms divisible by \(s^2\), is
\((1+t^2)^{-1/2}+st(1+t^2)^{-3/2}\). For even indices the linear term has zero coefficient, and \(s^2\equiv0\pmod9\). Consequently, for every \(m\ge0\) and \(z\equiv1\pmod3\),
\[
D_{2m}(z)\equiv P_{2m}(0)=A_m
:=(-1)^m4^{-m}\binom{2m}m\pmod9.
\tag{1}
\]
Here the apparent rational quantities have denominators powers of four, which are units modulo nine; the congruences are rigorous in \(\mathbb Z_{(3)}\).

**3. Prime-square binomial scaling.** For all nonnegative integers \(a,b\),
\[
\binom{3a}{3b}\equiv\binom ab\pmod9.
\tag{2}
\]
Indeed, in \(\mathbb Z[T]\), \((1+T)^3=1+T^3+3T(1+T)\). Expanding its \(a\)-th power modulo nine leaves terms with zero or one occurrence of \(3T(1+T)\); the latter terms have exponents congruent to one or two modulo three, so the coefficient of \(T^{3b}\) is exactly that of \((1+T^3)^a\) modulo nine.

Apply (2) with \(a=2q,b=q\). By the exact central-binomial ratio \(\binom{2m+2}{m+1}/\binom{2m}m=2(2m+1)/(m+1)\), the quantities in (1) obey
\[
\begin{aligned}
A_{3q}&\equiv (1+3q)A_q\pmod9,\\
A_{3q+1}&\equiv4(1+6q)A_q\pmod9.
\end{aligned}
\tag{3}
\]
For the first equality use \(4^{-2q}\equiv1+3q\pmod9\); for the second, the exact ratio \(A_{m+1}/A_m=-(2m+1)/(2(m+1))\) gives \(A_{3q+1}/A_{3q}\equiv4(1+3q)\pmod9\). Denominators in this ratio are units for \(m=3q\). Only \(q\pmod3\) enters the right-hand sides.

Iterating (3) over the ternary digits \(u_i\in\{0,1\}\), with \(A_0=1\), proves \(A_m\equiv1+3c(u)\pmod9\): inserting a least-significant zero increases the residue exponent by the next digit, while inserting a least-significant one increases it by \(1+2\) times the next digit, modulo three. Directly, the displayed formula for \(c\) has precisely the same two recursions and vanishes for the empty word. Combining with (1) and Step 2 establishes the complete pointwise congruence and criterion.

**4. Exact enumeration.** Process the digits \(u_0,\dots,u_{r-1}\) from least to most significant. After the first digit, track its current terminal value \(a\in\{0,1\}\) and accumulated residue \(c\in\mathbb Z/3\mathbb Z\). Appending the next digit \(b\in\{0,1\}\) gives
\[
(a,c)\longmapsto\bigl(b,c+(2+a)b\bmod3\bigr).
\]
In the state order \((0,0),(0,1),(0,2),(1,0),(1,1),(1,2)\), write the transition matrix, with columns indexed by old states, as
\[
M=\begin{pmatrix}
1&0&0&1&0&0\\
0&1&0&0&1&0\\
0&0&1&0&0&1\\
0&1&0&1&0&0\\
0&0&1&0&1&0\\
1&0&0&0&0&1
\end{pmatrix}.
\]
The first digit produces the state vector \(v=(1,0,0,0,1,0)^{\mathsf T}\), and the indicator of residue zero is \(e=(1,0,0,1,0,0)\). Thus \(N_0=1\) and \(N_r=eM^{r-1}v\) for \(r\ge1\). An exact six-by-six rational-function calculation gives
\[
\sum_{r\ge1}N_r t^r=t\,e(I-tM)^{-1}v
=\frac{t(1-2t+2t^2)}{(1-2t)(1-t+t^2)}.
\tag{4}
\]
This identity is also checked directly by multiplying the displayed matrices, so it needs no numerical extrapolation. Adding \(N_0=1\), partial fractions give
\[
\sum_{r\ge0}N_r t^r
=\frac1{3(1-2t)}+\frac{2-t}{3(1-t+t^2)}.
\]
The second denominator has reciprocal roots that are sixth roots of unity; its coefficients are the six-periodic values \((2,1,-1,-2,-1,1)/3\). This proves the exact formula for every \(r\ge0\). \(\square\)

## Verification
Run `python3 verify.py` in the same folder. It uses the standard Python library and reports 9,282 exact finite diagnostic checks: comparison of the defining Delannoy sum with the Legendre recurrence; all nine argument residues at every index below \(3^8=6561\); the full predicted set of universal congruence indices; scaling congruences and the digit formula for representative admissible indices; and the counts \(N_0,\ldots,N_8=(1,1,1,2,5,11,22,43,85)\). The proof's infinite quantifiers are established in Steps 1–4, not by the finite checks.

## Relationship to prior work
The polynomial identity \(D_n(X)=P_n(1+2X)\), ordinary Lucas congruences, and the Legendre generating function are classical. The previously published first-power Delannoy fixed-divisor result classifies \(D_n(z)\equiv1\pmod p\) for all \(z\) using digit vectors; at \(p=3\) it yields exactly the digit restriction \(d_i\in\{0,2\}\). That result **does not** give the prime-square coupling \(\sum_i u_i u_{i+1}\) or the exact six-periodic prime-square count. Guo's 2014 Delannoy-polynomial congruences concern weighted sums of powers over the index, rather than the universal fixed-divisor problem at a single index. Sun's 2011 Legendre-polynomial congruences concern prime-index or truncated polynomial expressions and related higher-power congruences; they do not state this all-index universal mod-nine classification. Pan's 2015 \(q\)-Delannoy Lucas congruence is another first-order structural precursor. Rowland–Yassawi's general automatic-congruence framework permits the construction of finite automata for broad algebraic-sequence congruences but does not explicitly supply this concrete six-state language and exact count. The complete prime-power value image of \(D_n(1)\) concerns a different quantifier and does not settle which individual indices give \(D_n(z)=1\) simultaneously for every \(z\pmod9\). Searching related formulations did not identify an equivalent theorem; this is a qualified historical-priority assessment, not a proof of uniqueness.

## Limitations
The result is specific to the prime square nine; it does not classify universal congruences modulo \(27\), \(p^2\) for every prime, or exact valuations of the complete fixed divisor. The pointwise formula is asserted for indices avoiding digit one; indices with digit one are eliminated modulo three but not otherwise classified modulo nine. The public mathematical literature may contain a differently worded specialization of a more general automatic-sequence theorem.

## References
1. Zhi-Hong Sun, *Generalized Legendre polynomials and related congruences modulo \(p^2\)*, arXiv:1101.5386v1, publicly submitted 2011-01-27. https://arxiv.org/abs/1101.5386
2. Victor J. W. Guo, *Some congruences involving powers of Delannoy polynomials*, arXiv:1412.7724v1, publicly submitted 2014-12-10. https://arxiv.org/abs/1412.7724
3. Hao Pan, *A Lucas-type congruence for \(q\)-Delannoy numbers*, arXiv:1508.02046v1, publicly submitted 2015-08-09. https://arxiv.org/abs/1508.02046
4. Eric Rowland and Reem Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635v1, publicly submitted 2013-10-31. https://arxiv.org/abs/1310.8635
5. *A noncyclic base-13 fixed-divisor spectrum for Delannoy polynomials*, accessible mathematical record with detailed proof and a \(p=3\) digit specialization. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-noncyclic-base-13-fixed-divisor-spectrum-for-delannoy-polynomi--b2f35cba40cf
6. *Complete ternary residue spectrum of the central Delannoy numbers*, accessible mathematical record on the complete output-value image. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-ternary-residue-spectrum-of-the-central-delannoy-number--a6b6e5fa5c14
