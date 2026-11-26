# Exact radius-two Kendall swap balls for words with repeated symbols

## Finding
Let \(\Sigma\) be any alphabet and let \(w=w_1\cdots w_n\in\Sigma^n\), with \(n\ge2\). A swap exchanges two adjacent positions. Let \(B_2(w)\) be the set of **distinct words** obtained from \(w\) using at most two swaps, counting a no-op swap of equal adjacent symbols neither as necessary nor as a new word. Define

\[
 b=\sum_{i=1}^{n-1}[w_i\ne w_{i+1}],\qquad
 t=\sum_{i=1}^{n-2}[w_i\ne w_{i+1}][w_{i+1}\ne w_{i+2}],
\]
\[
 d=\sum_{i=1}^{n-2}[|\{w_i,w_{i+1},w_{i+2}\}|=3],\qquad
 e=\sum_{i=1}^{n-2}[[w_i=w_{i+1}]\ne[w_{i+1}=w_{i+2}]].
\]
The square brackets are indicator functions. Empty sums are zero. Then

\[
\boxed{|B_2(w)|=1+b+\binom b2-t+2d+e.}
\]

The expression is evaluable in \(O(n)\) time and \(O(1)\) extra space; no assumption that symbols are distinct is needed. If \(|\Sigma|=q\ge3\), its exact maximum over all length-\(n\) words is

\[
\boxed{\max_{w\in\Sigma^n}|B_2(w)|=\binom{n+1}{2}-1.}
\]

Equality holds precisely when every consecutive triple of symbols is pairwise distinct (and, for \(n=2\), when the two letters differ). There are exactly \(q(q-1)(q-2)^{n-2}\) maximizing words. For uniformly random \(w\in\Sigma^n\), put \(p=(q-1)/q\). The exact mean is

\[
\boxed{\mathbb E|B_2(w)|=1+(n-1)p+\frac{(n-2)(n+1)}2p^2.}
\]

Equivalently, the graph on all \(q^n\) words, joining two **different** words when at most two adjacent swaps connect them, has precisely

\[
\frac{q^n}{2}\left((n-1)\frac{q-1}{q}
+\frac{(n-2)(n+1)}2\frac{(q-1)^2}{q^2}\right)
\]
undirected edges. These formulas concern the usual adjacent-swap distance within fixed-composition components; they do not claim anything about other edit channels.

## Assumptions and scope
Swaps act on positions, so the alphabet need only admit equality tests. Every output of at most two swaps necessarily has the same symbol multiplicities as the input. The ball is a **set**, not a multiset of edit histories; swapping identical adjacent symbols leaves the word unchanged. The maximum and mean claims assume \(q\ge3\) for sharp maximum attainment, and \(q\ge2\) for the mean; the local formula holds for all alphabets and \(n\ge2\). A length-one word has ball size one and is outside the displayed maximum formula.

## Proof
Call an edge \(i\) active if \(w_i\ne w_{i+1}\). Exactly \(b\) distinct words arise from a single swap because their two altered positions identify the swapped edge. Swapping twice at the same edge restores the initial word. If two swapped edges \(i,j\) are disjoint (\(|i-j|\ge2\)), each must be active already in the original word. The resulting word changes exactly the four positions in their two edge blocks, identifying the unordered pair \(\{i,j\}\) uniquely. The number of such pairs is \(\binom b2-t\), since \(t\) counts active consecutive edge pairs, which are the only nondisjoint active edge pairs.

It remains to analyze swaps of the two overlapping edges of a three-position window \(abc\). The left-then-right order yields \(bca\) provided \(a\ne b\) and \(a\ne c\); the right-then-left order yields \(cab\) provided \(b\ne c\) and \(a\ne c\). When \(a,b,c\) are all different, there are exactly two new outputs, each changing all three positions. When exactly one neighboring pair is equal (patterns \(aab\) or \(abb\), with the other symbol different), there is exactly one new output, changing the two nonadjacent endpoint positions. When \(a=c\ne b\), both second swaps would exchange equal letters and give no new two-swap output; the all-equal case likewise gives none.

The changed-position supports distinguish the four classes: one swap changes two adjacent positions, disjoint swaps change exactly four positions, all-distinct overlapping swaps change exactly three consecutive positions, and repeated-neighbor overlapping swaps change exactly two positions separated by one position. Within each class the support determines the relevant edge or triple; in an all-distinct triple the two cyclic outputs differ. Thus there are no uncounted duplicates, proving the ball formula.

