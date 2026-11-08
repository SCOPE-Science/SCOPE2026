# Sharp unbordered subsequence-universality thresholds and binary boundary classification

## Finding
Let \(\Sigma_q=\{0,1,\ldots,q-1\}\) be a labeled alphabet, \(q\ge2\). A word is *unbordered* if no nonempty proper prefix equals a suffix. Its scattered-subsequence universality index \(\iota_{\Sigma_q}(w)\) is the largest \(k\ge0\) such that every word of length \(k\) over \(\Sigma_q\) is a subsequence of \(w\). For every integer \(k\ge1\), the least length of a simultaneously unbordered, \(k\)-universal word is
\[
L_q(k)=\begin{cases}
2,&q=2,\ k=1,\\
2k+1,&q=2,\ k\ge2,\\
qk,&q\ge3,\ k\ge1.
\end{cases}
\]

For the binary exceptional case, the entire set of shortest witnesses admits an explicit half-length classification. Fix \(k\ge2\), put \(m=k-1\), and take a vector \(c=(c_1,\ldots,c_m)\in\{0,1\}^m\). Let \(\bar c_i=1-c_i\) and
\[
T(c)=001\,c_1\bar c_1\cdots c_m\bar c_m.
\]
Define \(\mathcal C_k\) by \(c_m=0\) and, for each \(1\le j\le m-1\), the *absence* of the simultaneous conditions
\[
 c_{m-j}=1,\qquad c_{m-j+1}=0,\qquad
 (c_{m-j+2},\ldots,c_m)=(c_1,\ldots,c_{j-1}).
\]
The empty-tuples equality at \(j=1\) is understood to hold. Then every binary shortest witness, and no other word, is exactly one of
\[
T(c),\quad\overline{T(c)},\quad T(c)^R,\quad\overline{T(c)^R}
\qquad(c\in\mathcal C_k),
\]
where bar denotes bitwise complementation and \(R\) reversal. These four families are pairwise disjoint. In particular their exact number is \(4|\mathcal C_k|\), and this gives a complete constructive enumeration from binary vectors of length \(k-1\). The counts for \(k=2,3,\ldots,9\) are respectively \(4,4,8,12,24,44,88,168\); for \(k=1\) the two shortest witnesses are `01` and `10`.

## Assumptions and scope
All statements quantify over every integer \(q\ge2\) and \(k\ge1\), with the fixed full ambient alphabet \(\Sigma_q\). A subsequence need not be contiguous. Distinct words, rather than embedded occurrences, are counted. A proper border is nonempty and shorter than the word. For \(q=2\), letters are exactly \(0,1\). No asymptotic closed-form count for \(|\mathcal C_k|\) is asserted.

## Proof
**Arch fact.** Greedily take the shortest nonempty prefix containing all \(q\) symbols, remove it, and repeat. The number of completed arches is the scattered-subsequence universality index. The forward direction follows by splitting a universal word into complete-alphabet blocks; the reverse uses the greedy arch characterization, recalled by Adamson (2023). Hence every \(k\)-universal word has length at least \(qk\). At binary length exactly \(2k\), every arch must be a two-letter pair \(a\bar a\), with no remainder.

**Alphabets of at least three letters.** Write \(A=01\cdots(q-1)\), \(B=02\cdots(q-1)1\) and \(W=A^{k-1}B\). Every length-\(q\) block is a permutation, hence \(W\) is \(k\)-universal of length \(qk\). The letter \(0\) occurs only at positions congruent to \(1\) modulo \(q\). Thus any nonempty border, whose suffix starts with the initial letter \(0\), would have length divisible by \(q\). Every such prefix ends in \(q-1\), whereas every nonempty suffix ends in \(1\). Since \(q\ge3\), no border exists. This realizes the lower bound.

**Binary lower bound and construction.** At length \(2k\), write any \(k\)-universal binary word uniquely as \(a_1\bar a_1\cdots a_k\bar a_k\). If \(a_1\ne a_k\), the first and last letters agree, giving a border of length one. If \(a_1=a_k\) and \(k\ge2\), its first and last pairs agree, giving a proper border of length two. Thus no such word is unbordered when \(k\ge2\). The word \(001(01)^{k-1}\) has exactly \(k\) complete arches and is unbordered: its first two letters are `00`, its last letter is `1`, and every proper suffix of length at least two that begins in `0` starts with `01`. Hence \(L_2(k)=2k+1\) for \(k\ge2\). At \(k=1\), `01` and `10` have length two and are unbordered.

