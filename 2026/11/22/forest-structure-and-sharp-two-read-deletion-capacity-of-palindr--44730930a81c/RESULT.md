# Forest structure and sharp two-read deletion capacity of palindromic words

## Finding

Let \(q\ge2\) be an integer and \(\Sigma\) a labeled alphabet of size \(q\). Let \(\mathcal P_n=\{w\in\Sigma^n:w=w^{\mathrm R}\}\). Let \(D_1(w)\) be the set of distinct words obtained by deleting exactly one symbol. Define \(H_{q,n}\) on \(\mathcal P_n\) by joining two distinct palindromes \(x,y\) when \(|D_1(x)\cap D_1(y)|\ge2\). Its independent sets are exactly the source codes recoverable from any two distinct one-deletion outputs.

The graph \(H_{q,1}\) is edgeless, as is \(H_{q,2m}\) for every \(m\ge1\). For every \(m\ge1\), \(H_{q,2m+1}\) is a forest with exactly \(q^m\) isolated vertices and the following nontrivial components:

- For each \(1\le r<m\), exactly \(\binom q2(q-2)q^{m-r-1}\) trees with \(2^r\) vertices.
- Exactly \(\binom q2\) trees with \(2^m\) vertices.

For a tree with \(2^r\) vertices, its precise recursion is given below: \(T_1=K_2\), and \(T_r\) consists of two copies of \(T_{r-1}\) joined by one edge between the opposite length-\((2r+1)\) alternating phases. In particular, \(|E(H_{q,2m+1})|=q(q^m-1)/2\). If \(M_q(n)\) is the maximum size of an independent set, then
\[
M_q(1)=q,\qquad M_q(2m)=q^m\ (m\ge1),\qquad M_q(2m+1)=\frac{q^m(q+1)}2\ (m\ge1).
\]
An optimal odd-length code for \(m\ge1\) consists of the palindromes whose central symbol is at most its immediate left neighbor, in any fixed total order on \(\Sigma\).

For example, at \(q=3,n=7\) there are \(81\) vertices, \(39\) edges, \(27\) isolates, nine two-vertex components, three four-vertex components and three eight-vertex components. The maximum two-read code contains \(54\) palindromes, versus \(27\) for a one-read code.

## Assumptions and scope

All source words have the same indexed length. Reversal is ordinary reversal, with no alphabet involution. Deletions are arbitrary single-coordinate deletions, including the endpoints. Repeated outputs count only once, and the two-read decoder is given two different outputs from the same word. Reconstruction need not identify the deleted positions. At \(n=1\) each word has only the empty deletion output.

## Proof

**Insertion uniqueness and even length.** If two distinct palindromes came from inserting the same symbol \(a\) before and after a factor \(S\) of one word, their varying parts would be \(aS\) and \(Sa\). If \(S\) consists entirely of copies of \(a\), these are equal. Otherwise, their first disagreement has \(a\) in the first palindrome and a different symbol in the second; at their last disagreement, it is the second palindrome that has \(a\). First and last disagreement positions must be mirror positions because both words are palindromes, a contradiction. For an even palindrome every symbol multiplicity is even, so its deletion output identifies the removed letter as the unique symbol of odd multiplicity. The insertion argument then rules out even one shared output between distinct even palindromes. The assertion at length one is immediate.

**Odd overlap recursion.** Let distinct odd palindromes of equal length at least three be \(P=aUa\) and \(Q=bVb\). If \(a=b\), every common output begins and ends with \(a\): if it did not begin with \(a\), both first positions would have to be deleted to yield the same suffix, forcing the parents equal. The end is symmetric. If such an output was obtained by deleting an outer \(a\), the fact that the output still has that outer symbol lets us delete the adjacent identical inner symbol instead. Hence
\[
D_1(P)\cap D_1(Q)=\{aza:z\in D_1(U)\cap D_1(V)\}.
\]

If \(a\ne b\), a common output starts with either \(a\) or \(b\). In the first case it must arise by deleting the first symbol of \(Q\); the output therefore ends in \(b\), so it must arise by deleting the last symbol of \(P\). Set \(n=2m+1\). This gives the overlap \(P_i=Q_{i+1}\) for \(1\le i<n\). Reversing that equality in both palindromes gives \(P_{i+1}=Q_i\) for \(1\le i<n\). Thus \(P_i=P_{i+2}\) for \(1\le i\le n-2\), with \(P_1=a\) and \(P_2=b\); the relations also determine \(Q\) as the opposite alternating phase. An output starting with \(b\) gives the same conclusion with the roles exchanged. Conversely, these opposite phases share the two different alternating outputs from endpoint deletion. The count vectors require deleting \(a\) from \(P\) and \(b\) from \(Q\); deleting these symbols at internal positions creates respectively an adjacent \(bb\) and an adjacent \(aa\). Either internal output has exactly its one newly joined equal pair, so an internal output cannot match an endpoint output or the other parent's internal output. This proves that the overlap in this case has exactly two members.

By stripping equal outer symbols, the recursion shows that an edge is exactly a pair agreeing outside a central interval of odd length \(2r+1\), \(1\le r\le m\), with the two opposite alternating phases of a pair of different symbols inside. The first and last differences determine that interval. If only the center differs, the overlap is the single output at the length-one stage, not an edge.

