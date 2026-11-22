# Exact shortest unique factors of dyadic regular-paperfolding prefixes

## Finding
Let \(p_1p_2\cdots\) be the regular binary paperfolding word, defined by \(p_n=1\) when the odd part of the positive integer \(n\) is \(1\pmod 4\), and \(p_n=0\) otherwise. Let \(P_k=p_1\cdots p_{2^k}\). A *globally shortest unique factor* is a contiguous substring occurring at exactly one starting position in \(P_k\), of the shortest length among all such substrings.

**Theorem.** For every integer \(k\ge6\), the shortest unique factor length is exactly
\[
L_k=2^{k-4}+1.
\]
There are exactly two globally shortest unique factors, each occurring once. Their **zero-based** starting positions are precisely
\[
11\cdot2^{k-4}-1,\qquad 12\cdot2^{k-4}-1.
\]
The two factors are necessarily different, as each occurs only once. For example the length-\(64\) prefix has two length-\(5\) shortest unique factors starting at positions \(43\) and \(47\).

## Assumptions and scope
The alphabet is \(\{0,1\}\) and factors are contiguous; occurrence counts include overlapping starts. This is the **global** shortest-unique-factor invariant, not a position-constrained shortest unique substring, an absent **subsequence**, or a cyclic-factor invariant. Position indices in the theorem and verification scripts start at zero. The theorem covers every finite dyadic prefix with \(k\ge6\), without any asymptotic or probabilistic assumption. The specified paperfolding convention begins \(1101100111001001\ldots\).

## Proof
Write \(x_i=p_{i+1}\) for zero-based indices. The defining odd-part rule gives the exact recurrences
\[
x_{2j}=1-(j\bmod2),\qquad x_{2j+1}=x_j\quad(j\ge0).
\]
Thus \(P_k\) is obtained from \(P_{k-1}\) by interleaving the alternating filler \(1,0,1,0,\ldots\) at even global indices and the letters of \(P_{k-1}\) at odd global indices. We establish a constant-length parity delimiter and a finite factor-completeness property before applying induction.

**Lemma 1 (length-seven parity rigidity).** A factor of length at least seven in the infinite word has a unique starting-position parity. Indeed, a complete enumeration in \(P_8\) gives twelve length-seven factors at even zero-based starts and sixteen at odd starts, with disjoint sets. To justify passing from this finite enumeration to *all* factors, use Lemma 2. (This parity-rigidity phenomenon was also established for general paperfolding sequences as Lemma 2 of Allouche, 1992; it is not claimed as novel here.)

**Lemma 2 (finite coverage and short multiplicity).** Every length-sixteen factor of the infinite paperfolding word occurs at its same starting-position parity within \(P_8\). Indeed, all bits \(p_n\) with \(16\nmid n\) are determined by \(n\bmod32\). In any window of sixteen positions at most one index is divisible by sixteen. For each residue class of window starts modulo \(32\), take the seven representative starts \(r+32t\), where \(1\le r\le32\) and \(0\le t\le6\). All seven windows are contained in \(P_8\) and have the same nonspecial bits. If a special index is \(16h\) at the first representative, its seven values are \(p_{h+2t}\). When \(h\) is odd, these alternate; when \(h\) is even, they equal the seven consecutive values \(p_{h/2+t}\), among whose odd-indexed arguments at least two different values occur. Hence both permitted values at the special index occur in the seven representatives. This proves same-parity completeness.

A separate complete enumeration of the length-sixteen factors of \(P_8\) gives exactly sixty-four distinct factors, with occurrence-frequency histogram sixteen at multiplicity three, forty-seven at multiplicity four, and one at multiplicity five. Consequently, **every factor of length at most sixteen in any \(P_k\) with \(k\ge8\) occurs at least three times**, since it extends inside the infinite word to a length-sixteen factor that already has at least three occurrences in \(P_8\).

**Lemma 3 (occurrence transfer and its right-boundary exception).** Let \(k\ge9\) and \(u\) be a factor of \(P_k\) of length at least seventeen. Its starting parity is fixed by Lemma 1. Project \(u\) to its letters at odd global positions, obtaining a contiguous factor \(v\) of \(P_{k-1}\) of length at least eight. All occurrences of \(v\) have one starting parity by Lemma 1, so alternating even-position filler is identical when reinserted. Every occurrence of \(v\) yields an occurrence of \(u\), *except possibly* the terminal occurrence of \(v\) as the suffix of \(P_{k-1}\) when \(u\) ends with an even-position filler. That single boundary occurrence then lacks room for the final filler. No other occurrence is lost and none occurs at the opposite starting parity. If \(u\) ends at an odd global index, there is **no** lost terminal occurrence and \(u\) and \(v\) have exactly equal occurrence counts.

**Induction and the boundary invariant.** In addition to the theorem, induct on the following two assertions:

(A) every factor of \(P_k\) shorter than \(L_k\) occurs at least twice;

(B) every *suffix* of \(P_k\) shorter than \(L_k\) occurs at least three times.

Both assertions hold at \(k=8\): by Lemma 2 every factor of length at most sixteen (that is, shorter than \(L_8=17\)) appears at least three times. Direct exhaustive counting also verifies that exactly two length-seventeen factors occur once, starting at positions \(175\) and \(191\).

