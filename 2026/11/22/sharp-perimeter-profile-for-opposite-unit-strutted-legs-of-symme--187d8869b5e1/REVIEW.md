# Self-review

## Correctness — PASS
The unique interior-side intersection of unit circles at the leg endpoints is computed exactly. Its polygon containment reduces to two independent half-plane inequalities; the resulting squared comparison has an explicit exact polynomial factorization, with nonnegative and strictly positive factors on the full domain. The equality coordinates have positive shorter base and exact squared diagonal lengths \(1\). Triangle inclusion handles \(a\ge1\). All quantifiers and boundary cases are stated, and the independently coded geometry checks and exact symbolic coefficient arithmetic pass. The Python checks are supplementary to the universal analytic proof.

## Originality — PASS (best-knowledge, with priority risk)
The full-text original 2022 source establishes a perimeter-three theorem only for **adjacent** strut sides; a nonadjacent-leg hypothesis cannot be substituted into it. The 2025 Ptolemy note verifies a special-pentagon result with adjacent struts, not the opposite-leg family. The 2023 quadrilateral result minimizes perimeter with fixed global boundary self-Chebyshev radius; that hypothesis is not supplied by local opposite-leg struts. Related public studies of symmetric trapezoids optimize dilation, centroidal perimeter depth, or convexification rather than the sharp constrained perimeter. Searches for an opposite-leg or isosceles-trapezoid strut profile did not surface an implication or a containing table. Accessible prior findings were checked for the mathematical statement as well as variants. Residual risk: older unindexed extremal quadrilateral calculations or an inaccessible more general theorem may cover this special case; absence from searches alone is not evidence of uniqueness.

## Mathematical value — PASS
This is a sharp boundary counterexample to extending a published theorem from adjacent to opposite sides: not just a diagram, it gives the complete fixed-leg feasibility conditions, sharp parameterized bound, unique equality family, and sharp global constant under exactly the original length normalization. The geometry is natural, because opposite-leg struts are the first missing incidence pattern for a quadrilateral after the consecutive-side case. No global claim about arbitrary quadrilaterals is inferred.

## Limits and scientific integrity
Boundary strut witnesses are included in the quantified definition. The exact global constant is proved for isosceles trapezoids, not all polygons. The fixed-leg equality family is restricted to \(0<a<1\); \(a\ge1\) is handled by a different lower bound. The algebraic checker is a reproducibility aid, not a substitute for proof, and prior-art novelty is not an independently certified priority assessment.

Self-review: passed. Independent audit: not yet performed.
