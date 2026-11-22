# Scientific review

## Correctness (PASS)

The Fano-plane graph is generated explicitly, and the two independent standard-library programs exhaust all 3,683 candidate sensor sets of size at most three. They independently confirm 336 optimal triples and generate both complete movement graphs. The 168 isolated states and 28 six-cycles are certified by degree and component traversals, and the three-independent-edge supports with complementary forbidden choices are checked for all six-cycles. Exhaustive breadth-first searches certify connectivity and all 56,280 unordered jump distances. The two programs use different Fano models, closure procedures, state encodings and graph traversals, with identical outputs.

## Originality (PASS, scoped evidence)

The closest primary reconfiguration paper [1] defines the framework and derives other graph-family results, but does not classify the Coxeter graph. The closest 2022 cubic power-domination paper [2] proves general bounds in other conditions and does not derive this fixed-graph minimum census, movement decomposition or distance profile. A direct comparison with published Coxeter perfect-matching work and Heawood path-cover work concerns different feasible-set predicates. Searches for power domination and Coxeter aliases produced no covering theorem or table. Risk: unindexed or inaccessible equivalent finite work remains possible; lack of a matching title alone is not proof of priority.

## Value (PASS)

The Coxeter graph is a canonical 28-vertex cubic distance-transitive graph of girth seven. A complete optimal-monitoring and relocation classification on it is a natural reproducible benchmark, and the observed split between 28 six-state local-mobility islands and 168 frozen optima while arbitrary replacement stays connected demonstrates a structural difference between physical and unrestricted sensor movement. The complementary-corner/matching geometry explains the hexagons rather than merely listing component sizes. No downstream theorem or infinite-family consequence is claimed.

## Limits

This is an exact finite computer-assisted result. Verification programs are part of the proof; no independent external audit or priority certification has been performed. The model is ordinary power domination, not total domination or random sensor survival.

Self-review: passed. Independent audit: not yet performed.
