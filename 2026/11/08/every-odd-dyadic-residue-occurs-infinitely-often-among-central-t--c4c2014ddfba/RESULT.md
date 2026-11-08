# Every odd dyadic residue occurs infinitely often among central trinomial coefficients

## Finding
For every integer \(n\ge0\), write
\[
T_n=[x^0](x^{-1}+1+x)^n=[x^n](1+x+x^2)^n.
\]
Then, for every integer \(k\ge1\),
\[
\{T_n\bmod 2^k:n\ge0\}=(\mathbb Z/2^k\mathbb Z)^\times,
\]
and **every odd class is realized at infinitely many distinct indices**. Equivalently,
\[
\overline{\{T_n:n\ge0\}}=\mathbb Z_2^\times.
\]
A constructive mechanism is furnished by the limit \(L=\lim_{r\to\infty}T_{2^r}\), which satisfies \(L\equiv3\pmod8\).

## Assumptions and scope
All coefficients and polynomial congruences are over the integers. The constant-term operation \([x^0]\) applies to Laurent polynomials with integer coefficients. A congruence between Laurent polynomials is coefficientwise. The index \(n\) ranges through all nonnegative integers; \(k\) ranges through the positive integers. The group \((\mathbb Z/2^k\mathbb Z)^\times\) consists of its odd residue classes. Density in the \(2\)-adic topology is equivalent to surjectivity onto every finite residue quotient. No claim about natural frequencies of representing indices is made.

## Proof
**Parity.** The standard finite expansion gives
\[
T_n=\sum_{j=0}^{\lfloor n/2\rfloor}\binom n{2j}\binom{2j}j.
\]
For every \(j\ge1\), the central binomial coefficient \(\binom{2j}j\) is even (pair each \(j\)-element subset of a \(2j\)-element set with its complementary subset; the pair contains distinct subsets). The term \(j=0\) equals one. Thus \(T_n\equiv1\pmod2\) for every \(n\ge0\).

**Frobenius precision and separated blocks.** Put \(P(x)=x^{-1}+1+x\). In the Laurent polynomial ring over the integers,
\[
P(x)^{2^s}\equiv P(x^{2^s})\pmod2
\]
for all integers \(s\ge0\), by repeated Frobenius in characteristic two. If Laurent polynomials \(A\equiv B\pmod2\), then
\[
A^{2^h}\equiv B^{2^h}\pmod{2^{h+1}}
\]
for every integer \(h\ge0\). Indeed the case \(h=0\) is the assumption, and
\(A^{2^{h+1}}-B^{2^{h+1}}=(A^{2^h}-B^{2^h})(A^{2^h}+B^{2^h})\), with the second factor even; induction gives the stated precision.

Consequently, for integers \(r\ge s\ge0\),
\[
P(x)^{2^r}\equiv P(x^{2^s})^{2^{r-s}}\pmod{2^{r-s+1}}.\tag{1}
\]
Fix \(k\ge1\), choose \(r\ge k\), and set \(s=r-k+1\). The right side of (1) has only exponents divisible by \(2^s\). Therefore every coefficient of \(P^{2^r}\) at an exponent \(j\) satisfying \(0<|j|<2^s\) is divisible by \(2^k\). For every integer \(m\) with \(0\le m<2^s\), convolution of constant terms with \(P^m\), whose support is \([-m,m]\), gives the **separated-block congruence**
\[
T_{2^r+m}\equiv T_{2^r}T_m\pmod{2^k}.\tag{2}
\]

**The stable doubling value.** Taking \(s=1\) in (1), for every \(r\ge1\) obtain
\[
P(x)^{2^r}\equiv P(x^2)^{2^{r-1}}\pmod{2^r}.
\]
The right-hand constant term is \(T_{2^{r-1}}\). Hence
\[
T_{2^r}\equiv T_{2^{r-1}}\pmod{2^r}.\tag{3}
\]
Thus \(T_{2^r}\) is Cauchy in \(\mathbb Z_2\). Denote its limit by \(L\). Since \(T_4=19\) and all differences after index \(4\) have divisibility at least \(8\),
\[
L\equiv19\equiv3\pmod8.\tag{4}
\]
Moreover \(T_{2^r}\equiv L\pmod{2^k}\) whenever \(r\ge k\).

