# Independent mathematical audit

## correctness

PASS

In an unfilled graph, the descending link is the discrete set of earlier neighbors, a cone exactly when that set has one vertex. A selected pair (v,u) therefore forces u before v and v before each other neighbor. Conversely a topological order of these requirements realizes every selected pair, and any extras are harmless in the downward closure. In a forest only opposed directions on an edge can form a directed cycle. Any such conflict has a two-incidence witness: distinct choices at the same center conflict along one of its chosen edges; choices at different centers can conflict only along their common edge, either when both choose the other or neither does. Counting separately by center and by original edge yields the conflict graph and its size formula. On C_n the selected even centers comprise a minimum cover, since each selected center covers two edges and all edges are covered. Orienting each selected center from its predecessor to its successor forces the full forward cycle; removing any one selection uncovers an edge and leaves a proper forward subgraph. The resulting minimal nonface has ceil(n/2) vertices. On C_3 no pair survives: two different centers either conflict on their common edge or force the full cycle. On C_4 a pair at adjacent centers is allowed with the same orientation sign (8 pairs), and one at opposite centers with opposite signs (4 pairs). Any triple on distinct centers has a consecutive chain of three, forcing equal signs on that chain if pairwise compatible, contrary to compatibility of its opposite endpoints. So both short cycles are flag with the reported maximal faces. Independently compared 15,752 incidence subsets with downward-closed enumerations of all orders on all nonempty labeled graphs on 2–4 vertices, and explicitly counted short-cycle facets (python3 /workspace/branches/independent-replay.py 4).

## originality

FAIL

The frozen record presents (C), the universal cycle nonface obstruction and short-cycle onset, as an original main addition. An earlier inspected Resultary proof gives an exact all-cycle face criterion on exactly the same strong complex. The claimed witness, its size, minimality, and flag onset are direct consequences of that criterion. This is demonstrated prior coverage of a material headline claim, not merely failure to locate a source. The coverage is cycle-specific; it does not establish prior coverage of the general-graph oracle or the forest conflict graph. The original package is assessed as written; no narrowed repair is submitted.

## value

PASS

The general oracle reduces an enumeration over strict filtrations to explicit precedence constraints and a topological sort, and the forest model supplies a local independence graph and a closed edge count for an unbounded class. Those are useful exact structural tools. By contrast the cycle obstruction and small-cycle flag onset add no distinct scientific value beyond the covering exact cycle criterion; the value pass rests on (A) outside the prior cycle setting and (B), not on counting (C) as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
