# Exact shortest palindromic subsequence-universal words over arbitrary alphabets

## Finding

For every alphabet \(\Sigma\) of \(q\ge2\) distinct labeled symbols and every integer \(k\ge1\), let \(L(q,k)\) be the minimum length of a palindrome that contains all \(q^k\) words of length \(k\) over \(\Sigma\) as **scattered subsequences**. Let \(N(q,k)\) count such optimal labeled words. Then
\[
L(q,k)=\begin{cases}qk,&k\text{ even},\\ q(k+1)-1,&k\text{ odd},\end{cases}
\qquad
N(q,k)=(q!)^{\lceil k/2\rceil}.
\]
The following characterizes *every* optimal word. If \(k=2m\), it is precisely
\[
P_1P_2\cdots P_m P_m^{\mathrm R}\cdots P_2^{\mathrm R}P_1^{\mathrm R},
\]
where each \(P_i\) is an arbitrary permutation of \(\Sigma\). If \(k=2m+1\), it is precisely
\[
P_1\cdots P_m\,VcV^{\mathrm R}\,P_m^{\mathrm R}\cdots P_1^{\mathrm R},
\]
where \(c\in\Sigma\) and \(V\) is a permutation of \(\Sigma\setminus\{c\}\). Here \(X^{\mathrm R}\) denotes reversal of the finite word \(X\). The concatenated blocks need not all be distinct.

## Assumptions and scope

A word \(u=u_1\cdots u_k\) is a scattered subsequence of \(w=w_1\cdots w_n\) if some indices \(1\le i_1<\cdots<i_k\le n\) satisfy \(u_j=w_{i_j}\) for every \(j\). A word is \(k\)-subsequence-universal if it contains every member of \(\Sigma^k\) as a scattered subsequence. A palindrome satisfies \(w=w^{\mathrm R}\), **not** the reverse-complement condition used for nucleic-acid codes. The alphabet is labeled: relabelings produce different words when the strings differ. The theorem covers all \(q\ge2\) and \(k\ge1\), without a bound on either parameter.

## Proof

**1. Consecutive alphabet-block lemma.** A word is \(k\)-subsequence-universal if and only if it admits a partition into \(k\) consecutive factors, each containing every letter of \(\Sigma\), possibly followed by a residual suffix. Sufficiency is immediate: embed the \(j\)-th required letter in the \(j\)-th block. For necessity, let \(U\) be the shortest nonempty prefix containing the complete alphabet and let \(a\) be its final letter. By minimality, \(a\) has no occurrence in the portion of the word preceding the last position of \(U\). If the word is \(k\)-universal, then for any \((k-1)\)-letter target \(v\), the target \(av\) embeds in the word. Every occurrence of the first \(a\) used by an embedding lies at or beyond the last position of \(U\), so \(v\) embeds into the suffix following \(U\). Thus that suffix is \((k-1)\)-universal. Repeat inductively. The shortest successive complete-alphabet blocks obtained this way will be called *greedy blocks*. In particular every universal word has at least \(k\) occurrences of each letter and length at least \(qk\).

**2. Lower bounds from symmetry.** Every palindrome has an even number of occurrences of every letter except possibly the central letter, which alone may have odd multiplicity. If \(k\) is even, the block lemma gives \(L(q,k)\ge qk\). If \(k\) is odd, universality requires at least \(k\) occurrences of each letter. In an even-length palindrome each letter then occurs at least \(k+1\) times. In an odd-length palindrome the central letter may occur \(k\) times, but each of the remaining \(q-1\) letters occurs at least \(k+1\) times. Hence any admissible palindrome has length at least \(q(k+1)-1\).

**3. Constructions.** For even \(k=2m\), choose any \(m\) permutations \(P_1,\dots,P_m\) of \(\Sigma\) and concatenate them with their mirror-image sequence of reversed permutations. This is a palindrome containing \(2m\) consecutive complete-alphabet blocks and has length \(2mq\). For odd \(k=2m+1\), choose the same outer blocks, any \(c\in\Sigma\), and a permutation \(V\) of the other \(q-1\) symbols; insert the palindrome \(VcV^{\mathrm R}\) centrally. Its first \(q\) symbols \(Vc\) already contain every letter, so there are \(2m+1\) complete-alphabet blocks, and its length is \(2mq+2q-1=q(k+1)-1\). These constructions meet the lower bounds.

**4. Necessity when \(k\) is even.** If a word reaches length \(qk\), the block lemma partitions it into exactly \(k\) length-\(q\) blocks. Each block is a permutation. Palindromicity forces the second half of the blocks to be the reversed first half, in reverse order. Hence precisely the stated even forms occur.

