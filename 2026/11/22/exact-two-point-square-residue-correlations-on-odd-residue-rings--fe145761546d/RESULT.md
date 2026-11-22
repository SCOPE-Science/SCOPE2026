# Exact two-point square-residue correlations on odd residue rings and a prime-power reversal

## Finding
Let \(Q(n)=\{y^2\bmod n:y\in\mathbb Z\}\) include zero and nonunit square classes. The *ordered cyclic two-point count* is
\[
A_n(h)=\#\{x\in Q(n):x+h\in Q(n)\}\quad(h\in\mathbb Z/n\mathbb Z).
\]
For every odd integer \(n\ge3\), the following gives \(A_n(h)\) for **every shift**, including shifts divisible by primes of \(n\), without summing over residues modulo \(n\).

Fix an odd prime \(p\), integer \(m\ge1\), and write \(\chi=\left(\frac{\cdot}{p}\right)\), extended by \(\chi(0)=0\). For \(0\le a\le m\), define the exact count
\[
S_{p,m}(a)=1+\frac{p-1}{2}\sum_{\substack{j\ge0\\a\le2j<m}}p^{m-2j-1};
\]
empty sums are zero. Define also
\[
U_{p,m}(t)=\frac{p-1}{2}\sum_{\substack{j\ge0\\2j<t}}p^{m-2j-1},\qquad 0\le t<m.
\]
For \(h\equiv0\pmod{p^m}\), the answer is \(A_{p^m}(h)=S_{p,m}(0)\). Otherwise, let \(t\in\{0,\ldots,m-1\}\) be the exact \(p\)-adic valuation of \(h\), and \(u\equiv h/p^t\pmod p\) be a nonzero unit.

If \(t\) is odd,
\[
\boxed{A_{p^m}(h)=U_{p,m}(t).}
\]
If \(t\) is even, put \(N_p(u)=(p-3-\chi(u)-\chi(-u))/4\). Then
\[
\boxed{\begin{aligned}
A_{p^m}(h)={}&U_{p,m}(t)+p^{m-t-1}N_p(u)\\
&+\mathbf1_{\chi(-u)=1}S_{p,m-t}(1)
+\mathbf1_{\chi(u)=1}S_{p,m}(t+1).
\end{aligned}}
\]
All terms are integers; \(N_p(u)\) is a nonnegative integer by its character-count interpretation. For an arbitrary odd modulus with prime-power factorization \(n=\prod_{i=1}^r p_i^{m_i}\), the complete two-point distribution is
\[
\boxed{A_n(h)=\prod_{i=1}^r A_{p_i^{m_i}}(h).}
\]

A structural consequence concerns *unit shifts* \(p\nmid h\). If \(p\equiv1\pmod4\), they fall into just two levels:
\[
\boxed{A_{p^m}(h)=\begin{cases}
\dfrac{p-5}{4}p^{m-1}+2S_{p,m}(1),&\chi(h)=1,\\[4pt]
\dfrac{p-1}{4}p^{m-1},&\chi(h)=-1.
\end{cases}}
\]
Their difference (square-shift minus nonsquare-shift) is exactly \(2S_{p,m}(1)-p^{m-1}\): it is \(+1\) at exponent \(m=1\), and **strictly negative at every exponent \(m\ge2\)**. If \(p\equiv3\pmod4\), the entire unit-shift spectrum instead collapses to one value,
\[
\boxed{A_{p^m}(h)=\frac{p-3}{4}p^{m-1}+S_{p,m}(1)\quad(p\nmid h).}
\]
For \(p=5\), the two levels at exponents \(m=1,2,3,4\), listed as (square-shift, nonsquare-shift), are \((2,1),(2,5),(6,25),(22,125)\).

## Assumptions and scope
The modulus \(n\) is any odd integer at least three. A square residue includes zero and every nonunit square, not merely a quadratic unit. Shift parameters are residue classes, and both occurrences are counted as residue classes rather than representations by roots. For the local formulas, \(p\) is an odd prime and \(m\ge1\). A \(p\)-adic valuation \(\nu_p(h)\) of a nonzero class modulo \(p^m\) means the unique integer \(t<m\) such that \(p^t\mid h\) and \(p^{t+1}\nmid h\); its unit part modulo \(p\) is independent of the representative. An empty sum is zero. The result makes no statement for even moduli or for higher-power residue sets.

## Proof
**1. Square layers.** The nonzero square classes modulo \(p^m\) have even \(p\)-adic valuations \(2j<m\), and the unit part of such a class must be a square modulo \(p\). Conversely, every such unit lifts to a square modulo each power of \(p\), by Hensel lifting because \(p\) is odd. For a fixed \(j\), the number of distinct classes of valuation \(2j\) is \((p-1)p^{m-2j-1}/2\). Zero contributes one class with valuation at least every \(a\le m\). Hence \(S_{p,m}(a)\) counts precisely the square classes whose valuation is at least \(a\), and \(U_{p,m}(t)\) counts precisely those whose valuation is smaller than \(t\).

**2. Partition of a shifted pair.** Suppose \(h=p^tu\not\equiv0\pmod{p^m}\), with \(u\) a unit. Partition the *square* values of \(x\) into \(\nu_p(x)<t\), \(\nu_p(x)=t\), and \(\nu_p(x)>t\), treating zero as having valuation \(m\) for this purpose. If \(\nu_p(x)<t\), adding \(h\) does not change the exact valuation or first nonzero digit, so \(x+h\) is also a square. This contributes exactly \(U_{p,m}(t)\).

