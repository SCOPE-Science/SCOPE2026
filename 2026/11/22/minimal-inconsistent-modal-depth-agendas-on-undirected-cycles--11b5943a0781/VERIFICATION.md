---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Quantification is over Boolean valuations of one letter at one root of a loopless undirected cycle, with depths 1 through n-1 indexed syntactically. The endpoint support B_j consists of j-2t modulo n for 0 <= t <= j. For any positive set, the valuation equal to its support union satisfies every negative whose support is not contained in that union. Consequently a minimal obstruction has exactly one negative, with pairs exactly the single-support containments; two positives of the same parity would make the smaller redundant. In even order the two parity chains lie on disjoint shores. In odd order n=2r+1 supports have size j+1 up to n-1; at e+o=n-2 for opposite-parity depths they are disjoint (opposite-parity integer endpoints could coincide modulo n only if separated by at least n) and partition the cycle. Nested enlargement gives the same cover above the threshold. Below it, a negative depth exceeding the same-parity positive by at least two has a new endpoint e+2 or o+2 absent from both supports, by distinct same-parity endpoints and the parity-specific walk bound. Once the union covers, the larger negative exceeds its same-parity support and its 0 (even) or 1 (odd) is absent from the opposite support (a full n-1 positive is excluded). This proves both directions. For e=2a, o=2b+1 the condition is a+b >= r-1, with a in 1..r-1 and b in 0..r-1. Each contributes r-a+r-1-b negatives; summing over b first gives (a+1)(2r-a)/2, then r(r-1)(2r+5)/6. At r=1 no a is available. With all depths at most r, the only candidate opposite-parity positives satisfying the threshold are r-1,r and neither can be exceeded by two. For r>=2 the depths r-1,r,r+1 do give a minimal triple. The proof is unrestricted in n; frozen finite checks cover only the documented ranges.

## originality

PASS

The semantic covering test is prior and the numerical cubic also occurs previously as the triple coefficient for an unrelated shifted cycle problem. Credit is for the complete classification of signed-box depth triples on the symmetric irreflexive cycle, including their interpretation and sharp least depth, not for inventing the covering technique or a previously unseen integer sequence. No scope-preserving reduction from the inspected results establishes that classification.

## value

PASS

Minimal inconsistency is a motivated obstruction in genuinely modal agendas. Here the classification decides all witnesses on an infinite standard family and reveals exactly how odd-cycle overlap creates a failure of pairwise consistency, including a sharp depth threshold that the numerical sequence alone cannot give. This is valuable as a classification and not merely as the evaluation of the cubic or as a new general aggregation impossibility result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
