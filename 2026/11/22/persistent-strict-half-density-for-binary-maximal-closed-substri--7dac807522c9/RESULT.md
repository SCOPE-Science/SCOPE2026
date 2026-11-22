# Persistent strict half-density for binary maximal closed substrings across a cut

## Finding

Let \(F_2(n)\) be the largest number of **positional maximal closed substring occurrences** of any binary word of length \(n\) that cross one internal cut. Then, for every integer \(n\ge13\),

\[
F_2(n)\ge \left\lfloor\frac n2\right\rfloor+1.
\]

In particular, an excess over half the length persists at every length from \(13\) onward; for every even \(n\ge14\) this gives \(F_2(n)>\lceil n/2\rceil\). This is a constructive lower bound, **not** a claim that equality holds for the unrestricted maximum. An explicit eight-run binary word realizes at least the displayed count at a specified cut.

## Assumptions and scope

A nonempty string is *closed* if it has length one or possesses a nonempty proper border (a prefix equal to a suffix) occurring only at its two ends. An occurrence \([i,j]\), with zero-based inclusive endpoints, is a maximal closed substring (MCS) when its factor is closed, and every available one-character extension to its left or right is open. Distinct positional intervals are counted even when they spell equal strings. A cut after index \(c\) is crossed precisely by intervals with \(i\le c<j\).

Fix \(a\ge3\) and \(\varepsilon\in\{0,1\}\), or take the exceptional pair \((a,\varepsilon)=(2,1)\). Define the binary word

\[
W_{a,\varepsilon}=11\,0^a\,1011101\,0^{a-1+\varepsilon},\qquad n=|W_{a,\varepsilon}|=2a+8+\varepsilon,
\]

with cut immediately after index \(c=a+2\), the isolated \(1\) following the first zero run. The construction covers every integer \(n\ge13\) by taking \(\varepsilon\) to be the parity of \(n\) and \(a=(n-8-\varepsilon)/2\).

## Proof

**One-character extension lemma.** If a length-at-least-two closed word \(U\) has longest border \(B\) of length \(b\), its right extension \(Ux\) is closed if and only if \(x\) agrees with character \(U[b]\), immediately after the first copy of \(B\). To see necessity, if \(Ux\) had a border of length at most \(b\), that prefix would also occur at the beginning of the second copy of \(B\), strictly before the new suffix occurrence, giving three occurrences. A longer border of \(Ux\) must have its first \(r-1\) letters equal to a border of \(U\), forcing \(r-1\le b\). Thus its only possible length is \(b+1\), which requires \(x=U[b]\). Conversely this equality extends both end copies of \(B\) to the new border \(Bx\), still with exactly two occurrences. The left-extension version follows by reversal: prepending a symbol preserves closedness precisely when it matches the character before the final copy of \(B\).

The following table lists \(a+5\) distinct candidate intervals and their longest borders. The ranges are zero-based, inclusive, and a row with an index \(j\) denotes one interval for every integer \(3\le j\le a\).

| Interval | Longest border | Number |
| --- | --- | ---: |
| \([0,a+5]\) | `11` | 1 |
| \([0,a+7]\) | `110` | 1 |
| \([1,a+3]\) | `10` | 1 |
| \([1,n-1]\) | \(1\,0^{a-1+\varepsilon}\) | 1 |
| \([j,2a+10-j]\), \(3\le j\le a\) | \(0^{a+2-j}\) | \(a-2\) |
| \([a+1,a+4]\) | `01` | 1 |
| \([a+1,a+9]\) | `010` | 1 |
| \([a+2,a+8]\) | `101` | 1 |

For each row, its proposed border occurs exactly twice: once at the interval's beginning and once at its end. This is immediate from the displayed run structure. More explicitly, each non-unary border listed (`11`, `110`, `10`, \(1\,0^{a-1+\varepsilon}\), `01`, `010`, `101`) has only those two occurrences in the specified interval. The unary border \(0^{a+2-j}\) lies in exactly the two outer zero-run pieces of its interval, with the intervening nonzero block separating them. Any border with exactly two occurrences is necessarily longest: a longer border would give an intervening third occurrence of its prefix. Hence all listed factors are closed, with exactly the stated longest borders.

