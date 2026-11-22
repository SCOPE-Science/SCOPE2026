# Sharp one-insertion sphere volumes of layered set partitions

## Finding
Let \(P\) be a partition of \([n]\), represented by its canonical restricted-growth word \(w=0^{a_1}1^{a_2}\cdots(k-1)^{a_k}\), with \(k\ge1\), positive integers \(a_i\), and \(\sum_i a_i=n\). Such partitions are called **layered**. Form \(\mathcal I(P)\) by inserting one new indexed element into any of the \(n+1\) linear gaps and putting that element either into any existing block or into a newly created singleton block. Standardize the names of the resulting blocks by first occurrence. Equal resulting partitions are counted only once, and the output partition need not be layered.

Let \(L_1,\ldots,L_h\) be the lengths of the maximal consecutive chains of indices \(i\) for which \(a_i=1\); the empty list is allowed. Then the exact one-insertion sphere volume is
\[
|\mathcal I(P)|=(n+1)(k+1)-n-\sum_{j=1}^{h}\binom{L_j+1}{2}.
\]

The extrema and number of extremizers have an explicit form for every \(1\le k\le n\). Write \(B=(n+1)(k+1)-n\), \(t=\min\{k,n-k\}\), \(s=k-t\), \(\ell=t+1\), and \(s=\ell a+b\) with \(0\le b<\ell\). Set
\[
T_{\min}=(\ell-b)\binom{a+1}{2}+b\binom{a+2}{2},\qquad
T_{\max}=\begin{cases}\binom{k+1}{2},&n=k,\\\binom{k}{2},&n>k.\end{cases}
\]
Then
\[
\min_P|\mathcal I(P)|=B-T_{\max},\qquad
\max_P|\mathcal I(P)|=B-T_{\min},
\]
where \(P\) ranges over all layered \(k\)-block partitions of \([n]\). When \(n=k\), both extrema are uniquely attained by the all-singleton partition. When \(n>k\), the minimum is attained by exactly two compositions (one if \(k=1\)): one nonsingleton block of size \(n-k+1\) at either endpoint and all other blocks singleton. For \(k<n<2k\), the maximum is attained by exactly \(\binom{t+1}{b}\) compositions: all \(t=n-k\) nonsingleton blocks have size two, and the singleton-chain lengths in their \(t+1\) intervening or endpoint gaps are \(a\) or \(a+1\) (exactly \(b\) gaps of the latter size). For \(n\ge2k\), the maximum is attained by precisely the \(\binom{n-k-1}{k-1}\) compositions with all parts at least two.

For example, the compositions \((1,1,2)\) and \((1,2,1)\) both have four elements and three blocks, but have insertion volumes \(13\) and \(14\), respectively: the arrangement of singleton blocks changes synchronization ambiguity.

## Assumptions and scope
A partition's blocks are unlabeled, although their canonical word labels are assigned in order of the blocks' first occurrences. Insertions act on indexed linear positions and preserve the order and existing block equivalences of the original \(n\) elements; new blocks may be created. All output partitions of \([n+1]\) are allowed. The theorem holds for every integer \(n\ge1\), \(1\le k\le n\), every positive composition \((a_1,\ldots,a_k)\), including \(n=k\), \(k=1\), and empty singleton chains. Distinctness means equality of final set partitions, not equality of insertion-site histories or of numerical block labels.

## Proof
**1. Partition the histories by block count.** There are \((n+1)(k+1)\) raw histories: one of \(n+1\) gaps, and one of \(k\) existing blocks or a new singleton block. Outputs from the two classes have respectively \(k\) and \(k+1\) blocks and cannot coincide.

**2. New-singleton histories.** If one inserts a new singleton at a gap, the only ambiguity in its position arises from crossing a pre-existing singleton block. Indeed, after removing any singleton element from the resulting partition one recovers \(P\) precisely when that element is a member of a consecutive chain of singleton blocks in the original layered composition. A chain of \(L\) singleton blocks thus makes its \(L+1\) adjacent gaps produce just one output, losing \(L\) raw histories. Gaps not linked by such a chain give distinct outputs, because at least one old block of size \(\ge2\) separates them. With \(s_0=\sum_j L_j\) singleton blocks, this class has \(n+1-s_0\) outputs.

**3. Existing-block histories.** Inserting an element into its block's original interval makes an entirely layered output, and there are exactly \(k\) such outputs (increase the corresponding part \(a_i\) by one). The total number of histories leading to these \(k\) outputs is \(\sum_i(a_i+1)=n+k\). Consequently \((n+1)k-(n+k)=(k-1)n\) histories yield a nonlayered output. Such an output has exactly one noncontiguous block. All blocks other than this exceptional block remain contiguous, because only one new position was inserted.

