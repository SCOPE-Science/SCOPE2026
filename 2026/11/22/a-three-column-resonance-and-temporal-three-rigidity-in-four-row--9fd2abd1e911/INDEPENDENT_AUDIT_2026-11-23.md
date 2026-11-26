# Independent mathematical audit

## correctness

PASS

For triples of four-bit columns (a,b,c), put an edge to (b,c,d) exactly when applying the column rule f three times on the shrinking window (a,b,c,d) returns a at its first site. The overlap forces every indexed closed walk to encode exactly one labelled space word satisfying F^3 x=x, and conversely, also at circumference 3 where input columns wrap. Independent exact reconstruction over 16^4 tuples gave 4096 vertices, 10824 edges and cyclic SCC sizes 1,1,3,3,8,136; the only cyclic components containing any state with f(a,b) different from a are the two simple triangles of alternating columns 5 and 10. Their words are repetitions of (5,5,10) and (5,10,10), up to horizontal phase. The update shifts those words because the center and north inputs are opposite in each cell. Each triangle contributes three indexed starts iff 3 divides n. Every other closed walk is fixed by F, so the six labelled states form exactly two primitive temporal three-orbits when they exist; no spatial quotient was taken. Direct cellwise checks at n=3,4,5 gave fixed/F^3-fixed counts (22,28),(42,42),(266,266), corroborating rather than replacing the all-length SCC argument. Private replay: /workspace/branches/df81a38a-7468-4771-a068-7d26579f1fae/independent_graph.py and independent_graph.log (the logged digest uses comma separators, unlike the frozen colon serialization). The supplied scripts were inspected, not executed.

## originality

PASS

The NEC rule and finite-state periodic-state enumeration are not new. The distinct supported claim is the universal circumference classification at height four: exactly two horizontal translating temporal-three orbits on multiples of three, and none otherwise. The strongest distinct catalogue match has height three and a materially different spectrum; the published statements inspected concern general enumeration machinery, stationary/critical states, or erosion and consensus. Access limitations are recorded separately.

## value

PASS

Temporal three is the first candidate for a three-step return distinct from a fixed state or flip. At this natural strip width the calculation classifies the entire periodic sector uniformly in circumference, not a few sizes, and shows that the richer height-three behavior collapses to two explicitly described waves. The result is useful as an exact obstruction and benchmark for recurrence in anisotropic majority dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
