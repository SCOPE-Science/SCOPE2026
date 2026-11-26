# Independent mathematical audit

## correctness

PASS

On a complete bipartite graph the destination part alternates deterministically. For m vertices in that part and k already visited, the greedy count increases with probability 1-(k/m)^2; any competing conditional increment probability is at most this when its count is k. Couple the two increments with a common uniform given their histories, and sample each full transition conditional on its increment, preserving the law of a history-dependent competitor. At equality the greedy increment dominates; at strict inequality a competing increment of at most one cannot overtake. Domination holds for both counts throughout and proves the stated deadline ordering including one-vertex parts. For the tripartite graph, the part and visited-count tuple are sufficient for the offer-category law, and the successors for each allowed action have exactly the displayed occupancy updates. Uniform properness holds even for history-dependent policies: from each vertex a fixed bounded walk visiting every vertex can be forced by identical offers with a common positive probability. Thus a conditional Bellman inequality can be summed up to bounded stopping times and then passed to completion; it compares the certified greedy policy with every randomized/history-dependent greedy policy. Independent rational policy iteration/evaluation reproduced 608 ordered comparisons, G=18.803347183744457..., D=18.802778086149420..., their exact stated difference 2285849200770243971848/4016620735540189127344279, and the exact positive continuation difference at (0,2,2) in C. The prescribed route to that profile has probability 1/21609 from the B start before the mixed offer. The residual of greedy evaluation under the modified policy is zero elsewhere and strictly favorable on this offer; its positive probability and uniform properness independently explain why D<G. The reproduction checked the greedy restriction and one deviation, not unrestricted optimality or minimal graph order.

## originality

FAIL

Two stronger indexed statements cover the two structural conclusions. The biclique result is stated directly under the same model for every deadline. The multipartite cutoff result identifies the very same graph, B-root-reachable profile, and better seen-first action using unrestricted optimal continuation, which already implies a strict whole-policy penalty on the greedy class from that start. The different exact greedy-continuation and single-switch fractions are verified but not stated by the cutoff result; they are a policy-evaluation refinement of the covered witness, not a distinct structural result. No historical ordering or dependence is inferred from the index paths.

## value

FAIL

The structural contrast and reachable counterexample are mathematically worthwhile, but already covered. The remaining numerical refinement is the gain from one prescribed fixed alteration, smaller than an unrestricted optimal-gap statement in scope. Beyond certifying the already covered contrary action via a particular strategy, no reason is established to need that precise policy-dependent root gain or its threshold. Its small magnitude is not itself the ground for rejection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
