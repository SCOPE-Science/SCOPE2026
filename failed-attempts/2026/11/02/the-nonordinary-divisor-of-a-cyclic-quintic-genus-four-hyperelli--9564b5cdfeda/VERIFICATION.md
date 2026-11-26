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

Off 0,1 the branch polynomial has ten simple zeros in the stated characteristics, so the genus is four. Expand (T²−(1+λ)T+λ)^((p−1)/2), T=x^5, and read entries at exponent pi−j in x. At p=3 the four row weights are λ, −(1+λ), −(1+λ), 1. At p=7 they are −3λ²(1+λ), 3λQ, 3Q, −3(1+λ) with Q=λ²+3λ+1; for example the T² and T⁴ coefficients of the cube are 3λ[(1+λ)²+λ] and 3[(1+λ)²+λ]. In both cases the sign of the four-cycle is minus, giving exactly the normalized determinants. The congruence j≡pi mod 5 restricts the support to a single cycle for any stated residue prime. A missing arrow kills every fourth semilinear iterate (also with inverse twists or the dual transpose convention); otherwise the matrix is invertible. Among smooth parameters, exactly two weights vanish at an exceptional root in p=3 or 7, giving rank two and a=2. In characteristic seven Q has discriminant 5, nonsquare in F_7, and no roots at 0,1,−1. Its two simple roots are therefore present over F_{7^r} exactly for even r, distinct from −1. The determinant orders on the smooth base are each two, with no boundary contribution. These checks replay from the displayed quadratic expansion and do not require finite sampling.

## originality

FAIL

The complete characteristic-seven contribution is already present in a stronger October 26 Resultary finding for the dihedral normal form. A geometric change of coordinates, with a unit determinant factor on the marked base, recovers exactly the claimed λ-rank and a-number strata and the doubled divisor. The distinction between marked points and geometric classes does not prevent prior implication. The exact characteristic-three catalogue analogue is later and is not by itself evidence of earlier priority.

## value

FAIL

The marked Cartier divisor would be a natural invariant, but the central characteristic-seven result is a unit-scaled pullback of an earlier exact calculation for the same geometric family. The surviving characteristic-three computation is the immediate coefficient read of F itself, with its exceptional fiber already known; the general dichotomy is the direct single-cycle consequence of the order-five symmetry. No independently motivated, nonroutine remainder warrants repair as a distinct finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
