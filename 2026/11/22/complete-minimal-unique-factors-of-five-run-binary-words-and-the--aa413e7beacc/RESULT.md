# Complete minimal unique factors of five-run binary words and the first eight-factor threshold

## Finding

A **minimal unique substring** (MUS) of a finite word is a nonempty contiguous factor that occurs at exactly one starting position, while every proper contiguous factor occurs at least twice (overlaps count). For any five positive integers \(a,b,c,d,e\), consider the binary word
\[
W=0^a1^b0^c1^d0^e.
\]
Set \(A=\max\{a,c,e\}\), \(B=\max\{b,d\}\), \(p=\min\{a,c\}+1\), \(q=\min\{c,e\}+1\), and \(m=\min\{b,d\}\). Write \(U\) for the predicate that exactly one among \(a,c,e\) equals \(A\). The **complete** MUS set is exactly the following eight possible words, each present if and only if its indicated condition holds:

| Factor | Necessary and sufficient condition |
|---|---|
| \(0^A\) | \(U\) |
| \(1^B\) | \(b\ne d\) |
| \(0^p1\) | \(a\ne c\) and not \((U\text{ and }A=p)\) |
| \(01^{m+1}\) | \(\lvert b-d\rvert\ge2\) |
| \(1^{m+1}0\) | \(\lvert b-d\rvert\ge2\) |
| \(10^q\) | \(c\ne e\) and not \((U\text{ and }A=q)\) |
| \(01^m0\) | \(b\ne d\) |
| \(10^c1\) | \(c\le\min\{a,e\}\) |

The eight displayed factors have distinct run patterns. Consequently every positive five-run binary word has at most eight MUSs, **eight is sharp**, and **ten is the least length admitting eight MUSs**. Eight MUSs are attainable at every length \(n\ge10\): the word \(W=0^2 1^1 0^1 1^3 0^{n-7}\) has all eight. At \(n=10\) it is `0010111000`, with MUS set the eight binary words of length three. The bitwise complements of the stated words satisfy the same conclusions.

## Assumptions and scope

The five run lengths are arbitrary **positive integers**, with no separation conditions or genericity assumptions. The word is linear, not circular. The two symbols are labeled \(0\) and \(1\); complementing swaps them. Counts concern distinct MUS factors, equivalently their unique occurrence intervals. A substring is *unique* when its occurrence multiplicity is one, not when a factor value has been selected only once from a set. For the one-letter deletions, the empty word is regarded as repeated. This theorem does not concern shortest unique substrings relative to a particular query interval, or absent/scattered factors.

## Proof

**Local minimality test.** For any occurring factor \(v\) of length at least two, minimal uniqueness is equivalent to \(v\) occurring once and each of the two factors obtained by deleting its first or last letter occurring at least twice. Every other proper contiguous factor is contained in one of these two. Both letters appear at least twice in \(W\), so no one-letter factor is unique.

**Pure powers.** There are three zero runs and two one runs. A pure zero factor occurs once only when its length is \(A\) and the longest zero run is unique. If its length is less than \(A\), the longest run already gives at least two occurrences; if two zero runs share length \(A\), the factor of that length repeats. In the unique-maximum case, \(0^A\) is minimal unique because \(0^{A-1}\) occurs at least twice in the same longest run. This proves the first row, including the possibility that \(U\) fails. Identical reasoning gives the second row for \(1^B\), with uniqueness exactly when \(b\ne d\).

**One change of symbol.** Every factor \(0^i1^j\), for \(i,j\ge1\), occurs at most once at each of the two zero-to-one run boundaries. It occurs twice precisely when \(i\le\min(a,c)\) and \(j\le\min(b,d)\); the two boundary run-length pairs are \((a,b)\) and \((c,d)\). A minimally unique factor cannot have \(i,j\ge2\), because its two one-letter deletions being repeated would force both inequalities and hence repetition of the full factor. With \(j=1\), its mixed one-letter-shorter factor is repeated exactly through threshold \(i-1\le\min(a,c)\), while its uniqueness requires \(i>\min(a,c)\), so \(i=p\). The other deletion is \(0^p\), which must repeat; by the pure-power case, it fails to repeat exactly when \(U\) holds and \(A=p\). This proves the third row. With \(i=1\), the only threshold is \(j=m+1\), but the pure one-factor \(1^{m+1}\) repeats precisely when the longer of the two one runs is at least two longer than the shorter, \(\lvert b-d\rvert\ge2\). This proves the fourth row.

The one-to-zero boundaries have run-length pairs \((b,c)\) and \((d,e)\). The same argument yields the fifth row \(1^{m+1}0\) and the sixth row \(10^q\), including its pure-zero deletion exception. The fact that there are two zero-to-one and two one-to-zero boundaries is used here; it would not be valid to copy the four-run formulas without adjusting the pure-run uniqueness test.

**Two changes: zero–one–zero.** A factor \(0^i1^j0^k\) crosses an entire one run, so \(j\) is either \(b\) or \(d\). If \(b\ne d\), this entire one run uniquely identifies the occurrence, and any factor with \(i>1\) or \(k>1\) has a shorter, still unique three-run factor. Thus the only possible minimal candidate from each boundary is \(01^b0\) or \(01^d0\). Its two truncated two-run factors each repeat exactly when the central one run is the **shorter** one run. Hence the sole candidate is \(01^m0\), proving the seventh row.

If \(b=d\), the two one runs are equal. To be unique, a putative three-run factor must cross a threshold in its left or right zero flank. But to have each of its one-letter-shorter factors repeated, both flank exponents would have to be within the minima of their respective pairs \((a,c)\) and \((c,e)\), so the original factor would appear at both one runs. The same conclusion holds for a flank of length one: its truncated two-run factor forces the remaining flank to fit at both boundaries. Therefore no three-run zero–one–zero MUS arises when \(b=d\).

