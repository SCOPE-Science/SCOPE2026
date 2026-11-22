# Two-deletion confusability of six-symbol palindromes: an exact edge law and quadratic code capacity

## Finding
Let \(\Sigma\) be a labeled alphabet of size \(q\ge2\). For each ordered triple \((a,b,c)\in\Sigma^3\), let \(P(a,b,c)=abccba\). Write \(D_2(w)\) for the set of distinct words obtained by deleting exactly two arbitrary positions of \(w\). Define a graph \(G_q\) with these \(q^3\) palindromes as vertices; two *distinct* vertices are adjacent precisely when their deletion shadows intersect.

**Theorem (all-alphabet edge and degree law).** The exact number of unordered edges is
\[
 |E(G_q)|=\frac{q^2(q-1)(9q-8)}2.
\]
The complete degree distribution is given by the following equality types of the three positions in \((a,b,c)\). The alphabet symbols in each pattern are abstract and differing letters denote different symbols.

| Triple equality type | Number of vertices | Degree |
|---|---|---|
| \(aaa\) | \(q\) | \(3q-3\) |
| \(aab\) | \(q(q-1)\) | \(6q-6\) |
| \(aba\) | \(q(q-1)\) | \(9q-12\) |
| \(abb\) | \(q(q-1)\) | \(6q-7\) |
| \(abc\) | \(q(q-1)(q-2)\) | \(9q-11\) |

Let \(A_q\) be the largest codebook consisting of six-symbol palindromes that corrects **exactly two arbitrary deletions**. For every \(q\ge2\),
\[
\left\lceil\frac{q^4}{9q^2-16q+8}\right\rceil\le A_q\le q^2.
\]
Furthermore, there is an explicit greedy construction giving at least \(\lceil q(q-1)/18\rceil\) mutually two-deletion-distinguishable palindromes for \(q\ge3\). Consequently \(A_q=\Theta(q^2)\) as alphabet size grows, with fixed source length six. No claim of an exact formula for \(A_q\) is made.

## Assumptions and scope
All words have a common fixed length of six and are *ordinary* reversal palindromes, without alphabet complementation. Two positions are removed, in arbitrary nonadjacent or adjacent locations, and resulting length-four outputs are deduplicated. Codeword pairs are unordered for edge counting; all codebooks are labeled by their actual alphabet, not quotiented by any symmetry. The alphabet size is a variable integer, not a word-length asymptotic. The error-correcting criterion is pairwise disjoint deletion shadows.

## Proof
**1. The all-alphabet edge certificate.** For any two length-six words, their two-deletion shadows intersect if and only if their longest common scattered subsequence has length at least four. Since \(P(a,b,c)\) uses each of \(a,b,c\) twice, the relation between \(P(a,b,c)\) and \(P(d,e,f)\) depends only on the *equality partition* of their six formal variables \((a,b,c,d,e,f)\).

Every such partition has exactly one restricted-growth encoding \((r_1,\ldots,r_6)\), where \(r_1=0\) and \(0\le r_j\le1+\max_{i<j}r_i\). The complete set has Bell number \(B_6=203\) members. The standalone standard-library checker `checks/verify_patterns.py` generates **all 203** recursively, forms the corresponding pair of six-letter palindromes, and evaluates a standard dynamic-programming longest-common-subsequence recurrence (equivalently, existence of a common four-letter deletion output). It rejects identical source triples. Of these 203 equality partitions, the counts of confusable *ordered* distinct source pairs using precisely \(r\) different alphabet symbols are exactly
\[
 (c_2,c_3,c_4)=(20,37,9),\qquad c_1=c_5=c_6=0.
\]
No sampling or finite-alphabet extrapolation occurs: these 203 partitions classify **every** possible pair over **every** finite alphabet. For each qualifying partition using \(r\) distinct labels, there are exactly \((q)_{\underline r}=q(q-1)\cdots(q-r+1)\) injective label assignments to a \(q\)-letter alphabet. The number of ordered edges is therefore
\[
20(q)_{\underline2}+37(q)_{\underline3}+9(q)_{\underline4}
=q^2(q-1)(9q-8).
\]
Swapping the two different source words fixes no ordered pair, so division by two establishes the edge formula. The executable enumerator is a complete finite proof certificate for the abstract six-variable partition claim; its explicit recursion and LCS algorithm are included, not merely their output.

**2. The degree spectrum.** The type of \((a,b,c)\) is preserved under every alphabet relabeling. A neighboring triple \((d,e,f)\) cannot contain two symbols absent from \(\{a,b,c\}\): at most one letter of the neighbor then belongs to the source's symbol set, and its palindrome contains that letter in at most two positions. Hence a common scattered subsequence has length at most two, below the four required. Thus, for a fixed source triple, the neighbor count is an *affine function of \(q\)*: neighbors using no new symbol contribute a constant, and the templates using one new symbol can each be assigned any of the \(q-r\) fresh letters, where \(r\) is the number of source letters. Exhaustive direct deletion-shadow comparison for representative source triples over alphabets of sizes \(r\) and \(r+1\) determines the two integer coefficients. The five base/new-symbol values are respectively \((0,3)\) for \(aaa\), \((6,6)\) for \(aab\), \((6,9)\) for \(aba\), \((5,6)\) for \(abb\), and \((16,9)\) for \(abc\). Therefore their degrees are exactly those in the table for every \(q\), with nonexistent types contributing zero vertices. Independently summing degree times multiplicity yields \(2|E(G_q)|\), agreeing with part 1.

