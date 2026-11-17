# Independent mathematical audit

## correctness

PASS

For h horizontal and v vertical edges of an induced matching, distinct row/column resources imply h+2v≤3t and 2h+v≤3t, hence h+v≤2t. Equality forces h=v=t and all resources saturated; each one-edge replacement is uniquely determined, proving freezing. For two removed horizontals/verticals there are five nontrivial resaturations apiece; for one of each eight, totaling 10*C(t,2)+8t²=13t²−5t. Row-only and column-only mixed swaps implement transpositions across a connected bipartite slot graph, proving connectivity for all t; independent row/column permutations prove transitivity. Independent fresh exhaustive state-graph BFS confirms 9 degree-8 states for t=1 and 8100 degree-42 states for t=2 with distance layers 1,42,705,4904,2448 (diameter 4). Only this finite diameter depends on enumeration.

## originality

PASS

Best of knowledge: the maximum induced matching count is old, but the sharp exchange radius, all-t connectivity and exact 13t²−5t valency are not mathematically implied by inspected packing counts or distinct reconfiguration results.

## value

PASS

Saturated maximum rook matchings form a natural finite reconfiguration space; proving the exact threshold between one-edge immobility and two-edge connectedness, together with all-order degree and transitivity, is a substantive structural theorem, even though the underlying packing count is old.

The dated certificate retains the supplied scientific assessment, sources and limitations.
