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

For A containing cone apex h, a collision between outside u,v can be resolved by a single appended w only if w belongs to {u,v}∪(N_H(u)△N_H(v)), giving ≤2d+2 repairs (prior). Two disjoint once-subdivided d-stars have degree max d for d≥2 and selecting apex plus terminal leaves leaves exactly the two centers colliding, while each 2d+2 unselected center/intermediate removes that collision; singleton complements cannot dominate, yielding an LDC partition into 2d+3 classes. On wheel K1∨C_m, m≥10, selected A includes h and rim outside U={1,2,3,6,7,8}, with 2,7 the sole collision and any U insertion repairs it; no singleton dominates, giving seven classes. Independently checked direct trace predicate on wheel m=10,11,15,30. All m and d follow from the local proof, not finite enumeration; no C_L wheel optimality claimed.

## originality

PASS

PASS for all-base-degree sharp apex-partner construction and explicit seven-class wheel locating-dominating coalition partition. The collision-based 2d+2 upper estimate is direct from the earlier Chellali et al. lemma and NOT credited as novel. Wheel lower bound seven is not an exact optimal wheel coalition number. The new uniform constructions are independently useful structural examples beyond the cycle-six upper bound.

## value

PASS

PASS: The concrete equality constructions show that the known local coalition partner bound can be sharp for EVERY maximum base degree, and a uniform wheel family exceeds the largest possible cycle partition by one block. Both are structurally motivated finite-graph results useful to extremal locating–dominating coalition theory; the known upper estimate is not counted as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
