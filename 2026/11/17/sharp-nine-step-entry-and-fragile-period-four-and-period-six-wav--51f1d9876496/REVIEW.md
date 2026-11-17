# Mathematical review

**Correctness — PASS.** Clipping every colour population to \(0,1,2\) preserves each neighbour-threshold test and commutes with a synchronous update, so the nine-trit quotient is exact. Tracking the original occupied buckets additionally preserves labelled colours. An exhaustive 19,683-state certificate checks \(F^{21}=F^9\); its cycle-permutation calculation and all 343 saturation size classes establish the sharp period diagram. A separately written vertex-level program reproduces the period and entry-time conclusions for 171,315 states on seven graph sizes. The sharp nine-step witness is explicit. The essential finite classification depends on the supplied executable certificate.

**Originality — PASS, qualified.** The 1993 lattice study [1] considers different graph families and phase questions; the directly relevant finite-graph studies [2,3] describe general period/transient bounds but were not accessible in full. Targeted published-record searches for exact tripartite threshold-two least-period phase diagrams found no theorem implying the fragile four-, six-, or twelve-cycle criteria. Known singleton-shore and two-shore analyses do not imply the all-positive three-shore classification. A binary parity automaton on multipartite graphs is not the same update rule. Historical-priority uncertainty concerning [2,3] remains material.

**Value — PASS.** The exact phase diagram contains genuinely thin and isolated period regimes: the period-four locus vanishes if either of its two size-two shores grows; period six occurs only at a single size triple; period twelve disappears when the smallest shore reaches four. The uniform sharp transient bound across unbounded graph sizes and the distinction between labelled and population periods make this a structural classification, not an arbitrary small census.

**Limits.** No complete attraction-basin sizes, no other threshold rules, no independent mathematical validation. The finite exhaustive part can be audited by running the included code; the unavailable 1995/1997 papers remain potential coverage risks.

Self-review: passed. Independent audit: not yet performed.
