---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The contradiction is valid. The official HAP census iterates all SmallGroups of order 64 and lists precisely identifiers 149, 150, 151, 170, 171, 172, 177, 178 and 182 among the nontrivial Bogomolov cases; identifier 199 is absent, hence has trivial multiplier. The same official page states that isoclinic groups have isomorphic Bogomolov multipliers. Therefore identifier 199 cannot be isoclinic to any of the nine, let alone share one family with all of them.

## originality

FAIL

Originality fails decisively. The HAP documentation itself supplies both premises: an exhaustive order-64 list of groups with nontrivial Bogomolov multiplier and the theorem that isoclinic groups have isomorphic Bogomolov multipliers. Since group 199 is absent while the nine listed groups are present, the record's conclusion is an immediate corollary of a published theorem and published census.

## value

FAIL

The result is a cheap consistency check of a malformed family description: one published invariant theorem plus one published exhaustive list settles it immediately. It computes no new family classification, epicenter, capability value or structural invariant. Under the required value bar, correcting the premise is useful operationally but is not a substantive mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
