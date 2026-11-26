# Independent mathematical audit

## correctness

PASS

Reconstructed the finite proof and independently reproduced the whole table with python3 /workspace/branches/petersen_reproduction.py (requires NumPy). It filters all 4^10 words by the fifteen edges and the ten distinct-neighbor-color tests; excluding one fixed label checks the three-palette case by symmetry (120 proper and zero dynamic), and the odd cycle excludes smaller palettes. All 5,760 valid states use four names. Recolouring edges were built by grouping on the other nine coordinates, so every edge differs at exactly one coordinate and no move is missed. Direct orbit-set equalities verify completeness of the four profiles. Exact successive neighbor-set layers from a representative of each orbit reached all 5,760 states; orbit-weighting and division by two at positive distances apply because both actions preserve legal moves and every unordered pair has two orientations. Reproduced degrees 9,9,6,6 and eccentricities 15,15,16,16 in the stated profile order, and matched all sixteen histogram entries, summing to 16,585,920 unordered pairs with 20,160 at distance one and 12,960 at distance sixteen. The computation is exhaustive for this named-palette, open-neighborhood, single-vertex graph only. Inspected, but did not execute, the two frozen implementations and their reference outputs.

## originality

PASS

The valid-state populations follow by testing the four already tabulated ordinary-coloring orbit representatives, and the same-day Kneser conflict-free theorem covers the minimum palette at n=5. These facts do not carry novelty credit. The surviving exact result is the metric of the legal induced recolouring graph, including the singleton/eccentricity equivalence. The closest earlier computation is for the full graph and gives different eccentricities and diameters; it does not give an induced distance table. The inspected dynamic and conflict-free sources contain no equivalent metric result. Best-of-knowledge assessment, not a publication-priority guarantee.

## value

PASS

The Petersen graph is a canonical cubic benchmark, and reconfiguring minimum-palette assignments subject to the natural local nonmonochromatic-neighborhood constraint can destroy connectivity or change shortest paths. The exact result says it stays connected but its diameter grows from 14 to 16, and a singleton class characterizes the entire radius-15 center of the constrained graph. That structural criterion, and the exact shell counts when needed for testing constrained recolouring methods, are useful on this graph without claiming a general cubic-graph theorem. Recomputing the published ordinary orbit table alone would not meet this value test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
