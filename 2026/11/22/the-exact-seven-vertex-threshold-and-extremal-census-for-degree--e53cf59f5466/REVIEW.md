# Scientific review — exact seven-vertex degree-two cut immunity

## Correctness — PASS

The claim is entirely finite and does not depend on extrapolation. The graph universe has \(2^{21}\) exact 21-bit encodings, and each unordered bipartition is represented by one of 63 nonempty subsets excluding a fixed vertex. The attached C++17 source exhausts all 21-bit masks of edge count at most fourteen and tests every such cut vertex by vertex. It finds none without a 2-cut at edge counts zero through thirteen, and exactly 15,015 with fourteen edges. Ten explicitly supplied fourteen-edge masks are individually checked and their pairwise disjoint relabelling orbits reproduce this complete set, yielding a ten-class classification. We inspected the exact supplied source and executed the checker with all assertions enabled. The independent seven-vertex graph-atlas cross-check yields the same ten isomorphism types and orbit sum. The exhaustive source, not a finite sample or a run log alone, is the certificate.

## Originality — PASS (historical priority qualified)

The principal source (Neopryatnaya–Verdenko–Voronov, arXiv:2611.26556, publicly submitted 2026-11-19) proves a universal \(2n-2\)-edge 2-cut theorem, has examples sharp at orders five, six, eight, and reports computed sharp edges at orders nine through fourteen. Its full HTML treatment and conclusion do not cover the order-seven minimum or any of the ten order-seven extremal isomorphism classes. The general bound implies only at least thirteen edges for 2-immunity on seven vertices, so it does not entail the equality fourteen or the extremal census. Gomes–Sau (2019) establishes general bounded-degree cut complexity, not the enumerative seven-vertex question; Bonsma–Farley–Proskurowski addresses matching cuts (degree one), not the 2-cut requirement. Targeted published-record searches and literature searches for seven-vertex 2-immune graphs, equivalent bounded-degree cuts, exact numbers and classifications yielded no covering record. The general Graph Atlas lists seven-vertex graphs but does not itself assert the new 2-cut filtering, edge threshold or orbit decomposition. An unindexed old enumeration remains a residual priority risk; an unsuccessful search is not a proof of global novelty.

## Value — PASS

The paper's list of sharp small orders omits seven, immediately between the sharp examples for orders six and eight, while also listing computational values for orders nine through fourteen. The result closes this natural first unreported small-order gap with an exact threshold and a complete structure classification, rather than an arbitrary induced subfamily or a single example. The ten distinct extremal graph types and their different orbit sizes show that the minimizers are not a unique canonical biclique construction. This is a motivated finite cutoff and exact complete classification; its value does not rely on an unrealized global density theorem. The contribution is confined to seven vertices, and its significance should not be inflated to progress on the general conjecture beyond that finite case.

## Closest literature and limitations

- A. Neopryatnaya, V. Verdenko, V. Voronov, *Edge cuts of bounded degree in sparse graphs*, arXiv:2611.26556v1 (2026-11-19), full HTML: https://arxiv.org/html/2611.26556v1
- G. C. M. Gomes, I. Sau, *Finding Cuts of Bounded Degree: Complexity, FPT and Exact Algorithms, and Kernelization* (2019): https://doi.org/10.4230/LIPIcs.IPEC.2019.19
- P. Bonsma, A. M. Farley, A. Proskurowski, *Extremal graphs having no matching cuts* (2012): https://doi.org/10.1002/jgt.20576

No extension to higher vertex orders is proved. The independent audit has not been performed. Possible historical priority under alternate terminology remains a risk.

Self-review: passed. Independent audit: not yet performed.
