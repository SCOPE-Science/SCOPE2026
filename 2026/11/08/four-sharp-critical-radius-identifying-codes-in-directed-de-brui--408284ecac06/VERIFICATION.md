---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For each (q,t)=(3,3),(4,3),(3,4),(4,4), n=2t-1. Every length-(n-1) prefix class can omit at most one word because two omitted final-letter variants have identical positive-radius predecessor signatures; hence |S| >= (q-1)q^(n-1). The modular-checksum code selects exactly q-1 per class. Independent from-source reconstruction exhaustively enumerated all q^n=243,1024,2187,16384 targets, each full closed incoming ball at radii 1..t, and every selected-signature uniqueness/nonemptiness check. Each instance passed and selected sizes were 162,768,1458,12288. This is a complete finite proof for exactly four stated parameters, not evidence for arbitrary q or t.

## originality

PASS

Best-of-knowledge original four nonbinary critical-length exact minima: the established prefix lower bound was not previously known to be attained at these (q,t) pairs. Related 2026 binary t>=3 and nonbinary t=2 results concern different cases and do not imply the four q>=3,t>=3 optima.

## value

PASS

The critical length n=2t-1 is exactly where the established construction loses optimality. The first four nonbinary radius-three/four boundaries close a natural concrete gap and provide sharp sensor costs and explicit code constructions, not an arbitrary collection of numerics; the finite full-signature certificate is appropriate for these finite graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
