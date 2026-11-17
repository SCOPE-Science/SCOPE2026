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

For unordered distinct triples, n<=2 has no queries, n=3 has one nonconstant classifier query. At n>=3 the all-zero vector and n singleton-one vectors collapse to one identically zero concept; at most 2^n-n<2^n distinct functions excludes a mistake tree of depth n. Four-bit queries 123,124,134 realize all eight three-bit response words using mixed assignments. Inductively for each leaf choose existing coordinates of values 0 and 1; query their triple with coordinate n+1, whose majority is exactly the new bit, leaving old labels untouched and all witnesses mixed. Depth increments once per coordinate, proving Ldim=n-1 for n>=4. Reimplemented exact truth-table minimax n<=7 and direct mixed-witness induction; both match. Important: upper bound uses distinct functions, not assignments.

## originality

PASS

After comparing exact statements, hypotheses, data orders and implications, no inspected stronger source subsumes the surviving precise claim; known prerequisite results and any overlapping subclaims are expressly credited. This is best-of-knowledge, not a claim of proof of historical priority.

## value

PASS

Determines exact realizable online dimension of a natural local Boolean observation family in which a latent vector is tested only by majority of three *different* coordinates. The near-complete n-1 adaptive capacity contrasts strongly with restricted local query arity and has a concrete recursive optimal mistake tree, not merely a generic composition inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
