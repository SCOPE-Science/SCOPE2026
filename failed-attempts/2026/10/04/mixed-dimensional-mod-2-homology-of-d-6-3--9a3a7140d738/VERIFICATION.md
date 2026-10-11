---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

A fresh independent exact replay enumerated all \(2^{15}\) labeled six-vertex graphs, retained exactly 4502 nonempty simplices with face vector \((15,105,455,1185,1647,915,180)\), and computed mod-two boundary ranks \((14,91,364,821,711,180)\). This gives Betti vector \((1,0,0,0,115,24,0)\) and Euler characteristic \(92\). The actual frozen verifier was also read; it independently cross-checks domination membership, downward closure, boundary-square identities and a canonical face digest. The non-equidimensional homology conclusion follows immediately.

## originality

FAIL

A stronger published SCOPE/Resultary record already determines the full homotopy type \(D_{6,3}\simeq\bigvee^{115}S^4\vee\bigvee^{24}S^5\). Its RESULT explicitly records the same face counts and boundary ranks and states that the earlier mod-two homology computation is implied by the wedge decomposition. Therefore the entire final claim is directly covered by a stronger published same-object theorem.

## value

PASS

As a standalone finite computation, the exact Betti profile is a natural answer to the boundary example highlighted by the foundational paper and rules out equidimensional sphere wedges. The scientific value is real, but it is already subsumed by the stronger published homotopy theorem, so originality failure prevents acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
