# Independent mathematical audit

## correctness

PASS

For J(a,b,c)=(−c,−b,−a), the three fixed triples are forbidden even against themselves. The other 24 form 12 pairs, bounding any period by 12. Selected windows are the edges of a closed trail, so degrees at fixed vertices and crossings of each invariant cut are even. Swapping an edge with its J partner preserves its incidence parity at (00,12,21) and its indicator for the cut {02,10}. Direct endpoint inspection gives all-pair parity 011 and five cut crossings. For 11 edges the unique omitted orbit that can correct 011 is represented by 121, which does not cross the cut. Hence both 12 and 11 are impossible. The displayed word has 10 distinct nonfixed orbits, and their uniqueness forces least period 10. Independent prefix search with exact two-window wrap closure found labeled counts 320, 0 and 0 at lengths 10, 11 and 12; this uses the actual word restriction, not the parity table. Replay: python3 /workspace/branches/independent_replay.py 4; output /workspace/branches/independent_replay.out. The frozen script and console artifact were read, not executed.

## originality

FAIL

The exact maximum is demonstrably covered by Mitchell–Wild arXiv:2602.04433v3, which extends the optimality statement to all odd alphabets at order three. Its February versions only gave 11 as upper bound for the audited instance; v3 is marked 22 October 2026 UTC, later than the frozen directory date. That distinction prevents attribution of the sharper bound to the February versions or a claim of earlier priority for v3, but does not make the current mathematical statements distinct.

## value

FAIL

The sharp value would close a real question relative to the February 10–11 gap; it is no longer an unresolved exact instance in the comparison corpus. The local parity proof is useful exposition but this record asserts no further structural result, independent classification or broader improvement beyond the now-covered maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
