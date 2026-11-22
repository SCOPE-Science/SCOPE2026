# Self-review

## Correctness: PASS

The rank-at-least-three equivalence is obtained by fully expanding the one-point-extension recursion three levels. Requiring both orientations from one anchor and four patterns from each corresponding pair is necessary and sufficient. On six vertices the two required full-pattern pairs demand contradictory anchor out-degrees, respectively three and two. The published seven-vertex tournament construction supplies existence; the bit code 17 is another direct witness. Rank four would require eight additional vertices outside a three-element marked set. Exact labelled and orbit census claims follow from the finite exhaustive enumeration in `verify.cpp` and are supported by its checked orbit stabilizers and total weights; `independent_check.py` cross-checks the predicate independently on bounded inputs. Main risk: a bug in either combinatorial encoding or group action. Mitigation: distinct recursion check, total-orbit closure, published unlabelled total of 456, orbit-stabilizer checks. Exhaustive computation is not confused with an infinite theorem.

## Originality: PASS within inspected evidence

The original rank paper already proves a rank-three tournament on seven vertices; this is credited. Its detailed tournament section and appendices inspected here do not enumerate all rank-three tournaments at the first order or show this exact minimum-size argument. McKay's table gives 456 total seven-vertex tournament classes, not the rank-three subclass. The public rank-three simple-graph result studies undirected graphs, and the directed colour-refinement census studies a different invariant; neither mathematically implies the new class-specific count. published-finding corpus semantic searches covering rank, tournaments, enumeration, equivalent variants and the exact counts found no overlapping claim. Incompleteness of indexed historical coverage remains a priority risk; failed searches do not establish global novelty.

## Value: PASS

The all-size rank property of tournaments motivates understanding the smallest finite witnesses of low rank. The sharp first seven-vertex threshold identifies a canonical finite layer, and the complete \(313\)-class symmetry census describes exactly which members of the known \(456\)-class tournament universe attain that rank, with full labelled multiplicities. This is a natural, previously non-implied exact finite classification, rather than an arbitrary sample or an incremental numerical example. No general larger-order theorem is asserted or required for this finite invariant.

The central remaining limitations are historical-priority uncertainty and the absence of independent peer validation. The complete computational evidence and exact scope are in the theorem and verification files.

Self-review: passed. Independent audit: not yet performed.
