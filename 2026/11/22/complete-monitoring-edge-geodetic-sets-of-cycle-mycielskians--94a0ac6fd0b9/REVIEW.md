# Independent mathematical audit

## correctness

PASS

For an apex edge, a geodesic with an internal shadow can reroute its apex-shadow-original segment via the other shadow adjacent to that original. A monitoring pair must therefore contain that shadow. For the shadow edge v_(i+1)u_i, rerouting a two-step segment through w or the middle rim vertex forces endpoint v_(i+1). From there only u_i and u_(i-1) require the tested edge: other shadows can use w, other originals at distance at most two have a route via u_(i+2), and any remaining original has a length-three route via the apex avoiding the tested edge. Reflection forces the other neighbor of each omitted original. Conversely, adjacent shadows have unique common neighbor w, the listed shadow-edge pairs work when the originals form a cover, and a rim edge is monitored by its selected original endpoint and the shadow two steps farther along the rim using the unique two-step path. These checks include n=5. The complements in the originals are cycle independent sets; rooted cyclic gaps give the all-set counts (including k=0 separately) and the 2/3-gap counts for maximal independent sets. This gives the exact size interval; comparing endpoints at n=5..13 and using the change under n→n+6 confirms purity only at 5 and 7. For odd n an optimum has one gap of three: a replacement can only move one of its endpoints by one rim edge, shifting the starting index by ±2, so jumps and slides agree and form a cycle. For even n the disjoint alternating optima differ by more than one replacement. Independent replay: python3 -I -B /workspace/reproduce.py 3 used BFS intersections of edge sets of shortest paths (not edge deletion) at n=5..15, certified forced-shadow pruning and both shadow-edge orientations, and verified the equivalent 698368 subset classifications at n=5..9 with their enumerators and moves. This is bounded corroboration; the uploaded checker was inspected only.

## originality

PASS

The distinct contribution supported by the inspected evidence is the full feasible-set characterization on cycle Mycielskians and its enumerative and reconfiguration consequences, not a claim to priority for the scalar minimum alone. Verified earlier results about cycles, vertex covers under higher girth, and subdivisions do not imply it by specialization. A primary paper studies Mycielskian monitoring numbers; its abstract is accessible but it could not be established from the available material whether it gives the cycle minimum or a stronger characterization. That uncertainty is material and explicitly retained; the abstract is not taken as evidence of noncoverage.

## value

PASS

The reduction turns a shortest-path edge-monitoring constraint on all 2n+1 vertices into a simple cycle cover with forced and optional vertices. It exposes both a nonmonotone purity exception and the precise parity split in optimal relocation, which are not encoded by knowing the minimum size. The value is the natural exact description of all sensor sets on an infinite family, not novelty of the standard independent-set counting formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