For the sharp maximum, write \(a=t-d\), the number of alternating triples \(aba\) with unequal neighboring symbols. Rearrangement gives
\[
|B_2(w)|=1+b+\binom b2+\sum_{i=1}^{n-2}g_i,
\]
where \(g_i\) is \(1\) for an all-distinct triple or exactly one unequal neighbor-edge, \(-1\) for an alternating \(aba\) triple, and \(0\) for an all-equal triple. Every \(g_i\le1\), and \(b\le n-1\). Therefore the displayed maximum is an upper bound. Equality requires \(b=n-1\); then triples with one equal neighbor-edge cannot occur, and every \(g_i=1\) demands all three letters be distinct. Conversely, that condition achieves equality. Choose the first two letters in \(q(q-1)\) ways and each later letter avoiding the preceding two in \(q-2\) ways, proving the count of extremizers.

For the exact mean, take independent uniformly random letters and set \(p=(q-1)/q\). The indicators of unequal consecutive letters are pairwise independent (indeed jointly independent), so \(\mathbb E[b]=(n-1)p\) and \(\mathbb E\binom b2=\binom{n-1}2p^2\). For each length-three window, the respective probabilities contributing to \(t,d,e\) are \(p^2\), \((q-1)(q-2)/q^2\), and \(2(q-1)/q^2\). Consequently \(\mathbb E[-t+2d+e]=(n-2)p^2\). Substitution gives the mean. Summing \(|B_2(w)|-1\) across centers counts each edge exactly twice, proving the graph-edge formula.

## Verification
The standalone script `verify_adjacent_swap_ball.py` computes the radius-two ball by exhaustive breadth-first generation of all single-swap neighbors, independently of the local counting formula. It compared the two methods on **88,397 words**, covering all binary words of lengths 2–12, all ternary words of lengths 2–9, all four-letter words of lengths 2–7, all five-letter words of lengths 2–6, and all six-letter words of lengths 2–5. It also independently compared the exact arithmetic mean and, for each tested \(q\ge3\), the maximum size and exact number of maximizing centers.

Run with `python3 verify_adjacent_swap_ball.py`. The expected final status begins `ADJACENT_SWAP_RADIUS2_PASS`. The script is confirmatory, not an exhaustive proof for arbitrary lengths; the preceding argument supplies that proof.

## Relationship to prior work
Cicirello introduced the Kendall tau **sequence** distance defined by adjacent swaps for equal-composition strings with repeated symbols and provided efficient point-to-point distance algorithms [1]. Buzaglo and Etzion's permutation-metric work treats Kendall balls and codes when all symbols are distinct [2]. Gabrys and coauthors consider codes for a deletion or an adjacent transposition [3]. The present theorem instead gives **center-specific ball cardinalities for any repeated-symbol word with two swaps**, their full-alphabet sharp maximum and extremizers, and their exact uniform mean. The all-distinct specialization recovers the familiar radius-two permutation count; it is not asserted to be new.

## Limitations
Only radius two is addressed. The theorem does not determine optimal code sizes or multiradius volumes, nor does a ball's cardinality alone certify a packing optimum. Prior-literature comparison is based on the specified primary passages and targeted searches; an equivalent low-radius enumeration in less searchable combinatorial literature cannot be ruled out. No independent audit has been performed.

## References
1. V. A. Cicirello, *Kendall Tau Sequence Distance: Extending Kendall Tau from Ranks to Sequences*, arXiv:1905.02752 (first posted 7 May 2019), §§3.2–3.3. https://arxiv.org/abs/1905.02752
2. S. Buzaglo and T. Etzion, *Bounds on the Size of Permutation Codes with the Kendall τ-Metric*, arXiv:1408.4963 (2014), §II and related weight-two discussion. https://arxiv.org/abs/1408.4963
3. R. Gabrys, V. Guruswami, J. Ribeiro, and K. Wu, *Beyond Single-Deletion Correcting Codes: Substitutions and Transpositions*, arXiv:2112.09971 (first posted 18 December 2021), §§1.3–1.4. https://arxiv.org/abs/2112.09971
