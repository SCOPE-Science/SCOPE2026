# Forest structure and sharp two-read deletion capacity of palindromic words

## Finding
Let \(q\ge2\) be an integer and \(\Sigma\) a labeled alphabet of size \(q\). Let \(\mathcal P_n=\{w\in\Sigma^n:w=w^{\mathrm R}\}\). Let \(D_1(w)\) be the **set of distinct words** obtained by deleting exactly one symbol. Define \(H_{q,n}\) on \(\mathcal P_n\) by joining two distinct palindromes \(x,y\) when \(|D_1(x)\cap D_1(y)|\ge2\). Thus an independent set is a source code recoverable from any two distinct one-deletion outputs.

**Theorem (complete graph structure and exact capacity).** The graph \(H_{q,1}\) is edgeless, as is \(H_{q,2m}\) for every \(m\ge1\). For every \(m\ge1\), the graph \(H_{q,2m+1}\) is a forest with precisely \(q^m\) isolated vertices and the following nontrivial connected components:

* for each \(1\le r<m\), exactly \(\binom q2(q-2)q^{m-r-1}\) trees having \(2^r\) vertices;
* exactly \(\binom q2\) trees having \(2^m\) vertices.

Here every size-\(2^r\) tree belongs to the same explicitly described recursive family: \(T_1=K_2\), and \(T_r\) consists of two copies of \(T_{r-1}\) joined by a single edge between their fully alternating configurations. In particular,
\[
|E(H_{q,2m+1})|=\frac{q(q^m-1)}2.
\]
Writing \(M_q(n)\) for the maximum size of an independent set of \(H_{q,n}\),
\[
\boxed{M_q(1)=q,\qquad M_q(2m)=q^m\ (m\ge1),\qquad M_q(2m+1)=\frac{q^m(q+1)}2\ (m\ge1).}
\]
A constructive optimal odd-length code consists of precisely those palindromes whose central symbol is less than or equal to its immediate left neighbor in any fixed total order on \(\Sigma\).

For example, at \(q=3\), \(n=7\), the graph has \(81\) vertices, \(39\) edges, \(27\) isolates, nine two-vertex components, three four-vertex components and three eight-vertex components. An optimal two-read code contains \(54\) palindromes, whereas an optimal one-read (disjoint-deletion-ball) palindrome code contains \(27\).

## Assumptions and scope
All source words have the same indexed length; ordinary reversal fixes each palindrome. Deletions are arbitrary single-coordinate deletions, including first/last positions. Distinct outputs are counted once despite duplicate deletion positions. A decoder is given **two different** outputs from the same word, not two copies of one output. The condition applies to pairwise reconstruction and does not require deletion positions to be identified. The alphabet is arbitrary but fixed and labeled; in the explicit code it carries an arbitrary fixed total order. The separate boundary case \(n=1\) is necessary because each one-letter word has only the empty deletion output.

## Proof
**Lemma 1 (a palindrome has at most one insertion of a specified symbol).** If two palindromes are obtained by inserting the same letter \(a\) into the same word, they coincide. Indeed, suppose the insertion of \(a\) before and after a factor \(S\) gives two different palindromes. If \(S\) consists only of copies of \(a\), the outputs are equal. Otherwise their first disagreement has \(a\) in the first palindrome and a non-\(a\) symbol in the second, whereas at their final disagreement the first palindrome has a non-\(a\) symbol and the second has \(a\). The first and last disagreement indices of two palindromes are symmetric about their common center, contradicting equality of the symbols of the first palindrome at mirror positions.

**Lemma 2 (even lengths).** Distinct even-length palindromes cannot have a common one-deletion descendant. In an even palindrome every letter has even multiplicity. Consequently the uniquely odd-multiplicity letter in a one-deletion output identifies the removed symbol. If two even palindromes yield the same output, they therefore have the same deleted letter; Lemma 1 makes the parents equal. Hence \(H_{q,2m}\) is edgeless. At length one every deletion ball is the singleton containing the empty word, so \(H_{q,1}\) is also edgeless under the two-output criterion.

