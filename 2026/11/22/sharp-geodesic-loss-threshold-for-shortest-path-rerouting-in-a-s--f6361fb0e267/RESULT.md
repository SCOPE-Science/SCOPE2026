# Sharp geodesic-loss threshold for shortest-path rerouting in a singly punctured Boolean cube

## Finding

Let \(n\ge2\), \(1\le k\le n-1\), and let \(v\in\{0,1\}^n\) have Hamming weight \(k\). Consider all shortest paths from \(0^n\) to \(1^n\) in the Boolean cube after deleting \(v\). Join two such paths when one intermediate cube vertex is changed and every intermediate route is still a shortest, \(v\)-avoiding route. Write \(\mathcal R_{n,k}\) for this reconfiguration graph. Then:

1. \(\mathcal R_{n,k}\) is connected and has exactly \(n!-k!(n-k)!\) vertices. It has
   \[
   |E(\mathcal R_{n,k})|=\frac{(n-1)n!-n\,k!(n-k)!}{2}.
   \]
   Exactly \(k!(n-k)!\) vertices have degree \(n-2\); every other vertex has degree \(n-1\).
2. With the natural permutation encoding of cube geodesics, the graph metric of \(\mathcal R_{n,k}\) agrees **on every pair** with unrestricted Kendall adjacent-transposition distance if and only if \(k=1\) or \(k=n-1\).
3. For every \(2\le k\le n-2\), two explicit valid routes have Kendall distance \(4\) but constrained reconfiguration distance **exactly \(6\)**. Thus a single failed internal cube vertex first produces a strict shortest-rerouting detour at \(n=4\), precisely at the non-extreme Hamming layers.

The distinction is between preserving the length of each underlying cube route (which remains \(n\)) and preserving the minimum number of *changes between routes* (which can grow). The deleted vertex excludes only the fraction \(1/\binom nk\) of the original cube geodesics, yet it changes the rerouting metric at every interior layer.

## Assumptions and scope

The cube has vertices \(\{0,1\}^n\) and edges between words differing in one coordinate. Endpoints are \(0^n\) and \(1^n\). A shortest path changes each coordinate from zero to one exactly once, so it is encoded by a permutation \(p=(p_1,\ldots,p_n)\) of \([n]\). Put \(A=\operatorname{supp}(v)\), \(|A|=k\), and \(B=[n]\setminus A\), \(|B|=m=n-k\). A path passes through \(v\) if and only if \(\{p_1,\ldots,p_k\}=A\). In particular, a valid permutation is one for which at least one element of \(B\) precedes an element of \(A\).

A reconfiguration step exchanges two adjacent entries of a valid permutation, with the resulting permutation remaining valid. For two permutations \(p,q\), write \(\tau(p,q)\) for the number of unordered pairs of labels with opposite relative orders in \(p\) and \(q\). This is their unrestricted Kendall distance. An isometric embedding here means that the **induced feasible adjacent-swap graph** preserves this metric; no claim is made about geometric isometric embeddings of the cube itself.

## Proof

**Permutation reduction.** Changing the order of two consecutive coordinate flips changes exactly one intermediate cube vertex. Conversely, two shortest cube routes differing at exactly one intermediate vertex must have the same prefixes and suffixes and exchange the order of two consecutive flips. Hence \(\mathcal R_{n,k}\) is precisely the subgraph of the adjacent-transposition permutahedron induced by permutations without the forbidden first-\(k\) set \(A\).

**Connectivity.** From any valid permutation, repeatedly swap an adjacent \(A,B\) pair into the order \(B,A\). Every such swap increases the number of cross pairs in the order \(B\) before \(A\); this number was positive initially, so every intermediate permutation is still valid. The process ends with all \(B\) symbols before all \(A\) symbols. In that state adjacent swaps within the \(B\) block and within the \(A\) block are all valid, and they can sort the labels in each block to a fixed common canonical permutation. Thus all valid permutations are connected.

**Counts and degrees.** The forbidden permutations form a facet of the permutahedron comprising \(F=k!m!\) permutations, so there are \(n!-F\) valid ones. Each forbidden permutation has exactly \((k-1)+(m-1)=n-2\) forbidden adjacent-swap neighbors: exchanges internal to its two blocks. Its only neighbor outside the facet is produced by exchanging positions \(k\) and \(k+1\). These outside neighbors are all distinct: the single \(B,A\) inversion at the block boundary uniquely determines its forbidden precursor. Consequently exactly \(F\) valid permutations lose one of the unrestricted degree-\(n-1\) edges; the other \(n!-2F\) lose none. The degree sum gives
\[
2|E|=F(n-2)+(n!-2F)(n-1)=(n-1)n!-nF.
\]
The argument includes \(n=2\), where the sole valid state has degree zero.

**Isometry at the extreme layers.** Suppose \(k=1\), so validity means that the unique \(A\) label cannot be first. Given two valid permutations \(p,q\), perform standard left-to-right adjacent-insertion sorting of \(p\) toward \(q\): bring the first target label \(q_1\) to the first position, then fix the second position, and so on. Because \(q_1\notin A\), the first entry never becomes the forbidden \(A\) label during the initial insertion: it is the original non-\(A\) first entry until \(q_1\) arrives. Thereafter the first entry is permanently \(q_1\), so every subsequent state is valid. The algorithm swaps each pair with discordant orders exactly once and hence has \(\tau(p,q)\) steps. No route could be shorter, since an adjacent swap changes just one pair order. For \(k=n-1\), validity means that the unique \(B\) label cannot be last. Reverse the ordering and apply the same argument. Thus these extreme-layer induced graphs are isometric in the full adjacent-swap graph.