**Two changes: one–zero–one.** There is only one internal zero run flanked by ones. Any factor \(1^i0^j1^k\) must have \(j=c\) and is unique. Minimality forces \(i=k=1\), because deleting an outer one otherwise still leaves the sole complete middle zero run. Thus the only candidate is \(10^c1\). Its left deletion \(0^c1\) occurs at the second zero-to-one boundary and also at the first exactly when \(a\ge c\); its right deletion \(10^c\) occurs at the first one-to-zero boundary and also at the second exactly when \(e\ge c\). This proves the last row.

**At least three changes.** A factor with four or five alternating runs contains the sole internal \(10^c1\) as a **proper** factor. This three-run factor occurs exactly once, whether or not it itself is minimally unique. Thus the larger factor cannot be minimally unique. We have exhausted all factor types, proving that the table is complete.

**Sharp threshold.** To realize all eight listed factors, the fifth and fourth rows require \(\lvert b-d\rvert\ge2\), so \(b+d\ge4\). The eighth row requires \(c\le a,e\); the third and sixth require \(a\ne c\) and \(e\ne c\), thus \(a,e\ge c+1\). To obtain the first row without suppressing the third or sixth, the unique maximum \(A\) must satisfy \(A\ge c+2\). Therefore \(a+c+e\ge 3c+3\ge6\), and \(a+b+c+d+e\ge10\). At \((a,b,c,d,e)=(2,1,1,3,3)\), all eight conditions hold. Increasing \(e\) preserves them, yielding eight at every larger length, as claimed.

## Verification

The supplied standalone `verify_five_general.py` counts overlapping occurrences of **all literal contiguous substrings** and checks the entire factor set against the table for every one of the \(6^5=7776\) positive parameter tuples with each length at most six. The separate `verify_suffix_general.py` instead uses lexicographically adjacent suffixes, common-prefix lengths, and shortest unique prefixes to derive MUSs without enumerating every substring first. It checks all \(7^5=16807\) tuples with each length at most seven, plus 180 additional randomly sampled tuples with individual lengths up to 89; it also checks the first eight-factor threshold through length 16 and the concrete shortest witness. Both programs use Python 3 standard library only, halt on disagreement, and output `status PASS`. Their matching outputs are embedded as adjacent `.out` files. These computations test the boundaries; the preceding case analysis, not finite extrapolation, proves the universal claim.

## Relationship to prior work

Mieno and collaborators established the MUS definition, generic substring-query algorithms and, in particular, a bound of \(2r-1\) MUSs on a word with \(r\) runs, as discussed in their work on run-length-encoded strings (2016). This general bound gives nine for five runs; it does not specify the sharp eight-factor threshold or the full factor list here. Their later space-efficient MUS work gives general algorithms rather than a parameter-uniform classification. The 2026 work of Charalampopoulos and collaborators concerns faster *shortest unique substring* and shortest absent substring algorithms; its object is different from the fixed-family MUS classification.

A published analysis of **separated** five-run binary words (2026) classifies seven/eight MUSs under the strong condition \(\min\{|a-c|,|a-e|,|c-e|,|b-d|\}\ge2\); the present result retains its generic template and removes all four separation requirements, with the necessary equality and unit-gap exceptions. That prior result requires length at least thirteen for its eight-factor cases, whereas the unrestricted first attainment is ten. A published study of binary words with **exactly two ones** already handles the special case \(b=d=1\), and a published four-run classification handles the smaller-run family. Those known specializations are not asserted as new. Computing one instance with a general MUS algorithm is not the same assertion as this all-parameter necessary-and-sufficient eight-template classification.

## Limitations

This is an exact theorem for binary words having **exactly five** nonempty maximal constant runs, not a formula for arbitrary strings or more runs. Its factor set includes several known specializations and recovers the known separated case, but the claim of originality concerns the **unrestricted** collision-regime classification and the sharp length-ten first attainment. It makes no independent-audit or publication-priority guarantee; an equivalent but unindexed special-case formula may exist.

## References

1. T. Mieno, S. Inenaga, H. Bannai, M. Takeda, *Shortest Unique Substring Queries on Run-Length Encoded Strings*, MFCS 2016, DOI: 10.4230/LIPIcs.MFCS.2016.69, https://doi.org/10.4230/LIPIcs.MFCS.2016.69.
2. T. Mieno, D. Köppl, Y. Nakashima, S. Inenaga, H. Bannai, M. Takeda, *Space-Efficient Algorithms for Computing Minimal/Shortest Unique Substrings*, arXiv:1905.12854 (first posted 2019-05-30), https://arxiv.org/abs/1905.12854.
3. P. Charalampopoulos, M. Mohamed, S. P. Pissis, H. Verbeek, W. Zuba, *Faster Algorithms for Shortest Unique or Absent Substrings*, arXiv:2605.04826 (first posted 2026-05-06), https://arxiv.org/abs/2605.04826.
4. *Seven-or-eight minimal unique factors in separated five-run binary words*, publicly available 2026-10-25, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-seven-or-eight-minimal-unique-factors-in-separated-five-run-bina--2eedb3c17d7e.
5. *Minimal unique factors of binary words with two marked symbols: exact spectrum*, publicly available 2026-10-26, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-minimal-unique-factors-of-binary-words-with-two-marked-symbols-e--82dd9adea10e.
6. *Exact minimal-unique-factor spectrum of four-run binary words*, publicly available 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-minimal-unique-factor-spectrum-of-four-run-binary-words--41aa7a29dd06.
