# Exact partition spectrum of total outer-independent coalitions in complete multipartite graphs

## Finding
Let \(r\ge3\) and let \(G=K_{n_1,\ldots,n_r}\) be a finite simple complete multipartite graph with **nonempty labelled** partite classes \(P_1,\ldots,P_r\), where each \(n_i=|P_i|\ge1\). Set \(N=\sum_{i=1}^{r}n_i\), and let \(c_G(k)\) count unordered vertex partitions into exactly \(k\) nonempty classes, none of which is a total outer-independent dominating set (TOIDS), such that each class has another class whose union with it is a TOIDS.

Put \(a_i=2^{n_i}-1\). **The full partition-size spectrum** is
\[
 c_G(k)=\begin{cases}
 2^{N-1}-1-\sum_{i=1}^r a_i,&k=2,\\
 \displaystyle\sum_{1\le i<j\le r}a_i a_j-2\mathbf 1_{\{r=3\}},&k=3,\\
 0,&\text{otherwise}.
 \end{cases}
\]
In particular, \(c_G(3)>0\), so the largest admissible number of classes is \(3\). The latter scalar equality was previously established for noncomplete complete multipartite graphs and for complete graphs; **it is not claimed here as a new finding**.

The structural classification is exact: a two-class partition is admissible if and only if **each class meets at least two partite sets**. A three-class partition is admissible if and only if **at least two classes are each contained in distinct partite sets**. For three classes the coalition graph is the path on three vertices, except for the unique partition \(\{P_1,P_2,P_3\}\) when \(r=3\), whose coalition graph is the triangle. Thus the partition spectrum refines the earlier extremal number by counting and classifying every admissible partition and every resulting coalition-graph type.

For example, on the labelled graph \(K_{2,2,2}\), there are exactly \(22\) admissible two-class partitions and \(25\) admissible three-class partitions; one of the latter has a triangular coalition graph.

## Assumptions and scope
The graph has at least three nonempty independent partite sets and every pair of vertices from different parts is adjacent. Vertices are labelled, while the blocks of a partition are unordered. A set \(D\subseteq V(G)\) is a TOIDS if every vertex has a neighbor in \(D\) and \(V(G)\setminus D\) is independent. Two disjoint non-TOIDS vertex sets form a coalition precisely when their union is a TOIDS. An admissible partition has at least two nonempty blocks and every block must have a coalition partner.

No balanced-part assumption is used; the result allows all singleton parts, arbitrary unequal part sizes, and \(r\) itself to vary. The original complete and complete-bipartite scalar calculations are not attributed to this work.

## Proof
**1. Characterization of TOIDS.** An independent vertex set of \(G\) is a subset of a single partite set (including the empty set). Thus a TOIDS \(D\) necessarily has \(V(G)\setminus D\subseteq P_i\) for some \(i\). Conversely, if the complement lies in \(P_i\), then \(D\) contains every vertex of the other \(r-1\ge2\) parts. Therefore every vertex, including every selected vertex, has a neighbor in \(D\), and the complement is independent. Hence
\[
 D\text{ is a TOIDS}\quad\Longleftrightarrow\quad V(G)\setminus D\subseteq P_i\text{ for some }i.
\]
The equivalence also holds for \(D=V(G)\), whose complement is empty.

**2. No admissible partition has four or more blocks.** Suppose \(\Psi\) has at least four classes. Pick coalition partners \(A,B\in\Psi\). By the characterization, all remaining classes together lie in one partite set \(P\). Choose one remaining class \(C\), and note that at least one other remaining class exists. Because \(C\) has a partner, it either partners \(A\), partners \(B\), or partners another remaining class. In the first case the complement of \(A\cup C\), which contains \(B\) and another nonempty class inside \(P\), must lie wholly in \(P\). Thus \(B\subseteq P\), so \(V(G)\setminus A\subseteq P\) and \(A\) itself is a TOIDS, a contradiction. The case of partnership with \(B\) is symmetric. The union of two remaining classes lies in \(P\) and cannot be a TOIDS, because a TOIDS contains all vertices outside some part, including vertices from at least two different parts. This is the final contradiction.

**3. The two-class criterion and count.** With two classes \(\{A,B\}\), their union is \(V(G)\), always a TOIDS. Neither class may itself be a TOIDS. By Step 1, this is equivalent to neither \(A\) nor \(B\) lying in one part, or, equivalently, both meeting at least two parts. There are \(2^{N-1}-1\) unordered partitions into two nonempty blocks. The forbidden partitions have a unique nonempty block contained in a single part \(P_i\): there are \(2^{n_i}-1=a_i\) choices of this block. Uniqueness follows because two pure blocks could not cover all three or more nonempty parts. Subtraction gives the displayed \(c_G(2)\).

