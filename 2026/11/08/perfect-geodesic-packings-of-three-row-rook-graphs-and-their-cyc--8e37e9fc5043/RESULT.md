# Perfect geodesic packings of three-row rook graphs and their cycle-index polynomial

## Finding

For every integer \(n\ge 3\), let \(R_n=K_3\mathbin{\square}K_n\), with vertices \((r,i)\) for \(r\in\{1,2,3\}\) and \(i\in[n]\). A **geodesic packing** is an unordered family of pairwise vertex-disjoint maximal shortest paths. Let \(g_n\) be the maximum number of paths in such a family. Then
\[
 g_n=n.
\]
Every packing of \(n\) paths partitions all \(3n\) vertices into shortest three-vertex paths. Such packings have a canonical permutation \(\pi\) on the columns, with no fixed points, and a canonical proper three-coloring \(f:[n]\to\{1,2,3\}\) of its directed cycles: \(f(i)\ne f(\pi(i))\) for all \(i\). This correspondence is a bijection.

Let \(A_{n,j}\) count maximum packings whose column permutation has exactly \(j\) cycles and put \(A_n(y)=\sum_j A_{n,j}y^j\). Then the complete cycle-index family has exponential generating function
\[
 \boxed{\sum_{n\ge0} A_n(y)\frac{t^n}{n!}
 =\frac{1}{(1-2t)^y(1+t)^{2y}}.}
\]
For the formal boundary values in this generating series, \(A_0(y)=1\) and \(A_1(y)=0\); the graph assertion concerns \(n\ge3\).

In particular, the exact number of maximum geodesic packings is
\[
 \boxed{A_n(1)=\frac{n!}{9}\left(4\cdot 2^n+(3n+5)(-1)^n\right).}
\]
The number whose column permutation is one cycle is
\[
 \boxed{A_{n,1}=(n-1)!\left(2^n+2(-1)^n\right).}
\]
For example, the cycle-count distributions for \(n=3,4,5,6,7\), written as \((A_{n,1},A_{n,2},\ldots)\), are \((12)\), \((108,108)\), \((720,720)\), \((7920,11160,3240)\), and \((90720,136080,45360)\).

## Assumptions and scope

All graphs are finite, undirected, and simple. The Cartesian product joins two distinct cells when they have the same row or the same column. A shortest path of length two is *maximal* in the subpath-inclusion sense used for geodesic packing. Paths are unoriented and packings are unordered, so no factorial from ordering the constituent paths is included. The statistic \(j\) counts cycles of the uniquely determined column permutation, not connected components of the graph formed by the chosen vertices.

## Proof

**1. The geodesics.** A pair of cells in the same row or column has distance one. A pair with different rows and different columns has distance two, by changing one coordinate at a time. Thus \(\operatorname{diam}(R_n)=2\). Every edge is contained in a length-two geodesic: if it is horizontal, extend one endpoint vertically to a different row and column relative to the other endpoint, and analogously for a vertical edge. Consequently the maximal geodesics are exactly the two-edge shortest paths. Each consists of three corners of a two-row, two-column rectangle, with one **pivot column** containing two cells and one **wing column** containing the third. The geodesic center is the pivot cell in the same row as the wing.

**2. The sharp packing size.** Every path consumes three vertices, so a packing has at most \(n\) paths. Suppose \(\mathcal P\) has exactly \(n\) paths. It covers the entire vertex set. In any column at most one chosen path can be pivoted, because the column has only three vertices and a pivot consumes two. There are \(n\) paths and \(n\) columns, so every column is the pivot of exactly one path. It has precisely one remaining cell, which is a wing of exactly one path. Writing \(\pi(i)\) for the wing column of the unique path pivoted at column \(i\), we obtain a permutation of \([n]\). A wing column differs from its pivot, hence \(\pi(i)\ne i\).

For each column \(i\), let \(f(i)\in\{1,2,3\}\) be the row of its unique wing cell. The path pivoted at \(i\) has its own wing at \((f(\pi(i)),\pi(i))\), so its center is \((f(\pi(i)),i)\). The row \(f(i)\) at column \(i\) is occupied by another path's wing; therefore \(f(i)\ne f(\pi(i))\).

