# Independent mathematical audit

## correctness

PASS

For a uniform arrival, an actual interval of normalized length l contributes l² to 2W/T. The guaranteed departure bounds every within-period wait, even when adjacent cycle statuses are dependent or some phases coincide. The four outcomes give the stated convex quadratic; the w term makes it strictly convex and averaging c,d is strictly improving unless they agree. After substitution the reduced Hessian has determinant 4Q. Solving the gradient equations produces the stated interior gaps, with a,c,d positive and b=(w(u+v+w)−uv)/(2Q). On b=0 the tangential derivative vanishes at a=(2u+v+w)/H and the inward derivative is 2(uv−w(u+v+w))/H. These certify the unique optimizer, including threshold equality, without searching other faces. For u=v=(1−w)/2, the inequality reduces to (1−w)²≥4w. Independently substituting the rational example gives W/T=29/138 versus 19/80 and reduction 151/1311. Frozen verify.py and VERIFICATION.md were inspected, not executed; the 165 rational tests only supplement the proof. No optimization over label order or positive minimum headways is established.

## originality

PASS

The expectation identity and quadratic-programming method are standard. The closest inspected statements do not give or subsume the exact co-dispatch phase and piecewise optimizer for the prescribed correlated law. This is a bounded coverage judgment, not a claim of publication priority.

## value

PASS

The competing outage patterns make a natural design question: can it be optimal to spend no headway between two departures that still sometimes operate together? The theorem gives a robust positive-probability region, exact boundary, and a unique optimizer on both sides; it shows concretely why strict separation intuitions from independent cancellations need not hold. The value is in that design law, not in the elementary wait identity or the illustrative percentage; there is no real-service calibration or deployment claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
