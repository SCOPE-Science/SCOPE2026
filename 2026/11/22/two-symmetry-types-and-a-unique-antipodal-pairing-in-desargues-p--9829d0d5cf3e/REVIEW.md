# Independent mathematical audit

## correctness

PASS

I built the 20 labelled vertices from five-label two-subset bitmasks and two layers, joining disjoint masks in opposite layers, and enumerated every 1-, 2-, and 3-element subset (20+190+1140). The empty set cannot mark any vertex. I started with the closed neighborhood and forced one available sole neighbor at a time. This computes the same least fixed point as simultaneous rounds: if more vertices are marked, a pending force either already has its target or that target is still the sole missing neighbor. There are no successes below size 3; exactly 240 triples succeed, and testing all triples shows success iff the original-graph distance signature is (2,3,5) or (3,3,4). The two signatures occur 120 times each. I applied all label permutations and both layer choices to one representative of each, recovering the two entire signature classes under S₅×C₂. I constructed edges by testing each unordered pair of optima: symmetric difference of size two for a jump, with original adjacency of the difference vertices additionally required for a slide. All-source breadth-first searches in both graphs reached all 240 states. Slide degrees are 4, hence 480 edges. Slide shells at distances 1 onward are (4,12,30,57,75,50,11,0) and (4,12,29,56,75,50,12,1), respectively. The sum over roots divided by two gives (480,1440,3540,6780,9000,6000,1380,60); the shell maxima give radius 7 and diameter 8. I checked every type-(3,3,4) configuration's unique distance-eight partner, agreement with the stated four-label perfect-matching/complement transformation, and disjointness from the given triple. In an undirected graph uniqueness in this orbit makes the partner rule a fixed-point-free involution with 60 unordered pairs. On unrestricted jumps the degrees are 17 and 13, the edge count is 1800 and the diameter is 4. Replay: case 4 of review_frozen_repro.py, or the exhaustive loops described here. The two frozen programs were inspected, not executed. This is an exhaustive finite certificate for the prescribed graph/rule, not a result for generalized Petersen graphs as a family.

## originality

PASS

The supported distinct contribution is the optimum-slide metric classification on this host, especially the split eccentricities and explicit disjoint antipodal involution, together with the optimum census used to build it. Earlier power-domination work could cover the scalar minimum, which is not credited here as new by itself. Same-day material on the same graph or the same move rule was substantively compared and concerns different configuration spaces.

## value

PASS

The host is a standard small distance-regular graph, and power-domination token sliding is explicitly posed as a research problem by Bjorkman et al. Preserving genuine local moves is a scientific distinction from a jump graph, not a post hoc cutoff. Here it creates a nonconstant eccentricity on a regular connected graph and a unique, structurally described pairing on only one optimum orbit. An exact slide example with this property and a full comparison against jumps is useful for testing proposed uniform-distance or extremal patterns in optimum reconfiguration. The value does not rest on merely enumerating 1,350 candidate subsets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
