# Scientific review

## Correctness
PASS. The state decomposition is exhaustive because any independent set contains at most one clique vertex, and such a vertex excludes only its own private leaf. Original-graph distances prohibit leaf-to-leaf two-hop moves but permit all clique-to-leaf moves. The adjacency classification follows directly. Every exchange of a leaf label requires two moves; an unmatched pure/mixed endpoint contributes one additional move. Constructive paths attain every bound, including the mixed-to-mixed zero- or one-move exceptions. This proves all pairs of distances, the maximum formula, edge counts, degrees and connectivity. Independently rebuilt graphs pass exhaustive BFS comparisons for every parameter pair through eight clique vertices; this does not replace the general proof.

## Originality
PASS, subject to ordinary historical-priority risk. The primary 2024 bounded-hop study proves reachability on split graphs and explicitly leaves the complexity of shortest two-hop split-graph reconfiguration open. Its inspected Introduction, Section 4 (split-graph cluster lemmas and decision algorithm) and Section 6 (open questions) do not give a clique-corona metric, its exact diameter or its degree/edge census. A 2021 split-graph study treats one-hop token sliding and hence cannot imply these two-hop distances. Related indexed token-sliding and Johnson-metric results involve different base graphs or other reconfiguration rules. Neither searches nor differing names prove universal novelty; a prior equivalent using corona, thin-spider or Johnson-incidence terminology remains possible.

## Value
PASS. The 2024 source identifies shortest two-hop reconfiguration on split graphs as a motivated, unresolved complexity direction. This infinite canonical split-graph family exhibits an exact metric, constructive optimal routing, a sharp three-regime diameter, and a complete two-orbit degree and edge census, stronger than a reachability assertion. The result identifies a nontrivial Johnson-type internal structure and explicitly limits the progress to the family, not the open general case.

## Closest literature and limits
The closest same-rule primary source is arXiv:2407.11768 (2024), particularly Section 4 and the concluding open question. The related one-hop sources are Belmonte et al., *Token Sliding on Split Graphs* (2021), and Hoang et al., *Shortest Reconfiguration Sequence for Sliding Tokens on Spiders* (2019). The latter concerns a tree with one branching center, not a clique with private leaves. An independently verified precedence determination is not claimed.

Self-review: passed. Independent audit: not yet performed.
