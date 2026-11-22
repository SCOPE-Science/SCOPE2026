# Exact index-six quasi-multiplicative orbit counts and sharp period twelve

## Finding

Let \(q=6s+1\) be a prime power, with \(s\ge1\). Denote by \(Q_6(q)\) the number of quasi-multiplicative equivalence classes of permutation-polynomial **functions** \(F:\mathbb F_q\to\mathbb F_q\) satisfying \(F(0)=0\) and having **exact polynomial index six**. Here two functions are equivalent when
\[
G(x)=uF(vx^d)\quad(x\in\mathbb F_q),\qquad
u,v\in\mathbb F_q^\times,\quad\gcd(d,q-1)=1.
\]
The polynomial index is \((q-1)/\gcd(q-1,e_2-e_1,\ldots,e_n-e_1)\) for the exponents of the nonzero nonconstant terms of the unique reduced representative.

The complete formula is:

| Arithmetic condition on \(s\) | \(Q_6(6s+1)\) |
|:--|:--|
| \(2\nmid s,\ 3\nmid s\) | \(\dfrac{60s^5+8s^2-3s+1}{6}\) |
| \(s\equiv2\pmod4,\ 3\nmid s\) | \(\dfrac{60s^5+16s^2-3s+2}{12}\) |
| \(4\mid s,\ 3\nmid s\) | \(\dfrac{s(20s^4+16s-1)}4\) |
| \(2\nmid s,\ 3\mid s\) | \(\dfrac{120s^5-8s^2+27s-9}{18}\) |
| \(s\equiv2\pmod4,\ 3\mid s\) | \(\dfrac{120s^5-16s^2+27s-18}{36}\) |
| \(12\mid s\) | \(\dfrac{s(40s^4+9)}{12}\) |

**The least possible quasi-polynomial period of \(s\mapsto Q_6(6s+1)\) is exactly \(12\)**, when restricted to prime-power values of \(q=6s+1\). In particular, the general period-divisibility bound \(2\ell\) for even index \(\ell\), recently proved by Fan, is sharp at the smallest squarefree composite index \(\ell=6\).

## Assumptions and scope

Only prime powers \(q\equiv1\pmod6\) are in the theorem's domain; neither a general integer \(6s+1\) nor permutation polynomials with nonzero constant term are included. Polynomial functions are identified modulo \(X^q-X\). The quasi-polynomial period means a positive integer \(T\) such that the function on the admissible \(s\)'s agrees on each residue class modulo \(T\) with a polynomial in \(s\). The displayed expressions have period dividing \(12\), and the last assertion rules out all smaller periods.

## Proof

**1. A finite-degree reduction.** By Fan [1, Theorem 4.5], for \(\ell=6\) there are degree-at-most-five polynomials \(P_r\in\mathbb Q[s]\), one for each residue \(r\pmod{12}\), such that \(Q_6(6s+1)=P_r(s)\) whenever \(6s+1\) is a prime power and \(s\equiv r\pmod{12}\). Thus *six distinct admissible values of \(s\) for every \(r\)* uniquely determine \(P_r\). Importantly, this finite determination of an infinite claim invokes the proven degree and period theorem; it is not an inference from an observed pattern.

**2. Exact finite counting.** Fix an admissible \(s\), a generator \(\gamma\) of \(\mathbb F_q^\times\), and \(\zeta=\gamma^s\). The normalized root-value model of [1, Sections 2–4] has \(120\) permutations \(\sigma\in S_6\) with \(\sigma(0)=0\). For each such \(\sigma\), write \(e_j\in\{0,1,\ldots,5\}\) for \(\sigma(j)-j\pmod6\). The normalized root values are \(U_j=\gamma^{e_j+6x_j}\), with \(x_0=0\) and \(x_j\in\mathbb Z/s\mathbb Z\).

