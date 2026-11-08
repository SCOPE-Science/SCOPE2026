# Review: Exact gap-constrained subsequence spectra of repeated permutation words

## Correctness — PASS

For \(q\ge2\), all host lengths \(qk\), query lengths \(h\), and arbitrary positive interval constraints on successive selected position differences, each query's letters determine a unique residue at every position. If a gap interval includes the needed residue, its least permissible representative lies among the first \(\min(q,b_i-a_i+1)\) differences. Greedily choosing those representatives gives the componentwise-earliest embedding. The mapping from initial phase and these differences to a distinct query is bijective, making the product generating polynomial an exact **distinct-language** enumerator rather than an embedding count. The maximal endpoint and inclusion–exclusion derivation prove all sharp thresholds and formulas, including \(h=1\), \(k=1\), and bounded intervals shorter than one period. The standalone verifier checked 1,472 exhaustive uniform instances and 4,000 seeded nonuniform instances, including counts and the uniform binomial expression. These finite checks are supplementary; the general statements rest on the explicit proof.

## Originality — PASS, qualified

The closest full-text comparison is Day–Kosche–Manea–Schmid, arXiv:2206.13896v1, which studies general gap-constrained matching and language analysis and proves general complexity results, not an exact distinct-query spectrum for powers of a permutation. The substantive comparison is with their definition of gap constraints, formal matching problems, and language-analysis discussion, not a title comparison. Adamson et al., arXiv:2304.05270, study gap-constrained longest common subsequences; Manea–Richardsen–Schmid, arXiv:2404.10497v1, consider generalized nonadjacent gap constraints and matching algorithms. Neither inspected statement gives the exact phase-by-phase bijection, product polynomial, or saturation boundary for the restricted host family. Published-record searches for repeated-permutation and periodic-host gap enumerations yielded no exact equivalent. The closest earlier related records concern editing distance to ordinary subsequence universality or distribution of unconstrained binary subsequence universality; both leave the requested finite-host gap constraints unaddressed. Accessible historical claims about binary bounded *total window* and rotation-complete necklaces use mathematically different acceptance conditions. Unindexed or implicitly derivable coverage remains a residual bibliographic risk, and the search does not prove uniqueness.

## Value — PASS

Variable-position gap intervals are a standard pattern-matching model with generally difficult language analysis. The theorem solves a complete nontrivial infinite host family, including the exact number of **distinct words** (not potentially many placements), the infinite-host local language, and the precise finite-host length for saturation and full universality. The dependence on \(\min(q,b_i-a_i+1)\) identifies a meaningful sharp transition between missing and complete residue coverage. The model is motivated by periodic streams and prescribed interarrival windows. This supplies substantially more structural information than running a standard dynamic program for one fixed query.

## Closest literature and limitations

- Day, Kosche, Manea, Schmid (2022), arXiv:2206.13896v1, general interval/regular gap-constraint matching and language analysis.
- Adamson et al. (2023), arXiv:2304.05270, gap-constrained LCS.
- Manea, Richardsen, Schmid (2024), arXiv:2404.10497v1, generalized gap constraints.
- The alphabet must appear as a permutation in each period; arbitrary multiplicities, noninterval gaps, and embedding counts are not covered. An equivalent formulation could be hidden in unindexed or uninspected material.

Self-review: passed. Independent audit: not yet performed.
