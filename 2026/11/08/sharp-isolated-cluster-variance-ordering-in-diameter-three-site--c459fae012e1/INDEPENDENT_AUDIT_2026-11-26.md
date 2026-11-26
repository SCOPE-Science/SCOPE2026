# Independent mathematical audit

## correctness

PASS

For fair independent vertex retention, condition on the four equiprobable hub states. The two single-hub states are respectively a binomial count of leaves at the absent hub plus the independent indicator that all leaves at the present hub are absent. This gives the claimed generating polynomial, mean (a+b)/4+A+B and second moment ((a+b)^2+a^2+b^2+2(a+b))/16+(b+1)A+(a+1)B, including a=0. Substitution (A,B,d) -> (2A,B/2,d+2) gives the transfer identity in RESULT.md lines 44–48. After subtracting (d+1)/8, the remainder is at least A(2+3d/4-3A)+3B²/4 when d<=4, and at least A(3+d/2-3A) when d>=4; both are positive by 0<B<=A<=1/8. For any d the excess tends to zero along a→infinity, b=a+d. The central edge of a diameter-three tree permits no other non-leaf vertices; diameter two gives the star. The successive transfers order the full list up to interchange, and its extreme quadratic coefficients are 1/32 and 1/16. A fresh integer mask enumeration checked all 18 unordered pairs for n=4–9 using N=2^n and the variance numerator N sum(z²)−sum(z)² over the masks; this corroborates, rather than proves, the formulas and transfers.

## originality

PASS

The supported distinct result is the all-order strict variance rearrangement for fixed double-star hosts under fair site retention, including the uniform sharp additive transfer threshold and full extremal classification. The elementary conditioning, variance expansion and component terminology are not a separate originality claim.

## value

PASS

The tree class is structurally natural and exhausts diameter at most three. An explicit positive gap gives the direction and magnitude of a shape transfer all the way to the star, including the case of an empty leaf class, and isolates an asymptotic factor of two between the extremes. This is a fluctuation comparison for fixed hosts, not just the routine enumeration of a moment at one parameter point.

The dated certificate retains the supplied scientific assessment, sources and limitations.