**5. Necessity when \(k\) is odd.** Let \(k=2m+1\) and let \(w\) be a shortest admissible palindrome. Choose any partition of \(w\) into \(2m+1\) consecutive full-alphabet factors and perhaps a residual suffix, as the lemma permits. From the left, remove the first \(m\) greedy full-alphabet blocks, of total length \(s\). From the right, remove the first \(m\) greedy full-alphabet blocks constructed from the reversed word. Because \(w\) is palindromic, these have the same block lengths as the left greedy blocks and thus total length \(s\). Greedy block boundaries reach no farther inward than the corresponding boundaries of *any* consecutive full-alphabet partition: by induction, each greedy block ends at the earliest position at which the next complete alphabet is available. The analogous assertion holds from the right. Therefore the remaining central factor contains the full \((m+1)\)-st alphabet block of the chosen partition and hence contains every symbol. It is a palindrome because equal-length prefix and suffix were removed. Each greedy block has length at least \(q\), so \(s\ge mq\). Any palindrome containing all \(q\) distinct letters has length at least \(2q-1\): all symbols except its possible central symbol must occur in mirrored pairs. Consequently
\[
q(k+1)-1=|w|=2s+|\mathrm{center}|\ge 2mq+(2q-1)=q(k+1)-1.
\]
Equality throughout forces all \(m\) left greedy blocks to have length \(q\), making each a permutation, and forces the center to have length \(2q-1\). The center must consist of one occurrence of the central symbol \(c\) and exactly two of every other symbol, once on each side. Its left half is therefore a permutation \(V\) of \(\Sigma\setminus\{c\}\), and it is \(VcV^{\mathrm R}\). This establishes the claimed odd classification, including \(m=0\).

**6. Counting without duplication.** For even \(k=2m\), the first \(m\) consecutive length-\(q\) blocks are uniquely readable from the word and each has \(q!\) possibilities. For odd \(k=2m+1\), those same \(m\) blocks and the central length-\((2q-1)\) palindrome are uniquely readable; the center has exactly \(q(q-1)!=q!\) choices. Distinct choices give distinct labeled words. In either parity the total is \((q!)^{\lceil k/2\rceil}\), as claimed. \(\square\)

## Verification

The accompanying standalone Python file `verify_palindromic_universal.py` enumerates **all palindromes** over the stated small alphabets, checks every candidate against **all subsequences of length \(k\)** by direct index-order embedding, checks that no shorter palindrome is universal, and compares the exact set of minimum-length palindromes with independently generated normal forms. The finite verification ranges are \(q=2, 1\le k\le7\); \(q=3, 1\le k\le5\); \(q=4, 1\le k\le3\); \(q=5, 1\le k\le2\). Running `python3 verify_palindromic_universal.py` prints one PASS per pair and `ALL_CHECKS_PASS`. These experiments supplement the proof and do not establish the unbounded statements alone.

## Relationship to prior work

The general shortest common supersequence problem concerns arbitrary finite input sets; Lagoutte and Tavenas [1] prove complexity results for restricted instances, rather than a reversal-constrained all-word instance. The all-permutation supersequence problem in Uznański [2] has a *different input family*, not all \(k\)-letter strings [2]. Adamson [3] counts, ranks, and enumerates **all** subsequence-universal words at specified length by dynamic programming; its counting recurrence and the standard arch characterization do not state the palindromic optimum, all minimizers, or their closed cardinality. Adamson et al. [4] establish automata-theoretic universality algorithms, and Fleischmann et al. [5] treat Simon congruence and factorization, but the respective main results do not provide the claimed exact reversal-constrained classification. The greedy arch criterion itself is **not new**; the result concerns its exact interaction with palindrome symmetry. Literature comparisons are limited to the checked materials, so prior independent discovery elsewhere remains possible.

## Limitations

No statement is made about shortest super**strings** (contiguous occurrences), arbitrary target sets, reverse-complement palindromes, or the number of non-optimal universal palindromes. The proof is elementary and requires no external computation. The bibliographic search does not certify global priority; the title and theorem should receive independent literature review before attribution or publication.

## References

[1] A. Lagoutte and S. Tavenas, *The complexity of Shortest Common Supersequence for inputs with no identical consecutive letters*, arXiv:1309.0422v1 (first posted 2013-09-02; inspected open full text v2), https://arxiv.org/abs/1309.0422 .

[2] P. Uznański, *All Permutations Supersequence is coNP-complete*, arXiv:1506.05079v1 (2015), https://arxiv.org/abs/1506.05079 .

[3] D. Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583v1 (2023), https://arxiv.org/abs/2304.04583 .

[4] D. Adamson et al., *k-Universality of Regular Languages*, arXiv:2311.10658v1 (2023), https://arxiv.org/abs/2311.10658 .

[5] P. Fleischmann et al., *\(\alpha\)–\(\beta\)-Factorization and the Binary Case of Simon's Congruence*, arXiv:2306.14192v3 (2023), https://arxiv.org/abs/2306.14192 .
