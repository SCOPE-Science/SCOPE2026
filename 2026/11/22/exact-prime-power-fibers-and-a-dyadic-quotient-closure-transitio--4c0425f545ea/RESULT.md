# Exact prime-power fibers and a dyadic quotient-closure transition for unit-seeded recurrences

## Finding
Let \(a\) be a nonzero integer and define
\[
x_0=x_1=1,\qquad x_{n+2}=a x_{n+1}+x_n\quad(n\ge0).
\]
For each prime \(p\mid a\), write \(h=\nu_p(a)\) and form the quotient set \(R_a=\{x_m/x_n:m,n\ge0\}\subset\mathbb Q\). Then every term is a \(p\)-adic unit and the following complete dichotomy holds.

**Regular case.** If \(p\) is odd, or \(p=2\) and \(h\ge2\), then for every integer \(k\ge1\), the least scalar period modulo \(p^k\) is \(1\) when \(k\le h\), and \(2p^{k-h}\) when \(k>h\). In the latter case, each residue congruent to \(1\pmod{p^h}\) occurs exactly twice per least period, once at an even index and once at an odd index; no other residue occurs. Furthermore, for distinct nonnegative integers \(s,t\),
\[
\nu_p(x_{2s}-x_{2t})=\nu_p(x_{2s+1}-x_{2t+1})=h+\nu_p(s-t).
\]
Consequently the closures in their stated ambient spaces are
\[
\overline{\{x_n:n\ge0\}}^{\,\mathbb Z_p}
=\overline{R_a}^{\,\mathbb Q_p}=1+p^h\mathbb Z_p.
\]
The Haar measure of either compact closure in \(\mathbb Z_p\) is \(p^{-h}\).

**Exceptional dyadic case.** If \(p=2\) and \(h=1\), the value closure contains both complete balls \(1+8\mathbb Z_2\) and \(7+8\mathbb Z_2\), and the quotient set instead has the full unit-group closure
\[
\boxed{\overline{R_a}^{\,\mathbb Q_2}=\mathbb Z_2^\times=1+2\mathbb Z_2.}
\]
Thus the quotient-set closure is the principal unit ball of depth \(h\) in every case, with a genuine change in the structure of the value fibers at dyadic valuation one.

## Assumptions and scope
The integer \(a\) may be positive or negative but must be nonzero; \(p\) is any prime divisor of \(a\), and indices are nonnegative integers. Valuation is normalized by \(\nu_p(p)=1\), and \(\mathbb Z_p\) is the ring of \(p\)-adic integers. Every quotient is defined because \(x_n\equiv1\pmod p\) for all indices. A scalar period means a positive \(T\) satisfying \(x_{n+T}\equiv x_n\pmod{p^k}\) for all \(n\ge0\). For the dyadic case \(h=1\) we claim the quotient closure and two full subballs of the value closure, but not a full value-frequency classification. No assertion concerns primes not dividing \(a\).

## Proof
**1. Matrix reduction and units.** Set
\[
M=\begin{pmatrix}a&1\\1&0\end{pmatrix},\qquad v=\binom11,\qquad e=\begin{pmatrix}0&1\end{pmatrix}.
\]
The state \((x_{n+1},x_n)^t=M^n v\), hence \(x_n=eM^n v\). Cayley–Hamilton gives \(M^2=I+aM\). When \(p\mid a\), the reduction of \(M\) modulo \(p\) interchanges coordinates and fixes \(v\); therefore \(x_n\equiv1\pmod p\) for every \(n\). In particular, all denominators are \(p\)-adic units, including when \(a<0\).

**2. Sharp isometry in the regular case.** Put \(C=M^2=I+aM\). For every positive integer \(d\), the binomial identity yields
\[
C^d-I=daM+\sum_{j=2}^{d}\binom dj a^jM^j.
\]
The elementary divisibility \(j\binom dj=d\binom{d-1}{j-1}\) gives \(\nu_p(\binom dj)\ge\nu_p(d)-\nu_p(j)\). Under the regular-case hypotheses, for all \(j\ge2\), \(jh-\nu_p(j)\ge h+1\). Thus each term in the sum is divisible by \(p^{h+\nu_p(d)+1}\) in every entry. For either \(\epsilon\in\{0,1\}\),
\[
x_{2(t+d)+\epsilon}-x_{2t+\epsilon}
=eM^\epsilon C^t(C^d-I)v
=da\,(eM^{\epsilon+1}C^tv)+O(p^{h+\nu_p(d)+1}).
\]
The parenthesized integer is \(1\pmod p\). The leading term has exact valuation \(h+\nu_p(d)\), proving both displayed isometries (the case \(s<t\) follows by symmetry).

