# Independent mathematical audit

## correctness

PASS

A shortest path moves monotonically in column and changes rows at most once. Extending to opposite corners shows that the 2n one-switch diameter paths are exactly the maximal geodesics. In one orientation a set is missed iff there is an integer switch strictly between the top maximum and bottom minimum; the reverse orientation gives the other inequality. On nonempty rows, the two failures are disjoint, and each extremal pair leaves independent free positions. In the one-row case exactly the two endpoints are required. This yields the all-set polynomial. There are 3n minimal pairs. In a transversal with no such pair, start with its leftmost vertex and then the first opposite-row vertex at least two columns right. The criterion forces a further vertex in the first row at least two columns beyond that opposite-row vertex. This triple hits all paths and excludes the endpoint pair, and the converse follows from the inequalities. For each doubled row the spaced triples number binom(n-2,3), with n-4 endpoint triples excluded for n>=5; the separate small-n cases give no triples through n=5, and the first actual triples occur at n=6. Independent BFS/path-containment and subset enumeration for n=2 through 8 agreed on all 87,376 subsets, including 85,577 transversals. The independent replay is independent_ladder_replay.py in the branch 598e155a-3e72-4511-967f-3f68cfaef930; the frozen script was not executed.

## originality

FAIL

The distinct indexed record a0aeb4172687 explicitly gives the same labeled classification, minimal polynomial, six-rung transition, maximal paths and exact transversal criterion on the identical Cartesian ladder. It does not print the all-set polynomial, but the exact criterion already supplies it by a direct gap count. This is a finding of mathematical coverage in the inspected catalogue, not a finding of earlier priority, copying or provenance: the comparison record carries a later date than the assignment's source record.

## value

FAIL

The labeled minimal-set classification and its first size-three examples are useful facts, but their full structure is already present in the inspected equivalent record. The remaining displayed all-set formula is a short weighted count from that same record's exact criterion. No distinct nonmechanical extension survives in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
