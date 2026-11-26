# Independent mathematical audit

## correctness

PASS

For m>1, write the reduced numerator a=mt+c, with c a unit mod m. For next denominator d put g=m/d and t+1=gs; the exact constraint is gcd(s,d)=1. If a is uniform on units mod m^{N+1}, t is uniform mod m^N independently of c. Conditional on d, s is uniform among residues mod m^N/g that are units mod d, so uniform on units mod d^N on reduction. The new numerator P(s)=mg s^2+(c-m)s is a permutation there: P(s)-P(s')=(s-s')[mg(s+s')+c-m], with the bracket a unit at every prime of d. The quotient probability is phi(d)/m, and conditioning on the full past preserves the required numerator uniformity by induction. The singleton modulus and integer absorption at d=1 are immediate. Multiplicativity factors finite path probabilities; consistency defines the process without a uniform measure on all positive integers. At prime p the decrement is min(e,G) with Pr(G>=k)=p^{-k}; summing over sums 0 through e-1 of the first n-1 geometric decrements gives the claimed hitting-time mass (for n=1 it is p^{-e}). The package records VERIFY_OK, but its script was not executed in this review.

## originality

FAIL

The 2012 source does not print a whole-path Markov theorem. Nevertheless its actual Theorem 2.3 proof gives the same single-step congruence bijection at exactly the needed precision. Removing the order filter in that bijection and counting lifts extracts the conditional numerator law and hence the entire displayed result. This is verified proof-level coverage, not a conclusion from a title, an unavailable source, or overlap of the hitting-time marginals alone.

## value

FAIL

The Markov description is useful exposition, but the frozen contribution as a research finding requires no new transition calculation beyond the cited bijection and standard product-kernel algebra. It supplies neither a new independent arithmetic invariant nor another consequence that closes an identified gap; the prime hitting law itself was already available.

The dated certificate retains the supplied scientific assessment, sources and limitations.
