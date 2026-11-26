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

For each fixed center the candidate averaging rows are all different. Outside the resulting finite set of tie hyperplanes the maximizing rows form a strict branch. A segment with positive generic endpoints has only finitely many switches; summing the variation bounds on its linear pieces, then using continuity to approximate arbitrary nonnegative endpoints, bounds the global two-input quotient by the maximum strict-branch norm. Conversely a small perturbation of a strictly feasible, positively translated baseline realizes its branch on both inputs. The linear branch preserves constants; integration of binary upper-level cuts gives exact cyclic coarea for the input and a triangle-inequality bound for the output. Its norm is therefore the maximum over all proper nonempty cuts, including disconnected ones. Independent exact enumeration gives the unrestricted envelopes 1, 5/4, 7/5, 2 and exactly three C₆ masks above 19/10. In each exceptional mask the two full rows are opposite; their competing radius-one triples partition the cycle, so the full average is the mean of the two triple averages and cannot strictly exceed both. Thus the only excessive masks are not strict branches. The four displayed baseline and cut perturbation pairs were checked to retain their unique branches and attain the claimed constants; for C₆ their variation pair is 1/50 and 19/500.

## originality

PASS

The supported distinct claim is the exact, attained two-input variation modulus for the centered operator, including the strict-branch obstruction at six vertices. The inspected centered one-input variation and graph Lᵖ results compute different invariants. The reported same-value uncentered C₆ result was not independently located; its possible additional centered coverage remains a named risk.

## value

PASS

The sizes are a meaningful cutoff rather than an arbitrary sample: the unrestricted row envelope is sharp for the first three cycles and first fails at C₆, where opposed full-cycle choices create a new feasibility constraint. The exact modulus quantifies sensitivity to differences between two signals, a question not answered by one-input variation bounds. The cut reduction and analytic obstruction explain why exhaustive small-instance values are sharp and why the naive bound first overestimates them.

The dated certificate retains the supplied scientific assessment, sources and limitations.
