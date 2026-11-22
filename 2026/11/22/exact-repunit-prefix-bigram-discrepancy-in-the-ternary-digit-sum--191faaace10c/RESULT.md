# Exact repunit-prefix bigram discrepancy in the ternary digit-sum word

## Finding
Let \(t(n)=s_3(n)\bmod 3\), where \(s_3\) is the sum of base-three digits, and let
\[
 A(N)=\#\{0\le n<N:(t(n),t(n+1))=(0,1)\},\qquad N_r=(3^r-1)/2.
\]
For every integer \(r\ge1\), write \(r=3k+s\), \(s\in\{0,1,2\}\). Then
\[
 A(N_r)-\frac{3N_r}{13}=
 \begin{cases}
 -k,&s=0,\\
 k+10/13,&s=1,\\
 1/13,&s=2.
 \end{cases}
\]
The frequency of the factor \(01\) is \(3/13\). The infinite word \(t\) is sharply \(2\)-letter-balanced but is **not factor-balanced**: its \(01\) discrepancy is unbounded. These are properties of the single classical ternary digit-sum word, not claims for every generalized Thue–Morse word.

## Assumptions and scope
Digits and letters are in \(\{0,1,2\}\); indices start at zero. The factor \(01\) is *contiguous*, not a scattered subsequence. The number \(A(N)\) counts pair starts \(0,\ldots,N-1\), so the relevant prefix of \(t\) has length \(N+1\). A letter is \(C\)-balanced when its counts in any two equal-length factors differ by at most \(C\). Factor-balancedness requires a potentially factor-dependent bound for *every* finite factor. The source \(t\) is fixed by the primitive length-three substitution \(a\mapsto a(a+1)(a+2)\) modulo three.

## Proof
**Carry reduction.** Let \(c(n)\) be the number of trailing base-three digits equal to two in \(n\), including \(c(0)=0\). Incrementing changes the digit sum by \(1-2c(n)\), hence
\[
 t(n+1)-t(n)\equiv1+c(n)\pmod3.
\]
Consequently \((t(n),t(n+1))=(0,1)\) precisely when both \(s_3(n)\equiv0\pmod3\) and \(c(n)\equiv0\pmod3\).

**Exact finite count.** The base-three expansion of \(N_r\) consists of \(r\) ones. Each \(0\le n<N_r\) has a unique highest position \(j\in\{0,\ldots,r-1\}\) where its digit is zero rather than one: higher positions are ones and the \(j\) lower positions are arbitrary. If exactly \(c\) of those lower positions are trailing twos, then three cases exhaust the valid contributions to \(A(N_r)\):

* For \(0\le c\le j-2\), \(3\mid c\), the next digit is zero or one and at least one higher free digit remains. Exactly \(2\cdot3^{j-c-2}\) choices have digit sum zero modulo three.
* For \(c=j-1\), admissibility requires \(j\equiv1\pmod3\). The next digit zero or one solves the digit-sum condition exactly once if \(r\not\equiv0\pmod3\), and never otherwise.
* For \(c=j\), all free lower digits are two and the digit at \(j\) stops the carry. This contributes one exactly when \(j\equiv0\pmod3\) and \(r\equiv1\pmod3\).

The first case sums to
\[
 B_r=\sum_{h=0}^{\lfloor(r-3)/3\rfloor}\big(3^{r-3h-2}-1\big),
\]
with the empty sum interpreted as zero. The last two cases contribute respectively
\[
 \mathbf1_{3\nmid r}\,\#\{0\le j<r:j\equiv1\pmod3\},\quad
 \mathbf1_{r\equiv1\,(\mathrm{mod}\,3)}\,\#\{0\le j<r:j\equiv0\pmod3\}.
\]
Elementary geometric summation gives, for \(r=3k,3k+1,3k+2\) respectively,
\[
 A(N_r)=
 \begin{cases}
 3(27^k-1)/26-k,\\
 9(27^k-1)/26+k+1,\\
 27(27^k-1)/26+1.
 \end{cases}
\]
Substituting \(N_r=(3^r-1)/2\) proves the asserted exact discrepancy. In particular the subsequence \(r=3k\) gives discrepancy \(-k\) for all \(k\ge1\).

