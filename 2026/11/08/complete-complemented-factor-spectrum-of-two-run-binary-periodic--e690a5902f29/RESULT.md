# Complete complemented-factor spectrum of two-run binary periodic words

## Finding

For positive integers \(a,b\), let \(W_{a,b}=(0^a1^b)^\omega\) be the right-infinite binary word with one zero run and one one run per period. Let \(\mathcal F_{a,b}(n)\) be its set of distinct contiguous factors of length \(n\), and for a binary word \(u\) let \(\overline u\) be its bitwise complement. Define the *complemented-factor language*
\[
\mathcal C_{a,b}=\{u\in\{0,1\}^{+}:u,\overline u\text{ are both factors of }W_{a,b}\},\qquad
c_{a,b}(n)=|\mathcal C_{a,b}\cap\{0,1\}^n|.
\]

**Theorem (unequal runs).** If \(a\ne b\) and \(m=\min(a,b)\), then the **entire** complemented-factor language is
\[
\boxed{\mathcal C_{a,b}
=\{0^i,1^i:1\le i\le m\}
\ \cup\ \{0^i1^j,1^i0^j:1\le i,j\le m\}.}
\]
Thus
\[
\boxed{c_{a,b}(n)=\begin{cases}
2n,&1\le n\le m,\\
2(2m-n+1),&m<n\le2m,\\
0,&n>2m;
\end{cases}}
\]
and its finite, length-refined enumerator and total number of nonempty complemented factors are
\[
\boxed{\sum_{n\ge1}c_{a,b}(n)z^n=\frac{2z(1-z^m)(1-z^{m+1})}{(1-z)^2},\qquad
|\mathcal C_{a,b}|=2m(m+1).}
\]
In particular, the maximum complemented-factor length is exactly \(2m\), so the first complement-free factor length is \(2m+1\).

**Theorem (equal runs).** If \(a=b=m\), then \(\mathcal C_{m,m}\) is the full nonempty factor language of \(W_{m,m}\) and
\[
\boxed{c_{m,m}(n)=2\min(n,m)\qquad(n\ge1).}
\]
Consequently, an arbitrarily small integer asymmetry in the two run lengths changes the complemented-factor language from infinite to finite. The unordered pair \(\{a,b\}\) matters only through \(\min(a,b)\) in the unequal case.

Equivalently, since complementing \(W_{a,b}\) produces a cyclic rotation of \(W_{b,a}\), the same theorem classifies the **intersection** of the nonempty contiguous-factor languages of \(W_{a,b}\) and \(W_{b,a}\).

## Assumptions and scope

All factors are *contiguous*, not scattered. The word is one-sided infinite, but every cyclic phase occurs in every period, so its factor language is the same as that of the corresponding bi-infinite periodic word. Both run lengths range over all positive integers. The binary involution exchanges \(0\) with \(1\), without reversal. Distinct words, not positional occurrences, are counted. The empty word is excluded. The maximum-length claim is only for unequal runs; for equal runs there are complemented factors of every positive length.

## Proof

**1. Mixed factors with two transitions cannot be complemented when the run lengths differ.** Assume \(a\ne b\). Any factor with at least two changes of letter contains a complete internal maximal constant-letter run between two consecutive changes. Such a run has length exactly \(a\) if it contains zeros, or exactly \(b\) if it contains ones. Its complement would have to contain, between the corresponding two changes, a complete run of the *opposite* letter of the same length. The opposite letter's complete runs in \(W_{a,b}\) have the other, unequal length. This is impossible. Thus every word in \(\mathcal C_{a,b}\) has at most one transition.

**2. Exhaustive characterization of transition-free and one-transition factors.** Both \(0^i\) and \(1^i\) are factors precisely when \(1\le i\le m\). For positive integers \(i,j\), the contiguous factor \(0^i1^j\) occurs precisely when \(i\le a\) and \(j\le b\), because a run boundary is available in every period. Its complement \(1^i0^j\) occurs precisely when \(i\le b\) and \(j\le a\). Hence the two appear together precisely when \(i,j\le m\). Reversing the roles of the letters gives the same criterion for \(1^i0^j\). By Step 1, there are no other complemented factors. This proves the set identity, including necessity and sufficiency.

