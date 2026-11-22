# Scientific review of the final claim

## Correctness — PASS

The central probability coupling is exact because the total attachment weight in an affine degree model is deterministic while every leaf carries the same weight. The independent categorical law has nonnegative mass at its null outcome and matches the entire leaf-set Markov transition, not merely one-time marginals. Disjoint occupancy-coordinate blocks and the negative-association closure theorem establish dependence inequalities for distinct leaf vertices observed at different deterministic sizes. The joint probability formula follows by exclusion of independent categorical outcomes; inclusion-exclusion reconstructs the full Boolean law. The two-sided concentration bound follows from negative association and bounded-variable exponential moments. For any strictly positive degree kernel, explicit four-vertex formulas prove nonpositive pair covariances; exhaustive five-vertex conditioning gives the exact rational covariance and algebraic threshold. All assumptions, finite horizons and limiting qualifications are explicit. The packaged exact checker passed 1,272 assertions and is not substituted for the analytical proof.

## Originality — PASS against inspected literature

The closest general result is Dubhashi–Ranjan's 1996 negative-association theorem for independent ball allocations; that general dependence theorem is **not claimed as new**. Its application here needs the new exact law-level reduction of a degree-dependent attachment process to independent categorical trials. Hartle–Krapivsky's 2026 study treats empirical degree/leafdegree distributions, and Bryc–Minda–Sethuraman treat total leaf-count deviations; neither establishes the complete individual leaf-survival law. The 2020 young-age tree result establishes pairwise leaf repulsion for independently selected parents with deterministic probabilities, rather than the state-dependent degree-weighted mechanism. The sharp five-vertex sign reversal for a positive nonlinear kernel adds a distinct motivated boundary that neither general occupancy theory nor cited preferential-attachment fluctuation work supplies. Relevant searches and record comparisons found no covering statement. Priority risks remain: an unlocated older representation of affine leaf survival or an explicit equivalent nonlinear threshold could reduce originality.

## Mathematical value — PASS

The principal object is the **entire labeled leaf-survival process**, a more informative invariant than the aggregate leaf count. Its complete finite-dimensional law at arbitrary vertex-specific observation times gives exact joint probabilities and simultaneous concentration guarantees for any selected subpopulation. The sharp five-vertex nonlinear sign change shows that negative dependence depends on attachment structure and identifies the earliest possible failure; this is not merely a routine numerical counterexample. The result supplies a natural structural boundary rather than an arbitrary special-case parameter computation.

## Scope and limitations

The association statement requires nonnegative affine slope and positive leaf weight; it chooses one observation size per vertex. The five-vertex threshold is specific to the one-parameter family with equal first two degree weights, while first-size minimality is universal for positive degree kernels. The Hoeffding estimate may not be optimal, and infinite-tree conclusions require the displayed proof rather than finite tests. The historical-priority search is not exhaustive and independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
