# Geodesic-packing polynomials of complete multipartite graphs and reentrant purity for doubleton parts

## Finding

For any integer \(r\ge2\) and labelled complete multipartite graph \(G=K_{n_1,\ldots,n_r}\) with \(n_i\ge2\), the full generating polynomial of vertex-disjoint maximal geodesic families and the generating polynomial of inclusion-maximal such families are given by explicit finite directed-array sums. In the equal-doubleton family \(G_r=K_{2,\ldots,2}\) (\(r\) parts), these sums simplify to closed factorial polynomials. The complex whose vertices are maximal geodesics and whose faces are pairwise vertex-disjoint families is pure precisely for \(r\in\{2,3,4,5,7\}\). In particular, purity fails at \(r=6\), returns at \(r=7\), and fails for every \(r\ge8\).

Let \(\mathcal P_{G}(z)\) enumerate *all* geodesic packings by number of constituent maximal geodesics, including the empty packing. Let \(\mathcal M_G(z)\) enumerate packings maximal **by inclusion**. For every ordered pair \(i\ne j\), take a nonnegative integer \(q_{ij}\). Define
\[
 o_i=\sum_{j\ne i}q_{ij},\qquad c_i=\sum_{j\ne i}q_{ji},\qquad u_i=n_i-2o_i-c_i,\qquad k=\sum_{i\ne j}q_{ij}.
\]
Sum only arrays with \(u_i\ge0\) for all \(i\), and define their exact integer multiplicities by
\[
 A(\mathbf q)=\frac{\prod_{i=1}^r n_i!}{2^k\bigl(\prod_{i=1}^r u_i!\bigr)\bigl(\prod_{i\ne j}q_{ij}!\bigr)}.
\]
Then
\[
 \boxed{\mathcal P_G(z)=\sum_{\mathbf q}A(\mathbf q)z^k,\quad
 \mathcal M_G(z)=\sum_{\mathbf q:\,\neg\exists i\ne j\;(u_i\ge2\,\wedge\,u_j\ge1)} A(\mathbf q)z^k.}
\]

For \(G_r=K_{\underbrace{2,\ldots,2}_{r\ \mathrm{parts}}}\), set \((x)_{\underline{k}}=x(x-1)\cdots(x-k+1)\), with \((x)_{\underline0}=1\), and write \([P]\) for 1 when proposition \(P\) holds and 0 otherwise. Then
\[
 \boxed{\mathcal P_{G_r}(z)=\sum_{k=0}^{\lfloor2r/3\rfloor}\binom rk(2r-2k)_{\underline{k}}z^k,}
\]
\[
 \boxed{\mathcal M_{G_r}(z)=\sum_{k=\lceil r/2\rceil}^{\lfloor2r/3\rfloor}
 \binom rk\binom{r-k}{2k-r}2^{2r-3k}k!z^k
 +[r\equiv1\pmod3]\binom r{2(r-1)/3}\frac{r+2}{3}\left(\frac{2(r-1)}3\right)!z^{2(r-1)/3}.}
\]
The second term applies only when \(r\ge4\), automatically true for \(r\ge2\) with \(r\equiv1\pmod3\). The complete set of cardinalities of maximal packings is the integer interval
\[
 \boxed{\left\lceil\frac r2\right\rceil\le k\le\left\lfloor\frac{2r}3\right\rfloor.}
\]
The number of maximum packings when \(3\mid r\) is \(\binom r{r/3}(2r/3)!\). Illustratively, \(\mathcal M_{G_6}(z)=960z^3+360z^4\), whereas \(\mathcal M_{G_7}(z)=12600z^4\).

## Assumptions and scope

Graphs are finite, simple, undirected, with labelled vertices. Every part has at least two vertices and there are at least two parts. A geodesic is a shortest path, maximal when not a proper subpath of any other geodesic. A geodesic packing is a family of *vertex-disjoint* maximal geodesics; its size is the number of paths, not the total number of graph vertices used. Inclusion-maximality concerns adding another disjoint maximal geodesic. An individual length-two geodesic is determined by its three vertices, since its two endpoints are nonadjacent. We do not count ordered orientations of a path as different.

