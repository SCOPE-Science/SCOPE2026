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

PASS

For every unequal tuple in scope, an inward force at depth a+k sees neither the hub nor another arm, and a is the least depth it sees. Once the first m−1 arms are black, their depth-k vertex forces the hub; the shallower forcers expose successively depths 1 through k−1 on the last arm, the hub forces depth k, and within-arm forces proceed outward. Every pair of depths a≤b with b−a≤k is covered by a window starting at max(1,b−k), even at an end or at length k+1. The Gram block is therefore exactly supported on the required within-arm pairs; the nonnegative threshold couplings neither cancel entries nor introduce false edges. The zero-sum window recurrence permits arbitrary first k coordinates on each arm. Choosing their sum to be zero makes the hub and all threshold-block contributions vanish, giving (m−1)k independent null vectors. For any exact-support matrix, restriction of its kernel to a forcing set is injective by the forcing-row equations. This proves equality and the rank formula. Independent replay: python3 /workspace/spider_power_check.py; BFS power, exact rational rank and forcing closure agreed at (4,4,5), k=3; (5,7,11), k=4; (9,9,9,10), k=8; all size-five initial sets were also excluded in the first case. The reproduction is bounded; the written argument handles the full quantifier. Uploaded scripts were inspected, not run.

## originality

FAIL

The October 18 indexed theorem includes every frozen nonuniform instance and gives the same minimum rank, maximum nullity, forcing number, matrix entries, and forcing chronology. The failure is established coverage of the actual claim, not a mere title match, inference from uniform symmetry, or allegation about authorship or priority.

## value

FAIL

The heterogeneous spider-power problem is intrinsically worthwhile, but this submission does not add a new regime, certificate, or interpretation to the exact more general indexed result. The restriction to unequal lengths does not create a distinct contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
