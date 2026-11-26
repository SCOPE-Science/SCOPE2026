# Independent mathematical audit

## correctness

PASS

The corrected statement specifies the unique cubic seven-cage, i.e. minimum order, rather than unqualified uniqueness among cubic graphs of girth seven. The latter is not true: for example take two copies of the cage, choose an edge outside a fixed 7-cycle in each, and cross-connect their endpoints after deleting the two edges. The new graph is cubic, has more vertices and retains a 7-cycle; a cycle using the new edges must traverse both sides and each side's replacement path has length at least six. This correction does not change the explicitly labelled graph or any enumeration. An independent exhaustive computation constructed the graph, checked degree, girth and base diameter, tested all 0–3 vertex subsets using simultaneous Boolean observation arrays, and compared sparse all-pairs shortest paths for the two exact exchange relations. It reproduced 0, 0, 0, 576 successful placements, wave counts 144, 272, 160, edge counts 6184 and 1328, all distance and eccentricity histograms, and the exact eight named pairs at (1,8) with sixteen distinct endpoints. The bound and matching refer only to minimum placements. The frozen scripts were inspected, not executed.

## originality

PASS

Best of current knowledge: the prior framework and cage are known, but the optimum census and paired-distance result on their specific feasible configurations are supported as distinct. The narrow wording correction makes no novelty claim about cage uniqueness.

## value

PASS

The canonical smallest cubic girth-seven graph gives a reproducible benchmark for minimum-preserving relocation. The joint metric and labelled matching identify exactly which one-step jumps intrinsically force eight slides, information not present in the separate diameters or in a minimum placement count. The repair preserves that finite structural contribution and makes no application or larger-family claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