**Lemma 3 (exact one-deletion overlap recursion for distinct odd palindromes).** Write \(P=aUa\), \(Q=bVb\) with odd length at least three and \(U,V\) themselves palindromes. If \(a=b\), then
\[
D_1(P)\cap D_1(Q)=\{aza:z\in D_1(U)\cap D_1(V)\}.
\]
Indeed a common descendant not beginning with \(a\) would require deleting the first symbol from both parents, making the remaining suffixes equal and thus making the parents identical. Symmetrically every common descendant ends in \(a\). If one representation deletes an outer \(a\), the resulting descendant's equal outer symbol allows that deletion to be moved to the adjacent inner \(a\), without changing the output. Therefore the deletion can always be realized inside \(U,V\), proving the equality. Conversely any common inner descendant gives a common outer descendant by adjoining \(a\) at both ends.

If \(a\ne b\), the two deletion sets intersect **if and only if** \(P\) and \(Q\) are the opposite phases of the fully alternating palindromes \((ab)^m a\), \((ba)^m b\). To see necessity, any common descendant starts with \(a\) or \(b\). If it starts with \(a\), the initial \(b\) of \(Q\) and the final \(a\) of \(P\) must be deleted, so \(P\) and \(Q\) are one-position cyclic shifts. The two palindromic equalities then force period two, hence these alternating forms. The other initial symbol is symmetric. Conversely they share the two distinct alternating outputs of length \(2m\) from endpoint deletion. These are the only common outputs: their letter-count vectors require deleting \(a\) from \(P\) and \(b\) from \(Q\); internal such deletions produce respectively adjacent \(bb\) and \(aa\), which cannot coincide. Thus in this case the intersection has **exactly two** members.

**Lemma 4 (canonical centered alternating edges).** Induct on \(m\). At \(m=0\) the two-read graph is edgeless. For equal outer letters, Lemma 3 preserves the number of shared outputs and embeds each smaller edge under the operation \(U\mapsto aUa\). For different outer letters Lemma 3 supplies precisely the fully alternating cross-edge. It follows that two distinct odd palindromes are adjacent in \(H_{q,2m+1}\) exactly when they agree outside a symmetric central interval of odd length \(2r+1\), for some \(1\le r\le m\), and on this interval are the two opposite phases of an alternating word on an unordered pair of different letters. This interval is uniquely determined by the first and last indices at which the parents disagree.

**Lemma 5 (forest and component spectrum).** Represent a palindrome of length \(2m+1\) by the sequence \((c_0,c_1,\ldots,c_m)\) read from its center to its left end. If \(c_0=c_1\), Lemma 4 gives no incident edge; there are \(q^m\) such isolates. Otherwise fix the unordered pair \(S=\{c_0,c_1\}\). Every edge preserves \(S\) and changes only a consecutive initial sequence of the \(c_i\) consisting of alternating symbols of \(S\). Let \(r\) be the largest integer from \(1\) to \(m\) such that \(c_2,\ldots,c_r\) all belong to \(S\); thus either \(r=m\) or \(c_{r+1}\notin S\). The outer string \(c_{r+1},\ldots,c_m\) is invariant along edges, and so is \(S\). Holding these data fixed leaves \(2^r\) vertices: two orientations for \((c_0,c_1)\), and two choices at each of \(c_2,\ldots,c_r\).

Within this set, edges of radius less than \(r\) preserve \(c_r\) and give two copies of the analogous \(r-1\) graph; exactly one radius-\(r\) edge joins their two opposite fully alternating configurations. Starting with a single edge at \(r=1\), induction shows that the component is a tree of \(2^r\) vertices. When \(r<m\), choose \(S\) in \(\binom q2\) ways, choose the first excluded letter \(c_{r+1}\) in \(q-2\) ways, and choose the remaining \(m-r-1\) outer letters in \(q^{m-r-1}\) ways. When \(r=m\), only \(S\) is chosen. This proves the component spectrum (the factors involving \(q-2\) are zero when \(q=2\)). Summing edges by unique radius also gives
\[
\binom q2\sum_{r=1}^{m}q^{m-r}=\frac{q(q^m-1)}2.
\]

