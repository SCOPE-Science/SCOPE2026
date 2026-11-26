# Independent mathematical audit

## correctness

PASS

Each same-part pair gives one uniform midpoint on the opposite part. The two sets of draws are disjoint, and opposite-part paths cover no nonterminals. Inclusion–exclusion on the fixed nonterminal targets gives the exact product for all a,b, including zero draws. At the window the floor error in the number of draws is O(sqrt(N log N))=o(N); the r-th falling factorial moment on each shore tends to exp(-cr). Independence gives the joint Poisson limit; the zero event is a continuity cell by using half-integer boundaries. Off window the expected miss count is N^(1-lambda^2+o(1)); distinct miss indicators have nonpositive covariance, so Var(U)<=E(U), providing the below-threshold bound, and Markov handles the above-threshold case. A deterministic assignment exists exactly when the available pairs can be assigned injectively to the N-a required midpoints on each shore. The reliable random budget is a first-order comparison, not a claim of probability tending to one at the center of the window. Independently checked the examples 1/9 at (3,2,2) and (37/64)^2 at (4,3,3). VERIFICATION.md lines 19–23 record 47 bounded cases, N=2–4, via verify_random_routes.py; that upload was inspected, not run, and the finite checks do not prove either asymptotic.

## originality

FAIL

No exact prior statement of the randomized biclique theorem was located, but the full random law is a direct reparameterization of two independent ordinary targeted occupancy experiments, and the balanced deterministic threshold is a specialization of the prior capacity criterion. There is no surviving distinct mathematical result in the frozen finding beyond these applications; this is a coverage-by-implication decision, not a claim of a verbatim duplicate.

## value

FAIL

The optimized-versus-random comparison is a clear illustration of coupon collection, but the sqrt(log N) factor just converts known draw budgets N and N log N into balanced counts of pairs. Neither the exact product nor the asymptotic window needs a graph-specific estimate after the single free midpoint is named. No independently valuable nonroutine remainder was established; no repair is offered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
