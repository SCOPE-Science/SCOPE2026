# Scientific review: rectangular-box vertex Rips filtration

## Correctness
PASS. The face criterion is the exact subset-sum formula for squared distances of binary vertex triples. It leaves only one potentially variable comparison between \(C\) and \(A+B\). The full list of intermediate clique complexes follows from explicit edge-difference sets: disjoint edges, disjoint four-cycles, the cube graph, two tetrahedra, two tetrahedra joined by four edges, the independence complex of two disjoint four-cycles, and the cross-polytope boundary. The integral cellular boundary cycles of the six cube faces generate the degree-one cycle lattice with one primitive relation, giving the stated persistence intervals and excluding field-dependent torsion. The direct verifier checked 364 parameter triples and 2564 stages, independently reducing all simplex boundaries. Finite tests are corroboration, not the universal proof.

## Originality
PASS against inspected evidence, with a residual bibliographic risk. Saleh–Titz Mite–Witzel prove the regular-cube special case but not varying rectangular side lengths or the change of intermediate homotopy type across \(c^2=a^2+b^2\). Shukla's hypercube theorem uses shortest-path/Hamming distance, which is not the Euclidean metric with distinct coordinate weights. Chachólski–Jin–Scolamiero–Tombari develop abstract decompositions but do not state the specific parameter classification. Indexed comparisons with other Euclidean-polytope and cube Rips findings concern different vertex sets or metrics. An equivalent unpublished or unindexed calculation remains possible.

## Value
PASS. A natural three-parameter family of eight-vertex point clouds exhibits a sharp geometric phase boundary and several different homotopy stages. The classification gives the full field-independent barcode, including all zero-dimensional mergers, five degree-one bars with explicit endpoints, and the final degree-three bar. Unlike the regular cube calculation, it resolves all anisotropic aspect ratios, simultaneously handling equal-length degenerations, and provides a compact reproducible test case for persistence calculations.

## Closest literature and limitations
The closest primary source is Saleh–Titz Mite–Witzel, arXiv:2302.14388 (2023), particularly the regular cube theorem and the definitions in the first six pages. Shukla, arXiv:2202.02756 (2022), treats a non-Euclidean graph metric. See RESULT.md for precise domain, proof, code, other references, and limits. This is a self-review, not external independent certification.

Self-review: passed. Independent audit: not yet performed.
