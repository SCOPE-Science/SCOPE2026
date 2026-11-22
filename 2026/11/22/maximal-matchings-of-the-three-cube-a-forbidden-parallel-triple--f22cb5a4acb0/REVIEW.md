# Scientific review: maximal-matchings of the three-cube

## Correctness — PASS

The claimed domain is exactly the 12-edge graph \(Q_3\), and maximal means inclusion-maximal. The proof exhausts all \(2^{12}=4096\) candidate edge sets by an explicit matching/maximality predicate, finding 17 concepts of sizes three and four. An independently implemented C++17 checker obtains the same 17 concepts and all face coefficients. The 48-element cube automorphism group has exactly the matching-support orbits listed in RESULT.md, including one forbidden orbit of twelve parallel triples and the two nonshattered perfect-matching orbits. A 25-by-25 signed boundary minor has exact determinant \(+1\), with boundary rank 25; this proves the primitive image required for torsion-freeness. The positive branch from any first query contains only five concepts, proving the Littlestone upper bound three, and a shattered three-support yields the matching lower bound. Code and saved outputs were replayed from the stated source files. The claim is finite, not an extrapolation to infinite cases.

## Originality — PASS within investigated evidence

The 2018 conference paper by Drmota, Ramos, Requilé and Rué addresses maximal-matching counts and size distributions in graph classes, not the edge-membership trace complex of the eight-vertex cube. Benediktsson, Macpherson and Adler (arXiv:2007.16042, 2020) treat the neighborhood relation in Johnson and Hamming graphs rather than edge queries on maximal matchings. Existing ordinary matching-complex and higher matching-complex results concern different families of simplices; none of the inspected statements implies this support-wise classification or its integral homology. Search comparisons covered alternate terminology involving maximal independent sets in the cuboctahedral line graph, and the exact polynomial and Betti ranks. Some repository-hosted related results were visible only as publication abstracts; no priority claim is made against uninspected full text or unindexed tables.

## Value — PASS

This gives a natural complete edge-query shattering classification for a canonical symmetric three-dimensional graph: the only extra obstruction after matching and support-size feasibility is a geometrically meaningful parallel triple. The result identifies all 38 facets in three symmetry orbits, proves agreement of static and online dimensions, and computes both nonzero integral homology groups with a unimodularity witness. The two-degree homology of the resulting nonpure complex is not the homology of the usual cube matching complex. These coherent structural and topological properties make the precise finite invariant useful beyond merely recounting known graph matchings.

## Closest literature and limitations

Drmota–Ramos–Requilé–Rué (AofA 2018), DOI 10.4230/LIPIcs.AofA.2018.18, first published 2018-06-18; Benediktsson–Macpherson–Adler, arXiv:2007.16042, first posted 2020-07-31. Related scientific records on the ordinary cube matching complex and cuboctahedral independence complexes cover different object/parameter pairs. The finite exhaustive computation has no missing cases, but the novelty comparison is necessarily evidence-limited; no result for larger cubes and no homotopy decomposition are asserted.

Self-review: passed. Independent audit: not yet performed.
