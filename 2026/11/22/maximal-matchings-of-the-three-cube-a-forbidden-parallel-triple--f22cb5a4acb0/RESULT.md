# Maximal-matchings of the three-cube: a forbidden-parallel-triple shattering law and two-degree integral homology

## Finding

Let \(Q_3\) be the graph with vertex set \(\{0,1\}^3\), joining vertices differing in one coordinate. Let \(\mathcal C\) be the Boolean concept class consisting of the edge-incidence vectors of all **inclusion-maximal** matchings of \(Q_3\); a query asks whether a specified graph edge belongs to the matching. Write \(\mathcal S\) for the simplicial complex of edge-query supports shattered by \(\mathcal C\).

**Exact structural theorem.** A support \(S\subseteq E(Q_3)\) is shattered if and only if (i) its edges are pairwise vertex-disjoint, (ii) \(|S|\le3\), and (iii) its three edges, when \(|S|=3\), do not all have the same coordinate direction. The 48 cube symmetries give three orbits of nonempty shattered facets: one orbit of six two-edge facets and two orbits of shattered three-edge facets of sizes 24 and 8. Consequently
\[
\Phi_{\mathcal C}(z)=\sum_{S\in\mathcal S}z^{|S|}=1+12z+42z^2+32z^3,
\qquad \operatorname{VCdim}(\mathcal C)=\operatorname{Ldim}(\mathcal C)=3.
\]
The reduced integral homology groups are torsion-free and satisfy
\[
\widetilde H_1(\mathcal S;\mathbb Z)\cong\mathbb Z^6,\qquad
\widetilde H_2(\mathcal S;\mathbb Z)\cong\mathbb Z^7,
\]
with all remaining reduced integral homology zero. In particular, this shattering complex is nonpure and has nonzero homology in two adjacent degrees.

## Assumptions and scope

All graph edges are unordered, all matchings are sets of pairwise vertex-disjoint edges, and *maximal* means inclusion-maximal, not necessarily maximum-cardinality. The ambient query universe has exactly twelve edges. The statement concerns this labeled three-dimensional binary cube only; it is not asserted for higher-dimensional cubes or for the ordinary matching complex (all partial matchings).

For a finite concept family \(\mathcal C\), a support \(S\) is shattered when its traces \(\{M\cap S:M\in\mathcal C\}\) comprise all \(2^{|S|}\) subsets of \(S\). The Littlestone dimension is the maximum depth of a complete binary tree of membership queries whose root-to-leaf response sequences are realized by concepts.

## Proof

**Finite matching classification.** Encode cube vertices by integers \(0,\ldots,7\) (their three binary bits). Order its edges lexicographically:
\[
(0,1),(0,2),(0,4),(1,3),(1,5),(2,3),(2,6),(3,7),(4,5),(4,6),(5,7),(6,7).
\]
Represent a subset by a twelve-bit integer whose bit \(j\) indicates the \(j\)-th edge in this list. A subset \(M\) is a maximal matching precisely if no two selected edges share a vertex and every edge outside \(M\) meets a selected edge. This criterion checks all \(2^{12}=4096\) possible edge subsets, with no probabilistic or partial enumeration. Exactly 17 satisfy it: nine have four edges (perfect matchings), and eight have three edges (two for each of the four antipodal unmatched-vertex pairs). There is no smaller maximal matching.

**Complete trace table.** The group of vertex maps \(v\mapsto t\oplus\pi(v)\), where \(t\in\{0,1\}^3\) and \(\pi\) permutes the three bit positions, has 48 elements and acts on all edge subsets. For each orbit of *matching* supports, the following table gives the minimum twelve-bit representative, orbit size, and number of distinct traces of the 17 maximal matchings. The bit encoding is fully specified above.

| Support size | Representative | Orbit size | Distinct traces |
|---|---:|---:|---:|
| 0 | 0 | 1 | 1 |
| 1 | 1 | 12 | 2 |
| 2 | 10 | 12 | 4 |
| 2 | 12 | 24 | 4 |
| 2 | 80 | 6 | 4 |
| 3 | 52 | 24 | 8 |
| 3 | 84 | 12 | 7 |
| 3 | 328 | 8 | 8 |
| 4 | 212 | 3 | 10 |
| 4 | 449 | 6 | 12 |

The table is checked by applying all 48 coordinate-isometries to every representative and by exact trace enumeration; the orbit sizes sum to the complete matching-subset counts in every support degree. A shattered support must itself be a matching, since the all-one labeling must be realized. The only failing three-edge matching orbit (representative 84) consists of the 12 ways to choose three of the four parallel edges in one coordinate direction; each has exactly seven traces. Neither four-edge orbit realizes all 16 traces. Heredity of shattering excludes any larger support. The matching-supported classes with two or fewer edges all shatter. This proves the structural theorem and the face polynomial. The six two-edge facets are precisely orbit 80; all 32 shattered triples are facets.

