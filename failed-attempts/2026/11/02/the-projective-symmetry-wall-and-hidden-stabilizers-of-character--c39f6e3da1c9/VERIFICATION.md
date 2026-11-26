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

On the affine chart, x=t^q makes k(t) purely inseparable over k(x,y), while t solves T^(q+2)+T−y with derivative 1, so the parametrization is birational. The unique singular point and its tangent Z=0 force an affine action fixing t=∞ on the normalization. Under t↦αt+β, the coefficient of t² in (αt+β)^(q+2) is β^qα² and is separate from t^q for q≥4; for q=2 those cross terms cancel. Comparison of the remaining coefficients gives precisely the two lists. The differential of the equation is Z^(q+1)δX+XZ^qδZ; coefficient comparison forces the outer rows to be scalar modulo the middle row, giving Lie dimension 3 after the scalar quotient, larger than either reduced dimension. In the stated finite subgroup, invertibility permits the normalization Z′=Z, and Frobenius gives F(M)=d^qF using d^(q(q+1))=1. The conditions are closed, compatible with multiplication and inversion, and the coordinate ring has length q(q+1)·q·q. This is a contained subgroup, not the whole nonreduced stabilizer.

## originality

FAIL

The principal geometric dichotomy and the entire Lie-dimension/non-smoothness claim on the same equations and parameter range are already stated in Resultary --0359b25a3f49, and the q≥4 geometric classification also appears in --02864c85bd52. The proposed finite subgroup and numerical length are not explicitly covered in those passages. They follow by taking the q-Frobenius kernel of the middle-row transformations fixing X and Z and adjoining the already known diagonal group; this does not rescue the frozen classification as a distinct finding.

## value

FAIL

The geometric wall and non-smoothness are worthwhile but already covered. The isolated new detail is the size of a natural, immediately available Frobenius subgroup, not an exact invariant of the whole stabilizer. Its construction is the direct effect of the equation depending on Y only through Y^q; the numerical length gives neither a sharp nilpotence bound nor a full scheme classification, and no further mathematical need for this lower bound is demonstrated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
