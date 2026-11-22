# Scientific review

## Correctness
**PASS.** The proof first counts all distinct one-insertion supersequences, then subtracts disallowed run extensions for admissible receivers, and exactly counts the only possible repair of an overlong receiver. Distinct parent words rather than insertion positions are used consistently. Two disjoint run-composition constructions establish the rational bivariate spectrum. A dominant double-pole argument, using aperiodicity for \(h\ge2\), proves the limiting geometric distribution. The checker independently tests 20,470 receiver words, all parent lists, and the formal-series histograms.

## Originality
**PASS, with bounded historical uncertainty.** The 2018 supersequence-distribution study treats unrestricted binary parents; the 2021 RLL paper counts/optimizes constrained codes and develops source asymptotics; the 2020 RLL-SIDC paper develops a code construction. None of the examined mathematical statements includes a complete all-cap, all-receiver one-deletion inverse-list formula or its limiting geometric law. Earlier locally relevant records about the asymmetric no-`11` source and about deleted *overlapping reads* do not imply this symmetric run-cap result. Equivalent results in unindexed deletion-channel literature remain possible and should be investigated independently.

## Value
**PASS.** Maximum-homopolymer constraints are standard in coding for synchronization-sensitive storage. The result provides an exact finite-length ambiguity distribution and an explicit limiting fraction of receiver strings that determine a unique source. The surprising distinction is that atypical receiver strings containing one overlong run dominate feasible receiver observations, and their small decoding lists have a nondegenerate geometric law. This is an all-parameter reconstruction invariant, not a one-off short-length computation.

## Limits
The uniform-output law is not a source-conditioned likelihood; no optimal error-correcting code size or multiple-deletion capacity follows. Historical priority has not been independently certified.

Self-review: passed. Independent audit: not yet performed.
