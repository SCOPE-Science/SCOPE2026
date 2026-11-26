# Independent mathematical audit

## correctness

PASS

With a,c != 0 and characteristic 17, F(x^4) is squarefree iff the cubic F(t)=at^3+bt+c is separable: all roots are nonzero and the fourth-power map is étale there. A squarefree degree-12 branch polynomial gives genus five; repeated roots decrease the branch degree after square-factor removal. The discriminant is -4ab^3-27a^2c^2, with one zero b for each a,c because cubing permutes F17*. Independent replay /tmp/opencode/check_cyclic_independent.py computed the polynomial gcd with its derivative for all 4352 triples and counted all affine fibers from a direct square-root census plus both possible points in the infinity chart (y/x^6)^2=a there). It confirms 4096 genus-five triples, 32 smooth pointless ones, and normalized pairs (3,5),(5,3),(12,14),(14,12) at c=3. Exact enumeration of all 256 scalings (u,v) gives precisely that 32-element pointless set as the orbit of (5,3,3); this proves one abstract class within the family without asserting diagonal transformations are the only available isomorphisms. The resulting map to the separable cubic quotient has degree four, with the four distinct powers of x->4x acting faithfully; the odd-degree cubic quotient has a rational point at infinity and is elliptic. Both x=0 and infinity are included, and zero RHS is a point.

## originality

PASS

The exact classification of this coefficient family at F17 survives, not the existence of pointless genus-five hyperelliptic curves. Howe–Lauter–Top's Table 1 genus-three example over F17 has an irreducible quadratic factor x^2+13x+1 (remainder zero, discriminant 12 nonsquare mod 17, checked by exact division), so Becker–Glass Theorem 3.2 supplies genus-five existence. Neither gives the exact cyclic-four pullback stratum. The closest indexed genus-five classification statements use different families and fields; no exact table for this F17 family was established.

## value

PASS

This is a complete pointlessness and rigidity calculation in the natural degree-four cyclic pullback of short Weierstrass elliptic curves at a small split field, not an arbitrary list of sparse equations or a first existence claim. For comparisons of arithmetic behavior under cyclic pullbacks the precise marked population and fact that it is one diagonal orbit are useful; a point-count example or general existence theorem does not supply that rigidity. No claim about arbitrary genus-five curves, arbitrary fields or every twist of the geometric curve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
