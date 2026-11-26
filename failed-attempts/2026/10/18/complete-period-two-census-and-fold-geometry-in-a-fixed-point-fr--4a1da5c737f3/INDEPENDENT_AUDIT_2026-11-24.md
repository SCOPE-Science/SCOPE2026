# Independent mathematical audit

## correctness

PASS

A fixed point requires y=0 and bx²+d=0, impossible. On a two-cycle the first coordinates move by +t and −t with t>0, so the points can be written with midpoint m and first coordinates m∓t/2. The difference of the two vertical return residuals is 2t((1+b)m−2), and at m=2/(1+b) each residual is −Q(t). This proves an exact bijection; the sign of the concave quadratic's maximum, strict monotonicity for c≥c₀, and the positive-root formula give the counts and the expansion in c₀−c. The two signed Jacobians have lower rows (h∓w, α∓z), giving the trace and determinant and det(I−DF²)=2(1+b)tQ′(t). It vanishes at the double root and is negative at the larger simple root, so that root has a multiplier >1. The strict Schur conditions characterize linear asymptotic stability, not nonlinear behavior on the unit circle or a nondegenerate normal form at every double root. A fresh symbolic reproduction in /workspace/review-checks/two_cycle.py also obtained the rational example's amplitudes 1/2 and 31/2 and the stated Schur signs; the frozen checker was inspected, not run.

## originality

FAIL

The distinct indexed attraction-band record cc95e26c74ab has a narrower headline theorem but its proof already establishes the all-positive-parameter orbit bijection and general return trace, determinant and Schur test in different variables. The headline census, multiplier classification and escape expansion here are direct consequences of that general kernel. This is a finding of existing mathematical coverage, not a priority determination: the covering record has a later displayed date, and the evidence does not support a claim about who first arrived at the result or derivation between records.

## value

FAIL

The exact classification is intrinsically relevant to the founding numerical bifurcation, but there is no substantial additional finding left after accounting for the indexed general bijection and derivative identities. The remaining Taylor coefficient and a new numerical parameter choice with exact substitution do not by themselves constitute a motivated independent classification or witness. No surviving repair is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
