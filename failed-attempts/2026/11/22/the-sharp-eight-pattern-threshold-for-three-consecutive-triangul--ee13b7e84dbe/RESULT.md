# The sharp eight-pattern threshold for three consecutive triangular Legendre symbols

## Finding
For any prime \(p\ge5\), write \(\chi_p\) for the Legendre symbol on \(\mathbb F_p\), extended by \(\chi_p(0)=0\), and let \(T_n=n(n+1)/2\). For each sign word \((a,b,c)\in\{-1,1\}^3\), put
\[
N_p(a,b,c)=\#\{n\in\mathbb F_p:(\chi_p(T_n),\chi_p(T_{n+1}),\chi_p(T_{n+2}))=(a,b,c)\}.
\]
Define \(s=\chi_p(2)\), \(t=\chi_p(3)\), \(u=\chi_p(-1)\) and \(E_p=\sum_{n\in\mathbb F_p}\chi_p(n(n+1)(n+2)(n+3))\). Then *all eight frequencies* are given exactly by
\[
8N_p(a,b,c)=p-4+(a+c)(-s-1-t)+b(-s-2)+b(a+c)(-1-u-t)+acE_p+abc(-s-2u).
\]
In particular, every sign word occurs for every prime \(p\ge19\). This universal threshold is sharp: at each of the primes \(5,7,11,13,17\), at least one word fails to occur. The quartic moment is the Frobenius trace of a genus-one curve and satisfies \(\lvert E_p+1\rvert\le2\sqrt p\). These are *index-pattern* frequencies, not frequencies of triangular residue values.

## Assumptions and scope
All quantifiers above range over odd prime fields of order at least five; \(n\) is a residue class, and zero Legendre values are excluded from every \(N_p\). The four exceptional zero-index classes \(n=0,-1,-2,-3\) are pairwise distinct in this range. A 'complete pattern' means all eight ordered sign triples have strictly positive multiplicity. The theorem makes no statement about the first occurrence in ordinary positive integers, polynomial values at composite moduli, or longer patterns.

## Proof
Put \(A(n)=\chi_p(T_n)\), \(B(n)=\chi_p(T_{n+1})\), and \(C(n)=\chi_p(T_{n+2})\), and let \(U=\mathbb F_p\setminus\{0,-1,-2,-3\}\). For \(n\in U\), the desired indicator is \((1+aA(n))(1+bB(n))(1+cC(n))/8\). We evaluate its eight moment sums over \(U\).

The zeroth moment is \(p-4\). As \(\chi_p(T_n)=s\chi_p(n(n+1))\) and every translated, monic, separable quadratic has complete character sum \(-1\), the three single moments are
\[
\sum_U A=\sum_U C=-s-1-t,\qquad \sum_U B=-s-2.
\]
For example, the excluded nonzero values of \(A\) at \(n=-2,-3\) are \(1,t\); those of \(B\) at \(n=-3,0\) are both one. The products \(AB\) and \(BC\) are \(\chi_p(n(n+2))\) and \(\chi_p((n+1)(n+3))\), except that an omitted square factor enforces a zero at its central root. Correcting these excluded roots and the endpoint gives
\[
\sum_U AB=\sum_U BC=-1-u-t.
\]
The product \(AC\) is \(\chi_p(n(n+1)(n+2)(n+3))\), which already vanishes at all four excluded indices, so \(\sum_U AC=E_p\). Finally, the triple product equals \(s\chi_p(n(n+3))\) except at \(n=-1,-2\), where both have value zero; the values of the latter quadratic at these two points are both \(\chi_p(-2)=us\). Consequently,
\[
\sum_U ABC=-s-2u.
\]
Expanding the indicator and inserting the seven moments establishes the exact integer identity for every sign word; in particular, the right side is divisible by eight.

The monic quartic \(y^2=x(x+1)(x+2)(x+3)\) has four distinct branch points and two rational points at infinity, hence defines a smooth genus-one curve over \(\mathbb F_p\). Its total point count is \(p+E_p+2\), so Hasse's inequality implies \(\lvert E_p+1\rvert\le2\sqrt p\). Bounding the other four signed corrections by \(6,3,6,3\), respectively, gives
\[
8N_p(a,b,c)\ge p-23-2\sqrt p>0\qquad(p\ge37).
\]
The only primes \(5\le p<37\) are \(5,7,11,13,17,19,23,29,31\). Compute their signs by Euler's criterion \(\chi_p(d)\equiv d^{(p-1)/2}\pmod p\), with the result interpreted as \(0,1,-1\). Exhaustive enumeration of the at most \(p-4\) admissible indices gives the following minimum counts among the eight sign words:

| \(p\) | 5 | 7 | 11 | 13 | 17 | 19 | 23 | 29 | 31 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(\min N_p\) | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 2 | 2 |

The independent exact code `checker.py`, included with this result, reproduces the table and compares the direct enumeration with the closed formula across every prime from five through 997. For every prime at least 19 the minimum is positive, and for all smaller eligible primes it is zero. This closes the finite case and proves both the threshold and its sharpness.

## Verification
Run `python3 checker.py` using Python 3.9 or later; no third-party dependencies are needed. The script checks all eight sign counts by two independent routes (direct evaluation and the evaluated-moment formula), checks that the quartic moment satisfies Hasse, and verifies the complete small-prime threshold certificate. The proof above establishes the theorem for arbitrary prime size; the finite program independently tests the arithmetic and exactly covers the only cases not decided by the universal inequality.

## Relationship to prior work
Wang and Fang (2023) investigate runs of ordinary quadratic residues and nonresidues with constant additive step, including four- and five-position bounds. Wang and Li (2023) treat consecutive ordinary quadratic-residue triples. Their input variables are linear translates, not the three successive quadratic polynomials \(T_n,T_{n+1},T_{n+2}\). Conrad's note gives the standard character-indicator expansion and a general \(O(\sqrt p)\) estimate for ordinary consecutive *linear* arguments. The expansion step itself is not claimed as new; the specifically simplified eight-count identity, its genus-one term, and the proven sharp triangular-pattern universal cutoff are the contribution here. Ulness (2022) studies triangular residues modulo composite integers and residue saturation, not their consecutive-index Legendre sign words.

## Limitations
The bound \(p-23-2\sqrt p\) is deliberately conservative; it proves positivity only from prime 37 onwards and relies on an exact finite certificate below. The exact formula retains a quartic Frobenius trace, which can oscillate with \(p\). General ordinary consecutive-character expansions may subsume the *method* but do not alone establish the sharp triangular cutoff. A more specialized unindexed study of successive triangular quadratic-character patterns could contain an equivalent result; priority is not independently established. Independent peer verification of priority is outside the scope of this result.

## References
1. X. Wang and H. Fang, 'The Distribution Properties of Consecutive Quadratic Residue Sequences', *Journal of Mathematics*, 2023, DOI: https://doi.org/10.1155/2023/5253261 (public 2023-10-03).
2. X. Wang and A. H. Li, 'Distribution Properties and Applications of Consecutive Quadratic Residues', *Acta Mathematica Sinica, Chinese Series* 66 (2023), 389–398, DOI: https://doi.org/10.12386/A20210160 (public 2023-03-15).
3. K. Conrad, 'Quadratic Residue Patterns Modulo a Prime', https://kconrad.math.uconn.edu/blurbs/ugradnumthy/QuadraticResiduePatterns.pdf (date not verified; methodological background only).
4. D. Ulness, 'Structure of Triangular Numbers Modulo \(m\)', *Mathematics and Computational Applications* 2022, https://www.mdpi.com/2673-9909/2/3/20 (public 2022-07-01).
