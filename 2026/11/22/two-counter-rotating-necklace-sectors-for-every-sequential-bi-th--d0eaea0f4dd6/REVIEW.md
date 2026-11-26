# Independent mathematical audit

## correctness

PASS

The frozen proof's line 83 incorrectly equates the number of labelled orientations to the Eulerian schedule count: at n=4,a=2 there are 6 orientations but 16 schedules. The replacement RESULT.md corrects this distinction, keeps the valid maximum-rank-cut argument, and verifies the count used for the uniform-permutation mean. In the repaired proof the incoming left/right wiring labels are B/A by induction across the earlier endpoint of each edge, and labels are restored at sweep boundaries. Walls can only move in the indicated directions or annihilate in opposite-class pairs. If a mixed pair lasted collision-free for ab sweeps, the lifted relative displacement would change by n(a+b) in increments at most one, forcing a collision. In H_A the rule copies the right bit; visits decrease along each contracted B-block, whose right endpoint copies the unread next block bit across its A-edge and propagates it through the block. The reverse statement holds in H_B. This proves conjugacy on bits, including constants and a=1 or b=1, rather than merely rotation of wall patterns. Fixed-point and primitive-orbit counts follow from the rotation gcd and Möbius inversion. Rank reversal and the Eulerian generating function at 2 give the exact mean and the simple pole at log 2 gives the coefficient and both asymptotics. Independently checked the actual one-step block shift, periodic-state membership, fixed-point counts through d=n, and orientation versus schedule histograms for every schedule and state at n=3..7 (5910 schedules; 695472 pairs). The repair also states the exact scope of the frozen Python verification rather than implying a direct symbol-by-symbol check by that program.

## originality

PASS

For the repaired claim the natural-scan recurrent set and single rotation are credited as an exact known specialization. The Eulerian count is also credited as a permutation statistic appearing for another local rule. The distinct result is the arbitrary-schedule explicit two-sector recurrence and period census for (1,3) on the simple cycle, with its consequent schedule-averaged population. Neither the general orientation/cycle equivalence principles nor the closest other-graph or other-rule classifications provide this surviving statement.

## value

PASS

For a standard local bi-threshold rule, the theorem gives the entire recurrent set and exact periods for arbitrary permutation schedules, going beyond long-cycle examples, general update-order equivalences and the known one-scan classification. The two opposed wall directions explain why the periodic core changes with schedule, and the exact average quantifies its size under uniform permutation sampling. Neither the corrected orientation distinction nor the known Eulerian census is itself the asserted contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
