# Review

## Correctness (PASS)

The proof uses the independent uniform parent process, the exact subtree-size martingale scaling, and the one-step conditional product for a parent-choice indicator. Summing a telescoping covariance yields all three cases for every label pair and every finite tree size, including deterministic boundary columns. The standalone verifier tested all recursive trees through nine vertices by exact rational arithmetic (6,322 assertions including further column-sum checks). Enumeration is not the basis of the all-size proof.

## Originality (PASS, with residual risk)

The relevant primary literature separates degree counts (Kuba–Panholzer 2007) from descendant-subtree sizes and their two-vertex joint law (Kuba–Panholzer 2006, 2009). The mixed direct-child/whole-subtree kernel, its strict triangular sign structure, and its equal-share cancellation are not explicit in the material inspected. Published-record searches for degree/subtree covariance aliases found no equivalent or stronger stated theorem. An older multivariate increasing-tree generating function might imply the formula without stating it; historical-priority risk remains and independent audit has not occurred.

## Value (PASS)

Direct branching and entire genealogical lineage are the natural local and global birth-indexed descriptors of the uniform random recursive tree. The result gives the complete all-label dependence kernel, with exact sign localization, an unexpected downstream zero-covariance region, and a conservation-driven equal-share cancellation across older vertices. It provides a reusable baseline for age-sensitive dependence and distinguishes correlation from genealogical dependence.

## Limits

The law does not assert independence or extend automatically to nonuniform attachment. Exhaustive checks are finite; the analytic argument is necessary. Historical priority is qualified.

Self-review: passed. Independent audit: not yet performed.