**3. Counts and generating function.** The unary factors contribute \(2\sum_{i=1}^{m}z^i\). The one-transition factors contribute \(2(\sum_{i=1}^{m}z^i)^2\). These two sets are disjoint. Summing and simplifying,
\[
2\frac{z(1-z^m)}{1-z}+2\left(\frac{z(1-z^m)}{1-z}\right)^2
=\frac{2z(1-z^m)(1-z^{m+1})}{(1-z)^2}.
\]
For \(n\le m\), both unary factors occur and there are exactly \(2(n-1)\) one-transition factors, giving \(2n\). For \(m<n\le2m\), the positive solutions of \(i+j=n\) with \(i,j\le m\) number \(2m-n+1\), and each gives two orders. For \(n>2m\), there are no solutions or unary factors. Evaluating the finite polynomial at \(z=1\) gives \(2m+2m^2=2m(m+1)\). At length \(2m\), precisely \(0^m1^m\) and \(1^m0^m\) survive.

**4. Equal-run boundary.** If \(a=b=m\), shifting the period by \(m\) positions sends each symbol to its complement. Therefore every occurring word has an occurring complement. For \(1\le n\le m\), no factor can contain two transitions; the two unary words and \(2(n-1)\) one-transition words give \(2n\) distinct factors. At length \(m\), these \(2m\) words distinguish all \(2m\) cyclic starting positions. For \(n\ge m\), extending any length-\(m\) phase factor preserves distinctness, and there are only \(2m\) phases. Hence the factor count is constantly \(2m\) from length \(m\) onward. This proves \(2\min(n,m)\) for every \(n\ge1\).

## Verification

The standalone Python file `verify_complement_spectrum.py` independently constructs each periodic factor set by cyclic-phase substrings, independently complements its strings, and compares the resulting set word by word against the theorem's explicit language. It also compares every length count and total count. A run over all \(256\) ordered pairs \(1\le a,b\le16\) checked \(13{,}568\) parameter-length profiles up through length \(3(a+b)+2\), with all checks passing. This is a finite regression check; the proof above establishes the unbounded quantified statement.

Example: for \((a,b)=(3,5)\), the complemented-factor counts at lengths \(1,2,3,4,5,6\) are \(2,4,6,6,4,2\), followed by zeros; the total is \(24\). For \((a,b)=(3,3)\), the counts are \(2,4,6,6,6,\ldots\) and never vanish.

## Relationship to prior work

Currie, Dvořáková, Ochem, Opočenská, Rampersad and Shallit introduce the two natural complement-avoidance invariants: forbidding a complementary pair at a given factor length and bounding the *total* number of complemented factors (arXiv:2209.09598, first posted September 20, 2022; later published in 2025). Their published theorems focus on repetition thresholds for general infinite words and special morphic witnesses. The present result supplies an explicit complete complemented-factor **language** and a length-refined enumerator for the entire two-run periodic family, without any finite-critical-exponent claim. The general possibility that different periodic words have only finitely many common factors is not asserted as novel; the exact intersection and its sharp \(\min(a,b)\) law are the claims here.

Dvořáková, Medková and Pelantová investigate complementary-symmetric Rote sequences, a different aperiodic family, emphasizing critical exponent and recurrence. Standard total factor-complexity formulas for two-run periodic words and counts of antisquare factors do not themselves specify which factors occur together with their bitwise complements. The equal-run symmetry case is elementary background, included for a complete boundary classification.

## Limitations

The statement is restricted to binary periodic hosts with exactly one constant run of each letter per period. There is no assertion for periods with four or more runs, general periodic pairs, aperiodic words, scattered subsequences, or occurrence multiplicities. The work contains a same-model correctness/originality/value review and finite tests; independent validation and independent audit have not been performed. Searches did not establish bibliographic uniqueness: a specialized equivalent result in unindexed work remains possible.

## References

1. J. Currie, L. Dvořáková, P. Ochem, D. Opočenská, N. Rampersad, and J. Shallit, *Complement Avoidance in Binary Words*, arXiv:2209.09598 (first public September 20, 2022), https://arxiv.org/abs/2209.09598; *Electronic Journal of Combinatorics* 32(4), P4.24 (2025), https://doi.org/10.37236/11555.
2. L. Dvořáková, K. Medková, and E. Pelantová, *Complementary Symmetric Rote Sequences: The Critical Exponent and the Recurrence Function*, *Discrete Mathematics & Theoretical Computer Science* 22(1) (2020), https://doi.org/10.23638/DMTCS-22-1-20.
