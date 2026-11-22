# Scientific review

## Correctness — PASS

Every invariant five-mer set is a union of sixteen two-element reverse-complement orbits. The two constant loops and the alternating two-cycle force particular orbits. A finite exhaustive search of all 14893 orbit subsets of size at most six, using two independently implemented graph methods (Kahn elimination and DFS cycle checking), certifies that exactly ten six-orbit choices and no smaller choices decycle the graph. All ten exact rational first-hit expectations follow by acyclic recurrences, with path and complementation statistics checked. The result makes no infinite-order extrapolation.

## Originality — PASS (qualified)

The 2003 foundational source develops unavoidable sets and graph reformulations. The 2024 reverse-complement sketching paper states the known twelve-word optimum and a shortest residual path length of six for one optimized selection, but neither its inspected main result nor its tables classify every optimal selection or their full path/expectation spectra. The 2026 parity theorem concerns existence and a lower-bound obstruction, not enumeration of the ten equality cases. No indexed statement found in the targeted comparisons implies the new classification. A supplementary archive associated with the 2024 study was not accessible for inspection, and unpublished software could duplicate the count.

## Value — PASS

This complete classification resolves the natural equality layer of a constrained minimum-decycling problem, rather than a selected arbitrary parameter table. At fixed minimum sampling density, the only ten admissible selectors have different worst-case guaranteed-hit windows (eleven, thirteen and fifteen symbols) and distinguishable exact uniform-hit expectations. This directly identifies the available optimization tradeoff and permits independent benchmarking of strand-invariant short-word selectors without asserting practical DNA conclusions.

## Scope and residual risk

This is an exact small-instance result, not a general-order formula. Real genomic input is not modeled by uniform fair bits. Prior completeness could be affected by unindexed numerical experiments and unavailable ancillary files. Two code paths verify the new computations; no external independent mathematical audit is asserted.

Self-review: passed. Independent audit: not yet performed.
