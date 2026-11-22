# A sharp ternary synthesis-reference frontier for one-deletion-correcting three-letter codes

## Finding

Let \(\Sigma=\{0,1,2\}\). In a reference-driven synthesis process, a reference word \(s\in\Sigma^T\) can synthesize exactly the length-three words that are scattered subsequences of \(s\). A code \(C\subseteq\Sigma^3\) corrects one deletion if the sets \(D_1(u)\) of distinct length-two deletion outputs are pairwise disjoint. Define
\[
F(T)=\max_{s\in\Sigma^T}\max\{|C|: C\subseteq\operatorname{Sub}_3(s),\ D_1(u)\cap D_1(v)=\varnothing\text{ for }u\ne v\}.
\]
Then, for every integer \(T\ge0\),
\[
F(T)=\begin{cases}0&0\le T\le2,\\1&3\le T\le4,\\2&T=5,\\4&6\le T\le8,\\5&T\ge9.\end{cases}
\]
The largest feasible code has five words, so the exact minimum synthesis lengths for code sizes \(M=1,2,3,4,5\) are respectively \(3,5,6,6,9\); larger sizes are impossible. Among all \(3^6=729\) labeled six-position references, **exactly twelve** synthesize a four-word one-deletion-correcting code. They are precisely the six alphabet relabelings of `012021` and the six relabelings of its reversal. Every such reference supports **exactly one** four-word correcting code, whose deletion outputs partition all nine length-two ternary words.

In contrast, the periodic reference `012012` supports at most three correcting words; its seven-position continuation `0120120` supports four. Thus optimizing the reference saves one synthesis cycle for four-word codes, even though periodic references maximize the *total* number of distinct synthesizable words without the correction constraint.

## Assumptions and scope

The alphabet symbols are labeled and word order matters. References are arbitrary finite words; the synthesis mechanism processes their letters one at a time and each strand may skip a cycle. All codewords have length exactly three, deletion removes exactly one symbol, and distinct outputs rather than deletion-position multiplicities determine correction. Codes are sets, not multisets. No insertion or substitution correction is asserted. Alphabet relabeling means a single global permutation of \(\Sigma\); reversal reverses the entire reference and each corresponding codeword.

## Proof

**1. A global five-word ceiling, with equality classification.** There are only nine two-letter deletion outputs. A constant word `aaa` has one deletion output, namely `aa`. A nonconstant three-letter word has two outputs if it has exactly two runs, or three outputs otherwise. Every nonconstant word with any repeated symbol has a diagonal output `aa` for some symbol \(a\). A two-output nonconstant word has exactly one such diagonal output.

Suppose five words had pairwise disjoint deletion sets. If there were no constants, at least ten deletion outputs would be needed. If there were one constant, the four other words would have to have exactly two outputs each, so they would require four *different* remaining diagonal outputs, whereas only two are available. If there were two constants, among three other words at least two would have exactly two outputs (otherwise more than nine outputs would be needed); they would need two different remaining diagonal outputs, whereas only one is available. Hence all three constants `000`, `111`, `222` are compulsory. The other two codewords must use three distinct letters, since any repeated-letter word has a diagonal deletion output. The six permutations of `012` split into precisely three disjoint deletion-shadow pairs, each a word paired with its reversal. Therefore there are exactly three five-word codes, and a sixth word is impossible. A reference synthesizing any five-word code must contain at least three occurrences of each alphabet symbol, so \(T\ge9\). The reference `012012012` realizes this bound using the code \(\{000,111,222,012,210\}\).

**2. Lower lengths by embedding incidence.** If two length-three words correct one deletion together, they have no common scattered length-two word. Any chosen sets of three embedding positions within a common reference therefore meet in at most one position. For two codewords, their six positions require at least five reference positions. For three codewords, inclusion-exclusion gives at least \(9-3=6\) reference positions. Thus \(F(T)=1\) for \(3\le T\le4\) and \(F(5)\le2\). The reference `01201` realizes two codewords, `011` and `120`, with disjoint deletion sets.

**3. A sharp six-position construction.** The reference `012021` synthesizes the four words
\[
C_*=\{\mathtt{002},\mathtt{011},\mathtt{120},\mathtt{221}\}.
\]
Their deletion sets are respectively
\[
\{\mathtt{00},\mathtt{02}\},\quad
\{\mathtt{01},\mathtt{11}\},\quad
\{\mathtt{10},\mathtt{12},\mathtt{20}\},\quad
\{\mathtt{21},\mathtt{22}\}.
\]
They are disjoint and together equal \(\Sigma^2\). Four words are thus achievable at \(T=6\). By the global five-word classification, five are impossible for every \(T<9\). Monotonicity supplies the full frontier.

