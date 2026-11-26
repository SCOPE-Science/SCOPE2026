# Independent mathematical audit

## correctness

PASS

Reconstructed the graph on the 27 triples. The seven-vertex closed-neighborhood bound rules out sizes below four. An independent enumeration used combinations, closed-neighborhood unions and union-find on the selected vertices, obtaining zero connected dominating sets through size seven and 11,340 at eight. Independently formed transitions by grouping eight-sets by their seven-vertex intersections; each jump is counted once, and a Hamming-distance-one test on the two extensions distinguishes slides. This gave 73,386 jump and 14,094 slide edges. Unweighted sparse shortest paths over seven disjoint source slices covered every jump source, all reached all states, every eccentricity was nine, and the unordered-pair histogram at distances 1–9 was 73386, 448416, 1964574, 5972616, 12581730, 19397880, 17513334, 6099786, 240408. All slide components were checked, giving (order,diameter,count) = (2,1,162), (9,4,72), (18,9,108), (52,11,162). Directly applying all 6^4 coordinate/symbol maps returned one orbit per component order and state orbit counts 1, 3, 7 at sizes 324, 648, 1296. Inspected both original verifier sources and distinguished their recorded outputs from this fresh full finite reproduction. Replay: /workspace/branches/census.py, census_aggregate.py and census-run/{structure.txt,jump-*-*.txt,jump-aggregated.txt}; pass a scratch output directory to census.py, then run the slices [0,256), [256,2048), [2048,4096), [4096,6144), [6144,8192), [8192,10240), [10240,11340) and aggregate. This proves the finite census, not any larger-family result.

## originality

PASS

The inspected literature and the closest indexed records cover general enumeration, a different move model, or a different graph or invariant. They do not state or give the specific fixed-minimum connected domination and exact jump/slide census here. Approval is bounded by the searches and material inspected.

## value

PASS

A complete metric and orbit classification for the first ternary three-coordinate product is a usable benchmark for optimal connected-backbone reconfiguration. The all-state split between global jump connectivity with every eccentricity nine and 504 small non-isolated slide components is substantive routing information, not determined by the static optimum or ordinarily available from a general reconfiguration algorithm without doing the census. The exact distances and slide orbit data let other implementations test reachability, routing and symmetry reductions on a reproducible fixed graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
