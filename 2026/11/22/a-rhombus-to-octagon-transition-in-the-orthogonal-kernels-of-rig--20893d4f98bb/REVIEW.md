# Scientific review

## Correctness — PASS

The theorem uses the original all-nonempty-face orthogonal projection definition. Projection to each pair of lateral triangles gives one of the two independent strict inequalities; their intersection implies the edge, base, interior and vertex conditions. The finite-plane cuts give the entire kernel, not merely a sufficient subset. At any fixed height the section is a homothetic copy of the basal polygon, so an exact two-halfplane calculation gives the volume. The change from a dominating halfplane to two active constraints occurs precisely at \(h^2=|a^2-b^2|\). The positive-part term is quadratic at a nonsquare transition, making the fraction exactly \(C^1\) there. The fixed-area reduction has a strictly negative derivative in both regimes, with no missing endpoint case. Reproducibility: `python3 VERIFY.py`, 3,840 direct-face-foot trials and twelve exact rational shoelace area checks. Experiments support but do not prove the universal statement.

## Originality — PASS (best-knowledge comparison)

Pavlík (arXiv:2611.14277, Sections 4–6) proves an all-polytope projection kernel criterion for three-dimensional orthogonal tilings, not a formula for the metric kernel of a rectangular pyramid or its volume. The companion (arXiv:2611.13896, Sections 5–6) gives general polyhedral cutout constructions, also not this exact fraction or basal face transition. Related publicly indexed calculations concern the normal-foot locus of the regular octahedron; all-face kernels of axis-stretched cross-polytopes, higher cross-polytopes and parallelotopes; and shadow/section probabilities of right rectangular pyramids. They do not dominate the new kernel statement or its optimization. A search failure does not prove novelty, and an older or unindexed equivalent remains possible. There is no claim of formal independent certification.

## Value — PASS

The orthogonal kernel is exactly the geometric admissibility region for a natural polytope decomposition into orthogonally bipolar cells. Determining its full volume and topology in a three-parameter class is a motivated geometric invariant, not a restatement of the kernel definition. The four- to eight-vertex transition is a genuine active-face change with a second-derivative jump, and the square uniquely solves a shape-optimization problem at fixed area and height. These facts distinguish permissibility, combinatorial type and quantitative robustness of orthogonal cutout tilings.

## Source scope and limitations

The proofs cited above justify a complete three-parameter result only for a centered right rectangular pyramid. Neither the square extremum nor the phase diagram extends here to oblique pyramids. Earlier indexed results were compared by implication, not merely title; the priority assessment is provisional pending broader expert review.

Self-review: passed. Independent audit: not yet performed.
