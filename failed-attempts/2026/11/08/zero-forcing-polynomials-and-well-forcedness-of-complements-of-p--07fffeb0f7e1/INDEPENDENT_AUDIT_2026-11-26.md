# Independent mathematical audit

## correctness

PASS

Four whites block every first force. With three whites, a blue center must have its two original neighbors white; it forces the third. A vertex two steps from the center in the original path or cycle then sees exactly one of the remaining whites in the complement. The lone remaining white always has a complement neighbor. Every pair extends to such a triple: use its midpoint at distance two, extend two steps along a shortest path from one endpoint at distance at least three, or extend an adjacent pair past one endpoint to get a distance-two pair, using the side with room on a path. Thus exactly the admissible triples give inclusion-minimal blue sets. Each center counts n−3 triples; two centers coexist exactly when separated by two steps, giving n−4 path pairs or n cycle pairs. Three centers require a triangle in the distance-two pair graph and occur only in C6, with the two alternating triples. Inclusion–exclusion gives both stated coefficients. The independent replay `python3 /workspace/independent_checks.py 2` accepted by branching over legal first moves and matched the enumerators and minimal sets for both families for 5≤n≤10; this is supplementary to the all-order argument. The supplied checker was inspected, not run.

## originality

FAIL

The central claim, the two complete family enumerators, is already covered at statement level by the 2026-10-18 Resultary record, including the exceptional C6 term, and independently corroborated for paths by the 2026-11-02 fort record on a larger parameter range. This is not a title-only match or a failure based on unavailable text. The additional well-forcedness assertion is correct but its historical coverage was not established; neither a distinct narrow claim nor a repair is being passed here.

## value

PASS

The structural result that every successful two-white configuration extends to a successful triple, thereby explaining all inclusion-minimal blue sets, has mathematical use beyond reporting the already covered polynomials. Its three-white witness structure explains when a complement can force and why the six-cycle term appears. This value assessment credits the structural classification, not the recomputation of known enumerators as a new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
