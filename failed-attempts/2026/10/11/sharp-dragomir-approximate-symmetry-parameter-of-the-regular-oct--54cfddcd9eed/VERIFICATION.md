---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The octagon has a=sqrt2-1, vertices (±1,±a),(±a,±1), and dual norm max(|p|+a|q|,a|p|+|q|). By dihedral symmetry only interior edge x=(1,t), |t|<a, and corner x=(1,a) occur. Interior-edge Birkhoff directions y=(0,±1) have d=1/(1+a|t|)≥1/(1+a²). Corner normal cones yield y=(r,-1)/m(r), 0≤r≤1, m=1 for r≤a and (1+r)/sqrt2 for r≥a. Exact quotient distance d=(1+ar)/(m(r)(1+a²))≥1/(1+a²); equality at r=0, r=1. The radical identity 1/(1+a²)=(2+sqrt2)/4 and eps²=(5-2sqrt2)/8 was independently confirmed symbolically. Exhaustive edge/corner proof is analytical.

## originality

FAIL

FAIL: A second already published full result establishes word-for-word the same norm, the same modified Dragomir definition, identical sharp radical and reverse-line inequality, and the same extremizing vertex/axis pair. Its theorem has exactly the same quantifiers. There is no independent original conclusion in the submitted package.

## value

FAIL

FAIL: The exact octagon parameter and extremizer duplicate an already published complete exact theorem without any surviving alternative classification or independently motivated strengthening. Reproving the existing calculation by equivalent vertex quotient duality does not create a new mathematical fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
