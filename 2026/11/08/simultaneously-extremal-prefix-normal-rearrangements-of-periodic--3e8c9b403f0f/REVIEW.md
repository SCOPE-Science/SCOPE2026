# Self-review

## Correctness — PASS

The multiset-window lemma is valid at every length, including more than one full cycle: it decomposes a cyclic interval into entire periods and a submultiset remainder. For arbitrary consecutive \(1\)-occurrences in any rearranged word, the number of intervening \(0\)-runs controls the number of available \(1\)-runs. Sorted large \(1\)-runs ensure the same one-count is reached after no more run boundaries, while sorted small \(0\)-runs ensure that those boundaries have no greater total length. Hence the canonical prefix reaches every achievable one-count no later in absolute position. The proof covers all positive run lengths, all numbers of runs including one, all finite window lengths including zero, and multi-period windows. The extracted finite checker compares all short permutations and directly checks occurrence spans; it is not being mistaken for an infinite proof.

## Originality — PASS, with bibliographic risk

The 2016 prefix-normal-forms paper describes Parikh-envelope representations for an individual word, not a global comparison over all independent run-length permutations. The 2017 run-length jumbled-indexing paper computes individual-string indexes but does not state a simultaneous sorted-run extremizer. The 2018 infinite-prefix-normal paper defines and analyzes the broader property; its inspected sections give no equivalent sorting theorem. Semantic searches for prefix-normal run sorting, rearrangement, cyclic factors, and run-length Parikh maxima found closest public research records about paperfolding prefix-normal defect, binary short-multispectrum codes, and DNA profile rankings; their mathematical objects and quantified comparisons do not imply this result. Accessible historical claims were checked for the same extremal statement; none matched. Searches cannot prove global absence of an earlier equivalent rearrangement lemma, and that possibility remains a documented risk.

## Mathematical value — PASS

The same explicit arrangement is optimal for *every* window length, rather than for a chosen fixed length, over factorial-sized independent run-order families. It solves a natural global run-profile extremal problem, gives a closed-periodic jumbled-count envelope, and provides a constructive infinite class of prefix-normal binary words. Strictness occurs already for \(\{3,2,1\}\) and \(\{1,2,4\}\) at window length five. This is a motivated all-parameter structural theorem, not a numerical isolated slice, routine renaming or narrow certificate.

## Closest prior work and limits

The closest full-text sources are arXiv:1611.09017, arXiv:1702.01280, and arXiv:1811.06273. None was identified as establishing the claimed all-permutation inequality in the material inspected. The alphabet is binary and the period is composed of positive alternating run lengths; no uniqueness of optimizers, aperiodic extension, or independent audit is claimed. The finite code exercises the boundary cases but cannot substitute for the full proof.

Self-review: passed. Independent audit: not yet performed.
