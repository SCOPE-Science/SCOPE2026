# Scientific review: two-row Toom attraction basins

## Correctness — PASS

The three-input majority identity gives a two-case exact column update, and every initial agreeing column is invariant. Distances to the next initially agreeing column determine first-entry time; the input-to-output characterization forces seeds at exactly the target's cyclic interfaces. This proves the complete basin formula for every \(n\ge3\). The exact Ising transfer matrix has eigenvalues \(4,2\), and its insertion trace gives the finite-ring two-point formula. The Perron eigenvalue is simple, so the local Markov limit follows rigorously. Direct simulation and independent exact matrix checking agree across their stated finite ranges.

## Originality — PASS, with historical qualification

Relevant published prior work establishes the deterministic NEC majority rule, general Toom erosion, stochastic stationary-state Ising comparisons and anchored-interface dynamics. None of the inspected accessible full texts supplies the pointwise two-row absorption-basin weights or the associated initial-data-induced zero-field Ising limit. A published three-row Toom fixed-point count does not imply these basin statements. Explicit equivalence, broader-coverage, exact-table and implication comparisons are recorded in AUDIT.json. The 1997 ground-state article had no accessible full text, and additional unindexed precedent remains a risk; this is not a claim of exhaustive historical uniqueness.

## Mathematical value — PASS

The observed finite-size equilibrium-looking law is not postulated but produced by a deterministic out-of-equilibrium dynamical rule from unbiased initial data. The complete basin census identifies the mechanism, includes both rare periodic exceptions and the two exceptional constant-state masses, and yields exact correlations and a nontrivial thermodynamic limit. This connects natural questions about basin weighting and stationary-state selection to an explicit Ising interaction, rather than merely counting fixed states.

## Limitations

Only exactly two rows and deterministic zero-noise north-east-center majority are covered. The conditional fixed-point law is distinct from a stationary distribution of stochastic Toom dynamics. Historical priority is not independently established, and external mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
