---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

A distance-two selected pair obstructs the other diagonal of the square. Conversely, at each geodesic step with at least two remaining flips, the distance-decreasing neighbors are pairwise at distance two and cannot all be selected. Maximality is therefore independent domination in each parity. Closed neighborhoods have size 22, with intersection size 6 or 0 at center distances 4 or 6. Distance-six pairs form a matching, and an all-distance-four triple has the unique common midpoint given by the intersection of the two weight-four supports after translation. Inclusion–exclusion rules out size at most three and gives coverage 64 for a four-set exactly when its six-edges form a perfect matching. Translating one six-edge to 0,b yields the third and fourth vertices c,b+c. Counting gives 224×10/2=1120 per parity and 1,254,400 labeled unions. Independent exhaustive checks for both parities found the same histogram and zero affine identity failures; replay: python3 /workspace/branches/0eff1380-a90f-4137-a7be-b2d0e5aa6000/independent_replay.py 7. The claim is specifically the seven-cube, not general dimension.

## originality

FAIL

An earlier Resultary entry gives the exact named census and the equivalent perfect-matching characterization; its complementary support argument already yields the affine-plane formulation. No distinct remainder survives.

## value

FAIL

A labeled extremal census for the lower visibility problem would be useful if unknown, but the exact family and its size are already available with a proof. Rephrasing its perfect matching in affine language adds no independently useful unknown exact fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
