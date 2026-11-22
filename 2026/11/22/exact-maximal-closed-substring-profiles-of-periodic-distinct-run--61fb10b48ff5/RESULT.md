# Exact maximal-closed-substring profiles of periodic distinct-run prefixes

## Finding

Let \(q\ge3\) and let \(a_0,\ldots,a_{q-1}\) be pairwise distinct letters. For positive integers \(r_i\), define
\[
P=a_0^{r_0}a_1^{r_1}\cdots a_{q-1}^{r_{q-1}},\qquad
p=\sum_{i=0}^{q-1}r_i,\qquad s_i=\sum_{h<i}r_h.
\]
Consider every nonempty prefix \(W_n\) of \(P^\omega\). Write uniquely \(n=kp+t\) with \(k\ge1\) and \(0\le t<p\), so the present theorem addresses prefixes at least one period long. Let \(K(n)\) count **occurrences** of maximal closed substrings in \(W_n\), not distinct substring values.

Define \(c(t)=|\{i:s_i<t\}|\) and
\[
H(t)=\sum_{i=0}^{q-1}\min\bigl(r_i-1,\max(0,t-s_i)\bigr).
\]
Then the exact output-size formula is
\[
\boxed{K(kp+t)=(k-1)p+q+c(t)+H(t)+\mathbf1_{\{k\ge2\ \mathrm{or}\ t\ge r_0\}}.}
\]
There is also a complete classification of the positions of all maximal closed substrings, given below. In particular, at every complete power \(k\ge2\),
\[
\boxed{K(kp)=(k-1)p+q+1,}
\]
and \(\lim_{n\to\infty}K(n)/n=1\). After the first two periods, appending a letter creates either zero, one, or two new maximal closed substring occurrences in the difference of total counts: the first letter of a run of length at least two has increment two, each strictly interior letter has increment one, the last letter has increment zero, and a singleton run contributes one. This exact three-valued local law is periodic with period \(p\).

**All positions, in one-based indices.** In addition to every maximal monochromatic run interval of \(W_n\), include for each \(i\in\{0,\ldots,q-1\}\), \(j\ge0\), and \(1\le h<r_i\) with \((j+1)p+s_i+h\le n\), the interval
\[
\left[1+jp+s_i+r_i-h,\ (j+1)p+s_i+h\right].
\]
Finally include the entire interval \([1,n]\) exactly when \(n\ge p+r_0\). These three families are disjoint and comprise **all** maximal closed substring occurrences.

## Assumptions and scope

A nonempty substring is *closed* if it is a single letter or has a proper nonempty border appearing exactly twice, as prefix and suffix. A closed occurrence \([u,v]\) of \(W_n\) is *maximal* if neither available one-character extension \([u-1,v]\) nor \([u,v+1]\) is closed. Each occurrence interval is counted separately even when another has identical content. All run letters are distinct, with cyclic indexing, and every run length is positive. Prefixes shorter than a full period are not part of the formula. The claim concerns contiguous substrings rather than scattered subsequences or the set of distinct closed factors.

## Proof

**Periodic boundary rigidity.** In the bi-infinite word \(P^\omega\), every directed boundary bigram \(a_i a_{i+1}\), including the cyclic last-to-first transition, occurs in one position modulo \(p\). This follows immediately from the pairwise distinct letters and \(q\ge3\). Consequently every mixed-letter factor has its starting phase uniquely determined modulo \(p\), and any two occurrences of that factor begin a multiple of \(p\) positions apart.

**Mixed-border maximal occurrences.** Take a nonconstant closed substring \(X\) with a mixed-letter longest border \(B\). Its two occurrences of \(B\) must start exactly \(p\) positions apart: a larger positive multiple would put an intervening copy within \(X\), violating closure. Thus \(X\) has length \(p+|B|\), and its length-\(|B|\) prefix includes a directed boundary. If \(X\) admits an extension to the left, the new length-\(|B|+1\) prefix and suffix still agree, since the letters preceding the two border occurrences are one period apart. There are exactly two occurrences of this longer border in the extended factor: the unique mixed-factor phase precludes any third occurrence. Thus that extension is also closed. The identical argument applies to an available right extension. Therefore a mixed-border closed occurrence is maximal only if it has no left and no right extension, i.e. it is the whole word.

**Unary-border maximal occurrences.** If a nonconstant closed substring has a constant-letter longest border \(a_i^h\), the two border occurrences must lie in successive runs labeled \(a_i\): an intervening full run would give a third occurrence of the same border. The endpoint fragments each have exactly \(h\) letters, since a longer endpoint fragment would also create another border occurrence. Hence the candidate must be the displayed interval with \(1\le h\le r_i\). If \(h<r_i\), extending either endpoint (when possible) adds an extra occurrence of every possible unary border within the nearby run, while no mixed-letter border can be formed because the two endpoint fragments remain different phases within their respective runs. Thus both available extensions are not closed and the occurrence is maximal. If \(h=r_i\), the word at the two ends contains entire equal runs one period apart. Each available extension is itself closed: it has a mixed border obtained by including the adjacent matching letter, which appears at exactly those two aligned phases. Thus a candidate with \(h=r_i\) is maximal only when it is the whole word. This also shows no other nonconstant maximal occurrence can have a unary border.

