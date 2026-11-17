---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The exact local majority update is AND of rim neighbours at hub 0 and OR at hub 1; the hub changes on strict rim majority. The symmetric-coupling two-time Lyapunov argument establishes eventual period ≤2, with a self-diagonal <1 to encode tie retention. Constant hub gives exactly the two unanimous fixed states and two exceptional even-rim primitive cycles. For hub zero to flip and return, a rim word must have k>n/2, e=Σ x_i x_(i+2)<n/2, and no isolated occupied vertex under step-two adjacency. The polynomial R_m counts cyclic one-runs ≥2 via m/r binomial run compositions; even n gives two independent step-two cycles and R_(n/2)^2. These identities prove the exact claimed formula for all n≥4; independent direct graph dynamics checks n=4..11 reproduce orbit counts 2,5,11,21,34,66,77,220.

## originality

FAIL

Decisive prior full mathematical results for the identical model supply the identical two-parameter cyclic-run coefficient formula, same hub-flip inequalities, two fixed points, and identical even-rim +2 correction. The submitted polynomial is algebraically the same as earlier G_l/Q_l and does not create an original final claim.

## value

FAIL

An exact dynamical orbit census is mathematically meaningful in itself, but this particular complete wheel majority orbit census was already established for the same parameter range by earlier published proofs. Alternative coefficient notation and restating the even-rim correction do not yield an independently useful new result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
