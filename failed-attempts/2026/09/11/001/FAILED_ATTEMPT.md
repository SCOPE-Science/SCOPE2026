# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** A transcendental Brauer-Manin weak-approximation witness in a D4-symmetric quartic K3 pencil via specialization and quaternion evaluation
- **Round:** 2026-09-07-first-light-01
- **Lane:** 670
- **Disposition:** NO_RESULT
- **Domain:** Arithmetic Geometry
- **Method:** lattice-polarized Torelli specialization with Brauer-Manin Azumaya local-invariant evaluation

## Problem

Let X/Q be the smooth quartic K3 surface x^4+y^4-z^4-w^4+(x^2*y^2-z^2*w^2)=0, which contains the conjugate lines L1:{x-z=y-w=0}, L2:{x-z=y+w=0} and hence carries an explicit genus-1 fibration. Test whether X carries a transcendental 2-torsion Brauer-Manin obstruction to weak approximation by (a) certifying geometric Picard rank 2 via reductions at p=3,5 with logged Frobenius polynomials, and (b) evaluating one explicit quaternion Azumaya representative at two explicit adelic points with opposite local-invariant sums.

## Attempted claim

For the smooth quartic K3 X/Q above, there exist an explicit quaternion Azumaya representative A=(f,g)_2 with f,g in Q(X)^x built from ratios of the linear forms defining L1,L2 (cleaned of ramification along divisors), and explicit adelic points P,Q in X(A_Q) coinciding outside {2,infty} (or another fixed finite bad set), such that the Brauer-Manin local-invariant sums differ: sum_v inv_v(A(P_v))=0 while sum_v inv_v(A(Q_v))=1/2, and A is transcendental (pairs trivially with the certified rank-2 NS lattice), hence X(Q) is not dense in X(A_Q)^{Br} and weak approximation fails via a transcendental class.

## Research outcome

Target (transcendental quaternion weak-approximation witness on X) BLOCKED on both arms: X_3 singular kills the (3,5) specialization route; exhaustive 0/21 monomial residue check kills L1/L2-linears Azumaya candidates. Preset fallback (exact rho=2 via (3,5) certificate) ATTEMPTED_AND_BLOCKED on its literal criterion for the same reason (X_3 singular); replacement-prime upper bound underdetermined from feasible traces. Audited partials preserved: Q-smoothness + good reduction at >=5, X_3 singular locus (12 pts), rho>=2 lattice (det 3), verified counts #X(F5)=80/#X(F25)=1112/#X(F7)=120/#X(F49)=3480, monomial residue no-go.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

['rho<=2 upper bound not established (needs Frobenius moments to r=11, infeasible in-hour)', 'Quaternion no-go covers monomial L1/L2-linears symbols only; non-monomial symbols over pointless conics not exhaustively ruled out', 'No adelic-point or Hilbert-symbol evaluation performed (no unramified symbol found)', 'Fallback exact (3,5) criterion impossible due to X_3 singularity, not due to method failure']

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: ['rho<=2 upper bound not established (needs Frobenius moments to r=11, infeasible in-hour)', 'Quaternion no-go covers monomial L1/L2-linears symbols only; non-monomial symbols over pointless conics not exhaustively ruled out', 'No adelic-point or Hilbert-symbol evaluation performed (no unramified symbol found)', 'Fallback exact (3,5) criterion impossible due to X_3 singularity, not due to method failure']

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
