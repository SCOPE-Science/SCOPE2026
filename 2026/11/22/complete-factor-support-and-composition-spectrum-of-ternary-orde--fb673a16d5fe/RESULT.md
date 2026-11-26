# Complete factor-support and composition spectrum of ternary order-four negative-avoiding cycles

## Finding
Let \(w\) be a cyclic word of length \(40\) over \(\mathbb Z_3\). Call its set of \(40\) cyclic contiguous four-letter factors \(S(w)\). Assume all these factors are distinct and no two are additive negatives of one another (including a factor equal to its own negative). There are **exactly \(218{,}564\) distinct factor sets** \(S(w)\) satisfying these conditions. These are distinct sets, **not** distinct cyclic words. Precisely \(274{,}624\) of the \(2^{40}\) choices of one four-letter factor per nonzero negative pair yield degree-balanced overlap graphs; exactly \(56{,}060\) balanced choices have disconnected nonzero-degree support and cannot be a single cycle. For each realizable support the number of occurrences of the symbol \(0\) is \(13\); the number \(j\) of occurrences of \(1\) is any integer from \(8\) through \(19\), and no other value is attainable. The complete spectrum of distinct support sets is:

| \(j\) | Balanced | Connected, realizable | Disconnected |
|---:|---:|---:|---:|
| 8 | 58 | 58 | 0 |
| 9 | 840 | 774 | 66 |
| 10 | 5522 | 4596 | 926 |
| 11 | 19740 | 15444 | 4296 |
| 12 | 44266 | 34694 | 9572 |
| 13 | 66886 | 53716 | 13170 |
| 14 | 66886 | 53716 | 13170 |
| 15 | 44266 | 34694 | 9572 |
| 16 | 19740 | 15444 | 4296 |
| 17 | 5522 | 4596 | 926 |
| 18 | 840 | 774 | 66 |
| 19 | 58 | 58 | 0 |
| Total | 274624 | 218564 | 56060 |

## Assumptions and scope
The alphabet \(\mathbb Z_3=\{0,1,2\}\) is labeled. Negation is coordinatewise modulo three; in particular, it fixes \(0\) and swaps \(1\) and \(2\). Window order is four, with wraparound, and rotations are not used to identify *factor supports* since a rotation leaves the same support automatically. The 40-window maximum follows from the 40 antipodal pairs of nonzero four-grams (Mitchell–Wild, Theorem 4.1); the present result enumerates the realizable **factor-support sets** at that maximum, not the number of Euler tours or circular words. Letter exchange \(1\leftrightarrow 2\) is **not** quotiented out.

## Proof
There are \(3^4=81\) four-letter words, and only \(0000\) equals its additive negative. The remaining \(80\) words partition into \(40\) disjoint pairs \(\{e,-e\}\). Each eligible length-40 cycle uses exactly one member of each pair. Conversely, any such selection \(S\) produces a directed graph on the \(27\) three-letter vertices: the edge \((a,b,c,d)\) points from \((a,b,c)\) to \((b,c,d)\). A cyclic word with exactly this edge set exists if and only if this graph is balanced at every vertex and all of its nonzero-degree vertices lie in one underlying undirected component. The necessity follows by tracing the word's windows; sufficiency is the directed Euler-circuit theorem. This graph–word equivalence is fully constructive.

For each selected edge, assign the flow \(+1\) at its three-letter prefix vertex, \(-1\) at its suffix vertex. The \(26\) nonzero vertices form \(13\) negative pairs \(\{u,-u\}\). For each \(u\), the selected outdegrees at \(u\) and \(-u\) add to \(3\), because their respective outgoing edges are paired by negation, exactly one per pair. The corresponding indegrees also add to \(3\). Thus the net flow at \(-u\) is the negative of the net flow at \(u\); it suffices to test the \(13\) lexicographically smaller representatives. At \(000\), exactly one edge leaves, from the pair \(\{0001,0002\}\), and exactly one enters, from the distinct pair \(\{1000,2000\}\); the loop \(0000\) is prohibited. So its net flow is identically zero, and the \(13\) equations are necessary and sufficient for balance.

