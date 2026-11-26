# Independent mathematical audit

## correctness

PASS

For 0<a<1 write s=√(1−a²/4), h=√(a²−δ²), S=p+q. The only candidate inward from the right leg is its midpoint minus (s/a)(h,δ). The bottom half-plane gives δ≤a²/2 upon squaring nonnegative sides, and the left half-plane gives S≥(2s/a)(a²−2δ²)/h. The top and right inequalities are automatic, and reflection gives the other witness. As a function of u=δ² the latter bound has derivative (2s/a)(u−3a²/2)/(a²−u)^(3/2)<0 on the feasible range, and at δ=a²/2 it equals 2−a². Equality forces p=1 and q=1−a²>0; the opposite long-base vertices then serve as witnesses since the long base and both diagonals have length one. Adding 2a and minimizing for 1/2≤a<1 gives the unique 11/4 case at a=1/2. For 1≤a<2, convex perimeter monotonicity with an included (1,1,a) triangle gives at least a+2; at a=2 the diameter bound gives 4; a>2 is impossible. This proves the continuum claim independently of the packaged checks.

## originality

PASS

The strongest indexed match is the same finding. The closest verified primary theorem concerns consecutive strut sides, not the opposite legs, and does not give this feasibility profile or optimum. No equivalent or stronger coverage was established in the inspected evidence.

## value

PASS

This is a motivated test of what breaks if consecutive strut sides are replaced by opposite ones in a natural symmetric class. The exact feasible widths and the unique sharp family show more than one counterexample: they give the full fixed-leg boundary and identify how the optimal witnesses saturate two supporting lines.

The dated certificate retains the supplied scientific assessment, sources and limitations.
