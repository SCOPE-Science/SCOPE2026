# The one-or-two maximal-common-subsequence law for disjoint-alphabet conjugate powers

## Finding

Let \(A\) and \(B\) be arbitrary nonempty finite words over disjoint alphabets, and let \(r,s\) be arbitrary positive integers. Put \(X=(AB)^r\) and \(Y=(BA)^s\). A maximal common scattered subsequence is a word that embeds in both \(X\) and \(Y\), but is not a proper scattered subsequence of any other common subsequence.

**Theorem.** If \(r<s\), the unique maximal common subsequence is \(X\); if \(r>s\), it is \(Y\). If \(r=s=k\), there are exactly two maximal common subsequences, namely
\[
U=B(AB)^{k-1},\qquad V=A(BA)^{k-1}.
\]
More strongly, in the equal-power case the *entire* common-subsequence language is the union of the two downward closures:
\[
\operatorname{Sub}(X)\cap\operatorname{Sub}(Y)
=\operatorname{Sub}(U)\cup\operatorname{Sub}(V).
\]
Here \(\operatorname{Sub}(Z)\) denotes the set of all distinct scattered subsequence words of \(Z\), including the empty word. The two maximal subsequences have lengths
\[
|U|=k(|A|+|B|)-|A|,\qquad
|V|=k(|A|+|B|)-|B|.
\]
Consequently, the longest-common-subsequence length is \(k(|A|+|B|)-\min(|A|,|B|)\), the shortest-maximal-common-subsequence length is \(k(|A|+|B|)-\max(|A|,|B|)\), and the gap is \(\bigl||A|-|B|\bigr|\). If \(|A|=|B|\), both maximal words are longest; otherwise exactly one is longest. When \(r\ne s\), the longest and shortest maximal-common-subsequence lengths both equal \(\min(r,s)(|A|+|B|)\).

## Assumptions and scope

Each word is a finite sequence of symbols. The words \(A\) and \(B\) may contain repeated letters or arbitrary internal order, but are nonempty and satisfy \(\operatorname{alph}(A)\cap\operatorname{alph}(B)=\varnothing\). Integers \(r,s\) range over all positive integers. Distinct subsequence strings are counted, not index embeddings. Inclusion is scattered-subsequence containment, not contiguous-factor containment. The source words are linear words with specified starting positions; rotations are not permitted during matching.

## Proof

First suppose \(r<s\). Because \(s\ge r+1\), the word \(X=(AB)^r\) occurs as a contiguous factor of \(Y=(BA)^s\), beginning immediately after the first block \(B\). Thus every subsequence of \(X\) is common, and no common word can be longer in the subsequence partial order than the whole word \(X\). Hence \(X\) is the unique maximal common subsequence. The case \(r>s\) is symmetric: \(Y=(BA)^s\) occurs in \(X=(AB)^r\), beginning immediately after its first \(A\) block.

Now set \(r=s=k\). The identities
\[
X=A U=V B,\qquad Y=U A=B V,
\]
show that \(U=B(AB)^{k-1}\) and \(V=A(BA)^{k-1}\) are both contiguous factors of both source words. Hence their subsequences are all common.

Conversely, let \(T\) be any common subsequence that does not embed in \(U\). Since \(U\) is \(X\) with its first complete \(A\) block deleted, every embedding of \(T\) in \(X\) must select at least one letter from that initial \(A\) block. This selected letter must be the first selected letter of \(T\), so \(T\) begins with a letter of \(\operatorname{alph}(A)\). Similarly, \(U\) is \(Y\) with its final complete \(A\) block deleted. Every embedding of \(T\) in \(Y\) must select at least one letter from that final \(A\) block, so \(T\) ends with a letter of \(\operatorname{alph}(A)\).

Since \(\operatorname{alph}(A)\) and \(\operatorname{alph}(B)\) are disjoint, any embedding of \(T\) in \(X\) ending with an \(A\)-alphabet letter uses no positions from the final \(B\) block. It therefore embeds in \(X\) without its final \(B\) block, which is \(V\). (Equivalently, its embedding in \(Y\), beginning with an \(A\)-alphabet letter, uses no positions from the initial \(B\) block and embeds in \(V\).) This establishes the claimed equality of common-subsequence languages.