For \(k\le h\), all terms are \(1\pmod{p^k}\). For \(k>h\), each parity branch as the input \(t\) runs over \(0,\ldots,p^{k-h}-1\) is a bijection onto the \(p^{k-h}\) residues of \(1+p^h\mathbb Z/p^k\mathbb Z\). Hence the period \(2p^{k-h}\) gives exactly two occurrences per allowed residue. It is a scalar period because \(C^{p^{k-h}}\equiv I\pmod{p^k}\). No smaller even scalar period is possible by the isometry. Nor can an odd period \(2u+1\) occur: modulo \(p^{h+1}\), the binomial expansion gives \(x_{2t}\equiv x_{2t+1}\equiv1+ta\); matching \(x_{2u+1}\) with \(x_0\) would require \(p\mid u\), whereas matching \(x_{2u+2}\) with \(x_1\) would require \(p\mid(u+1)\). This proves the least period.

The isometries show that each parity subsequence is dense in \(1+p^h\mathbb Z_p\), proving the value closure. Because the ball is a multiplicative subgroup of \(\mathbb Z_p^\times\), every quotient lies in it. Since \(x_0=1\), the value set itself belongs to the quotient set, so the quotient closure equals the same ball.

**3. The exceptional binary lift.** Suppose \(a=2u\) with \(u\) odd. Direct expansion gives
\[
M^4=I+4B,\qquad B=u^2I+u(1+2u^2)M.
\]
Modulo two, \(M\) is a coordinate swap, \(B\equiv I+M\), and hence \(B^2\equiv0\pmod2\) and \(BM^rv\equiv0\pmod2\) for every nonnegative integer \(r\). The following four small congruences are obtained from the recurrence modulo sixteen:

| \(a\pmod8\) | \(r\) | \(x_r\pmod8\) | \(x_{r+4}-x_r\pmod{16}\) |
|---|---:|---:|---:|
| 2 | 1 | 1 | 8 |
| 2 | 3 | 7 | 8 |
| 6 | 0 | 1 | 8 |
| 6 | 2 | 7 | 8 |

Fix either of the two listed \(r\)-values for the given parameter. For \(d\ge1\), write
\[
(M^4)^d-I=4dB+\sum_{j=2}^d\binom dj(4B)^j.
\]
Since \(B^2\) is entrywise even, \(\nu_2((4B)^j)\ge2j+1\) for \(j\ge2\). Combining this with \(\nu_2(\binom dj)\ge\nu_2(d)-\nu_2(j)\), all higher terms are divisible by \(2^{\nu_2(d)+4}\). Meanwhile \(eBM^rv\) has valuation exactly one, by the table, and \(M^{4t}\equiv I\pmod4\) does not change that leading valuation because \(BM^rv\) is an even vector. Therefore, for distinct \(s,t\ge0\),
\[
\nu_2(x_{4s+r}-x_{4t+r})=3+\nu_2(s-t).
\]
Thus each selected residue branch is an exact \(8\)-scaled isometry. Its image modulo \(2^k\) for \(k\ge3\) is the complete ball of residues centered at \(x_r\pmod8\). These two branches give \(1+8\mathbb Z_2\) and \(7+8\mathbb Z_2\) in the value closure.

**4. Exact binary quotient closure.** Every term is odd, so all quotients lie in \(\mathbb Z_2^\times\). We have a term \(c\) congruent to \(3\pmod8\): take \(c=x_2=a+1\) when \(a\equiv2\pmod8\), and \(c=x_3=a^2+a+1\) when \(a\equiv6\pmod8\). Since the value closure contains both \(1+8\mathbb Z_2\) and \(7+8\mathbb Z_2\), and since taking ratios by a fixed nonzero term is continuous, the quotient closure contains four entire balls:
\[
1+8\mathbb Z_2,\qquad7+8\mathbb Z_2,\qquad
c(1+8\mathbb Z_2)^{-1}=3+8\mathbb Z_2,\qquad
c(7+8\mathbb Z_2)^{-1}=5+8\mathbb Z_2.
\]
Their disjoint union is \(\mathbb Z_2^\times\), proving equality. There are no missing dyadic unit classes; no nonunits can appear as limits because the unit group is closed in \(\mathbb Q_2\).

