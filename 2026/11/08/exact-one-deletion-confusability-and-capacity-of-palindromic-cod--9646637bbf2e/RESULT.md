# Exact one-deletion confusability and capacity of palindromic codes

## Finding

Fix an alphabet \(\Sigma\) of size \(q\ge 2\). Let \(\mathcal P_n\) be the length-\(n\) palindromes, and let \(D_1(w)\) be the set of distinct length-\(n-1\) words produced by deleting exactly one position of \(w\). Two distinct palindromes are **confusable** if their one-deletion descendant sets intersect. Let \(G_n(q)\) denote the resulting simple, labeled graph.

**Theorem.** For each \(n\ge1\), the largest subset of \(\mathcal P_n\) whose members have pairwise disjoint one-deletion descendant sets has size
\[
A_{\mathrm{pal}}(n,q)=q^{\lceil n/2\rceil-\mathbf1_{n\text{ odd}}}=q^{\lfloor n/2\rfloor} \quad(n\ge2),
\]
with \(A_{\mathrm{pal}}(1,q)=1\). More explicitly, for even \(n=2m\) every palindrome belongs to a correcting code of size \(q^m\); for odd \(n=2m+1\), any fixed-central-symbol subfamily has the optimal size \(q^m\).

There is also an exact description of the **entire** confusability graph. For every even \(n\), \(G_n(q)\) has no edges. For odd \(n=2m+1\), its number of unordered edges is
\[
|E(G_{2m+1}(q))|=\frac{q(q^{m+1}-1)}2.
\]
For \(n=1\), \(G_1(q)=K_q\). For odd \(n\ge3\), the graph consists of \(q\) induced copies of \(G_{n-2}(q)\), one for each outer letter \(a\) in \(aua\), together with exactly one edge for each unordered pair \(\{a,b\}\) of different outer letters, joining the alternating palindromes \((ab)^m a\) and \((ba)^m b\). These are all its edges.

## Assumptions and scope

The alphabet is finite with \(q\ge2\) labeled letters. Codewords have a common positive length, positions are indexed, reversal is the ordinary reversal without letter involution, and the channel performs **exactly one ordinary single-symbol deletion at an arbitrary position**. Repeated deletion outputs count only once. The theorem applies to arbitrary alphabets and all stated lengths, not just binary words, and does not concern palindromic block deletions, substitutions, or two-read reconstruction.

## Proof

**Lemma 1 (fixed inserted letter determines a palindromic supersequence).** For any word \(y\) and fixed letter \(a\), at most one distinct palindrome can be obtained by inserting a single copy of \(a\) into \(y\). Suppose insertions at positions \(i<j\) yield palindromes \(P=XaSZ\) and \(Q=XSaZ\). If every symbol in \(S\) is \(a\), then \(P=Q\). Otherwise let \(s\) be the first non-\(a\) symbol of \(S\), and \(t\) its last non-\(a\) symbol. At the leftmost position where \(P,Q\) differ, \(P\) has \(a\) while \(Q\) has \(s\ne a\); at their rightmost position of disagreement, \(P\) has \(t\ne a\) while \(Q\) has \(a\). For two palindromes, the set of differing indices is invariant under position reflection, so the first and last differing indices must be mirror images. But the symbols of \(P\) at those indices would have to agree, a contradiction. This proves the lemma.

If distinct palindromes \(P,Q\) have a common descendant \(y\), let \(a,b\) be their respective deleted letters. If \(a=b\), Lemma 1 forces \(P=Q\), impossible. Thus \(a\ne b\). A palindrome of even length has even occurrences of each symbol; a palindrome of odd length has exactly one symbol with odd multiplicity, namely its central symbol. It follows that two distinct even palindromes can never be confusable, and two distinct odd palindromes with the **same central symbol** cannot be confusable. For odd length \(2m+1\), fixing the central symbol therefore yields \(q^m\) mutually nonconfusable words. For even length \(2m\), all \(q^m\) palindromes form a correcting code.

