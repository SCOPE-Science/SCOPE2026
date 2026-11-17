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

PASS: Reconstructed both graph-normalization and exact all-order Ldim proof for K_{n,n} minus a size-t matching. Every positive query fixes one row/column, hence Ldim<=n-1; the four-by-four t=3 tree gives an eight-leaf base, and choices of two allowed edges in one row make both branches contain rank-(n-2) residual classes for n>=5, including a full forbidden diagonal. The VC argument uses partial matching supports and Hall degree/two-matching obstructions, with small-order exceptions handled separately. Independent direct minimax enumeration gave (n,t,Ldim)=(2,0,1),(2,1,0),(3,0,2),(3,1,2),(3,2,1),(3,3,1),(4,0,3),(4,3,3),(4,4,2),(5,5,4). The finite check alone does not prove the universal induction.

## originality

PASS

Best-of-knowledge: the general n>=5 full t=0..n Littlestone phase diagram extends earlier exact derangement n<=5 online cases, prior static matching support formulas, and general online learning bounds; existing sources do not imply the unrestricted online recurrence or matching-deletion induction. The exact one-unit static/adaptive gap at t=n is motivated, not claimed independently novel at n=5.

## value

PASS

A natural adaptive-learning invariant for perfect assignments under forbidden-edge constraints; the all-n deletion phase diagram and the static/online one-unit boundary answer a motivated problem not settled by earlier derangement n<=5 cases or counting formulas. Proof uses substantive induction and exact exceptional classification, not only finite recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
