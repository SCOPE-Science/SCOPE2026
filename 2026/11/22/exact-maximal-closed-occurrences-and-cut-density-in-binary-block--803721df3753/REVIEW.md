# Review of exact maximal closed occurrences and cut density

## Correctness — PASS
The occurrence characterization follows by classifying closed mixed factors according to whether the witnessing border is mixed (then it has period equal to the primitive two-run period, and any proper occurrence extends) or unary (then its two copies must be in successive equal-letter runs). Unary runs and the entire word supply the other MCSs. A direct counting argument gives the total, while an offset bound for bridges at every cut gives the sharp cut maximum. Two different exhaustive border/extension implementations corroborate all interval endpoints in 97 and 48 small parameter settings, respectively, and a separate large symbolic family confirms the cut formula. Computer checks do not prove the infinite result; the written combinatorial argument does.

## Originality — PASS against accessible evidence
The classic MCS paper introduces the global object and algorithm, but not these exact periodic-family endpoints. The earlier four-run formula already gives the two-period total count; it does not give the classification for all repetition counts or the sharp cut maximum. The 2026 RLE and internal-query papers contain broadly applicable tools and upper bounds, not a verified identical explicit theorem in the accessible material. Their full texts could not be inspected, leaving a specific historical-priority risk. Searches covered aliases: maximal closed repeats, maximal gapped repeats, two-run block powers, periodic MCS, and gap/cut crossings.

## Value — PASS
The natural run-length-encoded family \((0^a1^b)^k\) is a small but nontrivial test class for MCS output size and internal-cut density. Its complete endpoint set is linear in the number of blocks, while the exact worst cut density depends on the primitive period and not on the number of repetitions. This gives a precise structural boundary case relevant to compressed enumeration and localized queries, beyond simply evaluating an existing general upper bound.

## Limits and closest sources
The general problem remains more difficult for nonuniform run profiles. The four-run total-count specialization was previously covered. The 2026 internal-query and compressed-enumeration preprint full texts were unavailable for complete equivalence checking; neither access failure is represented as proof of novelty. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