If \(\nu_p(x)>t\), then \(x+h\) has valuation exactly \(t\) and unit leading digit \(u\). Thus this branch contributes \(S_{p,m}(t+1)\) if \(t\) is even and \(\chi(u)=1\), and zero otherwise. If \(\nu_p(x)=t\), it can only occur when \(t\) is even. Write \(x=p^tz\) with \(z\) a unit square modulo \(p^{m-t}\). The condition that \(x+h\) is also square is that \(z+u\) is a square modulo \(p^{m-t}\).

The case \(z\not\equiv0,-u\pmod p\) has \(N_p(u)\) choices for \(z\pmod p\) such that both \(z\) and \(z+u\) are nonzero squares. Each choice has precisely \(p^{m-t-1}\) lifts, all still satisfying both square-unit conditions. The remaining case \(z\equiv-u\pmod p\) exists only when \(\chi(-u)=1\). In that case the map \(z\mapsto z+u\) bijects the admissible lifts with all the *nonunit square classes* modulo \(p^{m-t}\), counted by \(S_{p,m-t}(1)\). Summing all disjoint branches proves both parity cases.

**3. Elementary character count.** For \(u\not\equiv0\pmod p\),
\[
4N_p(u)=\sum_{z\not\equiv0,-u\pmod p}(1+\chi(z))(1+\chi(z+u))
=p-2-\chi(u)-\chi(-u)+\sum_{z\bmod p}\chi(z(z+u)).
\]
The last sum is \(-1\). Indeed completing the square transforms its argument into a nonzero scalar multiple of \(v^2-u^2\), while the elementary identity \(\sum_{v\bmod p}\chi(v^2-u^2)=-1\) follows by counting the \(p-1\) pairs \((v,w)\) with \((v-w)(v+w)=u^2\). This establishes \(N_p(u)=(p-3-\chi(u)-\chi(-u))/4\), including its integrality. The zero-shift case is the one-point count \(S_{p,m}(0)\).

**4. The unit-shift dichotomy and reversal.** Set \(t=0\) in the formula. When \(p\equiv3\pmod4\), \(\chi(-u)=-\chi(u)\), so the character-count term is constant and exactly one of the two valuation-tail indicators is one. When \(p\equiv1\pmod4\), \(\chi(-u)=\chi(u)\), so the two displayed levels follow by substitution. At \(m=1\), \(S_{p,1}(1)=1\), making their difference \(+1\). For \(m\ge2\), the nonunit-square geometric series yields
\[
2S_{p,m}(1)\le 2+\frac{p^{m-1}}{p+1}<p^{m-1},\qquad p\ge5.
\]
The strict last inequality holds already at the smallest case \(p=5,m=2\), and its margin increases with \(p\) and \(m\). Hence the difference is negative for every higher prime-power exponent.

**5. Odd composite moduli.** Under the Chinese remainder correspondence \(\mathbb Z/n\mathbb Z\cong\prod_i\mathbb Z/p_i^{m_i}\mathbb Z\), a class is a square exactly when each component is a square. Both shifted membership conditions therefore factor independently. Multiplying local counts gives the final formula.

## Verification
A standalone Python 3 checker named `check_square_corr.py` is included. It builds square *sets* independently from the explicit valuation formula, compares every cyclic shift for small prime powers, selected shifts for larger prime powers, and every shift for selected odd composite moduli. It also checks the sign reversal for primes congruent to one modulo four and several exponents. On execution, the checker reported `PASS; exact shift comparisons and phase-inequality checks: 5207` and the prime-five example in the finding. These finite checks corroborate only the specified instances; the proof above supplies the infinite quantifiers.

## Relationship to prior work
Samer Seraj's 2022 and 2023 papers count the **number of distinct power residues** at prime powers; these are the one-point values \(A_{p^m}(0)\), not the complete shifted two-point function. Classical finite-field character sums and Paley difference-set results give the \(m=1\) pair counts, including the well-known two-level distribution for nonzero square classes. Huczynska and Johnson (2024) use this prime-field property in partial difference-set constructions. The present statement includes nonunit square classes and all valuation strata at arbitrary odd prime-power exponents, where the contrast between square and nonsquare unit shifts reverses its sign. The general formula also covers arbitrary odd composite moduli by the Chinese remainder theorem. The finite-field formulas and one-point counts are background, not claimed here as new.

## Limitations
Only odd moduli and quadratic (second-power) residues are covered. The claim neither establishes a new finite-field quadratic-character identity nor implies a general formula for the analogous higher correlations of three or more shifts. Although full statements and relevant sections of the listed primary sources were examined, an equivalent formulation may exist in older difference-set or arithmetic-correlation literature, including Fourier descriptions that encode the same kernel without naming these parameters. A particularly relevant published Fourier-algebra result for complete square sets was available at indexed-summary level but not in accessible full text; the possibility of an implicit equivalent there remains an originality risk. There has been no independent mathematical audit.

## References
1. S. Seraj, *Resolution of Mathar's Conjectures on Counting Power Residues*, INTEGERS 23 (2023), #A62, published 2023-08-25; https://math.colgate.edu/~integers/x62/x62.pdf .
2. S. Seraj, *Counting general power residues*, Notes on Number Theory and Discrete Mathematics 28 (2022), 730–743, first online 2022-11-07; https://nntdm.net/volume-28-2022/number-4/730-743/ .
3. S. Huczynska and L. Johnson, *New constructions for disjoint partial difference families and external partial difference families*, Journal of Combinatorial Designs 32 (2024), 190–213, first published 2024-02-04; https://onlinelibrary.wiley.com/doi/full/10.1002/jcd.21930 .
4. W. D. Stangl, *Counting Squares in \(\mathbb Z_n\)*, Mathematics Magazine 69 (1996), 285–289 (bibliographic information in Seraj's references).
