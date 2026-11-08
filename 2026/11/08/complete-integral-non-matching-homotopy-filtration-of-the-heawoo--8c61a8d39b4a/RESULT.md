# Complete integral non-matching homotopy filtration of the Heawood graph

## Finding

Let \(H\) be the Heawood graph, the point–line incidence graph of the Fano plane. Let \(\operatorname{NM}_k(H)\) consist of subsets of the 21 graph edges whose largest pairwise disjoint subcollection has size strictly less than \(k\). For every integer \(2\leq k\leq7\),

\[
\operatorname{NM}_k(H)\simeq\bigvee^{b_k} S^{2k-3},\qquad
(b_2,b_3,b_4,b_5,b_6,b_7)=(8,36,92,113,36,1).
\]

In expanded form:

| Matching threshold | Complete integral homotopy type |
|:--|:--|
| \(k=2\) | \(\bigvee^8S^1\) |
| \(k=3\) | \(\bigvee^{36}S^3\) |
| \(k=4\) | \(\bigvee^{92}S^5\) |
| \(k=5\) | \(\bigvee^{113}S^7\) |
| \(k=6\) | \(\bigvee^{36}S^9\) |
| \(k=7\) | \(S^{11}\) |

At \(k=1\), the complex has no nonempty faces. At \(k\ge8\), it is the full simplex and therefore contractible. Each nontrivial stage has free integral homology only in degree \(2k-3\), with rank \(b_k\). In particular, the sparse Heawood graph attains the general bipartite homological vanishing bound in every nontrivial threshold.

## Assumptions and scope

Represent the Fano plane by point labels \(p\in\mathbb Z/7\mathbb Z\) and line labels \(\ell\in\mathbb Z/7\mathbb Z\). Its incidence flags are \((p,p+d)\) for \(d\in\{0,1,3\}\), with arithmetic modulo seven. The difference set \(\{0,1,3\}\) gives exactly one common line for each pair of distinct points. The 21 flags are the vertices of the non-matching simplicial complexes (not vertices of the Heawood graph). A face is a nonempty selected flag set with maximum matching size less than the threshold. Orient each simplex by increasing flag index, indexed with point first and difference second. All statements concern geometric realizations and integral homotopy and homology; no equivariant identification is claimed.

## Proof

**Exact face determination.** For every bitmask \(s\) on the 21 flags define \(\nu(s)\) as the largest cardinality of a subset of flags with pairwise distinct point and line endpoints. For any least-index selected flag \(e\),

\[
\nu(s)=\max\bigl(\nu(s\setminus\{e\}),\;1+\nu(s\setminus N[e])\bigr),
\]

where \(N[e]\) denotes all flags incident to either endpoint of \(e\), including \(e\). The empty mask has value zero. This recurrence follows by partitioning matchings into those that exclude or include \(e\). It gives the full face set for each \(k\). An independent computation enumerates every matching and takes a subset maximum by a Boolean-lattice transform; the two methods agree for all \(2^{21}=2,097,152\) masks. There are respectively 77, 2,331, 33,971, 254,240, 963,641 and 1,844,248 nonempty faces at thresholds two through seven.

**An explicit acyclic matching.** At each threshold, start with all nonempty faces unmatched. Sweep the 21 flags in descending index order. For the current flag \(i\), pair each still-unmatched face \(s\) not containing \(i\) with \(s\cup\{i\}\), provided the latter is also still unmatched. Remove paired faces permanently and continue. The attached verifier constructs every pair and every covering relation of the nonempty face poset. It reverses each paired Hasse edge and uses complete topological sorting to certify the absence of directed cycles. The covering-relation totals at thresholds two through seven are respectively 126, 8,715, 189,231, 1,862,259, 8,593,830 and 18,646,131, and all are visited by the acyclicity checks. The residual critical-cell counts by dimension are

| \(k\) | Critical zero-cells | Other critical cells |
|:--|--:|:--|
| 2 | 1 | 8 in dimension 1 |
| 3 | 1 | 36 in dimension 3 |
| 4 | 1 | 92 in dimension 5 |
| 5 | 1 | 114 in dimension 7; 1 in dimension 8 |
| 6 | 1 | 41 in dimension 9; 5 in dimension 10 |
| 7 | 1 | 1 in dimension 11 |

Forman's discrete Morse theorem immediately gives the claimed sphere wedges for thresholds two, three, four and seven.