For any letter \(a\) present in \(A\), \(V\) has \(k\) times its multiplicity in \(A\), whereas \(U\) has only \(k-1\) times that multiplicity. Therefore \(V\) cannot embed in \(U\). For any letter \(b\) present in \(B\), the reverse multiplicity inequality shows that \(U\) cannot embed in \(V\). Their two downward closures therefore have exactly the two incomparable maxima \(U\) and \(V\). The length formulas follow by counting complete blocks. This completes the proof.

## Verification

The accompanying standalone Python program, `verification/verify.py`, constructs all distinct scattered subsequences by finite set expansion, intersects the two sets, and tests maximality by attempting every single-character insertion. It also checks the whole-language union identity in the equal-power case. It passed 1,144 test configurations covering nonempty disjoint-alphabet blocks of lengths one through three (with repetitions permitted), plus longer repeated-letter stress cases; these involved 92,735 distinct common subsequence strings in aggregate. The program uses only the Python standard library. Execute `python verification/verify.py` from the extracted package root. Finite tests are supporting checks, not an exhaustive proof for unbounded lengths; the proof above establishes the quantified theorem.

## Relationship to prior work

Conte, Grossi, Punzi and Uno (2023) give a compact directed acyclic graph enabling general MCS enumeration, counting and rank/select; their main theorems address arbitrary input strings algorithmically, rather than the present two-block conjugate-power language decomposition. Conte and coauthors (2022) previously provided a polynomial-delay enumeration algorithm and the general interspace characterization. Sakai (2018) gave algorithms for producing and testing an MCS. These algorithms apply to the present inputs, but their stated results do not provide the present symbolic two-element classification, nor the exact gap between shortest and longest maximal common subsequences. Work on longest common *cyclic* subsequences allows rotations during matching and thus uses a different problem definition.

For example, \(A=a^h\), \(B=b\), \(k\ge2\), with \(h\ge2\) and \(a\ne b\), gives exactly two maximal common subsequences whose lengths differ by \(h-1\), even over a two-letter alphabet. Thus maximality need not mean maximum length, by an unbounded additive margin in this structured family.

## Limitations

The disjoint-alphabet hypothesis is essential to the downward-closure identity: for \(A=a\), \(B=ab\), and \(k=1\), the strings \(X=aab\) and \(Y=aba\) have the common subsequence \(aa\), which does not embed in either proposed overlap word \(A=a\) or \(B=ab\). The theorem does not assert a classification for overlapping alphabets, arbitrary unrelated periods, more than two source strings, or subsequences modulo rotation. The claimed novelty is a closed-form family classification, not a new general-purpose MCS algorithm. An equivalent result outside the inspected literature cannot be excluded; no independent scientific audit is claimed.

## References

1. A. Conte, R. Grossi, G. Punzi, T. Uno, *A Compact DAG for Storing and Searching Maximal Common Subsequences*, arXiv:2307.13695 (first posted 2023-07-25), ISAAC 2023, DOI:10.4230/LIPIcs.ISAAC.2023.21. https://arxiv.org/abs/2307.13695
2. A. Conte, R. Grossi, G. Punzi, T. Uno, *Enumeration of Maximal Common Subsequences Between Two Strings*, Algorithmica 84 (2022), 757–783, DOI:10.1007/s00453-021-00898-5. Accepted full text: https://arpi.unipi.it/handle/11568/1139265
3. Y. Sakai, *Maximal Common Subsequence Algorithms*, CPM 2018, DOI:10.4230/LIPIcs.CPM.2018.1. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2018.1
4. F. Nicolas and E. Rivals, *Longest Common Subsequence Problem for Unoriented and Cyclic Strings*, Theoretical Computer Science 370 (2007), 1–18, DOI:10.1016/j.tcs.2006.10.002. https://www.lirmm.fr/~rivals/publication/nicolas-tcs-2007/
