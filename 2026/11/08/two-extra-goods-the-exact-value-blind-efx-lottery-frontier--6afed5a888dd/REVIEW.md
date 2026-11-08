# Scientific self-review

**Correctness — PASS.** The exact domain and EFX quantifiers are defined in `RESULT.md`. Positive values rule out empties, giving only T and D occupancies. The bottom-four criteria, matching adversarial valuation witnesses, and symmetrization prove an equality, not just a bound. The standalone standard-library checker performed 46,964 assignment-level EFX recalculations; finite checks support but cannot replace the proof. No computation-dependent infinite assertion is used.

**Originality — PASS (with residual risk).** Neoh–Teh (arXiv:2504.03951) already prove the universal \(n!\) EFX-count lower bound under identical valuations. Cohen–Teh–Wooldridge (arXiv:2609.28333) already use a uniform randomized balanced assignment at exactly one extra good. Neither inspected text settles the present two-extra-good value-blind minmax upper bound or the opposed T/D valuation witnesses. Searches of the relevant research records returned no covering claim; absence of matches does not prove uniqueness. See the four separate comparisons and source inspections in `AUDIT.json`.

**Mathematical value — PASS.** A natural question about ex-ante fair value-independent online allocations has an exact sharp minimax answer, an implementable optimal lottery, and a precise \(n^{-4}\) reliability law at two surplus goods. The two shape classes and opposed valuation regions constitute a structural boundary; the result is not claimed for value-aware policies or heterogeneous agents.

**Limitations.** Strictly positive common values, two surplus goods and value-independent actions are essential. The mathematical proof and finite checker are not independent validation. Unindexed equivalent work remains possible.

Self-review: passed. Independent audit: not yet performed.
