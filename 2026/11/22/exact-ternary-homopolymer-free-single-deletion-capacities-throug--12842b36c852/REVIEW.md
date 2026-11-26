# Independent mathematical audit

## correctness

PASS

Two deletion positions i<j give the same word iff the entire interval i…j is constant, impossible here. Disjoint shadows are exactly the decoding condition and must include descendants with adjacent repeats. The supplied color-prefix search is sound: independent color classes bound a clique on the remaining prefix, and each feasible extension has a largest processed vertex, so it is visited or excluded by the bound. Independently rebuilt the incidence and conflict masks from the definition, checked all supplied witnesses, and excluded a family of size M_n+1 by exact branching on a group of mutually conflicting words (one member or none); partitioning the remaining candidates into such groups gives a valid upper bound. This proved (1,1,3,4,8,12,22), with 1,837,807 nodes for the length-seven upper bound. For the ordinary packing LP, an independent rational replay checked every primal load and dual cover against the rebuilt incidence and verified equality of objectives (1,3/2,3,9/2,42/5,27/2,99/4). The empty word gives both optima at n=1. Lengths through six give fewer than 16 messages, while the length-seven witness suffices; its additive LP gap is 99/4−22=11/4. No assertion about later lengths or an asymptotic capacity is validated.

## originality

PASS

The exact finite integer and ordinary LP optima concern ternary input words of maximum run length one, with unconstrained deletion outputs and unknown position. Comparison finds the standard hypergraph and LP framework and multiple related exact capacities, but not a verified same-hypothesis theorem or a mechanical implication for these values. Credit is for the resolved finite optima and first 16-message length, not for either optimization formulation.

## value

PASS

The source restriction, unknown-deletion channel and minimum block length for 16 codewords define a concrete finite coding question rather than an arbitrary cutoff. The constructed optimum and exact exclusion of larger codes give an actionable threshold, while the rational LP table shows specifically where the ordinary shadow relaxation ceases to certify the integer sizes. Those exact facts are not supplied by the broader matching model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
