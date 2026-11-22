# Scientific assessment

## Correctness — PASS

The proof starts from the exact positive/negative sign-equivariant Euclidean projection, derives the KKT clipping caps and their strict-cell Jacobians, calculates the full absolute row sums \(1+(r-2)/(k_iH)\), and optimizes over all realizable active-group and clipping patterns. Piecewise-affine continuity turns the local maximum into a global bound. The constructed strict clipping pattern achieves every optimizing row sum by finite perturbed inputs, avoiding any unsupported passage from derivatives to finite sharpness. A standalone numerical and exact-fraction checker confirms 340 finite face enumerations, 120 sharp-pair comparisons, and 120 general two-input inequalities. The proof, not the finite tests, covers all group sizes and real inputs.

## Originality — PASS, with a documented historical-priority risk

Quattoni et al. (2009) give the clipping and KKT reduction for the identical mixed-norm ball; Chau et al. (2018), Chu et al. (2020), and Perez et al. (2023) develop projection algorithms. Their inspected derivations characterize how to compute one projection, but do not derive the exact global coordinate-maximum-norm Lipschitz coefficient, its sorted-block-size extremal law, or finite-pair attainability. Béjar et al. (2019) address a dual proximity operator; Perez and Barlaud (2024) explicitly study a different, non-Euclidean multilevel projection. Ordinary \(\ell_1\) projection formulas cover only the singleton-block subcase. Multiple targeted mathematical-record and literature searches found no direct or stronger coverage. Older or differently named group-projection sensitivity results could still establish priority; search absence does not imply historical uniqueness.

## Mathematical value — PASS

Group-supremum constraints occur in joint-sparsity and multi-task regularization, where Euclidean nonexpansivity gives no input-coordinate error budget. The theorem gives the **sharp** coordinatewise amplification from only group cardinalities, a complete at-most-two-groups phase boundary, attainable worst-case perturbations and a practical \(O(m\log m)\) sizing rule. The nonexpansivity dichotomy and the large-block limit demonstrate the mathematically meaningful gap between Euclidean and coordinatewise robustness; this is not merely an algorithmic restatement of clipping.

## Limits

The analysis excludes radius zero, nonuniform coordinate weights, overlapping groups and other ambient norms. The independent validation channel is unperformed. Historical priority beyond inspected sources is not certified.

Self-review: passed. Independent audit: not yet performed.
