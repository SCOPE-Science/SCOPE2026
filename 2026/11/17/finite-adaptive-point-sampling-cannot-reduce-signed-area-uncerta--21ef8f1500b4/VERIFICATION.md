---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

CDE first two channels equal X, third is F(X)=1/2∫X∧dX. Reflection of an arbitrary open path across the line joining its endpoints, then reversed traversal, creates a closed path of length ≤2B with signed area 2F; the signed isoperimetric inequality therefore gives |F|≤B²/(2π). Against any finite deterministic adaptive querying policy the adversary maintains a positive query-free time gap separating values 0 and q=(2B/π,0), answering left queries 0 and right queries q; reference straight transition fits B. After the finite transcript, two absolutely continuous opposite semicircle traversals of radius B/π fit entirely in the gap, use precisely total length B, return the same answers, and give F=±B²/(2π). Independently integrated the semicircle polynomial/trigonometric area exactly; no bound on instantaneous derivative invalidates short-gap hiding. Upper/lower match for each fixed finite N, with no appeal to asymptotics.

## originality

PASS

Closely relevant primary paper Gusev–Romanenkova–Zaytsev establishes the same output CDE information radius under the STRONGER pointwise L∞ speed bound and obtains decay ∝1/N; it does not entail the no-decay W¹,¹ total-variation result. The result is a sharp change in information-theoretic regularity threshold rather than a restatement of their semicircle upper bound.

## value

PASS

Sharp, easily testable boundary between successful finite sparse observations under bounded speed and complete finite-observation failure under only global path length; this is a mathematically motivated optimal recovery obstruction for a canonical CDE.

The dated certificate retains the supplied scientific assessment, sources and limitations.