**Integral attaching maps for the two remaining thresholds.** The signed Morse boundary is computed exactly by elimination along gradient pairs. For an oriented matched pair \((\sigma,\tau)\) with \(\dim\tau=\dim\sigma+1\), write \(\partial\tau=\varepsilon_{\tau,\sigma}\sigma+\sum_{\rho\ne\sigma}\varepsilon_{\tau,\rho}\rho\), with all incidence signs equal to \(\pm1\). Replacing the coefficient of \(\sigma\) by the exact integer combination \(-\varepsilon_{\tau,\sigma}\sum_{\rho\ne\sigma}\varepsilon_{\tau,\rho}\rho\) and recursively eliminating gradient pairs gives the Morse boundary in the basis of critical cells. This recursion terminates because the directed Hasse graph was checked acyclic.

For \(k=5\), the boundary from the single critical 8-cell to the 114 critical 7-cells has coefficient \(-1\) at critical target column 11 (zero-based ascending-mask order). Hence its image is primitive, and the attaching map is equivalent to the inclusion of one sphere summand, leaving \(113\) seven-spheres.

For \(k=6\), the Morse boundary from five critical 10-cells to 41 critical 9-cells has a 5-by-5 submatrix in target columns 1, 7, 13, 19 and 24 equal to

\[
\begin{pmatrix}
-1&0&0&0&0\\
0&-1&0&0&0\\
0&0&-1&-1&0\\
0&0&0&1&0\\
0&0&0&0&1
\end{pmatrix},
\]

whose determinant is \(-1\). Thus all five attaching maps form a primitive direct summand in the free integral degree-nine group, leaving \(41-5=36\) nine-spheres. Since the lower CW skeletons are wedges of spheres of dimensions at least seven and nine, respectively, the Hurewicz isomorphism identifies attaching-map homotopy classes with their integral degrees. Unimodular changes of sphere bases, followed by cancellation of the corresponding cell pairs, establish the stated homotopy types, not just homology groups.

For an independent integral cross-check, the increasing-index matching gives a unit boundary entry at target column zero when \(k=5\), and, when \(k=6\), a 6-by-6 Morse boundary minor in columns 2, 7, 13, 38, 32 and 23 has determinant \(+1\). These different CW models give the same wedge dimensions.

Finally, a matching in a bipartite graph with seven point and seven line vertices has size at most seven. Therefore every edge subset belongs to \(\operatorname{NM}_k(H)\) when \(k\ge8\), giving a simplex.

## Verification

The attached standalone `verify_nonmatching_heawood.cpp` requires a GCC- or Clang-compatible C++17 compiler with built-in bit-count intrinsics. Execute:

```sh
c++ -O3 -std=c++17 verify_nonmatching_heawood.cpp -o verify_nm
./verify_nm
```

The attached `nonmatching_verification.txt` records a complete successful execution. The program independently enumerates all matching masks, verifies Fano incidence, compares maximum-matching values on every edge subset, constructs two distinct acyclic matchings per threshold, topologically sorts every oriented incidence, and computes both decisive signed integer Morse boundaries in two distinct pivot orders and corresponding determinant-one certificates. The last line is `ALL_CHECKS_PASS`.

## Relationship to prior work

Linusson–Shareshian–Welker (first public arXiv version 15 October 2004) determine exact non-matching homotopy types for the complete graph and complete bipartite graph. Neither formula applies directly to the sparse 21-edge Heawood graph. Holmsen–Lee's later general result proves that the reduced homology of a bipartite graph's non-matching complex vanishes in dimensions at least \(2k-2\). This finding gives explicit homotopy types of a sparse, noncomplete, distance-transitive incidence graph, with nonzero groups in dimension \(2k-3\) for every nontrivial threshold. Previously reported Heawood matching, perfect-matching and two-matching complexes impose different face conditions (collections of disjoint edges or bounded vertex degrees), so their conclusions are not interchangeable with the condition \(\nu(s)<k\).

## Limitations

The computation is exact for this graph and all positive matching thresholds, but does not assert corresponding formulas for other projective planes or for arbitrary bipartite graphs. It does not classify equivariant homotopy types or construct canonical sphere generators. Published-priority comparisons cannot exclude unindexed equivalent calculations. The verification is reproducible finite computation and a mathematical discrete-Morse argument, not independent external certification.

## References

1. S. Linusson, J. Shareshian and V. Welker, *Complexes of graphs with bounded matching size*, arXiv:math/0410345v1 (15 October 2004), https://arxiv.org/abs/math/0410345. See Theorems 1.1, 1.4 and 2.4.
2. A. F. Holmsen and S. Lee, *Leray numbers of complexes of graphs with bounded matching number*, arXiv:2003.11270 (first posted 25 March 2020), https://arxiv.org/abs/2003.11270. See Theorem 1.1.
3. J. Baez, *Heawood Graph*, AMS Visual Insight (1 August 2015), https://blogs.ams.org/visualinsight/2015/08/01/heawood-graph/.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145; discrete-Morse theorem quoted in reference 1, Theorem 2.4.
