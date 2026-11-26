# Phase rigidity and exact complementary-subsequence capacity of permutation powers

## Finding

Fix an integer \(q\ge3\), let \(P=0\,1\,\cdots\,(q-1)\), and let \(r\ge0\). For a word \(w\) and a scattered subsequence \(u\), write \(C(w,u)\) for the **set of distinct linear words remaining** after removing any order-preserving positional embedding of \(u\) in \(w\). Let \(R_h=h\,(h+1)\,\cdots\,(q-1)\,0\,\cdots\,(h-1)\) denote the \(h\)-th cyclic rotation of \(P\), for \(0\le h<q\).

**Complete phase-language theorem.** The elements of \(C(P^{r+1},P)\) are exactly the words
\[
R_{s_1}R_{s_2}\cdots R_{s_r},
\]
where the phase sequence \((s_1,\ldots,s_r)\) belongs to
\[
0^*1^*2^*\cdots(q-1)^*0^*.
\]
The last two displays refer to a regular expression on *phase symbols*, not to the original letter alphabet. Empty phase runs are allowed. Consequently, for every \(q\ge3\) and \(r\ge0\),
\[
\boxed{\left|C(P^{r+1},P)\right|=\binom{r+q}{q}-r.}
\]

More strongly, the only remainder created by more than one embedding of \(P\) is \(P^r\), which has **exactly \(r+1\) embeddings**; every other remainder comes from one embedding. The identical statement holds after consistently relabeling the \(q\) distinct letters of \(P\) in any order. In particular, for \(q=3\), the distinct-output counts as \(r=0,1,2,3,4,5\) are \(1,3,8,17,31,51\).

## Assumptions and scope

All words are finite and linear, not cyclic or rotation-equivalence classes. The alphabet has exactly \(q\ge3\) distinct symbols, each occurring once in \(P\). The host consists of precisely \(r+1\) complete copies of the same period \(P\), and the deleted subsequence is exactly one copy of \(P\). A positional embedding is a strictly increasing tuple of source positions reading \(P\); different embeddings may leave the same remainder, which is counted only once. At \(r=0\) the only output is the empty word. The case \(q=2\) follows the same proof but is already a known specialization of the binary alternating-complement theorem and is deliberately excluded from the novelty claim.

## Proof

**Step 1: parameterize every deleted embedding.** Index source copies of \(P\) by \(0,1,\ldots,r\). An embedding of the increasing-symbol word \(P\) selects one occurrence of symbol \(i\) in copy \(t_i\) for every \(0\le i<q\). Its source positions are \(qt_i+i\). These positions increase strictly in symbol order if and only if
\[
0\le t_0\le t_1\le\cdots\le t_{q-1}\le r.
\]
Indeed, if \(t_i>t_{i+1}\), the source-position difference is at most \(1-q<0\); otherwise it is positive. Thus embeddings correspond bijectively to weakly increasing length-\(q\) tuples in \(\{0,\ldots,r\}\), numbering \(\binom{r+q}{q}\).

**Step 2: derive the phase blocks without assumptions about the output.** For each \(j=0,\ldots,r-1\) set
\[
h_j=\#\{i:0\le i<q,\ t_i\le j\}.
\]
Then \(0\le h_0\le\cdots\le h_{r-1}\le q\). Since the \(t_i\) are nondecreasing, the set of symbols already deleted in a source copy at or before \(j\) is the initial segment \(\{0,\ldots,h_j-1\}\). In the remaining word, the \((j+1)\)-st occurrence of every symbol \(i<h_j\) comes from original source copy \(j+1\), whereas for every symbol \(i\ge h_j\) it comes from original copy \(j\). All of these selected occurrences are ordered as
\[
h_j,(h_j+1),\ldots,(q-1),0,1,\ldots,(h_j-1),
\]
which is exactly rotation \(R_{h_j\bmod q}\). Their positions precede the corresponding \((j+2)\)-nd occurrences of the same symbols. Moreover, the last source position of this \(j\)-th output block precedes the first position in the next one: this follows from \(h_j\le h_{j+1}\), since either the earlier block ends in copy \(j\), or it ends with symbol \(h_j-1\) in copy \(j+1\), while the next block starts at or after symbol \(h_{j+1}\) in copy \(j+1\). Consequently the entire remainder is the concatenation
\[
R_{h_0\bmod q}\cdots R_{h_{r-1}\bmod q}.
\]
No other letters remain, since both sides have length \(qr\).