**The multiplicative unit group.** Let \(k\ge3\). For any odd \(u\equiv3\pmod8\), \(\nu_2(u-1)=1\) and \(\nu_2(u+1)=2\), so \(\nu_2(u^2-1)=3\). Repeated squaring shows
\[
\nu_2(u^{2^h}-1)=h+2\qquad(h\ge1).\tag{5}
\]
Indeed all squares \(u^{2^h}\) with \(h\ge1\) are congruent to one modulo eight, and their sum with one has valuation exactly one. Equation (5) proves that the order of \(L\bmod2^k\) is \(2^{k-2}\). All powers of \(L\) reduce modulo eight to one or three, and these form an index-two subgroup with \(2^{k-2}\) elements. Hence the powers of \(L\) exhaust precisely the odd residues congruent to one or three modulo eight. Since \(T_3=7\equiv7\pmod8\), multiplication by seven maps this subgroup bijectively onto the complementary odd residues congruent to seven or five modulo eight.

**Realizing every product by actual indices.** Fix \(k\ge3\), \(b\in\{0,3\}\), and an arbitrary integer \(t\ge0\). Choose integers \(k\le r_1<\cdots<r_t\) sufficiently separated that
\[
b+\sum_{i<j}2^{r_i}<2^{r_j-k+1}\qquad(1\le j\le t).\tag{6}
\]
Such choices exist recursively because one can take the next exponent arbitrarily large. Applying (2) successively, with \(m=b+\sum_{i<j}2^{r_i}\), gives
\[
T_{b+\sum_{j=1}^t2^{r_j}}\equiv T_b\prod_{j=1}^tT_{2^{r_j}}\equiv T_b L^t\pmod{2^k}.\tag{7}
\]
For \(t=0\) the empty sum is zero and (7) simply means \(T_b\). As \(t\) varies, \(T_0L^t=L^t\) supplies the subgroup and \(T_3L^t=7L^t\) supplies its complementary coset. Thus every odd residue occurs. Keeping \(t\ge1\) fixed while increasing the last exponent (or choosing arbitrarily many different separated exponent sets) yields infinitely many distinct indices for each represented class; for the class attained with \(t=0\), replace \(t\) by the positive multiple \(2^{k-2}\) of the order of \(L\). Finally the statement for \(k=1,2\) follows by reducing the already proved \(k=3\) statement. Together with parity, these assertions prove the finding.

## Verification
The standalone script `verify_trinomial.py` evaluates the integer recurrence
\[
(n+1)T_{n+1}=(2n+1)T_n+3nT_{n-1}
\]
from \(T_0=T_1=1\), checks the defining binomial formula through index \(100\), checks odd parity through index \(2048\), verifies the block relation (2) on a range of exponents and residues, and compares generated unit subgroups modulo powers of two. It also empirically checks complete coverage for moduli through \(2^8\). These finite tests are not used to deduce the unrestricted theorem; that deduction is supplied above.

## Relationship to prior work
Noe (2006, Theorem 8.1) established parity for generalized central trinomial coefficients; his Theorem 8.5 treats divisibility by primes. Sun's 2010 preprint (subsequently published 2014) studies a broad family of trinomial congruences, chiefly weighted sums and congruences at odd primes. The integer-sequence record OEIS A002426 includes the Gauss congruences \(T_{np^r}\equiv T_{np^{r-1}}\pmod{p^r}\), which in the case \(p=2\) imply existence of \(L\), but do not by themselves imply that every odd residue is a central trinomial value. Kohen (2024) studies density and symmetry modulo primes, not images modulo arbitrary powers of two. The additional information here is the separated-block multiplication law, the multiplicative generator of an index-two unit subgroup, and the full all-level surjectivity and infinite attainment. A previously unrecognized stronger general theorem could still imply this statement; exhaustive historical priority is not asserted.

## Limitations
Only the ordinary central trinomial sequence and the prime two are treated. No asymptotic frequencies of indices in a given residue class are determined. The existence constructions generally use very large indices. Independent specialist validation and a complete historical priority audit are not provided.

## References
1. T. D. Noe, “On the Divisibility of Generalized Central Trinomial Coefficients,” *Journal of Integer Sequences* **9** (2006), article 06.2.7, https://cs.uwaterloo.ca/journals/JIS/VOL9/Noe/noe35.pdf.
2. Z.-W. Sun, “Congruences Involving Generalized Central Trinomial Coefficients,” first publicly posted 2010-08-23, arXiv:1008.3887, https://arxiv.org/abs/1008.3887.
3. OEIS Foundation, sequence A002426, “Central trinomial coefficients,” https://oeis.org/A002426 (dynamic reference).
4. N. Kohen, “Density and Symmetry in the Generalized Motzkin Numbers mod \(p\),” arXiv:2411.03681, first posted 2024-11-06, https://arxiv.org/abs/2411.03681.
