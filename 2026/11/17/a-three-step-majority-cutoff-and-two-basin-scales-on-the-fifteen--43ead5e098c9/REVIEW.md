# Independent mathematical audit

## correctness

PASS

Independently rebuilt KG(6,2) from all fifteen 2-subsets of six points, with six disjoint-neighbor bit masks and the precise strict-majority threshold four/tie old-bit rule. Exhaustively generated all 2^15=32768 state updates anew and verified F^5(x)=F^3(x) for every x. The witness 63→28704→32→0→0 gives F^4(63)≠F^2(63), proving three steps sharp. Independently computed first periodic-entry populations (t,p)=(0,1):502,(0,2):5340,(1,1):4426,(1,2):3780,(2,1):13680,(3,1):5040. Full orbit-basins exactly (period,size,number)=(1,1,360),(1,10,140),(1,10944,2),(2,2,2460),(2,20,210); 502 fixed and 2670 temporal 2-cycle orbits. Six maximum 5-edge intersecting-star sets characterize Aut(KG(6,2))=S6 (pairwise intersecting >3 edges form a star), and independent adjacent-transposition BFS on all recurrent temporal orbit keys yields exactly eight fixed and eighteen 2-cycle spatial classes with sizes matching the published table. These are complete finite proofs, not sampled states; source code was also read at actual frozen paths.

## originality

PASS

General symmetric threshold-system theory already proves eventual period at most 2, but it does not imply the exact sharp three-step bound, five orbit-basin sizes or 26 S6 classes for this particular map. Other same-graph published records use NOR or three-state excitation, different local transition rules. Bounded originality PASS for exact natural complete census, with unindexed historical enumeration risk.

## value

PASS

KG(6,2) is the first triangle-containing two-set Kneser graph and a natural highly symmetric test object. The exact and sharp three-step relaxation, basin spectrum and 26 complete S6 orbit classes give meaningful dynamics beyond a routine application of eventual period-two theory. The large unanimous basins versus isolated 2-cycles and symmetry splitting are reproducible finite structural invariants a future study of graph majority dynamics can use without repeating the full enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
