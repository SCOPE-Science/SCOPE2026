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

PASS: The two 4x4 Boolean labeled de Bruijn transition matrices are reconstructed from the exact Rule 22 local rule. Closed walks are equivalent to indexed periodic predecessors, and B0^4=B0^5 stabilizes every zero run, reducing all possible weight-3 cases to 125 capped gap triples. The explicit exhaustive table then proves all large-n families, with rotation-count correction n/3 and small n=5..9 boundary values. Independently evolving binary source words through bounded lengths confirmed the low-weight classification, but the unbounded statement is proved by matrix stabilization.

## originality

PASS

The stable smallest unreachable Hamming layer of cyclic Rule 22 is described by three orientation-sensitive gap families and exact 3n count.

## value

PASS

The first Hamming layer with a one-step Garden-of-Eden target on a periodic ring is a natural sparse-image invariant for a nonlinear elementary cellular automaton. The exact sharp 3n count and oriented gap rigidity for all ring sizes, including exceptional boundary n=9, are useful as concrete reachable-image constraints, not a gratuitous tiny experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
