# Independent mathematical audit

## correctness

PASS

Gu–Wang's (1.10)–(1.12) and (3.1c–d) give the stated antiphase recurrence when transport is suppressed and L has eigenvalue λ on (1,−1). The derivative in the unknown successor is 3+2βt+(3t/4)[2A²+(A+B)²]>0 and the cubic is onto. The exact phase-only ODE preserves positivity and its starter is e^(−kt)a₀+O(a₀³), k=β−1>0. The linearized discriminant is 4(1−2kt−4kt²); the three strict Schur inequalities hold on both sides and at the double root. Below or at threshold, (1−kt)(3+2βt)−2(1+t)=1−kt(1+2t)−2(kt)²>0, so the starter slope exceeds the root midpoint. The positive linear sequence is bounded below by a constant times Rⁿ, or (n+1)Rⁿ at the double root. For R<q<R^(1/3), local contraction in an equivalent norm bounds the cubic forcing by O(a₀³q^(3n)); Duhamel with the correct simple or Jordan power bound transfers positivity uniformly in n, not only at each fixed n. Above threshold the update is conjugate to a contracting rotation plus cubic error, so the nonzero trajectory has summable angular errors; local injectivity prevents hitting zero. Irrational rotations, or the evenly spaced rational orbit for 0<θ<π/2, have infinitely many visits bounded away from the boundary of each sign half-plane, unaffected by the vanishing phase error. This proves convergence with infinitely many signs of each kind for all sufficiently small nonzero histories on that side. The two-cell example has λ=2 and β=2, giving τ_c=(√5−1)/8. Scope is phase only, fixed step, near zero, and the positivity branch uses the stated exact starter, not Gu–Wang's unspecified admissible second-order starter. VERIFICATION.md and verify.py were inspected, not executed; the sampled sign patterns are printed diagnostics, not an all-time or machine-certified sign proof.

## originality

PASS

The distinct result is the sharp nonlinear near-equilibrium classification for the actual shifted-force phase recurrence and the stated starter, including the double-root positivity proof and the all-small-history oscillation result above it. Neither the scheme nor the general possibility of a numerical BDF sign reversal is new.

## value

PASS

This is a fully quantified counterexample to inferring sign fidelity from modified-energy stability, in the smallest nontrivial conserved-mean spatial subsystem of a concrete integrator. It gives a usable timestep boundary, including equality, and proves persistent decaying sign reversals even for arbitrarily small, correctly initialized positive data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
