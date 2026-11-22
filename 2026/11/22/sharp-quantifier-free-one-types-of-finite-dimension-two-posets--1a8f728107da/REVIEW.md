# Scientific review

**Correctness — PASS.** A two-linear-order realizer maps every nonparameter one-type into an \((m+1)\)-by-\((m+1)\) cut grid. For each marked point, the two neighboring cuts \((i-1,p_i)\) and \((i,p_i-1)\) have the same strict predecessor/successor pattern. These \(m\) edges form a forest, so the number of nonparameter patterns is at most \(m^2+m+1\). An explicit reverse-rank antichain gives each all-incomparable or one-sided consecutive-interval pattern, achieving the bound. Adding the \(m\) equality types proves the exact extremum. The actual bundled checker enumerates every parameter permutation through eight and verifies the interval patterns, returning `VERIFY_OK`. The finite enumeration is corroboration, not the proof.

**Originality — PASS within inspected evidence.** The 2026 two-order satisfiability paper uses a richer signature and studies a different logical invariant. The 2026 bounded-model-checking paper provides general type bounds. The nearest public exact type-count result concerns complete types of a monotone two-order Fraïssé limit carrying an extra relation, so neither statement directly implies the pure dimension-two poset atomic type spectrum. Searches for aliases, two-dimensional poset one-point extensions, and complete parameter types did not find the exact bound. Residual risk: a classical permutation-poset or geometric folklore argument might be equivalent.

**Value — PASS.** Sharp all-arity quantifier-free type growth and minimal realizing model size are intrinsic finite-model-theoretic invariants. The collision forest explains the nontrivial loss of \(m\) patterns when forgetting the two order coordinates and retaining their strict product order. The antichain extremizer gives a canonical interval normal form; this is structurally more informative than a low-arity census.

**Scope and limits.** The result does not cover complete first-order types, arity greater than one or order dimension at least three. Priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
