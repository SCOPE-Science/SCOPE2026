# Review of edge-metric bases of the Heawood graph

## Correctness — PASS

The 14 vertices and 21 edges are defined by an explicit modular Fano incidence relation. Edge-distance formulas are derived from shortest-path distances. A complete 14-choose-up-to-5 enumeration rules out all smaller bases and identifies all 168 five-vertex bases; independently the geometry-based verifier constructs 28 point triangles times three eligible tangent-line pairs, plus the dual 84 configurations, and verifies exact equality of the two collections. Complete replacement enumeration proves 420 jump edges, 168 slide edges, the 5-regular connected jump graph of diameter five, and 21 slide components isomorphic to eight-cycles. Independent scripts use shortest-path and direct-incidence methods and pass. A finite certificate here is exhaustive, not a heuristic or a claim about larger graphs.

## Originality — PASS (historical priority qualified)

Kelenc–Tratnik–Yero's archived first preprint (arXiv:1602.00291v1) defines edge metric dimension and derives results for several general graph families; the examined original text does not contain Heawood/Fano incidence-graph bases or their exchange spaces. Bartoli–Kiss–Marcugini–Pambianco (doi:10.26493/1855-3974.2125.7b0) treat vertex-resolving sets in projective incidence graphs; vertex versus edge distinctions prevent their theorems from covering the present configurations. Searches of equivalent terminology and related published mathematical records, including edge metric bases for crown and half graphs, found no stronger overlapping statement. Unindexed earlier calculations or differently named reconfiguration results remain possible. Absence from search is not a proof of novelty.

## Value — PASS

This exactly classifies all optimal edge-sensing landmark sets on the canonical cubic girth-six incidence graph, not just its optimum cardinality. The Fano triangle/tangent construction explains the count of 168. The two natural relocation rules behave sharply differently: unrestricted jumps connect every optimum, while adjacency-constrained slides partition the optima into 21 octagons naturally identified with eight-cycles of the original graph. This supplies a concrete, geometrically interpretable robustness distinction, beyond an isolated small-invariant computation.

## Scope and limitations

The claim is confined to the Heawood graph. Its computer-assisted portions exhaust small, explicitly specified finite sets and are reproducible using the attached Python 3 scripts. Independent scholarly validation and a definitive exhaustive historical-priority review have not occurred.

Self-review: passed. Independent audit: not yet performed.