**3. Quadratic bounds for correcting codes.** Holding the first two letters \((a,b)\) fixed gives a clique of size \(q\): all \(P(a,b,c)\) share the four-letter deletion output \(abba\) (delete positions three and four). The \(q^2\) distinct cliques partition the graph, forcing \(A_q\le q^2\).

For any finite graph with degrees \(d_v\), randomly order the vertices and select those preceding all of their neighbors. The selection is independent and has expectation \(\sum_v1/(d_v+1)\). By the harmonic-arithmetic mean inequality it is at least \(|V|^2/(|V|+2|E|)\). Substituting \(|V|=q^3\) and the proven edge formula gives \(A_q\ge q^4/(9q^2-16q+8)\); integrality supplies the ceiling.

For an explicit constructive lower bound, greedily choose maximal three-element subsets of the alphabet with no shared two-element subset. Each chosen triple contributes one palindromic codeword. Two chosen triples intersect in at most one alphabet symbol, which appears twice in each corresponding palindrome, so they share no four-letter subsequence and their deletion shadows are disjoint. Every unchosen three-subset must contain one of the three pairs already used by a chosen triple. A selected triple blocks at most \(3(q-2)\) three-subsets; there are \(\binom q3\) total. Hence at least \(\binom q3/[3(q-2)]=q(q-1)/18\) triples are selected. Combining the upper and either lower bound proves quadratic order.

## Verification
Run `python3 checks/verify_patterns.py` and `python3 checks/verify_direct.py` using Python 3 and only its standard library. The first program traverses all 203 abstract partitions, independently evaluates the dynamic-programming longest-common-subsequence condition, confirms the support-profile \((20,37,9)\), and checks the resulting polynomial for alphabet sizes 1 through 20. The second program constructs every actual word and each of its fifteen deletion-position pairs, compares the resulting distinct length-four shadows for all alphabet sizes 1 through 7, and checks every vertex degree and edge count. It independently verifies greedy pair packing through alphabet size 30 and direct codeword shadow disjointness through alphabet size 10. The two observed run markers were `PATTERN_OK` and `DIRECT_OK`. Complete abstract partition enumeration, not the finite tests for selected alphabet sizes, supplies the all-alphabet proof.

## Relationship to prior work
Kulkarni and Kiyavash's 2012 general multiple-deletion hypergraph treatment already provides the constrained-source modeling framework; this theorem does not claim to invent that framework or the standard random-order independent-set inequality. Published palindrome-specific work on **one ordinary deletion** gives different conflict graphs: a length-six palindrome code correcting one deletion may include every palindrome, whereas two-deletion shadows intersect heavily. Published finite results for palindromic **block** deletions concern a different error mechanism on an unrestricted source. Published two-deletion reconstruction equality-pattern results concern *maximum common outputs among input pairs that are already one-deletion separated*, rather than all confusable pairs within the palindrome-induced source. A prior finite balanced-ternary six-word deletion-code result includes some of these sources but neither gives this whole \(q\)-parameter edge and degree distribution nor implies the quadratic all-alphabet capacity order.

## Limitations
The graph statistics are exact for every alphabet but only at source length six and exactly two arbitrary deletions. The code-capacity result establishes its order in \(q\) with explicit finite bounds, **not** an exact optimum or equality classification. The exhaustive proof assumes the deterministic source programs are executed as supplied; independent external audit has not been performed. Equivalent computations in unindexed literature may exist. No assertion about genomic error distributions, physical sequencing, or increasing blocklength is made.

## References
1. A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128 (first public 2012-11-13), https://arxiv.org/abs/1211.3128 .
2. D. Cullina, A. A. Kulkarni and N. Kiyavash, *Two Approaches to the Construction of Deletion Correcting Codes: Weight Partitioning and Optimal Colorings*, arXiv:1211.4056 (first public 2012-11-16), https://arxiv.org/abs/1211.4056 .
3. *Exact one-deletion confusability and capacity of palindromic codes*, publicly accessible research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-one-deletion-confusability-and-capacity-of-palindromic-cod--9646637bbf2e .
4. *A binomial-tree model for binary palindromic single-deletion codes*, publicly accessible research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-binomial-tree-model-for-binary-palindromic-single-deletion-cod--3c7b3453f9ef .
5. *Complete equality patterns for short nonbinary two-deletion reconstruction*, publicly accessible research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-complete-equality-patterns-for-short-nonbinary-two-deletion-reco--8cefff0252dd .
6. *Exact binary length-six palindromic-duplication and deletion optima*, publicly accessible research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-binary-length-6-palindromic-duplication-and-deletion-optim--d41a86ca777b .