## Proof

**Step 1: maximal geodesics.** In \(G\), vertices in different parts have distance 1, while distinct vertices in the same part have distance 2. Every geodesic has at most two edges. A two-edge geodesic therefore has its two endpoints in one part \(i\), and its internal vertex (center) in another part \(j\). It is automatically maximal because the diameter is two. Every one-edge geodesic between parts \(i\) and \(j\) extends to a two-edge geodesic, by choosing a second endpoint in part \(i\), which is possible because \(n_i\ge2\). Thus the maximal geodesics are exactly the indicated two-edge paths.

**Step 2: directed-array counting.** For each \(i\ne j\), let \(q_{ij}\) count paths whose two endpoints are in part \(i\) and whose center lies in part \(j\). These paths consume \(2o_i+c_i\) distinct vertices from part \(i\). Fixing the whole directed array, allocate within part \(i\) the endpoint labels for every \(j\), the center labels received from every \(j\), and the \(u_i\) unused vertices. The multinomial coefficient is
\[
 \frac{n_i!}{u_i!\prod_{j\ne i}(2q_{ij})!\prod_{j\ne i}q_{ji}!}.
\]
Pair the \(2q_{ij}\) endpoint labels into \(q_{ij}\) unordered pairs in \((2q_{ij})!/(2^{q_{ij}}q_{ij}!)\) ways. Assign the \(q_{ij}\) center vertices to these pairs in \(q_{ij}!\) ways. Multiplying over parts and ordered types gives exactly \(A(\mathbf q)\). Conversely every packing yields exactly one directed array with exactly one such choice of allocations and pairings. This proves \(\mathcal P_G\).

**Step 3: maximality.** A new maximal geodesic is disjoint from the packing if and only if the unused vertices include two from some part \(i\) and one from a different part \(j\). Equivalently, \(u_i\ge2\) and \(u_j\ge1\) for some \(i\ne j\). Negating this condition gives the stated exact filter for \(\mathcal M_G\). No maximality of an individual graph path is being confused with maximality of a packing.

**Step 4: the doubleton polynomial.** For \(G_r\), a part supplying endpoints for a path exhausts both its vertices and cannot also supply a center or another endpoint pair. If there are \(k\) packed paths, their \(k\) endpoint-pair parts are distinct. Choose these parts in \(\binom rk\) ways. Every center must be chosen among the other \(r-k\) parts, comprising \(2(r-k)\) labelled vertices, and the \(k\) distinct endpoint-pair parts can be assigned \(k\) distinct centers in \((2(r-k))_{\underline{k}}\) ways. Therefore \(3k\le2r\) and the displayed formula for \(\mathcal P_{G_r}\) follows.

**Step 5: maximal doubleton packings.** Suppose \(k\) endpoint-pair parts have been used. Each of the remaining \(r-k\) parts contains 0, 1, or 2 unused vertices. The filter in Step 3 says that maximality holds if either (I) every remaining part has at most one unused vertex, or (II) exactly one remaining part has two unused vertices and all other parts have none. In case (I), every one of the \(r-k\) center-eligible parts must supply at least one center, while altogether they supply \(k\) centers. Thus \(r-k\le k\le2(r-k)\). Exactly \(d=2k-r\) parts must supply both vertices, and the other \(2r-3k\) parts must supply one. For fixed \(k\), choose the endpoint-pair parts, choose the \(d\) double-center parts, choose one of two center vertices in each single-center part, and biject the \(k\) distinct endpoint-pair parts with the selected center vertices. This gives
\[
 \binom rk\binom{r-k}{2k-r}2^{2r-3k}k!.
\]
In case (II), exactly two vertices remain unused, so \(3k=2r-2\). Thus \(r\equiv1\pmod3\) and \(k=2(r-1)/3\). Choose the \(k\) endpoint-pair parts and then the one completely unused part among the remaining \(r-k=(r+2)/3\) parts. Every vertex in the other center-eligible parts is used, and there are \(k!\) bijections from endpoint-pair parts to centers. These two cases are disjoint, yielding the second displayed polynomial.