**Localization of the extra symbol.** Let \(k\ge2\) and let \(w\) be a binary \(k\)-universal word of length \(2k+1\). The greedy decomposition has exactly \(k\) arches. Each has length at least two; the one extra symbol is either a one-letter remainder or belongs to one length-three arch of form \(aa\bar a\). All other arches are unlike adjacent pairs. If the longer arch is strictly interior, the word starts and ends with unlike pairs. Such a word necessarily has a border of length one when the initial and final pair symbols differ, or a border of length two when they agree. The same dichotomy excludes a longer final arch: its final pair is \(a\bar a\), while its last letter is \(\bar a\). Thus an unbordered word has either a length-three first arch or a one-letter remainder. In the latter case, writing \(w=(a_1\bar a_1)\cdots(a_k\bar a_k)e\), unborderedness forces \(e=\bar a_k\): otherwise \(e=a_k\), and comparison of the first letter with \(e\) creates either a one-letter border or a two-letter border. Reversing gives a word beginning with \(\bar a_k\bar a_k a_k\), that is, a length-three first arch. Complementation reduces its initial double letter to `00`.

**Border test for the normalized family.** Consider \(T(c)=001c_1\bar c_1\cdots c_m\bar c_m\). No even-length border can occur, because every even-length suffix begins with two unequal letters whereas the initial pair is `00`. A one-letter border occurs exactly when \(c_m=1\). For \(1\le j\le m-1\), a border of odd length \(2j+1\) must compare the prefix \(001c_1\bar c_1\cdots c_{j-1}\bar c_{j-1}\) with the suffix \(\bar c_{m-j}c_{m-j+1}\bar c_{m-j+1}\cdots c_m\bar c_m\). These are equal exactly when \(c_{m-j}=1\), \(c_{m-j+1}=0\), and the indicated remaining \(j-1\) pairs equal the first \(j-1\) pairs. The only other possible odd proper border has length \(2m+1\); it begins with the third letter `1`, so it cannot match the initial `0`. This proves precisely the defining tests of \(\mathcal C_k\). Forward words have equal first two letters and unequal last two; their reversals have the opposite property, and complements start with the opposite bit. Therefore no witnesses are duplicated, proving the classification and count.

## Verification
The standalone Python file `verify_unbordered.py` independently evaluates greedy universality, direct enumeration of all binary target subsequences, and all proper borders. It compares the classification with exhaustive binary words for \(1\le k\le9\), additionally excluding shorter words for \(2\le k\le9\), and validates the reduced-code characterization through \(k=14\). It also checks the \(q\ge3\) construction over \(3\le q\le8\), \(1\le k\le15\). The recorded checks passed: 1,048,564 binary words tested, 676 independent direct-universality comparisons, plus the code-enumeration checks. Finite tests are corroboration; the preceding proof covers all values of the quantified parameters.

## Relationship to prior work
Arch factorization and unconstrained universality counting are established tools in Adamson, *Ranking and Unranking k-subsequence universal words* (2023), and Adamson et al., *k-Universality of Regular Languages* (2023). Gabric, *Ranking and unranking bordered and unbordered words* (2023), treats border-free word ranking without a subsequence-universality constraint. The present result resolves their intersection at the first feasible length, including a binary-specific one-letter obstruction and a complete optimal-witness boundary classification. It does not claim the earlier arch criterion or general unbordered-word algorithms as new. A broader unindexed classification of this intersection could still exist.

## Limitations
The result is restricted to unbordered individual finite words, not cross-bifix-free sets of words. It does not provide a closed elementary expression or asymptotics for \(|\mathcal C_k|\), nor optimized ranking algorithms. The novelty comparison is best-knowledge based rather than proof of uniqueness; independent review remains outstanding.

## References
- D. Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583, first posted April 10, 2023. https://arxiv.org/abs/2304.04583
- D. Gabric, *Ranking and unranking bordered and unbordered words*, arXiv:2305.03000 (2023). https://arxiv.org/abs/2305.03000
- D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, and D. Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658, first posted November 17, 2023. https://arxiv.org/abs/2311.10658
