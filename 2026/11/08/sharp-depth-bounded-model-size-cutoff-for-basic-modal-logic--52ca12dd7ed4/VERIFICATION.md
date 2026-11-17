---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Reconstructed recursive complete depth types T_j=C×P(T_{j-1}), truncation surjections, characteristic formulas, universal carrier T_{d-1}, a distinguished node pi_d(t), sections for all nonroot successors and the simultaneous depth-induction. The root realizes any target depth-d type despite cycles. The formula requiring every predecessor characteristic type as distinct successors forces h_{d-1} worlds. k=0, d=1, empty successor sets, and d=0 handled. Repository checker.py independently inspected; finite cases do not establish this infinite theorem.

## originality

PASS

Lück (2019) proves precisely the type-count recurrence and a canonical model containing all rank-d types simultaneously; these are not the sharp per-point h_{d-1}-world construction and lower bound. No matching full statement in searched published results. Distinction is substantive rather than a new name for type counts; historical folklore/corollary remains possible.

## value

PASS

An exact length-independent bound on the worst minimal model size for the natural fixed-depth, fixed-vocabulary fragment determines a sharp exhaustive-model testing cutoff and the necessary reuse of types in cyclic models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
