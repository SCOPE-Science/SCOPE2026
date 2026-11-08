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

The theorem has an unrestricted combinatorial proof in `RESULT.md`. Run `python3 verify_poset_comparisons.py` using Python 3 standard library only.

The program directly tests all linear extensions against all comparison traces, independently of the quotient criterion. It enumerates all 242 labeled posets on one through four vertices, all supports for every such poset, and all 1024 supports for each of 75 deterministically selected five-vertex posets. It also enumerates all 4231 labeled five-vertex posets to validate the sampler's domain, compares the VC maximum to the longest-chain formula for every poset of size at most four, and checks a two-component quotient-cycle obstruction.

Expected output:

`POSET_COMPARISON_SHATTER_PASS all_posets_n_le_4=242 sampled_n5=75 tested_pairs=90975 posets_n5=4231`

Finite tests are not a proof of the all-poset statement. Their role is to catch representation, quantification, and boundary-case errors. This package does not independently validate the historical novelty claim or perform an external mathematical audit.
