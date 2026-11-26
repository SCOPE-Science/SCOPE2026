# Independent mathematical audit

## correctness

PASS

The step h_s=1_(s,1) gives Rh_s=(1−s)/(1−x) below s and 1 above. Integrating again gives the two HR branches of RESULT.md; positivity and constant preservation fix the sign of the defect on either side, so the integrated error is (1−s)Li₂(s)−[s+(1−s)log(1−s)]log s. It vanishes at both endpoints by the elementary limits. Re-differentiation confirms F' and F''. With q=1−s, the dilogarithm reflection identity, Li₂(q)≥q+q²/4 and −log q≥s+s²/2 give F'≥4q−3q²/4−1−π²/6>0 for s≤1/5. For s≥1/5 the same log bound gives F''≤−3−s−log(s)/(1−s)<0 (the positive last term is decreasing and is below 5/2 at 1/5). The derivative at 1 from the left tends to −1−π²/6. Thus F has exactly one maximizing jump point. For a real BV equivalence class the step-measure superposition is exact almost everywhere, and Tonelli applies since the step responses are uniformly bounded and |Df| is finite. Equality in its final scalar bound requires all of |Df| to be supported at that maximizing point, and the converse holds for each such jump. Reflection conjugates HR and RH and sends the point to 1−s. For H alone the jump error is −s log s and has supremum 1/e; F(1/2)>1/e already. Independent diagnostic: bisection on [0.2,0.8] using a 200-term dilogarithm series gave s≈0.5891954149874201, C≈0.4105074987179437, F(1/2)≈0.3974673465533782; the omitted series tail is bounded by s^201/(201²(1−s)). The analytic replay, not these decimals or the supplied checker, establishes global sharpness and equality. The supplied VERIFICATION.md and checker were inspected without execution.

## originality

PASS

The exact composed-operator identity defect and its unique jump locations are distinct from the known mixture, output-variation, same-direction iteration and weighted boundedness results inspected. The underlying step-superposition technique itself is not novel.

## value

PASS

The two natural averaging directions might be expected to balance approximation error; their sequential use instead raises its sharp variation-normalized worst case above the single-pass value. The exact, asymmetric location and the full equality classification describe where this happens, not just that a numerical candidate exceeds a bound. The proof settles a meaningful norm for the simplest opposed composition; it does not claim the higher-iteration problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
