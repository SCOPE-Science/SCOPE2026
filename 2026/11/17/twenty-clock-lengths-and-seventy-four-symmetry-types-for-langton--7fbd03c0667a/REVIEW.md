# Review of the \(3\times4\) ant orbit classification

## Correctness

**PASS.** An explicit local inverse establishes that every one of the \(196608\) states is immediately periodic. `verify_direct.py` checks the inverse and generator commutation on every state and obtains cycle/symmetry classes by exhaustive orbit tracing and union-find. Independently, `verify_independent.cpp` checks the state successor indegrees, counts cycles and applies Burnside's lemma to the 48-element geometric group. Both reproduce all 20 rows, the period-weighted total, and 74 symmetry types. Output logs are included, but executable proofs are the source of the finite certification.

## Originality

**PASS, qualified.** The closest accessible torus treatment is the 2019 discussion that lists the all-white \(3\times4\) axis-dependent periods 72 and 56, reversibility, group symmetries and parity bounds. It does **not** give the full 20-period distribution or the 74-class symmetry quotient. The 2011 generalized-ant paper concerns recurrence hardness on infinite lattices; the 2020 twisted-torus paper concerns algorithmic hardness on a different geometry. OEIS A386970 lists one return time per \(n\times3\) size. Related prior finite calculations for \(2\times n\) and the \(3\times3\) square do not imply the first unequal-sided \(3\times4\) census. No checked stronger classification covers the precise claim, although unindexed computations remain possible. These comparisons are statements about the mathematical scopes, not proof of global uniqueness.

## Mathematical value

**PASS.** The first nonsquare, genuinely two-dimensional finite torus is a canonical test case for the ant's geometric symmetries. Its exact return spectrum and full symmetry quotient answer a natural classification question that single-background period tables cannot answer. The coexistence of 18 inequivalent symmetry types at period 72 and exactly two maximal-period types demonstrates that time period is not a complete geometric invariant. The precise 74-class answer is itself the meaningful finite classification, without a claim of a general theorem for all sizes.

## Residual limitations

This is an exact finite-state statement and no larger-torus generalization is proved. Relevant accessible primary texts were inspected for their definitions, main theorems, and scope, not automatically treated as absent merely because a search snippet failed to mention the counts. Historical priority remains conditional on this finite literature survey; independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
