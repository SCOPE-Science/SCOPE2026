# Independent mathematical audit

## correctness

PASS

The positive radius h+h''=R−8ε cos(3θ) gives a unique analytic oval of width 2R. A zero of the support half-difference f=ε cos(3θ)−z·n must have f'=0 for a convex union, since two distinct singleton support points leave their joining segment uncovered. Analyticity and antipodality force a sign-changing zero; its multiplicity is then at least three. At that zero f''=−8ε cos(3θ), and f=f'=f''=0 yields exactly the three candidate vectors listed. For z=(−3ε,0), f=4ε cos³θ; at the only two switches the support points coincide. All boundary points of the hull are therefore covered, and the common point z (inside the disk of radius R−ε contained in K) gives coverage of the interior along rays. Rotation gives the other cases. The centered support is R+4ε|cos θ|³. At a join, the radius is R+24ε|θ−θ₀|+O(|θ−θ₀|³). Positive radius makes arclength a C¹ change of normal angle; the tangent is C¹ with respect to arclength, but curvature has unequal one-sided derivatives, proving C² and not C³ for the geometric boundary. The support integrals use ∫|cos θ|³=8/3, ∫cos⁶ θ=5π/8, and ∫9cos⁴ θ sin² θ=9π/8 over the full circle, giving the claimed perimeter and both areas. This is analytic throughout; the frozen sampling code was inspected as a diagnostic, not used as proof.

## originality

PASS

The closest known general reflection results supply the lower bound and a criterion, not exactness for this smooth oval. Closely matching records concern the same family's Wigner caustic or orthoptic, not reflection unions. The exact centers and the union formulas survive the targeted comparison; historical priority is not certified.

## value

PASS

This is a sharpness example for a classic three-center lower bound in the restrictive class of analytic, strictly positively curved constant-width bodies. Unlike a cusp count alone it characterizes every reflection union that is convex, and the exact support, area gain and curvature joins give reusable information about those unions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
