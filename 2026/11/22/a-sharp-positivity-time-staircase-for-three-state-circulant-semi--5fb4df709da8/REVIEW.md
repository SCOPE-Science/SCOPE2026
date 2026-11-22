# Scientific review: positivity-time staircase

## Correctness — PASS

The matrix identity \(J^2=-(I-P)\) yields the exponential explicitly. The minimum of the nine entries becomes a scalar comparison against a piecewise-cosine envelope, and strict concavity of its logarithm on each angular cell gives the exact count, with equality tangencies explicitly excluded. Differentiation of the global maximum establishes the unique parameter thresholds and their asymptotic count. The two-dimensional obstruction follows from Cayley–Hamilton and the sign of the off-diagonal exponential coefficient. The independent Taylor/squaring tester passed 1,276 assertions across selected finite parameters; the written proof covers all positive real parameters and all nonnegative times.

## Originality — PASS (qualified)

A three-dimensional normal rotation–decay example is explicitly known from Glück (2022), Example 5, so it is not claimed as novel. General spectral eventual-positivity characterizations are known from Noutsos–Tsatsomeros (2008), Daners–Glück–Kennedy (2015/2018) and later work. The contribution evaluated is narrower and distinct: **the exact component topology** of the entrywise positive-time set for the two-parameter circulant family, its explicit count and critical staircase, arbitrarily large component counts in dimension three, and a proof of the minimal dimension. The inspected closely related primary material and semantic research comparisons do not state or imply this numerical/topological classification without further computation. Historical coverage by uninspected works remains possible; a failed database query alone is not novelty evidence.

## Mathematical value — PASS

Eventual positivity theory tells when positivity finally holds but typically does not quantify repeated transient sign changes. This theorem classifies every transient failure interval and its creation threshold for a natural finite-dimensional normal semigroup, while proving that this complexity is already possible at the minimal dimension. The exact damping-to-frequency count is a meaningful structural invariant of the positivity-time set, not an arbitrary parameter sample or a routine norm estimate.

## Limitations

The known base example and general spectral criteria are expressly excluded from the novelty claim. Priority is not independently certified and may be affected by older detailed matrix-exponential calculations. Tests sample finite data only; analytic derivations establish the unbounded-count statement.

Self-review: passed. Independent audit: not yet performed.