For each antipodal pair, choose bit zero or one according to its lexicographic orientation. Split the \(40\) pairs into two sets of \(20\). An assignment to a half has a \(13\)-coordinate integer imbalance vector and an integer count of selected edges whose first letter is \(1\). Enumerate all \(2^{20}\) assignments in each half, group by imbalance vector, and join only opposite vectors. Every joined pair is exactly one globally balanced selection; no selected four-gram set is produced twice. The exact-integer certificate `verify_supports.cpp` implements this two-half enumeration by Gray-code updates and lexicographic grouping. Its global balanced count by the first-letter-one count is the second column of the table. On every balanced join, an undirected union–find on the 27 graph vertices tests connectedness of the positive-degree support, producing the third column and its complement. This is a finite **exhaustive proof** of the stated numbers, not a sample. A distinct implementation, `verify_supports.py`, uses vectorized Cartesian doubling and integer-key sorting and independently reproduces all counts. Both implementations test every balanced selection, including all potentially disconnected ones.

Finally, exactly \((3^3-1)/2=13\) of the forty antipodal pairs consist of edges beginning with symbol \(0\). Thus every selected support has \(13\) zero-starting edges. In any realized Eulerian circular word, counts of letters are exactly the counts of outgoing edges by first letter, giving 13 zeros and \(j\) ones. Every integer \(8\le j\le19\) occurs because its realizable-count table entry is positive. For an independent existence check, `witnesses.txt` provides explicit circular words for \(j=8,\ldots,13\); negating symbols yields \(j=19,\ldots,14\). `verify_supports.py` checks the displayed witnesses directly.

## Verification
Compile and run `verify_supports.cpp` with a C++17 compiler (for example `g++ -O2 -std=c++17 verify_supports.cpp -o supports && ./supports`); run `python verify_supports.py` with NumPy. The former traverses each half by Gray codes, groups with integer flow keys and uses disjoint sets; the latter builds Cartesian halves in vectorized arrays and groups independently. Each computes exactly 274624 balanced candidates and 218564 connected ones, independently at each composition. Exhaustiveness rests on a bijection between 40-bit choices and antipodal-factor support selections and on exact checks of the 13 representative flow coordinates; finite enumeration is appropriate because the claim is exclusively about the fixed order-four case. The six witness cycles and their negations are length forty and satisfy the distinctness and exclusion conditions by literal checks.

## Relationship to prior work
Mitchell and Wild, *Negative Avoiding Sequences* (first publicly posted March 26, 2026; updated November 2026), establish the negative-factor selection framework, maximum period, and existence. Their ternary order-four example notes that a simple pseudoweight maximizer construction does not realize the maximum but does not enumerate all maximum-period **factor supports**, their Eulerian/disconnected split, or their letter-count spectrum. The earlier *Orientable and Negative Orientable Sequences* studies constraints involving reversal and negative reversal, which are different equivalence relations. Other adjacent de Bruijn and orientable-cycle enumerations cannot be imported by numerical analogy; their forbidden relations and domain differ. The present statement is a factor-support census and is not a claim of a new maximum-period bound.

## Limitations
The proof is fully finite and limited to the ternary alphabet and window length four. It does not count distinct cyclic words, oriented Euler tours, or equivalence classes under alphabet permutation. Its numerical values rely on complete exact enumerations with inspectable sources; no closed symbolic formula across window sizes is asserted. An unindexed equivalent computation is a residual priority risk; no independent external audit is claimed.

## References
1. C. J. Mitchell and P. R. Wild, *Negative Avoiding Sequences*, arXiv:2603.25286, first posted 2026-03-26, https://arxiv.org/html/2603.25286v3 . Theorems 3.2 and 4.1, Example 5.3, and Section 8.
2. C. J. Mitchell and P. R. Wild, *Orientable and Negative Orientable Sequences*, arXiv:2409.00672, https://arxiv.org/abs/2409.00672 .
3. F. Alhakim and coauthors, *Orientable sequences over non-binary alphabets*, arXiv:2407.14866, https://arxiv.org/abs/2407.14866 .
