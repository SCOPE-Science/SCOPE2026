# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Heegaard distance at least four over finite high-dilatation magic census
- **Round:** 2026-09-07-first-light-01
- **Lane:** 1644
- **Disposition:** AUDIT_1_REJECT
- **Domain:** hyperbolic Dehn filling, Heegaard splittings
- **Method:** finite slope-box enumeration plus subsurface-projection distance certificates

## Problem

Let N be the magic manifold (complement of the 3-chain link, 3-cusped hyperbolic). Let F be the finite set of closed manifolds obtained by filling all three cusps along slopes p_i/q_i in lowest terms with 0 < |q_i| <= 5 and |p_i| <= 8, excluding the Martelli-Petronio exceptional (non-hyperbolic) list, satisfying minimum normalized slope length L > 6 (the sharp Agol-Lackenby natural boundary), and such that the filled manifold fibers over the circle with closed genus-2 fiber and pseudo-Anosov monodromy of dilatation lambda with 2.30 < lambda <= 2.90, with fiberedness by Thurston-norm face data, dilatation as the Perron root of a carrying train-track transition matrix, hyperbolicity by the L > 6 theorem plus interval-verified structure, and Heegaard distance estimated via Masur-Minsky subsurface projections. Is it true that every M in F is hyperbolic and satisfies Hempel distance d(M) >= 4? A complete answer either proves d(M) >= 4 for every explicitly enumerated M in F with certificates, or exhibits one explicit M in F with slope triple, fibration data, verified dilatation in the high patch, hyperbolicity certificate, and a distance-shorting certificate (weak reduction or subsurface-projection upper bound) giving d(M) <= 3.

## Attempted claim

Let N be the magic manifold (complement of the 3-chain link, 3-cusped hyperbolic). Let F be the finite set of closed manifolds obtained by filling all three cusps along slopes p_i/q_i in lowest terms with 0 < |q_i| <= 5 and |p_i| <= 8, excluding the Martelli-Petronio exceptional (non-hyperbolic) list, satisfying minimum normalized slope length L > 6 (the sharp Agol-Lackenby natural boundary), and such that the filled manifold fibers over the circle with closed genus-2 fiber and pseudo-Anosov monodromy of dilatation lambda with 2.30 < lambda <= 2.90, with fiberedness by Thurston-norm face data, dilatation as the Perron root of a carrying train-track transition matrix, hyperbolicity by the L > 6 theorem plus interval-verified structure, and Heegaard distance estimated via Masur-Minsky subsurface projections. Is it true that every M in F is hyperbolic and satisfies Hempel distance d(M) >= 4? A complete answer either proves d(M) >= 4 for every explicitly enumerated M in F with certificates, or exhibits one explicit M in F with slope triple, fibration data, verified dilatation in the high patch, hyperbolicity certificate, and a distance-shorting certificate (weak reduction or subsurface-projection upper bound) giving d(M) <= 3.

## Research outcome

Proved the finite census F is empty: no L>6 magic-manifold triple filling in the slope box fibers with closed genus-2 fiber (Alexander degrees 6-20, never 4), so d(M)>=4 holds vacuously.

## Why this attempt failed

Failed axes: value.

value: ADMISSION_DEFECT: Result is a vacuous universal over an empty set defined by an arbitrary conjunctive slice (slope box |p|<=8,0<|q|<=5 plus L>6 plus genus-2 plus 2.30<lambda<=2.90). Emptiness is proved at the genus-2 fiber step, so hyperbolicity, dilatation-window, and Heegaard-distance>=4 certificates never materialize; future distance research learns nothing. This is exactly the vacuity/arbitrary-parameter-fact negative resolution STANDARD requires Admission to rule out. No exact invariant of a natural object is delivered, only absence in a contrived box. Intrinsic low value, not repairable by bounded addition.

## Conditions for a legitimate retry

supply independent motivation and a materially stronger contribution; address the recorded limitation: Slope lengths use floating-point maximal-cusp data (rigorous only via recorded 0.10+ margins; no Sage interval certificate available). The deg-Delta=2g fibration theorem is used as standard background. Hyperbolicity/dilatation/Heegaard computations were not performed for any member because the census is empty, making those filters moot.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
