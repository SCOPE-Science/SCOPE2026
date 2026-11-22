# Scientific review

**Correctness — PASS.** The first BWT row is preceded by one. At separated positive zero gaps, the only one in level \(t\) occurs at a gap of length \(t\), and an all-zero level separates marked levels; the one-starting suffix contributes only zeroes. Partition enumeration of ordered gap multisets and a uniform-composition union bound complete the claimed all-parameter theorem. The proof includes cases \(k=1\), periodic inputs for the upper bound, and all boundary inequalities. Executable checks supply independent finite tests, not infinite certification.

**Originality — PASS (against inspected sources).** Giuliani et al. already give isolated polynomial-gap constructions with \(2k\) runs; a published increasing-gap theorem gives a complete transform for a different boundary structure; a published fixed-weight-three theorem proves a sharper special-case spectrum. Direct comparison of objects, hypotheses and implications establishes that those do not provide this all-weight partition count or the uniform \(k=o(n^{1/3})\) random law. Kumallagov's 2026 article considers a different maximal-unclustering problem. Residual risk: unindexed earlier equivalent work.

**Value — PASS.** The sharp sparse-weight BWT law quantifies how frequently a compression transform reaches its maximal number of runs despite the input's few markers; the primitive-necklace partition count is a natural exact object. No assertion is made that the sufficient sparsity threshold or full maximum-run count is optimal.

Self-review: passed. Independent audit: not yet performed.
