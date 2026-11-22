# Forty edge-resolving partitions of the Petersen graph and their complete enumerator

## Finding

Let \(P=KG(5,2)\) be the Petersen graph. Its edge partition dimension is exactly
\[
\boxed{\operatorname{epd}(P)=4}.
\]
There are exactly **40 unlabeled edge-resolving vertex partitions into four nonempty blocks**, all having sorted block sizes \((1,3,3,3)\). They form a single orbit under the natural action of \(S_5\) on the two-subsets of five labels. More generally, the cardinality enumerator of all edge-resolving partitions is
\[
\boxed{E_P(z)=40z^4+11965z^5+14877z^6+5045z^7+720z^8+45z^9+z^{10}.}
\]
In particular, there are exactly \(32693\) edge-resolving partitions, counted without block order. A representative optimum has the four blocks
\[
\{v_{01}\},\quad \{v_{02},v_{13},v_{24}\},\quad
\{v_{03},v_{14},v_{23}\},\quad \{v_{04},v_{12},v_{34}\}.
\]
The result distinguishes *edge* partitions from ordinary vertex-resolving partitions. Its value \(4\) also contradicts a later published claim of value \(6\); the present proof supplies both the four-block witness and an exhaustive lower bound.

## Assumptions and scope

The graph is simple, undirected and unweighted. Its vertices are \(v_{ab}=\{a,b\}\) for \(0\le a<b\le4\); two vertices are adjacent precisely when their underlying two-subsets are disjoint. It has ten vertices, fifteen edges and diameter two. For a graph edge \(e=uv\) and nonempty vertex block \(B\), define
\[
d_P(e,B)=\min_{w\in B}\min\{d_P(u,w),d_P(v,w)\}.
\]
An *edge-resolving partition* is an unordered set of nonempty pairwise disjoint vertex blocks whose union is the vertex set, such that for every two distinct graph edges \(e\ne f\) there is a block \(B\) with \(d_P(e,B)\ne d_P(f,B)\). The edge partition dimension is the least number of blocks in such a partition. Reordering the blocks changes only the coordinate order and is not counted as a distinct partition. All counts here refer to this standard global edge-resolving condition, not the condition comparing only incident edges.

## Proof

**Distance formula and a direct four-block witness.** For distinct vertices of \(KG(5,2)\), graph distance is one for disjoint two-subsets and two for intersecting two-subsets. The displayed four-block partition yields the following fifteen distinct edge-distance vectors. For the edges written as pairs of two-digit vertex labels, the vectors in block order are:

```
01-23: 0101    01-24: 0011    01-34: 0110
02-13: 2011    02-14: 2001    02-34: 1010
03-12: 2100    03-14: 2101    03-24: 1001
04-12: 2110    04-13: 2010    04-23: 1100
12-34: 1110    13-24: 1011    14-23: 1101
```

Thus \(\operatorname{epd}(P)\le4\). The complete enumeration below shows no one-, two- or three-block edge-resolving partition.

**Exhaustiveness.** Every unordered partition of ten labelled vertices into \(k\) nonempty blocks corresponds bijectively to a unique restricted-growth word \((c_0,\ldots,c_9)\) with \(c_0=0\) and \(0\le c_i\le 1+\max_{j<i}c_j\). The block count is \(1+\max_i c_i\). At the next position, appending each existing label or the one new label generates every partition once. Thus the supplied enumerators inspect exactly the \(B_{10}=115975\) set partitions, not a sample. For each partition, they calculate for each edge and block the exact minimum over its vertices, and accept the partition if and only if the fifteen resulting vectors are pairwise different. The counts by number of blocks are
\[
(0,0,0,40,11965,14877,5045,720,45,1)
\]
for \(k=1,2,\ldots,10\). This proves the polynomial and the lower bound.

**A reduced obstruction check for three blocks.** If an edge joins blocks \(B_i,B_j\) of a three-block partition, its first two corresponding distances are zero; its distance to the remaining block is either one or two. Hence no pair of blocks can contain more than two crossing edges, and the total number of crossing edges is at most six. Of the \(\left\{\begin{smallmatrix}10\\3\end{smallmatrix}\right\}=9330\) three-block partitions, exactly 105 have at most six crossing edges. Exactly 15 of these have at most two edges between each block pair. In all fifteen, the other two blocks are adjacent singleton vertices and the first block contains the other eight vertices. The two edges connecting one singleton to the eight-vertex block then have identical signatures (zero to the singleton and large block, one to the other singleton). This independent necessary-condition screen rules out three blocks. The stated counts are computed from the explicit graph edges by both included verifiers, without relying on an untested structural assertion.