**4. The three-class criterion.** Consider three non-TOIDS classes \(\{A,B,C\}\). The coalition graph on these classes has no isolated vertex, so it contains at least two of the possible three edges. The edge \(AB\) exists exactly when the opposite class \(C\) lies in one part, by Step 1. Thus at least two of \(A,B,C\) are contained in individual partite sets. If two such classes lie in the same part, their union lies in that part, so the remaining class is itself a TOIDS, forbidden. Hence the two pure classes lie in **distinct** parts. Conversely, if \(A\subseteq P_i\) and \(B\subseteq P_j\) are nonempty for distinct \(i,j\), with \(C=V(G)\setminus(A\cup B)\), then all three are nonempty because \(r\ge3\). The set \(C\) is not a TOIDS, because its complement meets two parts; neither pure class is a TOIDS. Both \(A\cup C\) and \(B\cup C\) are TOIDS, establishing admissibility.

**5. The three-class count and coalition graph.** Choose \(i<j\), a nonempty subset \(A\subseteq P_i\), and a nonempty subset \(B\subseteq P_j\); let \(C\) be the complement. This produces \(\sum_{i<j}a_i a_j\) representations of admissible unordered partitions. All such representations are unique unless all three blocks are pure. Since all \(r\) parts must be covered, that exceptional case requires \(r=3\), and the sole exceptional partition is \(\{P_1,P_2,P_3\}\). It has three representations rather than one, so subtract two. In the exceptional case each pair of classes is a coalition; otherwise exactly the two pairs meeting the unique mixed class are coalitions. Together with Step 2, this proves every asserted formula and classification.

**6. Existence and an asymptotic consequence.** Choosing one vertex from each of two distinct parts and using the complementary class gives an admissible three-class partition, so \(c_G(3)>0\). For balanced parts \(n_1=\cdots=n_r=m\), fixed \(r\ge3\), the fraction of admissible partitions with three blocks is asymptotic to \(r(r-1)2^{-(r-2)m}\), even though three is the maximum block count. This follows by retaining the leading terms \(c_G(2)\sim2^{rm-1}\) and \(c_G(3)\sim\binom r2 2^{2m}\).

## Verification
The accompanying standalone `verify.py` independently implements total domination and outer independence using adjacency masks, enumerates all unordered set partitions, and tests every coalition pair directly. It checks every sorted positive part-size profile with at least three parts and total order at most nine, comprising \(67\) distinct profiles; all \(13{,}339\) accepted partitions match the formulas (\(8{,}199\) with two blocks and \(5{,}140\) with three). It also tests the coalition-graph classification. The final replay prints `VERIFY_OK`.

The unrestricted theorem rests on the preceding proof; finite enumeration is a consistency check, not an infinite proof. Reproduction requires only Python 3: `python verify.py`.

## Relationship to prior work
Buntina and Golmohammadi introduced the TOI-coalition partition and proved general bounds and exact scalar values for complete graphs, complete bipartite graphs, paths, and cycles in arXiv:2607.23623. In particular, the complete-bipartite scalar result grows with the larger part, unlike the constant scalar value for three or more parts. A previous separate complete-multipartite scalar classification already establishes the bound of three for noncomplete graphs with at least three parts; our contribution is **not** that bound, but the complete structural classification and exact labelled counts \(c_G(2)\), \(c_G(3)\), together with the coalition-graph census.

Nearby mathematical studies of total outer-component domination, total restrained coalitions, locating-dominating coalitions, and outer-independent Roman functions use different defining predicates. Their set-count or coalition-number formulas do not imply the TOI partition classification or its exact enumeration by an immediate parameter identification. Search and literature comparison did not identify an existing formula for these partition counts; historical priority is nevertheless provisional.

## Limitations
The theorem applies to complete multipartite graphs with at least three nonempty parts, not to arbitrary graphs, complete bipartite graphs, or arbitrary graph joins. The largest coalition number itself was known in this domain and is not presented as a novelty. The count assumes labelled vertices and unordered blocks. Independent mathematical verification and historical-priority certification have not been performed.

## References
1. O. Buntina and H. Golmohammadi, *Total outer-independent coalition in graphs*, arXiv:2607.23623v1 (first publicly submitted 2026-07-26); revised version also lists J. C. Valenzuela-Tripodoro. https://arxiv.org/abs/2607.23623.
2. *Total outer-independent coalition number of noncomplete multipartite graphs with at least three parts*, prior scalar classification (2026). This result is acknowledged for the scalar invariant; its scientific statement does not give the all-partition count proved here.
3. S. Alikhani and N. Ghanbari, *Super Coalition Number in Graphs*, arXiv:2607.22686 (2026), https://arxiv.org/abs/2607.22686. The super-domination predicate differs from total outer-independence.
