# Scientific review: median-component decomposition of the one-pass pop-stack permutation graph

## Correctness — PASS
The class is the established direct sum of descending blocks, one for each composition. The central new lemma analyzes inversion graphs on values: an adjacent-position swap toggles exactly one inversion edge, and preserving the disjoint-clique inversion graph forces precisely the local move \(2\leftrightarrow1+1\). Fixed blocks of size at least three determine components, with the intervening one/two-block tilings yielding Cartesian products of Fibonacci cubes. The deletion-before-insertion route proves exact Hamming distance, alternating strings give exact diameters, and the signature construction gives both rational enumerators. Direct program checks used actual permutations, actual pop-stack operation, adjacent-swap edges, all pairwise graph distances through \(n=8\), and component formulas through \(n=12\). These computations corroborate, but do not replace, the all-length proof.

## Originality — PASS (historical-priority risk remains)
Pudwell–Smith [1] gives the one-pass sortable class and its composition parametrization; that fact is explicitly prior, not claimed new. Bauer–Copenhaver [2] analyzes iteration counts for the same pop-stack operator, not the induced graph under feasible adjacent-position swaps. Literature and published-finding corpus searches using the specific avoidance pair, adjacent swaps, weak-order formulations, layer-block invariants, and Fibonacci factors did not locate a covering statement. Related permutation reconfiguration results for other avoidance classes are not implication-equivalent: their legal moves and component signatures differ. In particular, an accessible earlier result for \(\operatorname{Av}(231,321)\) yields a connected facilitated hypercube, whereas the present graph on \(\operatorname{Av}(231,312)\) is disconnected for \(n\ge3\). No absence-of-search-result is treated as a uniqueness proof. A general weak-order theorem not found in the searches, and other unindexed historical equivalents, remain possible.

## Value — PASS
The task of determining which one-pass sortable permutations can be transformed into which others using only local legal swaps is a natural constrained-state reachability problem. The result does more than count a known permutation class: it gives **complete component types**, an optimal shortest-route algorithm, exact component and isolated-state generating functions, and a sharp unique largest-component statement. Its median-graph product geometry provides reusable structure for navigation, optimization and random-walk investigations on the restricted permutation graph. In particular, the feasible swap network has exponentially many vertices but the identity's reachable fraction is exponentially small.

## Closest literature and limitations
[1] Lara Pudwell and Rebecca Smith, *Two-stack-sorting with pop stacks*, arXiv:1801.05005 (2018-01-15), especially the introduction and the stated equivalence of one-pass sortability with \(\operatorname{Av}(231,312)\) and layered compositions. Full-text source: https://faculty.valpo.edu/lpudwell/papers/popstacks.pdf .

[2] Morgan Bauer and Keith Copenhaver, *A new lower bound for deterministic pop-stack-sorting*, arXiv:2307.08188 (2023-07-17); operator definition and sections on iterative sorting, rather than internal adjacency of the one-pass class.

[3] Murray Elder and Yoong Kuan Goh, *\(k\)-Pop Stack Sortable Permutations and \(2\)-Avoidance*, *Electronic Journal of Combinatorics* 28(1), P1.54 (2021). Its accessible description addresses finite pattern bases for iterative pop-stack sortability, not the graph in the claim. The complete text was not relied upon for a no-coverage finding.

No external independent mathematical audit has been performed. The verified computational checks are finite and do not by themselves establish the all-length result.

Self-review: passed. Independent audit: not yet performed.