**Adaptive rank.** Every edge belongs to exactly five of the 17 maximal matchings: edge transitivity and the sum of matching sizes \(9\cdot4+8\cdot3=60\) give \(60/12=5\). If a depth-four complete query tree existed, its first positive branch would require at least eight distinct matchings to realize its eight leaves, contradicting five. A shattered three-support provides a fixed-order depth-three complete tree, so the adaptive dimension is three.

**Integral topology.** Order the 42 shattered two-supports and 32 shattered three-supports by their integer masks. Form the integral simplicial boundary matrix \(B\) of size \(42\times32\), whose column for a triple \(\{i<j<k\}\) has signed entries corresponding to deleting these edge indices with signs \(+,-,+\). Exact Gaussian elimination gives \(\operatorname{rank}_{\mathbb Q}B=25\). A direct unimodular certificate is the submatrix on the following zero-based row and column indices:

`rows=[0,1,2,3,4,5,6,7,8,9,11,12,14,15,16,17,18,20,21,22,23,25,26,30,31]`

`columns=[0,1,2,3,4,5,6,7,8,10,11,12,13,14,16,17,18,19,20,22,24,25,26,28,30]`

Its exact integer determinant is \(+1\). Hence the nonzero Smith invariant factors are all one and the image of \(B\) is a primitive sublattice. The one-skeleton is connected, since every pair of disjoint cube edges is a shattered two-support; its vertex-edge boundary has rank eleven. Thus
\[
\operatorname{rank}\widetilde H_1=42-11-25=6,
\qquad \operatorname{rank}\widetilde H_2=32-25=7.
\]
The primitive image gives no torsion in \(\widetilde H_1\), and \(\widetilde H_2\), being a kernel in a free abelian group, is free. There are no higher faces or other nonzero reduced homology groups.

## Verification

The source files `verify.py` and `verify.cpp` implement independent complete edge-subset, trace, and face enumerations using the vertex/edge definitions above. Both check every possible support, including the forbidden-parallel-triple criterion. Python additionally enumerates all 48 automorphisms and verifies every orbit-table row, computes the rational boundary rank using exact fractions, and evaluates the specified 25-by-25 determinant using integer Bareiss elimination. C++ independently checks the boundary rank modulo two. The recorded successful outputs are in `verification_python.txt` and `verification_cpp.txt`. These calculations are finite exhaustive certificates; no infinite extension is claimed or inferred from finite data.

## Relationship to prior work

Drmota, Ramos, Requilé and Rué (2018) study the enumeration and distributions of maximal matchings across graph classes. Their methods and results are about counting matching configurations, not Boolean traces on subsets of the cube's edges or the associated simplicial homology. Benediktsson, Macpherson and Adler (2020; journal 2022) study the neighborhood formula on Johnson and Hamming graphs; this is a different concept relation from edge incidence in maximal matchings of \(Q_3\). Existing results on the *ordinary* matching complex of \(Q_3\) describe all partial matchings, whereas the present simplicial complex is formed by the supports shattered by its inclusion-maximal matchings. Neither complex contains the other as an automatic homological consequence of the definition, and the computed integral homology ranks differ.

## Limitations

The result is a complete finite theorem for \(Q_3\), not a higher-dimensional formula or a classification of all cubic graphs. Only integral homology is asserted; no integral wedge-of-spheres homotopy equivalence is claimed. The finite verification is complete for the specified 4,096 edge subsets, but literature indexing cannot prove absolute historical novelty, and some relevant repository-hosted scientific records could not be read in full. Independent mathematical validation has not been carried out.

## References

1. Michael Drmota, Lander Ramos, Clément Requilé, Juanjo Rué. *Maximal Independent Sets and Maximal Matchings in Series-Parallel and Related Graph Classes*. AofA 2018, 18:1–18:15. DOI: [10.4230/LIPIcs.AofA.2018.18](https://doi.org/10.4230/LIPIcs.AofA.2018.18). First verified public publication: 2018-06-18.
2. Bjarki Geir Benediktsson, Dugald Macpherson, Isolde Adler. *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*. [arXiv:2007.16042](https://arxiv.org/abs/2007.16042), first posted 2020-07-31; *Discrete Applied Mathematics* 312 (2022), 29–44, DOI: 10.1016/j.dam.2021.09.017.
