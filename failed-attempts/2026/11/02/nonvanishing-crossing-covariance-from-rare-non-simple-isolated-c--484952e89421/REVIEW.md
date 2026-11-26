# Independent mathematical audit

## correctness

PASS

For a fixed candidate, isolation is equivalent to internal pairing on both arcs; given it, the arc matchings are independently uniform. The mean crossings on j chords is j(j−1)/6 by counting alternating pairs on four endpoints. With m=n−1 and an arc split (s,m−s), the resulting conditional deficit is −[m+s(m−s)]/3. There are 2n candidates, except n at the antipodal tie, proving the exact mean and covariance (including s=0). For s=1 and n≥4 the factor m+s(m−s)=2n−3 cancels in the covariance. For s≥2, the double-factorial ratio r at s=2 is O(n⁻²); the successive ratio (2s+1)/(2(m−s)−1) is at most 1/2 up to the quarter cutoff and at most one to the midpoint. The first range sums geometrically even with the crossing weight bounded by m(1+s), and the remote range is exponentially small times a polynomial. The tails are O(n⁻²) in mean and O(n⁻¹) in covariance; Markov gives convergence in probability. No s=1 non-tie formula is used at n=3. Frozen verify.py was inspected, not executed. Its exact finite enumeration is corroboration, not proof of the asymptotic.

## originality

FAIL

Already covered, not merely unestablished. Distinct Resultary record 0f60fb4dde2a states the same aggregate non-simple mean and covariance asymptotics and the identical shortest non-simple layer, and its exact termwise arc-split calculation yields every shorter-arc stratum by pairing symmetric terms, including the singleton tied term. No new claim survives the change of indexing.

## value

FAIL

The rare-event correction is mathematically meaningful, but already available in exactly this ensemble. The tabulation by short gap is just a regrouping of its existing summands and adds no useful independent invariant, mechanism or bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
