# Independent mathematical audit

## correctness

PASS

The two radial profiles cross where sin(theta) sin(2u-theta)=0. In the open angular range the crossings select two antipodal arcs of each ellipse; exchange symmetry makes all four arcs congruent. Differentiation gives the stated speed and moving-limit derivative. I checked the numerator factorization exactly with symbolic expansion: for 0<t<1/2 and A>B>0 its factors are strictly positive, and both speeds are positive, giving the strict derivative sign. With W(t) the speed as a function of t=sin²(u), at perpendicularity P''=-2 W'(1/2). Half of this agrees exactly with C in RESULT.md line 29. The smooth integral even about perpendicularity eliminates cubic terms; the one-sided slope at alignment is 2(b-a) and gives a cusp on extending to signed rotations. My bounded reproduction, python /workspace/branches/replay_frozen.py 4, uses eccentric anomaly and the ordinary parametric ellipse speed rather than the source polar-speed quadrature, and also checks the symbolic certificate and coefficient. For (a,b)=(1.2,1),(3,1),(15,0.5) the approximate quadratic coefficients were 0.21161268, 2.44729996 and 1.99002659. The proof, not the samples or reported 629 diagnostics, establishes strictness and uniqueness up to symmetries. Circular, displaced, or unequal copies are not within the strict theorem.

## originality

PASS

Best-knowledge pass for the all-angle perimeter comparison and opposing sharp endpoint laws. The crossing geometry is established context; neither the strongest indexed same-functional shape analogue nor the closest inspected ellipse statements cover the comparison. No historical priority is certified.

## value

PASS

The rotated intersections need not be nested, so the ordering of perimeter is not a consequence of inclusion. The sign certificate and exact positive curvature turn a geometric orientation choice into a quantitative optimizer, providing an explicit comparison for perimeter-sensitive models and for related convex shape families without claiming those generalizations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
