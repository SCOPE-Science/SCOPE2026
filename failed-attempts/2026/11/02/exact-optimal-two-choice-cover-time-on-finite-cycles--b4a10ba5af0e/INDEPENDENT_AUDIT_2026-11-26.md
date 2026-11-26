# Independent mathematical audit

## correctness

FAIL

The exact expected cover time is correct, and the proof establishes the natural optimal rule of choosing the offered neighbor closest to the unvisited set. The Finding's literal distance-to-an-end-of-the-visited-arc policy is not correct without an explicit unvisited-first exception: with two visited vertices, the other visited vertex is itself an arc end (distance zero), whereas the offered unvisited neighbor is at distance one from the arc. Choosing the other visited vertex when both directions are offered gives mean phase duration 4 rather than 4/3, contradicting the Finding's simultaneous instruction to take the unvisited offer. This is a policy wording failure, not a counterexample to the value formula. To check the value, conditional on any discovery history the visited set is a single interval with the walker at an end, and fresh offers are independent. For k≥2 identify its two absorbing outside directions with the target on C_(k+1); the offered transitions up to that absorption have exactly the same law, with target distance j+1. For k=1 the next step is forced to discover a vertex, independent of the chosen offer. Each policy has a uniformly geometric absorption bound because a run of k identical double-direction offers forces an exit. Bellman verification thus bounds every history-dependent controller and gives equality for the closest-to-unvisited policy, including ties in continuation values. The phase means 2−2·3^(-m) and 2−3^(-m) for k=2m and k=2m+1 sum to the two stated parity formulas. A fresh exact-rational diagnostic checked k=1,...,6 by solving the absorbing linear system with probabilities 3/4 and 1/4 for every left/right policy and comparing all starting states (663 assertions including Bellman checks); n=7 gives 259/27. This is finite corroboration, not proof. The frozen checker.py and VERIFICATION.md were inspected, not executed.

## originality

FAIL

An earlier distinct indexed exact target-hitting theorem in the same model determines every nontrivial cover phase and its optimal policy by a direct state identification. The only remaining operation is to sum its distance-one means. No independently stated earlier exact cycle-cover formula is needed for this implication. The journal source on tori genuinely gives only order bounds; that distinction does not undo the stronger exact indexed overlap.

## value

FAIL

The optimal constant for the canonical cycle case would be a useful exact refinement of a linear growth theorem in isolation. Here the optimal phase value and policy are exact existing results after absorption relabeling. The remaining geometric series is a routine consequence, so neither the constant nor a wording-only policy repair leaves a distinct valuable finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
