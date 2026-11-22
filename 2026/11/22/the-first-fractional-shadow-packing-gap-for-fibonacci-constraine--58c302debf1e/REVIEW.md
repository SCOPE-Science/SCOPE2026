# Mathematical review

**Correctness — PASS.** The claim concerns a fully defined directed Z-channel on the binary no-adjacent-ones constrained source. The supplied independent finite certificates establish both lower and upper bounds: six short-length matching integer-primal/dual pairs, rational seventh-length primal and dual of value \(9\), and an eight-clique covering plus an eight-word compatible code. An exact exhaustive recursion over the 34-vertex conflict graph counts precisely ten maximum codebooks. `verify.py` checks every certificate from the supplied file. This is a finite proof covering every admissible word in the stated length range, not extrapolation from samples.

**Originality — PASS, qualified.** Polyanskii–Zhang (arXiv:2105.01427, 2021-05-04) addresses unrestricted Z-channel codes, particularly rate/list-decoding bounds. Rameshwar–Kashyap (arXiv:2301.05098, 2023-01-12) does treat \((d,\infty)\) run-length-limited codes, but under symmetric error/erasure or Hamming-distance based bounds, not the present directed single-error shadow incidence. The nearest mathematical record on *deletions* from no-adjacent-ones words reports a fractional gap at length six, not this Z-channel gap at seven. Search and inspection found no covering statement, but general database/literature incompleteness remains a risk.

**Value — PASS.** The first strict failure of the canonical read-output fractional packing bound is a motivated finite-block obstruction in the intersection of one-sided noise and run-length constraints. The exact bound and number of optima are useful for testing improved converses or constrained asymmetric-code constructions, independent of any long-block asymptotics. This is not a re-tabulation of a known unrestricted channel optimum.

**Limits and residual risks.** No asymptotic results, no generalization to multiple errors, no independent audit, and no assertion that unindexed literature has been excluded. The proof is transparent finite enumeration supplemented by short primal, dual and clique-cover certificates.

Self-review: passed. Independent audit: not yet performed.
