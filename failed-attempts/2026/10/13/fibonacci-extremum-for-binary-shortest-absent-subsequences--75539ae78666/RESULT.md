# Fibonacci extremum for binary shortest absent subsequences
## Finding
Let \(w\) be a finite binary word with alphabet exactly \(\{0,1\}\), and let its universality index be \(\iota(w)=k\ge1\). Let \(F_1=F_2=1\) be the Fibonacci numbers. Then
\[
|\operatorname{SAS}(w)|\le F_{k+3}.
\]

The bound is attained by the alternating-arch word
\[
A_k=01\,10\,01\,10\cdots,
\]
with exactly \(k\) two-letter blocks. Hence
\[
|\operatorname{SAS}(A_k)|=F_{k+3}.
\]

A binary \(k\)-universal word has length at least \(2k\). Among words of this minimum length, equality occurs exactly for \(A_k\) and its bitwise complement.

## Assumptions and scope
A subsequence is obtained by deleting zero or more letters while preserving order. A word is \(k\)-universal when it contains every binary word of length at most \(k\) as a subsequence. The universality index \(\iota(w)\) is the largest such \(k\). A shortest absent subsequence, abbreviated SAS, is an absent subsequence of minimum possible length; when \(\iota(w)=k\), every SAS has length \(k+1\).

The alphabet is required to be exactly \(\{0,1\}\). The result is about the number of distinct SAS, not their number of embeddings.

## Proof
Kosche, Koß, Manea, and Siemer define \(A_k\) by alternating an increasing alphabet permutation and its reversal. Their Proposition 3.21 proves that \(A_k\) maximizes the number of SAS among all words with universality index \(k\). Thus, in the binary case it remains to count the SAS of
\[
A_k=01\,10\,01\,10\cdots.
\]

Their SAS characterization gives a particularly simple binary recurrence. For one block \(01\), the possible adjacent letters of an SAS are
\[
00,\ 10,\ 11,
\]
so if \(p\) and \(q\) count feasible prefixes ending in \(0\) and \(1\), appending this block sends
\[
(p,q)\longmapsto(p+q,q).
\]
For a block \(10\), the possible adjacent pairs are \(00,01,11\), and the update is
\[
(p,q)\longmapsto(p,p+q).
\]
Before processing any block, \((p,q)=(1,1)\).

Because the block orientations in \(A_k\) alternate, the updated coordinate is always the smaller one after the first step. Consequently, after \(i\ge1\) blocks, the two coordinates, in increasing order, are
\[
(F_{i+1},F_{i+2}),
\]
and the total number of feasible length-\(i+1\) SAS is
\[
F_{i+1}+F_{i+2}=F_{i+3}.
\]
At \(i=k\) this gives \(|\operatorname{SAS}(A_k)|=F_{k+3}\). Proposition 3.21 then gives the claimed global upper bound.

It remains to classify equality at minimum word length. Any binary \(k\)-universal word needs at least \(k\) occurrences of each letter, hence has length at least \(2k\). At length \(2k\), its arch factorization consists of \(k\) blocks, each equal to \(01\) or \(10\).

For an arbitrary sequence of those blocks, use the same two-coordinate recurrence. Suppose after \(i\) blocks the sorted coordinates are \(x\le y\). Inductively,
\[
x\le F_{i+1},\qquad y\le F_{i+2}.
\]
Indeed, the next update keeps one old coordinate and replaces the other by \(x+y\), so after sorting the new pair is bounded by
\[
(F_{i+2},F_{i+3}).
\]
Therefore its total after \(k\) blocks is at most \(F_{k+3}\).

Equality forces both coordinate bounds to be sharp at every preceding step, and the unchanged coordinate must be the larger one. Thus each new block must update the currently smaller coordinate. After the first block this forces the block orientations to alternate. There are exactly two such choices, according to whether the first block is \(01\) or \(10\); these are \(A_k\) and its complement.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier checks the Fibonacci recurrence for the alternating extremal through \(k=15\), directly enumerates all candidate shortest absent subsequences through \(k=10\), and exhausts every one of the \(2^k\) minimum-arch orientation patterns through \(k=12\).

As an independent finite stress test, it enumerates every binary word of length at most \(12\), computes its universality index by arch scanning, tests subsequence membership directly, and reconstructs its complete SAS set. Every tested word satisfies the Fibonacci bound, and every tested minimum-length equality case is one of the two alternating words.

The general proof does not rely on those finite experiments: the global extremality of \(A_k\) is the published Proposition 3.21, while the binary Fibonacci count and minimum-length equality classification follow from the explicit two-coordinate induction above.

## Relationship to prior work
Kosche, Koß, Manea, and Siemer introduced the SAS framework used here and proved that \(A_k\) maximizes the number of SAS at fixed universality index. They characterize an SAS of \(A_k\) as a sequence obeying alternating weak inequalities. Their quantitative result only establishes exponential growth under a large-even-alphabet assumption and explicitly notes that the estimate is not tight; it does not state the binary Fibonacci count.

Adamson, Fleischmann, Huch, Manea, Sarnighausen-Cahn, and Wiedenhöft later generalized the extremal construction from shortest absent subsequences to absent subsequences of arbitrary prescribed length. Their Theorem 4.16 again identifies alternating reversed arches as extremal. In the subsequent counting discussion they state that whether a closed form exists for the number of scattered factors of this extremal construction remains open in general. They do not state the binary shortest-length specialization
\[
F_{k+3}.
\]

The present result therefore supplies an exact closed form in the fundamental binary SAS case and classifies the minimum-length equality cases.

## Limitations
The Fibonacci formula is specific to a binary alphabet and to shortest absent subsequences. It does not give a closed form for larger alphabets or for absent subsequences longer than \(k+1\).

The equality classification proved here is restricted to \(k\)-universal words of minimum possible length \(2k\). Longer words can be bounded by the same extremal theorem, but no complete equality classification for all lengths is claimed.

An unindexed note or unpublished calculation could have observed the binary Fibonacci specialization despite the targeted literature and database searches.

## References
1. M. Kosche, T. Koß, F. Manea, and S. Siemer, “Absent Subsequences in Words,” arXiv:2108.13968v1, first public version 2021-08-31; Fundamenta Informaticae 189(3–4), 199–240, DOI 10.46298/fi.9221.
2. D. Adamson, P. Fleischmann, A. Huch, F. Manea, P. Sarnighausen-Cahn, and M. Wiedenhöft, “Tight Bounds for the Number of Absent Subsequences,” arXiv:2407.18599v1, first public version 2024-07-26; FCT 2025, LNCS, DOI 10.1007/978-3-032-04700-7_2.