Maximality follows by comparing context letters at the corresponding two border copies. In the order of the table, the pairs *(preceding character of the whole interval, preceding character of its terminal border copy)*, when both exist, are respectively: absent, absent, \((1,0)\), \((1,0)\), \((0,1)\), \((0,1)\), \((0,1)\), \((0,1)\). The pairs *(following character of the interval, following character of its initial border copy)*, when both exist, are: \((1,0)\), \((1,0)\), \((1,0)\), absent, \((0,1)\) or absent at the right edge, \((1,0)\), \((0,1)\), \((0,1)\). Every available comparison is unequal. The one-character extension lemma therefore shows that every listed interval is an MCS. In the exceptional \(a=2\) case, the indexed middle row is empty; all context comparisons remain valid because \(\varepsilon=1\).

Each interval contains indices on both sides of \(c=a+2\). Their endpoint pairs are distinct, and their number is

\[
4+(a-2)+3=a+5=\left\lfloor\frac{2a+8+\varepsilon}{2}\right\rfloor+1.
\]

Thus \(F_2(n)\ge\lfloor n/2\rfloor+1\) for all the covered lengths, which are precisely all \(n\ge13\). \(\square\)

## Verification

The standalone program `verify.py` independently recomputes the closedness of each proposed factor by enumerating its border occurrences, and separately checks both one-character extensions. Running `python3 verify.py` checks \(57\) parameter pairs (lengths \(13\)–\(69\)), \(1211\) asserted MCS occurrences, and \(15\) complete enumerations of the entire cut-crossing MCS family at shorter lengths. The program prints `PASS` if all assertions hold; its executed output is supplied as `verification-output.txt`. These finite computations test the formulas; the preceding symbolic proof establishes every admissible parameter.

## Relationship to prior work

Faro, Marino, and Pavone (2026, arXiv:2611.11552, Section 7) proved the universal upper bound \(3(n-1)\) for MCSs crossing a cut, and provided for every length a binary construction with at least \(\lfloor(n-1)/2\rfloor\) crossing MCSs. The present construction gives a strict improvement to that *specific lower construction* at every \(n\ge13\), and establishes its persistence over every longer length. It does not improve the leading asymptotic lower-density coefficient of \(1/2\) or the universal upper bound. General valid-pair and run-length-encoded MCS enumeration are known (Umezaki et al. 2026); those algorithmic characterizations do not by themselves specify this all-length witness and cut count. The finite length-fourteen instance is not separately claimed new.

## Limitations

The claim is a lower bound only; it neither determines the exact extremal value \(F_2(n)\) nor classifies its global maximizers. Its additive improvement over the previously exhibited lower construction is one or two crossings and leaves the leading asymptotic coefficient unchanged. The particular eight-run family is constructive, not asserted unique or optimal. Independent mathematical audit and exhaustive literature coverage have not been performed.

## References

1. S. Faro, F. P. Marino, A. Pavone, *Internal Queries for Maximal Closed Substrings*, arXiv:2611.11552v1 (public 8 November 2026), https://arxiv.org/abs/2611.11552 . Relevant material: Definition 1, Theorem 12, Proposition 14, Appendix B.
2. H. Umezaki, H. Shibata, Y. Nakashima, S. Inenaga, *Compact Enumeration of Maximal Closed Substrings in Run-Length Encoded Strings*, arXiv:2607.02838v2 (originally public 3 July 2026), https://arxiv.org/abs/2607.02838 . Relevant material: Definition 1, Lemma 1 and Section 4.
3. J. Fischer, D. Köppl, *Output-Sensitive Enumeration of Maximal Closed Substrings in Linear Space*, arXiv:2610.38114v1 (public 28 October 2026), https://arxiv.org/abs/2610.38114 .
