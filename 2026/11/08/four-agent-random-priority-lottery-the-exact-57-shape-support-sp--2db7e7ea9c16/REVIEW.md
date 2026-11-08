# Self-review

## Correctness — PASS

The theorem is a finite exhaustive census. Every one of \(24^4=331{,}776\) labeled strict preference profiles appears exactly once in `rsd4.cpp`'s four nested loops and each priority order once in its inner 24-element loop. Every resulting allocation selects a different unused house for each agent, thus defines a valid matching. The direct computation records the number of different resulting matchings and all positive priority multiplicities. An independently implemented `set`-based allocator in `verify_rsd4_support.py` enumerates 17,550 anonymous ranking multisets, checks their canonicalization under 24 object relabelings gives 762 classes, restores their exact agent-label multiplicities, and verifies the full 57-shape frequency table. Both routines use exact integer counts and assert totals and all support-size cells; they agree entry-for-entry. This is genuinely exhaustive finite proof, not numerical sampling or extrapolation.

## Originality — PASS

Classical all-market results identify the RSD lottery and its equivalence with the core from random endowments, and later work extends lottery equivalence. They do not state the support-size distribution over four-agent preference profiles or the 57 outcome-multiplicity shapes. The initiating 2023 study focuses on efficiency and fairness under uncertain priority, not this exact census. Closest accessible published finite studies count three-agent RSD lottery shapes and four-agent ordinal inefficiency or RSD/probabilistic-serial dominance. Neither property logically determines the present frequencies or forbidden support cardinalities, although their computation domains overlap. A 2014 paper on reachable *sets of houses* studies a distinct invariant; square assignments use all objects. Actual mathematical-record and literature comparisons found no covering table. Residual risk: unindexed enumeration or inaccessible supplementary materials may already contain it.

## Value — PASS

The deterministic matching support is a natural operational measure of how many complete allocations uncertain priority can select, distinct from marginal assignment support. At the first four-agent market beyond a complete three-agent spectrum, a surprisingly constrained set of 57 partitions of the 24 priorities occurs; eight of the 24 potential support sizes are ruled out. Exact frequencies, the mean \(1597/288\), and the rarity \(101/6912\) of support at least 14 give a complete finite benchmark for assignment lotteries and for evaluating compressed lottery representations. The result is a motivated natural classification rather than an arbitrary slice of a large computation.

## Scope and priority limits

The proof is exact for the stated finite model, but the evidence does not yield an all-size theorem. All general lottery-equivalence and Pareto-efficiency characterizations are credited to prior work. The author-manuscript form of one relevant mechanism-equivalence paper was inaccessible; its abstract is consistent with, but does not cover, the exact frequency table. Unindexed prior enumerations cannot be excluded. The review has not been independently replicated outside the included code paths.

Self-review: passed. Independent audit: not yet performed.
