# Scientific review: binary two-plane Plücker shattering

## Correctness — PASS

The object is the binary two-plane Plücker incidence concept family, not all alternating matrices. For every rank-two row matrix, its minor is one exactly when the corresponding two column symbols are distinct nonzero elements of \(\mathbb F_2^2\). This proves a bijection with nondegenerate complete-tripartite-plus-isolates edge graphs, and fixes the hypothesis count. The \(K_{2,n-2}\) witness independently realizes all four edge-bit choices at each free vertex. For \(n=4,5,6\), complete enumeration of all \(2^{\binom n2}\) query supports proves the upper bounds, every polynomial coefficient, and every facet type. Independent integer and packed-word Gaussian eliminations over \(\mathbb F_2\) prove the reduced homology ranks. Two implementations using distinct concept-generation constructions agreed exactly. No infinite generalization is inferred.

## Originality — PASS within inspected evidence

The classical Plücker embedding and Gaussian-binomial concept count are excluded from novelty. Beelen--Singh's full accessible arXiv article establishes the same ambient point model, but Theorem 4.4 concerns parity-check families, not all binary coordinate projections of single points. Piñero--Singh's accessible author manuscript studies weights of linear codewords, not shattering under arbitrary selected Plücker-coordinate queries. Fitzpatrick--Iosevich--McDonald--Wyman's finite-field VC work concerns spheres. Indexed related reports on restricted quasisymmetric Grassmannians and neighborhoods in Grassmann graphs neither state nor imply these coefficientwise classifications or mod-two homology computations. The exact graph-type facet lists, especially the six-label theta/double-star/disjoint-triangle strata, were not found in the compared literature. Historical priority is not independently certified; earlier unindexed tables are a material residual risk.

## Mathematical value — PASS

Grassmann points, their coordinate projections and puncturing are canonical geometric objects. A full finite type-realization classification exposes phenomena absent from both raw Grassmannian cardinality and the common scalar VC dimension: in the first three nontrivial orders, top facets all have bipartite form \(K_{2,n-2}\), yet numerous strictly smaller inclusion-maximal query supports produce nonpure complexes, and mod-two homology occupies distinct degrees. The six-label theta facet and the two adjacent nonzero homology ranks provide a specific structural transition. This exact motivated benchmark can guide conjectures about higher-rank Plücker projections without asserting such conjectures as proved. It is not an arbitrary graph slice or routine consequence of a known weight spectrum.

## Closest references and limits

- P. Beelen and P. Singh, arXiv:2001.06278, full accessible article (Introduction, Plücker preliminaries, Theorem 4.4, decoding context): canonical model and code decoding, no complete shattering classification.
- F. Piñero and P. Singh, DOI:10.1007/s10623-018-0567-1, accessible author manuscript (Abstract, Introduction, Theorem 3.8): affine Grassmann codeword weight spectrum with different quantifiers.
- D. Fitzpatrick et al., arXiv:2108.13231, accessible abstract, definitions and main theorem: VC dimension of finite-field spheres, not Plücker coordinates.
- J. Castillo and J. Samper, arXiv:1809.00281, accessible abstract/introduction: topology of matroid complexes, not this nonpure projection-shattering complex.

Exact finite computations are limited to \(n=4,5,6\). Mod-two homology does not determine integral homology or homotopy. Prior literature and inaccessible historical records might still overlap. No external mathematical certification has occurred.

Self-review: passed. Independent audit: not yet performed.
