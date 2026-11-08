# Scientific review

## Correctness: PASS

The all-size proof uses the exact bipartite spanning-tree count, a bijection deleting prescribed leaves, the elementary single-edge likelihood tilt, and a four-case conditional edge-probability table. The resulting covariance matrix is explicitly outer-product rank one, with all boundaries \(a,b\ge2\), \(w=0\) and \(w=1\) addressed. Symmetry of the edge-transitive base model proves exact invariance of the entire aggregate leaf-count law, not only its first moments. The four algebraic residuals were zero under symbolic simplification; the standalone independent enumerator passed 520 rational assertions. Finite tests do not establish the infinite parameter statement; that responsibility rests with the proof.

## Originality: PASS (qualified)

Relevant mathematical literature includes Ge--Dong's 2019 nearly-complete-bipartite tree counts, Dong--Ge's 2021 prescribed-forest formula, Rapoport's 2023 general unweighted degree-field probabilities, and Fita Sanmartín--Schnörr--Hamprecht's 2024 weighted ordinary-degree moment formulas. None of these inspected works states the exact four-class conductance-dependent leaf-covariance formula, its rank-one structure, or the unchanged joint distribution of the two total leaf counts. General determinantal/degree machinery can serve as a starting point for recomputation and makes this a qualified rather than categorical historical-novelty assertion. Historical specialization could be unlocated.

## Value: PASS

A single local edge-conductance change produces both signs of cross-part leaf covariance, with a complete analytic checkerboard for every part size, yet preserves the distribution and independence of aggregate leaf counts. This reveals how local dependence can remain invisible to aggregate statistics, and provides an all-parameter exact benchmark for weighted random spanning trees; it is not merely a small numerical improvement or a rephrasing of a tree count.

## Scope and residual risk

The claim is confined to complete bipartite graphs with one conductance-modified edge and cross-part degree-one events. It does not imply labeled degree-vector independence or a conclusion for multiple tilted edges. A specialized formula may exist outside the inspected papers; no independent mathematical or historical-priority audit has taken place.

Self-review: passed. Independent audit: not yet performed.
