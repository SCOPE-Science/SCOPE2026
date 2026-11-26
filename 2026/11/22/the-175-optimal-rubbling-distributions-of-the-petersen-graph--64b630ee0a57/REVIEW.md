# Independent mathematical audit

## correctness

PASS

The first-move recurrence is exact for target-by-target reachability: the starting support accounts for the empty sequence, all neighbor pairs with repetition give precisely the legal moves once multiplicities are checked, and each successor has one fewer pebble. To independently test the computation, I propagated target demands backwards, starting at a single pebble on each given target. A weight-w demand is obtained from a successful weight-(w-1) demand either by padding a pebble anywhere or by replacing one demanded occurrence of the destination by its two input pebbles. This is sound by executing the first move and then the successful suffix, and complete by taking the actual successor of a successful first move. In pebbling mode only equal input vertices are allowed. Exhausting all multisets of weight zero through four found no successful state of weight below four and respectively 10,0,45,30,90 rubbling successes by occupancy type at four. Only the ten stacks work by ordinary pebbling. The 30 double-plus-single successes are exactly the Kneser labels ab,ac,bc with the doubled edge ab; all 210 four-singleton supports agree with the six induced-forest counts and classifications. Ground-label permutations produce 17 orbits, eight successful, and all 17 rows of the frozen CSV match the independent sizes, reachability counts and shape labels. The search is exhaustive at the stated finite weights, not a generalization to other graphs.

## originality

PASS

The equal minimum of four is antecedent, not a new result, and the known stacked construction already supplies ten successes. The supported distinct result is the complete labelled optimizer census and geometry, with exact ordinary-pebbling exclusivity and natural orbits. None of the compared statement-level evidence gives this classification.

## value

PASS

The Petersen graph is a canonical benchmark and both games already share the same minimum. Counting which placements work, not just the minimum resource budget, isolates exactly the change caused by strict moves: 165 previously infeasible distributions become feasible, 90 with every pebble separate. The support-geometry rule makes the exact census useful for comparing placement flexibility and testing move models; it is not merely a restatement of the optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
