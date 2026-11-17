# Scientific assessment

## Correctness — PASS

The local fixed-point condition is evaluated separately for every one of the three rows and every ordered pair of vertical three-bit columns. Uniform columns admit all east neighbors; the six nonuniform symbols have exactly their own loops and the directed six-cycle \(1\to3\to2\to6\to4\to5\to1\) as nonuniform successors and admit no uniform successors. This establishes the global phase exclusion on every finite cyclic word. The number of nonuniform closed walks is counted by stay/advance choices whose total advance is divisible by six, including all winding multiplicities. The roots-of-unity identity proves the exact spectral formula and leading-order equality. Both independent verification programs were executed and passed, with outputs included. There is no extrapolation from the enumerated circumferences.

## Originality — PASS (historical priority qualified)

The deterministic Toom rule, transfer-graph counting, and general concept of frozen configurations are pre-existing. The specific all-circumference classification for three-row toroidal fixed configurations, its strict uniform/nonuniform column dichotomy, and its exact six-step binomial census were not found in searches of the relevant literature and mathematical records. Makowiec's 1998 full-text article addresses noisy critical regimes and statistics of stationary measures rather than the specified finite deterministic fixed-state set. The very relevant 1997 article was available only as an abstract, describing simulation-based ground-state work; unpublished or inaccessible exact counts remain a residual priority risk. Similar fixed-point formulas for four-neighbor majority on three-row tori and majority on triangular cylindrical graphs concern genuinely different local rules and do not entail the six-cycle result.

## Value — PASS

This is a complete natural fixed-state invariant for the first three-row periodic strip of a canonical asymmetric eroder, rather than a parameter chosen for a numerical curiosity. The exact formula identifies two structurally incompatible families with identical leading entropy: vertically uniform and vertically mixed fixed configurations each have asymptotically \(2^n\) states. The six-state winding mechanism provides a reusable representation for exact sampling and further statistical work on constrained stationary patterns. No theorem about noisy stationary measures or other temporal periods is claimed.

## Closest sources and limitations

Makowiec (1997), DOI 10.1103/PhysRevE.56.5195, abstract only; Makowiec (1998), arXiv:cond-mat/9808247, full text and relevant sections inspected; Barkema et al. (2014), DOI 10.1103/PhysRevE.90.042116, abstract inspected. The asserted novelty is specific to the exact fixed-point subshift, not to Toom dynamics generally. Incomplete historical indexing and the 1997 full-text access limit remain risks. The derivation is purely deterministic and fixed-state only.

Self-review: passed. Independent audit: not yet performed.
