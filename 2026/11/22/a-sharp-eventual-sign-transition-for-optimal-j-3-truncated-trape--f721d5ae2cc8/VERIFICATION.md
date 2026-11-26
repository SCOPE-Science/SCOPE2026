---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Ferrari's symbol and optimized J=3 coefficients reproduce δ_3. Its derivative is (2−sqrt(2))(z−2−sqrt(2)/2) times the strictly positive quadratic z²−(1+sqrt(2))z+1+sqrt(2). This gives a unique real minimum and fixes the positive-real-pole regime. For P_q(Rx)/(1−x), expand the normalized cubic factors (1−tx)(1−2ux+νx²) to get F/c_0²=(1−ν)(1−2tu+t²ν), with ν=R²/|z_+|² and the second factor positive. The coefficients of the expanded symbol give F=−vR²G(R); the five positive Bernstein coefficients of G' and endpoint signs in the supplied interval isolate the only crossing. At the coalescence of the real roots the identity still holds with t=1, and G(R_c)>0 ensures that the positive double root is not dominant. Below q_* the simple positive pole gives a strictly positive leading coefficient. Above q_* there is no positive pole on the convergence circle; applying Pringsheim to either sign of an allegedly one-sided tail proves infinitely many coefficients of each strict sign. At q_* the competing complex poles must be controlled: direct residue comparison reduces A>2|B| to (R+Re z_+)|T−z_+|²>2R(T−R)². The quoted Vieta/rational boxes give a lower bound 15.627192309 against an upper bound 9.41696994, so equality in the modulus comparison still yields eventual strict positivity. Formal coefficient recurrence independently supports the stated lag-four sign defect at q=1. These are eventual sign statements, not all-lag or full-solver stability statements.

## originality

PASS

The symbol, pole methods and related sign theorems are prior. The checked sources do not supply this quartic reciprocal's unique positive-to-complex dominant-pole transition, its strict equality residue decision, or the full eventual sign classification for J=3.

## value

PASS

For an actual optimized convolution quadrature rule, the classification separates strict positivity of the long-lag tail from indefinitely recurring negative weights across all positive relaxation parameters. The behavior at the tied poles does not follow from radius alone, and the explicit negative short-lag witness distinguishes the question from A-stability or all-lag positivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
