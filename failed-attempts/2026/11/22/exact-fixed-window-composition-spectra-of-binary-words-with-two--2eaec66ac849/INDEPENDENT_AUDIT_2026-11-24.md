# Independent mathematical audit

## correctness

PASS

The readout is equivalent to (T,U) because its length is known and N_2=U, N_1=T-2U. An incidence interval for a marker at i runs from max(1,i-h+1) to min(i,n-h+1). Its size is c_i=min(i,h,n-i+1) in the claimed range, and U is intersection size. Distinct positions have distinct intervals, so T>2U and U≤h-1. For a positive overlap below full incidence, at least one marker is in an endpoint band; opposite endpoint bands cannot overlap. With the left endpoint chosen, either both markers are at most h and positions are (u,t-u), or only the first is at most h and positions are (t-h,t-u). The branches meet at t=h+u and each yields just one permitted left orientation; reflection gives the second. Two full-incidence markers have distance h-u for u>0; for u=0, count pairs at distance at least h in a central band of n-2h+2 positions. Disjoint markers below full incidence are either on opposite ends (t-1 choices at t≤h, 2h-1-t at h<t<2h), or one is in the central band and the other has incidence t-h (2(n-h-t+2) choices for h<t<2h). This proves the five formulas and positivity exactly on the feasible region, except the single zero (2h,0) at n=3h-2. The full-incidence disjoint case requires n≥3h-1; evaluating the multiplicities gives the stated singleton classes. Its proportion is 1-6(h-1)/n+O_h(n^-2); the square dominates the normalized collision sum with remainder O_h(n^-2), proving the asymptotic. Independently enumerated all literal windows for 154 complete (n,h) cases at h=2..15 and n=3h-2..3h+8, including the one-short boundary, and checked singletons at and after saturation. Replay: python3 /workspace/independent_checks.py 4. The frozen verification script was inspected, not run.

## originality

FAIL

The fixed-layer theorem is mathematically correct but is mechanically implied by the prior two-marker length-limited deck result, which supplies the exact wordwise polynomials and classifies and counts their signatures by the same outer-gap cases. The different observation and different capacities are real; what fails is originality of the evaluated coarsening, not equality of the two channels. The implication below recovers the complete frozen finding, not merely the common saturation threshold or a single table entry. No inaccessible source or same-day priority assumption is needed for this decision.

## value

FAIL

The unordered single-width capacity, singleton fibers, and collision probability are motivated reconstruction statistics, but this frozen contribution is a routine projection and evaluation of a complete prior exact classification. In particular, the collision term only squares the dominant entry obtained from the previously identified two-large-endpoint, separated regime. The analysis does not supply a separate nonmechanical claim beyond the prior exact signature and its elementary consequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