**Lemma 6 (sharp independent-set capacity).** For each choice of outer coordinates \(c_2,\ldots,c_m\) and unequal adjacent central letters \(c_0,c_1\), swapping the central two coordinates yields a distinct palindrome joined to the original by a radius-one edge, corresponding to flipping its central three symbols. These edges form a disjoint matching of size \(q^m(q-1)/2\). Any independent set on the \(q^{m+1}\) vertices contains at most one endpoint of each matched edge, so its size is at most \(q^m(q+1)/2\). Fix an ordering of the alphabet and retain exactly the palindromes with \(c_0\le c_1\). Since every edge flips the two distinct central letters, no such edge has both endpoints retained. There are \(q^{m-1}\binom{q+1}{2}=q^m(q+1)/2\) retained palindromes. This meets the upper bound, proving the exact odd-length capacity. Even length and length one follow from Lemma 2.

## Verification
Two standalone Python 3 standard-library programs accompany this statement. Run `python3 direct_check.py` and `python3 structural_check.py` from this package. The first computes actual distinct deletion-output sets and compares **all** pairs of palindromes (including arbitrary alphabet symbols), independently checking the alternating-interval edges, graph components, matching and even-length emptiness. Its checked odd parameters are \(q=2,1\le m\le7\), \(q=3,1\le m\le4\), \(q=4,1\le m\le3\), \(q=5,1\le m\le2\); it checks even lengths for \(q=2,3,4\) and \(1\le m\le4\). The second generates canonical alternating edges without using deletion sets, then verifies exact component spectra, forest acyclicity, matching upper bounds and explicit independent codes at \((q,m)=(2,9),(3,6),(4,4),(5,3),(6,3),(7,2)\). Both completed successfully. These finite checks corroborate the all-length proof and are not claimed to establish infinitely many cases by enumeration.

## Relationship to prior work
Levenshtein's sequence reconstruction framework and the pre-2016 work on constrained-source deletion codes motivate distinguishing single-read from multiple-read recoverability. Kulkarni and Kiyavash (2012) provide constrained-source single-deletion bounds, not exact multiple-read palindromic capacities. Cai et al. (2020) establish the Type-A alternating-interval criterion for two overlapping single-deletion outputs. That criterion explains the mechanism but does not give the sharp independence number or the component spectrum on the palindrome sublanguage.

The published exact **one-read** palindrome result states a different graph condition, requiring merely one shared output, and has odd-length optimal code size \(q^m\); the present two-read threshold gives \(q^m(q+1)/2\) and an explicit forest decomposition. The published unrestricted **two-read** edge census does not supply an independent-set bound on the palindromic induced subgraph. These stronger or overlapping premises are credited rather than claimed as new. The statements here concern the joint specialization plus exact structural and code-capacity conclusions; no independence from those premises is claimed.

## Limitations
The theorem is for palindromic **source** words and exactly one ordinary deletion per read; it does not handle noisy reads with distinct numbers of deletions, arbitrary nonpalindromic codewords, indels, or multi-deletion capacity. A matching provides the sharp upper bound here, not for the unrestricted reconstruction graph. Historical unindexed equivalent classifications remain possible. The finite computational checks do not substitute for a complete formal verification or historical-priority survey.

## References
1. A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128v1, first publicly posted 2012-11-13. https://arxiv.org/html/1211.3128v1
2. D. Cullina and N. Kiyavash, *An Improvement to Levenshtein's Upper Bound on the Cardinality of Deletion Correcting Codes*, arXiv:1302.6562v1, first publicly posted 2013-02-26. https://arxiv.org/html/1302.6562v2
3. K. Cai, H. M. Kiah, T. T. Nguyen, and E. Yaakobi, *Coding for Sequence Reconstruction for Single Edits*, arXiv:2001.01376v1, first posted 2020-01-06. https://arxiv.org/abs/2001.01376
4. J. Chrisnata, H. M. Kiah, and E. Yaakobi, *Optimal Reconstruction Codes for Deletion Channels*, arXiv:2004.06032v1, first posted 2020-04-13. https://arxiv.org/abs/2004.06032
5. *Exact one-deletion confusability and capacity of palindromic codes*, published mathematical record, 2026-11-08. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-one-deletion-confusability-and-capacity-of-palindromic-cod--9646637bbf2e/RESULT.md
6. *Exact edge count of the finite-alphabet two-read single-deletion reconstruction graph*, published mathematical record, 2026-10-04. https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-edge-count-of-the-finite-alphabet-two-read-single-deletion--737fed325e91/RESULT.md