**Step 6: cardinality spectrum and purity.** All \(k\) with \(\lceil r/2\rceil\le k\le\lfloor2r/3\rfloor\) admit case-(I) configurations: select \(d=2k-r\) double-center parts and one center from each remaining center-eligible part. Case (II) introduces no additional sizes: for \(r=3t+1\ge4\), its size \(2t\) lies in the same interval. This proves the exact maximal-size interval. The packing complex has these maximal families as facets; it is pure iff the interval contains one integer. For \(r=2,3,4,5,6,7\) its endpoint pairs are respectively \((1,1),(2,2),(2,2),(3,3),(3,4),(4,4)\); for \(r\ge8\), division into residue classes modulo six gives \(\lfloor2r/3\rfloor>\lceil r/2\rceil\). Hence purity holds exactly for \(r=2,3,4,5,7\). For \(3\mid r\), the maximum size \(2r/3\) uses all vertices, so choose its \(2r/3\) paired parts and biject their paths to both vertices in each of the remaining \(r/3\) center-only parts, proving the stated multiplicity.

## Verification

The included `verify.py` independently constructs maximal geodesics as unordered three-vertex shortest paths, enumerates every vertex-disjoint path family, and tests whether any further path can be added. This direct enumeration is compared with the directed-array polynomial on 18 nonuniform/multi-part profiles and with the closed doubleton polynomials for \(2\le r\le7\). It enumerates 38,436 path families in total across these profiles. Additional exact symbolic doubleton checks cover \(2\le r\le30\). The command is `python3 verify.py`. The unrestricted statement is established by the preceding combinatorial proof, not by these finite tests.

## Relationship to prior work

Manuel, Brešar and Klavžar introduced geodesic packing and its complexity and dual transversal connection in their 2022 preprint (arXiv:2210.15325), proving among other things the scalar packing number for balanced bicliques. Their full accessible preprint does not give the directed-array cardinality distribution or the doubleton multipartite maximal-packing spectrum. Those scalar results are not claimed as new. The 2011 Orlovich–Dolgui–Finke–Gordon–Werner theory of dissociation in line graphs and related enumerations supplies an adjacent description of two-edge path packings in bipartite graphs; counting such path packings when \(r=2\) is consequently not treated as the sole novelty. The new assessed focus is the all-configurations, inclusion-maximal classification across arbitrary complete multipartite graphs and the exact exceptional purity set for doubleton parts. These results concern path packings, not vertex \(k\)-limited packings, geodesic transversals, edge-geodesic partitions or geodetic vertex sets.

## Limitations

The multivariate directed-array formula is a finite sum, not a closed expression for every coefficient using only elementary functions of the part sizes. The closed doubleton formulas apply only when every part has exactly two vertices. No general closed formula for the maximum packing number over arbitrary part-size vectors is asserted here. Finite validation covers only the stated finite cases, and no independent mathematical audit or exhaustive literature-priority certification has been performed. An unindexed equivalent result about packing \(P_3\) paths may exist.

## References

1. P. Manuel, B. Brešar, S. Klavžar, *Geodesic packing in graphs*, arXiv:2210.15325 (first public 2022-10-27); journal version, *Applied Mathematics and Computation* 459 (2023), 128277. https://arxiv.org/abs/2210.15325
2. Y. Orlovich, A. Dolgui, G. Finke, V. Gordon, F. Werner, *The complexity of dissociation set problems in graphs*, *Discrete Applied Mathematics* 159 (2011), 1352–1366. https://doi.org/10.1016/j.dam.2011.04.023
3. M. G. Anand, T. Jeba Raj, *The geodesic-transversal problem on complementary prisms*, *Ceylon Journal of Science* 55 (2026), 1643–1660, DOI 10.4038/cjs.v55i4.9666. Its complete-multipartite transversal scalar concerns a different invariant and is not claimed here.
