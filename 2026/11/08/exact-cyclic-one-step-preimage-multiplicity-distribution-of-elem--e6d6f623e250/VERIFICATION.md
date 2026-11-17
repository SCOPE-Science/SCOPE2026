---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

Backward maps g0=(0,2,3,3), g1=(2,0,1,1) were constructed from x_{i-1}=y_i XOR(x_i OR x_{i+1}); fixed points of their composition bijectively encode cyclic preimages even for n=1,2. Independently rebuilt the 41-element transformation semigroup and its rank-three cases; no composition supports four fixed points, and the only triple-fiber output is 1^n for 3|n. Independently constructed the 16x16 pair de Bruijn transfer matrix with characteristic polynomial t^11(t-2)(t-1)(t^3-t^2-2), yielding second moment 2^n+1+s_n. The sum, first moment, second moment and triple count solve the four C_{n,j}; directly checked all 8190 output words for n=1..12. Exact finite matrix identity and semigroup closure, not only bounded enumeration, prove all n.

## originality

PASS

The 2 November Rule30 image theorem already determines C_{n,0}, because it counts unreachable outputs using the SAME recurrence; this component is expressly credited. It does NOT determine C_{n,2}, C_{n,3}, the sharp fiber ceiling, nor the complete histogram from C0 alone. The 8 November signed-block collision-language result concerns which outputs have multiple predecessors and explicitly treats full aggregate frequency as known; both were jointly reconciled, so it cannot be used as independent earlier priority evidence. The triple-fiber congruence obstruction and exact multiplicity distribution survive the comparison.

## value

PASS

Complete inverse-fiber size distribution gives exact ambiguity beyond mere image size for a canonical permutive CA on periodic rings. Maximal fiber three, its unique target at 3|n, and frequencies of unique vs doubly invertible outputs answer a natural inverse-dynamics question not mechanically resolved by the already known orphan count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
