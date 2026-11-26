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

Writing A=g^a, B=g^b makes A^k/B^t either 1 or at distance at least 1/2 from 1. The digit equation bounds its discrepancy times A^m by 2C+1, proving uniform eventual resonance, even with unbounded t,k. The remaining condition is precisely Euclidean division with quotient c_m (also for negative offsets). Positive offsets at least double; for offsets below -1 the positive integer -c_m-1 at least doubles and is bounded by C-1. Neither case can have even one edge if C<=1. For c_m=0 or -1 a period-preserving choice (k,t)=(bh,ah) works indefinitely, using respectively 0 or B^t-1 as the digit block. Periodicity gives the stated density. The phase sequence 1,2,...,2^L realizes L consecutive edges with A=B=2, including the zero-edge case. The independent-root citation is mathematically applicable: (E-A)(E^h-1) annihilates the recurrence and A is the unique simple dominant root. The inspected source is an arXiv preprint; a separate publication status is not established. Read the frozen proof, verification note and code without executing the upload. A bounded independent integer replay checked 1,152 candidates (58 admissible), 59,536 signed floor cases and sharp examples through L=12; it is not an unbounded proof.

## originality

FAIL

The earlier indexed same-base result already gives uniform unbounded resonance, the identical offset rule, the 0/-1 mechanism and the quantitative growth inequality. With coprime exponents a,b, resonance lets one group indices modulo b and treat resonant blocks as base D=A^b=B^a blocks. The claimed classification, floor law and growth upper bound then follow from the earlier result on each grouped periodic sequence. The elementary nonresonance gap estimate is the same discrete-power argument as the earlier proof. The earlier source does not state the exact power-of-two sharpness examples; the exhibited consecutive powers add an explicit extremizer, but not an independently substantial new classification. This is demonstrated overlap and implication, not a failed search or a claim that the entire statement appears verbatim.

## value

FAIL

A useful question is how long a nonterminal walk can last as the offset range grows, but the submitted answer adds only the direct iteration and an equality case of an existing doubling inequality. The unequal-base regrouping preserves the same local dynamics and provides no new mechanism. After removing covered content, an isolated restatement of that growth bound with consecutive powers as the equality example does not establish a substantial independent mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
