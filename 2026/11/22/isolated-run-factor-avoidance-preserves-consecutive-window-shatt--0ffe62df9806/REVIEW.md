# Self-review

**Correctness — PASS.** The exact forbidden-factor condition reduces to a gap of \(r+1\) between consecutive zero coordinates. Every such gap must contain a free interior site when the query support omits all length-\(r+2\) windows. Splitting one bad gap introduces only shorter gaps and preserves every prescribed coordinate; this proves every Boolean trace exists both on a path and a circle. The face formulas follow from gap compositions, and the VC bounds follow from minimal hitting sets for equal-size intervals. The standalone checker independently tested every support for 70 finite domain/parameter cases, 16,260 decisions; these finite tests support but do not establish the universal theorem.

**Originality — PASS, with residual priority risk.** The known isolated-one trigram result is not newly claimed; neither the prior substring-mask work on a single sequence nor the general shattering-extremal literature supplies the new universal longer isolated-run path/circle equivalence as an inspected statement. The common run-avoidance enumerator is credited rather than claimed original. Broad searches of equivalent formulations and indexed findings revealed related two-factor, exact-transition and Walsh-spectrum results with different concept classes or predicates. Some plausible general partial-word results and full texts were not exhaustively checked; absolute priority remains provisional.

**Value — PASS.** The same shattering complex persists under replacement of the forbidden all-one run by a structurally different isolated-one-run factor, for an unbounded family of factor lengths. Simultaneously the cyclic versus linear boundary yields a completely explicit all-order support count and a sharp one-rank drop at each nonmultiple of the window length. This answers a natural structural-completion question extending, not simply renaming, the known length-three case.

**Limitations.** The proof covers neither other palindromes nor multiple forbidden patterns; it does not address online learning. No independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
