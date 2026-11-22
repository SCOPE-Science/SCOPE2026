# Scientific review: maximal gap-run spectrum of quotient semigroups

## Correctness — PASS

The integer-interval decomposition is exact because a fixed number of consecutive generators gives every intermediate integer. For every quotient modulus \(p\ge2\), the nonempty interval threshold is \(h=\lceil p/2\rceil\). Successive endpoint differences equal \(k-\lfloor t/p\rfloor-\mathbf1_{t\bmod p\ge h}\). They remain positive in exactly \(p\) consecutive locations for each length \(k-1,\ldots,1\), with the single initial block of length \(hk\). This proves completeness, boundaries, genus and Frobenius number without appealing to finite data. The standalone checker separately confirms 975 parameter pairs and 246,675 maximal blocks using a direct modular membership test.

## Originality — PASS on inspected evidence

Liu, arXiv:2312.10889 (2023), gives generating functions and generators for quotients; Cabanillas, arXiv:1904.08240 (2019), gives general lattice/continued-fraction descriptions and Frobenius/genus algorithms; Adeniran et al., arXiv:1809.09360 (2018), gives genus formulas. A related indexed 2026 result finds the three isolated gaps for the particular quotient \(\langle3k+1,3k+2\rangle/3\) and provides a full Apéry set; that stronger data can imply the entire \(p=3\) specialization. Accordingly no independent novelty for that specialization is asserted. It does not give an all-modulus run-frequency classification. Another indexed result gives uniform run statistics for *unquotiented* two-generator semigroups, a different object. In the inspected primary sections and indexed mathematical statements, no equivalent two-parameter maximal-run histogram was found. A sufficiently general algorithm might yield this formula upon specialization, but neither the exact count statement nor its derivation was present in the inspected materials. This is best-knowledge originality, not independent publication-priority certification.

## Mathematical value — PASS

The lengths and frequencies of maximal missing-integer intervals are natural local invariants that genus and Frobenius number alone do not determine. A complete simultaneous classification for every integer quotient modulus is a uniform higher-modulus classification beyond the previously analyzed small-modulus case: it gives every possible length and every frequency, including an unexpectedly uniform multiplicity \(p\) for all shorter lengths. The theorem also supplies compact closed formulas for the resulting global invariants and an exact bivariate enumerator. No arbitrary parameter slice or numerical cutoff is used.

## Residual risks

The broad quotient literature contains lattice-based general algorithms, so the result might be implicitly obtainable from older formulas even though no direct statement was located. Indexed mathematical work published in 2026 was not fully readable in every case; the threefold isolated-gap result is explicitly narrower. The proof has been reviewed within the same process but not independently.

Self-review: passed. Independent audit: not yet performed.
