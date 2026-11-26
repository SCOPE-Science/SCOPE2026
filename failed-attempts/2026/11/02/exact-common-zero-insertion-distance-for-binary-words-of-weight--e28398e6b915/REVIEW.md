# Independent mathematical audit

## correctness

PASS

The two end slots of a linear word are one cyclic edge; splitting its padding only changes a common origin. The expanded two-point support is determined up to rotation by the unordered complementary separation lengths. For either possible orientation, cancelling common edges leaves two sums of strictly positive gap lengths. Equal arc sets cost zero, strict inclusion is infeasible, and in the remaining case the initial deficit is a lower bound attained in one edge of the smaller exclusive part. If the supports share exactly one point a, the orientation fixing a is impossible, and the other has cost |r+s−n| for the two distinct clockwise offsets r,s from a. Each of the two exclusive edge sets is nonempty (they contain, respectively, the outgoing and incoming edges at a). Its maximum n−3 occurs exactly at offset pairs {1,2} and {n−2,n−1}. With disjoint supports, grouped or alternating membership gives a feasible orientation using opposite nonempty interpoint gaps of lengths alpha and gamma as the exclusive parts; their difference is at most n−4. This proves the count 4n for n>=4 and the separate zero cases n=2,3. `python3 -B /workspace/review_checks.py 4` independently checked 812 ordered pairs through n=7 by enumerating common padding allocations over all n+1 linear gaps by increasing total and testing literal rotations.

## originality

FAIL

Resultary record 02e33461ac29 dated 2026-10-25 already gives the same instance-wise cost, optimal single-gap construction, sharp maximum, count, and a complete extremizer description for exactly this zero-only common insertion problem. The cyclic-edge expression rewrites its two exact minimizations and its three extremizer cases, rather than extending their mathematical scope.

## value

FAIL

The exact weight-two optimum is a worthwhile response to the broader literature question, but its costs, construction, diameter and extremizer census are already available with proof. The change to cyclic-edge notation does not provide a separate invariant, stronger theorem or new case, so the frozen record adds no distinct scientific result. No genuinely new surviving claim was identified for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