**Classification and symmetry.** Every accepted four-block partition has block-size profile \((1,3,3,3)\); there are exactly forty. The group \(S_5\) preserves disjointness and therefore edge-distance signatures. Acting on the displayed representative by all 120 ground-label permutations produces forty distinct partitions, and the resulting set equals the complete forty-partition list. Hence all minima form one natural symmetry orbit. No unexamined automorphism assumption is used.

## Verification

Two standalone, independently organized programs compute the same result from different graph representations. `check_kneser.cpp` builds the disjointness graph of all ten two-subsets, enumerates restricted-growth words, calculates exact edge-signature vectors, checks the three-block obstruction and enumerates the \(S_5\) orbit. It requires a standard C++17 compiler. `check_gp.py` uses Python's standard library, constructs \(GP(5,2)\) from its outer pentagon, inner step-two cycle and spokes, reconstructs vertex distances by breadth-first search, independently enumerates set partitions and confirms the entire graph-automorphism orbit by enumerating the 120 automorphisms.

Run from the artifact directory:

```
g++ -std=c++17 -O2 check_kneser.cpp -o check_kneser
./check_kneser
python3 check_gp.py
```

The outputs must end with `KG5_CHECK_OK` and `GP_CHECK_OK`. Expected complete program output is provided in `check_kneser.out` and `check_gp.out`. The programs contain assertions on every numerical claim above. The evidence is an exhaustive finite computation with a complete explicit search space, **not** extrapolation from selected examples.

## Relationship to prior work

Kuziak, Maritz, Vetrík and Yero (2023) defined edge-resolving vertex partitions and proved general bounds, as well as values on paths, cycles and various multipartite graphs. Their result does not determine the Petersen graph's complete edge-partition census. Ali, Ahmad and Jamil (2024), Theorem 16 and summary Table 10, report \(\operatorname{epd}(P)=6\); a directly verified four-block counterexample and the exhaustive proof here establish the incompatible value \(4\), with the exact forty-minimum classification. The 2024 paper also discusses *local* edge partition dimension, which is a different invariant; this theorem concerns the global edge partition dimension defined in 2023.

The previously published classification of 7040 minimum *vertex*-resolving partitions of the Petersen graph does not give the edge-resolution result. Vertex signatures distinguish ten vertices; the new condition instead distinguishes fifteen edges, and only forty four-block partitions meet that latter requirement. Neither the published scalar claim of six nor the 7040 vertex-partition count implies the present result.

## Limitations

This is an exact finite theorem only for the ordinary ten-vertex Petersen graph; there is no claimed formula for all generalized Petersen or Kneser graphs. The enumeration counts partitions with unordered blocks, not color-labelled assignments. No external independent scholarly validation has been performed, and an unindexed earlier enumeration of the same invariant cannot be ruled out. The 2024 contrary assertion was compared against the actual published text; no inference about author intentions is made.

## References

1. D. Kuziak, E. Maritz, T. Vetrík and I. G. Yero, *The edge partition dimension of graphs*, Discrete Mathematics Letters **12** (2023), 34–39, first published 2023-03-30, DOI:10.47443/dml.2023.010. https://www.dmlett.com/archive/v12/DML23_v12_pp34-39.pdf
2. S. Ali, F. Ahmad and M. K. Jamil, *The novel resolvability parameter, local edge partition dimension of graphs*, Open Journal of Discrete Applied Mathematics **7** (2024), 59–71, first published 2024-12-22, DOI:10.30538/psrp-odam2024.0105. https://pisrt.org/psrpress/j/odam/2024/3/The-novel-resolvability-parameter-local-edge-partition-dimension-of-graphs.pdf
3. *The 7,040 optimal resolving partitions of the Petersen graph form a diameter-eight relocation network*, publicly accessible mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-7-040-optimal-resolving-partitions-of-the-petersen-graph-for--fa2b190525a1
