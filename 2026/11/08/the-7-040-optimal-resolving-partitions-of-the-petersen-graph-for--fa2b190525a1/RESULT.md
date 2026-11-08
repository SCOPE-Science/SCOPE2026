# The 7,040 optimal resolving partitions of the Petersen graph form a diameter-eight relocation network

## Finding

For the Petersen graph \(P=KG(5,2)\), let \(\mathscr P\) be the family of *unlabeled* resolving partitions into the minimum number of blocks. Let \(R\) have vertex set \(\mathscr P\), with an edge between two partitions if they differ only by moving a single original graph vertex from its present block to a different block, while leaving every block nonempty and maintaining the resolving condition. The move does **not** require the old and new blocks to contain adjacent graph vertices.

The exact result is
\[
\operatorname{pd}(P)=4,\qquad |V(R)|=7040,\quad |E(R)|=34500,\quad R\text{ connected},\quad \operatorname{rad}(R)=7,\quad\operatorname{diam}(R)=8.
\]
The eccentricity distribution is \(6300\) states of eccentricity \(7\) and \(740\) states of eccentricity \(8\). The degree multiplicities, in `degree:count` notation, are
```
3:20, 4:60, 5:300, 6:720, 7:660, 8:840, 9:660, 10:1380,
11:240, 12:780, 13:540, 14:240, 15:400, 16:120, 18:20, 19:60
```
The sorted block-size profiles and counts are
```
(1,1,1,7):20; (1,1,2,6):60; (1,1,3,5):60;
(1,1,4,4):60; (1,2,2,5):960; (1,2,3,4):1920;
(1,3,3,3):240; (2,2,2,4):1320; (2,2,3,3):2400.
```
There are no optimal partitions of any other shape.

## Assumptions and scope

All graphs are finite, simple, undirected. The vertices of \(P\) are the ten two-element subsets of \(\{0,1,2,3,4\}\), with two distinct vertices adjacent precisely when they are disjoint. For nonempty \(B\subseteq V(P)\), define \(d(v,B)=\min_{w\in B}d_P(v,w)\). An unordered partition \(\Pi=\{B_1,\ldots,B_k\}\) is *resolving* when the \(k\)-component vectors \((d(v,B_1),\ldots,d(v,B_k))\) distinguish all ten vertices. The definition is unaffected by simultaneous permutation of components and blocks. A *minimum* resolving partition has the smallest possible \(k\), not necessarily the fewest vertices in any one block. Relocation is a **one-vertex block transfer**; it is neither a swap of two vertices nor a token slide along an edge of \(P\).

## Proof

**Distance and local-resolvability lemma.** In \(KG(5,2)\), two distinct vertices are distance \(1\) exactly when their two-element labels are disjoint, and distance \(2\) otherwise: if they intersect, their two-element union has size three, and the complementary two-element subset is adjacent to both. Consequently, for any partition \(\Pi\), vertices in distinct blocks already have different distance signatures (their zero coordinates differ). For two distinct vertices \(u,v\) in the *same* block, \(\Pi\) resolves them exactly when some other block \(B\) contains a neighbor of exactly one of \(u,v\) **in the sense of block adjacency**: \(N(u)\cap B\ne\varnothing\) and \(N(v)\cap B=\varnothing\), or vice versa. Equivalently, the two distances to \(B\) are \(1\) and \(2\). This is necessary and sufficient, not a heuristic check.

**Exhaustive canonical partition lemma.** A set partition of ten labelled vertices into exactly \(k\) nonempty *unlabeled* blocks is uniquely encoded by a restricted-growth word \((a_0,\ldots,a_9)\), with \(a_0=0\), \(0\le a_i\le 1+\max_{j<i}a_j\), and \(\max_i a_i=k-1\). Starting with the singleton prefix \((0)\), the program `check_partition_kneser.cpp` generates these words by visiting each allowed value in ascending order, excluding values \(\ge k\), and tests the exact preceding local-resolvability condition. No valid partition is missed or repeated. For three blocks the exhaustive count is \(0\); for four blocks it is \(7040\). The impossibility of one block is immediate, and two blocks cannot resolve this ten-vertex diameter-two nonpath (also independently directly checked by `check_partition_gp.py`, which returns zero two-block resolving partitions). Thus \(\operatorname{pd}(P)=4\). The four-block census and shape distribution follow from this complete finite enumeration.

