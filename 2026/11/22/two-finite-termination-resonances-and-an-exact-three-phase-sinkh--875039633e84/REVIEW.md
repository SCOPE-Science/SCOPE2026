# Scientific review of the hub–clique Sinkhorn theorem

## Correctness — PASS

The exact eigenvalue decomposition, scalar scaling equation, derivative calculation, and two crossover equalities together prove the three-regime formula and its globally unique optimum. The row–column normalization residual factorization yields exactly two finite-completion parameters. The remaining claim that no later finite completion is possible uses the published general theorem of Cohen and Nathanson, which was inspected at its full-text statement and proof. The bundled finite checker passes 5605 assertions, including exact rational equalities and numerical derivative agreement. Its finite testing is not mistaken for a proof of universal quantifiers. The weakest assumption is exact arithmetic for finite termination; numerical floating-point implementations are not asserted to finish exactly.

## Originality — PASS, subject to residual literature risk

Knight's general singular-value convergence factor and Cohen–Nathanson's universal at-most-two-scalings result are prior work, not new results. The full texts of those papers were inspected, as were related explicit-scalings studies by Nathanson and accelerated-balancing work by Knight and Ruiz. The inspected articles do not give the family-specific three-mode parameter switch, globally optimal hub affinity, or simultaneous exact resonance-and-rate comparison. The nearest indexed contemporary mathematical results concern binary scaling, unbalanced multi-block variants, or diagonal condition-number optimization on different matrices and cannot imply the family-specific result without an additional analysis. Search incompleteness and related unindexed work remain risks; this is a self-review, not publication-priority certification.

## Value — PASS

There is a practical and structural optimization question: how to select one relative affinity for fastest local worst-case balancing of an exchangeable hub–clique kernel without restricting perturbations to the symmetry subspace. The answer identifies three successive spectral mechanisms and a unique optimal parameter, and it separates worst-case asymptotic rate from exact completion for the original initialization. The precisely quantified near-optimality of the two-step resonance gives a genuine performance trade-off, not just a restatement of a known convergence-rate formula. The narrow kernel family and exact-arithmetic dependency are transparent limits.

Self-review: passed. Independent audit: not yet performed.
