# Sharp relative logarithmic growth of semi-Pell and semi-Fibonacci partition counts

## Finding

Let \(f(n)\) be the semi-Fibonacci numbers and \(p(n)\) the semi-Pell numbers, defined for positive integers by \(f(1)=p(1)=1\) and, for integers \(t\ge 1\),
\[
f(2t)=f(t),\quad f(2t+1)=f(2t)+f(2t-1),
\]
\[
p(2t)=p(t),\quad p(2t+1)=2p(2t)+p(2t-1).
\]
Then, **through positive odd integers \(N\to\infty\)**,
\[
\boxed{\lim_{\substack{N\to\infty\\N\ \mathrm{odd}}}\frac{\log(p(N)/f(N))}{\log N}=1.}
\]
Equivalently, \(p(N)/f(N)=N^{1+o(1)}\) along the odd indices. The common leading logarithmic growth is
\[
\log f(N)=\frac{(\log N)^2}{2\log 2}+O(\log N\log\log N),\qquad
\log p(N)=\frac{(\log N)^2}{2\log 2}+O(\log N\log\log N).
\]
The relative exponent is the distinctive assertion, not a claim of an asymptotic constant or equivalence \(p(N)\sim Nf(N)\).

## Assumptions and scope

All logarithms without subscripts are natural logarithms. A **binary partition with odd multiplicities** of \(N\) is an unordered partition into powers of two in which each power that appears has an odd positive multiplicity. Let \(\mathcal B_N\) denote the set of such partitions. If \(\lambda\in\mathcal B_N\), let \(r(\lambda)\) denote its number of occupied power-of-two levels strictly larger than \(1\). For odd \(N\), the power \(1\) must occur, so the total number of occupied levels is \(r(\lambda)+1\).

The two elementary partition interpretations are
\[
f(N)=|\mathcal B_N|,\qquad p(N)=\sum_{\lambda\in\mathcal B_N}2^{r(\lambda)},\quad N\text{ odd}.
\]
They also follow directly by checking their recurrences: for an odd argument \(2t+1\), deleting a single \(1\) when its multiplicity is one leaves an even partition, while deleting two \(1\)'s when the multiplicity is at least three leaves an odd partition. In the weighted interpretation, when the multiplicity of part \(1\) is exactly one, removing this part leaves a nonempty even partition; reinserting it allows two independent choices (marked or unmarked), because it is not the largest part. This explains the factor \(2\) on the even term for \(t\ge1\). For an even argument all parts are even and can be halved. The initial value at \(N=1\) is one in each case. Equivalently, the first count is unmarked odd binary partitions and the second counts their overpartitions with the largest part obligatorily overlined; the other distinct part sizes are independently overlined or not.

If \(N=2^sM\) with \(M\) odd, both functions satisfy \(f(N)=f(M)\) and \(p(N)=p(M)\). Thus the theorem also applies to any integer sequence whose odd parts tend to infinity, when the odd part replaces \(N\) on the right-hand side. It does not assert a comparable exponent in terms of \(N\) along powers of two.

## Proof

**Step 1: the size of the unmarked family.** Take any odd \(N\ge 3\), set \(m=\lfloor\log_2 N\rfloor\), and note \(2^m\le N<2^{m+1}\). An odd binary partition is specified by the multiplicities of its occupied powers \(2^j\) for \(1\le j\le m\), followed by the uniquely determined positive odd multiplicity of \(1\). Ignoring the sum constraint only increases the count; each level \(j\ge1\) has at most \(1+\lfloor N/2^j\rfloor\) possibilities (absent or an odd positive multiplicity). Therefore
\[
f(N)\le \prod_{j=1}^{m}\bigl(1+\lfloor N/2^j\rfloor\bigr)
\le\prod_{j=1}^m2^{m+2-j}=2^{m(m+3)/2}.\tag{1}
\]

For a lower bound let \(m\ge16\), and define
\[
h=m-\lceil2\log_2 m\rceil-4.
\]
Then \(1\le h<m\). For every \(j=1,\ldots,h\), choose independently an odd integer \(u_j\) in the interval
\[
1\le u_j\le \left\lfloor\frac{2^{m-j}}{2m}\right\rfloor.
\]
The number of choices for \(u_j\) is at least \(2^{m-j}/(8m)\). Indeed \(m-j\ge \lceil2\log_2m\rceil+4\), so the upper limit is at least \(8m\), and the number of positive odd integers up to it is at least one quarter of the upper limit. Since
\[
\sum_{j=1}^h u_j2^j\le \frac{h2^m}{2m}<\frac{2^m}{2}\le \frac N2,
\]
there is a unique positive odd remaining multiplicity \(u_0=N-\sum_{j=1}^h u_j2^j\) of the part \(1\). Different choices yield different partitions, giving
\[
f(N)\ge\prod_{j=1}^h\frac{2^{m-j}}{8m}
=2^{hm-h(h+1)/2-h\log_2(8m)}
=2^{m^2/2-O(m\log m)}.\tag{2}
\]
Combining (1) and (2), uniformly for all odd \(N\to\infty\),
\[
\log_2 f(N)=\frac{m^2}{2}+O(m\log m).\tag{3}
\]