**Frequency.** Let \(B_r(a)\) be the number of occurrences of \(01\) wholly within the finite word \(\varphi^r(a)\), with \(B_0(a)=0\), and put \(S_r=\sum_{a=0}^2B_r(a)\). The length-three substitution decomposes \(\varphi^r(a)\) as \(\varphi^{r-1}(a)\varphi^{r-1}(a+1)\varphi^{r-1}(a+2)\). Each of its two joining pairs has difference \(r\pmod3\) between the letters. Thus the two joins contribute across the three shifts exactly twice when \(r\equiv1\pmod3\), and zero otherwise, giving
\[
 S_r=3S_{r-1}+2\mathbf1_{r\equiv1\,(\mathrm{mod}\,3)},\qquad S_0=0.
\]
Moreover \(B_r(a)=S_{r-1}+e_r(a)\) with \(0\le e_r(a)\le2\), so the counts for three shifts differ by at most two. Therefore
\[
 \lim_{r\to\infty}\frac{B_r(a)}{3^r}
 =\lim_{r\to\infty}\frac{S_r}{3^{r+1}}
 =\frac13\sum_{h\ge0}\frac{2}{3^{3h+1}}=\frac3{13}.
\]
Every aligned length-\(3^r\) block of \(t\) is a cyclic letter-shift of \(\varphi^r(0)\). Partitioning arbitrary sufficiently long factors into such blocks and at most two partial edge blocks, and then letting \(r\to\infty\), proves the frequency limit uniformly over starting position. This supplies the frequency needed to interpret the unbounded prefix deviations as a failure of factor-balancedness: if the number of \(01\) occurrences in any two length-\(L\) factors differed by at most \(C\), the limiting average over their translated positions would force each factor's count to differ from its frequency times \(L\) by at most \(C\), contradicting the deviations above (the difference of one boundary pair is at most one).

**Sharp letter balance.** Every aligned three-letter block of \(t\) is a permutation of \(0,1,2\). For each letter \(a\), the discrepancy between its count in the prefix of length \(n\) and \(n/3\) lies in \([-2/3,2/3]\). Consequently two arbitrary equal-length factors have counts of \(a\) differing by less than \(8/3\), hence by at most two. Both \(00\) and \(11\) occur (for example beginning at indices \(44\) and \(8\)), so the balance constant two is sharp for the letter zero.

## Verification
The standalone Python file `verify_repunit.py` independently computes base-three digit sums, contiguous \(01\) occurrences, the digit-partition sum, and the closed formula for all \(1\le r\le12\). It also checks the letter-balance inequality over 297 tested pairs of letter and window length and exhibits sharpness. The captured output is `verification_output.txt`. All reported finite checks passed, but the infinite assertions rest on the exact carry argument and finite-word substitution recurrence, not on enumeration.

## Relationship to prior work
Espinoza, Popoli and Stipulanti (first made public February 3, 2026) study factor-balancedness and discrepancy and establish general sufficient conditions, including a discrepancy/balance equivalence. Balková (first made public July 25, 2011) determines factor frequencies for generalized Thue–Morse morphisms, including the framework for the frequency here. The previously studied binary Thue–Morse factor \(01\) has a discrepancy-transducer treatment by Spiegelhofer (2021). The present statement concerns the **different ternary base-three digit-sum word** and explicitly determines the oscillating discrepancy along all base-three all-ones prefix lengths; neither frequency existence alone nor a binary-case result implies these three residue-class formulas.

## Limitations
The formula is restricted to the contiguous factor \(01\) and the special lengths \(N_r\). It does not determine the global maximum discrepancy at each finite length, all pair discrepancies, or the corresponding law for arbitrary bases or moduli. The factor frequency itself is prior knowledge; novelty is claimed only for the exact prefix-discrepancy formula and its stated balance consequences. Priority against unindexed or indirect equivalent results remains a risk. Independent validation has not been performed.

## References
1. B. Espinoza, P. Popoli and M. Stipulanti, *Factor-balancedness, linear recurrence, and factor complexity*, arXiv:2602.03746 (public February 3, 2026), https://arxiv.org/abs/2602.03746.
2. Ľ. Balková, *Factor frequencies in generalized Thue-Morse words*, arXiv:1107.5033 (public July 25, 2011), https://arxiv.org/abs/1107.5033.
3. L. Spiegelhofer, *Gaps in the Thue–Morse word*, arXiv:2102.01018 (public February 1, 2021), https://arxiv.org/abs/2102.01018.
