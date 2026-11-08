# Scientific review: role-marked domination–location polynomial of cycles

## Correctness — PASS
For \(n\ge5\), two exterior vertices have the same nonempty locating signature only when they lie two edges apart and have no selected neighbor except their common midpoint. This proves the exact \(00100\) obstruction. The distinct domination requirements give \(000\) and \(111\). The weighted sixteen-state de Bruijn transfer counts labelled cyclic words without overcounting; an exact characteristic-polynomial calculation yields the six-term recurrence and initial polynomials. Positive coefficients and two attaining terms give the sharp least and greatest class sizes. The dominant-root argument yields the asymptotic. Recomputed symbolic determinant and independent all-subset graph checks through cycle order 16 support, but do not replace, the infinite proof.

## Originality — PASS, with residual risks
The motivating work [1] proves a much broader *existence* theorem (Theorem 6) for all graphs without isolates, but contains no labelled enumeration for cycles. Work [2] treats the stronger condition that **both** classes are locating-dominating, mainly as an existence question on specific graph families; even a complete count of two-sided partitions would not automatically count one-sided DLDS partitions. Related published graph-polynomial work found in mathematical records concerns other graphs or domination variants, without an implication covering this exact mixed-role polynomial. Exact phrase, alias, and broad semantic searches did not locate a theorem implying the displayed sextic recurrence, the complete cycle coefficients, or the sharp size interval. Searches do not prove historical novelty: an unindexed earlier generating-function treatment may exist.

## Mathematical value — PASS
The theorem addresses the explicit natural counting gap after an existence theorem and determines **all** size coefficients for an infinite graph family. Three exact forbidden local configurations reduce the enumeration to a nontrivial weighted finite-state system with a factored characteristic polynomial, sharp feasible class-size boundaries, and an explicit asymptotic growth constant. These are structural and enumerative conclusions, not simply another existence construction or a small numerical table.

## Closest prior sources and limits
[1] D. Chakraborty, F. Foucaud, M. A. Henning, T. Laihonen, “A Note on Partitioning the Vertex Set of a Graph into a Dominating Set and a Locating Dominating Set,” *Electronic Journal of Combinatorics* 33(1), P1.51 (2026), DOI 10.37236/14049. Inspected the published full-text statement and proof sections.

[2] F. Foucaud, P. V. Maniya, K. Paul, D. Pradhan, “Locating-dominating partitions for some classes of graphs,” *Discrete Mathematics* 349 (2026), 114886, DOI 10.1016/j.disc.2025.114886. Inspected the open full text's definitions and existence theorems.

The graph, role ordering, vertex labels and minimum order are material hypotheses. Finite enumeration is not a proof beyond the checked orders. Historical priority and the proof still require independent assessment.

Self-review: passed. Independent audit: not yet performed.
