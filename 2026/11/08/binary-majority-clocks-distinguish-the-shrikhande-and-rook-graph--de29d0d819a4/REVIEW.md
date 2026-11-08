# Scientific assessment

## Correctness — PASS

The claim is restricted to two explicitly constructed sixteen-vertex graphs under strict synchronous open-neighbor majority, with tie retention. The exact finite proof enumerates all \(2^{16}\) input states of each graph, constructs the complete successor function and directly classifies the first periodic entrance and least period. No extrapolation from sampled configurations is made. A second standalone algorithm uses coordinate-neighbor lists and signed-opinion sums, independently checking the entire \((\tau,p)\) table. A third algebraic/combinatorial checker verifies regularity, the common-neighbor identity, four-clique populations and four-occupied fixed-state counts. Both graph constructions satisfy \(A^2=4I+2J\), and explicit configurations demonstrate sharp transient maxima. The finite code and outputs have been executed and their common fields compared exactly.

## Originality — PASS, with historical-priority uncertainty

The two graphs' cospectrality and strong regularity are classical, and eventual period at most two follows from Goles–Olivos. The new target is not those properties but the **exact labelled majority temporal census and its spectral separation**. The closest literature inspected concerns general finite-graph period restriction, infinite/unimodular majority, random-graph stabilization and tree stabilization. These results do not determine the exact fixed-state count, primitive two-cycle count or sharp first-entry distribution for either graph. Existing related studies of the same cospectral pair with other dynamics or topological invariants are distinct statements: their transition operators are not binary majority. Searches for the graph names, rule aliases and exact populations did not identify a stronger or equivalent result. This is best-knowledge originality, not a guarantee that no unindexed earlier census exists. The 1980 Goles–Olivos article was not fully inspected; its established general result is explicitly acknowledged, and an equivalent graph-specific table there would alter priority.

## Mathematical value — PASS

These are the unique classical nonisomorphic graphs with strongly regular parameters \((16,6,2,2)\), making them a canonical test of invariance under shared spectrum and local intersection numbers. The measured difference is not limited to a redundant invariant: it separates counts of fixed points, periodic orbit types and sharp transient depths, and gives the complete 131,072-state combined temporal classification. The elementary four-clique argument provides a structural reason for one of the divergences; the other dynamical differences require the nonlinear update. It supplies an exact reproducible benchmark for spectral versus nonlinear-dynamical information rather than an arbitrarily sampled graph.

## Closest literature and limitations

Goles–Olivos (1980) provides the period restriction, Benjamini et al. (arXiv:1405.2486) studies majority convergence on other graph classes, Fountoulakis–Kang–Makai (2020) treats dense random graphs, and Benjamini–Zakharov–Zhukovskii (2026) treats finite trees. Cameron (2025) documents the classical cospectral graph pair. The full historical-priority risk and exact scope are in `AUDIT.json`. The proof is a complete finite exhaustive certificate, not an all-graph theorem or an independent external validation.

Self-review: passed. Independent audit: not yet performed.
