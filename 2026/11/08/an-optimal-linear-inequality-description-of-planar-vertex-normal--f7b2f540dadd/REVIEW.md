# Self-review

**Final claim.** The full-dimensional supporting-point parameter cone for any \(N\ge3\) pairwise distinct prescribed planar unit normals has an optimal nearest-neighbour H-description: precisely \(2N\) facets for positive-spanning directions, or \(2N-2\) if one angular gap is at least \(\pi\). Its only lineality consists of common translations.

## Correctness — PASS

The explicit two-dimensional wedge identity transforms each adjacent directed inequality pair into a nonnegative tangent-cone decomposition of the consecutive point displacement. Along an ordered circular or semicircular chain, projection monotonicity establishes every omitted normal-support comparison. The strict one-target-equality witnesses are obtained from vertices of slightly perturbed circumscribed polygons, using auxiliary directions inside a large gap where necessary. The point tuple consisting of the normals is strictly feasible; all-equalities vectors are common translations. These arguments address all \(N\ge3\), every angular arrangement (including exact semicircles), and all degenerate point tuples.

Numerical confirmation: 378 configurations, 15,514 bounded LP tests; 4,748 independent retained-facet separation witnesses and 10,766 omitted-inequality implications. The proof, not these finite tests, supports the universal claim.

## Originality — PASS, provisional historical priority

Rieger's arXiv:2608.26615v1 defines the exact same cone and, in Section 5, proves particular individual redundancies (Lemmas 22–23), explicitly distinguishing these from simultaneous redundancy. Its statements do not imply an exact simultaneous minimal system or a two-regime facet classification. Pinelis's polygon convexity theorem arXiv:cs/0701045 tests edge-angle order and may supply related geometric intuition, but not the ambient parameter-cone facet census. Padrol–Pilaud–Poullot's *Deformed Graphical Zonotopes* (DOI:10.1007/s00454-023-00586-x) concerns support-height normal-fan deformation cones, not vertex coordinates. Semantic database checks and accessible preceding claims found no directly covering theorem. The main residual risk is an earlier equivalent theorem indexed under convex interpolation or support-point fitting terminology.

## Mathematical value — PASS

The exact cone description replaces \(N(N-1)\) inequalities by \(2N\) or \(2N-2\) in a natural geometric parameterization, with every survivor provably necessary. This is not merely a routine local convexity restatement: it gives a complete global, boundary-inclusive simultaneous reduction, a sharp half-circle phase transition and an exact facet enumeration. The result directly answers the motivating research distinction between *individual* and *simultaneous* redundancy.

## Limitations and verification status

The theorem applies only in dimension two and assumes distinct unit normals. The proof is fully given; computational checks are finite and numerical. Priority is provisional, and no independent mathematical assessment has been performed.

Self-review: passed. Independent audit: not yet performed.
