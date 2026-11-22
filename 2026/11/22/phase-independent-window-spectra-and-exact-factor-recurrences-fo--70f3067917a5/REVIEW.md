# Scientific review

**Correctness: PASS.** The morphism \(a\mapsto0^{p-1}(a+1)\) has a common prefix of length \(p^k-1\) in its \(k\)-fold iterate, and each source letter survives in the final coordinate. Prime-adic local periodicity plus coprime CRT recurrence makes every source factor occur in every source residue class modulo the \(p\)-free part. The phase-slice injection is therefore a bijection, with no missed edge phases. The exact factor recurrence is proved by an exhaustive partition of source-block offsets, with the all-zero overlap handled separately for lengths below \(2p\). Independent complete-template and CRT-phase checkers replayed on 525 full-factor and 13,542 phase inputs.

**Originality: PASS against accessible comparisons.** Cassaigne–Kaboré (2026) give the length-valuation window-complexity formula for Thue–Morse but not the prime-base valuation sequences nor the all-phase bijections and radix factor recurrence. Bognini–Ammar (2025) address base-two generalized period-doubling kernel/gap factorizations, not these window spectra. Indexed base-two factor counts and phase-related boundary invariants do not imply the prime-base all-phase theorem. Searches for alternative terminology, substitution/Toeplitz aliases, stronger coverage, and exact tables did not identify the complete claim. Residual risk: earlier unindexed equivalent theorems or a broader result in an unexamined source.

**Value: PASS.** The result provides an all-length, all-phase exact invariant and effective linear-recursive computation for a canonical family of aperiodic prime-base automatic words, showing sharp oscillation between the alphabet-size floor on prime-power lengths and unbounded counts along coprime lengths. The prime arithmetic, all-offset bijection and explicit factor recurrence are structurally motivated by the new window-complexity framework, rather than an isolated small census.

**Limitations.** Prime bases only; no composite-base universality. Finite checks do not replace proof and originality is limited by search coverage. Prior work's base-two formulas remain credited.

Self-review: passed. Independent audit: not yet performed.
