# Reflection complexity of the triangular-marker binary word

## Finding

Let \(\mathbf t=1\,0^1 1\,0^2 1\,0^3 1\cdots\), with one at the zero-based positions \(j(j+1)/2-1\) for integers \(j\ge1\). Define \(\mathcal L_n\) as the set of distinct length-\(n\) contiguous factors of \(\mathbf t\). Its **reflection complexity** \(R(n)\) counts equivalence classes in \(\mathcal L_n\) where two words are equivalent if one is the reversal of the other. The empty factor is included for \(n=0\).

For every integer \(n\ge0\),
\[
\boxed{\sum_{n\ge0}R(n)z^n=\frac{1+z-z^2+z^5}{(1-z)^3(1+z)(1+z+z^2)}.}
\]
Equivalently, for every \(m\ge0\) and \(s\in\{0,1,2,3,4,5\}\),
\[
\boxed{R(6m+s)=6m^2+2(s+1)m+c_s,\qquad(c_0,c_1,c_2,c_3,c_4,c_5)=(1,2,2,4,5,7).}
\]
The quasi-polynomial has least period six. If \(P(n)=|\mathcal L_n|\) denotes ordinary factor complexity, then
\[
P(n)=\left\lfloor\frac{(n+1)^2}{4}\right\rfloor+1
\quad(n\ge0),\qquad
R(n)\sim\frac{n^2}{6},\quad \frac{R(n)}{P(n)}\longrightarrow\frac23.
\]
The auxiliary ordinary-factor formula is included to derive the new reversal-quotient enumeration; it is not presented as a new general factor-complexity theorem.

## Assumptions and scope

All words are over the fixed alphabet \(\{0,1\}\). Factor means **contiguous** factor, not scattered subsequence. The sequence is one-sided, has no added terminal symbol, and contains a \(1\) at positions \(0,2,5,9,14,\ldots\). Each factor is counted once irrespective of multiplicity; if both a nonpalindromic factor and its reversal occur, they form one class; if only one occurs, that factor forms a singleton class. The claim holds for all lengths \(n\ge0\), without a finite cutoff.

## Proof

**1. Classification of factors.** Exactly one \(0^n\) occurs for every \(n\ge1\). Every factor containing exactly one \(1\) has the unique form \(0^a1 0^b\) with \(a,b\ge0\), and every such word occurs since arbitrarily long zero gaps appear on both sides of sufficiently late ones. Thus there are \(n\) distinct one-\(1\) factors at length \(n\).

A factor with exactly two ones has the unique form
\[
0^a1 0^j1 0^b,\qquad j\ge1,\quad0\le a\le j-1,\quad0\le b\le j+1.
\]
Indeed, the gap of \(j\) zeroes between the two selected consecutive ones is preceded by the gap of \(j-1\) zeroes (where the initial gap is zero) and followed by the gap of \(j+1\) zeroes. No other occurrence of the two-one pattern can circumvent these exact inequalities, because every complete gap length occurs exactly once.

A factor containing three or more ones is determined uniquely by the number \(a\) of initial zeroes, and the first internal gap length \(j\). The next internal gap has length \(j+1\). Conversely, the possible pairs are exactly
\[
j\ge1,\qquad0\le a\le j-1,\qquad n\ge a+2j+4.
\]
For each such pair, the required length-\(n\) factor is the unique prefix of the infinite tail beginning \(a\) positions before the corresponding marker. To enumerate them, put \(j=a+d\) with \(a\ge0,d\ge1\); the minimum permitted length is \(3a+2d+4\).

**2. Ordinary factor generating function.** Let \(P(z)=\sum_{n\ge0}P(n)z^n\). Partition factors according to their number of ones: zero, one, exactly two, or at least three. The four generating functions (with the empty word separately) give
\[
\begin{aligned}
P(z)={}&1+\frac{z}{1-z}+\frac{z}{(1-z)^2}\\
&+\sum_{j\ge1}\frac{z^{j+2}(1-z^j)(1-z^{j+2})}{(1-z)^2}
+\frac{z^6}{(1-z)(1-z^2)(1-z^3)}.
\end{aligned}
\]
Here the final summand follows from \(n=3a+2d+4+h\), \(a,h\ge0,d\ge1\). Summing the geometric terms and reducing gives
\[
P(z)=1+\frac{z(2-z-z^2+z^3)}{(1-z)^3(1+z)},
\]
whose coefficients are \(P(n)=\lfloor(n+1)^2/4\rfloor+1\), also valid at \(n=0\).

