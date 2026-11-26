# Odd-order extremizers for two-connected permutation inversion graphs

## Finding

For every \(m\ge1\), the minimum inversion count among permutations of length \(2m+1\) whose inversion graph is two-vertex-connected is \(3m\). There are exactly \(3m-2\) such minimizers. Exactly \(m\) of them have one occurrence of the pattern \(321\), and the other \(2m-2\) avoid it.

For \(m\ge2\) the minimizers are precisely the **distinct** permutations obtained by inserting a point of inversion degree two into the even ladder permutation \(L_{2m}\). The table and duplicate classes below specify how to generate each minimizer once. At \(m=1\) the sole minimizer is \(321\).

## Definitions and scope

An inversion graph joins positions \(i<j\) of a permutation \(\pi\) when \(\pi_i>\pi_j\); triangles are precisely occurrences of \(321\). A two-vertex-connected graph has at least three vertices and stays connected on deleting any vertex. Write \(I_{p,v}(a)\) for insertion of rank \(v\) after precisely \(p\) entries of a length-\(r\) permutation \(a\), where \(0\le p\le r\) and \(1\le v\le r+1\); increase each old value at least \(v\) by one. The new degree is
\[
\delta_a(p,v)=\#\{i\le p:a_i\ge v\}+\#\{i>p:a_i<v\}.
\]

Set \(L_4=3412\) and \(L_{r+2}=F(L_r)\) for even \(r\ge4\). The operation \(F\) increments the maximum entry of its input of length \(r\), inserts the new maximum \(r+2\) immediately before the old final entry, and appends \(r\). For example, \(L_6=351624\) and \(L_8=35172846\).

## Proof of the extremum and structural classification

Inversion graphs are 4-chordal, and the two-connected 4-chordal bound is \(|E|\ge 3|V|/2-2\) [1, Proposition 2.8]. For odd order \(2m+1\) this gives at least \(3m\) inversions. At even order \(2m\), \(m\ge2\), the unique minimizer is \(L_{2m}\), with \(3m-2\) edges [1, Remark 3.6]. A new vertex of degree two preserves two-connectivity: deleting it leaves the original graph; deleting an original vertex leaves the new one adjacent to at least one vertex of the connected remainder. Such an insertion exists, for example at \((p,v)=(0,3)\). It adds exactly two inversions, so attains the odd lower bound. At order three only \(321\) has a two-connected graph.

For the converse use an anchored greedy induced ear decomposition [1, Lemmas 2.3, 3.3 and Corollary 2.7]. It starts at a triangle or induced square, and each step adds either one vertex and at least two edges, or two vertices and three edges along the attaching path. If the start is a triangle, with \(a\) two-vertex and \(b\) one-vertex steps, \(2a+b=2m-2\), so \(|E|\ge3+3a+2b=3m+b/2\). Equality forces \(b=0\). If the start is a square, \(2a+b=2m-3\), so \(|E|\ge4+3a+2b=3m+(b-1)/2\). Here \(b\) is odd and positive, and equality forces \(b=1\). In both cases each step has its minimum edge increment. If the last step adds one vertex, the previous permutation is therefore the even extremizer, and the last vertex has degree two. If it adds two, the previous permutation has odd order and is itself extremal. By [1, Lemma 3.5(i)], the new vertices in an anchored two-vertex step are the topmost, third from the right and the rightmost, third from the top, respectively. In ranks this is precisely \(F\). The order-five case reached from a triangle gives \(F(321)=42513=I_{1,2}(L_4)\).

For the induction when \(r\ge4\) is even, the following commutations hold for degree-two cells of \(L_r\):
\[
 F(I_{p,v}(L_r))=
 \begin{cases}
 I_{p,v}(L_{r+2}) & p<r,\ v\le r,\\
 I_{r-3,r}(L_{r+2}) & (p,v)=(r-2,r+1),\\
 I_{r-1,r-2}(L_{r+2}) & (p,v)=(r,r-1).
 \end{cases}
\]
The table below gives no other exceptional cells, including at \(r=4\). In the first case the inserted point precedes the old final entry and the old maximum remains the highest of the initial points of \(F\)'s input. On both sides the old maximum ends at rank \(r+2\), the two points added by \(F\) end at ranks \(r+3,r+1\), and all other ranks and positions agree. To check the exceptions, write \(L_r=(P,r,u,w)\) with \(w=r-2\) and \(u<r-2\), which follows from the recursion even for \(r=4\). In the first exception both words are \((P,r,r+2,u,r+3,w,r+1)\). In the second they are \((P^+,r+2,u,w,r+3,r-1,r+1)\), where \(P^+\) raises the entries of \(P\) at least \(r-1\) (there is no \(r-2\) in \(P\)). Each resulting insertion has degree two, since the resulting extremal word has exactly two more inversions than \(L_{r+2}\). This proves the converse by induction.

## Exact census

