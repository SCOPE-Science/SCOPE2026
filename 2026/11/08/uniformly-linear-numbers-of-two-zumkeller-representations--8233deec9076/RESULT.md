# Uniformly linear numbers of two-Zumkeller representations

## Finding

Let \(Z\) be the positive Zumkeller numbers: a positive integer belongs to \(Z\) precisely when its set of positive divisors can be divided into two disjoint subsets having equal sums. For every positive integer \(n\), write
\[
R(n)=\#\{(a,b)\in Z\times Z:a+b=n\}.
\]
The pairs are **ordered**. There is a positive absolute constant \(c\) such that \(R(n)\ge cn\) for all sufficiently large \(n\). More explicitly, with \(M=94185\),
\[
\begin{aligned}
R(n)&\ge\frac{n-92}{18\cdot80^2} &&(n\ge90\text{ even}),\\
R(n)&\ge\frac{10(n-M)}{11\cdot88M^2}-1 &&(n>M\text{ odd}).
\end{aligned}
\]
Consequently
\[
\liminf_{n\to\infty}\frac{R(n)}n\ge\frac{10}{11\cdot88\cdot94185^2}
=1.164558094710488\ldots\times10^{-12}>0.
\]
Since trivially \(R(n)\le n-1\), this establishes the sharp growth **order** \(R(n)=\Theta(n)\); it does not assert existence of a limiting normalized representation count.

## Assumptions and scope

All variables are ordinary positive integers. Divisors include the integer itself. A decomposition into two Zumkeller numbers may repeat a summand; different ordered pairs are counted separately. The constants arise from the published residue-pair construction of Somu, Kukla and Tran (2023), reproduced and exhaustively checked in `check.py`. We use the earliest arXiv publication of that paper, 22 October 2023, as the motivating source.

## Proof

**Coprime-multiplier lemma.** If \(s\in Z\) and \(\gcd(s,q)=1\), then \(sq\in Z\). Indeed, each divisor of \(sq\) is uniquely a product of a divisor of \(s\) and a divisor of \(q\). Multiply each part of an equal-sum divisor partition of \(s\) by the full divisor set of \(q\); both resulting sums are multiplied by \(\sigma(q)\). In particular,
\[
s(1+Ls t)\in Z\quad(t\ge0)
\]
for any positive integers \(L\) and \(s\in Z\).

**Two uniform Zumkeller progressions.** For every integer \(k\ge1\), the number \(3\cdot2^k\) is Zumkeller. Its divisor sum is \(4(2^{k+1}-1)\), and the amount required in addition to the divisor \(3\cdot2^k\) to reach half the total is \(2^k-2\). That nonnegative integer is a sum of distinct powers of two smaller than \(2^k\), all proper divisors. Hence, by the coprime-multiplier lemma, every positive integer \(m\equiv6\) or \(12\pmod{18}\) is Zumkeller: such integers have the form \(3\cdot2^kq\), where \(k\ge1\) and \(\gcd(q,6)=1\).

Similarly \(11\cdot2^k\in Z\) for every \(k\ge3\), since its divisor sum is \(12(2^{k+1}-1)\), and the gap from the divisor \(11\cdot2^k\) to half this total is \(2^k-6\), a sum of distinct powers of two smaller than \(2^k\). Consequently
\[
88m\in Z\qquad(m\ge1,\ 11\nmid m),
\]
because one factors \(m=2^e q\) with \(\gcd(q,22)=1\).

**Even target integers.** The six integers \(6,12,20,28,40,80\) are Zumkeller; `check.py` verifies each against its full divisor set. Every even residue modulo \(18\) admits a choice of a fixed seed \(a\) from that set and \(\beta\in\{6,12\}\), such that \(a+\beta\) has the designated residue. The table is

| \(n\bmod18\) | \(a\) | \(\beta\) |
|---:|---:|---:|
| 0 | 12 | 6 |
| 2 | 80 | 12 |
| 4 | 28 | 12 |
| 6 | 12 | 12 |
| 8 | 20 | 6 |
| 10 | 40 | 6 |
| 12 | 6 | 6 |
| 14 | 20 | 12 |
| 16 | 40 | 12 |

