# Scientific review

## Correctness — PASS

The exact linear-algebra claim follows from the reduced-column kernel lemma, a row-by-row Gram–Schmidt basis of nested persistent chain spaces, and additive full-boundary outer products. The reduction is left-to-right and the basis-change matrix upper triangular; deleting later columns and earlier rows therefore preserves the specified kernel basis. With a fixed end time, the admissible spaces are nested in start time, so reusing each orthogonal vector is valid. The cost at row \(t\) is \(O(mk_t^2+(nm+n^2)k_t)\); summing and bounding the prefix counts gives the stated formula. All stated quantifiers include tied filtration levels and zero reduced columns. The supplied checker independently compares against rational null-space projection on genuine simplicial filtrations. Finite testing is not a proof.

## Originality — PASS, with residual priority risk

The motivating Kirchner–Vittorietti paper (arXiv:2611.09610v1, 2026-11-06) explicitly provides the reduction basis and incremental reuse, then conjectures a worst-case dense complexity order in its Section 6. This result does not claim that starting idea; it singles out a fixed-end evaluation order and proves an instance-sensitive amortized cost for that schedule. Mémoli–Wan–Wang (arXiv:2012.02808, Appendix E) supplies an earlier all-pairs Schur-complement algorithm and is not dominated. PETLS (arXiv:2508.11560) is another prior implementation. A logically identical scheduling argument in unindexed material remains a priority risk, and the proof does not establish a bound for every scheduling policy.

## Value — PASS

The contemporaneous paper singles out the global construction cost as an open computational issue. A reproducible order with an exact event-count-sensitive amortized bound makes that target unconditional for a concrete algorithm and is useful for planning dense memory/time budgets in entire filtrations. This is more than one finite numerical instance: it covers all finite face-closed filtrations, every homological degree, tied filtration events, and worst-case input families. It is not a claim of universal algorithmic optimality; different existing Schur methods may outperform it.

## Limitations and sources

See `RESULT.md` for the proof, exact scope, competing established methods, and references, and `VERIFICATION.md` for the exact rational test and limits. No independent scientific review or exhaustive publication-priority determination is asserted.

Self-review: passed. Independent audit: not yet performed.
