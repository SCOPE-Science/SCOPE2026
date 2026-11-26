# Independent mathematical audit

## correctness

PASS

The unique missing colour at each endpoint is the only viable alternative, so matching missing colours characterize the legal moves. I enumerated proper colourings by first-use-ordered classes, expanded over all 24 palettes after verifying that every partition uses four classes, bucketed colourings by deletion of one edge coordinate to form all transitions, and computed components by BFS. The result was 49920 states, 109440 edges, 960 singletons and two components of 24480, with the full frozen degree histogram reproduced. Explicit symbol and palette actions gave one frozen orbit and the asserted sign action on the two mobile components. Replay: python3 branches/independent_petersen.py. This is exact for four named colours and one-edge moves only.

## originality

FAIL

The distinct indexed Petersen local-sign and distance result gives the same census, degree distribution and frozen criterion and implies the claimed group actions, including the full frozen orbit. Thus the assigned scientific content is covered by a stronger result in the examined catalogue. The indexed result has a later date label than the frozen record; this decision is about demonstrable coverage in the current evidence, not a finding about which came first or whether they were developed independently. No independent scientific remainder in the frozen finding was established.

## value

FAIL

The state graph and its two mobile classes are a natural benchmark. However, as a distinct scientific finding this record supplies a component census and actions already covered by the stronger indexed analysis; the independent reproduction verifies them but does not establish an additional boundary, obstruction or invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
