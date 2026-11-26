# Independent mathematical audit

## correctness

PASS

The first integral has gradient (2 X_i^y,-2 X_i^x); the trace-zero linear part has positive determinant 3 beta_i^2+omega_i^2 and the signed quadratic is definite. Two transverse intersections of a section chord have heights y and 2h_i-y. On the entry half-line the intervening ellipse arc stays in the intended half-plane; the other half-line gives an immediate unchanged-height leg. Tangency has the common limiting height. More generally a trace-zero center with nonzero upper-right entry B and additive x-component d has h=-d/B and section velocity B(y-h), giving the same folds with the corresponding entry signs. Composing g1, reset, g2, reset and using |a s1|=1 gives Q(u)=H+sigma abs(abs(u)+t). Nonexpansiveness makes Q(u)-u nonincreasing. Its sigma-tail value is exactly sigma Delta, and the other tail has the opposite unbounded sign; hence a fixed point exists precisely for Delta<=0, including an entire fixed ray at equality. For Delta>0 every orbit is strictly monotone in direction sigma and cannot have a finite limit by continuity, so it reaches the exact translation ray. For capture, distance to a fixed point decreases to a limit, confining the omega set to two candidate points. A bounded orbit's omega set is mapped onto itself (use accumulating predecessors), so f^2 fixes each member z. Choose a parity that accumulates at z. On that subsequence distance to z is nonincreasing and tends to zero; finitely many unit-slope pieces through (z,z) make the distance exactly preserved under f^2 sufficiently near z. Therefore the subsequence hits z after finitely many steps. An invariant probability is supported on cycles by recurrence; on each orbit invariance gives equal weights, or one can push forward to the Borel representative min(y,P(y)) on {P^2(y)=y}. In escape, invariance plus dominated convergence for compact interval indicators rules out a probability. The example is exactly y->2-y on [4/5,6/5], with midpoint fixed. These results classify section iterations, not flight durations, grazing/Zeno realizations or isolated regular limit cycles. The frozen checker was inspected, not run; python3 /workspace/independent_checks.py 5 checks section intersections using an explicit linear-center flow and checks finite normal-form orbit samples independently.

## originality

PASS

The same four-branch return map and the restriction for regular isolated cycles are prior. The distinct supported result is the single critical-affine scalar deciding the exact global return dynamics, with finite capture (not just convergence), the exact tail increment, and the resulting invariant-measure description. No novelty is assigned to the abstract nonexpansive mechanism alone. The access-limited impact and piecewise-isometry papers leave named priority risks.

## value

PASS

Unit reset modulus is a natural boundary where both strict contraction and expansion cease to decide the dynamics. A parameter test for every section initial condition, including skipped legs, separates exact finite-time capture from translation with quantified drift. The two-cycle family demonstrates the need to classify more than fixed points or regular isolated cycles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
