# Self-review

## Correctness
**PASS.** The source's inequalities place the branch breakpoint strictly inside the invariant core, make the left exterior orbit strictly increase and the right exterior orbit strictly decrease, and prevent either exterior branch from skipping the core. Exact affine iterates determine the two disjoint survivor intervals and their length. Solving their endpoint threshold conditions proves the full tail, maximum first-entry time, and boundary logarithmic scale. The endpoint \(\varepsilon=0\) is analyzed directly, with the excluded state \(x=1\) handled explicitly. `capture_checker.py` passed 431 supplementary exact rational/grid checks. A finite grid was not used to infer an infinite-domain theorem.

## Originality
**PASS within inspected evidence.** Gaivão–Laurent–Nogueira's source preprint arXiv:2212.10944v1, Sections 2–5, and its accessible journal version prove only pointwise finite entrance (Lemma 4.1), not the complete first-entry distribution, sharp global cutoff, or critical boundary scaling. Laurent–Nogueira arXiv:1907.08655v1 addresses dynamics on a reduced interval, not first entrance from its exterior. Related research records for Sel'kov, quantized contractions and two-zone flows concern different systems and do not imply this exact five-parameter first-entrance law. No universally conclusive novelty guarantee is claimed; unindexed prior calculations remain possible.

## Mathematical value
**PASS.** The invariant core is the published paper's natural reduction from five parameters to the three-parameter dynamics. The result quantifies exactly how long the reduction can take, for all starting points and all strict admissible parameters, and gives a complete statistical invariant rather than numerical trajectories. A natural admissibility-boundary degeneration separates exploding worst-case latency from bounded mean latency, a distinction not resolved by the previously known pointwise capture statement. The algebra is elementary but the classification is complete and mathematically motivated.

## Sources and limitations
Original primary sources: arXiv:2212.10944v1; doi:10.1007/s00010-024-01064-2; arXiv:1907.08655v1. The claim does not provide return-time statistics inside the core and its critical endpoint is only for the displayed family. Relevant unindexed analyses and equivalent unpublished calculations are residual originality risks.

Self-review: passed. Independent audit: not yet performed.
