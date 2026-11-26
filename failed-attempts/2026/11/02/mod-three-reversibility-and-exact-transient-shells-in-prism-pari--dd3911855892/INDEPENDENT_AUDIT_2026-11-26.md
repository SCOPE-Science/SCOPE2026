# Independent mathematical audit

## correctness

PASS

On the two cyclic layers over F2[z,z^-1]/(z^n-1), the three-neighbor update becomes upper triangular with equal diagonal B=z^-1(z^2+z+1) and upper entry 1 after the invertible change (u,v) to (u,u+v). The cubic-root factor divides z^n-1 exactly for 3|n, then with multiplicity e=2^v2(n) by squarefreeness of the odd part. Its two-row primary summand has binary dimension 4e and is nilpotent; the complement is invertible and supplies all periodic configurations. On the primary summand the even powers are B^t I. For odd t, the kernel equations are B^t v=0 and B^(t-1)(Bu+v)=0. With w=Bu+v these become B^(t-1)w=0 and B^(t+1)u=0, so the kernel dimensions are exactly the two truncated valuations in the result, including t=1 and powers where entries vanish. In particular e=1 gives dimensions 0,2,4, while even e gives 4 min(t,e). Multiplying by the count on the complementary primary factors and subtracting cumulative counts proves the shells. On dyadic rims z^n-1=(z+1)^n, the uncoupled adjacency A=z^-1(z+1)^2 has A^(n/2)=0. Here F^(2^j)-I=A^(2^j)I for j>=1, giving saturation at j=s-1 and the stated fixed-space dimensions at smaller powers. For j=0 the same two-row substitution uses diagonal A and gives dim ker A^2=4. Consecutive differences divided by the corresponding primitive periods prove the full dyadic census, including s=2.

## originality

FAIL

Shown covered by distinct earlier Resultary 98fe0217a715, which has the identical labelled prism, neighbor rule and normalization. It states the reversibility criterion, recurrent dimension, transient maximum, cumulative counts at every entry time, and a stronger fixed/primitive-period formula valid for all n and temporal exponents. The present shell counts and dyadic census are direct evaluations of those formulas. The same-day 884f1b68d250 also gives overlapping results under the alias cubic anti-conformist dynamics, but no inferred priority from that date is needed for this decision.

## value

FAIL

Exact reversibility, entry shells and orbit counts of this natural finite system would be useful invariants if not already available. The full population data can already be read from the earlier cumulative and stronger temporal census through arithmetic differences and specializations, and the ungirded-rim contrast is immediate nilpotence of the scalar cyclic adjacency. This package has no genuinely distinct scientific remainder; the more explicit dyadic expressions may have expository use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
