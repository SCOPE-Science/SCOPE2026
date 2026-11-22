# Review of the characteristic-three rational Pascal-line fiber theorem

## Correctness — PASS

The theorem is proved for all \(q=3^m\) with \(m\ge2\), not inferred from a sample. Projective normalization uses sharp triple transitivity of \(\operatorname{PGL}_2\) on the conic. Direct cross products give the normalized Pascal line; the quadratic discriminant separates tangent, secant, and exterior types. The rational substitution in the final vertex has exactly four excluded values, and their zero/character-sum contributions are explicitly derived, including the exceptional case \(b=-1\). The resulting three orbit counts are converted into exact per-line counts using the group action and the dihedral factor twelve.

The standalone checker uses quotient-field arithmetic to verify the normalized classification in three extension fields, and an independent direct side-intersection enumeration checks every one of the 12,600 hexagons on \(\mathbb F_9\). The finite calculations are corroboration rather than proof for arbitrary \(m\). Critical assumptions, zero discriminants, and divisibility factors are specified in `RESULT.md`.

## Originality — PASS (qualified)

The exact claim is the full rational Pascal-line **fiber multiplicity** in characteristic three, for each rational tangent, secant, and exterior line. Chipalkatti–Da Silva (arXiv:2202.12975) study the Pascal map and its degeneration loci; Chipalkatti (arXiv:2303.10319) solves the different problem of simultaneous prescribed Pascal lines. Halbeisen–Hungerbühler (2024) classify twins of conic hexagons; Fernandes (1993) analyzes finite ovals via Pascal properties. None of the inspected relevant parts supplies this finite-characteristic-three three-type distribution.

Previously calculated characteristic-two and characteristic-at-least-five rational-fiber distributions do not cover characteristic three. The latter formulas cannot be continued by substituting a formal value for the quadratic character of \(-3\); the special square identities in characteristic three change the zero and character sums. The projective dual Brianchon formulation is equivalent to the claim but no stronger known formula was found in the searches. The closest searched indexed Pascal–Kirkman incidence spectrum concerns a fixed sextuple and characteristic at least seven, rather than fibers over all rational sextuples. The strongest residual priority risk is an unindexed older computation of the same characteristic-three fiber counts or an equivalent Brianchon enumeration. A negative search result is not a proof of global priority.

## Mathematical value — PASS

This is the remaining odd-small-characteristic case in a natural complete finite-field conic incidence question. Characteristic three is structurally exceptional: several discriminants of forbidden collisions become exact squares, so ordinary odd-characteristic formulas do not specialize. The complete exact fiber count is nontrivial, describes every rational line rather than average or aggregate counts, and shows that the Pascal map on cyclic rational hexagons is surjective over **every** characteristic-three field in which such a hexagon exists. The sharp first-field threshold \(q=9\) and the complete tangent/secant/exterior multiplicities are useful natural invariants for computational finite geometry and dual Brianchon incidence.

## Limits and priority risk

The theorem does not address the scheme structure of the Pascal morphism, geometric sextuples not rational pointwise, or degenerations. Older unindexed finite-geometry sources could contain an equivalent count. No independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
