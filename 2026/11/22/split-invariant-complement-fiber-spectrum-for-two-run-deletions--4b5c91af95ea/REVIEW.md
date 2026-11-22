# Scientific review

## Correctness: PASS

The four block tokens are exhaustive and disjoint for each source block. A two-run deleted subsequence permits no more than one empty token, and no `B` before `A`. This forbids creation of `01` across block boundaries, so every remaining adjacent `01` recovers a unique intact source block. The `01` counts distinguish zero-empty-token from one-empty-token outputs; the latter have a unique nonempty token decomposition and a central insertion gap. Weak-composition counting proves the all-parameter formula. Direct positional enumeration (447 parameter triples, 7,181 embeddings) and independently generated token-model fibers (286 cases) agree. The scripts and captured outputs are embedded. No finite computation is used as the proof of the infinite quantifiers.

## Originality: PASS against inspected evidence

The full text of Adamson–Fleischmann–Huch (arXiv:2603.20790v1), particularly its definition, algorithms, Section 4 and conclusion, was inspected. Its generic procedures do not state the exact prescribed two-run residual histograms. A related alternating-deletion result has a different deleted pattern, the general two-letter run-pair formula concerns only deletion length two, and a fixed-composition result counts the union across deleted patterns rather than a fixed pattern's fiber distribution. The earlier 2004 subsequence enumeration concerns all deleted patterns. No equivalent split-invariant fiber formula was located in the inspected indexed results and targeted public searches. Unindexed historical shuffle identities remain possible and independent priority assessment has not occurred.

## Value: PASS

This is an all-length, all-run-split classification of the exact preimage multiplicity law for a natural family in a recently introduced complement-set problem. It detects a structural dichotomy between singleton fibers and gap-dependent collision fibers, explains why distinct deleted patterns of the same length have identical full fiber spectra, and replaces a general embedding-enumeration procedure by a closed formula. Its value comes from this structural equality and complete collision profile, not merely a low-degree binomial count.

## Limits

Only binary alternating hosts and prescribed two-run deleted patterns of length at least three are covered; neither general patterns nor general hosts are classified. Checks at finite lengths are regressions, not infinite certificates. Historical priority outside inspected literature remains open.

Self-review: passed. Independent audit: not yet performed.