For even \(n\ge90\), put \(m=(n-a-\beta)/18\ge0\). For every integer \(0\le t\le\lfloor m/a^2\rfloor\), the ordered pair
\[
\bigl(a(1+18at),\ 18(m-a^2t)+\beta\bigr)
\]
adds to \(n\), and both entries are Zumkeller. The pairs are distinct since the first entry strictly increases. Thus
\[
R(n)\ge\left\lfloor\frac{m}{a^2}\right\rfloor+1\ge\frac{n-92}{18\cdot80^2}.
\]

**Odd target integers.** A finite residue-pair certificate from Somu--Kukla--Tran (2023, Table 1), verified by exact arithmetic in `check.py`, supplies for each of the \(44\) odd classes \(r\pmod{88}\) two positive Zumkeller integers \(u_r,v_r\le M\), both congruent to \(r\), for which
\[
11\nmid\frac{v_r-u_r}{88}.
\]
The checker stores all \(88\) integers and verifies both membership and these congruences by exact arithmetic, with membership established by an exhaustive subset-sum recurrence over **all proper divisors** of each seed.

Fix odd \(n>M\). Select its residue class and corresponding seeds. Since their two quotients \((n-u_r)/88\) and \((n-v_r)/88\) differ by a nonzero residue modulo \(11\), at least one seed \(s\le M\) satisfies
\[
m=\frac{n-s}{88}\ge1,\qquad11\nmid m.
\]
For every integer \(t\) with \(0\le t\le\lfloor(m-1)/s^2\rfloor\), consider
\[
\bigl(s(1+88st),\ 88(m-s^2t)\bigr).
\]
The first member is Zumkeller by coprime multiplication; the second is Zumkeller whenever \(11\nmid(m-s^2t)\). If \(11\mid s\), this holds for every such \(t\); otherwise at most one integer out of every \(11\) consecutive values of \(t\) is excluded. With \(T=\lceil m/s^2\rceil\), there are therefore at least
\[
T-\left\lceil\frac{T}{11}\right\rceil\ge\frac{10T}{11}-1
\]
distinct ordered representations. Since \(T\ge(n-M)/(88M^2)\), the stated odd lower bound follows. The even and odd bounds together give the displayed uniform positive lower limit. This completes the proof.

## Verification

Run `python3 check.py` with the standard Python library. Its recorded stdout is `check_output.txt`. The checker lists the 44 source pairs (88 seeds), generates complete divisor sets independently, and uses a bitset dynamic program implementing all attainable subset sums of proper divisors. It checks all relevant residue conditions and the six even seeds, then tests both endpoint constructions on 964 even and 2,951 odd sample integers. Exhaustive finite seed certification plus the symbolic argument above proves the unlimited bound; finite sample tests alone are not extrapolated to infinity.

## Relationship to prior work

Somu, Kukla and Tran (arXiv:2310.14149, 2023, Section 4 and Table 1) prove that all integers above \(94185\) are sums of two Zumkeller numbers. The present result changes the quantified conclusion: **each sufficiently large integer has linearly many ordered representations**, not merely at least one. Their source provides the finite residue-pair seeds; the repeated coprime-multiplier construction and the quantitative counting are the additional argument. OEIS A083207 lists Zumkeller numbers, and A368007 records integers lacking a two-Zumkeller representation, rather than the uniform representation-count growth law. These sources do not state the linear lower bound. Unindexed prior equivalent work cannot be excluded by database searches alone.

## Limitations

The normalized count \(R(n)/n\) need not be known to converge; only its positive uniform lower limit and a trivial finite upper bound are shown. The numerical constant is extremely small and is not claimed optimal. The 44-pair finite certificate is required for the odd-target bound, and each of its entries is recomputed from its complete divisor set by the included checker.

## References

1. S. T. Somu, A. Kukla and D. V. K. Tran, *Some Results on Zumkeller Numbers*, arXiv:2310.14149v1 (22 October 2023), revised arXiv:2310.14149v2 (27 November 2023), especially Table 1 and Section 4. https://arxiv.org/abs/2310.14149
2. OEIS A083207, *Zumkeller or integer-perfect numbers*. https://oeis.org/A083207
3. OEIS A368007, *Positive integers which cannot be written as a sum of two Zumkeller numbers*. https://oeis.org/A368007