**Components and counts.** Represent a palindrome by \((c_0,c_1,\ldots,c_m)\) from center to left end. If \(c_0=c_1\), the edge rule gives no incident edge, yielding \(q^m\) isolates. Otherwise put \(S=\{c_0,c_1\}\), and let \(r\) be the last index of the maximal initial segment using symbols only from \(S\). Every incident edge flips an alternating initial segment \(c_0,\ldots,c_s\) with \(1\le s\le r\), so \(S,r\) and the tail \((c_{r+1},\ldots,c_m)\) are invariant. A fixed choice of those data gives \(2^r\) vertices: two choices of orientation for the first two symbols, and two choices at each remaining position through \(r\). At \(r=1\) they form a single edge. For \(r>1\), fixing \(c_r\) to either symbol gives a copy of the tree for \(r-1\) under all flips with \(s<r\). The unique edge with \(s=r\) connects those two copies at their fully alternating endpoints, with the endpoint in each copy determined by the prescribed \(c_r\). This proves that each such class is connected and acyclic. Counting \(S\) and the tails gives the component spectrum: for \(r<m\) the first tail position has \(q-2\) choices and the rest have \(q\) each, while \(r=m\) has no tail. Counting edges by unique radius gives
\[
\binom q2\sum_{r=1}^m q^{m-r}=q(q^m-1)/2.
\]

**Sharp capacity.** The flips with \(s=1\) give a matching of size \(\binom q2 q^{m-1}\) on the \(q^{m+1}\) vertices. An independent set omits at least one endpoint per matching edge. The set with \(c_0\le c_1\) is independent by the edge rule, since every edge reverses the strict order of the two central symbols. Its size is \(q^{m-1}\binom{q+1}{2}\), meeting the bound. The edgeless cases have all their vertices available. For the example's one-read comparison, fixing \((c_1,\ldots,c_m)\) gives a class with a common center-deletion output and hence capacity at most one per class. Choosing \(c_0=c_1\) in each class meets the bound: the overlap recursion requires either only the center to differ or a central alternating interval with distinct central letters. Neither is possible for distinct chosen words.

## Verification

The accompanying Python 3 standard-library checkers use two different finite methods. `direct_check.py` compares actual distinct deletion-output sets across all palindrome pairs for odd-length parameters \(q=2,1\le m\le7\); \(q=3,1\le m\le4\); \(q=4,1\le m\le3\); and \(q=5,1\le m\le2\), and even-length parameters \(q=2,3,4\) and \(1\le m\le4\). It checks even-length emptiness and the odd adjacency criterion, components, matching and code. `structural_check.py` generates alternating edges without deletion sets and checks component sizes, acyclicity and capacity for \((q,m)=(2,9),(3,6),(4,4),(5,3),(6,3),(7,2)\). The original runs completed successfully. The finite checks corroborate the structural theorem; the overlap argument and induction prove all lengths.

## Relationship to prior work

The Type-A criterion of Cai et al. characterizes two shared one-deletion outputs in the unrestricted setting. On the palindrome sublanguage this forces a centered alternating interval. The prior one-read palindrome result already supplies the outer-letter recursion with a clique on the length-one alphabet. The two-read graph retains the alternating cross-edges and removes the one-output clique edges at the base; its total edge count can also be found by subtracting those edges from the one-read census. The contribution here is the exact component spectrum for the remaining forest and the sharp two-read independent-set result. The binomial-tree shape has appeared in the binary one-read problem, where the full odd-length graph is a single larger tree instead. The constrained-source bounds of Kulkarni and Kiyavash and the unrestricted two-read edge census do not give the palindrome-restricted two-read capacity.

## Limitations

The result is for palindromic source words, exactly one ordinary deletion per read, and two distinct observed outputs. It does not cover multiple deletions, unequal deletion counts, insertions, or arbitrary source constraints. The matching is sharp here, not in the unrestricted reconstruction graph.

## References

1. A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, https://arxiv.org/abs/1211.3128.
2. D. Cullina and N. Kiyavash, *An Improvement to Levenshtein's Upper Bound on the Cardinality of Deletion Correcting Codes*, https://arxiv.org/abs/1302.6562.
3. K. Cai, H. M. Kiah, T. T. Nguyen, and E. Yaakobi, *Coding for Sequence Reconstruction for Single Edits*, https://arxiv.org/abs/2001.01376.
4. J. Chrisnata, H. M. Kiah, and E. Yaakobi, *Optimal Reconstruction Codes for Deletion Channels*, https://arxiv.org/abs/2004.06032.
5. [*Exact one-deletion confusability and capacity of palindromic codes*](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-exact-one-deletion-confusability-and-capacity-of-palindromic-cod--9646637bbf2e), 2026-11-08.
6. [*Exact edge count of the finite-alphabet two-read single-deletion reconstruction graph*](https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-edge-count-of-the-finite-alphabet-two-read-single-deletion--737fed325e91), 2026-10-04.
7. [*A binomial-tree model for binary palindromic single-deletion codes*](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-a-binomial-tree-model-for-binary-palindromic-single-deletion-cod--3c7b3453f9ef), 2026-11-02.
