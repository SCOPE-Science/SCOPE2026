# Review of the finite binary suffixient-sensitivity theorem

## Correctness — PASS

Definitions agree with the supermaximal-right-extension characterization of minimum suffixient-set cardinality in Fujimaru et al. [1], Definitions 1–5. Lemma 2 justifies the optimized one-letter left-extension test. All \(32{,}766\) binary words and \(425{,}986\) directed one-bit substitutions through length fourteen are checked; two independent finite SRE implementations agree everywhere. The complete equality list contains sixteen positive directed edges, all with measure five to eleven. Direct position-set exhaustive checks independently confirm the key four witness pairs. The claim is finite; no asymptotic extrapolation is inferred.

## Originality — PASS against inspected sources

[1] proves asymptotic \(\Omega(\sqrt n)\) edit sensitivity for the same measure, but does not give the exact first six-unit binary threshold or full finite sensitivity profile and equality set. [2] treats suffixient-set decision algorithms and [3] online maintenance. Searches for exact binary finite sensitivity, equivalence through right-maximal extension characterizations, and stored adjacent finite-table results found no dominating claim. Distinguishing from an indexed string-attractor or insertion-covering table is necessary: those are different statistics. Residual risk: an obscure or unpublished equivalent finite enumeration cannot be ruled out by text search.

## Mathematical value — PASS

The sensitive quantity controls the necessary number of suffixient samples in compressed-search structures. A one-bit flip at the shortest possible word length can raise that minimum from five to eleven, more than doubling it. Exact first-threshold data, the full small-length profile and complete extremizer classification give a motivated reproducible boundary for index stability and complement the asymptotic lower-bound theory; this is not a trivial substitution or mere benchmark of unrelated data.

## Limits

The proof is a finite exhaustive computer-assisted result, with source code, outputs and independent direct-witness testing, not an infinite symbolic theorem. Claims beyond length fourteen or a uniqueness assertion against all possible historical literature are expressly excluded. Independent verification by a different author is not asserted.

Self-review: passed. Independent audit: not yet performed.

## References

[1] H. Fujimaru et al., *Smallest Suffixient Sets: Effectiveness, Resilience, and Calculation*, arXiv:2506.05638, Sections 3–4. https://arxiv.org/html/2506.05638v7

[2] D. Cenzato et al., *Testing Suffixient Sets*, arXiv:2506.08225, Sections 2–3. https://arxiv.org/html/2506.08225v2

[3] D. Köppl and G. Kucherov, *Smallest Suffixient Set Maintenance in Near-Real-Time*, MFCS 2026, DOI 10.4230/LIPIcs.MFCS.2026.86.