**Unary occurrences and the whole word.** A constant-letter occurrence is maximal exactly when it is a complete available maximal run: a proper contained constant block extends to another closed constant block. A constant run interval cannot extend to a nonconstant closed word by just one letter (its endpoints would then differ). For the whole prefix, when \(p\le n<p+r_0\), every nonempty border is unary and has an internal occurrence within the first run, so the whole word is not closed. At \(n=p+r_0\), it makes a complete first return to \(a_0^{r_0}\). For \(n>p+r_0\), the border of length \(n-p\) contains a unique-phase directed boundary and occurs only at offsets zero and \(p\); hence the whole word is closed. The three stated interval families are exhaustive and disjoint.

**Counting.** The complete and partial maximal runs give \(kq+c(t)\) occurrences. For each complete adjacent pair of cycles and each run type, the unary-border intervals give \(r_i-1\) choices: a total of \((k-1)(p-q)\). In the last incomplete cycle, the additional choices are \(\min(r_i-1,\max(0,t-s_i))\), totaling \(H(t)\). The whole-prefix occurrence contributes one exactly when \(n\ge p+r_0\), equivalently \(k\ge2\) or \(t\ge r_0\). Adding gives the boxed identity. Since \(c(t)+H(t)\) is bounded in one period, \(K(n)=n+O(p+q)\) for fixed \(P\), and the limit follows. For complete periods \(c(0)=H(0)=0\); comparing consecutive positions of a period establishes the stated zero/one/two increment law, including singleton runs and cycle boundaries.

## Verification

The standalone C++17 program `verify_prefix_mcs.cpp` implements the definition by literal substring comparisons and a separate construction of the three claimed interval families. The run `c++ -std=c++17 -O2 verify_prefix_mcs.cpp -o verify_prefix_mcs && ./verify_prefix_mcs` returned `PASS cases=3564 distinct_MCS_occurrences_checked=74917 substring_occurrences_considered=1374270`. Exhaustive parameter coverage includes all \(q\in\{2,3,4\}\), run lengths in \(\{1,2,3\}\), cycle counts \(1\le k\le4\), and every partial-prefix length, supplemented by 180 seeded larger cases. The tests also include the permitted theorem domain \(q\ge3\). For \(P=\mathtt{aabbbc}\), the prediction gives \(K(6)=3\), \(K(12)=10\), and \(K(18)=16\). These finite checks corroborate the proof and are not used as an infinite certificate.

## Relationship to prior work

Faro, Marino, and Pavone (2026) give general indexing and query frameworks for maximal closed substrings, including query-boundary decomposition; they do not state the specific all-prefix, phase-sensitive count and location formula for distinct-run periodic words. Fischer and Köppl (2026), and Umezaki et al. (2026), develop general output-sensitive enumeration and compressed run-based representations of maximal closed substring occurrences; those algorithmic results do not by themselves give the explicit periodic output profile. Closely related work on *distinct closed factor values* of distinct-run powers gives an exact length spectrum and a quadratic total, but does not determine which **positional occurrences** are maximal or what happens at partial periods. Published exact four-run maximal-closed-occurrence counts cover short four-run inputs (including the corresponding two-letter two-period case), not the arbitrary-period, at-least-three-distinct-letter prefix classification. The present result does not claim general maximal-closed-substring enumeration is new.

## Limitations

The theorem requires \(q\ge3\) distinct cyclic run letters, positive run lengths, and at least one complete period. The formula can be checked for binary two-run cases, but those are not asserted as a new contribution. The cited general enumeration frameworks could yield the claimed profile by further specialization; priority is assessed from the inspected sources rather than assumed globally. The accessible material for the compressed run-based enumeration paper did not include a complete inspected full text; this leaves a residual novelty comparison risk. No independent external mathematical audit has been performed.

## References

1. S. Faro, G. Marino, and M. Pavone, *Internal Queries for Maximal Closed Substrings*, arXiv:2611.11552, first publicly posted 2026-11-08. https://arxiv.org/abs/2611.11552
2. J. Fischer and D. Köppl, *Output-Sensitive Enumeration of Maximal Closed Substrings in Linear Space*, arXiv:2610.38114, first publicly posted 2026-10-28. https://arxiv.org/abs/2610.38114
3. T. Umezaki, T. Shibata, Y. Nakashima, and S. Inenaga, *Compact Enumeration of Maximal Closed Substrings in Run-Length Encoded Strings*, arXiv:2607.02838, 2026-07-03. https://arxiv.org/abs/2607.02838
4. *Closed-factor spectrum of cyclic distinct-run powers*, published mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-closed-factor-spectrum-of-cyclic-distinct-run-powers--be455d83c34c/RESULT.md
5. *The exact maximal closed-substring spectrum of four-run words over arbitrary alphabets*, published mathematical record, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-the-exact-maximal-closed-substring-spectrum-of-four-run-words-ov--86be57deefbe/RESULT.md
