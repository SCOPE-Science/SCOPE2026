# Unique shortest two-arch extremizers for absent subsequences
## Finding
Let \(\Sigma\) be an alphabet of size \(\sigma\ge4\). Among all shortest words \(w\) with universality index
\[
\iota(w)=2
\]
that maximize the number of absent subsequences of length \(3\), the complete equality class is
\[
w=P\,P^R,
\]
where \(P\) is an arbitrary permutation of \(\Sigma\).

Consequently there are exactly
\[
\sigma!
\]
labeled shortest extremizers, and they form one class under relabeling of the alphabet.

The known extremal construction \(P P^R\) minimizes the number of existing subsequences simultaneously at every length. Therefore the same classification also shows that \(P P^R\) is the unique shortest simultaneous extremizer, up to relabeling, when the universality index is \(2\).

## Assumptions and scope
A subsequence is obtained by deleting letters while preserving their relative order. The universality index \(\iota(w)\) is the largest integer \(r\) for which every word of length \(r\) over \(\Sigma\) occurs as a subsequence of \(w\).

A word with \(\iota(w)=2\) has two complete arches in its arch factorization. Each arch contains every alphabet symbol, so every such word has length at least \(2\sigma\). At the shortest possible length \(2\sigma\), the word has empty rest and both arches are permutations of \(\Sigma\). Thus every shortest candidate has the form \(P Q\) for two permutations \(P,Q\).

Prior work proves that the alternating construction \(P P^R\) has the fewest existing subsequences, equivalently the most absent subsequences, for every length. The issue settled here is the equality classification at shortest length.

## Proof
Relabel the alphabet according to the first arch, so
\[
P=0\,1\,\cdots\,(\sigma-1).
\]
Write the second arch as a permutation \(Q\).

Every length-\(3\) subsequence of \(P Q\) uses either exactly two or exactly three distinct symbols, since each symbol occurs only twice.

First fix a pair \(a<b\). If \(b\) precedes \(a\) in \(Q\), exactly three length-\(3\) subsequences supported on \(\{a,b\}\) occur:
\[
aba,\qquad abb,\qquad bba.
\]
If \(a\) precedes \(b\) in \(Q\), exactly four occur:
\[
aab,\qquad aba,\qquad abb,\qquad bab.
\]
Let
\[
A(Q)=|\{(a,b):a<b\text{ and }a\text{ precedes }b\text{ in }Q\}|.
\]
The total contribution from two-symbol supports is therefore
\[
3\binom{\sigma}{2}+A(Q).
\]

Now fix three symbols \(a<b<c\). Restrict \(Q\) to these symbols. A direct six-case check gives five distinct length-\(3\) permutations when the restricted order is
\[
abc,\quad acb,\quad bac,
\]
and four when it is
\[
bca,\quad cab,\quad cba.
\]
Let \(E(Q)\) count the three-element subsets whose restricted order belongs to the first group. The contribution from three-symbol supports is
\[
4\binom{\sigma}{3}+E(Q).
\]

Hence the exact count is
\[
|\operatorname{ScatFact}_3(PQ)|
=
3\binom{\sigma}{2}
+
A(Q)
+
4\binom{\sigma}{3}
+
E(Q).
\]

Both \(A(Q)\) and \(E(Q)\) are nonnegative. The minimum possible value is therefore at least
\[
3\binom{\sigma}{2}+4\binom{\sigma}{3}.
\]
For \(Q=P^R\), every pair is in decreasing order and every triple has restricted order \(cba\), so
\[
A(P^R)=E(P^R)=0,
\]
and the lower bound is attained.

Conversely, if \(Q\neq P^R\), then \(Q\) is not decreasing. Thus some pair \(a<b\) occurs in increasing order in \(Q\), giving
\[
A(Q)\ge1.
\]
Therefore
\[
|\operatorname{ScatFact}_3(PQ)|
>
|\operatorname{ScatFact}_3(PP^R)|.
\]
So the reverse second arch is the unique minimizer after the first arch is fixed.

Undoing the alphabet relabeling, the shortest extremizers are exactly \(P P^R\). There is one for each of the \(\sigma!\) permutations \(P\), and all lie in one relabeling class.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier first reconstructs the two local counting tables used in the proof. It then exhausts every second permutation after normalizing the first arch for all alphabet sizes
\[
2\le\sigma\le8,
\]
checks the exact formula
\[
3\binom{\sigma}{2}+A(Q)+4\binom{\sigma}{3}+E(Q),
\]
and confirms that the reverse permutation is the unique minimizer.

As an independent labeled check, it exhausts all ordered pairs of permutation arches for \(\sigma=4\) and \(\sigma=5\), recovering exactly \(\sigma!\) extremizers and verifying that every one is \(P P^R\).

The finite checks are supplementary. The infinite classification follows from the pair/triple support decomposition above.

## Relationship to prior work
Adamson, Fleischmann, Huch, Manea, Sarnighausen-Cahn, and Wiedenhöft prove that alternating permutation arches minimize the number of existing subsequences, and hence maximize absent subsequences, for every subsequence length at fixed universality index. Their first public version gives this construction as Theorem 29; the revised version states it as Theorem 4.1.

The revised source explicitly notes that its arguments do not exclude other shortest words with the same extremal counts. It gives the special case \(\iota=2,\sigma=3\) as a table where only the reversed second arch is simultaneously extremal. The present result proves the equality classification for every \(\sigma\ge4\) when \(\iota=2\).

Earlier shortest-absent-subsequence work and exact count formulas determine the extremal value at length \(3\), but do not imply which shortest words attain equality for general alphabet size. The binary equality case is also known separately. The new statement is the infinite equality classification beyond those small cases.

Targeted searches for uniqueness of the alternating-arch extremizer, two-permutation-arch equality cases, and reverse-permutation classifications did not locate a covering published result.

## Limitations
The theorem fixes universality index \(2\) and classifies shortest extremizers. It does not classify longer extremizing words, nor does it settle equality classifications for universality index at least \(3\).

The exact length-\(3\) extremal value is not claimed as new here; it is used as the equality threshold. The new content is the complete shortest equality classification for all \(\sigma\ge4\).

An unindexed note or unpublished computation could contain the same equality observation.

## References
1. D. Adamson, P. Fleischmann, A. Huch, F. Manea, P. Sarnighausen-Cahn, and M. Wiedenhöft, “Tight Bounds for the Number of Absent Scattered Factors,” arXiv:2407.18599v1, first public version 2024-07-26; revised as “Tight Bounds for the Number of Absent Subsequences,” arXiv:2407.18599v2.
2. M. Kosche, T. Koß, F. Manea, and S. Siemer, “Absent Subsequences in Words,” arXiv:2108.13968v1, 2021.
