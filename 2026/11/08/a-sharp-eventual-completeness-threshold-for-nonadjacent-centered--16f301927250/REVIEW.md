# Scientific review

## Correctness — PASS
The exact identity \(B_n=B_{n-1}\cup(c_n+B_{n-2})\) partitions admissible subsets by whether their last index is selected. Two different implementations of that identity exhaustively verify \([9084,17230]\subseteq B_{41}\), \([9084,18522]\subseteq B_{42}\), and \(9083\notin B_{45}\). Larger indices cannot contribute to \(9083\) because \(c_{46}=9316\). The explicit inequalities for \(U_n=\lfloor n^3/4\rfloor\) prove interval coverage for all \(n\ge41\). No experimental observation is substituted for the infinite proof.

## Originality — PASS within inspected evidence
Kureš' 2023 result permits repeated centered nonagonal terms. OEIS A352349 permits distinct terms but no index separation; its known cutoff is \(2648\). Dantas e Moura and coauthors' fully accessible 2022--2023 work treats greedy \(S\)-legal index-difference sequences rather than legal sums from a fixed quadratic sequence. Targeted indexed literature and mathematical-record searches, including equivalent descriptions by sparse representations and Zeckendorf-type legality, found no stated implication giving the threshold \(9083\). The short Kureš article was available only as a bibliographic preview, and unindexed equivalent work remains a risk; absence of search results is not treated as uniqueness proof.

## Mathematical value — PASS
The no-consecutive-index condition is the classical Zeckendorf legality constraint, here imposed on a historically studied family of centered figurate numbers. The exact obstruction \(9083\) quantifies how this structural restriction changes eventual additive completeness from the already-tabulated unrestricted distinct-summand threshold \(2648\). The induction supplies a finite-to-infinite mechanism and the exact cutoff, not merely large numerical experiments. The result is naturally limited to one meaningful case and does not purport to classify all forbidden index sets.

Self-review: passed. Independent audit: not yet performed.
