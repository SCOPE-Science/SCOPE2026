# Scientific assessment

## Correctness — PASS

The main statement quantifies over all nonempty finite sequences of factor sizes at least two and all fixed variable widths. A permanent coordinatewise \(k\)-pebble invariant proves the equivalence direction without a quantifier-depth bound: at most \(k-1\) stationary symbols occupy any coordinate, and matching cutoffs at \(k\) are precisely what is needed for a matching next symbol. Conversely, an edge belongs to an order-\(t\) clique exactly when its changed coordinate has at least \(t\) symbols. These clique tests define each truncated factor-size edge class with \(k\) variables. Coloured path distance is definable using the same variable budget by bound-variable reuse. The maximum coloured component distance equals the number of factors in that class, so every multiplicity can be distinguished. The cases of one and two variables and the isolation-width boundary are separately proved. All 482 computational parameter checks passed, but the proof does not depend on extrapolating them.

## Originality — PASS, qualified

The full 2005 paper by Klavžar and Peterin addresses Hamming-graph embeddings and edge labelings, not finite-variable logical equivalence. Grohe and Otto supply general pebble-game theory without this family classification. The complete arXiv HTML text of the 2024 paper by Cai et al. addresses coherent configurations and counting Weisfeiler–Leman equivalence, not the collapse for counting-free logic. Existing classifications of equal-size Hamming factors and of two-factor rook graphs are proper restrictions; they do not imply an exact signature for arbitrary unbounded collections of distinct factor orders. Searches under Cartesian-product, mixed Hamming, pebble-game, and truncated-multiset formulations found no directly covering theorem. Historical-priority risk persists, particularly from broader logical-composition or product theorems that might imply the result without explicitly naming Hamming graphs.

## Mathematical value — PASS

The theorem gives a complete classification for all rectangular Hamming graphs, with arbitrary factor lengths and arbitrary heterogeneous factor sizes, at every finite-variable width. It also identifies the exact isolation width and gives a closed theory census at fixed dimension. These are natural structural invariants of a prominent graph-product class. The central edge-colour/path-diameter argument supplies an intrinsic logical reconstruction of an unbounded factor-multiplicity profile; merely knowing equal-alphabet or two-factor cases does not supply that reconstruction.

## Limits and closest literature

The theorem does not cover counting logic, non-complete factors, labelled coordinates, or a uniform definition of the factor count. Previous restricted cases and general graph-product characterization results are acknowledged. Exact historical priority has not been independently certified.

Self-review: passed. Independent audit: not yet performed.