**Step 2: almost all partitions occupy almost all possible levels.** Fix \(0<\varepsilon<1\). For a binary partition of odd \(N\), write \(r=r(\lambda)\) for the number of occupied levels \(j\ge1\). To bound the number of partitions with exactly \(r\) such levels, choose indices \(1\le j_1<\cdots<j_r\le m\). At index \(j_i\), there are at most \(N/2^{j_i}<2^{m+1-j_i}\) multiplicity choices. As \(j_i\ge i\), the number of such partitions is at most
\[
\binom mr 2^{r(m+1)-r(r+1)/2}.\tag{4}
\]
The exponent in (4) increases with \(r\in[0,m]\). Consequently, summing over \(r\le(1-\varepsilon)m\) and using \(\sum_r\binom mr=2^m\),
\[
\#\{\lambda\in\mathcal B_N:r(\lambda)\le(1-\varepsilon)m\}
\le2^{(1-\varepsilon^2)m^2/2+O(m)}.\tag{5}
\]
Dividing (5) by the lower bound (2) proves
\[
\frac{\#\{\lambda\in\mathcal B_N:r(\lambda)\le(1-\varepsilon)m\}}{|\mathcal B_N|}
\le 2^{-\varepsilon^2m^2/2+O(m\log m)}=o(1).\tag{6}
\]
In particular, the unmarked distribution of \(r(\lambda)/m\) converges in probability to \(1\), uniformly for odd \(N\) within a dyadic interval.

**Step 3: transfer to the marked count.** The interpretation above gives
\[
\frac{p(N)}{f(N)}
=\frac{1}{|\mathcal B_N|}\sum_{\lambda\in\mathcal B_N}2^{r(\lambda)}.
\]
Because \(0\le r(\lambda)\le m\), this ratio is at most \(2^m\). By (6), for each fixed \(\varepsilon>0\), at least a fraction \(1-o(1)\) of its summands have \(r(\lambda)>(1-\varepsilon)m\). Therefore
\[
(1-o(1))2^{(1-\varepsilon)m}
\le\frac{p(N)}{f(N)}\le2^m.\tag{7}
\]
Take base-two logarithms, divide by \(m\), let \(m\to\infty\), and finally let \(\varepsilon\downarrow0\). The result is
\[
\log_2(p(N)/f(N))=m+o(m).
\]
Since \(\log_2N=m+O(1)\), the stated relative exponent follows. Finally (3), (7), and \(m=(\log N)/(\log2)+O(1)\) give the two logarithmic growth formulas. This completes the proof.

## Verification

A standalone checker, `CHECKER.py`, builds both recurrence sequences to \(2^{18}-1\), independently enumerates odd-multiplicity binary partitions by occupied-level count for every \(1\le N<130\), checks the weighting \(2^{r(\lambda)}\), and prints the relative logarithmic exponent at \(N=2^m-1\) for \(5\le m\le17\). Its exact output is supplied as `CHECKER_OUTPUT.txt`. The finite checks confirm definitions and boundary cases; the limiting theorem uses the unrestricted counting proof above.

## Relationship to prior work

Ballantine and Beck (first publicly posted 20 March 2023), Section 12, explicitly propose comparing the asymptotic growth of several self-similar sequences at odd indices. Their Sections 1 and 6 give the semi-Fibonacci and semi-Pell partition interpretations used here. Keith and Munagi (preprint first posted 23 December 2019; later published in 2023) supply composition interpretations, recurrences, and generating functions but do not give the claimed asymptotic ratio in their inspected full text. OEIS A030067 and A129095 contain the individual sequences and related numerical tables; these known recurrences and enumerations are not claimed as new. The new contribution is the relative exponent obtained from near-full support concentration.

## Limitations

The result is a sharp exponent in a power-law comparison, **not** a multiplicative asymptotic equivalent or explicit second-order expansion. It concerns odd indices or, for arbitrary indices, the odd part. It does not compare semi-Tribonacci, semi-Padovan, semi-Lucas, or other sequences mentioned in the motivating open question. Existing more general asymptotic results for weighted binary partitions may imply the theorem even if they do not use its sequence names; this remains a literature risk, and unindexed work cannot be excluded by a search.

## References

1. C. Ballantine and G. Beck, *Partitions enumerated by self-similar sequences*, arXiv:2303.11493v1 (20 March 2023), especially Definition 1, Section 6 and Section 12. https://arxiv.org/abs/2303.11493
2. W. J. Keith and A. O. Munagi, *Binary compositions and semi-Pell compositions*, arXiv:1912.11148 (23 December 2019); revised as *Power compositions and semi-Pell compositions*, Online Journal of Analytic Combinatorics 18 (2023), Paper 2, especially Sections 1, 2, and 5. https://combinatorialpress.com/article/ojac/vol18/276.pdf
3. OEIS A030067, semi-Fibonacci sequence. https://oeis.org/A030067
4. OEIS A129095, semi-Pell sequence. https://oeis.org/A129095
