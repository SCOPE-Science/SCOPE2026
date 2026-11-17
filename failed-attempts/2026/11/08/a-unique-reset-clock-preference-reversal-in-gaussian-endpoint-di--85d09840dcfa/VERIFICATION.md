---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The submitted exact g_a has one curvature change; H_x(t)=x[e^{-t/x}-(1-t/x)_+] has strict total-positive ordering across x, so its weighted curvature integral has one positive-to-negative crossover. The independent-rate optimum comparison follows from the renewal-reward weighted-average inequality. Sources RESULT.md and verify.py inspected; finite tests are supplementary.

## originality

FAIL

The November 2 published theorem defines F_b(t)=1/2[(1+b(1-e^{-t}))+(1+b(1-e^{-t}))^{-1}-2], Δ_b(x)=E F_b(xZ)-F_b(x), and proves exactly one crossover with the same strict sign ordering for every b>0. Setting a=b yields g_a=F_b identically and x=2lambda/r. Its Section 3 proves the identical H_x ordered-kernel lemma, and even supplies a stronger sharp singular-width crossover law. The later numerical x_c(1) is also the published x_1≈0.428916361. The ancillary separately optimized periodic-over-Poisson inequality is an elementary known renewal-reward consequence, not a new surviving theorem.

## value

PASS

The matched-mean protocol sign crossover is a motivated thermodynamic diagnostic, but already covered by the stronger published exact result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
