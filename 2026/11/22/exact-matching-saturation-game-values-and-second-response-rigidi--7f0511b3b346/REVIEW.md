# Scientific review

## Correctness — PASS
The two-player score has exact backward-induction recurrences on the set of unmatched vertices. An independent bottom-up C++ calculation enumerates every subset for every one of the five graph skeletons, while a Python program independently constructs the graphs and memoizes the minimax recursion. All five values and both second-move histograms agree; all opening edges are checked. Both programs were executed from the included source files and their parsed outputs agree with `checks.json`. The verified finite domain is explicit, and no infinite-family claim is inferred from computation.

## Originality — PASS, with priority limits
The foundational preprint of Cranston, Kinnersley, O and West, arXiv:1208.0085, was read through its introduction, general results, applications and regular-graph section. The octahedron \(K_6\setminus M_3\) is their known construction, and the tetrahedron/cube entries are elementary. Their bound on the difference between the two starting conventions does not determine the dual icosahedral values \((5,6)\) and \((8,9)\), nor their exact reply multiplicities. The later "matcher game" has a different move protocol. Targeted mathematical-result, title/alias and direct-implication searches found no covering account of the two dual graph evaluations, subject to the risk of unindexed historical literature.

## Value — PASS
The five Platonic one-skeleta are a canonical complete test family for the game, not an arbitrary slice. The dodecahedron and its dual icosahedron exhibit a strict first-move penalty despite complete edge symmetry. On the icosahedron Min-first play can be met with a guaranteed perfect matching, but just one of the 21 second replies preserves that guarantee; on the dodecahedron, both game values lie strictly between the minimum and maximum terminal matching sizes. The exact reply profiles supply strategic information not conveyed by general inequalities or matching-number tables.

## Scope and risks
This is an exhaustive finite calculation, not a symbolic classification of strategies on arbitrary polyhedral graphs. Earlier coverage of the octahedron is expressly acknowledged, and absolute priority for the dual pair is unproved. Same-model consistency checking cannot substitute for independent review.

Self-review: passed. Independent audit: not yet performed.
