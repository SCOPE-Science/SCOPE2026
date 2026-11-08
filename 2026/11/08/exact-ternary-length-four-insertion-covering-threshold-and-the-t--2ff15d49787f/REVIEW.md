# Scientific review

## Correctness — PASS

The two exhibited sets contain respectively \(31\) and \(33\) distinct length-four words; direct subsequence incidence checking covers all \(243\) length-five targets and confirms that the larger set omits the length-three target `012`. Every repeated-symbol deletion target has a length-five guard word whose every length-four subsequence still contains the target. This reduces possible non-equivalence to the forbidden distinct-symbol target `012` by alphabet relabeling. The checker exhaustively rejects all insertion covers using at most \(30\) unrestricted centers and at most \(32\) centers avoiding `012`. Its branching is exhaustive, and its only shortcuts are proved necessary bounds or dominance by an already visited coverage state. The exact computation is part of the proof; no numerical optimization tolerances are used.

## Originality — PASS against inspected evidence

Xie–Sun–Ge (arXiv:2606.15379) provide the logical non-equivalence and general bounds; their inspected text does not state the sharp ternary four-to-five covering cost. Pikhurko–Verbitsky–Zhukovskii (arXiv:2409.06425) give general density results and smaller-parameter examples. Lenz–Rashtchian–Siegel–Yaakobi (arXiv:1911.09944) give broad bounds. Relevant existing research records concern opposite deletion-covering directions, packing optima or length-two insertion covering. No located statement implies the simultaneous 31/33 thresholds. Residual risk: earlier unindexed tables or computations may determine this small finite parameter.

## Value — PASS

The 2026 logical distinction between two natural covering channels makes the smallest finite-length *cost* of losing deletion coverage a motivated question. The exact two-codeword overhead at ternary length four gives a concrete, complete, tight boundary for code selection under a dual-coverage objective rather than an arbitrary numerical slice. It also provides a reproducible 243-target benchmark for exact covering methods. No asymptotic or broader minimality claim is asserted.

## Scope and limitations

Finite ternary length-four codebooks only. Neither the first occurrence of non-equivalence across all parameter choices nor independent certification is established. Priority beyond the inspected sources cannot be guaranteed.

Self-review: passed. Independent audit: not yet performed.
