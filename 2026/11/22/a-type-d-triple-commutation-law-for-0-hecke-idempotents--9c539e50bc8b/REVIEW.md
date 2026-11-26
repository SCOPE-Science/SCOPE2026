# Independent mathematical audit

## correctness

PASS

The primary source identifies all finite 0-Hecke idempotents with unique parabolic supports and gives the nested-or-orthogonal component criterion for commutation. Maximal components in that laminar family are pairwise separated and are exactly the union-components; conversely a union-component covered by one support has its full vertex set in one component of that support. Applying the criterion to all three pairs gives the rooted-state recurrence: for each pair the roots in its union can join only the children's nonzero root components, and the bitwise intersection must retain a common support. The leaf and two-leaf hub start the path and branching families at the claimed sizes. Independent exhaustive rank-four support enumeration gives (pairs,triples)=(164,1390) and (164,1420) for A and D respectively. The reachable state list and the all-coordinate integer certificate were independently reproduced. In a second exact calculation, quotienting by permutations of the three labels gave six orbit representatives (000,022,111,113,132,333), with child-to-parent transition rows (1,3,0,0,3,1); (1,1,2,1,0,0); (1,1,2,0,0,0); (1,1,2,1,0,0); (1,2,0,0,2,0); (1,3,0,0,3,1). The leaf and hub mass rows are (1,3,0,0,3,1) and (64,75,54,15,42,4). The corresponding polynomial annihilates the all-ones column; initial values give exactly the two stated numerators. This certifies the all-rank formal series rather than extrapolating from small ranks. Counts are ordered, allow identity and repeats, and use 0-Hecke multiplication; no universality for disconnected diagrams is inferred. Replay: RESULT.md lines 25–71, frozen VERIFICATION.md and verify_triples.py inspected without execution. Independent replay and output: branches/dcba8987-ff57-4d2b-ad15-e368df4686ec/independent_check.py and independent_check.log.

## originality

PASS

Credit exact equivalent coverage of the entire type-A comparator by the Catalan triple law, not merely matching initial numbers. For a path support J, associate the predecessor projection onto {1} union {i+1: i not in J}, using path vertices 1 through n. The nonfixed run between common fixed points is exactly a union-component of two supports. It lies wholly in one support iff the gap contains at most one of the two exclusive fixed-point colors, the Catalan criterion for commuting. Thus the Catalan law on n+1 points covers the A_n count and even refines it by ranks. No priority order is inferred from the same-day records. The originality pass is for the claimed branching type-D law and its evaluated D-minus-A difference; neither the equivalent path result nor the primary general tuple criterion evaluates the branching transfer.

## value

PASS

The evaluated series locates and quantifies the first branching obstruction in this A/D comparison to extending the known pair-count universality to triples. It gives all ranks and a simple correction to the path count, rather than only a cheap counterexample at rank four. The branch-dependent initial condition despite a shared short recurrence is a useful structural enumeration for finite 0-Hecke diagrams.

The dated certificate retains the supplied scientific assessment, sources and limitations.
