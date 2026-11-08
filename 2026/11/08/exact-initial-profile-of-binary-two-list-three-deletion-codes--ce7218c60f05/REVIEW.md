# Review: exact binary two-list three-deletion profile

## Correctness

PASS. For each of the eight lengths the result reduces to a fully enumerated binary subsequence-incidence matrix. Each explicit witness is checked against all possible deletion outputs. Nonnegative rational output weights and the derived nonnegative slack for every input word supply a dual upper bound strictly below the next integer, so the witness is provably optimal. The supplied standalone checker independently reconstructs every incidence by greedy subsequence testing; no floating-point optimization output is used as mathematical evidence.

## Originality

PASS against inspected sources, with historical-priority uncertainty. Lin (arXiv:2609.26650, full eight-page text inspected) proves general asymptotic bounds using deletion hypergraphs and does not state an exact small-length three-deletion/two-list profile. Guruswami–Håstad (arXiv:2007.10592, accessible abstract and bibliographic information inspected) concerns asymptotic two-deletion list codes; that statement does not imply the listed values. Indexed related exact results address either two-deletion/two-list optimization or three-deletion pairwise reconstruction, neither of which implies the present two-list/three-deletion integer program. Unindexed finite tables and uninspected full secondary manuscripts remain priority risks.

## Value

PASS. The fixed first nontrivial list size and three-deletion count give a natural first exact finite benchmark in a model primarily studied asymptotically. The first eight blocklengths display a nontrivial four-codeword plateau followed by a sharp increase at length eight, and the two larger values have independently checkable rational optimality certificates. Such exact small instances can benchmark hypergraph methods and code constructions without requiring an asymptotic theorem.

## Limits

The theorem covers only binary lengths three through ten, exactly three deletions and output-list size two. It does not establish encoding complexity, further lengths or uniqueness. The self-review is not independent validation.

Self-review: passed. Independent audit: not yet performed.