**Step 3: every nondecreasing phase-code sequence is realized.** Conversely, let \(0\le h_0\le\cdots\le h_{r-1}\le q\) be arbitrary. For symbol \(i\), set \(t_i\) to the first \(j\in\{0,\ldots,r-1\}\) with \(h_j\ge i+1\), if one exists, and set \(t_i=r\) otherwise. Then \(0\le t_0\le\cdots\le t_{q-1}\le r\), and precisely \(h_j\) of the \(t_i\)'s are at most \(j\). Therefore the map between weakly increasing \(t\)-tuples and weakly increasing \(h\)-sequences is a bijection. The displayed remainder formula consequently describes every obtainable word.

**Step 4: identify all collisions.** The rotations \(R_0,R_1,\ldots,R_{q-1}\) are pairwise distinct because they begin with different symbols. Thus two output words are equal exactly when their phase sequences agree modulo \(q\) at every block. The only distinct integer codes in \(\{0,\ldots,q\}\) that define the same rotation are \(0\) and \(q\). In a nondecreasing integer code sequence, all \(0\)'s occur before all positive codes, while all \(q\)'s occur after codes smaller than \(q\). If at least one code is strictly between \(0\) and \(q\), then all zero-phase codes before it must be \(0\) and all zero-phase codes after it must be \(q\); the full sequence is therefore uniquely determined by the output. If no such code occurs, every code is either \(0\) or \(q\), giving exactly the \(r+1\) nondecreasing sequences with a single possible \(0\)-to-\(q\) switch. Their common output is \(P^r\). The uniquely readable phase strings are therefore exactly \(0^*1^*\cdots(q-1)^*0^*\). There are \(\binom{r+q}{q}\) embeddings and precisely \(r\) repeated copies in the one exceptional fiber, so the distinct-output count is \(\binom{r+q}{q}-r\). At \(r=0\) there is one embedding and one empty remainder, consistent with every formula. \(\square\)

## Verification

Run `python3 verify_positional.py` and `python3 verify_recursion.py` from this package using the Python standard library. The former independently enumerates all \(q\)-position deletion masks, filters for subsequence \(P\), constructs residuals, and checks the complete language, all fiber multiplicities, and the formula over 36 parameter cases. The latter uses a two-branch memoized deletion recursion and a separately generated monotone-phase language over 25 parameter cases. Both checks passed with the exact results recorded in their respective text-output files. Finite tests corroborate but do not replace the all-parameter bijection and collision proof.

## Relationship to prior work

Adamson, Fleischmann and Huch (2026) introduce complement scattered factors \(C(w,u)\), give general algorithms and structural statements, and explicitly identify closed-form special cases as a direction for investigation. Their Sections 3–5 do not contain the all-alphabet phase-word classification or polynomial formula above. General algorithms can compute individual finite cases, but do not imply the displayed all-parameter expression without additional structural reasoning.

The previously published result *Binomial-tail law for complements of alternating words* fully treats the \(q=2\) special case and more general binary deletion lengths. This case is excluded from the newness claim here. *Exact embedding-multiplicity spectrum of cyclic permutation powers* counts how often an arbitrary prescribed **survivor** subsequence embeds in the source; it does not count outputs or collisions when a prescribed **deleted** subsequence is removed. *Short-deletion necklaces of permutation powers* counts output **rotation classes** from unrestricted deletion masks in a **circular** word; it does not give the distinct linear outputs left by deleting an increasing one-copy period, and its Burnside count cannot be substituted for the present formula.

## Limitations

The phase characterization requires a repeated period of pairwise distinct symbols and removal of exactly one whole period in its internal order. It does not characterize arbitrary deleted subsequences, non-permutation periods, or circular quotient outputs. The all-parameter theorem follows from a direct combinatorial proof; the executable checks test finite cases only. Searches and comparisons did not expose an equivalent all-alphabet formula, but classical shuffle-enumeration literature could contain an unindexed equivalent. No independent external audit or exhaustive global priority certification has been performed.

## References

1. Duncan Adamson, Pamela Fleischmann and Annika Huch, *(Sets of) Complement Scattered Factors*, arXiv:2603.20790, first publicly posted 2026-03-21, https://arxiv.org/html/2603.20790v1.
2. *Binomial-tail law for complements of alternating words*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-binomial-tail-law-for-complements-of-alternating-words--d7ef6cdd9c92.
3. *Exact embedding-multiplicity spectrum of cyclic permutation powers*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-embedding-multiplicity-spectrum-of-cyclic-permutation-powe--bcaf0c227997.
4. *Short-deletion necklaces of permutation powers: exact orbit counts and the first phase-wrap collision*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-short-deletion-necklaces-of-permutation-powers-exact-orbit-count--16ccfbf22eda.
