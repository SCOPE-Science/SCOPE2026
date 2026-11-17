---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Each internal degree-three path vertex sees hub and two distance-two vertices, which must have mutually distinct colours; the hub colour never occurs on the path, and c(v_{i+2})≠c(v_i). Hub demand caps each path-colour frequency at floor(n/2). Two available path colours cannot cover odd n within that cap. On even n the forced period-four binary word gives exactly 12 or 6 named solutions; on odd n the two parity-index paths are independently properly 3-coloured, and coefficient extraction enforces the frequency cap. Direct open-neighbourhood enumeration reproduced n=2:6,3:24,4:12,5:192,6:6,7:912,8:12. Edge case n=2 is K3.

## originality

PASS

Best-of-knowledge exact fan-graph strong-majority vertex invariant and labelled optimal census not covered by strong-odd fan-colouring or generic majority bounds. The forced distance-two path relation and hub frequency constraint combine into a genuine parity law and explicit odd-case generating function.

## value

PASS

Complete natural fan-family classification with parity change and exact named optimum counts, including a nontrivial finite generating-function expression for all odd n; not merely the already known general majority bound or strong-odd graph invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