**3. Reversed pairs.** Let \(H(n)\) be the number of unordered pairs \(\{u,u^R\}\) of *distinct* length-\(n\) factors for which both are present. Every such pair reduces the number of reversal classes by exactly one, so \(R(n)=P(n)-H(n)\).

There are no such pairs with zero ones. Among the one-one factors \(0^a10^b\), reversing swaps \(a\) and \(b\). Thus exactly \(\lfloor n/2\rfloor\) nonpalindromic reversal pairs occur.

For exactly two ones, reversing \(0^a1 0^j1 0^b\) swaps \(a,b\) while preserving \(j\). Both words occur if and only if \(a,b\le j-1\). Taking each pair once, write \(b=a+d\), \(a\ge0,d\ge1\). Its length is \(n=a+b+j+2\), and \(j\ge b+1\) is equivalent to
\[
n\ge 3a+2d+3.
\]
Hence the length generating function for two-one reversal pairs is
\[
\sum_{n\ge0}H_2(n)z^n
=\sum_{a\ge0,d\ge1,h\ge0}z^{3a+2d+3+h}
=\frac{z^5}{(1-z)(1-z^2)(1-z^3)}.
\]
There are no reversal pairs with three or more ones: the first two *complete* internal gaps increase from \(j\) to \(j+1\), whereas their order in the reversed factor decreases, which never occurs in \(\mathbf t\). Thus
\[
\sum_{n\ge0}H(n)z^n=
\frac{z^2}{(1-z)(1-z^2)}+
\frac{z^5}{(1-z)(1-z^2)(1-z^3)}.
\]
The first summand has coefficient \(\lfloor n/2\rfloor\).

**4. Closed formula and period.** Subtracting the last displayed series from \(P(z)\) and simplifying yields precisely
\[
\sum_{n\ge0}R(n)z^n=\frac{1+z-z^2+z^5}{(1-z)^3(1+z)(1+z+z^2)}.
\]
Expanding by residue class modulo six gives the six quadratic expressions in the finding. The reduced denominator has both a noncancelled factor \(1+z\) and a noncancelled factor \(1+z+z^2\), so the quasi-polynomial has least period six. The triple pole at \(z=1\) yields \(R(n)\sim n^2/6\). Since \(P(n)\sim n^2/4\), their ratio tends to \(2/3\). This proves the claim for every length.

## Verification

The accompanying dependency-free `verify.py` independently enumerates all factors from a provably sufficient finite prefix, forms reversal-equivalence classes directly, counts nonpalindromic pairs, and compares all values with the stated exact expressions. It checks every \(n=0,1,\ldots,120\) and additionally \(n=150,200,250\), including factors with at least three ones and boundary cases. Running `python3 verify.py` reports 124 tests passed. These finite comparisons support the case analysis but do not replace the all-length proof above.

## Relationship to prior work

Allouche, Campbell, Li, Shallit and Stipulanti introduced reflection complexity and its general relationship to ordinary factor complexity and reflected-factor counts [1]. That identity does not evaluate the joint occurrence of a word and its reversal for the triangular-marker language. Dvořáková and Pelantová establish general eventual-periodicity and minimum-growth criteria [2], while Blažek, Dvořáková and Pelantová extend the measure to antimorphism groups [3]; neither provides the present six-class quadratic formula in the inspected text. The fixed triangular-marker word is recorded independently as a triangular-number indicator [4]. Here the independent enumeration of exactly those nonpalindromic pairs that occur in both directions is the new ingredient. The ordinary factor count is used only as a supporting quantity.

## Limitations

The claim concerns this one exact increasing-gap sequence only; no formula for arbitrary strictly increasing gaps or finite-prefix reflection complexity is asserted. Primary-literature and research-record searches did not identify an equivalent period-six formula, but they cannot exclude unindexed prior work. The proof is self-contained, and the numerical checks are finite. There has been no independent scientific validation.

## References

1. J.-P. Allouche, J. M. Campbell, S. Li, J. Shallit, M. Stipulanti, *The reflection complexity of sequences over finite alphabets*, first public 2024-06-13, arXiv:2406.09302, https://arxiv.org/abs/2406.09302.
2. L. Dvořáková and E. Pelantová, *Reflection on the reflection complexity*, first public 2025-11-15, arXiv:2511.12358, https://arxiv.org/abs/2511.12358.
3. A. Blažek, L. Dvořáková and E. Pelantová, *Generalized reflection complexity*, first public 2026-10-10, arXiv:2610.14637, https://arxiv.org/abs/2610.14637.
4. OEIS A076127, *n-th term is binary string of length the n-th triangular number with ones at triangular-number positions*, https://oeis.org/A076127 (sequence identification, not a reflection-complexity formula).