If a nonlayered output has two different deletion positions whose removal returns the same layered source \(P\), both positions belong to the exceptional block: deleting any other block cannot reconnect that exceptional block. The exceptional block must consist of exactly two singleton occurrences; otherwise deleting either position leaves it noncontiguous. Furthermore, all blocks between its two occurrences must be singletons, for the opposite deletion to give exactly the same layered source after restandardization. Hence such a double history corresponds bijectively to a choice of two distinct singleton blocks in one maximal consecutive singleton chain of \(P\). Conversely, any pair in one such chain produces exactly one nonlayered output with two histories, obtained by moving either singleton label across the other intervening singleton blocks. No nonlayered output has three histories, because its exceptional block has only two occurrences. Therefore nonlayered old-block outputs number \((k-1)n-\sum_j\binom{L_j}{2}\); combining them with the \(k\) layered outputs gives \(k+(k-1)n-\sum_j\binom{L_j}{2}\) old-block outputs.

Adding step 2 yields
\[
(n+1-s_0)+k+(k-1)n-\sum_j\binom{L_j}{2}=(n+1)(k+1)-n-\sum_j\binom{L_j+1}{2}.
\]

**4. Optimize the singleton-chain penalty.** Each nonsingleton block requires at least one length unit beyond the mandatory one per block, so their count is at most \(t=\min\{k,n-k\}\). A chain of \(L\) singleton blocks contributes the increasing convex function \(\binom{L+1}{2}\). To minimize the penalty, use the largest possible number \(t\) of nonsingleton separators: turning an available singleton into a nonsingleton reduces both the singleton count and the penalty, while never increasing it. When \(n<2k\), those \(t=n-k\) blocks must each have size two, and the \(s=k-t\) singleton blocks occupy \(t+1\) gaps. Discrete convexity minimizes \(\sum\binom{L+1}{2}\) precisely when all gap lengths differ by at most one, giving \(T_{\min}\) and \(\binom{t+1}{b}\) choices. When \(n\ge2k\), take no singleton blocks; distributing \(n-2k\) further elements among \(k\) positive augmented sizes gives \(\binom{n-k-1}{k-1}\) compositions. When \(n=k\), no nonsingleton separator is possible.

To maximize the penalty for \(n>k\), at least one block must be nonsingleton and at most \(k-1\) singleton blocks remain. Since \(\binom{x+y+1}{2}>\binom{x+1}{2}+\binom{y+1}{2}\) for positive \(x,y\), all \(k-1\) singleton blocks must be in a single consecutive chain. The unique nonsingleton block must therefore be at one endpoint, and takes all excess length \(n-k\). This gives \(T_{\max}=\binom{k}{2}\) and the claimed two endpoint arrangements (one for \(k=1\)); for \(n=k\), the unique composition consists wholly of singleton blocks. The extremal formulas and counts follow.

## Verification
Run `python3 check.py` from this package. It enumerates all positive compositions \((a_1,\ldots,a_k)\) for each \(1\le k\le n\le10\), constructs all restandardized insertion outputs directly, and checks the closed formula and both extrema and their attainment counts. Separately it enumerates all set partitions of \([n+1]\) and deletes each of their \(n+1\) positions for \(n\le7\), an independent reverse-direction check. Observed output: `VERIFY_OK forward_layered_cases 1023 extremal_strata 55 independent_reverse_cases 127 max_n 10`. The infinite parameter range is proved in the preceding steps, not inferred from these finite tests.

## Relationship to prior work
Sagan's *Pattern Avoidance in Set Partitions* (2006) used restricted-growth presentations and studied avoidance classes and avoidance classes; the layered property is standard set-partition combinatorics. Dahlberg and coauthors (2015) provide another structural account of layered set partitions and their statistics. Bean, Bell and Ollson (2026) study horizontal and vertical insertion encodings and regularity of restricted-growth languages, a different operation from the full one-element superpartition sphere here. A pre-existing general one-deletion partition-read collision criterion classifies when two deletion positions give identical outputs; this is acknowledged as a broader structural antecedent and is not claimed as new. The present claim is instead the exact source-conditional inverse sphere volume together with sharp fixed-\((n,k)\) extrema and enumerations of all extremizers. These evaluations are not asserted in the named sources. Search results cannot exclude unindexed equivalent formulas.

## Limitations
Only one insertion into a layered source is treated; outputs may be nonlayered. We do not claim a code capacity, arbitrary multiple-insertion formula, or a theorem for all unrestricted source partitions. The class of source partitions is combinatorially structured and the result is a finite-block exact count, not an error-correction guarantee. Earlier undocumented equivalent evaluations could affect priority. The included verifier is finite and does not independently prove the all-parameter theorem.

## References
1. Bruce E. Sagan, *Pattern Avoidance in Set Partitions*, arXiv:math/0604292, originally posted 2006-04-12. https://arxiv.org/abs/math/0604292
2. Samantha Dahlberg et al., *Set partition patterns and statistics*, arXiv:1502.00056, originally posted 2015. https://arxiv.org/abs/1502.00056
3. Christian Bean, Paul C. Bell, Abigail Ollson, *The Insertion Encoding of Restricted Growth Functions*, Annals of Combinatorics, 2026. https://doi.org/10.1007/s00026-026-00832-y
