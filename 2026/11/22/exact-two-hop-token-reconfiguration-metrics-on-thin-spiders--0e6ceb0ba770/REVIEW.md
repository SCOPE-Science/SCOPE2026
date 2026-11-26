# Independent mathematical audit

## correctness

PASS

Two different leaves have host distance three, all leaf–clique pairs have distance at most two, and all distinct clique vertices have distance one. A mixed state forbids its own private leaf and any second clique token. These facts give exactly the stated adjacency. Project to the inclusion graph on the two consecutive Boolean ranks k and k−1: each lower-rank vertex is a clique of r−k+1 copies with identical upper-rank neighbors. Different projected endpoints have unchanged distances, by deleting fiber steps on projection and freely lifting inclusion paths with the specified endpoints. Within one mixed fiber the distance is zero or one. In the inclusion graph the Hamming difference gives a lower bound; same-rank paths attain it by replacing each mismatched element with two steps via the other rank (remove then insert in the upper rank; insert then remove in the lower rank). To finish at a lower-rank target T from S in the upper rank, first reach T plus an element of S outside T, then delete that element. These realizations give the three formulas and connectivity. Minimizing intersections for the three pair types gives respective maxima 2 min(k,r−k), 2 min(k−1,r−k)+1, and, for distinct lower labels when k≥2, 2 min(k−1,r−k+1). Comparing these yields the claimed diameter; k=1 is covered by upper pairs and k=r gives the star. Counting upper vertices, the lower fibers and their incident edges gives the stated sizes and degrees.

## originality

PASS

The supported contribution is the structure and exact geodesic metric for the bounded-hop independent-set graph on the clique corona, not the elementary Johnson metric or bounded-hop reachability. The strongest inspected primary comparison gives reachability on a superclass, not distances. The consecutive-rank inclusion and fiber description is an exact alternate presentation; no accessible theorem identifying this structure for the bounded-hop family or directly covering its full metric was verified.

## value

PASS

A clique with private leaves is a canonical split-graph family separating leaf exchanges, clique moves and mixed states. Its exact two-hop geodesic metric, even at maximum occupancy, gives more than a reachability algorithm and furnishes a concrete benchmark for the shortest variant. The transition to a two-rank incidence graph explains the whole distance and diameter profile; the value is this model-specific identification and complete invariant, not the standard subset distance by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
