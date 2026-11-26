---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Pezzella's Eq. (3) gives the frozen-start exponential predictor and a two-node correction using the start and prior endpoint per-capita rates with weights 1/2. Subtracting the two component logs gives the stated recurrence. With fixed r≠1 the initial log ratio is asymptotically linear with the opposite sign to log r. At each fixed subsequent sweep, the larger of exp(L) and exp(-L) dominates the O(h) part of the new log ratio, reverses its sign, and is the leading term (times h/2) in the log of the dominant component; the other component's log is O(h). The log of the total differs from the larger log by at most log 2. At sweep zero one predictor exponent has a positive slope, and r=1 leaves both stages at the equilibrium for every h. The (1,2) expressions follow by R0=2exp(-3h/2). Positivity for finite h and exact-flow conservation hold directly. Supporting verify.py was inspected as finite consistency evidence, not run and not used to justify the asymptotics.

## originality

PASS

No covering result was identified in the inspected comparisons. The same-model stability theorem is a derivative criterion at equilibrium; the distinct claim is a fixed-initial-state and fixed-finite-sweep nonlinear stiff limit with explicit tower asymptotics.

## value

PASS

A reversible exchange is a minimal, natural conservative coupled test for a method advertised as positive. The result distinguishes positivity and equilibrium preservation from stiff mass control and shows that no fixed finite number of corrections repairs even this test for any unequal positive start. The alternating tower law measures the failure, rather than merely giving an isolated unstable step or floating-point overflow example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
