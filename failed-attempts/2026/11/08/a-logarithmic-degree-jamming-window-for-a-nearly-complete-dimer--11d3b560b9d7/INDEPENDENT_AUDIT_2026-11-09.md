# Independent mathematical audit

## correctness

PASS

For a clique on N-1 and a hub with d neighbors, every terminal unmatched set has 0 or 2 vertices by parity and clique completeness. First-edge conditioning yields F(k,a) weighted by choose(a,2), a(k-a), choose(k-a,2) over choose(k,2)+a, with F(1,0)=1,F(1,1)=0. Conditional uniform permutation of clique pair eliminations gives the exact hazard product for hub survival. E summed hazard = [d/(N-1)] H_((N-2)/2); finite-population negative covariance yields variance O(d/N), the log vs linear hazard error has bounded expectation O(d/N+(d/N)^2). For finite d log N/N -> c this implies e^-c; the infinity case follows by monotonic hub-neighborhood coupling or uniform bounded-error tightness. Exact independent rational labeled recursion gives p_(8,2)=739/1518 and p_(8,6)=1/21, matching stated recurrence.

## originality

FAIL

A full published research finding establishes precisely the same near-clique hub graph, equal-rate dimer greedy matching process, exact recurrence, and limiting two-vacancy probability e^-c for all degree sequences, with an additional one-missing-edge boundary formula. The submitted theorem is literally its parameter-renamed special case; novelty is absent. Publication date both Nov 8; no within-day priority is asserted.

## value

FAIL

Uniform-edge dimer jamming on an almost complete graph is motivated, but the submitted exact recursion and logarithmic threshold reproduce a prior complete theorem, with no surviving new invariant or extension; scientific value as a distinct research result fails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
