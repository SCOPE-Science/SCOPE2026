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

For D=GP(10,2), the valid degree≤1 induced-subset predicate equals exclusion of 60 centered triples. Independent enumeration found 63,143 faces incl empty, f-vector as stated; pivot Morse matching gave 31,566 pairs with critical cells 1 in dimension5, 6 in dimension6, 4 in dimension7. Independent topological sort visited all 63,143 faces across 410,520 oriented Hasse covers. Source `dodecahedral_f1_verifier.py` gives exact integer Morse matrices ∂6=[0,0,-1,0,1,0] and ∂7 as printed in RESULT.md, AB=0 and unit maximal minors (rank1,4), which yield a 6-sphere by integral cell cancellation in the simply-connected CW model. Stage zero independently gave 5,828 faces, 2,912 pairs, 4 critical S5 cells, and null inclusion/cofiber follow from π5(S6)=0. Integer Morse entries inspected in source and agree with complete previously published certificate; independent checker rebuilt face poset/acyclicity but did not independently recompute every gradient-path matrix coefficient.

## originality

FAIL

Exact earlier published integral homotopy theorem identifies the same finite simplicial complex under the alias Ind_2(D), giving F_1(D)≃S^6; the earlier stage-zero theorem gives F_0(D)≃∨^4 S^5. Since π_5(S^6)=0, the inclusion and ∨^5S^6 cofiber are standard corollaries, so no surviving original final mathematical assertion.

## value

FAIL

The computation is reproducible and correct, but the stage-one homotopy is a strict restatement of a published Ind_2(D) theorem and the cofiber follows formally from it plus published Ind(D); no independent unknown exact invariant or structural gap remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
