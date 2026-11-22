# Self-review

## Correctness — PASS

The exact substitution \\(x=-(v+dy)/h\\) produces two quadratics, convex on the nonnegative half-line and concave on the nonpositive half-line. Their vertex conditions \\(v<K\\) and \\(v>-K\\) are necessary and sufficient for active folds. Exhaustive root counts on each strict interval and endpoint give the stated one-, two- and three-predecessor census, including the switching line. The origin's three predecessors are directly evaluated; differentiability at the origin follows because \\(x|y|=o(\\sqrt{x^2+y^2})\\), and the other two have positive Jacobian determinant. The signed multiplicity follows from the identity between the determinant and the scalar derivative. The checker independently reconstructs actual roots and map outputs for rational boundary cases and randomized targets; it is corroborative rather than a substitute for the proof.

## Originality — PASS within inspected evidence

The original 2021 article studies forward-time attractors, fixed points, amplitude rescaling and control, rather than a complete global one-step predecessor classification. A previously reported theorem for the same map gives forward-orbit escape and asymptotic clocks, which does not imply the inverse-sheet geometry. Indexed inverse-sheet results for a coupled cubic map, a four-partition absolute-value map and a quadratic sine-circle map have nonconjugate defining equations, different inverse degrees and different fold structures. Targeted searches and a detailed equation comparison found no stronger source covering these specific inequalities or the meeting of the crease line and the two fold curves. Equivalent unindexed work remains possible.

## Mathematical value — PASS

The map was introduced to describe amplitude control and coexisting chaotic attractors, making the one-step ambiguity of state reconstruction a natural structural question. The theorem gives the exact global valence, the two sign-sensitive opening thresholds, the complete boundary multiplicities, a robust three-to-one observation region through the switching image and a signed inverse degree. In particular, the source's negative-coupling regime has three regular predecessors of the origin for every positive \\(a,k,h\\). The quadratic fold–crease separation is sharp, not a sample-dependent numerical threshold. The result does not imply any property of encryption security, forward attractors or general parameter-sign regimes.

Self-review: passed. Independent audit: not yet performed.
