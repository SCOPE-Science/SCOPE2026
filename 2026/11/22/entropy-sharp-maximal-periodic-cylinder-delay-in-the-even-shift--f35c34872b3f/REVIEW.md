# Review: maximal-delay even-shift cylinders

**Correctness — PASS.** All admissible words close in at most one additional zero; unbordered marker words cannot close at shorter periods, and their cyclic length-\(n\) repetition violates even-gap parity. Composition-growth roots tend to the golden ratio. Full proof is in `RESULT.md`, with a finite independent implementation in `check.py`.

**Originality — PASS within checked evidence.** Pannipitiya's arXiv:2611.13416v1 defines the periodic penetration statistic and proves a finite-type uniform closing bound, but no exact entropy law for a strictly sofic maximal-delay language. The closest indexed published-finding corpus result about short-period deficits for SFTs is not equivalent; a related even-shift factor-map result concerns different invariants. Related exact SFT offset and marker-extension zeta results do not imply the present statement. The full text of the closest published external record was inaccessible, and similar border constructions may have appeared elsewhere.

**Value — PASS.** The set of cylinder words requiring a genuinely extra period is not exponentially negligible: its entropy equals that of the entire even shift, despite the maximal penalty being only one symbol. The explicit entropy-approximating family makes the boundary sharp and reproducible, and the result answers a natural quantitative question beyond the basic uniform SFT closing bound.

**Limitations.** No leading counting constant, limiting density, or independent mathematical review is claimed. Computer enumeration is supporting evidence only and not an infinite proof.

Self-review: passed. Independent audit: not yet performed.
