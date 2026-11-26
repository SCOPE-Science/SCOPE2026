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

For distinct full-alphabet strings at distance one or two, a common radius-one output is obtained by keeping one center (distance one) or matching one center at one differing coordinate and the other at the second (distance two). Distance at least three excludes any common output. Independent replay, using embedded inputs checked for exact agreement with CERTIFICATE.json, regenerated all square-free sources with counts (3,6,12,18,30,42,60,78,108), verified that the n=6 and n=7 confusable pairs partition their respective source sets (bounds 21 and 30), and checked nonnegative exact weights on every n=8 and n=9 ball. Each ball received weight one with total budgets 63/2 and 48, so disjointness gives the integral upper bounds 31 and 48. The five n=9 orbits had 48 distinct legal centers and passed all 1,128 pair checks. Thus the integer maximum at nine is 48, with all earlier maxima <32; no exact n=8 value is established. Replay: /workspace/review-evidence/3/independent_audit.py and audit-full.txt in that directory. The frozen checker was inspected and not executed.

## originality

PASS

The Hamming-ball packing formulation, symmetry, and rational upper bounds are established tools. The increment is the explicit optimum and exclusion of all shorter lengths for the full square-free source constraint and arbitrary single substitutions, which do not follow from the closest inspected substitution-detection and cross-bifix results. No broader historical priority is asserted.

## value

PASS

For a natural strong repeat-avoidance constraint, five binary payload bits is a defined code-design target rather than a selected numerical coincidence. The result gives an exact capacity of 48 at the first feasible length, an explicit attaining set, and independently checkable compact dual certificates explaining why length eight cannot carry even 32. It is an exact benchmark for the stated substitution model, not an asymptotic or deployment claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
