# Independent mathematical audit

## correctness

PASS

Oddness of F and the charge update give q=-x/2 exactly and one primitive antipodal orbit per positive root of sin(Phi_b(x))=-x/a, with 0<x<=a. The residual is analytic past the compact counting interval and its derivative at zero is pi(1+b)+1/a>0, so the number is finite at every finite a. On a fixed prefix the two phases Phi_b +/- arcsin(x/a) have bounded range and are strictly concave for sufficiently large a, giving O_b(1) crossings. Beyond a fixed L with Phi_b'<0 the minus phase decreases; the plus phase has derivative sign 1-h_a(x), where h_a=-Phi_b'(x)*sqrt(a^2-x^2) has at most one maximum, starts above 1 at L and ends at 0. The terminal rise in the plus phase is at most pi/2, because Phi_b still decreases. Hence each family counts the phase drop -Phi_b(a) divided by 2pi with bounded rounding, turning-point and endpoint corrections. The excluded origin and possible shared endpoint alter the count by at most two. Recomputing the derivative gives J at both antipodes with trace 1-s and determinant -gamma*s, gamma>1 on x>=L, s=a*pi*cos(Phi_b)*[bx^2/4-(1+b)]. On [L,ca], |s| tends uniformly to infinity. For s>0 the characteristic polynomial is negative at both -1 and 1; for s<0 it is positive at 1 with trace >2 and determinant >1, so either both real roots exceed 1 or the conjugate pair has modulus >1. The two-step derivative is J^2. The same crossing count restricted to [L,ca] gives a fraction tending to c^3, and c can approach 1. This checks the fixed-b asymptotics, not finite-gain uniformity in b or other periods. The supplied numerical checker was inspected, not run, and is not needed for the proof.

## originality

PASS

Pass for the combined exact-order antipodal orbit census and density-one repulsion theorem, not the defining recurrence, the generic sine level-counting method or other same-map cubic counts. The strongest same-map comparison counts inverse fibers with a fixed target, while the primary map paper's inspected results address numerical dynamics.

## value

PASS

Reflection selects a canonical periodic-orbit class of the published map. A bounded-error count that resolves both the cubic and linear terms, together with its asymptotically almost entirely repelling character, separates growth of unstable periodic structure from statements about attractors or Lyapunov plots. This is a useful exact dynamical benchmark without claims of global chaos or applications to security.

The dated certificate retains the supplied scientific assessment, sources and limitations.
