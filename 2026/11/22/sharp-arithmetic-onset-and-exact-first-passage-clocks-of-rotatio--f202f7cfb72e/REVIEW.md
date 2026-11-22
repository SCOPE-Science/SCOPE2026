# Review of cyclic Boolean erosion symmetry clocks

## Correctness
**PASS.** Iterated one-sided AND erosion deletes the terminal site of each maximal one-run each update, preserving run starts until their lengths fall to zero. The exact run-start profile after \(t\) steps is the coordinatewise truncation \((h_i-t)_+\). Equality with a translate is equivalent to the maximum-discrepancy threshold. A vanished original run between surviving periodic runs forces a gap of at least five between successive surviving starts, establishing necessity; the explicit unique-singleton defect construction establishes sufficiency. Exhaustive finite checks support the proof without pretending to prove all \(n\).

## Originality
**PASS within inspected evidence.** The recent symmetry-enumeration article proves symmetry preservation and enumerates pre-existing symmetric configurations, not time-resolved symmetry birth in a fixed nonlinear rule. Classical binary morphological erosion establishes the run-shortening mechanism but does not itself state the first-passage stabilizer clock or sharp ring-length threshold. Relevant mathematical-research records about additive first-symmetry laws and different erosion automata concern distinct maps and do not imply this theorem. Residual historical priority risk remains because the literature cannot be exhaustively indexed.

## Mathematical value
**PASS.** The result gives all first-entry times into spatial stabilizer strata for every initial configuration of a natural nonlinear cellular automaton, plus a sharp composite-versus-prime/small-ring obstruction for nontrivial pre-extinction symmetry creation. This is a complete structural classification, not a single numerical observation or a restatement of symmetry monotonicity.

## Limits
The theorem concerns one erosion rule and does not enumerate all state counts at each first-entry time. Independent audit is not performed.

Self-review: passed. Independent audit: not yet performed.
