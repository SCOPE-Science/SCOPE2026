---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

FAIL

The conclusion is true, but the frozen universal proof is invalid. Line 37 assumes the oriented gap between two persistently labeled holes increases at every effective b. It instead decreases if b moves the second labeled hole. For n=6, the second rank decrease can output {5,1}, with labeled gap 5 to 1 equal to 2. Rotate five steps to {4,0} and apply b to reach {4,5}. The gap from the original first hole is now 1, and five more rotations reach H_*={3,4}. Here h=1 and E=1, contradicting the claimed E>=n-h-2=3 on an actual reaching word. The upper construction is correct. A separate valid lower-bound argument anchors at n-1 after each effective b and uses h for the other hole. Before the second rank decrease, at least h+1 rotations are needed from the last visit of the singleton hole to n-1. Between consecutive effective b's after that, the rotation cost is at least 1 if the anchor is the moved hole, giving h'=h+1, or n-h if h is moved, giving h'=n-h-1. Either cost is at least h'-h. At the last effective b, adjacency forces h_last=n-2; telescoping gives at least n-1 rotations before that b, and the final shift takes at least n-1 more. Together with the two rank decreases this proves 2n. This validates the conclusion independently but does not justify passing the submitted proof or issuing a repair for a mechanically covered claim.

## originality

FAIL

Ferens–Szykuła's Example 2.4 already states that Černý meets Don's bound for every subset size. The earlier Resultary two-defect result gives explicit witnesses b a^k b a^j with 0<=k,j<n for every size-(n−2) target of the standard Černý automaton. Only the single word with k=j=n−1 can have length 2n, and its holes are {n−3,n−2}. The two prior statements force the claimed unique extremizer without any new lower bound.

## value

FAIL

An extremizing target in this benchmark is a meaningful invariant in principle. Here its identity follows from a unique longest word form in an earlier explicit upper construction combined with already-stated sharpness. The record does not give the full profile or establish a structural result beyond this short consequence. Fixing the lower-bound argument would not recover a distinct valuable claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