For \(r=2m\ge6\), the cells \((p,v)\) of degree two are exactly
\[
\begin{gathered}
 (0,3),(1,2),(1,4),(2,1),\\
 (2j+1,2j),(2j+1,2j+2),(2j+1,2j+4)\quad(1\le j\le m-2),\\
 (r-2,r+1),(r-1,r-2),(r-1,r),(r,r-1).
\end{gathered}
\]
For verification of the table, the word for \(r\ge6\) is \((3,5,1)\), followed by the pairs \((2i+5,2i)\) for \(1\le i\le m-3\), followed by \((r,r-4,r-2)\). This follows by induction from \(F\). For \(t=v-1\) and \(A_p(t)=\#\{i\le p:a_i\le t\}\), the degree is \(p+t-2A_p(t)\). At \(p=0,1,2\) the prefixes are empty, \((3)\), and \((3,5)\), which yield the first row. At \(p=2j+1\), the prefix value set is \([1,2j-2]\cup\{2j-1,2j+1,2j+3\}\), taking the interval as empty when \(j=1\). The degree falls to two at \(t=2j-1\), then alternates between three and two through \(t=2j+3\) and rises thereafter; these are precisely the three cells at that \(p\). At the following even prefix a value is added, raising the degree by one for smaller \(t\) and lowering it by one for \(t\) at least that value. If the value is \(2j+5\), the degree before lowering is already at least four. At the final even prefix \(p=r-2\), the added value is \(r\), and the degree falls to two exactly at \(t=r\). The last two prefixes miss only \(r-2\), or miss nothing. Their degrees are respectively \(r-1-t+2\mathbf1_{t\ge r-2}\) and \(r-t\), giving the remaining cells.

There are \(3m+2\) cells. Two insertions that produce the same permutation must be removable at different positions of that permutation to recover the same standardized word. If the deletion positions are \(i<j\) with values \(a<b\), equality of standardized words at the first shifted index forces the entry right after \(a\) to be \(a+1\); comparing consecutive shifted indices forces the values through \(j\) to be \(a,a+1,\ldots,b\). More explicitly, the entry at position \(k+1\) after removing rank \(a\) must standardize to the same value as the entry at position \(k\) after removing rank \(b\), for \(i\le k<j\); for ranks from \(a\) through \(b-1\) this recurrence increments them by one. The case \(a>b\) follows by complementing values. The word for \(L_r\) shows that it has no adjacent consecutive-value pair for \(r\ge6\). Thus a common run arising from two insertion cells can only have two entries. Such a run formed with the old entry \(a_i=x\) gives the candidate cell pair \((i-1,x)\sim(i,x+1)\) when increasing, or \((i-1,x+1)\sim(i,x)\) when decreasing. Each such pair does indeed give equal insertions whenever its two cells occur. Applying this test to the table leaves exactly four disjoint pairs:
\[
 (0,3)\sim(1,4),\qquad (2,1)\sim(3,2),\qquad
 (r-3,r)\sim(r-2,r+1),\qquad (r-1,r-2)\sim(r,r-1).
\]
Keeping the first cell in each displayed pair and all singleton cells produces \(3m-2\) distinct permutations. For \(r=4\), the two triple classes are \(\{(0,3),(1,4),(2,5)\}\) and \(\{(2,1),(3,2),(4,3)\}\); the singletons are \((1,2)\) and \((3,4)\). They give \(34512,45123,42513,35142\), respectively.

The even ladder is triangle-free. A degree-two insertion creates one triangle if its two old neighbors are adjacent and no triangle otherwise. For the three cells at an interior odd prefix \(p=2j+1\), the neighbors are respectively the two left ranks \(2j+1,2j+3\) in increasing order, the left rank \(2j+3\) and right rank \(2j\), or the two right ranks \(2j,2j+2\) in increasing order. Only the middle case produces a triangle. At the first row of the table, only \((1,2)\) has a left and a right neighbor, the ranks \(3,1\); the other cells use increasing pairs \((1,2)\) on the right or \((3,5)\) on the left. In the final row, only \((r-1,r)\) has a left and a right neighbor, \(r,r-2\); the other cells use increasing pairs \((r-4,r-2)\) on the right or \((r-1,r)\) on the left. The two neighbors of a mixed left-right pair are inverted. Thus the triangular cells are exactly \((2j-1,2j)\) for \(1\le j\le m\); all are distinct singleton classes. For \(r=4\), the two triangle-containing words are the singleton insertions \(42513,35142\). Together with the \(321\) base case this gives the asserted split for all \(m\).

## Verification and limitations

The unchanged `verify.py` checks exhaustive odd orders three, five, seven and nine, even uniqueness through order eight, and the insertion table, distinct counts, triangle counts and commutation identities for even ladder orders through 50. Its terminal marker is `VERIFY_OK`; finite tests are corroboration only. The pair equivalences above follow from the symbolic deletion argument, not from inferring a pattern from the finite counts.

The lower bound, its even-order equality case and the anchored-ear machinery are from Verkama [1]. The odd-order minimum follows directly from the bound and a two-neighbor insertion. The additional conclusion here is the full odd-order classification, its distinct-permutation enumeration and the exact \(321\) split. General insertion-type bounds concern the same rank/position discrepancy but do not themselves constrain extremizers of the two-connectivity problem. The result is only about the minimum-inversion layer at odd order; it makes no claim about higher connectivity, nonminimal inversion counts or unique historical priority.

## References

1. E. Verkama, *Permutation patterns and higher connectivity in inversion graphs*, arXiv:2611.17237v1, preprint. https://arxiv.org/abs/2611.17237. In particular Proposition 2.8, Corollary 2.7, Lemmas 3.3 and 3.5, and Remark 3.6.
2. B. E. Tenner and V. Vatter, *Cyclomatic numbers and permutations*, arXiv:2607.06198. https://arxiv.org/abs/2607.06198.