The acting group consists of \(\omega=(k,t)\) with \(0\le k,t<6\), \(\delta=1+ks\) invertible modulo six, and induced index map \(\alpha(j)=t+\delta j\pmod6\). Such an element fixes the induced permutation precisely when
\[
\sigma(\alpha(j))-\sigma(t)\equiv\sigma(j)\pmod6
\qquad(0\le j<6).
\]
To impose exact index six, apply Möbius inversion over \(d\mid6\), with coefficients \(1,-1,-1,1\) for \(d=1,2,3,6\), respectively. For each \(d\) and \(c\in\mathbb Z/d\mathbb Z\), put \(m=6/d\). The fixed-point/support system has no solutions unless
\[
e_{j+m}-e_j\equiv scm\pmod6\quad(0\le j<6),
\qquad d\mid k(1+cs).
\]
Under those conditions set \(\widetilde k=k(1+cs)\pmod6\) and \(\rho_j=e_j-csj\pmod6\), using representatives between zero and five. On \(\mathbb Z/m\mathbb Z\), let \(\bar\alpha(j)=t+\delta j\pmod m\) and
\[
b_j=\frac{s\widetilde k j-\rho_j+\rho_{\bar\alpha(j)}-\rho_{t\bmod m}}6.
\]
The numerator is an integer multiple of six under the preceding stabilizer and support conditions [1, Lemma 4.1]. If the cycles of \(\bar\alpha\) are \(C_1,\ldots,C_N\), the number \(\nu_{\sigma,\omega,d,c}\) of solutions is zero unless the congruences
\[
|C_i|y\equiv\sum_{j\in C_i}b_j\pmod s
\quad(i=1,\ldots,N)
\]
have a common \(y\pmod s\); when they do, it is exactly
\[
\nu_{\sigma,\omega,d,c}=s^{N-1}\gcd(s,|C_1|,\ldots,|C_N|).
\]
Consequently Burnside's lemma [1, Theorem 4.2], without selecting double-coset representatives, gives
\[
Q_6(6s+1)=\frac1{|\Gamma|}
\sum_{\substack{\sigma\in S_6\\\sigma(0)=0}}
\sum_{\substack{0\le k,t<6\\\gcd(1+ks,6)=1\\\sigma\circ\alpha-\sigma(t)=\sigma}}
\sum_{d\mid6}\mu(d)\sum_{c\bmod d}\nu_{\sigma,\omega,d,c},
\]
where \(|\Gamma|=6\#\{k\in\{0,\ldots,5\}:\gcd(1+ks,6)=1\}\). Every summand is evaluated by finite integer arithmetic in the supplied `checker.py`; it loops over every normalized induced permutation, every admissible group element, all four squarefree divisors, and every supported residue \(c\).

**3. Exact interpolation certificate.** For each \(r=1,\ldots,12\), the following six values of \(s\) satisfy \(s\equiv r\pmod{12}\) and have \(q=6s+1\) prime (the primality assertions are also checked by trial division in the supplied code). Evaluating the foregoing integer sum gives the expression in the table of the Finding at all six points:

| \(r\) | Six distinct prime-field interpolation values \(s\) |
|:--|:--|
| 1 | 1, 13, 25, 37, 61, 73 |
| 2 | 2, 26, 38, 62, 110, 122 |
| 3 | 3, 27, 51, 63, 87, 123 |
| 4 | 16, 40, 52, 76, 100, 112 |
| 5 | 5, 17, 77, 101, 125, 137 |
| 6 | 6, 18, 30, 66, 90, 102 |
| 7 | 7, 55, 91, 103, 115, 151 |
| 8 | 32, 56, 68, 128, 188, 200 |
| 9 | 21, 33, 45, 81, 105, 153 |
| 10 | 10, 46, 58, 70, 118, 142 |
| 11 | 11, 23, 35, 47, 83, 95 |
| 12 | 12, 72, 96, 156, 168, 192 |

Since both sides are polynomials of degree at most five on each of the twelve classes and agree at six distinct arguments in that class, they coincide identically. This proves the six-case formula for *every* admissible prime power, not merely the sample fields.

**4. Minimality of the period.** For \(r\equiv6\pmod{12}\), the polynomial is \((120s^5-16s^2+27s-18)/36\), whereas for \(r\equiv0\pmod{12}\) it is \(s(40s^4+9)/12\); their difference is \(-(16s^2+18)/36\neq0\). Thus period six cannot work. For \(r\equiv4\pmod{12}\), the polynomial has leading coefficient \(5\), whereas for \(r\equiv0\pmod{12}\) it has leading coefficient \(10/3\). Thus period four cannot work. Every proper divisor of twelve divides six or four, so no proper divisor is a coefficient period. This also excludes **any other positive period** on the prime-power domain: if a period \(T\) were possible, compare the constituent polynomials along simultaneous classes modulo \(12\) and \(T\). Dirichlet's theorem ensures a simultaneous class contains infinitely many primes \(6s+1\) whenever the specified residues are compatible and avoid the unique forbidden residue modulo each prime \(p\ge5\) dividing \(T\); primes two and three are no obstruction since \(6s+1\equiv1\pmod6\). For each two residue classes modulo twelve that coincide modulo \(g=\gcd(12,T)\), one can choose a common residue modulo \(T\) avoiding those finitely many forbidden residues, then use the Chinese remainder theorem and Dirichlet to force equality of their constituent polynomials. If \(T<12\), its \(g\) is a proper divisor of twelve, hence divides either four or six, contradicting the two polynomial differences above. (Indeed the same argument shows every period \(T\) is divisible by twelve.) Thus the **least** period on the actual prime-power domain is twelve.

## Verification

Run `python3 checker.py` with Python 3 (no third-party dependencies). It verifies the exact Burnside count at **72 prime-field interpolation points**, additionally checks a seventh prime-field value in each residue class (12 out-of-sample checks), and independently enumerates normalized root-value orbits for \(s=1,2,3\). The successful final output is `INDEX6_SHARP_QUASIPERIOD_OK 72_prime_interpolations 12_extra_prime_controls 3_direct_orbit_checks`. Trial division in this file verifies every declared prime. The infinite inference is justified by the cited degree-five quasi-polynomial theorem and the polynomial identity argument, not by experimental extrapolation.

For small cases, the formula gives \(Q_6(7)=11\), \(Q_6(13)=165\), and \(Q_6(19)=1620\). The separate orbit enumerator reproduces all three values.

## Relationship to prior work

Fan [1] proved the general fixed-point counting mechanism and the period upper bound twelve for index six, and gave closed-form answers for odd prime indices and index four. The six explicit index-six polynomial formulas and the **sharpness** of the period bound at this squarefree composite index are not asserted in its theorems, case discussions or appendices. This note uses Fan's results as essential premises and does not claim a new general orbit-classification method.

Garg, Hasan, Li, Kumar and Pal [2] study quasi-multiplicative inequivalence among specifically constructed sparse permutation polynomials over quadratic extensions, not the complete exact-index-six orbit-count function. The prime-index binomial collision and sign-bias calculations of other works concern still different restricted families.

## Limitations

The proof depends on Fan's published general quasi-polynomial theorem and root-value fixed-point formula, and uses a reproducible finite calculation to determine the twelve coefficient polynomials. It does not give a new formula for nonzero-constant permutation-polynomial classes, nor a classification of individual polynomial representatives. The originality comparison is based on the inspected texts and indexed searches; an unindexed earlier index-six computation remains a possibility. Independent mathematical audit has not been performed.

## References

[1] Xiang Fan, *Permutation polynomials of given index up to quasi-multiplicative equivalence*, arXiv:2611.16944v1, publicly submitted 12 November 2026. https://arxiv.org/html/2611.16944v1 (Theorems A, B, 2.3, 4.2, 4.5 and Lemma 4.1).

[2] Kirpa Garg, Sartaj Ul Hasan, Chunlei Li, Hridesh Kumar, Mohit Pal, *Permutation polynomials with a few terms over finite fields*, arXiv:2503.20982v3, 2025. https://arxiv.org/html/2503.20982v3 (Section 5).
