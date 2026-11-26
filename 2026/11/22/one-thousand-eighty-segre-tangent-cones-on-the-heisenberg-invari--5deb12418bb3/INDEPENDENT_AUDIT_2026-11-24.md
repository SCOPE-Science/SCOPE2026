# Independent mathematical audit

## correctness

PASS

At [1:-1:0:...:0], dehomogenize at x0 and put x1=-1+a, x2=b. The linear parts of f0 and f4 are -3b and 3a; their equations solve for a,b with order at least three, since the other terms not involving a,b are cubics. The remaining f1,f2,f3 divided by 3 start with u3*u6-u4*u7, u4*u8-u5*u6 and u5*u7-u3*u8. They are three independent minors of the stated two-row matrix. The rank-one ideal is prime of dimension four (Segre parametrization), so a larger initial ideal would have dimension at most three, contrary to the dimension-four local ring; completion preserves the associated graded. For uniformity, index the coordinates by the affine plane over F3. The projective Heisenberg stabilizer of the representative is exactly the order-three subgroup of phase characters agreeing at its two support sites: no nonidentity translation fixes a two-element support. Its Heisenberg orbit has 27 points. The normalizer preserves the invariant cubic space, and its Sp(4,F3) quotient acts transitively on the 40 lines of F3^4, giving 40 disjoint 27-point orbits distinguished by their stabilizers. This already exhausts the 1080 singular points of the cited primary classification. The graded dimensions (d+1)*binomial(d+2,2) sum to the claimed Hilbert series and give multiplicity 3; the three independent quadrics make all three formal generators minimal in height 2. On the blowup the projectivized cone is a smooth Cartier exceptional divisor: a local equation is a nonzerodivisor, and a regular quotient by that equation implies the total local ring is regular. The ideal of the divisor restricts to the Segre O(1), giving its normal O(-1,-1). The symbolic support file was inspected, not executed; the local computation was reconstructed directly and the global facts checked against arXiv:2611.16593v1. The geometric facts extend from characteristic-zero algebraically closed base changes of the rational equations. This is about blowing up the reduced points, not the Jacobian scheme or an analytic identification of germs.

## originality

PASS

The supported contribution is the associated graded local algebra on this particular invariant fourfold, with the resulting ordinary point blowup. The fourfold itself, its degree, the singular point census, tangent-space dimension, rank-drop description and abstract Segre algebra are not new. The judgment is based on the inspected comparison, not a certified first-priority claim.

## value

PASS

Determining the full tangent cone at every point of an important explicit fourfold answers a natural local-geometric question left open by a tangent-space dimension and a nonreduced singular scheme. The Segre structure gives both the precise multiplicity and an explicit one-step resolution with known exceptional divisors and normal bundles, useful for later birational calculations without assuming any stronger analytic equivalence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
