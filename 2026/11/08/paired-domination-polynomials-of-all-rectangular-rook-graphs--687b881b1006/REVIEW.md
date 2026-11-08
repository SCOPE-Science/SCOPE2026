# Scientific review: paired-domination polynomials of rectangular rook graphs

## Correctness — PASS

The all-order proof is deductive, not an extrapolation from finite tests. Every selected rook placement corresponds to a unique simple bipartite row–column incidence graph. An empty row together with an empty column is exactly an undominated board square. A perfect matching in the selected rook graph is exactly a partition of the selected bipartite edges into incident pairs. The constructive even-indegree orientation of each connected component proves that this pairing exists if and only if each nontrivial component contains an even number of edges. The labelled exponential formula then retains just these even-edge connected components by the substitution \(z\mapsto-z\) inside a logarithm, resulting in \(\sqrt{F(u,v;z)F(u,v;-z)}\). Inclusion-exclusion over isolated row/column singleton components gives the stated generating function. The minimum-count cases are separately derived by row/column occupancy, including the unique exceptional overlap of nine sets when both dimensions equal three.

Three standalone programs were run from the package paths. Direct matching enumeration and formal integer-coefficient recursion agree on *all* coefficients for seven small rectangles. The independent occupancy program agrees on ten minimum counts, including boards of order five on one side. Output files record the exact results. The general result does not depend on exhaustive enumeration.

## Originality — PASS (self-review)

The 1998 founding article defines paired domination and supplies general theory, while the primary 2011/2013 Cartesian-product work proves inequalities for paired domination, not full configuration counts. The 2024 rook-graph polynomial treats **ordinary** domination, so its coefficient counts do not imply the paired counts; the direct \(2\)-by-\(2\) degree-two coefficients are six versus four. The 2005/2007 paired-product works are related by predicate but their accessible abstracts and summaries concern bounds, not a full two-parameter weight enumerator. Searches for `paired domination polynomial rook graph`, `paired domination polynomial line graph complete bipartite`, `paired dominating sets Cartesian product complete graphs enumerating`, and the even-edge component parity formulation did not find a prior equivalent theorem. Accessible research-record comparisons concerned distinct graph families (complete multipartite graphs, chain graphs) and do not subsume rook graphs. The general even-edge line-graph matching lemma and exponential formula are treated as known techniques, not original independent claims.

The early 1998 full article and the complete 2005/2007 publisher versions were not fully inspected. Search failure alone is not proof of novelty. These are historical-priority risks, not formal counterexamples; any future exact equivalent formula would supersede the present novelty assessment.

## Value — PASS

The complete paired-domination polynomial records every feasible set cardinality on an infinite natural class of Cartesian products, rather than only the numerical optimum. Its component-parity characterization is an efficient structural criterion that separates backup-pair feasibility from simple rook domination, and the formal square-root expression is a usable exact counting mechanism. The leading coefficients display genuine parity and boundary effects, including a nontrivial exceptional overlap at the smallest odd square. Ordinary domination polynomial and general paired-domination inequalities do not supply those counts.

## Source comparisons and scientific limits

The closest primary literature is Haynes–Slater (1998, definition and bounds), Brešar–Henning–Rall (2005/2007, Cartesian-product bounds), Choudhary–Margulies–Hicks (arXiv:1109.2174; 2013 journal, Cartesian-product inequalities), and Mertens (arXiv:2401.00716, the ordinary rook domination polynomial). The connected line-graph parity lemma has a classical explanation through perfect matchings of even claw-free graphs; no claim of its separate priority is made. See `RESULT.md` for the exact theorem and proof and `VERIFICATION.md` for reproducibility. The formula is formal, no asymptotic complexity claim is made, and publisher-access gaps and potential unindexed calculations limit historical certainty.

Self-review: passed. Independent audit: not yet performed.
