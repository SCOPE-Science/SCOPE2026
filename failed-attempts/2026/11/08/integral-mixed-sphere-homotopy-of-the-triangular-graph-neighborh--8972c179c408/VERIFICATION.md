---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The 21 common-open-neighborhoods have ten vertices each. Independent face enumeration reproduced 18,494 nonempty faces, f-vector (21,210,1190,3780,5187,4410,2520,945,210,21), and reduced mod-two Betti ranks 246 (dimension 3) and 7 (dimension 4). The assigned verify.py (Git blob 9a7e6d63...) specifies a complete 9,120-pair directed-Hasse acyclicity test on 98,805 incidences, one critical vertex and 246 degree-3 plus seven degree-4 cells; its exact signed integral gradient projection checks all seven four-to-three boundary columns zero. That yields the wedge by Hurewicz since pi3(wedge S3) is Z^246. The same theorem and integral proof are also explicitly provided in the earlier published full-text result. Independent mod-two computation alone would not prove integral homotopy, so the critical integral argument was inspected in the actual code and published proof.

## originality

FAIL

Exactly the claimed mixed-dimensional integral sphere wedge, including its critical-cell counts and zero signed attaching matrix, is already established in the published October 18 full-text T7 result; not only the earlier mod-two Betti vector. This is covered mathematical work rather than a surviving new claim.

## value

FAIL

The complete finite integral homotopy class of a natural triangular-graph neighborhood complex is mathematically meaningful, but prior exact coverage removes independent added value for this final claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
