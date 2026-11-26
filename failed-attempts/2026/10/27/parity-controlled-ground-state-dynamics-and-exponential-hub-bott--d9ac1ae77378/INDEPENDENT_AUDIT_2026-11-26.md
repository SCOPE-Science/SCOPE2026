# Independent mathematical audit

## correctness

PASS

For degree d and u agreeing open neighbours, the closed-neighbourhood rule flips iff 2u >= d; the change in monochromatic edges is d-2u. Outside the claimed block levels a peripheral update lowers energy by at least 1 (odd s) or 2 (even s), so no such state is recurrent. Balancing each edge-disjoint clique maximizes the cut independently. At odd s all these states are absorbing, including s=1. At even s, for fixed hub spin the moves are the connected inclusion graph on the two middle subset levels of each block; the hub changes only when all blocks have exactly half their peripheral spins opposite it. Reverse moves have the same 1/N probability, and an inactive hub supplies a self-loop. The probability of a strictly decreasing move before entrance is at least 1/N; summing the expected stopped energy decrements gives the claimed uniform entrance estimate. The stationary fraction of exit-enabled states in either hub sector is q^r, with q=(ell+1)/(2ell+1). A start conditioned on that sector remains dominated by twice the stationary law, so the chance of exit in t steps is at most t q^r/N, giving the stated ceil(N/(4 q^r)) lower bound. Independent hand check for s=r=2: 18 recurrent states, conductance 4/45, mixing lower bound 3 and entrance bound 15.

## originality

FAIL

The central equal-blade maximum-cut recurrence, parity class counts and explicit even-s mixing obstruction are covered by a distinct Resultary theorem for arbitrary blade sizes, combined with the classical single-clique theorem for r=1. The extra uniform entrance estimate follows directly from the already established local strict-decrease property by a stopped range-over-drift estimate; it is not a distinct substantive finding for this claim. This is a coverage finding, not a claim that the November catalogue entry preceded the frozen record in time.

## value

PASS

The classification provides a natural exact test case separating rapid entry into the maximum-cut set from exponentially slow equilibration within it. Its explicit bottleneck ties the time scale to a precise collective balance event rather than a fitted finite trend. The finite-size example and the crude entrance bound alone would not supply that value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
