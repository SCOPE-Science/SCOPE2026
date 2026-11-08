---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Execute `python3 verify.py` with Python 3.9 or newer (integer `bit_count` support). The verifier uses only standard-library fractions, itertools, and memoization, and constructs the entire graph from the embedded nineteen LCF offsets.

The first exact method conditions on the next eligible arrival and computes its generating polynomial and every site's inclusion probability by memoized deletion of the closed neighborhood. The second method independently enumerates all \(2^{19}\) subsets to obtain the \(139\) independent dominating sets, integrates the required arrival-order inequalities as rational functions, and sums their weights by size and site. Their equality is asserted for all nineteen sites, not just a global total.

The program additionally checks graph degrees, edges, girth exclusions, explicit automorphism generators, orbit sizes and six-cycle counts; checks the exact three rational output probabilities; verifies that probabilities sum to one; and verifies the rational mean and site-density identities. These finite calculations are exhaustive; they do not determine uncomputed dynamics or establish priority against inaccessible literature. Independent audit is not performed.
