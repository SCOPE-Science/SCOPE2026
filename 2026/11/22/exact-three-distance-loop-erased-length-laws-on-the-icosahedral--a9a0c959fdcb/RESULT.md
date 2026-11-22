# Exact three-distance loop-erased length laws on the icosahedral graph

## Finding
Let \(G\) be the simple icosahedral graph (12 vertices, 30 edges). Choose a uniform spanning tree \(\mathcal T\) and two distinct specified vertices \(s,t\) at ordinary graph distance \(d\in\{1,2,3\}\). Let \(L\) be the number of edges in the unique \(s\)-to-\(t\) tree path. Equivalently, \(L\) is the length of the chronological loop-erasure of simple random walk from \(s\) stopped upon first hitting \(t\).

The complete law is \(\Pr(L=k\mid d)=N_{d,k}/5{,}184{,}000\), where the following table gives **integer numerators**, with zero in each blank entry. The answer holds for every one of the 66 unordered vertex pairs, not just selected representatives.

| \(d\backslash k\) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1900800 | 1045440 | 561792 | 448920 | 469148 | 398776 | 232224 | 93888 | 27220 | 5280 | 512 |
| 2 | 0 | 1209600 | 1260384 | 1086696 | 788576 | 463488 | 236756 | 100416 | 31236 | 6240 | 608 |
| 3 | 0 | 0 | 1797120 | 1707360 | 903660 | 425240 | 209340 | 98360 | 34800 | 7400 | 720 |

A noteworthy structural consequence is that the chance that the tree path is already a geodesic **decreases and then increases** with underlying graph distance:

\[
\Pr(L=d\mid d)=
\begin{cases}
11/30,&d=1,\\
7/30,&d=2,\\
26/75,&d=3.
\end{cases}
\]

The corresponding exact means are

\[
\mathbb E[L\mid d=1]=930701/324000,\quad
\mathbb E[L\mid d=2]=1255111/324000,\quad
\mathbb E[L\mid d=3]=5713/1350.
\]

## Assumptions and scope
All edges have unit conductance. Spanning trees are sampled uniformly among the \(5{,}184{,}000\) distinct edge sets. The underlying walk is the usual discrete-time, uniform-neighbor random walk; its loop-erasure is chronological. Both endpoints are fixed before sampling. Path length counts edges, not vertices.

For an explicit, reproducible graph presentation, label the vertices \(0,1,\ldots,11\). Vertices \(0\) and \(11\) are the poles. The upper ring is \(u_i=1+i\), the lower ring \(v_i=6+i\), for \(i\in\mathbb Z/5\mathbb Z\). The edges are the five pole-to-ring edges at each pole, both five-cycles, and the ten staggered connections \(u_iv_i\) and \(u_iv_{i-1}\). This defines the simple icosahedral graph, with all degrees five.

## Proof
Let \(A=5I-\mathrm{Adj}(G)\) be the integer combinatorial Laplacian. For each self-avoiding \(s\)-to-\(t\) path \(\gamma\), let \(V(\gamma)\) denote its vertex set. The exact number of spanning trees whose unique \(s\)-to-\(t\) path is \(\gamma\) equals

\[
C(\gamma)=\det A_{V\setminus V(\gamma),\,V\setminus V(\gamma)},
\]

with empty determinant interpreted as one. Indeed, requiring all the edges of \(\gamma\) in a spanning tree and contracting those edges produces a bijection with the spanning trees of the contracted multigraph, and no spanning tree can contain a second \(s\)-to-\(t\) route. Loops after contraction do not matter, while parallel edges retain their multiplicities. Taking the matrix-tree cofactor at the contracted path vertex leaves precisely the displayed principal minor. Consequently,

\[
N_{d,k}=\sum_{\substack{\gamma:\ s\to t\text{ self-avoiding}\\|\gamma|=k}}C(\gamma).
\]

This is an identity for exact integers, not an appeal to statistical sampling. An exhaustive depth-first traversal of all finite simple paths and exact fraction-free determinant evaluation gives the table. The separately computed spanning-tree denominator is the determinant of any \(11\)-by-\(11\) Laplacian cofactor, \(5{,}184{,}000\). It can also be checked from the Laplacian eigenvalues \(0\) (once), \(6\) (five times), and \(5\pm\sqrt5\) (three times each):

\[
\tau(G)=\frac1{12}\,6^5(5^2-5)^3=5{,}184{,}000.
\]

For the shortest-path entries, the path multiplicities are respectively \(1,2,10\) and the equal per-path spanning-tree counts are \(1{,}900{,}800\), \(604{,}800\), \(179{,}712\). Their products are the three geodesic numerators, yielding the strict inequalities \(7/30<26/75<11/30\). Row sums are all exactly \(\tau(G)\), and multiplying columns by their lengths gives the stated means. The verifier checks all 66 unordered endpoint pairs directly, without assuming graph distance transitivity.

## Verification
Run `python3 verify_icosahedral_lerw.py` with Python 3 and no third-party libraries. It reconstructs all 30 edges from the two-ring representation, uses an exact integer Bareiss determinant for all principal minors, recursively enumerates all self-avoiding paths between each of the 66 pairs, compares their total weighted counts with the full displayed table, and checks normalization and means. A separate exact rational Gaussian-elimination calculation checks sample path probabilities using products of killed-walk Green-function diagonals. The computation confirms \(4{,}151\), \(4{,}734\), and \(5{,}170\) simple paths for representative pairs at distances one, two, and three, respectively. Every assertion is about a finite explicitly enumerated set.

## Relationship to prior work
The UST–loop-erasure correspondence and the matrix-tree theorem are established prior results, not new claims. Schramm (1999) and Lawler–Schramm–Werner (2001) treat scaling and structural properties of loop-erased walks and uniform spanning trees. Peres–Revelle (2004) prove limit laws for expanding graph families, not this finite polyhedral length table. Kenyon–Wilson (2011) give a much broader connection-probability formalism for surface graphs, whose principles can be used to derive finite connection probabilities but which does not present these three exact icosahedral distributions. Even the single-edge probability \(11/30\) is known from effective resistance; the contribution is the simultaneous full path-length census and its nonmonotone geodesic-probability comparison, not that one-edge identity alone. The general determinant technique is credited and needs graph-specific complete enumeration to yield the table.

## Limitations
The exact law is confined to the twelve-vertex, unit-weight icosahedral graph and two specified endpoints. It does not establish an infinite-size scaling law, a corresponding classification for other polyhedra, or robustness under changed conductances. A previous unindexed enumeration of the identical finite laws cannot be excluded; no claim of independent external validation or definitive historical priority is made.

## References
1. O. Schramm, *Scaling limits of loop-erased random walks and uniform spanning trees*, initial arXiv posting 1999-04-05, https://arxiv.org/abs/math/9904022.
2. G. F. Lawler, O. Schramm and W. Werner, *Conformal invariance of planar loop-erased random walks and uniform spanning trees*, initial arXiv posting 2001-12-20, https://arxiv.org/abs/math/0112234.
3. Y. Peres and D. Revelle, *Scaling limits of the uniform spanning tree and loop-erased random walk on finite graphs*, initial arXiv posting 2004-10-19, https://arxiv.org/abs/math/0410430.
4. R. W. Kenyon and D. B. Wilson, *Spanning trees of graphs on surfaces and the intensity of loop-erased random walk on planar graphs*, initial arXiv posting 2011-07-18, https://arxiv.org/abs/1107.3377.
5. *Two-point resistances in Archimedean resistor networks*, https://doi.org/10.1016/j.rinp.2022.105443, for the preexisting \(11/30\) adjacent-vertex effective resistance.
