# Scientific review

## Correctness — PASS

Every scattered \(ab\) deletion belongs to a unique ordered pair of constant-letter runs, and deletion within a run is indistinguishable. The proof explicitly characterizes the kernel of the run-pair-to-remainder map: the first-difference argument with rightmost canonical deletion positions forces singleton middle runs and a contiguous \(abab\) block. Iteration proves these moves generate all and only equalities. The resulting graph is a forest of paths, so subtracting its exact edge count gives the theorem. The expected-value formula follows by classifying dependent adjacent run starts and disjoint starts. The independent finite verifier passes all stated exhaustive/random tests and exact rational expectation checks, but does not replace the infinite proof.

## Originality — PASS, with residual risk

The 2026 work of Adamson, Fleischmann and Huch develops complement scattered factors and general algorithms; its conclusion leaves closed formulas in specific cases open. In the inspected text, no arbitrary-input cardinality identity for deleting distinct letters \(ab\) or collision-fiber characterization was found. Semantic searches of related deletion-channel statistics and recoverable earlier results found no claim implying this exact formula. A previously recorded alternating-input/alternating-deletion formula is narrower in source word and does not imply arbitrary-alphabet arbitrary-input coverage. Search absence does not demonstrate definitive priority; equivalent earlier wording may exist in the shuffle/deletion literature.

## Value — PASS

A motivated cardinality problem explicitly raised by the source literature has a closed answer for every word and alphabet in the first nontrivial ordered distinct-letter deletion case. The theorem explains exactly which embeddings collapse, turns count evaluation into one linear scan with constant auxiliary space, and yields an exact uniform-random expected count. It is a structural classification, not merely a recomputed finite table or a restatement of generic set construction.

## Closest literature and limitations

Adamson–Fleischmann–Huch, arXiv:2603.20790v1, §3 (general algorithm), §4 (structural properties), §5 (open counting question). The result does not treat longer or repeated-letter deleted patterns. Independent replication and complete priority validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