**4. Rigidity of six-position realizations.** Consider any four correcting codewords with embeddings \(E_1,E_2,E_3,E_4\), each a three-element subset of the six reference positions. Each \(E_i\cap E_j\) has size at most one. Let \(d_p\) be the number of embedding sets containing position \(p\). We have \(\sum_{p=1}^6d_p=12\), while
\[
6\ \le\ \sum_{p=1}^6\binom{d_p}{2}\ =\ \sum_{1\le i<j\le4}|E_i\cap E_j|\ \le\ 6.
\]
The first inequality follows from Cauchy-Schwarz and equality forces every \(d_p=2\). Consequently each pair of codewords shares exactly one embedding position, and the six positions carry the six edges of \(K_4\), with each codeword occupying its incident three edges.

To complete the *labeled* reference classification, perform the finite exhaustion described below: enumerate every ternary reference of length six, every length-three subsequence, and every compatible four-word set, comparing their distinct one-deletion output sets. The `verify_global.py` certificate enumerates all globally compatible codes first and tests embeddings by a greedy subsequence scan. Independently, `verify_reference.py` generates each reference's subsequences from all index triples and computes the exact compatible-code optimum by memoized graph search. Both find precisely the same twelve references. Exactly one four-codeword family is found for each, and each family's deletion sets partition \(\Sigma^2\). Directly comparing the twelve strings with the orbit of `012021` under six alphabet permutations and reversal proves the stated characterization. This is a finite exhaustive argument, not an extrapolation from samples.

**5. Periodic-reference comparison.** The two independent searches give a maximum of three for `012012` and four for `0120120`. The general rigidity classification also excludes `012012` at length six, as it is not a relabeling or reversal of `012021`. Therefore its shortest prefix supporting four codewords has length seven, versus six for an unrestricted reference.

## Verification

Run `python verify_global.py` and `python verify_reference.py` with Python 3 standard library, in the directory containing the files. The first enumerates all independent sets through five words in the global 27-word deletion graph, tests all \(3^T\) references for \(3\le T\le9\) by greedy embeddings, and checks the optimizer orbit. The second forms all distinct three-letter subsequences directly for each reference and recursively maximizes the code size using nine-bit deletion-output masks; it asserts the independent exact distributions for every \(T\) from three through nine. The two programs agree on the \(T=6\) capacity histogram \((39,336,342,12)\) at capacities one through four, on twelve and only twelve optimizers, and on all six preceding and subsequent finite-length distributions. The all-length conclusion follows from the proof, not merely from the finite runs.

## Relationship to prior work

Li, Yu and Ge (first publicly posted November 10, 2026, arXiv:2611.13434) define precisely the arbitrary-reference synthesis-time optimization with deletion correction, give general finite-length bounds and asymptotic results, and leave finite exact frontiers of this kind unstated in the inspected text. Chrisnata, Kiah and Pham (2023, arXiv:2305.07274) study deletion-correcting codes under a *fixed periodic reference*; their assumptions do not optimize over nonperiodic references. The unrestricted result attributed to Lenz et al. (2020) concerns the number of subsequences of a reference and does not imply that the same reference maximizes the size of a deletion-correcting subcode. The present finding gives a concrete exact separation. Previously published short-length deletion-code counts without reference constraints address a different optimization problem; no novelty is claimed for the basic deletion-shadow criterion or the existence of traditional deletion codes.

## Limitations

This is an exact result only for a ternary alphabet and length-three codewords. The generalization to longer words or other alphabets is not proved. Independent human assessment and exhaustive priority verification have not been performed. The finite classification is supported by complete executable enumerations and a structural incidence reduction; the enumerations are not themselves an infinite theorem.

## References

1. Y. Li, W. Yu and G. Ge, *Minimum Synthesis Time for Single-Deletion Correcting Codes of Prescribed Size*, arXiv:2611.13434, first posted 2026-11-10. https://arxiv.org/abs/2611.13434
2. J. Chrisnata, H. M. Kiah and V. L. P. Pham, *Deletion Correcting Codes for Efficient DNA Synthesis*, arXiv:2305.07274, first posted 2023-05-12. https://arxiv.org/abs/2305.07274
3. A. Lenz, Y. Liu, C. Rashtchian, P. H. Siegel, A. Wachter-Zeh and E. Yaakobi, *Coding for Efficient DNA Synthesis*, ISIT 2020, DOI:10.1109/ISIT44484.2020.9174272.
