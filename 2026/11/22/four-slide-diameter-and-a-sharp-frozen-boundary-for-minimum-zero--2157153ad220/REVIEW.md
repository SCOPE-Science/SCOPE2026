# Independent mathematical audit

## correctness

PASS

With four or more whites no blue vertex has exactly one white neighbor. With three, a first force needs a cycle-distance-two pair of whites with a blue midpoint. With two whites their open cycle neighborhoods differ on a blue site: for adjacent whites use an external cycle neighbor; for nonadjacent whites the cycle neighborhoods are unequal and contain neither white. The last white has a blue neighbor. For n≥7 this gives exactly the stated predicate. Counting incidences of distance-two pairs gives n(n−3); n triples of the form {i−2,i,i+2} are counted twice and there are no triple incidences, giving n(n−4). Each slide has a unique retained pair. For cyclic distances 1,2,3,4,≥5 the eligible third-site counts are 2,n−3,4,3,4 for n≥9; the prohibited consecutive third-site pairs contribute n(n−4) from distance two, n from distance three and n from the gap of length five (at n=9 from long gaps of distance-four pairs; at n=10 twice per antipode). Subtracting n(n−2) from the unrestricted count gives the claimed edge formula. For lifting, a capped long gap of length seven retains the first two sites at each end, leaving a segment of length at least three between these neighborhoods. Every arc of length one or two among marked sites and any allowed auxiliary is consequently preserved under expansion, and no long segment becomes short. This suffices for the white-triple predicate and the complement adjacency of every swap. Independently regenerated all 23,659 profiles and all 10,713 eligible pairs and validated each of the provided paths by literal forcing and slide checks, including the auxiliary restriction. This certifies existence of short paths, not a description of all shortest paths. For the disjoint lower-bound witnesses, a three-move path would have to follow one of the 36 monotone insertion/removal schedules; none does at n=7 or n=8, and the marked cyclic distances one and two at the n=8 witness are unchanged thereafter. Separate literal enumeration gave 14 vertices, 18 edges and components 12,1,1 at n=6; (21,42,4) and (32,92,4) at n=7,8, and agreed with the formulas through n=18.

## originality

PASS

The verified distinct content is the constrained slide edge count, exact metric and disconnected boundary. The scalar zero-forcing number, configuration count and associated unrestricted jump geometry are prior results, not credited as original here.

## value

PASS

This asks whether natural locally constrained moves suffice between optimal forcing sets, where unrestricted exchange can hide unreachable configurations or extra moves. It gives a sharp obstruction at six and an order-uniform sharp transition budget above it, with an exact measure of how many jumps the local constraint removes. These are structural facts about the stricter reconfiguration graph, not a recomputation of its known state count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