Conversely, take a fixed-point-free permutation \(\pi\) and a function \(f:[n]\to\{1,2,3\}\) with \(f(i)\ne f(\pi(i))\) for every \(i\). For each \(i\), form the path consisting of the two cells of column \(i\) in rows different from \(f(i)\), followed through the cell in row \(f(\pi(i))\) to the wing \((f(\pi(i)),\pi(i))\). More explicitly, its center is \((f(\pi(i)),i)\), its second pivot cell is the unique row outside \(\{f(i),f(\pi(i))\}\), and its wing is \((f(\pi(i)),\pi(i))\). These are valid two-edge geodesics. Their pivot cells partition all non-wing cells; because \(\pi\) is a permutation, their wings are precisely the remaining \(n\) cells, each once. The construction therefore yields \(n\) disjoint paths. It is inverse to the extraction above. Such a pair exists for every \(n\ge2\): choose an \(n\)-cycle and a proper three-coloring of it. Thus the upper bound \(g_n\le n\) is achieved.

**3. The weighted permutation count.** On a directed cycle of length \(\ell\ge2\), the number of row functions satisfying unequal colors along each arrow is the chromatic polynomial of a cycle at three colors:
\[
 c_\ell=(3-1)^\ell+(3-1)(-1)^\ell=2^\ell+2(-1)^\ell.
\]
For \(\ell=2\), this means the two distinct vertices must have different colors, giving \(c_2=6\). A length-one cycle is forbidden and has \(c_1=0\). Different permutation cycles can be colored independently. The exponential formula for labelled permutations, with a factor \(y\) per cycle, gives
\[
 \sum_{n\ge0} A_n(y)\frac{t^n}{n!}
 =\exp\left(y\sum_{\ell\ge1}\frac{c_\ell t^\ell}{\ell}\right)
 =\exp\left(-y\log(1-2t)-2y\log(1+t)\right).
\]
This is the asserted bivariate generating series. For \(y=1\), the partial-fraction identity
\[
 \frac1{(1-2t)(1+t)^2}
 =\frac{4/9}{1-2t}+\frac{2/9}{1+t}+\frac{1/3}{(1+t)^2}
\]
yields the scalar formula by extracting coefficients. To get the one-cycle count, choose an \(n\)-cycle in \((n-1)!\) ways and color it in \(c_n\) ways, giving \(A_{n,1}=(n-1)!c_n\). All statements follow.

## Verification

The standalone `verify.py` independently builds all \(R_n\), computes shortest-path distances by breadth-first search, forms the three-vertex maximal geodesic sets from those distances, and counts exact vertex-disjoint covers using a branching exact-cover search. It also independently enumerates all permutations and counts their cycle colorings. Tests for \(2\le n\le7\) agree in total and at every cycle count; this includes \(n=2\) as an extra boundary test, not a novelty claim. Run `python3 verify.py`. The computed totals are \(6,12,216,1440,22320,272160\) for those six orders. The finite computation corroborates, but does not replace, the proof for all \(n\).

## Relationship to prior work

Manuel, Brešar, and Klavžar introduced geodesic packing in 2022. Their Proposition 2.6 analyzes **geodesic transversals** of square rook graphs and their Lemma 2.3 gives a general packing upper bound. The present proof makes that upper bound sharp for three-row rook graphs and identifies the exact structure and multiplicities of all maximum packings; the cited paper does not state this classification.

The coefficient array \((A_{n,j})\) and its sum are **not new integer sequences**: they coincide with the triangle and row sums of OEIS A137946 (2008), where they are given through a matrix/Sheffer-series construction associated with \(K_3\). The contribution claimed here is specifically the bijection between the graph-geodesic packing configurations and properly colored permutation cycles, giving a graph-invariant interpretation of those known coefficients. This numerical overlap is a substantive priority limitation, not evidence that the integers were newly discovered.

## Limitations

The theorem classifies only maximum-cardinality geodesic packings of the three-row rook graphs, not all inclusion-maximal or all smaller packings, and does not address arbitrary numbers of rows. No independently performed mathematical audit or exhaustive review of every possibly related enumerative interpretation is claimed. Other descriptions of the OEIS triangle may yield the same graph interpretation, and this remains the main originality risk. The exact generating-function identity alone is already present in an equivalent form in the sequence database; the new statement is its graph-metric bijection.

## References

- P. Manuel, B. Brešar, S. Klavžar, *Geodesic packing in graphs*, arXiv:2210.15325, first submitted 27 October 2022; https://arxiv.org/abs/2210.15325. Consulted complete open preprint, especially Section 2 and Proposition 2.6.
- OEIS Foundation, *A137946: Triangle of coefficients associated with the expansion of the \(K_3\) graph matrix characteristic polynomial as a Sheffer sequence*, entry by R. L. Bagula, 30 April 2008; https://oeis.org/A137946. Consulted complete displayed triangle and row sums.
- V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, Results in Mathematics **79** (2024), 110, https://doi.org/10.1007/s00025-024-02133-3. Consulted article, especially Section 3 on Cartesian products; its focus is vertex general position rather than disjoint geodesic-path packings.