For the odd-length upper bound, fix the length-\(m\) prefix \(x\). The \(q\) palindromes \(xcx^{\mathrm R}\), one for each \(c\in\Sigma\), all produce the same descendant \(xx^{\mathrm R}\) by deleting their center. They form a clique. There are \(q^m\) such disjoint cliques covering all odd palindromes, so an independent set contains at most \(q^m\) vertices. At length one there is one clique of \(q\) letters, yielding the maximum one. This completes the capacity assertion.

It remains to prove the graph recursion. Let \(P=aUa\) and \(Q=bVb\) be distinct odd palindromes of length at least three.

**Different outer letters:** If \(a\ne b\), a common deletion descendant \(y\) must begin with \(a\) or \(b\), because only the first letter is deletable. Suppose it begins with \(a\). Then \(Q\) must lose its initial \(b\), so \(y=Q[2\ldots n]\) ends in \(b\). Consequently \(P\) must lose its final \(a\), giving \(y=P[1\ldots n-1]\). Hence \(P\) and \(Q\) are related by a one-position cyclic shift. Using palindromicity, \(P_i=P_{i+2}\) for all \(1\le i\le n-2\). Together with the distinct outer letters, this forces \(P=(ab)^m a\) and \(Q=(ba)^m b\). If \(y\) begins with \(b\), exchange their names. Conversely these alternating palindromes visibly share the length-\(n-1\) descendant obtained by deleting the last letter of one and the first letter of the other. Thus exactly one cross-edge joins each unordered pair of outer-symbol groups.

**Same outer letter:** If \(a=b\), any common descendant of two *distinct* palindromes must begin and end with \(a\). Indeed, if a descendant did not begin with \(a\), the first letter of both parents would have to be deleted, which would make their remaining suffixes identical and hence the parents identical. The final-letter argument is symmetric. A deletion of an outer \(a\) yielding such a descendant can instead be performed at the adjacent inner \(a\), if present. Therefore a common descendant can be taken as \(az a\), where \(z\in D_1(U)\cap D_1(V)\). Conversely any such \(z\) gives the common descendant \(aza\). It follows that the subgraph with outer symbol \(a\) is precisely \(G_{n-2}(q)\), under \(U\mapsto aUa\).

Writing \(e_m=|E(G_{2m+1}(q))|\), the decomposition gives \(e_0=\binom q2\) and \(e_m=q e_{m-1}+\binom q2\). Solving,
\[
e_m=\binom q2\sum_{j=0}^m q^j=\frac{q(q^{m+1}-1)}2.\]
This also completes the graph classification.

## Verification

The standalone standard-library program `verify.py` enumerates all palindromes and one-deletion descendants; it checks even-length nonconfusability, the odd-length edge formula, the **complete recursive edge list**, fixed-center independent codes, and clique partitions. Run `python3 verify.py` from this package. It reports `VERIFY_OK tests=33 checked_palindromes=2439` for all lengths 1–17 over a binary alphabet, 1–9 over a ternary alphabet, and 1–7 over a quaternary alphabet. These finite checks support but do not replace the all-length arguments above.

## Relationship to prior work

Kulkarni and Kiyavash (2012) and Cullina and Kiyavash (2013) develop deletion-channel combinatorial bounds, including general q-ary packing methods and constrained-source considerations. Their inspected proofs do not provide the palindrome-source all-length capacity, the complete recursive graph decomposition, or the exact odd-length edge formula here. A two-read deletion reconstruction graph addresses a **different** overlap threshold: pairs may have one shared descendant. No claim of independence from, or incompatibility with, general deletion-coding theory is made.

## Limitations

The theorem is about the restricted set of palindromic source words; it does not determine the unrestricted deletion-code optimum, code rates allowing arbitrary nonpalindromic sources, or multi-deletion channels. The exact graph classification and capacity are proved mathematically but have not undergone independent external review. Search cannot exclude unindexed equivalent historical results.

## References

1. A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128, publicly posted November 13, 2012. https://arxiv.org/abs/1211.3128 ; full text https://arxiv.org/html/1211.3128v1 .
2. D. Cullina and N. Kiyavash, *An Improvement to Levenshtein's Upper Bound on the Cardinality of Deletion Correcting Codes*, arXiv:1302.6562, publicly posted February 26, 2013. https://arxiv.org/abs/1302.6562 ; full text https://arxiv.org/html/1302.6562v2 .
