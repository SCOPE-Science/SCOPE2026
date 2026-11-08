# Self-review

## Correctness — PASS

The convex antiprism has 12 facets, 20 edges and six antipodal outward-normal axes. The exact face-normal sign criterion correctly counts the boundary edges of a generic orthogonal projection, independently corroborated by 10,000 direct projected-vertex convex-hull reconstructions. Pairwise intersection rays of six great circles cover all chamber corners when no triple intersection exists; the standard-library exact checker establishes this nonconcurrence, exhaustively tests 64 masks and 30 directed rays over \(\mathbb Z[\varphi]\), and verifies the explicit 32-region mask and angle-pattern table. Physical dihedral dot products determine the stated spherical angles, and Girard's formula integrates the areas into a complete probability distribution. Positivity and total area \(4\pi\) were checked. The simulation is not used as an infinite proof.

## Originality — PASS (historical-priority risk retained)

Glisse and Lazard's 2007 full text proves average-size upper bounds in broad classes of polyhedra, not an exact fixed pentagonal-antiprism law. Glisse–Lazard–Michel–Pouget (2016) analyze Poisson-point random polytopes and largest silhouettes, not the all-view fixed-solid distribution. The published central icosahedron section classification concerns a different object and section statistic, so its two-point law does not imply the present three-point antiprism projection law. A known universal regular-antiprism formula specializes to the same **mean**, but a single mean plus normalization does not determine three independent nonzero atom probabilities; the specific 32-chamber type/incidence enumeration is the new statement. Full-text access to Kettner and Welzl (1997) was unavailable despite searching open versions and an institutional-access attempt. Thus priority remains provisional. No claim is made that an unsuccessful search proves novelty.

## Value — PASS

The uniform pentagonal antiprism is a canonical convex uniform polyhedron, and random orthogonal silhouettes are a meaningful geometry-and-vision observable. Its complete exact discrete shadow law includes a rare decagon event (about \(2.04336\%\)) invisible to mean-only formulas, and the proof gives the entire spherical viewing-direction stratification, not a single arbitrary numeric constant. The chamber proof also provides a reusable method for combinatorial silhouette laws of other solids. This is a finite but structurally complete natural classification rather than an arbitrary data slice.

## Limits and closest sources

The result applies only to uniform orientation and the specific equilateral lateral-face height. Exceptional viewing directions are excluded as a zero-measure set. References: Glisse–Lazard (2007), Glisse et al. (2016), and the partially accessible Kettner–Welzl (1997). The previously published general antiprism **expected** silhouette count and an exact regular-icosahedron central-section law were checked for implication but do not state these three shadow probabilities. Full historical uniqueness remains unverified.

Self-review: passed. Independent audit: not yet performed.