**A necessary detour at every interior layer.** Let \(2\le k\le n-2\). Choose distinct \(a,a'\in A\) and \(b,b'\in B\), and let \(U\) be any ordering of the other \(k-2\) labels of \(A\), and \(V\) any ordering of the other \(m-2\) labels of \(B\). Consider
\[
p=U\,a\,b\,a'\,b'\,V,\qquad q=U\,a'\,b'\,a\,b\,V.
\]
Both are valid. They disagree on exactly four pair orders, so \(\tau(p,q)=4\). On any hypothetical four-swap route, no pair with the same relative order at both endpoints can be swapped. In particular, the relative orders \(a\prec b\) and \(a'\prec b'\) must always hold, while every \(U\) label precedes every moving label and every moving label precedes every \(V\) label. The only possible cross inversions in the moving four-letter window are \(b\prec a'\) (true initially) and \(b'\prec a\) (true finally). They cannot hold simultaneously, because together with the two fixed orders they would imply the impossible cyclic inequalities \(a\prec b\prec a'\prec b'\prec a\). As each adjacent swap changes one pair order, a four-swap route would at some point have neither cross inversion; at that point all \(A\) labels precede all \(B\) labels, and the forbidden vertex is visited. This contradicts feasibility.

The following six swaps avoid that state (with \(U,V\) unchanged):
\[
\begin{aligned}
a\,b\,a'\,b'&\to b\,a\,a'\,b'\to b\,a'\,a\,b'\\
&\to b\,a'\,b'\,a\to a'\,b\,b'\,a\\
&\to a'\,b'\,b\,a\to a'\,b'\,a\,b.
\end{aligned}
\]
Every displayed word has a \(B\) symbol before an \(A\) symbol. Since the full adjacent-swap graph is bipartite by permutation parity, a feasible route longer than Kendall distance \(4\) cannot have length \(5\). Consequently the true distance is exactly \(6\). This proves the claimed if-and-only-if threshold and its sharp first occurrence.

## Verification

Run `python3 verify.py` with the Python standard library. The checker independently constructs admissible permutations, their adjacent-swap edges, BFS shortest paths, and degree/edge counts for every \(2\le n\le8\) and every \(1\le k<n\) (28 cases). It exhaustively checks Kendall isometry at both extreme layers through \(n=6\), and verifies the exact distance-six witnesses for all interior layers through \(n=8\). For \(n\le6\), it also reconstructs cube path vertex sequences and independently identifies rerouting edges from one-intermediate-vertex changes, confirming the permutation reduction. All checks passed. The infinite assertions follow from the preceding proof, not the finite computations.

## Relationship to prior work

Asplund et al., *Reconfiguration graphs of shortest paths* (2017), Proposition 27, identify the unrestricted antipodal-cube shortest-path graph as an adjacent-transposition Cayley graph. Gajjar et al., *Reconfiguring Shortest Paths in Graphs* (first public 2021; subsequently AAAI 2022 and Algorithmica 2024), Section 5.4 and Theorem 5, establish unrestricted shortest rerouting length equal to Kendall distance. The present result instead removes one intermediate cube vertex and classifies exactly when that equality persists, while showing connectivity and quantifying the lost routes and affected edges.

The non-leaving-face property for permutahedra concerns shortest paths **between vertices within the same retained face**; it does not assert geodesic preservation after deleting that entire face. Classical faulty-cube routing concerns short paths *in the cube after failures*, not adjacent-step reconfiguration *between shortest cube paths*. These conclusions are not interchangeable.

## Limitations

No closed formula for arbitrary pairwise distances at interior Hamming layers is claimed. The six-step pair demonstrates the sharp smallest positive excess over Kendall distance; it does not prove a universal two-step upper bound on the excess or characterize all pairs with excess. The evidence of priority is limited to the referenced primary literature and accessible overlap searches; an unindexed equivalent may exist. Independent validation has not been carried out.

## References

- J. Asplund, K. Edoh, R. Haas, Y. Hristova, B. Novick, B. Werner, *Reconfiguration graphs of shortest paths*, arXiv:1705.09385v1, first public 2017-05-25; Proposition 27. https://arxiv.org/abs/1705.09385
- K. Gajjar, A. V. Jha, M. Kumar, A. Lahiri, *Reconfiguring Shortest Paths in Graphs*, arXiv:2112.07499v1, first public 2021-12-14; Section 5.4 / Theorem 5 in the expanded version. https://arxiv.org/abs/2112.07499 ; https://doi.org/10.1007/s00453-024-01263-y
- C. Ceballos, A. Pilaud and collaborators, *W-associahedra have the non-leaving-face property*, European Journal of Combinatorics 62 (2017), 272–285. https://doi.org/10.1016/j.ejc.2017.01.006
- Q.-P. Gu and S. Peng, *Optimal algorithms for node-to-node fault tolerant routing in hypercubes*, The Computer Journal 39 (1996), 626–629. https://doi.org/10.1093/comjnl/39.7.626