**Exact relocation certificate.** For each of the \(7040\) canonical four-block words, consider every vertex belonging to a block of size at least two, and replace its block label by each of the three alternative existing labels. Canonicalize the resulting word by relabeling the blocks in first-occurrence order, and retain the move exactly if the resulting canonical word belongs to the certified \(7040\)-word family. Every valid move has this form, and no other move meets the definition. Deduplication gives \(34500\) unoriented edges. Adjacency symmetry is checked explicitly.

Breadth-first search on this full graph from *every one* of its \(7040\) states visits all \(7040\) states. The maximum search depth is exactly \(7\) for \(6300\) starts and exactly \(8\) for \(740\) starts. It follows directly from the definition of eccentricity that \(R\) is connected, its radius is \(7\), and its diameter is \(8\). The exact unordered distance histogram is
```
1:34500; 2:233280; 3:1216140; 4:4667580;
5:10539140; 6:7642490; 7:442110; 8:2040.
```
These coefficients sum to \(\binom{7040}{2}=24777280\), providing a further exact consistency check. Since the finite state space is specified exhaustively, this exhaustive checker is a finite proof, not extrapolation from selected examples.

## Verification

`check_partition_kneser.cpp` is dependency-free C++17. From the directory containing it run `g++ -O3 -std=c++17 check_partition_kneser.cpp -o check_partition_kneser && ./check_partition_kneser`; compare with `check_partition_kneser.out`. The program computes all states, transitions, connected components and every pair distance; exits nonzero when a critical invariant differs. `check_partition_gp.py` uses only Python's standard library, builds the independent generalized Petersen graph \(GP(5,2)\) directly using a five-cycle, spokes and inner step-two edges, finds graph distances by BFS, enumerates partitions anew, and reconstructs all transitions. Run `python3 check_partition_gp.py`, comparing with `check_partition_gp.out`. Its independent counts, shape profile, degree histogram and connectivity agree, with additional representative eccentricity checks. The familiar isomorphism \(GP(5,2)\cong KG(5,2)\) is explicit: the outer five-cycle has two-element labels \((01,23,04,12,34)\), and the corresponding inner five vertices have labels \((24,14,13,03,02)\). Both outputs are included as reproducibility records, but the programs, not logs alone, specify and check the finite calculation.

## Relationship to prior work

Chartrand–Salehi–Zhang (2000) introduced the partition dimension and general resolving-partition framework; the known scalar dimension is not claimed as new. Rodríguez-Velázquez–Yero–Kuziak (2010) study partition dimension of **corona products**, rather than the full space of optimal resolving partitions on the Petersen graph or transitions among them. Raza–Liu–Azeem–Nadeem (2021), whose full article was inspected, give general upper bounds for **generalized Petersen graphs of substantially larger order**; these bounds do not imply the \(7040\)-state census, transition graph, or diameter. In contrast to ordinary proper-coloring reconfiguration, blocks here need not be independent sets. Equating the two would change the configuration space.

## Limitations

This is an exact finite result for the ten-vertex Petersen graph only. There is no statement that all generalized Petersen graphs have connected relocation networks, or that the diameter formula extends with graph order. The resulting finite algorithm is complete but not a symbolic classification of its automorphism orbits. The 2000 foundational article was available only as an abstract/preview; possible unindexed prior exhaustive computations cannot be excluded and require independent literature vetting. Independent scholarly audit has not yet been performed.

## References

1. J. A. Rodríguez-Velázquez, I. G. Yero and D. Kuziak, *The partition dimension of corona product graphs*, arXiv:1010.5144v1 (first made public 2010-10-25). https://arxiv.org/html/1010.5144v1
2. G. Chartrand, E. Salehi and P. Zhang, *The partition dimension of a graph*, Aequationes Mathematicae 59 (2000), 45–54, DOI:10.1007/PL00000127. https://link.springer.com/article/10.1007/PL00000127
3. H. Raza, J.-B. Liu, M. Azeem and M. F. Nadeem, *Partition Dimension of Generalized Petersen Graph*, Complexity (2021), article 5592476, DOI:10.1155/2021/5592476. https://onlinelibrary.wiley.com/doi/10.1155/2021/5592476