## Verification
The standalone `check.py` independently enumerates complete recurrence state periods and exact value frequencies for \(p\in\{2,3,5,7,11\}\), valuations \(h\in\{1,2,3\}\) where applicable, signed coefficients, and powers \(p^k\le10000\). It also tests the two exceptional binary value balls and the entire quotient unit group modulo \(2^k\) for \(3\le k\le10\). All **470** finite tests passed, directly involving **38,068** recurrence positions. The code checks the stated formulas rather than supplying a proof for unbounded \(k\); the preceding valuation arguments supply the infinite proof.

## Relationship to prior work
Antony and Barman's first public version dated 14 July 2022 (2023 journal publication), Theorem 1.10 and Example 1.11, already establish **non-density in \(\mathbb Q_p\)** for general unit-seeded recurrence families when the nonlast coefficients are divisible by \(p\). The present family is an order-two specialization of that hypothesis, so that non-density statement is explicitly not new; the added claims are the exact all-power value frequencies, the local isometry, and the full *proper* quotient-set closure, including the exceptional binary unit-group result. Their 2024 study concerns principally globally split integer-root characteristic polynomials and dense quotient sets with zero initial values, not the claimed unit-seeded local image theorem. Garcia, Hong, Luca, Pinsker, Sanna, Schechter and Starr (2017), Section 5, study first-kind seeds \((0,1)\) and second-kind companion seeds \((2,a)\), not the \((1,1)\) seed here. Carlip and Jacobson (1996) give residue distributions in a first-kind sequence with seeds \(0,1\) and an odd leading coefficient; that theorem does not cover our family. Related published work on odd-parameter Lucas companions gives a two-adic quotient closure on five valuation shells, but it uses a different seed, an odd coefficient, and a different valuation regime; a published repeated-root period result concerns primes at least five with repeated characteristic roots modulo \(p\), whereas the present characteristic polynomial is \(T^2-aT-1\) and reduces to \(T^2-1\) for odd \(p\mid a\). Neither implication yields the stated all-prime fibers and dyadic transition.

## Limitations
The theorem does not classify behavior at primes not dividing the recurrence coefficient or the full dyadic value distribution in the exceptional case. The exact closure is \(p\)-adic, not a claim of real density. The general non-density conclusion is prior art; no priority is asserted for it. The local isometry argument uses classical binomial and matrix techniques, so an equivalent formula may be implicit in older recurrence-residue literature; independent historical priority review remains warranted. Computations corroborate, but cannot independently certify, the universal claim.

## References
1. D. Antony and R. Barman, *p-Adic quotient sets: linear recurrence sequences*, arXiv:2207.07084v1, first posted 14 July 2022; *Bulletin of the Australian Mathematical Society* **108** (2023), 19–28, Theorem 1.10 and Example 1.11. https://arxiv.org/abs/2207.07084 ; https://doi.org/10.1017/S0004972722001563
2. S. R. Garcia, Y. X. Hong, F. Luca, E. Pinsker, C. Sanna, E. Schechter, A. Starr, *p-adic quotient sets*, *Acta Arithmetica* **179** (2017), 163–184, Section 5. https://doi.org/10.4064/aa8579-4-2017
3. D. Antony and R. Barman, *p-Adic quotient sets: linear recurrence sequences with reducible characteristic polynomials*, arXiv:2408.06949v1, first posted 13 August 2024. https://arxiv.org/abs/2408.06949
4. *Exact two-adic quotient-set closure for every odd-parameter Lucas companion*, published mathematical record, especially its distinct initial values and odd-parameter scope. (publicly indexed mathematical finding)
5. *Maximal ramified prime-power periods for quadratic recurrences*, published mathematical record, especially its repeated-characteristic-root hypothesis. (publicly indexed mathematical finding)
6. W. Carlip and E. Jacobson, *On the stability of certain Lucas sequences modulo powers of 2*, *Fibonacci Quarterly* **34** (1996), 298–305, Theorem 1.1. https://www.fq.math.ca/Scanned/34-4/carlip.pdf