Suppose the claims hold at \(k-1\ge8\), and write \(d=L_{k-1}\). For any factor \(u\) of length \(17\le\ell<2d-1\), its projected factor \(v\) has length at most \(\lceil\ell/2\rceil\le d-1\), hence appears at least twice by (A). If the trailing filler does not occur, all these occurrences transfer. If the trailing filler can exclude one occurrence, this happens only if \(v\) is a suffix of \(P_{k-1}\); property (B) gives at least three occurrences before the one possible loss. Thus \(u\) occurs at least twice, establishing (A) for these lengths. Shorter factors are covered by Lemma 2.

For a suffix \(u\) of \(P_k\) with \(17\le |u|<2d-1\), the last global position is odd. Its projected \(v\) is a suffix of \(P_{k-1}\), of length at most \(d-1\). By (B), \(v\) occurs at least three times, and no terminal occurrence is lost because \(u\) ends at an odd global position. This proves (B) at \(k\); short suffixes are again covered by Lemma 2.

Finally take a length-\(2d-1\) factor \(u\). At an **even** starting position it projects to a factor of length \(d-1\), which has at least two surviving occurrences by (A) and (B) as above. At an **odd** starting position it projects to a factor of length \(d\) and ends at an odd global index; occurrence counts transfer *exactly*. Consequently the uniquely occurring length-\(2d-1\) factors are in exact bijection with the uniquely occurring length-\(d\) factors of \(P_{k-1}\), and their zero-based starts obey \(i\mapsto2i+1\).

Starting with \(d=17\) and starts \(175,191\) at \(k=8\), induction gives \(L_k=2L_{k-1}-1\) and starts \(2i+1\), yielding the asserted closed forms for every \(k\ge8\). The two remaining allowed orders \(k=6,7\) are established by direct exhaustive counting, with shortest lengths and zero-based starts respectively \((5;43,47)\) and \((9;87,95)\); both agree with the same formulas. This completes the proof.

## Verification
Run `python3 verify_base.py` and `python3 verify_extensions.py` in a directory containing these two files. The first independently enumerates *all* factors of \(P_6,P_7,P_8\), the parity-separated length-seven sets, and every length-sixteen factor occurrence of \(P_8\). The second uses a different recursive construction of the sequence and nearest-neighbor longest-common-prefix calculations on sorted suffixes to check the theorem through \(k=12\), as well as the suffix boundary invariant at the threshold-minus-one length. The exact baseline certificate is sixty-four length-sixteen factors with histogram \((3:16,4:47,5:1)\). Both programs emit explicit PASS markers; their output is included as standalone text files.

The infinite claim rests on Lemmas 1–3 and the induction, not on extrapolating these finite experiments. A direct code enumeration is relied upon only for explicitly specified finite base cases and the constant-size factorizations in Lemmas 1–2.

## Relationship to prior work
Charalampopoulos, Mohamed, Pissis, Verbeek and Zuba (2026) analyze algorithms for computing global shortest unique and shortest absent substrings on arbitrary packed inputs. Their all-input algorithm does not state a uniform exact value or unique-start classification for dyadic paperfolding prefixes. Allouche (1992), **Lemma 2**, already proves length-seven starting-parity rigidity for any paperfolding sequence, and his main theorem counts the *distinct* factors of each length in the infinite word; the present proof credits and uses the parity fact, but the finite-prefix occurrence multiplicities, sharp unique length and two unique positions are distinct information. Shallit (2024/2025) studies run lengths of paperfolding sequences, not this finite-prefix uniqueness invariant. Faro, Marino and Pavone (2026) classify minimal unique factors in a Thue–Morse attractor setting, for a different automatic word. The published neighboring periodic-word classifications in the searchable research record likewise concern different morphisms and cannot imply this paperfolding conclusion solely from their numerical similarities.

## Limitations
The result is for the regular paperfolding convention above, not arbitrary generalized folding instructions, arbitrary prefix lengths, or cyclic occurrences. The shortest **unique** substrings are distinct from all inclusion-minimal unique substrings, whose full spectrum is not classified. Computational certificates check finitely many stated bases and examples; infinite validity is supplied by the induction. Although a structured literature and indexed-result comparison found no statement covering this exact theorem, an unindexed earlier equivalent remains a possible priority risk. Independent external validation has not been performed.

## References
1. Panagiotis Charalampopoulos, Manal Mohamed, Solon P. Pissis, Hilde Verbeek and Wiktor Zuba, *Faster Algorithms for Shortest Unique or Absent Substrings*, arXiv:2605.04826, first public 2026-05-06, https://arxiv.org/abs/2605.04826.
2. Jean-Paul Allouche, *The number of factors in a paperfolding sequence*, Bulletin of the Australian Mathematical Society 46 (1992), 23–32, https://doi.org/10.1017/S0004972700011655 (especially Lemma 2 and the factor-complexity theorem).
3. Jeffrey Shallit, *Runs in Paperfolding Sequences*, arXiv:2412.17930, first public 2024-12-23, https://arxiv.org/abs/2412.17930.
4. Simone Faro, Francesco Pio Marino and Arianna Pavone, *Smallest String Attractors and Minimal Coverage Certificates of Thue–Morse Words*, arXiv:2610.10950, first public 2026-10-07, https://arxiv.org/abs/2610.10950.
