# Scientific review: universal next-window support in bounded-density binary de Bruijn cycles

## Correctness — PASS
The proof constructs an Eulerian overlap graph, encodes all legal consecutive-window pairings by a necklace-connection multigraph, and characterizes their realizability by whether a selected edge is a bridge. The bridge classification treats parallel edges, primitive periods, the all-zero necklace and the top-weight necklace separately. The explicit detour handles potential interior bridges. Actual independent finite bridge and Euler-transition computations passed. No finite search is asserted to prove the quantified theorem; the all-parameter proof supplies that scope.

## Originality — PASS, qualified
Sawada, Stevens and Williams (2011) establish existence and generation of bounded-density binary de Bruijn cycles; Sawada, Williams and Wong (2013, 2016) establish broad gluing and necklace-generation methods. A published unrestricted next-order support theorem covers \(k=n\), while a complete weight-at-most-two cycle classification covers the fixed \(k=2\) source and may imply its window support. The all-interior-weight support law and its sharp divisibility criterion were not found in those primary sources or scoped mathematical-result comparisons. Earlier equivalent work in universal-cycle adjacency remains an unresolved priority risk; no absence-of-search-result is treated as a proof of novelty.

## Mathematical value — PASS
The theorem answers an exact, natural design question: which locally feasible length-\(n+1\) windows occur in at least one maximal-coverage bounded-weight cyclic source? The answer changes arithmetically precisely when the weight bound divides the window order. The result is an all-length structural classification, not only a small-case count. It does not count individual cycles or prescribe several transitions simultaneously.

## Literature and limitations
Original bounded-density cycle construction: https://www.socs.uoguelph.ca/~sawada/papers/max_density.pdf (2011). Weight-range gluing: https://www.socs.uoguelph.ca/~sawada/papers/den-range.pdf (2013). Greedy/necklace theorem: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v23i1p24/pdf/ (2016). Known unrestricted endpoint and fixed weight-two enumerations are ceded as antecedents. Independent mathematical review has not been performed.

Self-review: passed. Independent audit: not yet performed.
