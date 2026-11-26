# Independent mathematical audit

## correctness

PASS

A configuration returning after three steps has a harmonic total firing-count vector on the connected graph, so primitive states fire once or twice at each vertex. For a vertex firing once in phase i, write its chip count at firing as degree plus u; its next two counts are u plus the number of same-phase neighbors and degree+u minus the number of predecessor-phase neighbors. The conditions are equivalent to 0<=u<predecessor count. Iterating the predecessor requirement around the shores forces every phase on both. The resulting intervals give independent choices at fixed phases and the baseline mn+sum a_i b_i, since each cross-shore edge contributes one plus its equal-phase indicator. The complement commutes with the map, exchanges once and twice, and is nonnegative for the orbit states by the intervals; the total mass reflects at 4mn-m-n. Each fixed phase profile fills a band through 2mn-m-n. The bottom is mn+m+n-3 by minimizing the excess overlap, attainable with disjoint excess supports. The upper endpoints are onto colorings and the lower endpoints are disjoint-excess colorings: for both shores >3 their support sizes are (1,1), (1,2) or (2,1); a fixed double-support shore of size s contributes s(2^(s-1)-2s) assignments. This gives the stated E. A return after three but not one implies an orbit of length three. Inspected the frozen verification notes, code and captured outputs without executing the uploads. An independent symmetry-reduced census of all box-confined states with label multiplicities, compared coefficientwise via `python3 /workspace/reproductions/frozen_checks.py 3`, agrees for (2,4), (3,3), (3,4), (4,4) and (4,5). The box is exhaustive at these sizes since each periodic nonfixed vertex has a nonfire update and the interval 0 through 2d-1 is forward-invariant for that vertex. The finite census does not prove the general theorem.

## originality

FAIL

Earlier Resultary record 99e5dddcdc6e, primary RESULT.md equations (1)–(3), directly proves the labelled weighted three-phase census, reflection, exact full bands, and endpoint-coloring counts for every connected simple graph. Multiply its polynomial by three to count initial configurations rather than orbits; specialize to K_(m,n) and group colorings by shore populations. This gives exactly the frozen polynomial. Its all-graph support and endpoint rules give the frozen ones by the elementary bipartite overlap minimization and evaluation of the resulting coloring counts. The explicit presentation in the two shore sizes is useful but is covered, not a new census theorem. This verdict rests on the inspected earlier theorem, not on an unavailable publication or the already credited thin-shore result.

## value

FAIL

Mass-resolved periodic dynamics is a worthwhile invariant. In this submission, however, the new presentation groups the existing exact coloring census by the two shore profiles and evaluates the already specified endpoint counts using three disjoint-support cases. It does not isolate a new structural or exact invariant beyond that direct specialization; the simplifications do not provide a substantively useful surviving claim for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
