---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The cited method and indexing match JLK Eq. (36) and §6.2. Independently, starting with alpha2=-3/2 and alpha3=1, order conditions for 1,t,t^2 at the new time recover the alpha0, alpha1 and beta coefficients; on the reciprocal phases this gives the stated factorizations of beta. The homogeneous recurrence on first differences is z_{n+1}=z_n/2+alpha0 z_{n-1}. The two-phase product in difference coordinates has trace 1/4+alpha0(r,1/r)+alpha0(1/r,r) and determinant alpha0(r,1/r)*alpha0(1/r,r). I recomputed the exact trace and determinant and all three Schur expressions. Only A-B+C can lose strict positivity, with change at s=r+1/r=(5+sqrt(221))/4. The full monodromy has in addition the constant-mode root 1. At the boundary its three roots are distinct (parasite -1 and other parasite strictly between -1 and 1); beyond it the parasite polynomial evaluated at -1 is negative and has a root below -1. Bounded even powers and one fixed odd step give power boundedness for all steps, in either phase. For decay the leading coefficient is 1+lambda h_n beta, always nonzero for positive lambda h_n exactly when beta>=0. Both beta signs are nonnegative on [1/4,4], including the zero-beta phases at the endpoints. At r=9/2 the short-step phase has beta=-11/96, and lambda h=96/11 is singular with nonzero right-hand side for suitable initial history. This is algebraic solvability, not absolute stability.

## originality

FAIL

The central periodic homogeneous threshold is exactly covered by the earlier Resultary record dd9e864426bf, which has the same homogeneous companion recurrence, reciprocal monodromy boundary, and decisive quartic. Its different BDFL label does not distinguish the equations. That record does not cover the scalar-stage statement; the latter, however, is an immediate sign check on the published adaptive coefficient, and combining it with the known window gives the claimed separation without a new stability result. This is an actual overlap and direct implication, not a failure to establish access to historical references.

## value

FAIL

Distinguishing homogeneous zero-stability from algebraic solvability is useful for interpreting an integrator, and the sharp Floquet classification is substantive in its original source. As a new finding here the homogeneous classification is already available. Removing it leaves a sign-of-beta substitution into the published one-stage coefficient and a representative evaluation inside the known interval. This makes a helpful warning or worked example but not an independently substantive classification or witness beyond the immediate coefficient implication. No valuable, distinct repaired theorem is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
